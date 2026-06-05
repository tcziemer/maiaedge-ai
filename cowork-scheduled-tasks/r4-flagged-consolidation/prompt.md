# CRM Guardian - Flagged Consolidation (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget; HubSpot is the source of truth for the flagged-for-deletion pool. Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Daily, 12:00 PM CT, Monday-Friday. Cron: `0 12 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**

Runs FOURTH in the daily Cowork cycle (after Import Validator + Fresh Enrichment + Stale Re-Enrichment). Processes every company with `customer_segment = "Flagged for deletion"` and resolves the fate of each associated contact: preserve + reassociate to an ICP primary where possible, else flag for deletion. Does NOT touch non-flagged companies. No Apollo calls.

**This run produces the most important section of Cooper's daily review** - its output drives the manual bulk-delete review (Cooper's only required CRM action). That output now lands in the on-disk run report + the CRM Ops Daily Digest (which renders the bulk-delete pointer), not a per-run DM.

**CRM scale baseline:** 379 flagged companies - primary cleanup backlog. First-run drain could touch 1,000-2,000 contacts. Steady state (once backlog resolves): <20 flagged-company actions/day as Routine 3 newly flags duplicates.

---

## Connected Tools (Cowork)

- **HubSpot MCP** - read companies/contacts/deals/tickets; write `flagged_for_deletion`, `customer_segment` (Tier 1 segment-sync), contact reassociations
- **Slack MCP** - `slack_send_message` to Cooper (hard-failure ping ONLY), `slack_read_canvas` + `slack_update_canvas`
- **No Apollo, no web_search, no web_fetch.** This routine is purely HubSpot-internal.

---

## Delivery - quiet on success, ping only on hard failure

Do NOT DM Cooper a per-run debrief. On a clean or partial-but-recoverable run (including zero-flagged-company "backlog drained" runs and partial runs where the company cap was reached), the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r4-flagged-consolidation/...` (the report body structured in the Output section below becomes the on-disk report, NOT a DM - including the bulk-delete pointer), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work - including the contacts-flagged count and the bulk-delete / archive pointer - from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack MCP unreachable, an abort, or zero records processed against a non-empty flagged-company queue - as ONE line:

`:red_circle: CRM Guardian - Flagged Consolidation [FAILED/ABORTED] - [one-clause reason].`

Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk report + Run-log row are the fallback. (Historical note: R4 once went silent for 2+ days after April 28. A drained backlog is a SUCCESS state - it gets recorded in the disk report + Run-log row + digest, not skipped.)

---

## Reference Files (read at run start)

- `skills/crm-guardian/SKILL.md` (safety tiers + Cross-Routine Ledger)
- `skills/pre-deletion-audit/SKILL.md` (THE authoritative source - full Steps 0-5 workflow, 6-signal preservation logic, Mode A / Mode B, open-deal hard stop, dedup-primary search algorithm)
- `skills/crm-hygiene/SKILL.md` (Mode 11 Contact Deletion Flagging for reference)
- `context/hubspot/contact-schema.md`
- `context/hubspot/deals-schema.md`
- `context/hubspot/poc-schema.md`
- `context/hubspot/property-schema.md`
- `context/hubspot/territory-model.md`
- `context/core/icp-playbook.md`
- `context/core/segment-qualification.md`

---

## Run-Time Invariants

### A. Timezone
America/New_York. 90-day activity windows + 14-day createdate window are ET calendar days. Convert HubSpot UTC timestamps to ET before comparing.

### B. Scope
Operates ONLY on companies where `customer_segment = "Flagged for deletion"`. Everything else out of scope.

### C. Customer Protection - HARD STOP
If a flagged company has ANY deal where `hs_is_closed_won = true`, this is a bug upstream - do NOT proceed with contact flagging. Surface as Tier 3: "Flagged company has customer history; likely mis-flagged. Recommend: remove the Flagged-for-deletion segment and reclassify."

### C-bis. Pre-Phase-1 Enterprise Defensive Check (added 2026-05-11)
Enterprise was promoted to ICP on 2026-05-11. Some flagged-for-deletion records may have been flagged BEFORE that date under the old non-ICP framing. To prevent auto-deletion of accounts that are now in-ICP under the new framing:

- If a flagged company has `account_brief` containing keywords matching the four Enterprise sub-segments (`bank`, `insurer`, `payment network`, `hospital`, `health system`, `retailer`, `distribution center`, `BPO`, `delivery center`, `operations`, `outsourcing`) AND fits the scale profile ($1B+ rev signal in any field, multi-DC mention, etc.), do NOT proceed with contact flagging.
- Surface as Tier 3: "Pre-Phase-1 Enterprise mis-flag - flagged before 2026-05-11 ICP promotion. Recommend: remove Flagged-for-deletion segment, route to R1/R2 for Enterprise scale-gate re-evaluation."
- Cooper validates in HubSpot UI before any further action.

This is a one-time backfill check during the Enterprise promotion transition. After 30 days of clean R4 runs (no Tier 3 Enterprise mis-flags surfaced), this check can become best-effort rather than mandatory.

### D. Open-Deal Hard Stop
If a flagged company has ANY deal where BOTH `hs_is_closed_won = false` AND `hs_is_closed_lost = false` (deal still open), skip the entire company. Surface as Tier 3: "Flagged company has open deal; cannot consolidate. Recommend: resolve deal or re-evaluate flag."

**Implementation:** HubSpot's deal pipeline uses string keys AND custom numeric IDs for stages. Do NOT check `dealstage NOT IN (closedwon, closedlost)` - numeric closed-stage IDs (e.g. `3401264867`) will be missed. Use the booleans `hs_is_closed_won` + `hs_is_closed_lost`.

### E. Fresh-Record Safety
Skip any company where `createdate` is within the last 14 days (ET). Too new to judge - Tier 3 hold.

### F. Default to Tier 3 When Uncertain
Preserved contact with no ICP primary available → Tier 3 hold (do not flag, do not reassociate). Activity signal at the 90-day boundary → preserve (safe default).

### G. Idempotency
`flagged_for_deletion = true` writes are idempotent. Reassociation is idempotent once complete. Safe to re-run same-day.

### H. MaiaEdge Gotchas
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07).
- `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") was promoted to ICP on 2026-05-11. Four sub-segments only: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Anchor: Meijer.
- **ICP segments (6 total as of 2026-05-11):** `Data Center Colo Provider`, `Fiber Operator`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, **`Enterprise-CustomerSegment`**.
- **Defensive Enterprise check (added 2026-05-11):** If R3 (Duplicate Audit) or any upstream routine flagged a company as duplicate-of-X where X has `customer_segment = "Enterprise-CustomerSegment"`, treat the Enterprise primary as ICP for Mode A consolidation. Do NOT reassociate Enterprise contacts to a non-Enterprise primary or vice versa unless the duplicate-pair is unambiguous (same domain or same normalized name).

### I. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:**
- Contact `flagged_for_deletion = true` per Mode B non-preservation rules.
- Contact `flagged_for_deletion = false` if a preserved contact was previously false-flagged.
- Contact primary company reassociation per Mode A.
- Tier 1 segment/owner sync on reassociated contact (mirror primary).

**Hard stops:** MaiaEdge own (124293230301). Any write to a customer-history company. Any write that bypasses the 6-signal preservation check.

---

## 6-Signal Preservation Check (per contact)

A contact is **preserved** if ANY of these is true:

1. `notes_last_contacted` within the last 90 days (ET).
2. `notes_last_updated` within the last 90 days (ET).
3. Any associated deal where BOTH `hs_is_closed_won = false` AND `hs_is_closed_lost = false` (i.e. open).
4. Any associated open POC ticket (per `context/hubspot/poc-schema.md` - ticket in POC pipeline with non-terminal `hs_pipeline_stage`).
5. `lifecyclestage` in {`customer`, `opportunity`, `subscriber`}. (HubSpot's contact lifecyclestage enum: `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`.)
6. Contact `createdate` within the last 14 days (ET).

If none fire → contact is **not preserved** (eligible for Mode B flag, subject to protection filters).

---

## Workflow

For each flagged company (skip per invariants C, D, E):

For each associated contact:

### 1. Run the 6-signal preservation check.

### 2. If preserved:

#### Try Mode A reassociation to an ICP primary

Use `skills/pre-deletion-audit/SKILL.md` Step 2 as the authoritative dedup-primary search algorithm. Summary:

- Cascading search on the flagged company's `domain` and `name` for a potential ICP primary.
- **ICP primary** = a company where `customer_segment IN ('Data Center Colo Provider', 'Fiber Operator', 'Network Operator(Tier 1 / VNO)', 'MSP/Aggregator', 'NeoCloud', 'Enterprise-CustomerSegment')` AND `customer_segment != 'Flagged for deletion'`. (`Enterprise-CustomerSegment` added 2026-05-11 with the Enterprise ICP promotion - Meijer-class multi-DC enterprises.)
- **HIGH-confidence match:** exact domain match (after normalization: strip `www.`, lowercase, trim trailing `/`) OR exact normalized-name match.
- **MEDIUM-confidence match:** Levenshtein similarity ≥ 0.9 on normalized name with same country/state → **Tier 3 only** (surface, do not auto-reassociate).
- **Tiebreaker** if multiple HIGH candidates: pick the one with the most recent `notes_last_contacted`.

If a unique HIGH-confidence ICP primary match found:

- Reassociate contacts in batch via `manage_crm_objects.updateRequest` with `associations` field.
- Tier 1 if flagged source has zero open deals (always true here - invariant D already filtered).
- After reassociation: sync contact's `customer_segment` and `hubspot_owner_id` from the new primary (Tier 1).
- The reassociation action itself is Tier 2 (surfaced for Cooper visibility even when writes succeed).

If no ICP primary match OR only MEDIUM-confidence fuzzy match: **Tier 3 hold.** Log "preserved contact, no reassociation target" with the preserved contact's last-activity signal.

#### Implementation note - "reassociate" semantics

The HubSpot MCP `manage_crm_objects` tool only supports ADDING associations on update; there is no documented path to REMOVE an existing association through it. So in practice, "reassociate contact from flagged company to ICP primary" means: add a new association from the contact to the primary company. The contact's old association to the flagged company persists in the interim. This is acceptable because (a) the flagged company is on its way to archival via Cooper's bulk-delete review, and (b) HubSpot archive cleans up stale associations as a side effect of the company archive. Until that archival, contacts will appear under BOTH the flagged company and the new primary in HubSpot UI views.

To make the primary the contact's "primary company" (the one shown in the contact card header), pass `labels: ["Contact with Primary Company"]` in the new association - but only if that label exists in this HubSpot instance (verify before relying on it).

### 3. If not preserved:

Set `flagged_for_deletion = true` on the contact (Tier 1). This is the Mode B standalone flag path.

### 4. If a contact has `flagged_for_deletion = true` but IS now preserved (e.g., activity in the last 90 days):

Clear to `false` (Tier 1 correction).

### Protection filters - never flag a contact even if not-preserved:

- `hs_email_optout = true` (CAN-SPAM / GDPR suppression list - must retain)
- `lifecyclestage` in {`customer`, `opportunity`}
- Any open-deal association (deal where `hs_is_closed_won = false` AND `hs_is_closed_lost = false`)
- Any open POC ticket association

(Overlap with preservation signals is intentional belt-and-braces. Cost of double-checking a protection filter is zero; cost of false-flagging an opted-out contact is a CAN-SPAM violation.)

---

## Caps & Budgets

- **Company cap (first-run drain):** 150 flagged companies per run. First-run backlog ~379; drains in ~3 runs. Steady state typically <20/day.
- **Contacts per run:** soft cap 1,500 contact evaluations.
- **HubSpot writes:**
  - Contact reassociations + segment/owner sync: **batch cap 10 per `manage_crm_objects` call.** Loop 10/batch with ≥250ms between batches.
  - Contact `flagged_for_deletion = true` writes: same batch cap 10/call.
  - Soft cap 2,000 writes/run total during first-run drain; 200/run steady state.
  - Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s.
- **Session pacing:** 100 records/page, ≥1s between pages. Preload each company's contact + deal + ticket associations in a single per-company call (use `get_associations` via `search_crm_objects` with `associatedWith` filter).

---

## On-disk run report (structure)

Write this report to `weekly-reports/YYYY-MM-DD/r4-flagged-consolidation/run-report.md`. This is the durable record the CRM Ops Daily Digest reads from - it is NOT sent as a DM. Make the contacts-flagged count and bulk-delete pointer prominent; the digest renders them for Cooper.

**Header:**
```
CRM Guardian - Flagged Consolidation - [YYYY-MM-DD] - [N] contacts flagged, [M] reassociated, [K] Tier 3 held
```

**Body:**
```
Run summary: [F] flagged companies processed · [E] contacts evaluated · [Tier 1 flags / Tier 1-2 reassociations / Tier 3 holds counts] · [R] companies fully resolved

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts → flagged_for_deletion = true → review and bulk-delete
> [Then] Filter HubSpot Companies → customer_segment = "Flagged for deletion" → archive (this severs the stale associations from reassociated contacts)

[If Tier 3 > 0]
- [K] Tier 3 holds in the tables below (preserved contacts with no ICP primary; mis-flag investigations; open-deal blocks)

Run health: [GREEN / YELLOW / RED]
- GREEN: 0 errors, 0 mis-flag investigations, all writes succeeded
- YELLOW: writes succeeded but Tier 3 holds present OR mis-flag investigation flagged
- RED: ≥1 fatal error or aborted partway

Errors: [None | description]
```

**Detail tables (append to the report):** Reassociation table (source company → ICP primary → contact IDs) / Mode B flag table (contact IDs + reason) / Tier 3 held detail.

**Backlog-drained run:** report `0 flagged companies - backlog drained. Steady state. Run health: GREEN.` + the ✅ Run-log row. No DM.

**Hard failure (abort / MCP unreachable / zero processed against a non-empty queue):** write the report with `Run health: RED` (`RUN ABORTED at Step [X]. [error]. Companies processed: [F]. Contacts processed: [E].`), write the ❌ Run-log row, AND send the one-line failure ping per the Delivery rule near the top of this prompt.

---

## Cross-routine ledger

- **At run start:** read canvas `F0B0AFSB9LN`. Drain Routine 4 items - re-evaluate; resolve and remove if Cooper acted manually.
- **At run end:** append NEW Tier 3 holds with `[YYYY-MM-DD]`. Append ONE row to "Run log":
  `| YYYY-MM-DD | CRM Guardian - Flagged Consolidation | <status emoji> | <summary> | <links> |`
  Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped.

---

## Delivery

See the "Delivery - quiet on success, ping only on hard failure" rule near the top of this prompt. Summary:

- **Success / partial-recoverable runs:** NO DM. Write the on-disk run report (structure in the "On-disk run report" section) - including the bulk-delete pointer in a `>` callout and all detail tables (Reassociations / Mode B Flags / Tier 3 Held) inline - then append the Run-log row to canvas `F0B0AFSB9LN`. First-run reports (with the ~379-company backlog) are large; the on-disk report has no character limit, so write the full tables. The CRM Ops Daily Digest renders the bulk-delete pointer for Cooper.
- **Hard failure only** (HubSpot/Slack MCP unreachable, abort, or zero processed against a non-empty queue): one-line `:red_circle:` ping to `slack_send_message` channel_id `U0A24D9RJLS`. Retry the ping once (1s → 2s); if it still fails, the disk report + ❌ Run-log row are the fallback.
- **Body format:** Slack mrkdwn for the failure ping; the on-disk report uses plain markdown with tables in triple-backtick code blocks.

---

## Cross-routine coordination

- **Runs AFTER Routine 2 (11:00 AM CT Stale Re-Enrichment):** R2's HARD_DELETE writes feed R4's queue (newly-flagged companies become R4 candidates same day).
- **Cooper's manual archive** (filter Companies → "Flagged for deletion" → archive) is the next downstream step - R4 prepares the data, Cooper executes the bulk action.
