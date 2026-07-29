# Mass Re-Enrichment Sweep — Batch 37

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 37
**Run date:** 2026-05-19
**Records processed:** 50 / 50
**Records written:** 47
**HOLDs (no writes):** 3
**Pool remaining at batch start:** 998
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT="disabled" + Apollo-free path dominant)

## Path mix

- LIGHT (date stamp + minor): 36
- MEDIUM (1-3 field updates): 4 (R7 Critical Infra Partners, R28 Nscale, R35 Int'l Gateway, R42 ValorC3)
- FULL (full reclassification): 7 (R4 e&, R20 RingSquared, R26 Applied Digital, R38 GTI, R44 Solomon Islands Subsea, R45 Zain Omantel, R50 Quantum Loophole)
- HOLD: 3 (R41 Goodman Group, R43 SB Communications, R46 ING/Ting)

## Substantive changes

### R04 Emirates Telecommunications Group (e& / Etisalat) — id 208233820859
- Path: FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → Tier 1 Carrier - Network Op
- Confidence: high_90 → high_90
- Tier: tier_3 → tier_1
- infrastructure_profile: upgraded to Facilities Enterprise (50+); Route Miles Enterprise (50K+); POPs Enterprise (100+)
- Reason: UAE national incumbent (ADX:EAND), 100K+ km fiber + subsea, acquired Mohegan stake in PPF Telecom 2024 (6 EU markets), launched Wholesale Americas in Miami 2025. Continuing "national operator under-tiering" pattern (cumulative ~41).

### R07 Critical Infrastructure Partners — id 208875154161
- Path: MEDIUM
- Segment: Fiber Operator → Fiber Operator (unchanged)
- Sub-segment: Long Haul / Backbone - Fiber operator → Regional CLEC - Fiber operator
- Confidence: medium_7089 → medium_7089
- Tier: tier_2 → tier_3
- Reason: Within-fiber demotion. infrastructure_profile shows Mid-Size (1K-10K) route miles + "smaller fiber operator" brief — does not meet LH/B scale (50K+). Continuing "Long Haul/Backbone → Regional CLEC" demotion pattern (cum ~22).

### R20 RingSquared — id 209230110408
- Path: FULL
- Segment: Fiber Operator → MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator → Telecom Aggregator - MSP
- Confidence: high_90 → high_90
- Tier: tier_3 → tier_2
- Reason: 66 emp holdco rolling up regional carriers (8 acquisitions in 8 years). Core services SIP, UCaaS, SD-WAN, voice/data aggregation; fiber (MegaWatt) is acquired holding, not core operating business. Continuing "CPaaS/voice aggregator misclassified as Fiber Op Regional CLEC" pattern (cum ~6).

### R26 Applied Digital — id 239751073471
- Path: FULL
- Segment: NeoCloud → NeoCloud (unchanged)
- Sub-segment: Large Scale GPU - Neocloud → Crypto to AI - Neoclouds
- Confidence: high_90 → high_90
- Tier: tier_1 → tier_1 (unchanged - both NC1 and NC5 default Tier 1)
- Reason: BTC mining heritage pivoting to AI/HPC. Per Cooper 2026-05-14 policy: "Companies previously listed as Large Scale GPU - Neocloud or AI Signals - colo anchors but with BTC mining heritage now route to NC5 instead (Crusoe, Applied Digital, Prometheus Hyperscale moved 2026-05-14)."

### R28 Nscale — id 240242364125
- Path: MEDIUM
- Segment: NeoCloud → NeoCloud (unchanged)
- Sub-segment: Large Scale GPU - Neocloud → Sovereign AI Clouds - Neocloud
- Confidence: high_90 → high_90
- Tier: tier_1 → tier_1 (unchanged - both default Tier 1)
- Reason: UK-headquartered with explicit sovereign-AI positioning + Microsoft 200K GB300 strategic contract = clear Sovereign AI profile, not generic GPU compute. Brief explicitly says "sovereign AI cloud" - prior classification was a mismatch.

### R29 TeraWulf — id 240390403775
- Path: LIGHT (confidence only)
- Segment: NeoCloud (unchanged)
- Sub-segment: Crypto to AI - Neoclouds (unchanged)
- Confidence: manual_review_required → high_90
- Tier: tier_1 (unchanged)
- Reason: No-default-manual-review principle. TeraWulf is unambiguously a BTC-miner-pivoted-to-AI operator (Lake Mariner NY 750MW, $12.8B contracted HPC revenue) — clear Crypto to AI - Neoclouds fit. Prior manual_review_required was a default-set artifact.

### R35 International Gateway Co Ltd (42com-int) — id 251474980554
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: high_90 (unchanged in field, was already high_90)
- Tier: tier_3 (unchanged)
- Reason: Promoted from HELD/ambiguous brief. 2025-12 news confirms Asian wholesale gateway operator partnering with Google on Talaylink Project (Thailand-Australia subsea cable). Future-watch: could upgrade to Subsea cable operator on next pass if subsea share grows.

### R38 GTI Corporation — id 251474980561
- Path: FULL
- Segment: Fiber Operator → Other
- Sub-segment: Regional CLEC - Fiber operator → (cleared)
- Confidence: medium_7089 → high_90
- Tier: tier_3 → tier_5
- Reason: Equipment + services mix - matches D1 disqualifier. Reclassified to Other (partner/competitive reference) per aggressive Flagged-for-deletion policy distinguishing Other = useful competitive ref vs Flagged for deletion = no-positive-evidence non-fit.

### R42 ValorC3 Data Centers — id 251476786922
- Path: MEDIUM (brief + geo corrections)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo (unchanged)
- Tier: tier_3 (unchanged)
- Reason: Brief incorrectly stated "Brazilian colocation operator" while geo field showed US (St. George UT). Corrected brief to align with US identity. R3 duplicate hold with record 253632545468 (difdatacenters.com) carryover.

### R44 Solomon Islands Submarine Cable Company — id 251480338124
- Path: FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone - Fiber operator → Subsea cable operator
- Confidence: high_90 → high_90
- Tier: tier_2 → tier_2 (unchanged - Subsea default T2)
- Reason: Pure-play subsea operator (Coral Sea Cable + Solomon Islands Domestic Network) with minimal terrestrial. AIFFP $72.71M PE 2025-11. First Subsea cable operator promotion in this batch (cumulative 1 in sweep batch 37; prior batches 0).

### R45 Zain Omantel International — id 251480338125
- Path: FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator → International Backbone Specialist - Network Op
- Confidence: high_90 → high_90
- Tier: tier_3 → tier_2
- infrastructure_profile: upgraded to Route Miles Large (10K-50K); POPs Enterprise (100+)
- Reason: Continuing "national operator under-tiering" pattern. ZOI is the 50/50 JV handling all international wholesale for Zain + Omantel (50M+ subs, 8 countries, 20+ subsea cable systems, 16,000 km terrestrial). Major Middle East wholesale powerhouse - clear International Backbone Specialist fit.

### R50 Quantum Loophole — id 251526039256
- Path: FULL
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: AI Signals - colo → Hyperscale Wholesale - colo
- Confidence: low_5069 → high_90
- Tier: tier_1 (unchanged)
- Reason: Business model is hyperscale land/power wholesale (~5GW potential at 2,100-acre Frederick MD QLoop), not AI-tenant operating colo. Sold 150 acres to Rowan Digital Infrastructure 2024-06; Crosslink consortium build with Aligned + Edged as anchor tenants. Confidence upgraded - identity now clear post-MISDOMAIN correction at prior pass.

## HOLDs (no writes — preserved for Cooper / D7)

### R41 Goodman Group — id 251476786920
- Reason: Domain mismatch HOLD carries forward. HubSpot name "Goodman Group" at domain "giomaregroup.com" - mismatch. Real Goodman Group (ASX:GMG Australian REIT hyperscale developer) is at goodman.com. Giomare Group is unrelated entity. Either domain correction OR reclassification to Other - escalation to Cooper.

### R43 SB Communications Private Limited — id 251480338123
- Reason: Insufficient signal to disambiguate. Name "SB Communications" at "yscommunications.net" returns no clear canonical operator. Multiple candidates (SoftBank Telecom India / SB Broadband Bangalore / SB Networks Bangladesh). HELD for Cooper review.

### R46 ING (ting.com) — id 251513968344
- Reason: Name "ING" at domain ting.com (Tucows-owned Ting) - mismatch. Likely import typo or two entities conflated. Real Ting is a US fiber + MVNO operator. HELD pending Cooper decision on rename.

## Pattern carry-forward updates

- **National operator under-tiering** — cum ~41 (+1 batch 37: e&)
- **Within-fiber Long Haul/Backbone → Regional CLEC demotion** — cum ~22 (+1 batch 37: Critical Infrastructure Partners)
- **CPaaS/voice aggregator misclassified as Fiber Op Regional CLEC** — cum ~6 (+1 batch 37: RingSquared)
- **BTC heritage → Crypto to AI - Neoclouds policy migration** — Applied Digital reclassified this batch (continues 2026-05-14 policy work)
- **Subsea cable operator promotions** — cum 1 in this sweep (+1 batch 37: Solomon Islands SCC)
- **Equipment vendor / partner ref → Other reclassification** — +1 batch 37 (GTI Corporation)
- **Sovereign AI Clouds reclassification from Large Scale GPU** — NEW PATTERN batch 37 (+1: Nscale)
- **Hyperscale Wholesale - colo reclassification from AI Signals - colo** — NEW PATTERN batch 37 (+1: Quantum Loophole)

## Per-record summary (all 50)

| # | Company ID | Name | Path | Segment | Sub-segment | Tier | Confidence |
|---|---|---|---|---|---|---|---|
| R01 | 206187780842 | Nex-Tech | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R02 | 206711238359 | SmartCom Telephone | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R03 | 206936725203 | Plateau | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R04 | 208233820859 | Emirates Telecom (e&) | FULL | Network Op (T1/VNO) | Tier 1 Carrier - Network Op | tier_1 | high_90 |
| R05 | 208850117347 | CNI Team | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | medium_7089 |
| R06 | 208871558862 | Hurricane Electric | LIGHT | Network Op (T1/VNO) | International Backbone Specialist - Network Op | tier_1 | high_90 |
| R07 | 208875154161 | Critical Infra Partners | MEDIUM | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | medium_7089 |
| R08 | 208878748366 | PBI Fiber | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R09 | 208878748367 | MACH Networks | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R10 | 208907000559 | BCN Telecom | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R11 | 208908440283 | Dakota Carrier Network | LIGHT | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | high_90 |
| R12 | 208998030021 | Indigo | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R13 | 208998030022 | 46 Labs | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | medium_7089 |
| R14 | 209003423468 | Fuse | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R15 | 209026970360 | joink | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | medium_7089 |
| R16 | 209163212495 | Cielo | LIGHT | Data Center Colo Provider | Standard - colo | tier_3 | medium_7089 |
| R17 | 209166806768 | BCM One | LIGHT | MSP/Aggregator | Managed Network Services - MSP | tier_2 | high_90 |
| R18 | 209170399993 | B2 Telecom | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R19 | 209230110405 | DFN | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R20 | 209230110408 | RingSquared | FULL | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R21 | 209230110411 | CentraCom | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R22 | 209237307098 | Altaworx | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R23 | 223928806112 | Midwest Fiber Networks | LIGHT | Fiber Operator | Dark Fiber Specialist - Fiber Operator | tier_2 | high_90 |
| R24 | 233872561911 | Iceblue Internet | LIGHT | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 | high_90 |
| R25 | 236028986044 | Cogent Communications | LIGHT | Network Op (T1/VNO) | Pure Wholesale Carrier - Network Op | tier_1 | high_90 |
| R26 | 239751073471 | Applied Digital | FULL | NeoCloud | Crypto to AI - Neoclouds | tier_1 | high_90 |
| R27 | 240190285514 | White Fiber | LIGHT | NeoCloud | AI Infrastructure providers - Neocloud | tier_1 | medium_7089 |
| R28 | 240242364125 | Nscale | MEDIUM | NeoCloud | Sovereign AI Clouds - Neocloud | tier_1 | high_90 |
| R29 | 240390403775 | TeraWulf | LIGHT | NeoCloud | Crypto to AI - Neoclouds | tier_1 | high_90 |
| R30 | 240415486656 | RunPod | LIGHT | NeoCloud | Large Scale GPU - Neocloud | tier_1 | high_90 |
| R31 | 240431524557 | CoreWeave | LIGHT | NeoCloud | Large Scale GPU - Neocloud | tier_1 | high_90 |
| R32 | 240446137023 | J.P. Morgan & Co. | LIGHT | Enterprise-CustomerSegment | Financial Services - Enterprise | tier_3 | high_90 |
| R33 | 240447926006 | FluidStack | LIGHT | NeoCloud | Large Scale GPU - Neocloud | tier_1 | high_90 |
| R34 | 251270645453 | Telxius | LIGHT | Network Op (T1/VNO) | International Backbone Specialist - Network Op | tier_1 | medium_7089 |
| R35 | 251474980554 | International Gateway Co Ltd | MEDIUM | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R36 | 251474980555 | Talia Communications | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | high_90 |
| R37 | 251474980558 | HGC | LIGHT | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | high_90 |
| R38 | 251474980561 | GTI Corporation | FULL | Other | (cleared) | tier_5 | high_90 |
| R39 | 251476786918 | Ascenty | LIGHT | Data Center Colo Provider | AI Signals - colo | tier_1 | high_90 |
| R40 | 251476786919 | Menlo Digital | LIGHT | Data Center Colo Provider | Standard - colo | tier_3 | high_90 |
| R41 | 251476786920 | Goodman Group | HOLD | (unchanged) | (unchanged) | tier_3 | medium_7089 |
| R42 | 251476786922 | ValorC3 Data Centers | MEDIUM | Data Center Colo Provider | Standard - colo | tier_3 | medium_7089 |
| R43 | 251480338123 | SB Communications | HOLD | (unchanged) | (unchanged) | tier_3 | low_5069 |
| R44 | 251480338124 | Solomon Islands SCC | FULL | Network Op (T1/VNO) | Subsea cable operator | tier_2 | high_90 |
| R45 | 251480338125 | Zain Omantel International | FULL | Network Op (T1/VNO) | International Backbone Specialist - Network Op | tier_2 | high_90 |
| R46 | 251513968344 | ING (ting.com) | HOLD | (unchanged) | (unchanged) | tier_3 | low_5069 |
| R47 | 251526039251 | Lightpath | LIGHT | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 | high_90 |
| R48 | 251526039252 | ADN International Gateway | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | medium_7089 |
| R49 | 251526039254 | Northwestel Inc | LIGHT | Fiber Operator | Regional CLEC - Fiber operator | tier_3 | medium_7089 |
| R50 | 251526039256 | Quantum Loophole | FULL | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 | high_90 |

## Drain status

- Pool at batch 37 start: 998
- Processed this batch: 50 (47 written + 3 HOLD)
- Projected remaining: 998 - 50 = ~948 (HOLDs reappear in next pool; pool may also refill from concurrent R0/R1/R2)
- Sweep cumulative records processed across batches 1-37: estimated ~1,800+
- ETA: ~19 more batches at BATCH_SIZE=50 to drain remaining pool

## Run health: GREEN

- All 47 HubSpot writes succeeded (5 manage_crm_objects batches, totalProcessed = 47, failed = 0)
- No 429s, no enum validation errors
- 3 HOLDs deliberately not written per §7.5 HOLD path
- Apollo: 0 credits this batch (Apollo-free path dominant)
- No fatal errors
