# R2 Stale Re-Enrichment - 2026-05-28 (Cowork scheduled task)

**Status:** GREEN freshness - 0 stale candidates
**Run start:** 2026-05-28 11:00 AM CT (scheduled)
**Apollo budget:** 0/50 sub-cap consumed; W22 weekly 0/850 (850 remaining)

## Trigger query result

- **Filter group A** (last_enriched_date < 2026-01-28, exclude Flagged-for-deletion + MaiaEdge own): **0 records**
- **Filter group B** (no last_enriched_date AND has customer_segment, exclude Flagged-for-deletion): **0 records** (MaiaEdge own 124293230301 is filtered out)
- **Total candidates:** 0
- **Active company population:** 3,121 (down 2 from 3,123 on 2026-05-27)

## Pre-flight checks

- Apollo budget tracker read: W22 at 0/850 (W21->W22 auto-rollover was applied on 2026-05-25 R2 fire)
- Cross-routine ledger canvas F0B0AFSB9LN: R2 Tier 3 queue confirmed empty per 2026-05-25 R2 audit (all 21 prior R2 holds were resolved by Mass Re-Enrichment Sweep 2026-05-18/19); re-confirmed empty on 2026-05-26 + 2026-05-27 runs
- Stale-pool drain status: 4th consecutive 0-candidate R2 run (2026-05-25, 2026-05-26, 2026-05-27, 2026-05-28)

## Steady-state analysis

The daily R-Tier-Audit + R2 cadence is holding the rotation pool drained as designed. With ~3,121 active companies and a 120-day rotation requirement, break-even is ~26 records/day. Today's R1 candidate pool was 10 raw / 3 processed - no new records cross the 120-day staleness threshold yet (last bulk-import wave 2026-05-27 R1 wrote 100 records that are now fresh through ~2026-09-24).

## Writes summary

| Category | Count |
|---|---|
| Apollo enrich | 0 |
| HubSpot company writes | 0 |
| Segment changes | 0 |
| Tier changes | 0 |
| Heat recomputes | 0 |
| Owner re-derives | 0 |
| Evictions (HARD_DELETE) | 0 |
| Partner Target keeps | 0 |
| MISDOMAIN auto-corrects | 0 |
| Tier 3 new holds | 0 |
| Tier 3 carryovers drained | 0 (queue already empty) |

## Self-checks

- [x] HubSpot trigger query executed cleanly (4 filters per group, sorts ASC on last_enriched_date)
- [x] MaiaEdge own (124293230301) excluded by filter
- [x] Flagged for deletion excluded by filter
- [x] Apollo budget pre-flight: 850 cr available, well above 50 sub-cap
- [x] Canvas ledger Tier 3 R2 queue: empty
- [x] No silent run - Slack DM dispatched to U0A24D9RJLS

## Run health: GREEN
