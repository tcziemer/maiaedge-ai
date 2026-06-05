# CRM Guardian — Routine 3: Duplicate Account Audit + Contact Reassociation

Daily, 2:00 AM ET. You scan the full company table for duplicates, pick a primary, reassociate contacts to the primary, and flag the duplicate for deletion. Customer-history companies and primaries themselves are never flagged. No Apollo calls.

**CRM scale (as of 2026-04-24):** 3,489 companies total. Full paginated scan = ~35 pages at 1s/page = ~35 seconds of HubSpot reads. Duplicate detection is O(n) via domain-grouping and name-normalization dictionaries — NOT pairwise comparison.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/pre-deletion-audit/SKILL.md` (duplicate detection methodology, Mode A consolidation, contact preservation signals)
- `skills/crm-hygiene/SKILL.md` (Mode 2 Duplicate Detection)

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/territory-model.md`
- `context/hubspot/deals-schema.md`

**Connected tools:** HubSpot MCP, Slack MCP (report delivery via `slack_send_message`). No Apollo.

## Run-Time Invariants

### A. Timezone
America/New_York for all date math.

### B. Skip Already-Flagged
Companies with `customer_segment = "Flagged for deletion"` are not considered for flagging again, but they are still checked as a potential primary's duplicate (a fresh good record should not be merged into an already-flagged bad record — flagged records are never elected primary).

### C. Customer Protection — HARD STOP
Any company with ANY associated deal where `hs_is_closed_won = true` is NEVER flagged, even if it looks like a duplicate. If the proposed duplicate is a customer and the proposed primary is not, escalate to Tier 3 — human decides.

**Implementation note:** HubSpot's deal pipeline uses BOTH string keys (`closedwon`, `closedlost`) AND custom numeric IDs (e.g. `3401264867` = "Closed Won" in the custom MaiaEdge Deals pipeline). Do NOT filter solely on `dealstage IN ('closedwon', 'closedlost')` — numeric-ID closed stages would be missed. Always use the boolean `hs_is_closed_won = true` OR `hs_is_closed_lost = true` flags to identify closed deals deterministically. Any deal where BOTH booleans are false is "open."

### D. Error Containment
Per-pair try/except. Continue on failure.

### E. Default to Tier 3 When Uncertain
MEDIUM-confidence matches (fuzzy name match without domain match) are Tier 3 only — surface as merge suggestion, do not act.

### F. Idempotency
Write `customer_segment = "Flagged for deletion"` only AFTER contacts have been reassociated. Idempotent: a second same-day run sees drained, flagged duplicates and returns "All clean."

### G. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes on duplicate records:** `customer_segment = "Flagged for deletion"` (this is the one exception for this routine — gated by the Mode A workflow completing successfully and Customer Protection not firing).

**Pre-authorized writes on contacts:** `primary_company_id` / association reassociation.

**Hard stops:** MaiaEdge's own record (ID 124293230301). Never merge companies (HubSpot's native merge is out of scope — this routine only reassociates contacts and flags the loser).

## Detection Logic

**Algorithm (O(n), not O(n²)):**
1. Paginate all active companies (100 per page). For each, capture: `id`, `name`, `domain`, `customer_segment`, `last_enriched_date`, `num_associated_contacts`, `num_associated_deals`.
2. Build `domain_index`: dict keyed by normalized domain → list of company IDs sharing that domain.
3. Build `name_index`: dict keyed by normalized name → list of company IDs sharing that name.
4. A group is a candidate duplicate set when `len(domain_index[key]) >= 2` OR `len(name_index[key]) >= 2`.
5. Pair generation only within groups — avoids the pairwise-comparison blowup.

**HIGH confidence (act on):**
- **Exact domain match:** normalize with `lower(strip('http://', 'https://', 'www.', trailing '/'))`. Example: `Acme.com` matches `https://www.acme.com/`.
- **Normalized-name match:** normalize with `lower(strip suffix {Inc, Inc., LLC, L.L.C., Corp, Corp., Ltd, Ltd., GmbH, SA, BV, Co, Co., Group, Holdings, The (prefix)}; collapse whitespace; strip trailing punctuation)`. Example: "Acme Corp." = "ACME CORP" = "Acme, Inc." after normalization.

**MEDIUM confidence (Tier 3 only):**
- Fuzzy name match with Levenshtein distance ≤ 2 on the normalized name AND no domain match.
- Companies sharing an exact phone number or address but differing on name + domain.

**Not a duplicate:**
- Same parent brand with different regional domains (e.g., `acme.com` vs `acme.de`) — surface as Tier 3 note only.

## Primary Selection (HIGH confidence only)

Pick the primary with this deterministic precedence:

1. Most associated contacts (descending).
2. Most associated deals (descending).
3. Most recent `last_enriched_date` (descending; EMPTY treated as oldest).
4. Lower HubSpot company ID (ascending) — final tiebreak.

**Primary must NOT be** `customer_segment = "Flagged for deletion"`. If both candidates are flagged, skip the pair (human decides).

## Workflow (HIGH confidence pairs only)

For each pair:

1. Customer Protection check: if duplicate is a customer (any closed-won deal), escalate the pair to Tier 3 and skip.
2. Select primary per the precedence above.
3. Reassociate all contacts from duplicate → primary. Per-contact tier:
   - Tier 1 if duplicate has zero open deals.
   - Tier 2 if duplicate has any open deal (still reassociate contacts, but flag for Cooper because deal-protected account is being drained).
4. After ALL contacts reassociated successfully: set `customer_segment = "Flagged for deletion"` on the duplicate (Tier 1).
5. If any contact reassociation fails (e.g., the primary is the contact's existing association), log per-contact and do NOT flag the company yet — surface in Errors for follow-up.

**Implementation note — "reassociate" semantics:** The HubSpot MCP `manage_crm_objects` tool only supports ADDING associations on update; there is no documented path to REMOVE an existing association through it. So in practice, "reassociate contact from duplicate to primary" means: add a new association from the contact to the primary company. The contact's old association to the duplicate company persists in the interim. This is acceptable because (a) the duplicate company is flagged for deletion in step 4 and (b) Cooper's eventual bulk-archival of flagged companies cleans up the stale associations as a side effect of the company archive. Until that archival, contacts will appear under BOTH the duplicate (flagged) and the primary in HubSpot UI views — this is expected interim state, not a bug. If you want the primary to be the contact's "primary company" in HubSpot's sense (the one that shows in the contact card header), pass `labels: ["Contact with Primary Company"]` in the new association — but only if that label exists in this HubSpot instance (verify before relying on it).

**MEDIUM-confidence pairs:** do nothing automated. Add each to the Tier 3 "Possible duplicates — review" section with both company IDs, match signal, and recommended primary per the precedence (but do NOT act).

## Caps & Budgets

- **Pair cap:** 50 HIGH-confidence pairs acted on per run. If more exist, process by descending match confidence (domain-match first, normalized-name match second), remainder rolls to tomorrow. At current CRM size (3,489 companies) expected daily volume is single-digit pairs in steady state.
- **Tier 3 listing:** no cap on what is surfaced for review (report only).
- **HubSpot writes:**
  - Contact reassociations: use `manage_crm_objects.updateRequest` with `associations` field. **Batch cap: 10 contacts per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches.
  - Duplicate-flag company writes: same batch cap — 10 companies per call. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s.
  - Soft cap 500 writes/run total (contact reassociations dominate).
  - Exponential backoff (1s → 2s → 4s) on 429.
- **Session pacing:** full-table read uses 100 records/page with ≥1s between pages (~35 pages at current scale).

## Output

Structured report:

- **Subject:** `CRM Guardian — Duplicate Accounts — [YYYY-MM-DD] — [N] pairs consolidated, [M] Tier 3 held`
- **Hero:** pairs scanned, HIGH-confidence pairs acted on, contacts reassociated, duplicates flagged, Tier 3 count.
- **Consolidations (Tier 1/2):** table of duplicate ID → primary ID, match signal, contacts reassociated, duplicate now flagged.
- **Tier 3 held:**
  - Customer-history dupes (hard stop).
  - MEDIUM-confidence fuzzy matches for review.
  - Pairs where both were already flagged.
  - Pairs blocked by contact-reassociation errors.
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 3: Duplicate Accounts | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:busts_in_silhouette: *CRM Guardian — Duplicate Accounts* — [YYYY-MM-DD] — [N] pairs consolidated, [M] Tier 3 held`
- **Body format:** Slack mrkdwn. Consolidation tables go in triple-backtick code blocks (duplicate_id → primary_id → contacts_reassociated). Prefix every run `CRM Guardian — Duplicate Accounts —` for Slack search grouping.
- **Character limit:** 5,000 per text element; thread overflow via `thread_ts`.
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback.
