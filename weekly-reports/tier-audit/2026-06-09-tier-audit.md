# R-Tier-Audit 2026-06-09

- Total active accounts reviewed: 2871 (2873 active ICP, 2 excluded as type=Customer)
- Tier changes written: 7
- Heat changes written: 4
- Manual override skips (tier writes only, hs_is_target_account=true): 74 of 355 target accounts
- Heat writes on target-account records (not skipped): 2
- Circuit breaker triggered: NO (11 combined changes vs 287 threshold = 0.4%)
- Apollo budget consumed: 0

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 264413011658 | cleanspark.com | NeoCloud | Crypto to AI - Neoclouds | tier_2 | tier_1 | -1 | Default = T1; drift correction to segment default, no signal modifiers |
| 326325669589 | (Celeste) | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | -1 | Default = T3; drift correction to segment default |
| 326331061982 | expereo.com | MSP/Aggregator | Managed Network Services - MSP | tier_2 | tier_3 | +1 | Default T2, stale +1 (last_signal_date 2026-03-10 >90d, no engagement <=30d) = T3 |
| 326381387478 | telenor.dk | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default = T1; drift correction to segment default |
| 326390414028 | t-mobile.pl | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default = T1; drift correction to segment default |
| 326642119370 | telenor.com.pk | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default = T1; drift correction to segment default |
| 326692100825 | telenor.se | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | tier_1 | -1 | Default = T1; drift correction to segment default |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 206938584804 | vcomsolutions.com | Cool | Cold | last_signal_date (event) crossed 180d boundary (181d old) |
| 251593554625 | bridgepointetech.com | Warm | Cool | last_signal_date (event) 61d old, out of 60d Warm window, no stack/open deal (target acct, heat not frozen) |
| 253675771620 | aligneddc.com | Warm | Cool | last_signal_date (event) 61d old, out of 60d Warm window, no stack/open deal (target acct, heat not frozen) |
| 264588752580 | fnts.com | Cool | Cold | last_signal_date (event) crossed 180d boundary (181d old) |

---

R-Tier-Audit - 2026-06-09 (daily M-F)

Total active accounts reviewed: 2871

Tier changes written: 7
  Promotions (toward Tier 1): 6
  Demotions (toward Tier 5): 1

Heat changes written: 4
  Hot/Warm -> cooler: 4
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 2

Heat distribution after this run (all active ICP):
  Hot: 37
  Warm: 48
  Cool: 103
  Cold: 2683

Manual override skips (hs_is_target_account=true, tier only): 74 (of 355 target accounts)
Stale signals decayed (+1 tier) fired: 14 (1 produced a net tier write; rest target-frozen or already clamped)
Sustained quiet decayed (+1 tier additional) fired: 4
Open-deal modifier (-1 tier) carried by: 16 records (already at adjusted tier, 0 new writes)

Top tier changes by delta:
1. CleanSpark (NeoCloud / Crypto to AI - Neoclouds): T2 -> T1 -- drift to default
2. Telenor Danmark (Network Op / Tier 1 Carrier): T2 -> T1 -- drift to default
3. T-Mobile Polska (Network Op / Tier 1 Carrier): T2 -> T1 -- drift to default
4. Telenor Pakistan (Network Op / Tier 1 Carrier): T2 -> T1 -- drift to default
5. Telenor Sweden (Network Op / Tier 1 Carrier): T2 -> T1 -- drift to default
6. Celeste (Fiber / Regional CLEC): T4 -> T3 -- drift to default
7. Expereo (MSP / Managed Network Services): T2 -> T3 -- stale signal +1

Top heat changes:
1. Bridgepointe Technologies (MSP, target): Warm -> Cool -- 61d out of Warm window
2. Aligned Data Centers (Colo, target): Warm -> Cool -- 61d out of Warm window
3. vCom Solutions (MSP): Cool -> Cold -- 181d crossed 180d boundary
4. FNTS (MSP): Cool -> Cold -- 181d crossed 180d boundary

Unknown (segment, sub-segment) pair warnings: 7 (segment null fallback applied, no forced tier write):
  - Kordia (251536944849) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Telekom2 (316283788007) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Trans Pacific Networks / TPN (318106540781) | Fiber Operator + Subsea cable operator
  - Grupo GTD Chile (319135939295) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Gtd Colombia (326165246700) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - WiLine Networks (326183183051) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Gtd Peru (326259427057) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  (Cross-segment mismatches; D7 / Cooper data-quality follow-up. Not the 5 known MSP-on-colo pairs.)

Quality checks: all 11 changes written (7 tier + 4 heat), 0 failed; 0 tier writes on target accounts (74 frozen); every change has an associated HubSpot company note; circuit breaker computed at 10% of 2871 = 287. No connector-dropout signature (14 stale / 4 quiet across 2871 = 0.5%; heat distribution healthy).

Next run: 2026-06-10 3:00 PM CT
