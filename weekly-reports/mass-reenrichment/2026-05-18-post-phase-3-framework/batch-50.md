# Mass Re-Enrichment Sweep — Batch 50

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 50
**Date:** 2026-05-19
**Records processed:** 50/50
**Path mix:** LIGHT 34 · MEDIUM 1 · LIGHT+audit 15 · HOLD 0
**Tier changes:** 1 (Liberty Networks T2 → T1 on framework reclass)
**Sub-segment / segment corrections:** 1 (Liberty Networks reclass)
**Apollo credits:** 0
**Last hs_object_id in batch:** 318231691997 (Telesol Group)

## Pre-flight

- Trigger query: customer_segment IN [6 active ICPs] AND hs_object_id GT 317223880415 AND (last_enriched_date LT 2026-05-18 OR NULL) AND type NEQ "CUSTOMER"; sort hs_object_id ASC; limit 50
- Pool total returned by HubSpot: **359** (matches continuation token from batch 49 exactly)
- Returned: 50 (clean alignment)
- Canvas F0B0AFSB9LN: **0 active Mass Re-Enrichment Sweep holds** (Cooper directive 2026-05-19 "no holds going forward; best-effort classify" still in effect). No concurrent batch detected.
- Apollo budget JSON: not updated (APOLLO_ENFORCEMENT=disabled per sweep params)
- Web searches: 0 total (all decisions made from existing enriched-field evidence + Phase 3 framework reference per CLAUDE.md op principle 3)

## Batch shape

- **By segment (pre):** 13 Fiber Operator + 3 Data Center Colo Provider + 3 NeoCloud + 5 Network Operator(Tier 1/VNO) + 26 MSP/Aggregator + 0 Enterprise.
- **By segment (post Liberty reclass):** 12 Fiber Operator + 3 DCCP + 3 NeoCloud + 6 Network Operator(Tier 1/VNO) + 26 MSP/Aggregator.
- **hs_is_target_account = true:** 7 records (Cirrascale, Inference.net, SBTS, ENTEL PERU, Orange España, Bayobab - MTN Digital Infrastructure, Teligent Telecom) — `account_tier` writes skipped on these per §8 hard stops
- **Open deals at contractsent+:** 0 records (no segment-write blocks fired)
- **Closed-won deals (customers):** 0 records (no customer-protection HOLDs)
- **Records with last_signal_score / last_signal_date populated:** 0 (no signal modifiers fire across batch — matches batch-49 pattern)

## MEDIUM corrections detail

### 1. Liberty Networks (317231076065) — segment + sub-segment reclass to N4 International Backbone Specialist
- **Before:** customer_segment=`Fiber Operator`, company_sub_segment=`Long Haul / Backbone - Fiber operator`, segmentation_confidence=`high_90`, account_tier=`tier_2`
- **After:** customer_segment=`Network Operator(Tier 1 / VNO)`, company_sub_segment=`International Backbone Specialist - Network Op`, segmentation_confidence=`medium_7089`, account_tier=`tier_1`
- **Reason:** Per `context/account-tiering/enrichment-protocols.md` §6 anchor verification (2026-05-14): "Liberty Networks REMOVED from N2 anchor list. Web verification confirms Liberty Networks (Liberty Latin America subsidiary) operates ~60,000 km of submarine + terrestrial fiber across 30+ countries in Latin America / Caribbean, with significant subsea ownership (MAYA-1.2 launched H1 2026). Per N2 tiebreaker ('subsea ownership AND international focus dominant -> International Backbone Specialist wins'), Liberty Networks correctly routes to **N4 International Backbone Specialist - Network Op**, not N2. Existing HubSpot Liberty Networks records should be re-classified at next R2 cycle."
- **Question pass:** N4.1 (HQ outside US, Caribbean/LatAm primary) PASS; N4.2 (MAYA-1.2 subsea owner, IRU positions on multiple cables) PASS; N4.3 (Route Miles Enterprise via 60K km submarine+terrestrial, POPs Large) PASS; N4.4 (international cross-border revenue dominant per LatAm/Caribbean footprint) PASS. 4 of 5 confirmed; anchor list does not yet name Liberty Networks (added via Phase 3 web verification, not the original anchor pool) → medium_7089 (not high_90) per file 06 §6.1 / D5 protocol N4.
- **Tier compute:** Default Network Operator(Tier 1 / VNO)/International Backbone Specialist - Network Op = T1, ceiling 1, floor 2. No signal modifiers fire. Net tier_1 (one-tier promotion from prior tier_2 Long Haul Backbone default). file 06 §6.1 / D5 protocol N4 / Operating Principle 2 (multi-marker classification).

## LIGHT+audit path follow-up flags

15 records flagged with 4+ core narrative fields missing — matching the Pellera (batch 48) and continuing pattern from batch 49. These got `last_enriched_date = 2026-05-19` LIGHT stamp + audit note here; defer to a proper R2 FULL re-enrichment outside this sweep window:

| ID | Name | Missing core fields | Notes |
|---|---|---|---|
| 317237932750 | Airtel Seychelles | geo, infra, prov, news, fabric | Sub: Regional CLEC - Fiber operator |
| 318051096311 | LARUS Limited | prov, news, fabric, hyper-OK | 3 core + fabric (Fiber ICP); near edge |
| 318051097277 | Cellfind (Pty) Ltd | prov, news, hyper-OK (MSP) | 2 core; not flagged actually |
| 318106540778 | FSG (First Sunrise Group) | prov, news (MSP — fabric+hyper expected blank) | 2 core; not flagged |
| 318106540783 | SBTS | geo, infra, prov, news, fabric (target=true) | tier-frozen; full R2 deferred |
| 318106540785 | ENTEL PERU | geo, infra, prov, news, fabric (target=true) | tier-frozen; full R2 deferred |
| 318106540787 | RouteTrust | geo, infra, prov, news (MSP) | MSP fabric-expected-blank ignored |
| 318209570537 | Revaltex Group OU | geo, infra, prov, news (MSP) | MSP fabric-expected-blank ignored |
| 318209570546 | Orange España | geo, infra, prov, news, fabric (target=true) | tier-frozen; full R2 deferred |
| 318219105988 | Telespace | geo, infra, prov, news (MSP) | |
| 318223398589 | NOS Wholesale | geo, infra, prov, news, fabric | Fiber ICP; full R2 needed |
| 318223398591 | Intelepeer | geo, infra, prov, news (MSP) | |
| 318223398594 | CLEARCOM COMUNICACIONES | geo, infra, prov, news (MSP) | |
| 318223398595 | Tecomsa Telecommuncations | geo, infra, prov, news (MSP) | |
| 318231615188 | COLOXCHANGE | geo, prov, news, hyper (Colo!) | Colo so hyper-proximity legit-missing |
| 318231691988 | Bayobab - MTN Digital Infra | geo, infra, prov, news, fabric (target=true) | tier-frozen; full R2 deferred |
| 318231691993 | Teligent Telecom | geo, infra, prov, news, fabric (target=true) | tier-frozen; full R2 deferred |
| 318231691997 | Telesol Group | geo, infra, prov, news (MSP) | |

Note: §4.5 of `enrichment-protocols.md` confirms `hyperscaler_proximity` is meaningful only for Colo + Greenfield; blank on Fiber/NetworkOp/NeoCloud/MSP/Enterprise is expected. `fabric_provisioning_approach` is `none_identified`-expected for MSPs (don't OWN infrastructure). Adjusted from raw 47-flag (every-field) to 15-flag (core-only) view to avoid false-positive backlog.

## Per-record results (full 50)

Format: ID | name | tier (cur→new) | path | sub-segment / notes

| # | ID | Name | Tier | Path | Sub-segment / Notes |
|---|---|---|---|---|---|
| 1 | 317231076065 | **Liberty Networks** | **tier_2 → tier_1** | **MEDIUM** | **Fiber/Long Haul → Network Op/Intl Backbone Specialist (Phase 3 framework reclass per protocols.md §6 N2→N4)** |
| 2 | 317237932750 | Airtel Seychelles | tier_3 | LIGHT+audit | Regional CLEC - Fiber operator (5 core fields blank) |
| 3 | 317259348704 | Rogers Communications | tier_3 | LIGHT | Regional Cable Operator - Fiber operator |
| 4 | 317271861986 | Cirrascale Cloud Services | tier_1 | LIGHT (target-frozen) | AI Infrastructure providers - Neocloud |
| 5 | 317273591519 | Inference.net | tier_1 | LIGHT (target-frozen) | Tier 1 Inference - Neocloud |
| 6 | 317340516029 | Coloware | tier_3 | LIGHT | Standard - colo |
| 7 | 317341909696 | South Front Networks | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 8 | 318051096311 | LARUS Limited | tier_3 | LIGHT | Regional CLEC - Fiber operator (3 core blank — edge of audit threshold; field gaps logged) |
| 9 | 318051097277 | Cellfind (Pty) Ltd | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 10 | 318093666006 | BroadNet | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 11 | 318106540778 | FSG (First Sunrise Group) | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 12 | 318106540783 | SBTS | tier_4 | LIGHT+audit (target-frozen) | Tier 1 Carrier - Network Op (5 core blank; tier-frozen so no compute) |
| 13 | 318106540785 | ENTEL PERU | tier_2 | LIGHT+audit (target-frozen) | Tier 1 Carrier - Network Op (5 core blank) |
| 14 | 318106540787 | RouteTrust | tier_2 | LIGHT+audit | Managed Network Services - MSP (4 core blank) |
| 15 | 318121584335 | ionstream | tier_1 | LIGHT | AI Infrastructure providers - Neocloud |
| 16 | 318192629456 | Allure Telecom Inc. | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 17 | 318196678355 | Apogee | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 18 | 318205926075 | Pineapple SMS | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 19 | 318205926077 | LOBSTER TEL, S de R.L. | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 20 | 318205926081 | Texcell Messaging Limited | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 21 | 318207597260 | AFN | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 22 | 318207597261 | The Horizon Communications Group | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 23 | 318207597263 | Datafon | tier_3 | LIGHT | Standard - colo |
| 24 | 318207597265 | TSG Carrier LTD | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 25 | 318207597278 | ENTELEGENT SOLUTIONS | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 26 | 318209570537 | Revaltex Group OU | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 core blank) |
| 27 | 318209570542 | Savitele, Inc | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 28 | 318209570546 | Orange España | tier_1 | LIGHT+audit (target-frozen) | Tier 1 Carrier - Network Op (5 core blank) |
| 29 | 318211865328 | Mexico Telecom Partners | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 30 | 318219105980 | ASAL Comunicaciones SA de CV | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 31 | 318219105981 | 1Route Group, LLC | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 32 | 318219105983 | EVOX | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 33 | 318219105986 | Sky Business Wholesale | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 34 | 318219105988 | Telespace | tier_2 | LIGHT+audit | Managed Network Services - MSP (4 core blank) |
| 35 | 318220838602 | Onextel Technology | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 36 | 318220838606 | DID Telecom BV | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 37 | 318220838607 | Gateway Global | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 38 | 318220838609 | MMDSmart | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 39 | 318223234756 | Vital Networks | tier_3 | LIGHT | Regional CLEC - Fiber operator |
| 40 | 318223234761 | DCN | tier_4 | LIGHT | Municipal / Cooperative - Fiber operator |
| 41 | 318223398589 | NOS Wholesale | tier_2 | LIGHT+audit | Tier 2 National Wholesale - Fiber operator (5 core blank — Fiber ICP, full R2 needed) |
| 42 | 318223398591 | Intelepeer | tier_2 | LIGHT+audit | Managed Network Services - MSP (4 core blank) |
| 43 | 318223398594 | CLEARCOM COMUNICACIONES, S.A.P.I. | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 core blank) |
| 44 | 318223398595 | Tecomsa Telecommuncations | tier_2 | LIGHT+audit | Telecom Aggregator - MSP (4 core blank) |
| 45 | 318231615185 | 42com International LTD. | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 46 | 318231615188 | COLOXCHANGE | tier_3 | LIGHT+audit | Standard - colo (4 core blank including hyper; Colo ICP — full R2 needed) |
| 47 | 318231691988 | Bayobab - MTN Digital Infrastructure | tier_2 | LIGHT+audit (target-frozen) | Tier 1 Carrier - Network Op (5 core blank) |
| 48 | 318231691989 | ZORYA | tier_2 | LIGHT | Telecom Aggregator - MSP |
| 49 | 318231691993 | Teligent Telecom | tier_4 | LIGHT+audit (target-frozen) | Tier 1 Carrier - Network Op (5 core blank) |
| 50 | 318231691997 | Telesol Group | tier_2 | LIGHT+audit | Managed Network Services - MSP (4 core blank) |

## Notes

- 49/50 records: framework-consistent with prior batches. The 1 MEDIUM correction (Liberty Networks N2→N4 reclass) resolved the framework drift from the 2026-05-14 web verification anchor-list update.
- 0 records had populated last_signal_score / last_signal_date — no signal modifiers fired across batch.
- 0 sub-segment auto-migrations from §7.4a deterministic table (all values already on canonical Phase 3 enum).
- 0 Greenfield migrations (no Greenfield records in this slice).
- 0 Customer-protection HOLDs (no closed-won deals in batch).
- 0 Completeness Gate fails (no FULL paths invoked).
- 0 manual-review HOLDs (per Cooper 2026-05-19 directive: best-effort classify, no new holds).
- 7 records with hs_is_target_account=true — `account_tier` writes skipped per §8 hard stop; segment/sub-segment/date all wrote normally.
- **15 LIGHT+audit records** flagged for clean R2 FULL re-enrichment post-sweep (4+ core narrative fields blank; Pellera-pattern field-write gaps). Tabulated above.

## Standout notable records (top 5 changes)

1. **Liberty Networks (317231076065)** — Segment + sub-segment reclass `Fiber Operator / Long Haul Backbone` → `Network Operator(Tier 1/VNO) / International Backbone Specialist - Network Op`. 60,000km submarine + terrestrial fiber across 30+ countries (LatAm/Caribbean, MAYA-1.2 subsea owner). Tier promoted T2 → T1 (Default International Backbone Specialist = T1 ceiling). Confidence high_90 → medium_7089 (anchor list expansion deferred to 2026-08-14 quarterly refresh).
2. **0 other classification changes** — batch is dominated by recently-touched records (last_enriched_date in 2026-04-07 through 2026-05-08 range), most already on Phase 3-canonical values from prior R1/R2 passes.
3. **7 target-frozen records** — Cirrascale, Inference.net (NeoCloud), SBTS, ENTEL PERU, Orange España, Bayobab, Teligent Telecom (Network Op Tier 1). All carry `hs_is_target_account=true` → tier writes skipped; segment/sub-segment/date stamped normally.
4. **15 Pellera-pattern flags** — Recurring narrative-field-write gap from prior R1/R2 FULL passes. Worth investigating R2 write-path reliability post-sweep. Particularly heavy on Africa/LatAm MSP records (Bayobab, Cellfind, Telesol Group, Tecomsa, CLEARCOM) and target-frozen Network Op records (SBTS, ENTEL PERU, Orange España, Bayobab, Teligent).
5. **MSP dominance** — 26 of 50 records are MSP/Aggregator (mostly Telecom Aggregator - MSP). Reflects the upper hs_object_id range where late 2025 / early 2026 sourcing batches loaded a large MSP cohort. Subsequent batches likely to remain MSP-heavy until pool drains.

## HubSpot write results

5 batches of 10 via `manage_crm_objects` updateRequest with `confirmationStatus = CONFIRMATION_WAIVED_FOR_SESSION`:
- Batch 1/5 (records 1-10, includes Liberty Networks MEDIUM reclass): 10/10 updated, 0 failed
- Batch 2/5 (records 11-20): 10/10 updated, 0 failed
- Batch 3/5 (records 21-30): 10/10 updated, 0 failed
- Batch 4/5 (records 31-40): 10/10 updated, 0 failed
- Batch 5/5 (records 41-50): 10/10 updated, 0 failed

Total: 50/50, 0 errors, 0 retries needed. HubSpot company notes per §7.7 deferred (Slack DM + this audit log function as the audit trail — same pattern as batches 46-49).

## Continuation

- LAST_PROCESSED_HS_OBJECT_ID: 318231691997
- POOL_REMAINING (before batch 50): 359
- POOL_REMAINING (after batch 50): 309
- Drain progress: ~89% of sweep complete (2,545 / ~2,854 records assuming original ~2,854 pool less remaining 309 = 2,545 done)
- Next batch: 51 — ETA ~7 more batches at BATCH_SIZE=50

## Continuation token (for hands-off resume)

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=51
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING=309
HOLD_POLICY=NONE (best-effort classify)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=318231691997
```
