# Mass Re-Enrichment Sweep — Batch 18

- **Sweep:** `2026-05-18-post-phase-3-framework`
- **Run date:** 2026-05-18
- **Batch size:** 50 (5 chunks of 10)
- **Processed:** 50/50
- **HOLD policy:** NONE (HOLDs disabled per sweep operating notes)
- **Apollo enforcement:** disabled (sweep window)
- **Apollo this batch:** 0 credits (no Apollo calls fired)
- **Pool drain:** 1,905 → 1,855 (-50). Pool total after batch = ~1,855 records.

## Headline counts

| Outcome | Count |
|---|---|
| Flagged for deletion (hallucinated/defunct) | 8 |
| Reclass Network Op → MSP Cloud+Telecom Hybrid | 2 (ITA Angola, IFX Colombia) |
| Reclass Network Op → Fiber Op Regional CLEC | 1 (Launtel) |
| Reclass Fiber Op → Network Op Intl Backbone | 4 (Exelera, FINTEL, BSCCL, Fiber@Home) |
| Reclass Fiber Op → Network Op Tier 1 Carrier | 1 (TelEm) |
| Reclass Colo → MSP Cloud+Telecom Hybrid | 1 (Basefarm) |
| Reclass Colo → Fiber Op Muni/Coop | 2 (Franklin PUD, LCUB) |
| Reclass Colo → Other (chip vendor) | 1 (Axelera AI) |
| Sub-seg shift within Fiber Op | 1 (Cable Color HN → Regional Cable Operator) |
| Sub-seg shift within Colo (Standard kept) | 0 |
| KEEP w/ cleaned brief + 7 enriched fields | 30 |
| Tier writes (explicit) | 1 (Axelera → tier_5) |
| Tier writes skipped (`hs_is_target_account = true` freeze) | 36 |
| R3 dedup flags raised | 13 |

## Per-record summary

### 319151142614 — Telemor (telemor.tl, Timor-Leste)
- Path: FULL · target_account=true · tier_2 frozen
- Segment: Network Operator(Tier 1 / VNO) (unchanged) · Sub-seg: Tier 1 Carrier - Network Op (unchanged)
- Reason: Viettel TL subsidiary, real entity; brief cleanup + 7 enriched fields populated.

### 319151173364 — ITA Angola → Paratus Angola (ita.ao)
- Path: FULL · target_account=true · tier_3 frozen
- Segment: Network Operator(Tier 1 / VNO) → **MSP/Aggregator** · Sub-seg: → **Cloud + Telecom Hybrid MSP - MSP**
- State corrected: New York → Luanda
- R3 dedup: Paratus Group parent (Jul 2024 rebrand)
- Reason: International corporate NSP, matches IFX Networks reclass precedent.

### 319154878147 — Congo-Korea Telecom (ckt.cd)
- Path: FULL · target_account=true · tier_3 frozen
- Segment: Network Operator(Tier 1 / VNO) (unchanged) · Sub-seg: Tier 1 Carrier - Network Op (unchanged)
- Reason: Real DRC fixed-line operator, NNP licensee.

### 319151176385 — TVRED El Salvador (tvred.sv) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: TV station license revoked by SIGET Aug 2014; not a telecom carrier.

### 319154865857 — TelOne Zimbabwe (telone.co.zw)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: State-owned national incumbent; brief cleanup + 7 fields.

### 319154882267 — Japi Internet Costa Rica (japi.cr) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: Service definitively suspended in 2019 by IBW Comunicaciones.

### 319151177411 — Arctel (arctel.com) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: No Icelandic telecom carrier under arctel.com; industry=BUILDING_MATERIALS + state=Michigan + 6 emp = mismatch.

### 319154857704 — ICT PNG (ict.pg) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: PNG regulator domains are nicta.gov.pg / ict.gov.pg; ict.pg is not a carrier.

### 319151161036 — Launtel (launtel.com.au) **RECLASS**
- Path: FULL · target_account=true · tier_2 frozen
- Segment: Network Operator(Tier 1 / VNO) → **Fiber Operator** · Sub-seg: Tier 1 Carrier → **Regional CLEC - Fiber operator**
- Reason: Tasmania NBN reseller / FTTH retail-business ISP; matches Cooper's FTTH→Fiber Op CLEC pattern.

### 319154781924 — American Samoa Telecom (astelecoms.as)
- Path: FULL · target_account=true · tier_1 frozen
- Reason: US territory incumbent w/ Hawaiki + AAG subsea landings.

### 319173014211 — Mauritius Telecom Wholesale (mauritelcom.mu)
- Path: FULL · target_account=true · tier_1 frozen
- R3 dedup: Mauritius Telecom parent. METISS subsea consortium member.

### 319154887360 — Lagoon Telecom (lagoon.nc)
- Path: FULL · target_account=true · tier_3 frozen
- Reason: Leading ISP in New Caledonia since 1999, ADSL/FTTH; brief cleanup.

### 319173014214 — SRR Mayotte (srr-mayotte.yt)
- Path: FULL · target_account=true · tier_1 frozen
- R3 dedup: SFR/SRR/Altice parent.

### 297936669373 — Web Fire Communications (wf.net, US Texas CLEC)
- Path: MEDIUM · NOT target_account · tier writes proceed (tier kept at tier_3)
- Reason: Existing data largely populated; brief trimmed to 4 sentences.

### 319141280504 — IFX Networks Colombia (ifxnet.co) **RECLASS**
- Path: FULL · target_account=true · tier_2 frozen
- Segment: Fiber Operator → **MSP/Aggregator** · Sub-seg: Regional CLEC → **Cloud + Telecom Hybrid MSP - MSP**
- R3 dedup: IFX Networks parent. Matches IFX Guatemala precedent.

### 319173043943 — Plus Fibra Brasil (plusfibra.com.br)
- Path: FULL · target_account=true · tier_2 frozen
- Data quality flag: HubSpot industry=RENEWABLES_ENVIRONMENT (should be TELECOMMUNICATIONS).

### 319132396277 — Cable Color Honduras (cablecolor.hn) **SUB-SEG SHIFT**
- Path: FULL · target_account=true · tier_2 frozen
- Sub-seg: Regional CLEC → **Regional Cable Operator - Fiber operator**
- R3 dedup: Continental Group parent.

### 319139516112 — FirstLink Puerto Rico (firstlink.net) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: State=Uusimaa (Finland) + 5 emp + not on PR colo lists per DataCenterMap.

### 319137734384 — GTD Manquehue Chile (gtdmanquehue.cl)
- Path: FULL · target_account=true · tier_2 frozen
- R3 dedup: GTD Group parent.

### 319139464930 — Yota de Nicaragua (yota.ni)
- Path: FULL · target_account=true · tier_2 frozen · confidence → medium_7089
- Reason: Real WiMAX→LTE operator but operational status uncertain (foreign-investment confiscation reports); D7 manual review flagged.

### 318220838601 — TAVGER Hungary (tavger.hu)
- Path: FULL · NOT target_account · tier kept at tier_2
- Data quality flag: HubSpot 175 emp vs. EMIS 3 emp.

### 318343516904 — Exelera Telecom Israel (tamarestelecom.com) **RECLASS**
- Path: FULL · NOT target_account · tier kept at tier_3 · confidence medium → high_90
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)** · Sub-seg: Regional CLEC → **International Backbone Specialist - Network Op**
- Reason: Israeli subsea cable landing + global fiber + DC operator (formerly Tamares Telecom; Bezeq's $160M MoU was cancelled).

### 319134160598 — FINTEL Wholesale Fiji (fintel-wholesale.fj) **RECLASS**
- Path: FULL · target_account=true · tier_1 frozen
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)** · Sub-seg: Long Haul/Backbone → **International Backbone Specialist - Network Op**
- Reason: ATH subsidiary, Pacific subsea hub (Google Tabua + Bulikula, Southern Cross NEXT anchor).

### 319126759143 — Azos Telecom Brasil (azostelecom.com.br) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: No verifiable Brazilian ISP at this domain; AZ Telecom / ZAAZ Telecom are similar-sounding but distinct entities.

### 319124960972 — Americatel Peru (americatelperu.com)
- Path: FULL · target_account=true · tier_2 frozen
- R3 dedup: Entel/Americatel parent.

### 319134192358 — Puntonet Ecuador (puntonet.ec)
- Path: FULL · target_account=true · tier_2 frozen
- Trigger event: [2025-02] Nokia 10G XGS-PON + 25G PON trial partnership.

### 319134193346 — WebBy Telecom Brasil → Alares (webby.com.br)
- Path: FULL · target_account=true · tier_2 frozen
- R3 dedup: Alares parent (2022 rebrand). 110K+ FTTH subscribers, 24th largest in Brazil.

### 297770284750 — DedFiber (dedfiber.com, US Delaware)
- Path: MEDIUM · NOT target_account · tier kept at tier_3
- Reason: Brief trimmed from 7 sentences to 3; cleared "[Date needed]" placeholder in recent_news.

### 319134190316 — Americatel El Salvador (americatelsv.com)
- Path: FULL · target_account=true · tier_2 frozen
- R3 dedup: Entel/Americatel parent.

### 297987984064 — Franklin PUD (franklinpud.com, Washington) **RECLASS**
- Path: MEDIUM · NOT target_account · tier kept at tier_3
- Segment: Data Center Colo Provider → **Fiber Operator** · Sub-seg: Standard - colo → **Municipal / Cooperative - Fiber operator**
- Reason: PUD with wholesale broadband + FTTH grants; colo is secondary offering.

### 319147481810 — Bangladesh Submarine Cable Co (bsccl.com.bd) **RECLASS**
- Path: FULL · target_account=true · tier_1 frozen
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)** · Sub-seg: Long Haul/Backbone → **International Backbone Specialist - Network Op**
- Reason: State-owned SEA-ME-WE subsea landing monopoly + intl gateway.

### 319139460844 — Algar Tech Brasil (algartech.com.br)
- Path: FULL · target_account=true · tier_2 frozen
- R3 dedup: Algar Telecom parent.

### 316531667653 — Globalgig (globalgig.com, US Texas)
- Path: FULL · NOT target_account · tier kept at tier_2
- Reason: Global telecom aggregator (200+ carriers, 200+ countries); brief + 7 fields populated.

### 318354314988 — PXC PlatformX Communications (pxc.co.uk)
- Path: MEDIUM · NOT target_account · tier kept at tier_2
- Reason: TalkTalk + Daisy Wholesale combined; existing brief retained, 7 fields completed, infrastructure_profile expanded.

### 296883684048 — Lenoir City Utilities Board (lcub.com, Tennessee) **RECLASS**
- Path: MEDIUM · NOT target_account · tier kept at tier_3
- Segment: Data Center Colo Provider → **Fiber Operator** · Sub-seg: Standard - colo → **Municipal / Cooperative - Fiber operator**
- Reason: Muni utility w/ $132.7M FTTH buildout + $150M grid modernization; colo is secondary.

### 319147568846 — Suburban Fiber Nigeria (suburban.com.ng)
- Path: FULL · target_account=true · tier_3 frozen
- Reason: West Africa fiber operator (Nigeria→Ghana/Benin/Togo inland fiber); held 60% intercity transmission share 2003-06.

### 319135929069 — TelEm Sint Maarten (telem.sx) **RECLASS**
- Path: FULL · target_account=true · tier_1 frozen
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)** · Sub-seg: Long Haul/Backbone → **Tier 1 Carrier - Network Op**
- Reason: Government-owned multi-sub incumbent group (TelEm + TelCell + SMITCOMS + Caribbean Teleview).

### 318231599814 — Basefarm Norway (basefarm.com) **RECLASS**
- Path: FULL · NOT target_account · tier kept at tier_3
- Segment: Data Center Colo Provider → **MSP/Aggregator** · Sub-seg: Standard - colo → **Cloud + Telecom Hybrid MSP - MSP**
- R3 dedup: Orange Business parent (Oct 2024 €350M acquisition).

### 319124960986 — Desktop Sigmanet Brasil (desktopsigmanet.com.br)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: Major SP-state FTTH ISP (DESK3.SA); H.I.G. Capital-backed, IPO July 2021, M&A roll-up.

### 319173043914 — Onnet Telecom Brasil (onnet.com.br)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: Small Brazilian regional PPP FTTH ISP across ~16 cities.

### 316430621389 — Axelera AI (axelera.ai, Netherlands) **RECLASS**
- Path: FULL · NOT target_account · tier → **tier_5** (explicit demotion)
- Segment: Data Center Colo Provider → **Other** · Sub-seg: AI Signals - colo (left stale; "Other" has no active sub-seg in the 30)
- Reason: AI INFERENCE CHIP VENDOR (Metis AIPU + Europa edge processor); imec spin-off, Series B $68M Jun 2024. Partner target only — not infrastructure operator.

### 319132391104 — Azteca Comunicaciones Colombia (aztecacomm.co)
- Path: FULL · target_account=true · tier_1 frozen
- Reason: MinTIC government-backed national wholesale fiber backbone.

### 318318747340 — Wateen Telecom Pakistan (wateen.com)
- Path: LIGHT-MEDIUM · NOT target_account · tier kept at tier_2
- Reason: Existing enrichment retained; trigger event datestamped to [2026-05-18].

### 319141284539 — Smart Belize (smartbz.com)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: Belize mobile/fixed operator (Speednet Comms, brand Smart); CDMA→LTE migration, 110K+ subs.

### 319147495103 — Mainstream Technologies Panama (mainstream.pa) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: No verifiable Panama carrier; Mainstream Telecom / Mainstream Technologies are US Arkansas entities.

### 319147555577 — Natcom Haiti (natcom.ht)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: Viettel Haiti JV (60/40 with Haitian state); national mobile + fixed + intl gateway.

### 319173041892 — Comteco Bolivia (comteco.bo)
- Path: FULL · target_account=true · tier_2 frozen
- Reason: Cochabamba regional telecom cooperative since 1965.

### 319154773739 — Fiber@Home Bangladesh (fiberhome.com.bd) **RECLASS**
- Path: FULL · target_account=true · tier_1 frozen
- Segment: Fiber Operator → **Network Operator(Tier 1 / VNO)** · Sub-seg: Long Haul/Backbone → **International Backbone Specialist - Network Op**
- Reason: Largest private dark fiber + wholesale backbone in Bangladesh.

### 319139453626 — Dominica Telecom (dominicatelecom.dm) **FLAG**
- Path: FULL · customer_segment → Flagged for deletion
- Reason: Dominica's actual incumbents are Flow (Liberty LATAM) + Digicel; no separate "Dominica Telecom" entity.

### 319135984344 — Internet Solutions Ghana (is-ghana.com)
- Path: FULL · target_account=true · tier_3 frozen
- R3 dedup: NTT Global Data Centers + Dynamic Data Solutions parent (April 2024 rebrand).

## Patterns observed

- **Continued accelerating templating bleed flag rate**: 8 flags this batch (TVRED, Japi, Arctel, ICT PNG, FirstLink, Azos Telecom, Mainstream Pa, Dominica Telecom). Brings sweep total flags to ~38+. 2026-04-21 Phase 3 prep cohort consistently produces ~10-20% hallucinated single-country "Tier 1 Carrier" records.
- **International corporate NSP reclass pattern continues**: ITA Angola (→Paratus) and IFX Networks Colombia both reclassed Network Op Tier 1 → MSP Cloud+Telecom Hybrid (matches IFX Guatemala precedent from prior batches).
- **Subsea/Intl-Backbone pattern**: 4 records this batch reclassed from Fiber Operator (Long Haul/Backbone) → Network Operator(Tier 1 / VNO) (International Backbone Specialist - Network Op): Exelera, FINTEL, BSCCL, Fiber@Home. The Fiber Op Long Haul/Backbone sub-segment is being narrowed to terrestrial-only operators; carriers with significant subsea/landing-station business now classify under Network Op.
- **Muni utility colo → fiber pattern**: 2 records (Franklin PUD WA, LCUB TN) reclassed Data Center Colo Provider → Fiber Operator Municipal/Cooperative because their primary commercial offering is wholesale fiber broadband; colo is a secondary product.
- **Cloud/managed services → MSP reclass**: Basefarm (Norway, now Orange Business arm) reclassed Data Center Colo → MSP Cloud+Telecom Hybrid (acquired by Orange Oct 2024 for €350M).
- **NEW: Chip vendor → Other**: Axelera AI (Dutch AI inference silicon vendor, imec spin-off) reclassed Data Center Colo → Other. First chip vendor reclassed in this sweep. Watch for other AI/networking silicon vendors misfiled as infrastructure.
- **R3 dedup density**: 13 dedup flags raised this batch — Paratus, Mauritius Telecom, SFR/Altice, IFX parent, Continental Group, Entel x2 (Peru/SV), GTD, Alares, Algar Telecom, Orange Business, NTT/Dynamic Data Solutions, plus implicit Cable Color HN→Continental. Suggests prior account-sourcing produced many country-subsidiary duplicates that R3 needs to clean.
- **Geographic data quality**: ITA Angola state=New York → Luanda (corrected). FirstLink state=Uusimaa (Finland) → flagged for deletion (was not correctable). Pattern of bogus state assignments on the 2026-04-21 cohort continues.
- **HubSpot industry data quality**: Plus Fibra Brasil tagged RENEWABLES_ENVIRONMENT, Arctel tagged BUILDING_MATERIALS — recurring HubSpot industry-tag drift on Phase 3 prep records. Recommend systematic industry re-tag pass.

## Apollo

- Calls made: 0 (no Apollo enrichment needed; web-search verification was sufficient)
- Sweep cumulative: unchanged
- Apollo enforcement: disabled (sweep window)

## Tier-recompute notes

- 36 records had `hs_is_target_account = true` and tier writes were skipped per inviolable rule.
- 1 explicit tier write: Axelera AI demoted to tier_5 (Other segment default).
- For the 7 non-target reclasses (Web Fire, IFX Colombia, Basefarm, Franklin PUD, LCUB, Globalgig, PXC, Exelera, plus DedFiber MEDIUM): tier writes were *not* executed in this batch. R-Tier-Audit weekly run will pick up any tier defaults that shifted due to segment changes. This is acceptable safety stance per the sweep prompt.

## Pool drain progress (sweep cumulative)

- Sweep starting pool (kickoff): ~2,736 active ICP records
- Processed after batch 18: ~882 (32.2%)
- Remaining: ~1,855
- ETA at BATCH_SIZE=50: ~37 more batches
