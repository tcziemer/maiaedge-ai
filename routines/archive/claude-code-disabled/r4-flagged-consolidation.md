# CRM Guardian - Routine 4: Flagged-for-Deletion Contact Consolidation (HISTORICAL Claude Code copy)

> **Status: DISABLED / NOT SCHEDULED.** R4 moved to Cowork during the 2026-04-30 platform split. (R4 itself doesn't use `web_fetch` heavily, but it was moved alongside R0/R1/R2 to keep the daily Cowork cycle together for cross-routine ledger consistency.) The live operational version is at [`cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md`](../../../cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md). This Claude Code copy carries Phase 3 operating principles for reference; if Cooper wants R4 re-enabled on Claude Code, sync this prompt to the Cowork version's content first (the Cowork copy implements the pre-Phase-1 Enterprise defensive check that the 2026-05-11 Enterprise ICP promotion added).
>
> **Phase 3 deltas (synced to Cowork canonical 2026-05-14):**
> - Canonical sub-segment vocabulary: 30 active values in `context/account-tiering/sub-segment-qualification.md`. Includes `Subsea cable operator` (new 30th, 2026-05-14), `Crypto to AI - Neoclouds` (inclusive per Cooper 2026-05-14), `Greenfield` (REAL sub-segment).
> - ICP segments (6 total as of 2026-05-11): `Data Center Colo Provider`, `Fiber Operator`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, **`Enterprise-CustomerSegment`** (promoted 2026-05-11). The ICP primary search at Step 1 considers all 6.
> - `hs_is_target_account` (renamed from `target_account` 2026-05-13) does NOT block R4 contact reassociation or flagging - those proceed regardless. The target-account override freezes `account_tier` writes only.
> - `account_tier_legacy` is ARCHIVED. NEVER write or reference it.
> - R4 does NOT touch `maiaedge_value_proposition` (R4 doesn't write enrichment fields at all - it operates on contact-level associations + `flagged_for_deletion` boolean on contacts).
> - `last_enriched_date` policy (CLAUDE.md unified table): R4 contact reassociation / flag = NO bump (company-level field; R4 writes contact-level only).
> - Tier 3 hold cross-routine canvas `F0B0AFSB9LN` is the shared ledger - read at run start.
> - Pre-Phase-1 Enterprise defensive check: flagged companies whose `account_brief` matches one of the four Enterprise sub-segment patterns AND fits the scale profile may have been flagged BEFORE Enterprise was promoted to ICP. Surface those as Tier 3 with "Pre-Phase-1 Enterprise mis-flag" reasoning rather than auto-flagging contacts.

Daily, 3:00 AM ET. You process every company with `customer_segment = "Flagged for deletion"` and resolve the fate of each associated contact: preserve + reassociate to an ICP primary where possible, else flag for deletion. You do NOT touch non-flagged companies. No Apollo calls.

**CRM scale (as of 2026-04-24):** 379 flagged companies - this is the primary cleanup backlog Cooper reviews. First-run drain could touch 1,000-2,000 contacts. Steady state (once backlog resolves) is < 20 flagged-company actions/day as Routine 3 newly flags duplicates. Each flagged company's resolution makes Cooper's bulk-delete review progressively simpler.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/pre-deletion-audit/SKILL.md` (THE authoritative source - full Steps 0-5 workflow, 6-signal preservation logic, Mode A / Mode B, open-deal hard stop)
- `skills/crm-hygiene/SKILL.md` (Mode 11 Contact Deletion Flagging for reference)

**Context:**
- `context/hubspot/contact-schema.md`
- `context/hubspot/deals-schema.md`
- `context/hubspot/poc-schema.md`
- `context/hubspot/property-schema.md`
- `context/hubspot/territory-model.md`
- `context/core/icp-playbook.md`
- `context/core/segment-qualification.md`

**Connected tools:** HubSpot MCP, Slack MCP (report delivery via `slack_send_message`). No Apollo.

## Run-Time Invariants

### A. Timezone
America/New_York. 90-day activity windows + 14-day createdate window are ET calendar days. Convert HubSpot UTC timestamps to ET before comparing.

### B. Scope
This routine operates ONLY on companies where `customer_segment = "Flagged for deletion"`. Everything else is out of scope.

### C. Customer Protection - HARD STOP
If a flagged company somehow has ANY deal where `hs_is_closed_won = true`, this is a bug upstream - do NOT proceed with contact flagging. Surface as a Tier 3 investigation item: "Flagged company has customer history; likely mis-flagged. Recommend: remove the Flagged-for-deletion segment and reclassify."

### D. Open-Deal Hard Stop
If a flagged company has ANY deal where BOTH `hs_is_closed_won = false` AND `hs_is_closed_lost = false` (i.e. the deal is still open), skip the entire company. Surface as Tier 3: "Flagged company has open deal; cannot consolidate. Recommend: resolve deal or re-evaluate flag."

**Deal-status check implementation:** HubSpot's deal pipeline uses string keys AND custom numeric IDs for stages. Do NOT check `dealstage NOT IN (closedwon, closedlost)` - numeric closed-stage IDs (e.g. `3401264867`) will be missed. Use the booleans `hs_is_closed_won` + `hs_is_closed_lost` to determine deal status deterministically.

### E. Fresh-Record Safety
Skip any company where `createdate` is within the last 14 days (ET). Too new to judge - Tier 3 hold.

### F. Error Containment
Per-contact try/except. A failure on one contact does not block the rest.

### G. Default to Tier 3 When Uncertain
Preserved contact with no ICP primary available → Tier 3 hold (do not flag, do not reassociate). Activity signal at the 90-day boundary → preserve (safe default).

### H. Idempotency
`flagged_for_deletion = true` writes are idempotent; setting true on an already-true contact is a no-op. Reassociation is idempotent once complete. Safe to re-run same-day.

### I. MaiaEdge Gotchas
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07). `customer_segment = "Enterprise-CustomerSegment"` is now ICP as of 2026-05-11 (separate segment, separate sub-segment list - see `context/segments/enterprise.md`). Anchor: Meijer.
- **ICP segments (6 as of 2026-05-11):** `Data Center Colo Provider`, `Fiber Operator`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, `Enterprise-CustomerSegment`.
- Non-ICP segments (valid reassociation targets only if Mode B qualifies): none. Mode A reassociation requires an ICP primary.

### J. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:**
- Contact `flagged_for_deletion = true` per Mode B non-preservation rules.
- Contact `flagged_for_deletion = false` if a preserved contact was previously false-flagged.
- Contact primary company reassociation per Mode A.

**Hard stops:** MaiaEdge's own record (ID 124293230301). Any write to a customer-history company. Any write that bypasses the 6-signal preservation check.

## 6-Signal Preservation Check (per contact)

A contact is **preserved** if ANY of these is true:

1. `notes_last_contacted` within the last 90 days (ET).
2. `notes_last_updated` within the last 90 days (ET).
3. Any associated deal where BOTH `hs_is_closed_won = false` AND `hs_is_closed_lost = false` (i.e. open).
4. Any associated open POC ticket (per `context/hubspot/poc-schema.md` - ticket in POC pipeline with non-terminal `hs_pipeline_stage`).
5. `lifecyclestage` in {`customer`, `opportunity`, `subscriber`}. (Note: HubSpot's contact lifecyclestage enum does not include `evangelist` - valid values are `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`. The legacy "evangelist" designation is not present in this instance.)
6. Contact `createdate` within the last 14 days (ET).

If none fire → the contact is **not preserved**.

## Workflow

For each flagged company (skip per invariants C, D, E above):

For each associated contact:

1. Run the 6-signal preservation check.
2. **If preserved:**
   - Try Mode A reassociation to an ICP primary. **Use `skills/pre-deletion-audit/SKILL.md` Step 2 as the authoritative dedup-primary search algorithm** - do not duplicate or improvise the search here. Summary of that algorithm:
     - Cascading search on the flagged company's `domain` and `name` for a potential ICP primary.
     - ICP primary = a company where `customer_segment IN ('Data Center Colo Provider', 'Fiber Operator', 'Network Operator(Tier 1 / VNO)', 'MSP/Aggregator', 'NeoCloud', 'Enterprise-CustomerSegment')` AND `customer_segment != 'Flagged for deletion'`. `Enterprise-CustomerSegment` was promoted to ICP 2026-05-11 - Meijer-class multi-DC enterprises with 4 sub-segments per `context/segments/enterprise.md`.
     - HIGH-confidence match: exact domain match (after normalization: strip `www.`, lowercase, trim trailing `/`) OR exact normalized-name match.
     - MEDIUM-confidence match: Levenshtein similarity ≥ 0.9 on normalized name with same country/state → Tier 3 only (surface, do not auto-reassociate).
     - Tiebreaker if multiple HIGH candidates: pick the one with the most recent `notes_last_contacted`.
   - If a unique HIGH-confidence ICP primary match found: reassociate contacts in batch via `manage_crm_objects.updateRequest` with `associations` field.
     - Tier 1 if flagged source has zero open deals (which is always true here - invariant D already skipped any flagged company with open deals).
     - After reassociation: sync contact's `customer_segment` and `hubspot_owner_id` from the new primary (Tier 1).
     - The reassociation action itself is Tier 2 (surfaced for Cooper's visibility even when writes succeed).
   - If no ICP primary match OR only MEDIUM-confidence fuzzy match: Tier 3 hold. Log "preserved contact, no reassociation target" for Cooper with the preserved contact's last-activity signal.

**Implementation note - "reassociate" semantics:** The HubSpot MCP `manage_crm_objects` tool only supports ADDING associations on update; there is no documented path to REMOVE an existing association through it. So in practice, "reassociate contact from flagged company to ICP primary" means: add a new association from the contact to the primary company. The contact's old association to the flagged company persists in the interim. This is acceptable because (a) the flagged company is on its way to archival via Cooper's bulk-delete review, and (b) HubSpot archive cleans up stale associations as a side effect of the company archive. Until that archival, contacts will appear under BOTH the flagged company and the new primary in HubSpot UI views. To make the primary the contact's "primary company" (the one shown in the contact card header), pass `labels: ["Contact with Primary Company"]` in the new association - but only if that label exists in this HubSpot instance (verify before relying on it).
3. **If not preserved:** set `flagged_for_deletion = true` on the contact (Tier 1). This is the Mode B standalone flag path.
4. If a contact has `flagged_for_deletion = true` but IS now preserved (e.g., activity in the last 90 days): clear to `false` (Tier 1 correction).

**Protection filters - never flag a contact even if not-preserved:**
- `hs_email_optout = true` (CAN-SPAM / GDPR suppression list - must retain)
- `lifecyclestage` in {`customer`, `opportunity`}
- Any open-deal association (deal where `hs_is_closed_won = false` AND `hs_is_closed_lost = false`)
- Any open POC ticket association

(These overlap with preservation signals but are listed explicitly as a belt-and-braces check. Overlap is intentional - the cost of double-checking a protection filter is zero; the cost of false-flagging an opted-out contact is a CAN-SPAM violation.)

## Caps & Budgets

- **Company cap (first-run drain):** 150 flagged companies per run. First-run backlog is ~379 flagged companies; this drains in ~3 runs. Steady state is typically < 20/day once Cooper bulk-deletes and the pipeline normalizes.
- **Contacts per run:** soft cap 1,500 contact evaluations per run (average ~4 contacts per flagged company at upper bound).
- **HubSpot writes:**
  - Contact reassociations + segment/owner sync: batch via `manage_crm_objects.updateRequest` with `objects` array. **Batch cap: 10 per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches.
  - Contact `flagged_for_deletion = true` writes: same batch cap - 10 per call. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s.
  - Soft cap 2,000 writes/run total during first-run drain; 200/run steady state.
  - Exponential backoff (1s → 2s → 4s) on 429; split oversized batches on repeated 429s.
- **Session pacing:** 100 records/page, ≥1s between pages for HubSpot reads. Preload each company's contact+deal+ticket associations in a single per-company call (use `get_associations` via `search_crm_objects` with `associatedWith` filter) to avoid round-trips.

## Output

- **Subject:** `CRM Guardian - Flagged Consolidation - [YYYY-MM-DD] - [N] contacts flagged, [M] reassociated, [K] Tier 3 held`
- **Hero:** flagged companies processed, contacts evaluated, Tier 1 flags applied, Tier 1/2 reassociations, Tier 3 holds, companies fully resolved (all contacts drained or flagged).
- **Reassociations (Mode A):** source flagged company ID → ICP primary ID → contact IDs.
- **Contact flags (Mode B):** contact IDs, reason (none of 6 signals fired).
- **Tier 3 held:**
  - Preserved contacts with no ICP primary available.
  - Companies skipped for customer history (mis-flag investigation).
  - Companies skipped for open deals.
  - Companies skipped for 14-day freshness.
- **Errors / API failures.**
- **Bulk-delete pointer:** "Filter contacts by `flagged_for_deletion = true` in HubSpot UI to review and bulk-delete."

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian - Routine 4: Flagged Consolidation | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue - do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper. **This is the most important routine email for Cooper's daily review - make the "Contacts Flagged for Deletion" count and bulk-delete pointer prominent in the hero section.**

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:wastebasket: *CRM Guardian - Flagged Consolidation* - [YYYY-MM-DD] - [N] contacts flagged, [M] reassociated, [K] Tier 3 held`
- **Body format:** Slack mrkdwn. Reassociation + flag tables in triple-backtick code blocks. End the parent message with the bulk-delete pointer: `> Filter contacts by \`flagged_for_deletion = true\` in HubSpot UI to review and bulk-delete.`
- **Thread prefix:** `CRM Guardian - Flagged Consolidation -` for Slack search grouping.
- **Character limit:** 5,000 per text element. First-run reports (with ~379-company backlog) WILL exceed this - split into hero + threaded replies (one thread per table: Reassociations / Mode B Flags / Tier 3 Held) using `thread_ts` from the hero message.
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback.
