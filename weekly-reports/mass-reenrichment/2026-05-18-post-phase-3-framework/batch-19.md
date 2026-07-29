# Mass Re-Enrichment Sweep — Batch 19

- **Sweep:** `2026-05-18-post-phase-3-framework`
- **Run date:** 2026-05-18
- **Batch size:** 50 (5 chunks of 10)
- **Processed:** 50/50
- **HOLD policy:** NONE
- **Apollo enforcement:** disabled
- **Apollo this batch:** 0 credits
- **Pool drain:** 1,855 → 1,805 (-50)

## Headline counts

| Outcome | Count |
|---|---|
| Flagged for deletion (hallucinated/defunct) | 3 (Caribbean Communications, AST Alcance, TeleSapiens Argentina) |
| Reclass to Other (chip/non-telecom/tower) | 2 (Symbio.one hydrogen fuel cell, Helios Towers passive infra) |
| Reclass Fiber Op → Network Op + Subsea cable operator | 2 (Interchange Vanuatu, BW Digital) |
| Reclass Fiber Op → MSP Cloud+Telecom Hybrid | 1 (Netline Chile) |
| Reclass Fiber Op → MSP Telecom Aggregator | 1 (On Air Telecom) |
| Reclass Network Op → MSP Cloud+Telecom Hybrid | 1 (Symbio Australia post-Aussie Broadband) |
| Reclass Colo → Fiber Op Muni/Coop | 1 (Auburn Essential Services) |
| Sub-seg shift within Fiber Op (CLEC → Cable Operator) | 1 (Telecable CR) |
| Sub-seg shift within Fiber Op (CLEC → Long Haul/Backbone) | 1 (NEDETEL Ecuador) |
| Sub-seg shift within NeoCloud (Large Scale GPU → Crypto to AI) | 1 (Northern Data Group, BTC heritage) |
| KEEP w/ cleaned brief + R3 dedup flagged | 37 |
| Tier writes explicit | 2 (Symbio.one → tier_5, Helios Towers → tier_5) |
| Tier writes skipped (target_account=true) | 24 |
| R3 dedup flags raised | 17 |

## Notable patterns this batch

- **2 mis-segmented "Other" reclasses surfaced**: Symbio.one is a French HYDROGEN FUEL CELL company misfiled as Fiber Op; Helios Towers is passive cell-tower infrastructure (not active carrier). Both reclassed to Other tier_5. Watch for more tower companies (American Tower, Crown Castle, IHS Towers, ATC Africa) and adjacent non-telecom entities (energy/fuel/EV companies) in subsequent batches.
- **High R3 dedup density (17 flags)**: ICON+→PLN, Ecuadortelecom→Claro/AM, Telsur→GTD, Totalplay Empresarial→Totalplay/Grupo Salinas, Iceblue→Resolute CS, Ooredoo Wholesale→Ooredoo Group, Smart Axiata→Axiata, TELESYSTEM→Block Comms, Symbio AU→Aussie Broadband, Northwestel→BCE/Bell, **5 NeoCloud-arm-shares-parent-domain** (Claro Brazil AI=claro.com.br, Tata Comms AI=tatacommunications.com, Singtel RE:AI=singtel.com, SoftBank AI Cloud=softbank.jp, YTL AI Cloud=ytl.com, TELUS Sovereign AI=telus.com from chunk 4). Cooper should sweep these in R3 next run.
- **Continuing Fiber Op Long Haul/Backbone narrowing**: NEDETEL Ecuador sub-seg shifted Regional CLEC → Long Haul/Backbone (national wholesale with 150+ POPs). Plus BW Digital + Interchange Vanuatu reclassed entirely to subsea operator.
- **NeoCloud chunk 5 was mostly clean**: 10 well-enriched established players (Cipher, Singtel RE:AI, SoftBank AI, YTL AI, Tata Comms AI, Northern Data, Scaleway, Civo, PoliCloud, etc.). Just needed datestamp refresh + R3 dedup tagging.
- **BTC-heritage NC5 routing**: Northern Data Group reclassed Large Scale GPU → Crypto to AI per Cooper's 2026-05-14 pattern (BTC mining heritage + active divest → NC5).
- **HubSpot search index lag**: Chunk 5's initial query returned chunk 4's just-written records (~1-2 min indexing delay). Resolved by using offset=10.

## Per-record summary (abbreviated)

### Chunk 1
- 318211867355 ZenFi Networks (NYC dark fiber): KEEP Fiber Op Dark Fiber Specialist; brief + 7 fields filled.
- 319151115981 Americatel Guatemala: KEEP Tier 1 CLEC; R3 dedup→Entel.
- 319126765244 Telecable CR: Sub-seg → Regional Cable Operator (cable MSO, not CLEC).
- 319134248697 Caribbean Communications: **FLAG** (unverifiable, state=Grande-Terre Guadeloupe wrong).
- 319134160609 Interchange Vanuatu: **RECLASS** Fiber Op → Network Op Subsea cable operator (ICN1/ICN2 owner).
- 297984383723 Auburn Essential Services: **RECLASS** Colo → Fiber Op Muni/Coop (Indiana muni FTTH+colo).
- 316498875122 BW Digital: **RECLASS** Colo → Network Op Subsea cable operator (Hawaiki owner; Cooper anchor list).
- 318097753791 Dark Fiber Group Norway: KEEP small Nordic niche specialist.
- 319154790129 AST Alcance El Salvador: **FLAG** (unverifiable).
- 319134192331 NEDETEL Ecuador: Sub-seg → Long Haul/Backbone (national wholesale 150+ POPs; UFINET merger).

### Chunk 2
- 319132424918 Indonesia Comnets Plus (ICON+): KEEP Long Haul/Backbone; R3 dedup→PLN.
- 318368579300 REV (LA): KEEP CLEC; brief trim.
- 319124960987 Ecuadortelecom: KEEP CLEC; R3 dedup→Claro Ecuador/Am Móvil (legal entity name).
- 319145743057 Copel Telecom: KEEP Long Haul/Backbone; ownership update (Bordeaux Fund Nov 2020 sale).
- 319151118042 Telsur Chile: KEEP CLEC; R3 dedup→GTD; industry tag flag.
- 319145754317 TeleSapiens Argentina: **FLAG** (EdTech platform, not telecom).
- 319135940326 Maxcom: KEEP CLEC.
- 319134249658 Coppernet Solutions Zambia: KEEP Long Haul/Backbone.
- 319151115995 CEMIG Telecom: KEEP Long Haul/Backbone; R3 dedup→CEMIG; domain `cetemig.com.br` flagged.
- 319151118057 Totalplay Empresarial: KEEP CLEC; R3 dedup→Totalplay/Grupo Salinas.

### Chunk 3
- 322761764551 Netline Chile: **RECLASS** Fiber Op → MSP Cloud+Telecom Hybrid (IIoT + cloud telephony focus).
- 316596757224 Iceblue Global: KEEP MSP Telecom Aggregator; R3 dedup→Resolute CS (2024 acq).
- 319154781896 Ooredoo Qatar Wholesale: KEEP Tier 1 Carrier; R3 dedup→Ooredoo Group.
- 319135943411 Alfa Lebanon: KEEP Tier 1 Carrier (state-managed MNO).
- 319147483840 Smart Axiata Cambodia: KEEP Tier 1 Carrier; R3 dedup→Axiata.
- 318219155162 DataCrunch → Verda: KEEP NeoCloud AI Infrastructure; rebrand noted.
- 316528134903 Symbio Australia: **RECLASS** Network Op → MSP Cloud+Telecom Hybrid; R3 dedup→Aussie Broadband (Feb 2024 acq).
- 318223234757 TELESYSTEM: KEEP CLEC; R3 dedup→Block Communications.
- 318338275038 Blue Dragon Network: KEEP Telecom Aggregator.
- 319151089365 FSM Telecommunications: KEEP Subsea cable operator (HANTRU-1 + EMCS landings).

### Chunk 4
- 318220838600 Northwestel Inc.: KEEP Tier 1 Carrier; R3 dedup→BCE/Bell (Northern Canada incumbent).
- 316517719776 On Air Telecom: **RECLASS** Fiber Op → MSP Telecom Aggregator (wholesale-only per FCC).
- 319135982321 Onemax DR: KEEP Tier 1 Carrier.
- 320873732840 Symbio.one France: **RECLASS to Other tier_5** (hydrogen fuel cell, NOT telecom).
- 319134249719 Helios Towers West Africa: **RECLASS to Other tier_5** (passive tower infrastructure, NOT carrier).
- 303405064913 Civo: KEEP Sovereign AI Clouds.
- 303424995021 PoliCloud: KEEP AI Infrastructure providers.
- 251659209450 TELUS Sovereign AI: KEEP Sovereign AI Clouds; **R3 dedup HIGH PRIORITY** (domain telus.com).
- 244551342805 Hive Digital: KEEP Crypto to AI Neoclouds.
- 240444244683 Scaleway: KEEP AI Infrastructure providers; R3 dedup→iliad.

### Chunk 5
- 303445636824 Aleria AI (UAE): LIGHT refresh, AI Infrastructure providers.
- 303449222869 Claro Brazil AI: LIGHT refresh; **R3 dedup HIGH PRIORITY** (domain claro.com.br).
- 303474610936 TensorPool (YC W25): LIGHT refresh.
- 303467192035 Koyeb: LIGHT refresh.
- 303925580513 Tata Comms AI Cloud: LIGHT refresh; **R3 dedup HIGH PRIORITY** (domain tatacommunications.com).
- 296850118389 Cipher Mining: LIGHT refresh ($8.5B AI contracts).
- 198403706562 Singtel RE:AI: LIGHT refresh; **R3 dedup HIGH PRIORITY** (domain singtel.com).
- 320811765449 SoftBank AI Cloud: LIGHT refresh; **R3 dedup HIGH PRIORITY** (domain softbank.jp).
- 303399663350 YTL AI Cloud: LIGHT refresh; **R3 dedup HIGH PRIORITY** (domain ytl.com).
- 240444199640 Northern Data Group: **SUB-SEG SHIFT** Large Scale GPU → Crypto to AI (BTC heritage per Cooper pattern).

## Apollo

Calls made: 0. Sweep cumulative unchanged.

## Pool drain progress

- Sweep starting pool: ~2,736
- Processed after batch 19: ~932 (34.1%)
- Remaining: ~1,805
- ETA at BATCH_SIZE=50: ~36 more batches
