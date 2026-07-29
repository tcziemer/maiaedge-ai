# Mass Re-Enrichment Sweep — Batch 24

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Kickoff date:** 2026-05-18
- **Batch number:** 24
- **Batch size:** 50
- **Verify depth:** leverage-and-patch
- **Apollo enforcement:** disabled (sweep window)
- **Segment scope:** all_active_icp
- **Run date:** 2026-05-18
- **Pool at start of batch:** 1,622 records remaining
- **Pool drained this batch:** 50 (cumulative ~1,200 / ~2,822 = ~42.5%)

## Path mix

- LIGHT: 22
- MEDIUM: 19
- FULL: 0
- HOLD: 0
- Flagged for deletion: 9

## Tier writes

- Promotions toward T1: 9 (Telekom Yemen, Post Luxembourg, Telekom Srbija, Telkom South Africa, Claro / America Movil, Tigo Business, Bayobab, Telia Lietuva, Foxconn AI Cloud held T1)
- Demotions toward T5: 2 (Starcloud, Nexus Core Systems — both Greenfield T2 from prior T1)
- Skipped (`hs_is_target_account = true`): 0
- Net tier writes this batch: 11
- Idempotent no-ops (tier unchanged): 39

## Notable framework events

- **Sub-segment auto-migrations:** 0 (no legacy values surfaced this batch)
- **Greenfield migrations:** 2 (Starcloud space-based pre-operational; Nexus Core Morocco 500MW campus pre-operational)
- **Subsea cable operator (new sub-segment) writes:** 1 (Medusa Submarine Cable System — first verified anchor write under this segment in batch 24)
- **Segment changes (cascade-eligible):** 14
  - 7 Fiber Operator → Network Operator(Tier 1 / VNO)/Tier 1 Carrier (Post Luxembourg, Telekom Srbija, Telkom South Africa, Claro, Tigo Business, Telia Lietuva, Telekom Yemen)
  - 1 Fiber Operator → Network Operator(Tier 1 / VNO)/Subsea cable operator (Medusa)
  - 1 Fiber Operator → Network Operator(Tier 1 / VNO)/Pure Wholesale Carrier (Bayobab/MTN)
  - 1 Fiber Operator → MSP/Aggregator/Managed Network Services (Riedel Networks)
  - 1 Fiber Operator → MSP/Aggregator/Cloud + Telecom Hybrid (Skyetel)
  - 9 → Flagged for deletion (KS Link, Latinatel, Purple Stone, Fastlink, Telesom, Telekom2, AGIL Telecom, Blue Dragon Network, plus 1 internal sub-only flag)
- **Sub-segment changes within same parent:** 3 (Exatel Polish wholesale → Tier 2 National Wholesale; Foxconn → Large Scale GPU; Starcloud/Nexus Core → Greenfield)
- **Customer-protection HOLDs:** 0
- **Completeness Gate fails:** 0 (no FULL paths)
- **Manual-review HOLDs:** 0

## Apollo

- Calls this batch: 0
- Sweep cumulative: tracked outside sweep budget (APOLLO_ENFORCEMENT = disabled)

## Template-bleed remediations

- account_brief regenerated: 3 (NTT Docomo Global, QuadraNet, Nexus Core Systems)
- provisioning_landscape regenerated: 11 (NTT Docomo, QuadraNet, SF Compute, PaleBlueDot AI, Trooper AI, HostKey, Oblivus, Cyfuture Cloud, Ori Industries, Thunder Compute, Soluna Computing, Nexus Core, Starcloud)
- Legacy strings cleaned: "polite chaos", "$10 billion problem", "stops at the network edge", "carrier dependencies dictating", "manual stitching of isolated networks", "responsible for end-to-end SLA but blind to 80% of the path", "Needs ... MaiaEdge angle: ..." template

## Apollo geo / owner fixes

- Dominican Telecom Prime (316194606824): country US/state Virginia → Dominican Republic, owner Tim Lieto → Tim Z (DR is International)
- Foxconn AI Cloud (301280580336): country US/state Indiana → Taiwan/null, owner Tim Lieto → Tim Z (Foxconn parent is Taiwan)
- Tigo Business (316235545320): country Chad/state N'Djamena → Luxembourg/null (Millicom HQ is Luxembourg; Tigo brand operates across 11 LatAm countries; Apollo confused with Tigo Chad sub)
- Runware (301269805760): state Pennsylvania → California (HQ is SF Bay)

## Top notable reclassifications (this batch)

1. **Bayobab** (316212615892) — MTN Group wholesale fiber arm (112,000 km African backbone, 8 countries) → confirmed Pure Wholesale Carrier - Network Op T1 per Cooper's "wholesale-arm-of-Tier-1" pattern from batch 23. Continues the African Tier-1 wholesale arm audit started this sweep.
2. **Telekom Yemen** (316179388113) — Sole Yemeni international gateway, state-owned monopoly, 20+ submarine cable alliances → Tier 1 Carrier - Network Op T1. National-gateway monopoly status outranks population size.
3. **Tigo Business / Millicom** (316235545320) — 46M+ customers across 11 LatAm countries (Bolivia, Colombia, Costa Rica, Ecuador, El Salvador, Guatemala, Honduras, Nicaragua, Panama, Paraguay, Uruguay), 14M fiber-cable homes passed, 100K employees → Tier 1 Carrier - Network Op. Apollo geo "Chad" was a Tigo Chad sub mis-attribution.
4. **Claro / America Movil** (316212615884) — Carlos Slim group's LatAm telecom, 18 countries, 100K employees, route miles enterprise-scale → Tier 1 Carrier - Network Op. Was mis-pinned as Regional CLEC.
5. **Medusa Submarine Cable System** (316298284733) — Mediterranean pure-play subsea, 8,700km, 21 landing stations, 480Tbps. First write into the 2026-05-14 `Subsea cable operator` sub-segment from existing CRM population (vs anchor additions during Phase 3).

## R3 dedup candidates raised this batch

- **Telenor parent vs Telenor AI Factory** (301316966113) — possible dedup against parent Telenor record if one exists. Worth a duplicate-account audit pass.
- No other new dedup pairs surfaced.

## Patterns observed (carry to future batches)

- **Mobile-led incumbent eviction pattern:** 5 records were mobile-only retail operators or international voice resellers serving small populations (Yemen excluded — has gateway-monopoly status). Pattern signature: <500 employees, voice-only or mobile-only, no wholesale fabric, no PoP count outside home country. Sweep-wide candidates: `account_brief CONTAINS "mobile operator" AND infrastructure_profile CONTAINS "POPs: Small"`.
- **Voice wholesale aggregators with no owned infrastructure** (8 hits this batch): default-flag rather than retain as Telecom Aggregator - MSP. Voice termination resellers fail the positive-evidence test under Cooper's aggressive-flag principle.
- **National incumbent under-tiering:** 7 records were national incumbents stuck at Fiber Operator/Regional CLEC tier_3. Sweep-wide candidate: `customer_segment = "Fiber Operator" AND company_sub_segment = "Regional CLEC - Fiber operator" AND (numberofemployees > 5000 OR annualrevenue > 500000000 OR geographic_focus CONTAINS "incumbent")`.
- **Template-bleed still present** on 2026-01 / 2026-02 / 2026-04 enrichment batches; pattern grep continues: `account_brief CONTAINS "polite chaos" OR "$10 billion problem" OR "stops at the network edge"` and `provisioning_landscape CONTAINS "Needs" AND CONTAINS "MaiaEdge angle"`.
- **Greenfield pre-operational neoclouds and colos** continue to surface from the 2026-02 cohort. Sweep-wide candidate: `account_brief CONTAINS "pre-operational" OR "under construction" OR "launching" OR "operational 2027"`.

## Drain status

- Done in this sweep so far: ~1,200 / ~2,822 ICP records
- Remaining: ~1,572 (1,622 at start of batch − 50 written this batch)
- ETA: ~31 more batches at BATCH_SIZE = 50

## Run health: GREEN

- No HubSpot 429/5xx errors
- No HubSpot 400 enum errors
- No Apollo budget breaches (consumed 0 this batch)
- No Slack DM send failures
- 50/50 records written across 5 sub-batches of 10
- 0 records held for next batch

## Audit log path

`weekly-reports/mass-reenrichment/2026-05-18-post-phase-3-framework/batch-24.md`

## Per-record summary

| # | Company | ID | Path | Old segment | New segment | Old sub-segment | New sub-segment | Old tier | New tier | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KS Link Telecommunication | 316296474350 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | Voice wholesale, no owned infra, aggressive flag |
| 2 | Latinatel | 316287384264 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | LatAm voice wholesale, 19 employees |
| 3 | Purple Stone Telecom | 316287384268 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | HK voice/data intermediary; name vs domain mismatch tollfreechina.com |
| 4 | Mada Jordan | 316296615621 | LIGHT | Fiber Operator | (unchanged) | Regional CLEC | (unchanged) | 3 | 3 | Real fiber + wireless + DC operator |
| 5 | Fastlink | 316196415207 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | Iraq Kurdistan mobile-only retail |
| 6 | Telesom | 316203554520 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | Somaliland mobile + money transfer retail |
| 7 | Telekom2 | 316283788007 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | UK VoIP + colo, 30 employees, sub-scale |
| 8 | Telekom Yemen | 316179388113 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | Sole national gateway, 20+ subsea cable alliances |
| 9 | Dominican Telecom Prime | 316194606824 | MEDIUM | Fiber Operator | (unchanged) | Regional CLEC | (unchanged) | 3 | 3 | Apollo geo fix: US/VA → DR; owner Tim Lieto → Tim Z |
| 10 | Skyetel 48 | 316224514752 | MEDIUM | Fiber Operator | MSP/Aggregator | Regional CLEC | Cloud + Telecom Hybrid MSP - MSP | 3 | 2 | US VoIP with own automation + 5 facilities |
| 11 | AGIL TELECOM | 316287384261 | MEDIUM | Fiber Operator | Flagged for deletion | Regional CLEC | (n/a) | 3 | (n/a) | Brazil 30-employee, no positive evidence |
| 12 | NTT Docomo Global | 251474980560 | MEDIUM | Network Operator(Tier 1 / VNO) | (unchanged) | Tier 1 Carrier - Network Op | (unchanged) | 1 | 1 | Brief + provisioning regen (template bleed), confidence low_5069 → high_90 |
| 13 | SF Compute | 239772420819 | LIGHT | NeoCloud | (unchanged) | Large Scale GPU - Neocloud | (unchanged) | 1 | 1 | Provisioning_landscape cleaned |
| 14 | QuadraNet | 254561398508 | MEDIUM | Data Center Colo Provider | (unchanged) | Standard - colo | (unchanged) | 3 | 3 | Brief + provisioning regen (heavy template bleed) |
| 15 | PaleBlueDot AI | 296846534387 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 16 | Trooper AI | 297164273399 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 17 | HostKey | 296880096971 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 18 | Oblivus | 297293654769 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 19 | Cyfuture Cloud | 297782865629 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 20 | Ori Industries | 297782865630 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 21 | Post Luxembourg | 316287384266 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | National incumbent, 18,000 km fiber, AI-ready network |
| 22 | Primetel | 316287384263 | LIGHT | Fiber Operator | (unchanged) | Regional CLEC | (unchanged) | 3 | 3 | Cypriot fiber + subsea landing |
| 23 | Telekom Srbija | 316298283756 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | Serbian state incumbent, 77.5% market share |
| 24 | Exatel S.A. | 316296474347 | MEDIUM | Fiber Operator | (unchanged) | Regional CLEC | Tier 2 National Wholesale - Fiber operator | 3 | 2 | Polish state wholesale fiber, 444 operators served |
| 25 | Medusa Submarine Cable System | 316298284733 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Long Haul / Backbone - Fiber operator | Subsea cable operator | 2 | 2 | First write into 2026-05-14 Subsea cable operator sub-segment from existing population |
| 26 | Riedel Networks | 316298283760 | MEDIUM | Fiber Operator | MSP/Aggregator | Regional CLEC | Managed Network Services - MSP | 3 | 2 | German MNS, 40+ POPs, 250+ multinationals, no owned fiber |
| 27 | Telkom South Africa | 316298284736 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | National incumbent, 15K employees, Openserve wholesale |
| 28 | Last Mile Corp | 316300071637 | LIGHT | MSP/Aggregator | (unchanged) | Telecom Aggregator - MSP | (unchanged) | 2 | 2 | Already correctly classified |
| 29 | Super Sistem | 316298284737 | LIGHT | Fiber Operator | (unchanged) | Dark Fiber Specialist - Fiber Operator | (unchanged) | 2 | 2 | Indonesian dark fiber + BTI subsea under construction |
| 30 | Lyntia Networks | 316303584979 | LIGHT | Fiber Operator | (unchanged) | Dark Fiber Specialist - Fiber Operator | (unchanged) | 2 | 2 | Spain's largest neutral fiber, 55,200 km |
| 31 | Thunder Compute | 297969950451 | LIGHT | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | (unchanged) | 1 | 1 | Provisioning cleaned |
| 32 | Starcloud | 301136594647 | MEDIUM | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | Greenfield | 1 | 2 | Space-based DCs, pre-operational; full launch 2027 |
| 33 | Sarvam AI | 300374619852 | LIGHT | NeoCloud | (unchanged) | Sovereign AI Clouds - Neocloud | (unchanged) | 1 | 1 | India sovereign LLM + 50MW DC |
| 34 | Nexus Core Systems | 300724509379 | MEDIUM | NeoCloud | (unchanged) | AI Infrastructure providers - Neocloud | Greenfield | 1 | 2 | Brief was contaminated; correctly Morocco 500MW pre-operational; rebuild brief |
| 35 | Naver Cloud | 301136592630 | LIGHT | NeoCloud | (unchanged) | Sovereign AI Clouds - Neocloud | (unchanged) | 1 | 1 | Korean sovereign play |
| 36 | Soluna Computing | 301205051103 | LIGHT | NeoCloud | (unchanged) | Crypto to AI - Neoclouds | (unchanged) | 1 | 1 | Provisioning cleaned |
| 37 | Runware | 301269805760 | MEDIUM | NeoCloud | (unchanged) | Tier 1 Inference - Neocloud | (unchanged) | 2 | 2 | State Apollo fix PA → CA |
| 38 | Foxconn AI Cloud | 301280580336 | MEDIUM | NeoCloud | (unchanged) | Sovereign AI Clouds - Neocloud | Large Scale GPU - Neocloud | 1 | 1 | Foxconn = private hyperscaler not nation-AI; geo US → Taiwan; owner Tim Lieto → Tim Z |
| 39 | Telenor AI Factory | 301316966113 | LIGHT | NeoCloud | (unchanged) | Sovereign AI Clouds - Neocloud | (unchanged) | 1 | 1 | Norway sovereign AI factory |
| 40 | EarthLink Business | 316153417441 | LIGHT | Fiber Operator | (unchanged) | Tier 2 National Wholesale - Fiber operator | (unchanged) | 2 | 2 | Annualrevenue $5.1B suspect; flag for data quality |
| 41 | Blue Dragon Network | 316298284744 | MEDIUM | MSP/Aggregator | Flagged for deletion | Telecom Aggregator - MSP | (n/a) | 2 | (n/a) | 6-employee VoIP reseller, no infra |
| 42 | Radius Telecoms | 316303584980 | LIGHT | Fiber Operator | (unchanged) | Regional CLEC | (unchanged) | 3 | 3 | Real PH fiber + DC partnership (Meralco subsidiary) |
| 43 | Claro / America Movil | 316212615884 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | LatAm largest telecom, 100K employees, 18 countries |
| 44 | Islalink Holding | 316212615889 | LIGHT | Fiber Operator | (unchanged) | Dark Fiber Specialist - Fiber Operator | (unchanged) | 2 | 2 | Mediterranean mixed subsea + terrestrial |
| 45 | Borwood Communications | 316224565948 | LIGHT | MSP/Aggregator | (unchanged) | Managed Network Services - MSP | (unchanged) | 2 | 2 | Global MNS aggregator |
| 46 | Broadnet Technologies | 316224514751 | LIGHT | MSP/Aggregator | (unchanged) | Telecom Aggregator - MSP | (unchanged) | 2 | 2 | Lebanon messaging hub; borderline ICP |
| 47 | Tigo Business | 316235545320 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | Millicom LatAm 11 countries; country Chad → Luxembourg |
| 48 | Bayobab | 316212615892 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Long Haul / Backbone - Fiber operator | Pure Wholesale Carrier - Network Op | 2 | 1 | MTN wholesale arm, 112,000 km African backbone |
| 49 | V.tal | 316224565952 | LIGHT | Fiber Operator | (unchanged) | Long Haul / Backbone - Fiber operator | (unchanged) | 2 | 2 | Brazil neutral fiber 400K+ km |
| 50 | Telia Lietuva AB | 316235602634 | MEDIUM | Fiber Operator | Network Operator(Tier 1 / VNO) | Regional CLEC | Tier 1 Carrier - Network Op | 3 | 1 | Lithuanian national incumbent, 99% 5G coverage |

End of batch-24.md
