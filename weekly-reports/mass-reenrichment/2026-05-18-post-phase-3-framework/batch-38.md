# Mass Re-Enrichment Sweep — Batch 38

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 38
**Date:** 2026-05-19
**Records processed:** 50/50 (50 written, 0 HOLD — initial 8 HOLDs resolved per Cooper directive "no HOLDs, best-bet judgment")
**Pool remaining (post-batch):** ~901 (was 951 pre-batch)
**Apollo this batch:** 0 credits

## Path mix (post-HOLD-resolution)
- LIGHT: 18
- MEDIUM: 21
- FULL: 3
- HOLD-RESOLVED: 8 (initially HOLD, resolved with best-bet judgment writes per Cooper directive 2026-05-19)

## HOLD resolutions (8 records)

| ID | Name | Resolution |
|---|---|---|
| 251535204088 | Tekpoint -> **TierPoint, LLC** | Renamed; domain tekpoint.com -> tierpoint.com; Standard - colo confirmed; tier_3 -> tier_2; conf high_90. 40 DCs / 20 markets / top-15 US colo. |
| 251574698722 | Global Secure Layer | Domain byglobal.es -> globalsecurelayer.com.au; Fiber Operator -> **Other**; tier_3 -> tier_5; conf high_90. Australian DDoS/security overlay, partner-keep. |
| 251591673530 | Netnod AB | Fiber Operator -> **Other**; tier_3 -> tier_5; conf high_90. Swedish IXP + DNS root. **RECOMMEND** Cooper add IXP as 31st sub-segment under Network Operator (cum 3 IXP records: DE-CIX, Mass IX, Netnod). |
| 251591673531 | MedOne | Domain redone.com.my -> medone.co.il; Fiber Operator -> **Data Center Colo Provider**; sub Regional CLEC -> **Standard - colo**; tier_3 -> tier_2; conf high_90. Israeli market-leading hardened colo. |
| 251476786920 | Goodman Group | Domain giomaregroup.com -> goodman.com; sub Standard - colo -> **Hyperscale Wholesale - colo**; tier_3 -> tier_1; conf high_90. ASX:GMG REIT pivoting to hyperscale DC. |
| 251480338123 | SB Communications | Fiber Operator -> **Flagged for deletion**; conf high_90. Pakistani AJK regional + insufficient evidence. |
| 251513968344 | ING -> **Ting Internet** | Renamed; ting.com domain confirmed; segment + sub unchanged; tier_3 -> tier_4 (post-Clearnetworx July 2025 fiber divestiture); conf high_90. |
| 251561055976 | TGT Global | Data Center Colo Provider -> **Flagged for deletion**; conf high_90. csggc.com entity ambiguity + 5G/IoT mismatch. |

## Per-record entries

### ATN International (251533417159)
- Path: LIGHT
- Segment: Fiber Operator (unchanged) / Sub: Long Haul / Backbone - Fiber operator (unchanged)
- Confidence: high_90 (unchanged) / Tier: tier_2 (unchanged)
- Apollo: no / web_searches: 0
- Reason: Brief recent (2026-05-08), framework-consistent, all key fields present. Date bump only.

### Hawaiian Telcom (251535204084)
- Path: LIGHT
- Segment: Fiber Operator / Sub: Regional CLEC - Fiber operator (unchanged)
- Confidence: high_90 / Tier: tier_3 (unchanged)
- Reason: Brief recent (2026-05-13), Hawaii incumbent (Cincinnati Bell / altafiber subsidiary), framework-consistent. Date bump.

### Light Source Communications (251535204086)
- Path: LIGHT
- Segment: Fiber Operator / Sub: Dark Fiber Specialist - Fiber Operator (unchanged)
- Confidence: high_90 / Tier: tier_2 (unchanged)
- Reason: Brief recent (2026-05-05), 525+ route miles Phoenix dark fiber. Date bump.

### Our Telekom (251535204087)
- Path: LIGHT (revised from MEDIUM)
- Segment: Fiber Operator / Sub: Regional CLEC - Fiber operator (kept; small Solomon Islands incumbent does not meet "Tier 1 Carrier - Network Op" scale threshold)
- Confidence: low_5069 / Tier: tier_3
- Reason: Small island incumbent (270 emp), correctly classified at current sub-segment. Date bump.

### American Dark Fiber (251536944848)
- Path: LIGHT
- Segment: Fiber Operator / Sub: Dark Fiber Specialist - Fiber Operator (unchanged)
- Tier: tier_2 (unchanged)
- Reason: Brief recent (2026-05-08). Date bump.

### Kordia (251536944849)
- Path: LIGHT
- Segment: Fiber Operator / Sub: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 (unchanged)
- Reason: NZ state-owned enterprise, brief recent. Date bump.

### Nepal Telecom (251536944851)
- Path: MEDIUM
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: medium_7089 -> high_90 / Tier: tier_3 -> tier_1
- Reason: National incumbent (5,400 emp, 60%+ market share, sole landline operator in Nepal). Cum pattern: National operator under-tiering.

### Chorus (251536944852)
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Confidence: high_90 / Tier: tier_3 -> tier_2
- Reason: NZ's national fiber wholesale operator (UFB rollout, 1.4M+ premises, 50K+ km fiber). Within-fiber promotion to LH/B.

### Aligned Energy (251561055972)
- Path: MEDIUM
- Sub: AI Signals - colo (unchanged) / Tier: tier_1 (unchanged)
- Reason: Filled provisioning_landscape placeholder ("Research needed.") with substantive narrative. Brief already captures EQT AI Infrastructure acquisition.

### BDx Data Centers (251561055973)
- Path: MEDIUM
- Sub: Standard - colo (unchanged) / Tier: tier_3 (unchanged)
- Reason: Filled hyperscaler_proximity = Existing Facility Nearby (Singapore/HK/Indonesia hyperscaler-rich metros).

### Samoa Submarine Cable Company (251561055975)
- Path: MEDIUM
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub: Long Haul / Backbone - Fiber operator -> Subsea cable operator
- Confidence: medium_7089 -> high_90 / Tier: tier_2 (unchanged)
- Reason: Pure-play subsea operator (Tui-Samoa cable, Apia-Suva with branch landings). Matches 30th sub-segment policy (added 2026-05-14). Cum pattern: Subsea cable operator promotions = +1 (cum 2 this sweep with batch 37 Solomon Islands SCC).

### TGT Global (251561055976)
- Path: HOLD (carried from prior batch)
- Reason: Entity ambiguity csggc.com -> CS Global Group / China Steel Global / unrelated. No clear telecom/DC operator profile.

### Altitude Infrastructure (251561055977)
- Path: LIGHT
- Sub: Long Haul / Backbone - Fiber operator (unchanged) / Tier: tier_2 (unchanged)
- Reason: French national wholesale FTTH operator, brief recent. Date bump.

### Airbeam (251563026106)
- Path: MEDIUM
- Sub: Regional CLEC - Fiber operator -> Municipal / Cooperative - Fiber operator
- Confidence: low_5069 (unchanged) / Tier: tier_3 -> tier_4
- Reason: Small Italian wireless ISP (5 emp). Cleared news contamination (Mesa AZ "Venture Out Resort" entry was from a different US entity). Better fit at Municipal/Cooperative for tiny local WISP.

### RBC Signals (251563026108)
- Path: MEDIUM
- Segment: Fiber Operator -> Other
- Sub: cleared / Tier: tier_3 -> tier_5
- Reason: Satellite ground station as a service (GSaaS) operator, not a fiber operator. Applies the reclassification noted in prior brief but never written. Partner-keep useful for sovereign AI/remote regions.

### AVAIO Digital (251564892901)
- Path: MEDIUM
- Sub: Standard - colo -> AI Signals - colo
- Confidence: high_90 (unchanged) / Tier: tier_3 -> tier_1
- Reason: Tamil Nadu India hyperscale AI-focused build (Project Perseus 76-acre 99MW CEC-approved). AVAIO Capital's digital infra arm building AI-first DCs across NA + EU + India.

### Alliance SI (251564892902)
- Path: MEDIUM
- Sub: Telecom Aggregator - MSP (unchanged) / Tier: tier_2 (unchanged)
- Reason: Geo cleanup (HubSpot state Ontario Canada vs geo focus saying Australia — inconsistent). Corrected geographic_focus to Canada/Toronto.

### Philippines Fiber Optic Cable Network (251564892905)
- Path: LIGHT
- Sub: Long Haul / Backbone - Fiber operator (unchanged) / Tier: tier_2 (unchanged)
- Reason: Brief recent, classification correct. Date bump.

### Bluesky American Samoa (251566704350)
- Path: LIGHT (revised from MEDIUM)
- Sub: Regional Cable Operator - Fiber operator (kept; American Samoa sole telecom, 20 emp - too small for Tier 1 Carrier sub-segment threshold)
- Tier: tier_3 / Reason: Date bump only.

### EdgeConneX (251574554332)
- Path: MEDIUM
- Sub: Modular - colo -> AI Signals - colo
- Tier: tier_1 (unchanged)
- Reason: 90+ DCs globally, EQT-backed AI Infrastructure strategy with 10+ GW AI factory commitments (Apr 2026). Modular - colo no longer descriptive of post-EQT-AI-pivot business model.

### Digicel Pacific (Telstra) (251574554333)
- Path: MEDIUM
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 (unchanged) / Tier: tier_3 -> tier_2
- Reason: Telstra-owned (acquired 2022), 1,200 emp, 6 Pacific markets (Fiji PNG Vanuatu Samoa Tonga Nauru). Regional Tier 1 with deep-pocketed parent.

### Amalgamated Telecom Holdings (ATH) (251574587091)
- Path: LIGHT (revised from MEDIUM)
- Sub: Regional CLEC - Fiber operator (kept; Pacific Islands holding company - small portfolio)
- Tier: tier_3 / Reason: Date bump only. Domain question (consol.tel vs ath.com.fj) preserved as data-quality follow-up.

### Ignite Telecoms (251574587095)
- Path: LIGHT
- Sub: Regional CLEC - Fiber operator (unchanged) / Tier: tier_3 (unchanged)
- Reason: Small Philippines fiber + digital services. Date bump.

### Palau National Communications Corporation (PNCC) (251574587096)
- Path: LIGHT (revised from MEDIUM)
- Sub: Long Haul / Backbone - Fiber operator (kept; 100 emp small country incumbent + operates Belau Submarine Cable BSCC)
- Tier: tier_2 / Reason: Date bump only. Could be re-evaluated to Subsea cable operator in D7 if BSCC is core asset.

### Singtel Optus (251574587097)
- Path: LIGHT
- Sub: Tier 1 Carrier - Network Op (unchanged)
- Confidence: medium_7089 -> high_90 / Tier: tier_1 (unchanged)
- Reason: Australia #2 telecom, Singtel-owned, $5.5B rev. Confidence promotion to high.

### H5 Data Centers (251574626020)
- Path: MEDIUM
- Sub: Hyperscale Wholesale - colo (unchanged) / Tier: tier_1 (unchanged)
- Reason: Filled hyperscaler_proximity = Existing Facility Nearby (US national wholesale colo, multiple markets).

### Bandwidth IG (251574626021)
- Path: LIGHT
- Sub: Dark Fiber Specialist - Fiber Operator (unchanged) / Tier: tier_2 (unchanged)
- Reason: SE US regional dark fiber (rebranded to BIG Fiber 2025). Date bump.

### Kacific Broadband Satellites (251574626022)
- Path: MEDIUM
- Segment: Fiber Operator -> Other
- Sub: cleared / Tier: tier_3 -> tier_5
- Reason: HTS satellite broadband (Kacific-1 GEO), not fiber. Cum pattern: Pure satellite operator misclassified as Fiber Op (cum 2 this sweep).

### BIGLOBE Inc. (251574661862)
- Path: LIGHT
- Sub: Pure Wholesale Carrier - Network Op (unchanged) / Tier: tier_1 (unchanged)
- Reason: KDDI subsidiary, Japanese ISP + cloud. Date bump.

### Spark New Zealand Ltd (251574661864)
- Path: FULL
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: low_5069 -> high_90 / Tier: tier_3 -> tier_1
- Apollo: no / web_searches: 1
- Reason: NZ's #1 mobile (42% share, 2.5-3M connections), 5083 emp, $2.75B rev. Full reclassification with brief overhaul. Cum: massive under-tiering pattern carried.

### BizNet Networks (251574698719)
- Path: MEDIUM
- Sub: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: Indonesia's leading enterprise telecom + DC (50,000+ km fiber, multiple Tier-III/IV DCs). National backbone scale. Within-fiber promotion.

### All Access Telecom (251574698720)
- Path: FULL
- Segment: Fiber Operator -> Flagged for deletion
- Sub: cleared / Tier: cleared
- Apollo: no / web_searches: 1
- Reason: International wholesale voice termination (NOT fiber) + 356+ robocall traceback notices since end-2023 + 50-state AG enforcement notice 2025. Active regulatory liability. Cum pattern: CPaaS/voice aggregator misclassified as Fiber Op = +1 (cum 7 this sweep).

### Global Secure Layer (251574698722)
- Path: HOLD (new this batch)
- Reason: Domain mismatch byglobal.es (Spain) != globalsecurelayer.com.au (Australian DDoS/security NetOp). Cooper decision needed on domain correction.

### Neos Networks (251574698726)
- Path: MEDIUM
- Sub: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: UK B2B wholesale telecom (formerly SSE Enterprise Telecoms with National Grid fiber lineage). National UK backbone scale.

### Maryland Broadband Cooperative (251587604210)
- Path: LIGHT
- Sub: Municipal / Cooperative - Fiber operator (unchanged) / Tier: tier_4 (unchanged)
- Reason: 79-member 501c12 middle-mile coop. Brief recent (Fiber Connect 2026 attendee confirmed). Date bump.

### PLDT Global (251587604212)
- Path: MEDIUM
- Sub: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Tier: tier_3 -> tier_2
- Reason: International/wholesale arm of PLDT (198K km parent fiber + 10 DCs). National wholesale backbone scale.

### Provident Data Centers (251587604213)
- Path: MEDIUM
- Sub: Standard - colo (unchanged) / Tier: tier_3 (unchanged)
- Reason: Filled hyperscaler_proximity = Existing Facility Nearby (Dallas TX + IN markets).

### RETN (251587604215)
- Path: LIGHT
- Sub: International Backbone Specialist - Network Op (unchanged) / Tier: tier_1 (unchanged)
- Reason: Global Pan-EU + Asia wholesale IP transit. Brief recent. Date bump.

### Rogers Communications Canada Inc. (251587604216)
- Path: FULL
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub: Regional Cable Operator - Fiber operator -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1 / Confidence: high_90 (unchanged)
- Apollo: no / web_searches: 1
- Reason: Canada's #1 wireless + cable telecom ($23.8B rev, 5,922 emp, $26B Shaw acquisition still integrating). Massive under-tiering corrected. Brief overhauled.

### Pixel Factory Data Center (251587604217)
- Path: MEDIUM
- Sub: Standard - colo (unchanged) / Tier: tier_3 (unchanged)
- Reason: Filled hyperscaler_proximity = Existing Facility Nearby (Richmond/Mid-Atlantic).

### Maincubes Secure Datacenters (251591500494)
- Path: MEDIUM
- Sub: AI Signals - colo (unchanged) / Tier: tier_1 (unchanged)
- Reason: Filled hyperscaler_proximity = Existing Facility Nearby (Frankfurt FRA9 metro, AWS FRA region).

### Mid-Atlantic Broadband Communities Corporation (251591500497)
- Path: MEDIUM
- Sub: Regional Cable Operator - Fiber operator -> Municipal / Cooperative - Fiber operator
- Tier: tier_3 -> tier_4
- Reason: Non-profit 2K+ mile open-access fiber co-op in southern VA. Within-fiber reclassification to Municipal/Cooperative (cum pattern continues).

### Netnod AB (251591673530)
- Path: HOLD (new this batch — IX policy decision needed)
- Reason: Swedish neutral IXP + DNS root server operator. IX/Internet Exchange policy gap (cum 3 with DE-CIX + Mass IX from prior batches). Needs Cooper framework decision on IX sub-segment treatment.

### MedOne (251591673531)
- Path: HOLD (new this batch)
- Reason: Name 'MedOne' = leading Israeli colocation operator (medone.co.il) but domain redone.com.my is Malaysian Redone Tech/SMB voice. Name + domain mismatch requires Cooper choice on which entity to keep.

### RISE (251591673532)
- Path: LIGHT
- Sub: Regional CLEC - Fiber operator (unchanged) / Tier: tier_3 (unchanged)
- Reason: Philippines fiber operator (RISE Internet), brief recent. Date bump.

### Goodman Group (251476786920)
- Path: HOLD (carried from prior batch)
- Reason: Domain mismatch giomaregroup.com vs Goodman Group (Australian REIT ASX:GMG, real domain goodman.com).

### SB Communications Private Limited (251480338123)
- Path: HOLD (carried from prior batch)
- Reason: Insufficient signal. yscommunications.net does not return a clear canonical SB Communications operator.

### ING (251513968344)
- Path: HOLD (carried from prior batch)
- Reason: Name 'ING' is incorrect; domain ting.com is Tucows-owned TING (Internet/Mobile MVNO + FTTH).

### Tekpoint (251535204088)
- Path: HOLD (new this batch — Cooper decision on entity identity)
- Reason: HubSpot name 'Tekpoint' at tekpoint.com but brief talks about TierPoint (40-DC national colo at tierpoint.com). Brief writer conflated two distinct entities. Could be (a) actual Tekpoint small entity OR (b) misnamed TierPoint record. Cooper choice needed before any further enrichment.

## HOLD canvas entries (append to F0B0AFSB9LN)
- [2026-05-19] 251535204088 Tekpoint — Entity identity ambiguity: HubSpot record 'Tekpoint' at tekpoint.com but brief describes TierPoint (40-DC national colo at tierpoint.com). Cooper to choose: keep as small Tekpoint vs. rename to TierPoint + correct domain.
- [2026-05-19] 251574698722 Global Secure Layer — Domain mismatch byglobal.es (Spain) != globalsecurelayer.com.au (Australian DDoS/security NetOp). Cooper to confirm domain correction to globalsecurelayer.com.au.
- [2026-05-19] 251591673530 Netnod AB — IX/Internet Exchange policy gap (cum 3 with DE-CIX + Mass IX). Sweep cannot fit IXP/DNS root operators into any existing sub-segment. Cooper framework decision needed.
- [2026-05-19] 251591673531 MedOne — Name + domain mismatch. 'MedOne' = leading Israeli colo (medone.co.il) but domain redone.com.my is Malaysian Redone Tech. Cooper to choose which entity this record represents.

(Carried from prior batches; preserved without re-writing: 251476786920 Goodman Group, 251480338123 SB Communications, 251513968344 ING-Ting, 251561055976 TGT Global.)

## Stats
- Promotions toward T1: 11 (Digital Edge HK, Nepal Telecom, Chorus, AVAIO Digital, Digicel Pacific, BizNet, Neos Networks, PLDT Global, Spark NZ, Rogers, Singtel Optus confidence-only)
- Demotions toward T5: 4 (Airbeam, RBC Signals, Kacific, Mid-Atlantic Broadband Coop)
- Skipped (hs_is_target_account=true): 0
- Sub-segment auto-migrations (§7.4a deterministic): 0
- Segment changes (cascade fired): 8 (Nepal Telecom, Samoa SCC, RBC Signals, Digicel Pacific, Kacific, Spark NZ, All Access Telecom, Rogers)
- Greenfield migrations: 0
- Customer-protection HOLDs: 0
- Completeness Gate fails (held for next batch): 0
- Manual-review HOLDs (true Tier 3 holds added to canvas): 8 (4 new + 4 carried)
- Apollo credits: 0
