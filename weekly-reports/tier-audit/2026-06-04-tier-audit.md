## R-Tier-Audit 2026-06-04

- Total active accounts reviewed: 2577
- Tier changes written: 5
- Heat changes written: 1
- Manual override skips (tier writes only): 323
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (0.23% << 10%)

### Per-record tier changes

| Company ID | Name | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 175217873639 | GCI | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | hot signal -1 (score 30, event 2026-04-22 / 43d) |
| 292748543699 | Lyte Fiber | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | stacked signals -1 (signal_count_last_30d=2) |
| 314300605141 | Prominic.NET | Data Center Colo Provider | Standard - colo | tier_5 | tier_3 | -2 | reverts to default T3; last_signal_date null so stale/quiet cannot fire (over-decayed) |
| 316283788005 | IELO-Liazo Services | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_3 | tier_2 | -1 | default correction to T2, no modifiers |
| 317341909696 | South Front Networks | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | -1 | reverts to default T3 (over-decayed, no active signal) |

### Per-record heat changes

| Company ID | Name | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 292748543699 | Lyte Fiber | Warm | Hot | signal_count_last_30d=2 (stacked) -> Hot |

### Summary

R-Tier-Audit - 2026-06-04 (daily M-F)

Total active accounts reviewed: 2577

Tier changes written: 5
  Promotions (toward Tier 1): 5
  Demotions (toward Tier 5): 0

Heat changes written: 1
  Hot/Warm -> cooler: 0
  Cool/Cold -> hotter: 1
  Heat writes on target-account records (not skipped): 0

Heat distribution after this run (across all active ICP):
  :red_circle: Hot: 36
  :large_orange_circle: Warm: 27
  :large_yellow_circle: Cool: 75
  :white_circle: Cold: 2439

Manual override skips (hs_is_target_account=true, tier only): 323
Stale signals decayed (+1 tier): 0
Sustained quiet decayed (+1 tier additional): 0
Open-deal promotions (-1 tier): 0 net new (16 ICP open-deal accounts already Hot/at-tier from prior runs; idempotent no-op)

Top tier changes by delta:
1. Prominic.NET (Data Center Colo Provider): T5 -> T3 -- reverts to Standard-colo default; signal date cleared
2. GCI (Fiber Operator): T3 -> T2 -- hot signal -1
3. Lyte Fiber (Fiber Operator): T3 -> T2 -- stacked signals -1
4. IELO-Liazo Services (Fiber Operator): T3 -> T2 -- default correction
5. South Front Networks (Fiber Operator): T4 -> T3 -- reverts to default

Top heat changes:
1. Lyte Fiber (Fiber Operator): Warm -> Hot -- stacked signals (count=2)

Unknown (segment, sub-segment) pair warnings: 1
  - 318106540781 Trans Pacific Networks (TPN): Fiber Operator / "Subsea cable operator" (sub-segment belongs to Network Operator parent). Applied Fiber Operator null fallback (T3, ceiling 1, floor 4); computed T3 == current, no write. Data-quality follow-up: reclassify segment to Network Operator(Tier 1 / VNO) or correct sub-segment.

### Data-quality note (engagement field)

`notes_last_activity_date` returned EMPTY for all 2577 records this run, including the 16 ICP accounts with open June-2026 deals that demonstrably have recent activity. This is the HubSpot connector dropping the engagement rollup field (matches the known tier_audit_connector_dropout failure mode). Impact assessment: the engagement field only gates the stale (+1) and sustained-quiet (+1) demotion modifiers. This run produced ZERO demotions (all 5 tier changes are promotions), so the dropped field caused no false demotions. The 79 records with last_signal_date>90d already sit at their decayed tiers from prior runs; running the spec as written (engagement-absent => stale/quiet eligible on signal-date age) reproduced their maintained state idempotently rather than re-promoting them (the alternative of suppressing those modifiers would have wrongly re-promoted 68 records and thrashed daily). No Cooper escalation required because no writes depended on the unreliable field. If a future run shows pool-wide stale/quiet DEMOTIONS firing while notes_last_activity_date is empty, HOLD and DM Cooper.

### Quality checks
1. All eligible records processed: 2577 reviewed = changes + no-ops. PASS
2. No tier writes on hs_is_target_account=true: 323 skipped for tier; 0 target-account tier writes. PASS
3. All writes have HubSpot notes: 6/6 notes created + associated. PASS
4. Circuit breaker threshold 10% computed against 2577: 0.23% combined. PASS
5. Local audit log persisted: this file. PASS

last_enriched_date: NOT bumped (tier/heat-only writes per Unified Stamping Policy). 

Next run: 2026-06-05 3pm CT (Friday).
