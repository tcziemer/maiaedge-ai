# R-Tier-Audit - 2026-05-27 (Wed) - APPLIED

**Status:** :white_check_mark: **Complete. Circuit breaker tripped at 18.2%, Cooper approved, all 470 writes succeeded.**

**Run mode:** Daily M-F 3:00 PM CT (per 2026-05-21 cadence change).

## Headline

| | |
|---|---:|
| Active ICP records reviewed | 2,577 |
| Tier changes attempted | 458 |
| Tier changes succeeded | 458 |
| Heat changes attempted | 12 |
| Heat changes succeeded | 12 |
| Note creations succeeded | 470 |
| Failures | 0 |
| Target-account tier skips honored | 326 |
| Heat writes on target-account records (NOT skipped) | 10 |
| Combined % of pool changed | 18.2% |
| Circuit breaker | TRIPPED → Cooper approved all → applied |

## Sequence of events

| Time (UTC) | Event |
|---|---|
| 2026-05-27 20:00 | Scheduled fire (3pm CT) |
| 2026-05-27 20:00-20:10 | Phase 1+2+2b: paged 13 pages from HubSpot (2,577 records), computed tier + heat deltas for each |
| 2026-05-27 20:10 | Phase 3: change_count = 470 / 2,577 = 18.2% — circuit breaker tripped |
| 2026-05-27 20:11 | DRY-RUN file + CSVs persisted, DM sent to Cooper, canvas updated |
| 2026-05-27 ~20:50 | Cooper replied: "ok proceed with the changes" → Option A (approve all) |
| 2026-05-27 20:52-21:09 | Apply phase: 47 field-update batches + 47 note-creation batches = 94 MCP calls, 0 failures |
| 2026-05-27 21:09 | Audit log + completion DM sent |

## Modifier counts

| Modifier | Records |
|---|---:|
| Tier promotions (delta < 0, toward T1) | 368 |
| Tier demotions (delta > 0, toward T5) | 90 |
| Hot signal fired (-1) | 2 (TD, Citi) |
| White-hot signal fired (-2) | 0 |
| Stacked signals fired (-1) | 0 (Hut 8 heat-only) |
| Open-deal fired (-1) | 4 (HDCO Group, CENTRA Digital, Atlantech, Arvig) |
| Stale signal fired (+1) | 0 |
| Sustained quiet fired (+1) | 0 |

Only 6 of the 458 tier deltas were signal-modifier driven. The other 452 were pure default-table rebaselines from the Phase 3 (2026-05-14) framework migration backlog.

## Pattern breakdown

| Pattern | Count | Direction |
|---|---:|---|
| NetworkOp `Tier 1 Carrier - Network Op` T2→T1 | ~200 | promotion |
| NetworkOp `Tier 1 Carrier - Network Op` T3→T1 | ~95 | promotion |
| NetworkOp `Tier 1 Carrier - Network Op` T4→T1 | 4 (Akton, ONEMAX, SBTS, Teligent — delta -3) | promotion |
| MSP/Aggregator (Telecom Agg / Managed Net / Cloud+Telecom Hybrid) T3→T2 | ~55 | promotion |
| Data Center Colo `AI Signals - colo` T3→T1 | 6 (AUBix, RadiusDC, CENTRA, EdgeCloudLink, Qoob, Macquarie) + Conapto -1 | promotion |
| Data Center Colo `Greenfield` T3→T2 | ~12 | promotion |
| Data Center Colo `Standard - colo` T2→T3 | ~10 | demotion (floor correction) |
| Data Center Colo `Standard - colo` T4→T3 | ~12 | promotion |
| Fiber `Regional CLEC - Fiber operator` T2→T3 | ~50 | demotion |
| Fiber `Regional CLEC - Fiber operator` T4→T3 | ~30 | promotion |
| Fiber `Municipal / Cooperative - Fiber operator` T2/T3→T4 | ~10 | demotion |
| Open-deal modifier hits | 4 | promotion -1 |
| Hot-signal modifier hits | 2 | promotion |
| 1 unknown-pair fallback demotion | TPN T2→T3 | demotion |

## Heat changes (12 total, all applied)

| company_id | name | old_heat | new_heat | reason |
|---|---|---|---|---|
| 153481186012 | IENTC Telecom | (none) | Cold | no signal date |
| 155473925856 | RevNet | Hot | Cold | no signal date — truthing correction |
| 265768509166 | HDCO Group | (none) | Hot | open deal past appointmentscheduled |
| 300408171229 | TD Synnex | (none) | Cold | no signal date |
| 303445718756 | T-Systems | (none) | Cold | no signal date |
| 303890867935 | Crown Castle | (none) | Cold | no signal date |
| 321842590405 | Logicalis | (none) | Cold | no signal date |
| 324007013098 | TeraWulf | Cold | Warm | warm signal score=30.0 within 60d |
| 324007013101 | Crusoe Energy Systems | Cold | Cool | signal date within 180d (ds=61) |
| 324060022514 | Astound | Cold | Cool | signal date within 180d (ds=73) |
| 324208873163 | Hut 8 | Cold | Hot | stacked signals count_30d=2 |
| 324591600333 | ResetData | (none) | Cold | no signal date |

10 of the 12 heat changes were on `hs_is_target_account=true` records. Heat is NOT frozen by the target-account flag per spec §11.5; all 10 were applied.

## Heat distribution after run

| Heat | Records |
|---|---:|
| :red_circle: Hot | 25 |
| :large_orange_circle: Warm | 23 |
| :large_yellow_circle: Cool | 14 |
| :white_circle: Cold | 2,515 |

## Unknown-pair warning

| company_id | name | segment | sub_segment | Note |
|---|---|---|---|---|
| 318106540781 | Trans Pacific Networks (TPN) | Fiber Operator | Subsea cable operator | `Subsea cable operator` is canonically a Network Operator(Tier 1 / VNO) sub-segment per spec §5. Fell to Fiber Operator null fallback (T3). Tier demoted T2→T3 this run as result. Flag for D7 / R2 to correct segment to `Network Operator(Tier 1 / VNO)`. |

## Per-record audit trail

Every changed record received a HubSpot company Note with this format:

```
Tier <X> -> <Y> on 2026-05-27 by R-Tier-Audit: <reason>
Heat <X> -> <Y> on 2026-05-27 by R-Tier-Audit: <reason>
```

Records receiving both tier and heat updates (HDCO Group 265768509166, IENTC Telecom 153481186012) got separate notes for each.

## last_enriched_date

NOT bumped on any of the 470 writes, per CLAUDE.md Unified Stamping Policy. R2's 120-day rotation owns the enrichment freshness gate.

## Artifacts on disk

| File | Description |
|---|---|
| `weekly-reports/tier-audit/2026-05-27-tier-audit.md` | This file — final audit log |
| `weekly-reports/tier-audit/2026-05-27-tier-deltas-applied.csv` | 458 rows applied |
| `weekly-reports/tier-audit/2026-05-27-heat-deltas-applied.csv` | 12 rows applied |
| `weekly-reports/tier-audit/2026-05-27-DRY-RUN.md` | Original circuit-breaker dry-run report (retained for audit) |
| `weekly-reports/tier-audit/2026-05-27-DRY-RUN-summary.json` | Structured summary |
| `outputs/r-tier-audit-2026-05-27/page-0..12.json` | Raw HubSpot pages (audit trail) |

## Next run

Thu 2026-05-28 3:00 PM CT. With the Phase 3 backlog now drained, expected drift should be single-digit (just the daily signal-modifier evictions + occasional new-record heat initializations). If tomorrow trips the breaker again with the same default-rebaseline pattern, R2 may be writing tier values that don't match the defaults table — investigate the R2 tier-write logic.
