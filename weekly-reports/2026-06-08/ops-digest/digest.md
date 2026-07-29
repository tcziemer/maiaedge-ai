# CRM Ops Daily Digest — 2026-06-08 (Monday catch-up)

_Generated 16:57 CT. Window: 2026-06-05 16:45 CT → 2026-06-08 16:57 CT (Monday: covers weekend R3/R6 daily, Sun R5, Monday signal scan)._
_Read-only on HubSpot. Apollo 0/850 (W24). Dashboard: https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B7YMN4XEG_

## Stage 1 — Ground-truth deltas (HubSpot)

| Metric | Count | Source filter |
| --- | --- | --- |
| Enriched / re-enriched | 210 | last_enriched_date >= 2026-06-05 |
| NEW company records created | 341 | createdate >= 2026-06-05 |
| Signal writes (in-window event date) | 1 | last_signal_date >= 2026-06-05 (event-date semantics) |
| Flagged-co records modified in window | 225 | Flagged for deletion + hs_lastmodifieddate >= 2026-06-05 |
| Contacts touched | 7,244 | lastmodifieddate >= 2026-06-05 |
| Contacts flagged_for_deletion | 330 | flagged_for_deletion = true |
| Tier changes | ~64 (62 up / 2 down) | R-Tier-Audit today + weekend R6 |
| Heat changes | 12 | R-Tier-Audit (NeoCloud new-acct -> Cold) |

Note: Signal Scan wrote ~38 signal fields today (Colo 5 + NeoCloud 33 incl. 2 NEW accounts), but only 1 carries an in-window last_signal_date because the field stores event date, not detection date. Structured count understates field-write activity by design (2026-05-28 unification).

## Stage 2 — Fleet health (7 of 10 green; 3 normal partials; 0 blockers)

| Routine | Last run | Status | Records | Apollo |
| --- | --- | --- | --- | --- |
| R6 Territory & Hygiene | 06-08 01:00 ET | OK | weekend: 17 owners 06-07 + Sat sweep | 0/5 |
| R3 Duplicate Accounts | 06-08 02:00 ET | OK | full scan 06-06/07/08, no new HIGH pairs | 0 |
| R5 Contact Dedup | 06-07 (Sun) | OK | 18,801 scanned; 0 new dup groups; 531 stale flags cleared | 0 |
| R0 Import Validator | 06-08 09:00 | OK | quiet; 0 corrections; 6 Tier-3 dup stubs -> R3 | 0 |
| R1 Fresh Enrichment | 06-08 10:00 | WARN | small batch; Tier-3 holds added (normal) | 0/30 |
| R2 Stale Re-Enrichment | 06-08 11:00 | OK | GREEN; 10 written (6 low->med + 3 field-completions) | 0/50 |
| R4 Flagged Consolidation | 06-08 12:00 | WARN partial | 247 pool; 150 processed, 97 carryover; contacts preserved | 0 |
| R10 Completeness Sweep | 06-08 13:31 | WARN partial | 22 heat fills; 53 held (non-ICP) | 0/25 |
| Signal Scan (6 seg + aggregator) | 06-08 08:30-14:30 | OK | Colo 5 + NeoCloud 33 incl. 2 NEW; 3 rep DMs + xlsx | 0/250 |
| R-Tier-Audit | 06-08 15:00 | OK | 64 tier (62 up/2 down) + 12 heat; breaker ~1.x% OK | 0 |

Not expected today (not graded): D7 (Wed), R7 (1st), R9 (quarterly), R8 (Fri-only). All WARN rows are expected steady-state partials, not errors. Daily Sales Activity Brief scheduled 6:00 PM CT (post-digest).

## Stage 3 — Flagged for deletion (standing pool)

247 companies + 330 contacts. Reason breakdown (sums to 247):
- Duplicate (merged): 82
- D1 disqualified (no reference value): 74
- No ICP fit: 51
- Defunct / out of business: 30
- Hard junk / non-business: 10
- Dead domain: 0
- Stalled greenfield: 0
- Empty reason: 0

SAFE_TO_DELETE vs needs-review split not computed this run.

Decision (not delete): Fast Wave (323666965217) flagged but holds open deal "Broadstar - New Logo" $10K presentationscheduled — likely upstream mis-flag; R4 held on open-deal hard stop; recommend removing flag + reclassify.

HubSpot filters: Companies -> customer_segment = "Flagged for deletion"; Contacts -> flagged_for_deletion = true.

## Attention

- R10 structural loop — trigger company_sub_segment NOT_HAS_PROPERTY perpetually re-surfaces the non-ICP Other/Partner pool (~550) that can never carry an ICP sub-segment; non-drainable. Fix options surfaced to Cooper. Until fixed R10 writes only signal_heat = Cold and reports a false-large incomplete pool.
- ResetData frozen-tier loop still recurring daily (escalated; awaiting Cooper).
- Manual-review backlog 33 (up from 26 on 06-05). ~1.1% of active pool, under 5% target. D7 (Wed) drains.

## Manual-review backlog trend

HubSpot segmentation_confidence = manual_review_required: 26 (2026-06-05) -> 33 (2026-06-08), +7. Record for next trend: 33 (2026-06-08).

## Anomalies / notes

- Working ledger F0B0AFSB9LN exceeds canvas read limit (872K chars); parsed via saved tool-result file + apollo-budget.json history. Run-log rows for R3/R5/R6 weekend + Monday routines confirmed.
- Reason breakdown computed via CONTAINS_TOKEN per code; total reconciles exactly to 247.
- Apollo W24 auto-rolled from W23 (closed 0/850) on the 06-08 R1 fire.
