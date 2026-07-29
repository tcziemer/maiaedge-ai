# R-Tier-Audit 2026-06-17 (daily M-F)

- Total active ICP accounts reviewed: 2,844 (2,846 in pool; 2 excluded as `type = "Customer"`)
- Tier changes written: 1
- Heat changes written: 1
- Manual override skips (hs_is_target_account=true, tier writes only): 351
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (2 changes vs 10% threshold of 284.4)

## Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 300347451125 | cassavatechnologies.com | NeoCloud | AI Infrastructure providers - Neocloud | tier_1 | tier_2 | +1 | Default = T1, stale +1 = T2. last_signal_date 2026-03-18 (91d > 90d) AND no logged engagement on record. tier-compute-spec §7 |

## Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 326171164408 | hcltech.com | Cool | Cold | last_signal_date (event) 2025-12-18 = 181d, crossed 180d boundary; score 9, count 0, no open deal. tier-compute-spec §11.5 |

HubSpot company notes written: 376783875833 (Cassava), 376862447331 (HCL Technologies). `last_enriched_date` NOT bumped on either (tier-only / heat-only writes per CLAUDE.md Unified Stamping Policy).

---

## IMPORTANT FINDING - engagement field name in spec does not exist in HubSpot (flagged to Cooper)

The R-Tier-Audit prompt + the recalled MEMORY note specify `notes_last_activity_date` as the engagement field for the stale (+1) and sustained-quiet (+1) suppressor ("no rep activity <=30d / <=180d"). **That property does not exist on the Company object in this CRM** (neither does `hs_last_activity_date`). A `HAS_PROPERTY` filter on either returns a VALIDATION_ERROR; in a `properties` list they are silently ignored, so the bulk pull returned the field populated on 0 of 2,846 records.

This is NOT a connector dropout (the MEMORY-noted failure mode). It is a framework-reference-vs-reality mismatch in the spec text. Prior ledger rows show engagement HAS been sourced correctly in practice (e.g., 2026-06-16 promoted Pilot T4->T3 citing "rep engagement <30d"), so this is a documentation/clarity defect in the named field, not evidence of recurring bad writes. It still matters: the literal field `notes_last_activity_date` is unusable, so any executor that takes the spec at face value (as the first pass of this run did) will over-fire stale/quiet on signal-date age alone and demote actively-engaged accounts.

**Resolution this run:** engagement was derived from the real fields that DO exist, taking the most recent of: `notes_last_contacted`, `hs_last_sales_activity_timestamp`, `hs_last_logged_call_date`, `hs_last_logged_outgoing_email_date`, `hs_last_booked_meeting_date`. Stale/quiet were evaluated against that max-engagement date.

**Recommended fix:** update the R-Tier-Audit prompt (+ tier-compute-spec §7 + the MEMORY note) to reference `hs_last_sales_activity_timestamp` (and/or `notes_last_contacted`) instead of `notes_last_activity_date`. This affects every routine that inlines the stale/quiet modifier (R1, R2, R6, Signal Scan Stage 5b, D7).

### Spurious demotions correctly suppressed by using real engagement (would have been bad writes)

With the broken (null) engagement field, the raw pass proposed 4 tier demotions. Three were artifacts of the missing suppressor and were correctly held once real engagement was applied:

| Company ID | Name | Broken-field result | Correct result | Suppressing engagement |
|---|---|---|---|---|
| 297906089706 | Fibernow | T2 -> T3 (stale +1) | T2 (no change) | notes_last_contacted 2026-06-04 (13d) -> stale suppressed; open deal -1 holds at T2 |
| 320875891448 | Pilot | T3 -> T4 (stale +1) | T3 (no change) | notes_last_contacted 2026-06-12 (5d) -> stale suppressed |
| 254331348701 | STTELEMEDIA Global Data Centres | T2 -> T3 (stale +1, quiet +1) | T2 (no change) | last contacted 2026-01-15 (153d <=180d) -> sustained-quiet suppressed; stale-only nets to T2 = current |

Cassava Technologies is the one genuine stale demotion: signal 91d old AND no engagement of any kind on record.

---

## Run summary

```
R-Tier-Audit - 2026-06-17 (daily M-F)

Total active accounts reviewed: 2,844 (type=Customer excluded: 2)

Tier changes written: 1
  Promotions (toward Tier 1): 0
  Demotions (toward Tier 5): 1   [Cassava Technologies T1->T2, stale +1]

Heat changes written: 1
  Hot/Warm -> cooler: 1   [HCL Technologies Cool->Cold]
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 0

Heat distribution after this run (computed, all eligible ICP):
  :red_circle: Hot:  39
  :large_orange_circle: Warm: 65
  :large_yellow_circle: Cool: 120
  :white_circle: Cold: 2,620

Manual override skips (hs_is_target_account=true, tier only): 351
Stale signal +1 resulting in a tier change: 1 (Cassava)
Sustained quiet +1 resulting in a tier change: 0
Open-deal -1 resulting in a tier change: 0 (open-deal accounts already tiered or target-frozen)

Unknown (segment, sub-segment) pair warnings: 6 (null fallback applied; see below)

Next run: 2026-06-18 3:00 PM CT
```

## Unknown (segment, sub-segment) pair warnings - data-quality follow-up for Cooper

These records carry a `company_sub_segment` that does not belong to their `customer_segment` parent. R-Tier-Audit applied the segment null fallback per tier-compute-spec §6 and did NOT reclassify (reclassification is R2/R6/D7's job). None produced a tier change this run.

| Company ID | Name | customer_segment | company_sub_segment (mismatched) | Fallback used |
|---|---|---|---|---|
| 251536944849 | Kordia | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | Network Op null (T1, ceil 1, floor 2) |
| 318106540781 | Trans Pacific Networks (TPN) | Fiber Operator | Subsea cable operator | Fiber null (T3, ceil 1, floor 4) |
| 319135939295 | Grupo GTD Chile | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | Network Op null |
| 326165246700 | Gtd Colombia | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | Network Op null |
| 326183183051 | WiLine Networks | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | Network Op null |
| 326259427057 | Gtd Peru | Network Operator(Tier 1 / VNO) | Regional CLEC - Fiber operator | Network Op null |

## Interpretation notes / choices made this autonomous run

- **Open-deal modifier scope:** "open deal past appointmentscheduled" was scoped to the canonical main sales-pipeline stages only (`qualifiedtobuy`, `presentationscheduled`, `1996673735` Quote Provided, `decisionmakerboughtin`, `contractsent`) = 21 distinct ICP companies. A second pipeline exists (`Registered` / `Extension Granted` / `In Progress` / `Unassigned`, stage IDs 3807265502/03/04) but its stages are not in the canonical ordering, so they were excluded from the modifier. Conservative choice; flag if the second pipeline should count.
- **`type` exclusion** used exact title-case `Customer` (per MEMORY). 2 records excluded.
- **Pagination:** full pool pulled via `search_crm_objects` sorted `hs_object_id ASC` (15 pages, deduped to 2,846 unique).
- Compute was run deterministically in Python from the pulled records (no per-record LLM arithmetic).
