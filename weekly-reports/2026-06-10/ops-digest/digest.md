# CRM Ops Daily Digest — 2026-06-10

Window: since 2026-06-09 16:45 CT (prior ~24h). HubSpot = ground truth. Read-only on HubSpot; Apollo 0.

## Stage 1 — Ground-truth deltas (window)
- Enriched / re-enriched (`last_enriched_date >= 2026-06-09`): **133**
- Newly flagged for deletion (`customer_segment = Flagged for deletion` AND `hs_lastmodifieddate >= 2026-06-09`): **64** records modified-while-flagged (mostly R4 reassociation touches + R3 overnight dedup). Standing pool net delta: 267 → 301 = **+34 net new flags**.
- Signal writes (`last_signal_date >= 2026-06-09`): **0** (signal scan is Monday-only).
- Companies modified in window (tier/heat/segment/confidence proxy): **459**.
- NEW accounts (`createdate >= 2026-06-09`): **9** (includes QA smoke-test artifacts, e.g. "ZZZ QA Retest Conflict" / zzz-qa-retest-conflict.com, zzzsmoketestprospect.com).
- Contacts touched (`lastmodifieddate >= 2026-06-09`): **2,343**. Flagged contacts (`flagged_for_deletion = true`): **327**.
- Manual-review backlog (`segmentation_confidence = manual_review_required`): **0** (was 33 on 06-09). Field verified populated on 3,528 records → zero is real (D7 drain), not a connector dropout.

## Stage 2 — Fleet health
| Routine | Last run (CT) | Status | Records touched | Apollo |
|---|---|---|---|---|
| R0 Import Validator | 2026-06-10 09:02 | ✅ | imports validated | 0 |
| R1 Fresh Enrichment | 2026-06-10 10:09 | ✅ | 2 (Cyfuture ICP write; CMDB360 flagged No-ICP-fit) | 0/30 |
| R2 Stale Re-Enrichment | 2026-06-10 11:03 | ✅ | 39 (Novus evicted wrong-entity; ICE Tier-3 held) | 0/50 |
| R4 Flagged Consolidation | 2026-06-10 12:06 | ✅ | consolidation pass | 0 |
| R10 Completeness Sweep | 2026-06-10 13:31 | ✅ | 0 (ICP pool drained; quiet-on-success) | 0/25 |
| D7 Edge Case Resolution | 2026-06-10 09:01 | ✅ | manual-review 33 → 0 drained | 0 |
| R-Tier-Audit | 2026-06-10 15:04 | ✅ | 66 tier changes (2.31%, no breaker); all signal-decay demotions | 0 |
| R3 Duplicate Accounts | overnight 02:00 ET | ✅ (inferred from dedup flags) | dedup flags | 0 |
| R6 Territory & Hygiene | overnight 01:00 ET | ✅ (inferred) | territory/hygiene | 0/5 |

Apollo W24 (2026-06-08): 0/850. Daily Sales Activity Brief: dispatched 06-09 6pm; today scheduled 6:00pm CT (post-digest). Not graded: R5 (Sun), R8 (Fri), R7 (1st), R9 (qtr), Signal Scan (Mon).

## Stage 3 — Flagged-for-deletion queue (standing pool)
**301 companies + 327 contacts.**
| Reason code | Companies |
|---|---|
| Duplicate (merged) | 107 |
| D1 disqualified (no reference value) | 74 |
| No ICP fit | 73 |
| Defunct / out of business | 31 |
| Hard junk / non-business | 14 |
| Dead domain | 2 |
| Stalled greenfield | 0 |
| (empty reason) | 0 |

Breakdown via leading-code + legacy-phrasing substring fallback across full 301-record pull (2 pages). SAFE_TO_DELETE split not computed this run.
Decision-not-delete carry: Bits in Flight, Ltd (326674182894) flagged but has OPEN deal "H5 Data Centers - Partner Reg" → R4 open-deal hard stop.
Filters → Companies: `customer_segment = "Flagged for deletion"`; Contacts: `flagged_for_deletion = true`.

## Attention
- D7 today's disk report folder (`weekly-reports/2026-06-10/d7-edge-case-resolution/`) not present — D7 ran per scheduler and drained the manual-review queue, so functionally healthy; data gap only.
- ResetData frozen-tier loop (standing): `hs_is_target_account = true` + blank `account_tier`; Cooper decision pending (not in today's R1 pool).
- No missed fires, no circuit-breaker trips, no failed dispatches.

## Manual-review backlog trend
26 (06-05) → 33 (06-08) → 33 (06-09) → **0 (06-10)**. Shrinking — D7 drained the full queue. Record for next trend: 0.

## Run metadata
- Working ledger F0B0AFSB9LN exceeds canvas read limit (916K chars); Run-log + Tier-3 context parsed from apollo-budget.json history + scheduled-task lastRunAt + saved tool-result file.
- Dashboard canvas F0B7YMN4XEG refreshed (full replace) at 2026-06-10 16:53 CT.
- DM sent to Cooper (U0A24D9RJLS). Apollo W24: 0/850.
