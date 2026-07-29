# R-Tier-Audit 2026-06-11

- Total active accounts reviewed: 2862 (2864 active ICP, 2 excluded as type=Customer)
- Tier changes written: 5
- Heat changes written: 5
- Manual override skips (would-change tier, hs_is_target_account=true): 78 of 351 target accounts
- Heat writes on target-account records (not skipped): 1 (H5 Data Centers)
- Circuit breaker triggered: NO (10 combined changes vs 286 threshold = 0.3%)
- Apollo budget consumed: 0

### Connector-health check (no dropout)
`last_signal_date` populated on 243 records — exactly matches the independent `COUNT(*) WHERE last_signal_date IS NOT NULL` = 243, so no connector dropout of the signal field. Engagement populated on 335 records via the genuine fields `hs_last_sales_activity_timestamp` + `notes_last_contacted` (most-recent of the two); `notes_last_activity_date` is not a real Company property (0 populated) and `notes_last_updated` is deliberately excluded (batch maintenance-note timestamps are not rep activity). Heat distribution post-run is healthy (Hot 41 / Warm 50 / Cool 101 / Cold 2670). This is genuine low-volume daily drift, not a connector anomaly.

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 264034893521 | radius-dc.com | Data Center Colo Provider | AI Signals - colo | tier_1 | tier_2 | +1 | Default = T1, stale +1 (last_signal_date event >90d, no engagement <=30d) = T2 |
| 254549120743 | dynascale.com | MSP/Aggregator | Cloud + Telecom Hybrid MSP - MSP | tier_3 | tier_4 | +1 | Default = T2, stale +1, sustained-quiet +1 = T4 (signal event crossed 180d) |
| 193867595510 | gigabitfiber.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default = T3, open deal -1 = T2 (new deal past appointmentscheduled: Extension Granted) |
| 323823198922 | wisperisp.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 | Default = T3, open deal -1 = T2 (deal past appointmentscheduled: Registered) |
| 324641480388 | htcinc.net | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | tier_3 | -1 | Default = T4, open deal -1 = T3 (deal past appointmentscheduled: Registered) |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 254549120743 | dynascale.com | Cool | Cold | last_signal_date (event) 181d old, crossed 180d boundary, no stack/open deal |
| 251574626020 | h5datacenters.com | Cool | Hot | associated open deal past appointmentscheduled (target acct, heat not frozen; tier stays T1) |
| 193867595510 | gigabitfiber.com | Cold | Hot | associated open deal past appointmentscheduled (Extension Granted) |
| 323823198922 | wisperisp.com | Cold | Hot | associated open deal past appointmentscheduled (Registered) |
| 324641480388 | htcinc.net | Cold | Hot | associated open deal past appointmentscheduled (Registered) |

---

R-Tier-Audit - 2026-06-11 (daily M-F)

Total active accounts reviewed: 2862

Tier changes written: 5
  Promotions (toward Tier 1): 3 (Gigabit Fiber, Wisper ISP, HTC - all open-deal driven)
  Demotions (toward Tier 5): 2 (RadiusDC stale; Dynascale stale + sustained-quiet)

Heat changes written: 5
  Hot/Warm -> cooler: 1 (Dynascale Cool -> Cold)
  Cool/Cold -> hotter: 4 (H5, Gigabit Fiber, Wisper ISP, HTC - open-deal driven)
  Heat writes on target-account records (not skipped): 1 (H5 Data Centers)

Heat distribution after this run (all active ICP):
  Hot: 41
  Warm: 50
  Cool: 101
  Cold: 2670

Manual override skips (hs_is_target_account=true, would-change tier only): 78 (of 351 target accounts)
Stale signal modifier fired: 90 records (2 produced a net tier write; the rest were already at the decayed tier, target-frozen, or clamped)
Sustained-quiet modifier fired: 65 records (1 produced a net tier write - Dynascale)
Open-deal modifier (-1 tier) carried by: 20 records (3 produced a net new tier write; 7 target-frozen at computed/current; 10 already at adjusted tier)

Top tier changes:
1. HTC / Horry Telephone Cooperative (Fiber / Municipal-Cooperative): T4 -> T3 -- open deal
2. Gigabit Fiber (Fiber / Regional CLEC): T3 -> T2 -- open deal
3. Wisper ISP (Fiber / Regional CLEC): T3 -> T2 -- open deal
4. Dynascale (MSP / Cloud+Telecom Hybrid): T3 -> T4 -- stale + sustained-quiet
5. RadiusDC (Colo / AI Signals): T1 -> T2 -- stale

Top heat changes:
1. H5 Data Centers (Colo, target): Cool -> Hot -- open deal (tier frozen, heat truthful)
2. Gigabit Fiber (Fiber): Cold -> Hot -- open deal
3. Wisper ISP (Fiber): Cold -> Hot -- open deal
4. HTC (Fiber): Cold -> Hot -- open deal
5. Dynascale (MSP): Cool -> Cold -- 181d crossed 180d boundary

Unknown (segment, sub-segment) pair warnings: 6 (segment null fallback applied, no forced tier write - all computed == current):
  - Kordia (251536944849) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Trans Pacific Networks / TPN (318106540781) | Fiber Operator + Subsea cable operator
  - Grupo GTD Chile (319135939295) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Gtd Colombia (326165246700) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - WiLine Networks (326183183051) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  - Gtd Peru (326259427057) | Network Operator(Tier 1 / VNO) + Regional CLEC - Fiber operator
  (Cross-segment mismatches; D7 / Cooper data-quality follow-up. Not the 5 known MSP-on-colo pairs.)

Quality checks: all 10 changes written (5 tier + 5 heat), 0 failed; every change has an associated HubSpot company note (note IDs 375203798724 / 375253784271 / 375253984980 / 375264377586 / 375264565999 / 375264656099); 0 tier writes on target accounts (78 would-change records frozen); circuit breaker computed at 10% of 2862 = 286. No connector-dropout signature (signal-date population 243 matches independent count; heat distribution healthy). last_enriched_date NOT bumped (tier/heat-only writes per Unified Stamping Policy).

Next run: 2026-06-12 3:00 PM CT
