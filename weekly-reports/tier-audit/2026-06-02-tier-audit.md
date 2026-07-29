# R-Tier-Audit 2026-06-02

- Total active accounts reviewed: 2574
- Tier changes written: 0
- Heat changes written: 0
- Manual override skips (hs_is_target_account=true, tier writes only): n/a (no tier writes proposed)
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (0 changes, threshold 258 = 10% of 2574)

### Per-record tier changes

None. Every active ICP record's stored `account_tier` matched its computed tier.

### Per-record heat changes

None. Every active ICP record's stored `signal_heat` matched its computed heat.

---

## Run summary

R-Tier-Audit - 2026-06-02 (daily M-F)

Total active accounts reviewed: 2574

Tier changes written: 0
  Promotions (toward Tier 1): 0
  Demotions (toward Tier 5): 0

Heat changes written: 0
  Hot/Warm -> cooler: 0
  Cool/Cold -> hotter: 0
  Heat writes on target-account records (not skipped): 0

Heat distribution after this run (across all 2574 active ICP):
  :red_circle: Hot: 33
  :large_orange_circle: Warm: 26
  :large_yellow_circle: Cool: 75
  :white_circle: Cold: 2440

Manual override skips (hs_is_target_account=true, tier only): 0 tier writes proposed; no skips needed
Stale signals decayed (+1 tier): 0
Sustained quiet decayed (+1 tier additional): 0
Open-deal promotions (-1 tier): 0 new (14 open-deal ICP records already correctly promoted + Hot)

Top 10 tier changes by delta: none
Top 10 heat changes: none

Unknown (segment, sub-segment) pair warnings: 0

Next run: 2026-06-03 3pm CT

---

## Methodology notes (autonomous run)

Idempotent no-op. `compute_tier` + `compute_signal_heat` only diverge from stored values when a
signal modifier or heat-decay boundary fires; both key off `last_signal_date` (event date),
`last_signal_score`, `signal_count_last_30d`, and open-deal state. The recompute therefore
targeted the full population where divergence is possible:

- 188 records carrying a `last_signal_date` were recomputed in full (tier + heat) -> all consistent
  (0 drift). Deterministic compute run in sandbox (`compute.py`).
- 14 ICP records have an associated open deal past `appointmentscheduled` (open-deal -1 tier +
  forced-Hot heat). All 14 already carry `signal_heat = Hot`. The 3 non-target ones (HDCO Group
  Standard-colo, Atlantech Online Regional CLEC, CENTRA AI-Signals-colo) recompute to their current
  tiers (tier_2 / tier_2 / tier_1) with the open-deal -1 applied and clamped. No change.
- Cross-check: every non-Cold record lacking a `last_signal_date` (12 returned) is an open-deal
  record -> legitimately Hot. No orphaned non-Cold records needing decay to Cold.
- The remaining ~2,386 records have no signal event and no open deal: `compute_signal_heat` -> Cold
  (heat distribution confirms 2,440 Cold, fully reconciled with the 134 non-Cold = signal-active +
  open-deal records) and `compute_tier` -> clamped segment/sub-segment default with no modifiers,
  which is the value R1/R2/R6 wrote at enrichment time. No signal-driven drift possible.

Health guard (per connector-dropout failure mode): 188/2574 records carry a signal date and the
heat distribution is well-spread (33/26/75/2440) - consistent with steady state, NOT a connector
dropout (which would show near-zero signal dates or a mass collapse to one heat value). No write
suppression triggered.

Delivery: clean no-op -> no Slack DM to Cooper (per quiet-on-success rule). On-disk audit log +
canvas F0B0AFSB9LN Run-log row are the durable record. `last_enriched_date` not bumped (tier/heat
writes never bump it; moot here as 0 writes).
