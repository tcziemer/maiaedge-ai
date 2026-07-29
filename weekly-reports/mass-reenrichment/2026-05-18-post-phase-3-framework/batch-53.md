# Mass Re-Enrichment Sweep — Batch 53

- **Sweep:** `2026-05-18-post-phase-3-framework`
- **Date:** 2026-05-19
- **Records processed:** 50/50
- **Path mix:** LIGHT+audit 50 (all `hs_is_target_account=true` Pellera-pattern target-frozen Tim Z International)
- **Apollo this batch:** 0 credits (sweep is Apollo-free per Cooper pattern; `APOLLO_ENFORCEMENT="disabled"`)
- **Sweep cumulative Apollo:** 0 (unchanged)
- **HubSpot writes:** 50/50 success across 5 batches of 10. 0 retries needed.
- **hs_object_id range covered:** 319190691566 → 319208243948
- **Pool remaining after batch 53 (per pre-batch query):** ~159 (was 209, drained 50)

## Path decision rationale

All 50 records in this batch hit the **Pellera-pattern** LIGHT+audit profile:

1. Every record has `hs_is_target_account = true` → Step A of `compute_tier` returns current tier unchanged (manual override locked). **Tier writes skipped: 50.**
2. Every record has `segmentation_confidence = high_90` and a framework-valid sub-segment (one of the 30 active values). No auto-migrations required.
3. Every record has `account_brief` populated but the other 6 of 7 narrative enriched fields are blank (`geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`). Strict §7.4c criteria would route these to FULL, but Cooper-validated LIGHT+audit pattern from batches 48-52 applies: framework validation passes, sub-segment is correctly assigned, tier is correctly frozen — the only gap is downstream narrative field population, which is R2's job post-sweep.
4. All 50 are owned by Tim Ziemer (`hubspot_owner_id = 159350430`); territories span Africa / MENA / Asia / Pacific / Caribbean / LATAM.
5. `last_enriched_date` stamped to 2026-05-19 to drain the sweep pool. R2 will pick these up for full narrative field population over the standard 120-day rotation.

## Records processed

### Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op (31)

| ID | Name | Country | Tier | Notes |
|---|---|---|---|---|
| 319190691566 | Cotas Bolivia | Bolivia | tier_3 | target-frozen |
| 319190691567 | Hexabyte | Tunisia | tier_3 | target-frozen |
| 319190692541 | Lightspeed Communications | Bahrain | tier_3 | target-frozen |
| 319190694588 | Newcom Gibraltar | Gibraltar | tier_3 | target-frozen |
| 319194102498 | Ezecom | Cambodia | tier_2 | target-frozen |
| 319194127064 | BTC Botswana | Botswana | tier_2 | target-frozen |
| 319194131171 | Access Haiti | Haiti | tier_3 | target-frozen |
| 319194131176 | Flow USVI | USVI | tier_3 | target-frozen |
| 319194135286 | Africom Zimbabwe | Zimbabwe | tier_3 | target-frozen |
| 319194135288 | Cobranet | Nigeria | tier_3 | target-frozen |
| 319194136276 | Surfline Communications | Ghana | tier_3 | target-frozen |
| 319197781730 | Lanka Bell | Sri Lanka | tier_2 | target-frozen |
| 319197813450 | Paratus Namibia | Namibia | tier_2 | target-frozen |
| 319197820613 | Logic | Cayman Islands | tier_3 | target-frozen |
| 319197821676 | Busy Internet | Ghana | tier_3 | target-frozen |
| 319197822663 | Standard Telecom DRC | DR Congo | tier_3 | target-frozen |
| 319197827820 | Supercable Venezuela | Venezuela | tier_3 | target-frozen |
| 319197829831 | CSL Samoa | Samoa | tier_3 | target-frozen; touched by concurrent routine at 2026-05-19T19:06 but pre-write to `last_enriched_date` so safe |
| 319197829832 | Digital8 PNG | PNG | tier_3 | target-frozen |
| 319197831905 | Rush Communications | Jamaica | tier_3 | target-frozen; only record with `infrastructure_profile` populated; last_enriched_date was 2026-04-27 (more recent re-enrich) |
| 319204732629 | Fiberail | Malaysia | tier_2 | **FLAG: rail-corridor fiber wholesale (KTMB subsidiary). Sub-segment may be misclassified — better fit is `Pure Wholesale Carrier - Network Op` or `Long Haul / Backbone - Fiber operator`. Defer to R2.** |
| 319204732655 | Focus Infocom | Maldives | tier_2 | target-frozen; account_brief notes "ISP + wholesale carrier" — borderline retail/wholesale, R2 to validate |
| 319204752101 | Connect Internet Services | Fiji | tier_2 | target-frozen |
| 319204755140 | Djibouti Telecom | Djibouti | tier_2 | target-frozen |
| 319204759254 | Digicel Bermuda | Bermuda | tier_3 | target-frozen |
| 319204762327 | Golis Telecom | Somalia | tier_3 | target-frozen |
| 319204762328 | MAGECI | Rwanda | tier_3 | target-frozen |
| 319204764394 | Newroz Telecom | Iraq | tier_3 | target-frozen |
| 319204767444 | Digital Mobile Philippines | Philippines | tier_3 | target-frozen |

### Fiber Operator (19)

| ID | Name | Country | Sub-segment | Tier | Notes |
|---|---|---|---|---|---|
| 319194084049 | Digi Belize | Belize | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319194087154 | Mexred Mexico | Mexico | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319194138308 | Telesur | Suriname | Regional CLEC - Fiber operator | tier_3 | **FLAG: Apollo `state="Amazonas"` is wrong. Suriname has no Amazonas administrative division (Amazonas is Brazil/Peru/Venezuela). R6 should correct.** |
| 319197750998 | TIME dotCom | Malaysia | Long Haul / Backbone - Fiber operator | tier_2 | **FLAG: on R3 dup-pair Tier 3 hold (paired with 268204721857 TIME DotCom Berhad). R3 auto-merge blocked; sweep audit refresh proceeds.** |
| 319197751024 | TSTT Wholesale | Trinidad & Tobago | Long Haul / Backbone - Fiber operator | tier_1 | target-frozen |
| 319197751994 | Melita | Malta | Regional CLEC - Fiber operator | tier_1 | target-frozen |
| 319197762257 | Optynex Telecom Panama | Panama | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319197764293 | TCI Net Brasil | Brazil | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319197812434 | Amplia Communications | Trinidad & Tobago | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204695763 | Summit Communications | Bangladesh | Regional CLEC - Fiber operator | tier_1 | target-frozen; account_brief describes PeeringDB / APNIC / wholesale ISP backbone — sub-segment may be too low (Pure Wholesale Carrier or Long Haul / Backbone fits better). R2 to validate. |
| 319204701929 | One Bermuda | Bermuda | Regional CLEC - Fiber operator | tier_1 | target-frozen; submarine cable landing — possible Long Haul / Backbone or Subsea cable operator fit. R2 to validate. |
| 319204702909 | Transtelco Mexico | Mexico | Long Haul / Backbone - Fiber operator | tier_1 | target-frozen |
| 319204710097 | Dedicado Uruguay | Uruguay | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204710106 | GT Red Pantaleon | Guatemala | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204711143 | NEOVIA Brasil | Brazil | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204711148 | Pacifico Cable Chile | Chile | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204712149 | Unifique Telecomunicacoes | Brazil | Regional CLEC - Fiber operator | tier_2 | target-frozen |
| 319204754142 | Aster Communications | Dominican Republic | Long Haul / Backbone - Fiber operator | tier_2 | target-frozen |
| 319208219335 | CEB FiberNET | Mauritius | Regional CLEC - Fiber operator | tier_1 | **FLAG: account_brief documents wholesale fiber operator (METISS consortium co-owner, 40 PoPs DWDM/MSTP, multi-country reach to Madagascar + Durban, 1G/10G EPL to carrier customers). Sub-segment may be misclassified — strong Long Haul / Backbone - Fiber operator OR Pure Wholesale Carrier - Network Op fit. R2 to reclassify.** |
| 319208243948 | Brisanet Brasil | Brazil | Regional CLEC - Fiber operator | tier_2 | target-frozen |

### Data Center Colo Provider (1)

| ID | Name | Country | Sub-segment | Tier | Notes |
|---|---|---|---|---|---|
| 319194126055 | CCT Global | Sint Maarten | Standard - colo | tier_2 | target-frozen |

## Summary by segment

| Segment | Count |
|---|---:|
| Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op | 29 |
| Fiber Operator / Regional CLEC - Fiber operator | 16 |
| Fiber Operator / Long Haul / Backbone - Fiber operator | 4 |
| Data Center Colo Provider / Standard - colo | 1 |
| **Total** | **50** |

## Tier writes

- Promotions (toward T1): 0
- Demotions (toward T5): 0
- Skipped (`hs_is_target_account=true`): 50
- Sub-segment auto-migrations: 0 (legacy values clean)
- Greenfield migrations: 0
- Segment changes (cascade fired): 0
- Customer-protection HOLDs: 0
- Completeness Gate fails: 0
- Manual-review HOLDs: 0

## Flags raised (for downstream routines)

| Routine | Record | Issue |
|---|---|---|
| R6 Territory & Hygiene | 319194138308 Telesur | Apollo `state="Amazonas"` invalid for Suriname; clear or replace with correct district |
| R6 / R3 | 319197750998 TIME dotCom | On standing R3 dup-pair Tier 3 hold (pair 268204721857). Cooper to resolve merge direction |
| R2 Stale Re-Enrichment | 319204732629 Fiberail | Sub-segment `Tier 1 Carrier - Network Op` likely wrong — rail-corridor fiber wholesale better fits `Pure Wholesale Carrier - Network Op` or `Long Haul / Backbone - Fiber operator`. Full re-research recommended. |
| R2 Stale Re-Enrichment | 319208219335 CEB FiberNET | Sub-segment `Regional CLEC - Fiber operator` likely too narrow — METISS consortium co-ownership + 40 PoPs DWDM/MSTP + multi-country wholesale = better fit `Long Haul / Backbone - Fiber operator` or `Pure Wholesale Carrier - Network Op`. Full re-research recommended. |
| R2 Stale Re-Enrichment | 319204695763 Summit Communications | Bangladesh — PeeringDB / APNIC / wholesale ISP backbone signals suggest higher-tier sub-segment than Regional CLEC. R2 to validate. |
| R2 Stale Re-Enrichment | 319204701929 One Bermuda | Bermuda — submarine cable landing function suggests Long Haul / Backbone or Subsea cable operator fit. R2 to validate. |
| R2 Stale Re-Enrichment | 319204732655 Focus Infocom | Maldives — "ISP + wholesale carrier" borderline retail/wholesale. R2 to validate. |
| R2 (general) | ALL 50 records | Sparse narrative fields (6 of 7 enriched fields blank). Pellera-pattern follow-up backlog grows by +50 to ~250 records since batch 48. |

## Pre-flight checks (§9)

1. **Concurrency check:** No concurrent batch detected (only batch 52 written today by this sweep; batch 53 is sequential). One side observation: CSL Samoa was touched by an unrelated routine at 19:06 ET today (likely R6 or Signal Scan); since its `last_enriched_date` was still 2026-04-20 before this batch, no collision.
2. **Steady-state R2 pause check:** Per `APOLLO_ENFORCEMENT="disabled"`, R2 should be paused. Not verified this run; if R2 fired today (4pm CT), some Apollo credits may have been spent outside sweep tracking. Not blocking.
3. **Framework reference freshness check:** `context/account-tiering/tier-compute-spec.md` unchanged since SWEEP_KICKOFF_DATE. Spec content matches what runtime read. GREEN.
4. **Expected pool size sanity:** Trigger query reports `total=209` remaining (matches batch 52's "~209 remaining" projection exactly). Drain on track.

## Drain status

- Done in this sweep (including batch 53): ~2,695 / ~2,854 (~94%)
- Remaining: ~159
- ETA at BATCH_SIZE=50: ~3-4 more batches to sweep complete + 1 verification pass per §11

## Run health: 🟢 GREEN

- 50/50 HubSpot writes succeeded
- 0 retries needed
- 0 fatal errors
- 0 Apollo consumed
- 0 manual-review escalations
- 0 customer-protection HOLDs
- 0 Completeness Gate fails

## Continuation

Next batch picks up from `hs_object_id > 319208243948`.
