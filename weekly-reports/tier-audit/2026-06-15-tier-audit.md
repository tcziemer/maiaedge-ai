# R-Tier-Audit - 2026-06-15 (daily M-F)

- Total active accounts reviewed: 2847 (2849 ICP-segment records minus 2 `type = Customer` exclusions incl. HDCO GROUP; MaiaEdge own record excluded)
- Tier changes written: 11
- Heat changes written: 11
- Manual override skips (tier writes only): 78 (hs_is_target_account=true records whose computed tier differed; tier frozen, heat still written)
- Heat writes on target-account records (not skipped): 6
- Circuit breaker triggered: NO (17 changed records / 2847 = 0.60% < 10% threshold of 284.7)
- Apollo budget consumed: 0

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 193100077770 | alaskacommunications.com | Fiber Operator | Tier 2 National Wholesale - Fiber operator | 2 | 3 | +1 | Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, stale +1 = T3. |
| 193867595510 | gigabitfiber.com | Fiber Operator | Regional CLEC - Fiber operator | 2 | 3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3. |
| 194004502229 | arvig.com | Fiber Operator | Regional CLEC - Fiber operator | 2 | 1 | -1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, hot -1, open deal -1 = T1. |
| 254331348701 | sttelemediagdc.ph | Data Center Colo Provider | Hyperscale Wholesale - colo | 3 | 2 | -1 | Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2. |
| 254626062049 | metrobloks.com | Data Center Colo Provider | Greenfield | 2 | 3 | +1 | Default Data Center Colo Provider/Greenfield = T2, stale +1, sustained quiet +1 = T3. |
| 297906089706 | fibernow.com | Fiber Operator | Regional CLEC - Fiber operator | 2 | 3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, open deal -1, stale +1 = T3. |
| 322353526464 | getaccessplus.com | Fiber Operator | Regional CLEC - Fiber operator | 3 | 4 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4. |
| 322843549398 | tec.com | Fiber Operator | Regional CLEC - Fiber operator | 2 | 3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3. |
| 323823198922 | https://wisperisp.com | Fiber Operator | Regional CLEC - Fiber operator | 2 | 3 | +1 | Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3. |
| 324641480388 | https://www.htcinc.net | Fiber Operator | Municipal / Cooperative - Fiber operator | 3 | 4 | +1 | Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4; no active signal modifiers; reset to default = T4. |
| 326171164408 | hcltech.com | Enterprise-CustomerSegment | Outsourcing Services - Enterprise | 3 | 4 | +1 | Default Enterprise-CustomerSegment/Outsourcing Services - Enterprise = T3, stale +1 = T4. |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 193867595510 | gigabitfiber.com | Hot | Cold | no last_signal_date on record, no open deal -> Hot to Cold |
| 251574626020 | h5datacenters.com | Hot | Cool | signal decayed: last_signal_date (event) 2026-01-29 137d old, score 9, no stack, no open deal -> Hot to Cool |
| 254626062049 | metrobloks.com | Cool | Cold | last_signal_date (event) 2025-03-31 is 441d old (>180d) -> Cool to Cold |
| 320988084985 | newerainfra.ai | Warm | Cool | last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |
| 321635744480 | rowan.digital | Warm | Cool | last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |
| 322843549398 | tec.com | Warm | Cool | last_signal_date (event) 2026-04-14 now 62d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |
| 323823198922 | https://wisperisp.com | Hot | Cold | no last_signal_date on record, no open deal -> Hot to Cold |
| 324037036787 | appdirect.com | Warm | Cool | last_signal_date (event) 2026-04-14 now 62d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |
| 324641480388 | https://www.htcinc.net | Hot | Cold | no last_signal_date on record, no open deal -> Hot to Cold |
| 326532538071 | kakaocloud.com | Warm | Cool | last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |
| 326674125535 | nhncloud.com | Warm | Cool | last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool |

```
R-Tier-Audit - 2026-06-15 (daily M-F)

Total active accounts reviewed: 2847

Tier changes written: 11
  Promotions (toward Tier 1): 2
  Demotions (toward Tier 5): 9

Heat changes written: 11
  Hot/Warm -> cooler: 11
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 6

Heat distribution after this run (across all active ICP):
  :red_circle: Hot: 39
  :large_orange_circle: Warm: 66
  :large_yellow_circle: Cool: 120
  :white_circle: Cold: 2622

Manual override skips (hs_is_target_account=true, tier only): 78 of 351 target accounts (tier frozen where computed differed)
Modifier fires across active pool (most already reflected in current tier; only net deltas written this run):
  Stale signals (+1 tier): 97
  Sustained quiet (+1 tier additional): 65
  Open-deal (-1 tier): 16
  Hot signal (-1): 82  |  White-hot (-2): 0  |  Stacked (-1): 23

Top tier changes by delta:
1. Alaska Communications Systems Group (Fiber Operator): T2 -> T3 -- Default Fiber Operator/Tier 2 National Wholesale - Fiber operator = T2, stale +1 = T3.
2. Gigabit Fiber (Fiber Operator): T2 -> T3 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3.
3. Arvig (Fiber Operator): T2 -> T1 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3, hot -1, open deal -1 = T1.
4. STTELEMEDIA Global Data Centres (Data Center Colo Provider): T3 -> T2 -- Default Data Center Colo Provider/Hyperscale Wholesale - colo = T1, stale +1 = T2.
5. Metrobloks (Data Center Colo Provider): T2 -> T3 -- Default Data Center Colo Provider/Greenfield = T2, stale +1, sustained quiet +1 = T3.
6. Fibernow (Fiber Operator): T2 -> T3 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3, open deal -1, stale +1 = T3.
7. AccessPlus (Fiber Operator): T3 -> T4 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3, stale +1 = T4.
8. TEC (Fiber Operator): T2 -> T3 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3.
9. Wisper ISP (Fiber Operator): T2 -> T3 -- Default Fiber Operator/Regional CLEC - Fiber operator = T3; no active signal modifiers; reset to default = T3.
10. HTC, Inc. (Horry Telephone Cooperative) (Fiber Operator): T3 -> T4 -- Default Fiber Operator/Municipal / Cooperative - Fiber operator = T4; no active signal modifiers; reset to default = T4.
11. HCL Technologies (Enterprise-CustomerSegment): T3 -> T4 -- Default Enterprise-CustomerSegment/Outsourcing Services - Enterprise = T3, stale +1 = T4.

Top heat changes:
1. Gigabit Fiber (Fiber Operator): Hot -> Cold -- no last_signal_date on record, no open deal -> Hot to Cold
2. H5 Data Centers (Data Center Colo Provider): Hot -> Cool -- signal decayed: last_signal_date (event) 2026-01-29 137d old, score 9, no stack, no open deal -> Hot to Cool
3. Metrobloks (Data Center Colo Provider): Cool -> Cold -- last_signal_date (event) 2025-03-31 is 441d old (>180d) -> Cool to Cold
4. New Era Energy & Digital (Data Center Colo Provider): Warm -> Cool -- last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool
5. Rowan Digital Infrastructure (Data Center Colo Provider): Warm -> Cool -- last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool
6. TEC (Fiber Operator): Warm -> Cool -- last_signal_date (event) 2026-04-14 now 62d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool
7. Wisper ISP (Fiber Operator): Hot -> Cold -- no last_signal_date on record, no open deal -> Hot to Cold
8. AppDirect (MSP/Aggregator): Warm -> Cool -- last_signal_date (event) 2026-04-14 now 62d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool
9. HTC, Inc. (Horry Telephone Cooperative) (Fiber Operator): Hot -> Cold -- no last_signal_date on record, no open deal -> Hot to Cold
10. Kakao Cloud (NeoCloud): Warm -> Cool -- last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool
11. NHN Cloud (NeoCloud): Warm -> Cool -- last_signal_date (event) 2026-04-15 now 61d old (out of 60d Warm window), no stack, no open deal -> Warm to Cool

Unknown (segment, sub-segment) pair warnings: 6
  - Kordia (id 251536944849): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
  - Trans Pacific Networks (TPN) (id 318106540781): Unknown (segment, sub-segment) pair: Fiber Operator, Subsea cable operator. Using Fiber Operator null fallback.
  - Grupo GTD Chile (id 319135939295): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
  - Gtd Colombia (id 326165246700): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
  - WiLine Networks (id 326183183051): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.
  - Gtd Peru (id 326259427057): Unknown (segment, sub-segment) pair: Network Operator(Tier 1 / VNO), Regional CLEC - Fiber operator. Using Network Operator(Tier 1 / VNO) null fallback.

last_enriched_date: NOT bumped (tier/heat-only writes per Unified Stamping Policy)
Next run: 2026-06-16 (Tue) 3:00 PM CT
```