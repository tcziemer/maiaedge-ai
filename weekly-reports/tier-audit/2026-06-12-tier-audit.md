## R-Tier-Audit 2026-06-12

- Total active accounts reviewed: 2862
- Tier changes written: 2
- Heat changes written: 0
- Manual override skips (tier writes only): 79
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (0.07% of 2862, threshold 10%)

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 254331348701 | sttelemediagdc.com | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_2 | tier_3 | +1 | Default T1, stale +1, sustained quiet +1 = T3 (event >180d, no engagement <=180d) |
| 321479592663 | worldpay.com | Enterprise-CustomerSegment | Financial Services - Enterprise | tier_3 | tier_4 | +1 | Default T3, stale +1 = T4 (event >90d, no engagement <=30d) |

### Per-record heat changes

(none - heat fully aligned with compute across all 2862 active records)

---

R-Tier-Audit - 2026-06-12 (daily M-F)

Total active accounts reviewed: 2862

Tier changes written: 2
  Promotions (toward Tier 1): 0
  Demotions (toward Tier 5): 2

Heat changes written: 0
  Hot/Warm -> cooler: 0
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 0

Heat distribution after this run (across all active ICP):
  :red_circle: Hot: 41
  :large_orange_circle: Warm: 50
  :large_yellow_circle: Cool: 101
  :white_circle: Cold: 2670

Manual override skips (hs_is_target_account=true, tier only): 79
Stale signals decayed (+1 tier): 93 (records meeting stale condition; 2 produced a tier change this run)
Sustained quiet decayed (+1 tier additional): 70 (records meeting condition; folded into the 93 stale set)
Open-deal promotions (-1 tier): 20 (active-ICP records with an open deal past appointmentscheduled)

Top tier changes by delta:
1. STTELEMEDIA Global Data Centres (Data Center Colo Provider): T2 -> T3 -- stale +1, sustained quiet +1 (180d boundary crossed)
2. Worldpay (Enterprise-CustomerSegment): T3 -> T4 -- stale +1 (90d boundary crossed)

Unknown (segment, sub-segment) pair warnings: 6 (using segment null fallback per tier-compute-spec §6)
  - Kordia (251536944849): Network Operator(Tier 1 / VNO) / Regional CLEC - Fiber operator
  - Trans Pacific Networks TPN (318106540781): Fiber Operator / Subsea cable operator
  - Grupo GTD Chile (319135939295): Network Operator(Tier 1 / VNO) / Regional CLEC - Fiber operator
  - Gtd Colombia (326165246700): Network Operator(Tier 1 / VNO) / Regional CLEC - Fiber operator
  - WiLine Networks (326183183051): Network Operator(Tier 1 / VNO) / Regional CLEC - Fiber operator
  - Gtd Peru (326259427057): Network Operator(Tier 1 / VNO) / Regional CLEC - Fiber operator
  NOTE: These are a NEW data-quality cluster distinct from the 5 known MSP/colo pairs in CLAUDE.md
  (the Gtd Latin-America NetworkOp/Fiber-CLEC cross-pairing + TPN Fiber/Subsea). Logged for
  Cooper's data-quality follow-up; null fallback applied, no tier mistakes.

Quality checks:
  1. All eligible records processed: 2862 reviewed == 2862 loaded. PASS
  2. No tier writes on hs_is_target_account=true: 79 target-account tier deltas all skipped. PASS
  3. All tier writes have HubSpot notes: 2 notes created (375461151435, 375440997110). PASS
  4. Circuit breaker threshold == 10%: computed 0.07% < 10%. PASS
  5. Local audit log persisted: this file. PASS

Apollo budget: 0 (pure HubSpot read/compute/write).
Next run: 2026-06-15 3pm CT (Mon; daily M-F cadence).
