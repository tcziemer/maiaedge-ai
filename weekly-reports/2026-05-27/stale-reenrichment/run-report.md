# R2 Stale Re-Enrichment - 2026-05-27

**Run start:** 2026-05-27 11:00 AM CT
**Runtime:** Cowork scheduled task
**Status:** GREEN (steady-state, 0 candidates)

## Pool

- **Filter group A** (`last_enriched_date < 2026-01-27` AND not Flagged for deletion AND not MaiaEdge own): **0 records**
- **Filter group B** (no `last_enriched_date` AND has `customer_segment` AND not Flagged for deletion AND not MaiaEdge own): **0 records** (1 raw, but it's MaiaEdge own 124293230301, hard-stop excluded)
- **Total stale pool:** 0

## Triage

No candidates. No FULL / LIGHT / RECLASSIFY / DEFER work.

## Writes

- 0 Apollo enrich
- 0 HubSpot writes
- 0 segment changes
- 0 evictions
- 0 Tier 3 new holds

## Tier 3 Carryovers Drained

R2 Tier 3 queue was already confirmed empty at 2026-05-25 (Mass Re-Enrichment Sweep resolved all 21 prior holds: 14 fixed, 7 removed from HubSpot). No carryovers to drain today.

## Apollo Budget

- Sub-cap: 50 credits/run
- Used: 0 of 50
- Weekly W22: 0/850, 850 remaining

## CRM Snapshot

- Total active companies (excluding Flagged for deletion): **3,123**
- R1 today added/touched ~85 net-new + 100 writes. None will become stale until ~2026-09-24 (120 days from today).

## Steady-State Note

Third consecutive 0-candidate R2 run (2026-05-25, 2026-05-26, 2026-05-27). Daily R-Tier-Audit (M-F) + daily R2 (M-F) cadence is holding the rotation pool drained as designed.

Break-even calculation:
- Active pool: 3,123 records
- Rotation: 120 days
- Daily break-even: 3,123 / 120 = ~26 records/day
- R2 sub-cap: 50 records/day = 92% headroom

Backlog accumulates only when a Mass-Re-Enrichment Sweep refreshes a large cohort at once - those records all hit the 120-day mark together. Next expected spike: ~2026-09-15 (120 days after 2026-05-18 Mass Re-Enrichment Sweep, which touched all active ICP records).

## Self-Check

| Check | Result |
|---|---|
| Trigger query returned expected total | ✅ 0 |
| Apollo budget tracker updated | ✅ |
| Slack DM sent | ✅ |
| Canvas Run log appended | ✅ |
| No silent writes | ✅ |

Run health: **GREEN**
