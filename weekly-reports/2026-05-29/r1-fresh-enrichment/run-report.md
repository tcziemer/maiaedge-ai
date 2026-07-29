# R1 Fresh Enrichment - Run Report 2026-05-29 (Friday)

**Execution:** Cowork scheduled task. Run health: **GREEN** (pool drained to steady state).

## Pool
- Trigger query (5 filter groups) raw candidates: **8**
- Tier 3 client-side exclusions (verified per-ID against canvas F0B0AFSB9LN R0/R1/R2 sections): **7**
- Net processed: **1**
- Dynamic cap: 100 (total_candidates <= 200)
- Apollo: 0 credits used (sub-cap 30). Weekly W22: 0/850, 850 remaining. Monthly Apollo balance: 8,812 remaining.

## Tier 3 exclusions (standing holds, not re-processed)
| Account | HubSpot ID | Standing hold origin |
|---|---|---|
| columbus-networks (finetechnologies.co) | 324597786339 | R0 + R1 2026-05-27 MISDOMAIN/RENAMABLE ambiguity (Columbus Networks -> Liberty Networks rebrand vs unrelated FL MSP) |
| GATCO (gatco.net) | 324524875475 | R1 2026-05-26 no public identification (India) |
| Synnap (synnap.io) | 324498712298 | R1 2026-05-26 aspirational sovereign-AI claims unverified |
| Spartan Data Centers (spartandc.com) | 324535363289 | R1 2026-05-26 no public info / stealth |
| Attobahn, Inc. (attobahn.com) | 324610914007 | R1 2026-05-26 pseudoscientific claims, no operational network |
| Broadstar (gigabitfiber.com) | 323981908725 | R1 2026-05-22 duplicate of Gigabit Fiber (193867595510) + name mismatch, R3 queue |
| Tract Capital (tractcapital.com) | 321983866611 | R1 2026-05-08 duplicate of Tract (264635347666), R3 queue |

## Processed (1)
**ResetData** (324591600333) - Australia NeoCloud. **Path beta NO-OP (frozen tier).**
- Already fully classified: `customer_segment = NeoCloud`, `company_sub_segment = Sovereign AI Clouds - Neocloud`, `segmentation_confidence = high_90`, all 7 enriched fields populated, owner Tim Ziemer (International, correct), `last_enriched_date = 2026-05-26`, `signal_heat = Cold`.
- Gap that put it in the trigger query: `account_tier` is BLANK -> matches Filter Group B2 (`account_tier NOT_HAS_PROPERTY`).
- `hs_is_target_account = true` -> compute_tier returns at Step A (manual override). Tier write is skipped per inviolable rule. No other field gap exists.
- **Outcome:** no write, no `last_enriched_date` bump, no `signal_heat` touch (Path beta does not own heat). 0 Apollo.

### Recurring loop (escalation)
ResetData has now no-op'd on 2026-05-28 and 2026-05-29 (and surfaced again in R6 2026-05-29 as a frozen-tier territory note). Root cause: `account_tier` is empty while `hs_is_target_account = true`, so the freeze rule blocks the algorithm from ever populating tier, and B2 re-catches it daily. **Cooper action needed:** either (a) set `account_tier` manually on ResetData, or (b) clear `hs_is_target_account` so the algorithm assigns the Sovereign AI Clouds default (tier_1). Until then it will reappear in every R1 trigger query as a harmless no-op.

## End-of-pipeline self-checks
0 records written this run -> checks 1-4 (sub-segment nullness, confidence-evidence alignment, disqualifier audit, catch-all guard) all vacuously PASS.

## Writes
0 HubSpot writes · 0 evictions · 0 new Tier 3 holds · 0 segment changes.
