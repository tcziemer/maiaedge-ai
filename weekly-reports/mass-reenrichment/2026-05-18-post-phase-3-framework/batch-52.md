# Mass Re-Enrichment Sweep — Batch 52

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 52
**Date:** 2026-05-19
**Kickoff date:** 2026-05-18
**Records processed:** 50/50
**HubSpot writes succeeded:** 50/50 (5 batches of 10)
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Last hs_object_id in batch:** 319190688481 (Hai Telecommunications)

## Pre-flight

- Trigger query: customer_segment IN [6 active ICPs] AND type NEQ "Customer" AND (last_enriched_date LT 2026-05-18 OR NULL); sort hs_object_id ASC; limit 50
- Pool total returned by HubSpot: **259** (matches batch-51 continuation projection exactly)
- Returned: 50 (clean alignment)
- Canvas F0B0AFSB9LN: **0 active Mass Re-Enrichment Sweep holds** (Cooper directive 2026-05-18 "no holds going forward; best-effort classify" remains in effect). No concurrent batch detected.
- Apollo budget JSON: not updated (APOLLO_ENFORCEMENT=disabled per sweep params)
- Web searches: 0 total (decisions made from existing enriched-field evidence + Phase 3 framework reference per CLAUDE.md op principle 3 + Cooper batches 50-51 pattern)

## Path mix

- LIGHT: 1 (Vast.ai — stale generic recent_news cleared)
- LIGHT+audit (non-target, 4+ core fields blank): 7
- LIGHT+audit (target-frozen, Pellera-pattern): 41
- MEDIUM: 1 (Hawaiki Cable segment + sub-segment reclass to Subsea cable operator)
- FULL: 0
- HOLD: 0 (per Cooper directive)

## Tier writes

- Promotions (toward Tier 1): 0
- Demotions (toward Tier 5): 0
- Skipped (hs_is_target_account=true): 42
- All non-target tiers match defaults table (idempotent no-op)

## Sub-segment / segment corrections (MEDIUM detail)

### 1. Hawaiki Cable (319190597360) — Phase 3 anchor reclass to Subsea cable operator
- **Before:** customer_segment=`Fiber Operator`, company_sub_segment=`Long Haul / Backbone - Fiber operator`, segmentation_confidence=`high_90`, account_tier=`tier_1` (target-frozen)
- **After:** customer_segment=`Network Operator(Tier 1 / VNO)`, company_sub_segment=`Subsea cable operator`, segmentation_confidence=`high_90` (unchanged), account_tier=`tier_1` (target-frozen, write skipped)
- **Reason:** Per `context/account-tiering/enrichment-protocols.md` §6 anchor list (2026-05-14): "Hawaiki Submarine Cable / BW Digital" is a verified HIGH anchor under the new (30th) sub-segment `Subsea cable operator`, parent `Network Operator(Tier 1 / VNO)`. Existing account_brief evidence is unambiguous: "15,000km trans-Pacific subsea cable, 67 Tbps, carrier-neutral. Links Australia, New Zealand, American Samoa, Hawaii, and 5 PoPs on US West Coast. Pure-play subsea wholesale operator." Pre-Phase-3 record was misrouted to Fiber/Long Haul because Subsea cable operator did not exist as a sub-segment until 2026-05-14.
- **Tier compute:** hs_is_target_account=true → tier_1 frozen (no write). If unfrozen: Default Network Operator(Tier 1 / VNO)/Subsea cable operator = T2, ceiling 1, floor 3. No signal modifiers fire. Algorithmic tier_2; current tier_1 remains under manual override.

## LIGHT (1)

### 1. Vast.ai (318865028831) — stale generic recent_news cleared
- **Before:** recent_news_or_trigger_event=`"Continued GPU marketplace expansion through 2025-2026; broader AI infrastructure sector investment activity."` (no date prefix, generic placeholder)
- **After:** recent_news_or_trigger_event=`""` (cleared per §7.4 stale-clearing side-action)
- Other 7/8 fields complete: account_brief, geographic_focus, infrastructure_profile (Enterprise 50+), fabric_provisioning_approach (none_identified), provisioning_landscape, customer_segment=NeoCloud, sub-segment=AI Infrastructure providers - Neocloud, segmentation_confidence=medium_7089, account_tier=tier_1 (idempotent default for NC3).
- hyperscaler_proximity blank — expected None Known for NeoCloud marketplace model; not flagged.

## LIGHT+audit non-target (7) — flagged for post-sweep R2 FULL re-enrichment

These 7 non-target records have 4-6 core narrative fields blank. Got `last_enriched_date = 2026-05-19` LIGHT stamp + audit note here; defer to R2 FULL cycle (or D7 if R2 doesn't catch them in 30 days).

| ID | Name | Current tier | Sub-segment | Missing core fields |
|---|---|---|---|---|
| 318231692000 | Megatel Netcom Corporation | tier_3 | Regional CLEC - Fiber operator | geo, infra, prov, news, fabric, hyper (6) |
| 318231692002 | Whisl Telecom | tier_2 | Telecom Aggregator - MSP | geo, infra, prov, news (MSP fabric+hyper expected blank) |
| 318316962512 | Kins247 | tier_2 | Telecom Aggregator - MSP | prov, news (MSP fabric+hyper expected blank; geo + infra present) |
| 318343401174 | VINGN | tier_4 | Municipal / Cooperative - Fiber operator | prov, news, fabric, hyper-OK (USVI municipal fiber co-op) |
| 318348926654 | Samm Tecnologia | tier_2 | Long Haul / Backbone - Fiber operator | prov, news, fabric, hyper-OK (Brazilian backbone) |
| 318370362082 | QuattroCom | tier_3 | Regional CLEC - Fiber operator | prov, news, fabric, hyper-OK (Mexican regional CLEC) |
| 318585098989 | Airwavz | tier_3 | Regional CLEC - Fiber operator | prov, news, fabric, hyper-OK (US in-building wireless DAS — note: account_brief calls it "Network Operator External Extension" but record is Fiber/Regional CLEC; flag for R2 segment review) |

Note: §4.5 of `enrichment-protocols.md` — `hyperscaler_proximity` is meaningful only for Colo + Greenfield; blank on Fiber/NetworkOp/NeoCloud/MSP/Enterprise is expected. `fabric_provisioning_approach` is `none_identified`-expected for MSPs.

## LIGHT+audit target-frozen (41) — Pellera-pattern continuation

Same field-write gap pattern Cooper validated in batches 48-51. All 41 records are `hs_is_target_account=true`, owned by Tim Z (159350430), and have 6 of 7 narrative fields blank (only account_brief populated, often without date prefix on recent_news context). Tier writes skipped per §8 hard stops; segment/sub-segment writes proceed normally but all 41 records are already in the 30 active values so no migration writes fire. `last_enriched_date = 2026-05-19` stamped to drain from pool; flagged for post-sweep R2 FULL.

Africa: Mascom Botswana not in this batch (batch 51). This batch: 21st Century Technologies (Nigeria), SWIFT Networks (Nigeria), Aviso Telecom (Cote d'Ivoire), Malitel (Mali), Unitel Angola, Hai Telecommunications (Zambia).

MENA: Fast Link Iraq, Ooredoo Algeria Wholesale, INWI Wholesale (Morocco).

Asia/Pacific: Raajje Online (Maldives), Samoa Digital Services, Hypernet Indonesia, Sacofa (Malaysia), PTI Pacifica (Guam), Wantok Vanuatu, PNCC (Palau), Allo Technology (Malaysia), Vocus Wholesale (Australia), CMC Telecom (Vietnam), Link3 Technologies (Bangladesh), TasmaNet (Australia), PT ICON+ (Indonesia), Canl+ (New Caledonia), TVL (Vanuatu).

LatAm/Caribbean: Yofone Peru, Centennial (Puerto Rico), Digicel Jamaica, Balboa Communications Panama, NetBlue Brasil, Panama Digital, UTS Curacao, DirecPath Brasil, Optical Networks Peru, Setar (Aruba), Sumicity Brasil, Tricom (Dominican Republic), bmobile Vodafone (Trinidad), Massy Stores Telecom (Trinidad).

Plus rows 1-5 above (ONEMAX DR, Ten Peaks Canada, Akton Slovenia + the 7 Caribbean/LatAm/Asia from rows 3-5 of the date-only writes).

Wait that double-counts — full target-frozen list of 41 is below the per-record table.

## Apollo state data quality flags (deferred to R6, NOT corrected this batch)

Two target records have obviously incorrect `state` values from a stale Apollo enrichment. Cooper's batch 50-51 pattern defers Apollo state corrections out of this sweep (0 Apollo budget consumed). Flagged for R6 Territory & Hygiene + R2 FULL re-enrichment side-action:

| ID | Name | state (wrong) | country (correct) |
|---|---|---|---|
| 319190598331 | Telecom Vanuatu Limited (TVL) | North Carolina | Vanuatu |
| 319190678231 | Tricom | Kansas | Dominican Republic |

Both Tim Z territory. Owner does not change (159350430 international is correct).

## Side-actions

- recent_news_or_trigger_event cleared on 1 record: Vast.ai (318865028831) — stale generic placeholder, no date prefix.
- 0 sub-segment auto-migrations (no legacy values detected in batch).
- 0 customer-protection HOLDs (0 closed-won deals in pool).
- 0 segment-cascade fires (Hawaiki MEDIUM kept high_90 confidence; Fiber → Network Op cascade to contacts deferred to R6).

## Per-record audit log (all 50)

| ID | Name | Path | Segment | Sub-segment | Tier | Target | Notes |
|---|---|---|---|---|---|---|---|
| 318231692000 | Megatel Netcom Corporation | LIGHT+audit | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | 6 core fields blank — R2 FULL needed |
| 318231692002 | Whisl Telecom | LIGHT+audit | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | N | 4 core blank (MSP-adjusted) |
| 318231692004 | ONEMAX | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_4 | Y | Pellera-pattern |
| 318231692005 | Ten Peaks Data Centres | LIGHT+audit (target-frozen) | Data Center Colo Provider | Standard - colo | tier_4 | Y | Canadian colo; minimal data on file |
| 318231692007 | Akton Communications | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_4 | Y | Slovenian carrier |
| 318316962512 | Kins247 | LIGHT+audit | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | N | 2 core blank (MSP) |
| 318343401174 | VINGN | LIGHT+audit | Fiber Operator | Municipal / Cooperative - Fiber operator | tier_4 | N | USVI middle-mile fiber co-op |
| 318348926654 | Samm Tecnologia | LIGHT+audit | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | N | Brazilian backbone |
| 318370362082 | QuattroCom | LIGHT+audit | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | Mexican CLEC |
| 318585098989 | Airwavz | LIGHT+audit | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | N | US DAS operator; segment may need review (brief calls Network Op External Extension) |
| 318865028831 | Vast.ai | LIGHT | NeoCloud | AI Infrastructure providers - Neocloud | tier_1 | N | Stale generic news cleared |
| 319141370569 | Raajje Online | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Maldives |
| 319141370570 | Samoa Digital Services | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Samoa |
| 319173045987 | Yofone Peru | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Peru |
| 319173073597 | Hypernet Indonesia | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Indonesia |
| 319173074666 | Sacofa | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Malaysia (Sarawak) |
| 319173096167 | Centennial | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Puerto Rico |
| 319173096169 | Digicel Jamaica | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Jamaica |
| 319173099195 | 21st Century Technologies | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Nigeria |
| 319173102318 | Fast Link Iraq | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Iraq |
| 319173106384 | PTI Pacifica | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Guam |
| 319173106387 | Wantok Vanuatu | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Vanuatu |
| 319176690364 | PNCC (Palau) | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Palau — SEA-US + Echo cable landing |
| 319176714958 | Balboa Communications Panama | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Panama |
| 319176721104 | NetBlue Brasil | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Brazil |
| 319176721138 | Panama Digital | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Panama |
| 319176726213 | Ooredoo Algeria Wholesale | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y | Algeria |
| 319176744642 | Allo Technology | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Malaysia |
| 319176768213 | UTS Curacao | LIGHT+audit (target-frozen) | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | Y | Curacao |
| 319182113497 | Vocus Wholesale | LIGHT+audit (target-frozen) | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_1 | Y | Australia (ASC + INDIGO subsea) |
| 319182120671 | DirecPath Brasil | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Brazil |
| 319182126810 | Optical Networks Peru | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Peru |
| 319182207726 | Setar | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Aruba |
| 319182211807 | Aviso Telecom | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Cote d'Ivoire |
| 319182211819 | Malitel | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Mali |
| 319182213851 | SWIFT Networks | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Nigeria |
| 319182218965 | Canl+ | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | New Caledonia |
| **319190597360** | **Hawaiki Cable** | **MEDIUM** | **Network Operator(Tier 1 / VNO)** (was Fiber Operator) | **Subsea cable operator** (was Long Haul / Backbone) | **tier_1 (target-frozen)** | **Y** | **Phase 3 anchor reclass; D5 protocol N5 anchor "Hawaiki Submarine Cable / BW Digital"** |
| 319190598331 | Telecom Vanuatu Limited (TVL) | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Vanuatu — state="North Carolina" wrong, deferred to R6 |
| 319190611671 | PT ICON+ | LIGHT+audit (target-frozen) | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_1 | Y | Indonesia |
| 319190629074 | Sumicity Brasil | LIGHT+audit (target-frozen) | Fiber Operator | Regional CLEC - Fiber operator | tier_2 | Y | Brazil |
| 319190635215 | INWI Wholesale | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_2 | Y | Morocco |
| 319190656708 | CMC Telecom | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Vietnam |
| 319190658752 | Link3 Technologies | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Bangladesh |
| 319190674113 | TasmaNet | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Australia (Tasmania) |
| 319190678231 | Tricom | LIGHT+audit (target-frozen) | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | Y | Dominican Republic — state="Kansas" wrong, deferred to R6 |
| 319190679245 | Unitel Angola | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_2 | Y | Angola |
| 319190683379 | bmobile Vodafone | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Trinidad and Tobago |
| 319190684408 | Massy Stores Telecom | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Trinidad and Tobago |
| 319190688481 | Hai Telecommunications | LIGHT+audit (target-frozen) | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_3 | Y | Zambia |

## Drain status

- Pool before batch 52: 259 records
- Pool after batch 52: ~209 records (50 stamped to 2026-05-19, fall out of trigger query)
- Sweep cumulative: ~2,645 / 2,854 (~93%)
- ETA: ~5 more batches at BATCH_SIZE=50

## Run health

:large_green_circle: GREEN — 50/50 HubSpot writes succeeded across 5 batches of 10. 0 errors, 0 retries needed.

## Notable observations

1. **Continued Pellera-pattern density.** Batch 52 was again heavy on Africa / MENA / Asia / Pacific / LatAm / Caribbean Network Operator + Fiber Operator target_account records — 41 of 50 (82%) match the Pellera-pattern (6 of 7 narrative fields blank). Confirms the pattern is concentrated in this `hs_object_id` range (~319.1M-319.2M) which corresponds to the original Tim-Z international target_account batch import circa April 2026.
2. **Phase 3 anchor reclass surfaced: Hawaiki Cable.** The 30th sub-segment (`Subsea cable operator`, added 2026-05-14) found another retroactive match — Hawaiki was originally misrouted to `Fiber Operator / Long Haul / Backbone` because the Subsea sub-segment did not exist at original enrichment time. Brief evidence ("Pure-play subsea wholesale operator. 15,000km trans-Pacific subsea cable") is unambiguous. Same protocol that caught Liberty Networks in batch 50 — Phase 3 framework is still surfacing valid reclassifications 5 batches in.
3. **Vast.ai recent_news drift.** Generic placeholder "Continued GPU marketplace expansion through 2025-2026" with no date prefix is the cleanest example of stale signal field this batch — cleared per §7.4 side-action rule.
4. **Two Apollo state-data errors deferred.** TVL (Vanuatu) carries state="North Carolina"; Tricom (Dominican Republic) carries state="Kansas". Both target_account, both Tim Z territory. Not corrected this batch (Cooper's 0-Apollo sweep pattern); flagged for R6 Territory & Hygiene + R2 FULL.
5. **Airwavz segment-review flag.** account_brief describes "US in-building wireless infrastructure operator specializing in 5G-ready DAS" and calls it a "clear Network Operator (External Extension) profile" — but the record sits under `Fiber Operator / Regional CLEC`. The classification might need to move to Network Operator with the 5G DAS Track A signal, OR stay Fiber if the brief is over-fitting the narrative. Flagged for R2 FULL review.
6. **0 tier writes.** All non-target tiers match defaults table (idempotent); all 42 target tiers frozen per `hs_is_target_account=true`. Sweep is reaching a clean steady-state — most retroactive Phase 3 reclassifications have already been caught in earlier batches.
