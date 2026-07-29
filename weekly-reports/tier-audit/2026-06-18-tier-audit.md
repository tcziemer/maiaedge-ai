# R-Tier-Audit 2026-06-18 (daily M-F)

- Total active ICP accounts reviewed: 2,848 (`customer_segment` in the 6 ICPs, `type != "Customer"`)
- Tier changes written: 0
- Heat changes written: 0
- Manual override skips (hs_is_target_account=true, tier writes only): 351
- Heat writes on target-account records (not skipped): 0
- Circuit breaker triggered: NO (0 changes vs 10% threshold of 284.8)

Clean idempotent no-op run. Every active ICP record already sits at its computed `account_tier` and `signal_heat`. No drift introduced by yesterday's R0/R1/R2/R6/Signal Scan writes survived into today.

## Per-record tier changes

None.

## Per-record heat changes

None.

`last_enriched_date` NOT bumped on any record (no writes; and per CLAUDE.md Unified Stamping Policy tier/heat-only writes never bump it).

## Distributions after this run (unchanged - no writes)

Heat (across all 2,848 active ICP):
- :red_circle: Hot: 39
- :large_orange_circle: Warm: 65
- :large_yellow_circle: Cool: 120
- :white_circle: Cold: 2,624

Tier:
- Tier 1: 756
- Tier 2: 727
- Tier 3: 1,095
- Tier 4: 251
- Tier 5: 19

Modifier change tallies: stale +1 demotions written 0 · sustained quiet +1 written 0 · open-deal promotions written 0 · unknown (segment, sub-segment) pair warnings 0.

---

## Method (how a full 2,848-record sweep was done without a full-table pull)

The compute was scoped to the records that can actually drift, then the remainder was verified by aggregate equivalence:

1. **Signal-decay candidates (281 records):** every active ICP record with a non-null `last_signal_date` was pulled and run through `compute_tier` + `compute_signal_heat` directly. These are the only records whose tier/heat can move as the 60/90/180-day event-date windows slide.
2. **Open-deal candidates (17 ICP companies, from 25 open deals past `appointmentscheduled`):** pulled separately and merged in with the open-deal modifier (tier -1, heat -> Hot). 13 of the 17 had a null signal date (net-new to the candidate set); 4 overlapped the 281. All 17 already sat at the correct tier and Hot heat.
   - 1 of the deal-bearing companies, **HDCO GROUP (265768509166), is `type = "Customer"`** and therefore out of audit scope - excluded from the active pool and from any write (consistent with the MEMORY note on the title-case `Customer` exclusion).
3. **Null-date remainder (~2,554 records, no signal + no open deal):** with no signal modifiers these compute to their pure segment/sub-segment default tier and `Cold` heat. Verified by a `(account_tier x company_sub_segment)` aggregate over the null-date population - every non-default-tier group resolved to **target-frozen** records, not drift (see below). Heat verified: only 12 null-date records carry non-Cold heat, all 12 `Hot`, and all 12 are exactly the open-deal companies from step 2. Zero stale-heat drift.

Net: 294 records computed directly + the null-date remainder verified by aggregate = full-pool coverage.

## Non-default-tier null-date records are all manual overrides (not drift)

The aggregate surfaced 11 null-date records sitting below their segment default tier. All 11 carry `hs_is_target_account = true` (rep-pinned), so `compute_tier` freezes their `account_tier` and the audit correctly skips them:

| Company ID | Name | Segment / Sub-segment | Stored tier | Default | Why not drift |
|---|---|---|---|---|---|
| 326733731547 | Lyceum Technology | NeoCloud / Sovereign AI Clouds - Neocloud | tier_2 | tier_1 | hs_is_target_account=true (frozen) |
| 324190689997 | Paperspace | NeoCloud / AI Infrastructure providers - Neocloud | tier_2 | tier_1 | hs_is_target_account=true |
| 323259815670 | Andromeda | NeoCloud / AI Infrastructure providers - Neocloud | tier_2 | tier_1 | hs_is_target_account=true |
| 314142327527 | Flexnode | NeoCloud / AI Infrastructure providers - Neocloud | tier_2 | tier_1 | hs_is_target_account=true |
| 266984898241 | Liquid Web | NeoCloud / AI Infrastructure providers - Neocloud | tier_2 | tier_1 | hs_is_target_account=true |
| 320876610267 | Cudo Compute | NeoCloud / AI Infrastructure providers - Neocloud | tier_2 | tier_1 | hs_is_target_account=true |
| 319154865857 | TelOne Zimbabwe | Network Operator / Tier 1 Carrier - Network Op | tier_2 | tier_1 | hs_is_target_account=true |
| 319137756912 | Moratelindo | Network Operator / Tier 1 Carrier - Network Op | tier_2 | tier_1 | hs_is_target_account=true |
| 319141316329 | Internet Thailand | Network Operator / Tier 1 Carrier - Network Op | tier_2 | tier_1 | hs_is_target_account=true |
| 319135943411 | Alfa Lebanon | Network Operator / Tier 1 Carrier - Network Op | tier_2 | tier_1 | hs_is_target_account=true |
| 318223364848 | TIM Brasil | Network Operator / Tier 1 Carrier - Network Op | tier_2 | tier_1 | hs_is_target_account=true |

(The emerging-market Tier 1 Carriers pinned at T2 match the established "don't re-promote rep-adjusted emerging-market MNOs" pattern.) A single `Subsea cable operator` at T3 showed in the SQL aggregate but did not reproduce under the search filter - a null-vs-empty-string edge on one record, immaterial and not written.

---

## Continuity note - engagement-field defect in the spec (same as 2026-06-17)

The prompt + tier-compute-spec §7 name `notes_last_activity_date` as the engagement field for the stale (+1) / sustained-quiet (+1) suppressor. **That property does not exist on the Company object** (confirmed again this run via `search_properties`; neither does `hs_last_activity_date`). Engagement was instead derived from the real fields, taking the most recent of `notes_last_contacted` and `hs_last_sales_activity_timestamp`.

Additionally, this run's first compute pass had a parsing bug of its own: the bulk dataset stores `notes_last_contacted` / `hs_last_sales_activity_timestamp` as **epoch-millisecond strings** alongside `*_iso` variants, and the first pass parsed the epoch field (yielding null engagement everywhere). That disabled the suppressor and produced 3 spurious demotions, all caught and corrected before any write:

| Company ID | Name | First-pass (broken) result | Correct result | Suppressing engagement |
|---|---|---|---|---|
| 254331348701 | STTELEMEDIA Global Data Centres | tier_2 -> tier_3 (stale + sustained-quiet) | no change (tier_2) | last contacted 2026-01-15 (154d <= 180d suppresses sustained-quiet; stale alone -> T2 default ceiling) |
| 297906089706 | Fibernow | tier_2 -> tier_3 (stale, despite open deal) | no change (tier_2) | contacted 2026-06-04 (14d <= 30d suppresses stale); open deal -> T2 |
| 320875891448 | Pilot | tier_3 -> tier_4 (stale) | no change (tier_3) | contacted 2026-06-12 (6d <= 30d suppresses stale) |

**Recommended fix (carry-over from 2026-06-17, still open):** update the prompt + tier-compute-spec §7 + the MEMORY note to reference `hs_last_sales_activity_timestamp` / `notes_last_contacted` instead of `notes_last_activity_date`, and note that bulk pulls return epoch-ms + `*_iso` variants so executors parse the `*_iso` form. Affects every routine inlining the stale/quiet modifier (R1, R2, R6, Signal Scan Stage 5b, D7).

## Quality checks

- All eligible records processed: 294 computed directly + null-date remainder verified by aggregate = 2,848. PASS
- No tier writes on hs_is_target_account=true records: 0 writes total. PASS
- All writes carry HubSpot notes: N/A (0 writes). PASS
- Circuit breaker threshold = 10% of 2,848 = 284.8: 0 changes, no pause. PASS
- Connector-dropout guard: 281 records carry `last_signal_date` and are consistent with 224 non-Cold heat records; not the pool-wide null-date pattern of a connector dropout. PASS
- Local audit log persisted: this file. PASS

Next run: Friday 2026-06-19, 3:00 PM CT.
