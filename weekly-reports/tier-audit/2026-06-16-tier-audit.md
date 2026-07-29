# R-Tier-Audit 2026-06-16 (daily M-F)

- Total active accounts reviewed: 2850
- Tier changes written: 2
- Heat changes written: 2
- Manual override skips (tier writes only): 46
- Heat writes on target-account records (not skipped): 1
- Circuit breaker triggered: NO (4 changes vs 285 threshold = 0.14% of 2850)
- HubSpot writes: 4 field updates + 4 audit notes (0 failed)
- `last_enriched_date`: NOT bumped (tier/heat-only writes per Unified Stamping Policy)

## Method note

Active ICP non-customer pool = 2850 (Network Op 428, Colo 478, Fiber 1260, MSP 480, Enterprise 16, NeoCloud 188; 2 `type=Customer` excluded). `compute_tier` + `compute_signal_heat` (today=2026-06-16; windows 60d=2026-04-17, 90d=2026-03-18, 180d=2025-12-18, 30d=2026-05-17) were applied precisely to the 294 records that can deviate from the signal-quiet baseline: 281 signal-active (`last_signal_date` populated) + 16 open-deal-past-`appointmentscheduled` (4 overlap the signal-active set) + Verrus. The remaining 2556 signal-quiet, no-open-deal records were verified at their computed baseline (`account_tier` = segment default, `signal_heat` = Cold) via GROUP-BY aggregation + targeted drift pulls; every off-baseline candidate resolved to target-account freeze, open-deal correctness, unknown-pair fallback, or out-of-scope (Flagged/Customer) -> 0 changes in that population. Engagement read from `notes_last_contacted` / `hs_last_sales_activity_timestamp` (the live fields; `notes_last_activity_date` does not exist on COMPANY) and confirmed genuinely populated, not connector-dropped (161 ICP records carry sales-activity timestamps).

### Per-record tier changes

| Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
|---|---|---|---|---|---|---|---|
| 297906089706 | fibernow.com | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | tier_2 | -1 (promote) | Default T3; open deal past appointmentscheduled -1; rep engagement 2026-06-04 (12d) so stale did not fire = T2 |
| 320875891448 | pilotfiber.com | Fiber Operator | Regional CLEC - Fiber operator | tier_4 | tier_3 | -1 (promote) | Default T3; prior stale +1 cleared by rep engagement 2026-06-12 (4d, within 30d) = T3 |

### Per-record heat changes

| Company ID | Domain | Old Heat | New Heat | Reason |
|---|---|---|---|---|
| 300402851562 | comcast.com | Warm | Cool | last_signal_date (event) 2026-04-16 now 61d old, crossed 60d Warm window; score 27, no stack, no open deal. Tier frozen (hs_is_target_account=true); heat not frozen |
| 327822323424 | verrusdata.com | Cool | Cold | last_signal_date null, no open deal, no event in 180d -> Cold |

---

R-Tier-Audit - 2026-06-16 (daily M-F)

Total active accounts reviewed: 2850

Tier changes written: 2
  Promotions (lower tier number, toward Tier 1): 2
  Demotions (higher tier number, toward Tier 5): 0

Heat changes written: 2
  Hot/Warm -> cooler: 2
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 1

Heat distribution after this run (across all active ICP, non-customer):
  Hot: 39
  Warm: 65
  Cool: 121
  Cold: 2625

Manual override skips (hs_is_target_account=true, tier only): 46
  (target-account records in the computed set whose algorithmic tier differs from the pinned tier; tier write skipped, heat still recomputed)
Stale modifier fired (+1): 96 records in computed set (already at demoted/clamped tier -> 0 NEW demotions this run)
Sustained quiet modifier fired (+1 additional): 64 records in computed set (already clamped -> 0 NEW demotions)
Open-deal modifier fired (-1): 16 records (all ICP open-deal companies)

Top tier changes by delta:
1. Fibernow (Fiber Operator / Regional CLEC): T3 -> T2 -- open-deal -1, recent engagement (no stale)
2. Pilot (Fiber Operator / Regional CLEC): T4 -> T3 -- stale cleared by rep engagement within 30d

Top heat changes:
1. Comcast Business (Network Operator / Cable MSO Enterprise Division): Warm -> Cool -- event crossed 60d window (target account; heat not frozen)
2. Verrus (Data Center Colo Provider / Greenfield): Cool -> Cold -- signal-quiet, no open deal

Unknown (segment, sub-segment) pair warnings: 6
  (segment/sub-segment mismatch; tier resolved via segment null fallback and matched stored tier, so NO change. Data-quality items for R2/R6/D7 sub-segment correction, not R-Tier-Audit:)
  - WiLine Networks (326183183051), Gtd Peru (326259427057), Gtd Colombia (326165246700), Grupo GTD Chile (319135939295), Kordia (251536944849): customer_segment Network Operator(Tier 1 / VNO) carrying "Regional CLEC - Fiber operator" sub-segment -> Network Op null fallback T1 (== stored).
  - Trans Pacific Networks / TPN (318106540781): customer_segment Fiber Operator carrying "Subsea cable operator" sub-segment -> Fiber null fallback T3 (== stored).

Observations (out of scope this run, surfaced for Cooper's data-quality follow-up):
  - Several `Flagged for deletion` records carry stale high tiers (Dominica Telecom tier_1, Symbio tier_1, FirstLink tier_2, plus several tier_2 LATAM carriers). Non-ICP, so R-Tier-Audit does not touch them; clearing tier on flagged records could be folded into R4 / pre-deletion handling.

Next run: 2026-06-17 (Wed) 3:00 PM CT
