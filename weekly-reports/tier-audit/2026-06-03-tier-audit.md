# R-Tier-Audit 2026-06-03

- Total active accounts reviewed: 2575
- Tier changes written: 1
- Heat changes written: 0
- Manual override skips (tier writes only, hs_is_target_account=true): 323 (of which 71 had a suppressed computed-vs-current tier delta)
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (combined change_count 1 of 2575 = 0.04%, threshold 10%)

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 292796237529 | surfinternet.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4. file 06 §6.2 |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| (none) | | | | |

---

```
R-Tier-Audit - 2026-06-03 (daily M-F)

Total active accounts reviewed: 2575

Tier changes written: 1
  Promotions (toward Tier 1): 0
  Demotions (toward Tier 5): 1

Heat changes written: 0
  Hot/Warm -> cooler: 0
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 0

Heat distribution after this run (across all active ICP):
  Hot: 34
  Warm: 26
  Cool: 75
  Cold: 2440

Manual override skips (hs_is_target_account=true, tier only): 323 (71 with suppressed tier delta)
Stale signals decayed (+1 tier): 79
Sustained quiet decayed (+1 tier additional): 67
Open-deal promotions (-1 tier modifier applied): 14

Top tier changes by delta:
1. Surf Internet (Fiber Operator): T3 -> T4 -- Regional CLEC default T3, stale +1 (last_signal_date event 91d old, no engagement <=30d)

Top heat changes:
(none this run)

Unknown (segment, sub-segment) pair warnings: 1
  318106540781 Trans Pacific Networks (TPN): customer_segment=Fiber Operator with company_sub_segment='Subsea cable operator' (a Network Operator sub-segment).
  Applied Fiber Operator null fallback (T3, ceiling 1, floor 4); computed T3 == current tier, no write. R-Tier-Audit does not reclassify - flagged for D7/R2 segment review.

Quality checks: all eligible records processed (2575); no tier writes on hs_is_target_account=true; tier write carries a HubSpot note; circuit breaker threshold 10% computed against 2575; local audit log persisted.

Next run: Thursday 2026-06-04 3pm CT
```