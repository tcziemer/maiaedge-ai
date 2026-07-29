# CRM Ops Daily Digest — 2026-06-05

_Generated 16:56 CT. Window: 2026-06-04 16:45 CT → 2026-06-05 16:56 CT (Friday, prior ~24h)._
_Read-only on HubSpot. Dashboard: https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B7YMN4XEG_

## Stage 1 — Ground-truth deltas (HubSpot)

| Metric | Count | Source filter |
| --- | --- | --- |
| Enriched / re-enriched | 419 | `last_enriched_date >= 2026-06-04` |
| NEW company records created | 267 | `createdate >= 2026-06-04` |
| Company records modified in window | 1,150 | `hs_lastmodifieddate >= 2026-06-04` |
| Flagged-co records modified in window | 195 | `customer_segment = Flagged for deletion` + `hs_lastmodifieddate >= 2026-06-04` |
| Signal writes | 0 | `last_signal_date >= 2026-06-04` |
| Contacts touched | 4,137 | `lastmodifieddate >= 2026-06-04` |
| Contacts flagged_for_deletion | 531 | `flagged_for_deletion = true` |
| Tier changes | ~48 (45 R-Tier-Audit + 3 R6) | ledger |
| Heat changes | 10 (R-Tier-Audit) | ledger |
| Owner corrections | 90 (R6) | ledger |

Net flagged-for-deletion pool: 250 (06-04 digest) → 226 today = **−24**. The 195 "modified-in-window" figure is mostly R3/R4 re-touches of the existing pool, NOT net-new flags.

## Stage 2 — Fleet health (9 of 9 expected fired)

| Routine | Last run | Status | Records | Apollo |
| --- | --- | --- | --- | --- |
| R6 Territory & Hygiene | 06-05 01:00 ET | ✅ | 90 owners, 3 tier rewrites | 0/5 |
| R3 Duplicate Accounts | 06-05 02:00 ET | ✅ | 1 HIGH pair (Hotwire) | 0 |
| R8 Persona Fill | 06-05 ~09:00 ET | ✅ | 10 contact creates | 7/175 |
| R0 Import Validator | 06-05 09:00 | ⚠️ | 4 scanned, 2 RENAMABLE HIGH | 0 |
| R1 Fresh Enrichment | 06-05 10:00 | ✅ | 2/2 processed | 0/30 |
| R2 Stale Re-Enrichment | 06-05 11:00 | ✅ | 0 stale; 19 re-stamped | 0/50 |
| R4 Flagged Consolidation | 06-05 12:00 | ✅ | 218 pool; 89 contacts preserved | 0 |
| R10 Field Completeness Sweep | 06-05 ~13:30 | ✅ | sweep + deep-research + follow-up | 0/25 |
| R-Tier-Audit | 06-05 15:00 | ✅ | 45 tier + 10 heat (1.89%) | 0 |

Not expected today (not graded): D7 (Wed), R5 (Sun), Signal Scan (Mon), R7 (1st), R9 (quarterly). R0 ⚠️ = normal steady-state partial. Rep deliverable Daily Sales Activity Brief scheduled 6pm CT (post-digest).

Apollo W23: tracker header 0/850; R8 ledger reports 7 credits consumed. Well under cap either way.

## Stage 3 — Flagged for deletion (standing pool)

226 companies + 531 contacts. Reason breakdown:
- D1 disqualified (no reference value): 74
- Duplicate (merged): 67
- No ICP fit: 45
- Defunct / out of business: 30
- Hard junk / non-business: 10
- Dead domain: 0
- Stalled greenfield: 0
- Empty reason: 0

SAFE_TO_DELETE vs needs-review split not computed this run.

## Attention

- Non-blocking awareness: 267 new company records in window — larger than typical; consistent with a bulk import/seed batch. R0 + R10 absorbing. No action.
- No blockers, no failed fires, no 🔴 errors.

## Manual-review backlog

26 companies `segmentation_confidence = manual_review_required` (HubSpot ground truth). Under 5% target. Prior digest canvas-Tier-3 count was 14 (narrower set). D7 (Wed) drains. **Record for tomorrow's trend: HubSpot manual-review = 26 (2026-06-05).**

## Anomalies / notes

- `last_signal_date` query returned 0 — expected on a Friday (signal scan is Monday-only).
- Working ledger F0B0AFSB9LN exceeds canvas read limit (818K chars); parsed via saved tool-result file. Run-log rows + Tier-3 section read successfully.
