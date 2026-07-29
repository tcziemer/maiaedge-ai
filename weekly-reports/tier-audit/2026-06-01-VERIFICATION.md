# R-Tier-Audit VERIFICATION (CORRECTED READ-ONLY RE-RUN) - 2026-06-01 (Mon)

**STATUS: PAUSED. NO HUBSPOT WRITES. NO SLACK. READ-ONLY.**
**Agent:** a67e18956c99d9bd2 (continuation of paused run)

## Verdict
Fixing the engagement proxy alone did **NOT** restore normal drift. A **second connector regression** was found this session: `last_signal_date` / `last_signal_score` / `signal_count_last_30d` are dropped by the HubSpot MCP connector on ~93% of records, exactly like `notes_last_activity_date` was. With `last_signal_date` null pool-wide, the stale modifier's first clause `(last_signal_date is None OR >90d)` is universally satisfied, so stale(+1) fires anywhere the engagement proxy is also stale/dropped. **This is a field-access artifact, not real drift. The run stays paused.**

## Proxy-population diagnostic (the engagement-proxy fix DID partially work)
| Field | Populated | Rate | Note |
|---|---|---|---|
| `notes_last_updated` (new primary proxy) | 1540/2559 | **60.2%** | Was 0% via `notes_last_activity_date` last run. Proxy now returns. |
| `hs_last_sales_activity_timestamp` (fallback proxy) | 155/2559 | 6.1% | Thin; fallback only. |
| `notes_last_activity_date` (last run's proxy) | 0/2559 | 0.0% | Confirmed still dropped - the original regression. |
| `last_signal_date` (stale/quiet first-clause anchor) | 187/2559 | **7.3%** | **NEW regression found.** Spot-checked Arvig (194004502229): `recent_news_or_trigger_event` + `signal_heat=Hot` present, but `last_signal_date`/`last_signal_score`/`signal_count_last_30d` absent from response. Drop correlated with heat=Cold; the 187 that return are genuinely-fresh Signal-Scan-touched records. |

**Why drift is still high:** stale(+1) fired 1472x and quiet(+1) 1039x almost entirely because `last_signal_date` came back null, NOT because engagement is genuinely cold. Of 1312 demotions, 1269 had `last_signal_date` null (artifact-suspect) and only 43 had a real present-but-old signal date. The demotion pool's engagement-proxy population is just 30.2% (vs 60.2% pool-wide) - the proxy drop is biased toward exactly the records being demoted.

## Circuit breaker (corrected run)
- Total active ICP reviewed: **2559**
- Proposed changes (tier OR heat union): **1324**
- Threshold (10% of 2559): **255** (trigger spec cites 257)
- Change rate: **51.74%** -> EXCEEDS 10% -> **PAUSED**
- (Paused run was 84.87%; corrected run is 51.74% - improved by the proxy fix but still artifact-dominated by the `last_signal_date` drop.)

## Breakdown (held, not written)
- **tier_changes_total: 1319** (promotions 7 / demotions 1312)
- **heat_changes_total: 9** (hotter 7 / cooler 2)
- **stale(+1) fired: 1472**
- **sustained_quiet(+1) fired: 1039**
- **open_deal_promotion (proxy = num_associated_deals>0): 23**  _(caveat: this read-only proxy is broader than the spec's 'deal past appointmentscheduled, not closed'; some Hot-via-open-deal may be over-counted. The real run resolves deal stage via association lookup.)_
- **manual_override_skips (hs_is_target_account=true): 323**
- **unknown_pair_warnings: 1**
- **heat_distribution_after: {'Hot': 41, 'Warm': 25, 'Cool': 75, 'Cold': 2418}**

## Top 10 tier changes (held)
| Company | Segment | Change | Reason |
|---|---|---|---|
| 1025Connect (Long Island Interconnect) | Data Center Colo Provider | tier_3 -> tier_5 | base tier_3; stale(+1), quiet(+1) |
| 1Route Group, LLC | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |
| 2pifi | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |
| 3DS Communications | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |
| 42com International LTD. | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |
| 5G Networks Ltd | Data Center Colo Provider | tier_3 -> tier_5 | base tier_3; stale(+1), quiet(+1) |
| ASAL Comunicaciones SA de CV | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |
| ATCDC (Ashland Technology Complex) | Data Center Colo Provider | tier_3 -> tier_5 | base tier_3; stale(+1), quiet(+1) |
| ATLDC / Tulix Systems | Data Center Colo Provider | tier_3 -> tier_5 | base tier_3; stale(+1), quiet(+1) |
| Accel Net | MSP/Aggregator | tier_2 -> tier_4 | base tier_2; stale(+1), quiet(+1) |

### All promotions (7 - mostly legitimate, open-deal / hot / stacked driven)
| Company | Segment | Change | Reason |
|---|---|---|---|
| IENTC Telecom | Fiber Operator | tier_2 -> tier_1 | base tier_2; opendeal(-1) |
| vyvebb | Fiber Operator | tier_3 -> tier_2 | base tier_3; stacked(-1) |
| TDS Telecom | Fiber Operator | tier_4 -> tier_3 | base tier_3; no modifiers |
| Summit Broadband | Fiber Operator | tier_3 -> tier_2 | base tier_3; opendeal(-1) |
| Smart City Telecom | Fiber Operator | tier_3 -> tier_2 | base tier_3; hot(-1) |
| CMC Networks | Fiber Operator | tier_3 -> tier_2 | base tier_3; opendeal(-1) |
| TEC | Fiber Operator | tier_3 -> tier_2 | base tier_3; hot(-1) |

## Top 10 heat changes (held)
| Company | Segment | Change | Detail |
|---|---|---|---|
| AlasConnect | MSP/Aggregator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| CMC Networks | Fiber Operator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| IENTC Telecom | Fiber Operator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| NTT Global Networks | MSP/Aggregator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| South Front Networks | Fiber Operator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| Summit Broadband | Fiber Operator | Cold -> Hot | lsd=None lss=None cnt30=0 opendeal=True |
| vyvebb | Fiber Operator | Warm -> Hot | lsd=2026-05-18 lss=12.0 cnt30=2.0 opendeal=False |
| Granite State Communications | Fiber Operator | Warm -> Cool | lsd=2026-04-21 lss=14.0 cnt30=1.0 opendeal=False |
| Sonic Telecom | Fiber Operator | Warm -> Cool | lsd=2026-05-18 lss=12.0 cnt30=1.0 opendeal=False |

## Required fix before any write-enabled re-run
1. **Both regressions are connector field-access artifacts, not data problems.** Re-authorize / refresh the HubSpot MCP connector so it surfaces `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, AND `notes_last_activity_date`. Confirm `last_signal_date` returns non-null on a known-fresh record (Arvig 194004502229 - live `recent_news_or_trigger_event`, `signal_heat=Hot`).
2. Until the connector returns `last_signal_date`, the stale/quiet modifiers cannot be evaluated truthfully and R-Tier-Audit MUST stay paused - writing these 1324 changes would corrupt the active ICP tier pool by mass-demoting toward the floor.
3. The 7 promotions + the 9 heat changes are likely legitimate but are held with the paused batch (do not cherry-pick writes from a paused run).

## Full proposed-change list (1324 records, held - NOT written)
Persisted to `2026-06-01-VERIFICATION-proposed-changes.csv` alongside this file.

_Full computed record set at /tmp/recompute_out.json in the sandbox. Nothing written to HubSpot; no Slack sent._