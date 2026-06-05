# CRM Guardian — Routine 5: Contact Duplicate Flagging (Weekly)

Weekly, Sunday 1:00 AM ET. You scan the full contact table for duplicates and flag the losers for deletion (`flagged_for_deletion = true`). Exact-email duplicates are the only thing you act on; name-based duplicates are Tier 3 only. No Apollo calls.

**CRM scale (as of 2026-04-24):** 13,309 contacts total. Full paginated scan = ~133 pages at 1s/page = ~2-3 min of reads. Dedup detection is O(n) via email-normalization dictionary. Current contacts already flagged for deletion: 13 — weekly churn is expected to be small.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/crm-hygiene/SKILL.md` (Mode 11 Contact Deletion Flagging — canonical criteria and protection filters)
- `skills/pre-deletion-audit/SKILL.md` (preservation signal logic for context)

**Context:**
- `context/hubspot/contact-schema.md`
- `context/hubspot/deals-schema.md`
- `context/hubspot/poc-schema.md`

**Connected tools:** HubSpot MCP, Slack MCP (report delivery via `slack_send_message`). No Apollo.

## Run-Time Invariants

### A. Timezone
America/New_York for all date math.

### B. Error Containment
Per-contact try/except.

### C. Default to Tier 3 When Uncertain
Name-based matches without email or company agreement → Tier 3 only.

### D. Idempotency
`flagged_for_deletion = true` is idempotent. A second same-week run finds the losers already flagged and returns "All clean."

### E. Cadence Justification
Contact dedup churn is low — weekly keeps the scan tractable (full-table scan is expensive) without letting duplicates accumulate long enough to affect outreach attribution.

### F. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:** Contact `flagged_for_deletion = true` on HIGH-confidence duplicate losers, per the protection filters below. Contact `flagged_for_deletion = false` on a flagged contact that no longer qualifies (false positive from a prior run).

**Hard stops:** Never flag a contact belonging to MaiaEdge's own record (ID 124293230301). Never delete or archive — only set the flag field.

## Detection Logic

**HIGH confidence (act on):**
- Exact email match (case-insensitive, trimmed). Keep the contact with the most recent `lastmodifieddate`; flag the rest.
- Tiebreaker if `lastmodifieddate` equals: keep the contact with more associated deals; then more activity timestamps (`notes_last_contacted` recency); then lower HubSpot contact ID.

**MEDIUM confidence (Tier 3 only — do not act):**
- Same `firstname + lastname + associated_company_id` triple with different (or missing) emails.
- Same email local-part + company domain but different full emails (e.g., `jane@acme.com` vs `jane.smith@acme.com` at the same company) — surface as possible reassignment/rename, not a merge.

**Not a duplicate:**
- Empty or obviously generic emails (`info@`, `hello@`, `noreply@`) — skip the pair; these are handled by Routine 6 / crm-hygiene Mode 11, not here.

## Protection Filters (never flag)

A contact is ineligible for `flagged_for_deletion = true` from this routine if ANY of these is true. This mirrors the 6-signal preservation check used by Routine 4 — once a contact has any active relationship signal, the dedup routine doesn't touch it; humans handle the merge instead.

1. `hs_email_optout = true` (CAN-SPAM / GDPR suppression list — must retain)
2. `lifecyclestage` in {`customer`, `opportunity`} (HubSpot's contact lifecyclestage enum does NOT include `evangelist` — valid values are `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`)
3. Any open-deal association — use boolean `hs_is_closed_won = false` AND `hs_is_closed_lost = false` to identify open deals. Do NOT filter on `dealstage NOT IN (closedwon, closedlost)` — HubSpot's pipeline uses BOTH string keys and custom numeric stage IDs, and numeric closed stages would be missed.
4. Any open POC ticket association
5. **`notes_last_contacted` within the last 90 days (ET).** A contact actively touched by a rep in the last quarter is in an active relationship — never flag, even if it's a duplicate-by-email. The activity history sits on this record; flagging it as a loser would orphan the engagement record from the rep's view.
6. **`notes_last_updated` within the last 90 days (ET).** Catches activity surfaces that don't go through `notes_last_contacted` (e.g., logged tasks, internal notes, manual property edits by a rep, meeting follow-ups). Belt-and-suspenders with #5.
7. **Contact `createdate` within the last 14 days (ET).** Fresh records can't reasonably have 90-day activity history yet — let them age before any dedup decision. The next weekly scan picks them up once they age past 14 days.

**Tie-break logic with the expanded filter set:** if the intended loser (per the keeper-selection precedence in the Detection Logic section above) hits any of filters 1-7, attempt to promote the OTHER candidate to loser. The OTHER must also pass all 7 filters to be flag-eligible. If both candidates are protected, skip the pair entirely and surface as Tier 3 ("two protected duplicates; manual merge recommended") — Cooper or the rep merges in HubSpot UI, picking which record's history wins.

**Why this matters:** the keeper-selection rule uses `lastmodifieddate`, which updates on ANY field change including programmatic syncs. Without filters 5-7, a contact with stale `lastmodifieddate` but recent rep activity could lose to a freshly-synced-but-untouched-by-rep duplicate. The activity filters guard against this — rep-engaged contacts are never silently demoted regardless of who has the newer modification timestamp.

## Workflow

1. Paginate full contacts table. Group by normalized email (lowercased, trimmed). Skip groups of size 1.
2. For each group of size ≥ 2:
   - Apply HIGH-confidence precedence to pick the **keeper**.
   - All non-keepers → evaluate protection filters.
   - Unprotected losers → set `flagged_for_deletion = true` (Tier 1).
   - Protected losers → Tier 3 (surface with reason: "protected by customer lifecyclestage" / "open deal" / etc.).
3. MEDIUM-confidence name+company matches → add to Tier 3 "Possible name duplicates — review" list. Do not act.
4. Sweep: any contact currently `flagged_for_deletion = true` that no longer qualifies as a duplicate loser (e.g., the keeper was deleted, leaving this one as the only remaining) → clear to `false` (Tier 1 correction).

## Caps & Budgets

- **Record cap:** up to 2,000 HIGH-confidence flags per run. At current contact scale (13,309) this cap is well above expected weekly churn — the first run may hit it if historical duplicates have accumulated, but steady state is dozens per week.
- **HubSpot writes:** use `manage_crm_objects.updateRequest` in batch mode (each `object`: `objectType=contacts, objectId, properties={flagged_for_deletion: "true"}`). **Batch cap: 10 `objects` per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s.
- **Pagination rhythm:** 100 contacts per page, ≥1 second between pages, to respect the 100/10s burst limit. Full scan of 13,309 contacts = ~133 pages ≈ 2.5 minutes.
- **Memory:** email-normalization dictionary for 13,309 contacts is negligible (< 5 MB).

## Output

- **Subject:** `CRM Guardian — Contact Dedup (Weekly) — [YYYY-MM-DD] — [N] flagged, [M] Tier 3 held`
- **Hero:** contacts scanned, duplicate groups found, Tier 1 flags applied, Tier 3 holds, protected-loser skips.
- **Flag summary (Tier 1):** counts by reason (exact-email duplicate keeper selected).
- **Tier 3 held:**
  - Two-protected-loser pairs (recommend manual merge).
  - MEDIUM-confidence name+company matches.
  - Other boundary cases.
- **Cleared flags:** contacts whose `flagged_for_deletion` dropped back to false this week.
- **Errors / API failures.**
- **Bulk-delete pointer:** "Filter contacts by `flagged_for_deletion = true` in HubSpot UI to review and bulk-delete."

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 5: Contact Dedup | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:mag: *CRM Guardian — Contact Dedup (Weekly)* — [YYYY-MM-DD] — [N] flagged, [M] Tier 3 held`
- **Body format:** Slack mrkdwn. Duplicate-group summary in triple-backtick code blocks. End the parent message with the bulk-delete pointer: `> Filter contacts by \`flagged_for_deletion = true\` in HubSpot UI to review and bulk-delete.`
- **Thread prefix:** `CRM Guardian — Contact Dedup (Weekly) —` — distinct from daily routines so weekly runs group separately in Slack search.
- **Character limit:** 5,000 per text element; thread overflow via `thread_ts`.
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback.
