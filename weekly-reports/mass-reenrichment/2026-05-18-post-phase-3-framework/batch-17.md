# Mass Re-Enrichment Sweep — Batch 17

**Sweep:** 2026-05-18-post-phase-3-framework
**Date:** 2026-05-18
**Records processed:** 50 / 50
**Pool drain:** 1,954 → 1,904 (50 records written, 2.6% additional drain)
**Sweep cumulative drain:** ~832 / 2,715 (~30.6%)
**Apollo this batch:** 0
**Path mix:** 50 MEDIUM / 0 FULL / 0 LIGHT / 0 HOLD

All 50 records came from the 2026-04-21 Phase 3 prep cohort of `target_account=true` international "Tier 1 Carrier - Network Op" records carrying the universal templating bleed ("[Country] [Name], carrier/MNO with external extension motion to business customers. Regional wholesale partnerships."). All carry `hs_is_target_account=true` so account_tier writes were skipped per spec; segment / sub-segment / 7 enriched fields / brief / segmentation_confidence writes proceeded normally.

## Chunk 1 (records 1-10)

### Telecom Niue (Rocket Systems) (319135911643)
- Path: MEDIUM
- Domain: teliani.nu → telecomniue.com (MISDOMAIN)
- Segment: unchanged (Network Operator Tier 1 / VNO)
- Sub-segment: unchanged (Tier 1 Carrier - Network Op)
- Confidence: high_90 → medium_7089
- Tier: skipped (target_account=true)
- Reason: Niue SOE, Manatua Consortium founding member. Domain corrected; enriched fields filled.

### SkyCable Corporation (319134216949)
- Path: MEDIUM
- Sub-segment: Tier 1 Carrier - Network Op → Cable MSO Enterprise Division - Network Op
- Confidence: high_90 → medium_7089
- R3 dedup flag: vs PLDT parent (acquired SkyCable broadband+cable assets May 2023)

### SRG (319132458692)
- Path: MEDIUM
- Sub-segment: Tier 1 Carrier - Network Op → Cable MSO Enterprise Division - Network Op
- R3 dedup flag: vs Cable Bahamas parent (acquired SRG/IndiGo 2011)

### Hafa Adai Communications (319134261952)
- Path: MEDIUM → EVICTION
- Segment: Network Operator(Tier 1/VNO) → Flagged for deletion
- Reason: Not an independent carrier - prepaid SIM/eSIM tourist product brand of IT&E (real Guam carrier).

### Sunbeach (319134254780)
- Path: MEDIUM
- Sub-segment: unchanged
- Confidence: high_90 → medium_7089
- Reason: Real Barbados ISP+mobile (BSE-listed); templating cleanup + enriched fields filled.

### Powertel Communications (319126833889)
- Path: MEDIUM
- Data fix: state="Alabama" cleared (Zimbabwe entity)
- Confidence: high_90 → medium_7089
- Reason: ZESA-owned Zimbabwe fiber operator; Seacom subsea handoff; Paratus JV.

### Now Telecom (319134216948)
- Path: MEDIUM
- Confidence: high_90 → medium_7089
- Reason: Existing brief already non-templated; filled remaining 6 enriched fields.

### Smart Telecom Uganda (319132461809)
- Path: MEDIUM → EVICTION
- Segment: Network Operator(Tier 1/VNO) → Flagged for deletion
- Reason: DEFUNCT - ceased operations 2021-08-31; subscribers absorbed by MTN, Airtel, Axian Telecom.

### Anguilla Telecom (319132457666)
- Path: MEDIUM → EVICTION
- Segment: Network Operator(Tier 1/VNO) → Flagged for deletion
- Reason: No real entity at angliaphone.ai; real Anguilla carriers are Digicel + Flow. Hallucinated record.

### Zeop (319134246587)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → Fiber Operator
- Sub-segment: Tier 1 Carrier - Network Op → Regional CLEC - Fiber operator
- Reason: Reunion FTTH/FTTR pioneer, ~500 emp. Clear fiber operator, not a Tier 1 carrier.

## Chunk 2 (records 11-20)

### Telecel Faso (319134256849)
- Path: MEDIUM; templating cleanup; Burkina Faso 3rd-largest MNO; 300-site state-backed expansion noted.

### Karib Telecom (319132457671)
- Path: EVICTION → Flagged for deletion
- Reason: Hallucinated record; real BVI carriers are CCT, Digicel, Flow.

### Turknet (319135948527)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → Fiber Operator
- Sub-segment: Tier 1 Carrier - Network Op → Regional CLEC - Fiber operator
- Reason: Turkish FTTH+enterprise alt-carrier, not a national incumbent.

### Dataco PNG (319134245594)
- Path: MEDIUM; PNG state wholesale fiber+Kumul subsea; enriched fields filled.

### Multilink (319137787625)
- Path: MEDIUM; Haitian ISP since 1999; WiMAX license holder; confidence medium_7089.

### Bluesky Samoa (319139433174)
- Path: MEDIUM; existing brief OK; filled enriched fields. Digicel Pacific sub. SSCC founding shareholder.

### Moratelindo (319137756912)
- Path: MEDIUM; existing brief OK; filled enriched fields; Indonesian wholesale fiber backbone.

### MTL (Malawi Telecommunications Limited) (319139517120)
- Path: MEDIUM → MISDOMAIN + RENAME
- Name: "Malawi Telecom" → "MTL (Malawi Telecommunications Limited)"
- Domain: malawi-telecom.mw → mtl.mw
- Reason: HubSpot record was a templated stub; corrected to canonical MTL entity (TNM co-founder, Malawi fixed-line incumbent).

### Digicel Martinique (319137786605)
- Path: MEDIUM; R3 dedup flag vs Digicel Group parent (D2 wholesale-arm policy).

### SPT Wallis et Futuna (319139433179)
- Path: MEDIUM; existing brief OK; filled enriched fields. French overseas territory incumbent.

## Chunk 3 (records 21-30)

### Uniti Wireless (319139513059)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → Fiber Operator
- Sub-segment: Tier 1 Carrier - Network Op → Regional CLEC - Fiber operator
- Reason: Morrison/Brookfield/CSC consortium-owned Australian greenfield FTTH leader; clear fiber operator.

### bmobile Solomon Islands (319141352154)
- Path: MEDIUM → MISDOMAIN
- Domain: bmobilesb.sb → bmobile.com.sb
- Notable signal: Recently launched Lynk sat2phone satellite-to-mobile service - one of first global MNOs.

### NationLink (319139523298)
- Path: MEDIUM; Somali B2B ISP; templating cleanup + enriched fields.

### Newcom Honduras (319137792711)
- Path: MEDIUM; absorbed by Millicom Cable Honduras via AMNET merger; R3 dedup flag vs Millicom parent. Confidence low_5069.

### CityNet Philippines (319145768664)
- Path: MEDIUM; existing brief OK; filled enriched fields.

### IFX Networks Guatemala (319141366515)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → MSP/Aggregator
- Sub-segment: Tier 1 Carrier - Network Op → Cloud + Telecom Hybrid MSP - MSP
- Reason: IFX Networks #1 LATAM MSP w/ 130K km fiber + 24 DCs across 18 countries. New Tier III Guatemala DC 2025 ($65M, 128 racks). R3 dedup flag vs IFX parent record.

### Digicel Suriname (319141365444)
- Path: MEDIUM; R3 dedup flag vs Digicel Group parent.

### Telma Telecom Malagasy (319145797348)
- Path: MEDIUM; Madagascar incumbent (Axian Group); LION cable consortium member.

### Vivatel (319141363396)
- Path: MEDIUM; Tanzanian smaller ISP; confidence low_5069 (thin web evidence).

### Simbanet Uganda (319141363390)
- Path: MEDIUM; Ugandan smaller ISP; confidence low_5069 (thin web evidence).

## Chunk 4 (records 31-40)

### Flow Barbados (319141367539)
- Path: MEDIUM; R3 dedup flag vs Liberty LATAM / Flow Caribbean parent.

### Marshall Islands NTA (319145726678)
- Path: MEDIUM; state="California" cleared; HANTRU-1 subsea cable operator.

### Qualitynet Kuwait (319147571900)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → MSP/Aggregator
- Sub-segment: Tier 1 Carrier - Network Op → Cloud + Telecom Hybrid MSP - MSP
- Reason: Kuwait #1 enterprise ICT/Internet provider; acquired by stc Kuwait Nov 2018 for $92.8M. R3 dedup flag vs stc Kuwait parent.

### Tonga Communications Corporation (319151089373)
- Path: MEDIUM; industry="HIGHER_EDUCATION" → "TELECOMMUNICATIONS"; SOE incumbent + Tonga Cable subsea.

### DGtek (319151160043)
- Path: MEDIUM → SEGMENT FLIP + MISDOMAIN
- Domain: dgtek.com.au → dgtek.net
- Segment: Network Operator(Tier 1/VNO) → Fiber Operator
- Sub-segment: Tier 1 Carrier - Network Op → Regional CLEC - Fiber operator
- Reason: Independent Australian FTTP carrier, 100K+ premises in Melbourne metro; acquired FG Telecom.

### Cable & Wireless Seychelles (319151089360)
- Path: MEDIUM; existing brief OK; filled enriched fields. Liberty LATAM operating arm.

### Only Mayotte (319147572975)
- Path: MEDIUM → MISDOMAIN
- Domain: only-mayotte.yt → only.yt
- R3 dedup flag vs Telecom Reunion Mayotte (TRM, Iliad/Axian JV) parent.

### Vodafone Greece Wholesale (319151161037)
- Path: MEDIUM; state="Stockholm County" cleared; R3 dedup flag vs Vodafone Greece parent.

### TTCL Tanzania Telecommunications (319151168188)
- Path: MEDIUM; Tanzania incumbent, state-controlled.

### Paircom (319145818814)
- Path: EVICTION → Flagged for deletion
- Reason: No real Nigerian operator found at paircom.com.ng. Hallucinated record.

## Chunk 5 (records 41-50)

### Tuvalu Telecommunications Corporation (319147475672)
- Path: MEDIUM; existing brief OK; filled enriched fields. VAKA subsea cable / Google Pacific Connect.

### Digicel TCI (319145813720)
- Path: MEDIUM; R3 dedup flag vs Digicel Group parent.

### Symphony Communications (319147525818)
- Path: MEDIUM; existing brief OK; filled enriched fields. Thai enterprise ISP.

### LICT (319147562721)
- Path: HOLD-equivalent → D7 escalation (confidence low_5069)
- Reason: lict.net entity does not match real A&B carriers (APUA/Flow/Digicel/ACT). 342 Apollo employees suggests real business but classification uncertain; possibly Lynch Interactive Corp (US rural ILEC) misfiled under A&B country. Escalate to D7.

### ETL Enterprise Telecom Lao (319147521753)
- Path: MEDIUM; existing brief OK; filled enriched fields. Laotian incumbent state-controlled.

### Digicel Guyana (319147570928)
- Path: MEDIUM; R3 dedup flag vs Digicel Group parent.

### Basslink Telecoms (319147546308)
- Path: MEDIUM → SEGMENT FLIP
- Segment: Network Operator(Tier 1/VNO) → Fiber Operator
- Sub-segment: Tier 1 Carrier - Network Op → Dark Fiber Specialist - Fiber Operator
- Reason: Telecom arm of Basslink HVDC interconnector; dark fiber on 370km Bass Strait subsea route. Hydro Tasmania owned since 2022. Only diverse Tasmania-mainland subsea fiber path.

### Kidanet (319145823968)
- Path: MEDIUM → MISDOMAIN
- Domain: kidanet.fj → kidanet.com.fj
- R3 dedup flag vs FINTEL/ATH (Amalgamated Telecom Holdings) parent.

### Montserrat Telecom (319145814739)
- Path: EVICTION → Flagged for deletion
- Reason: Hallucinated record at montserrat-telecom.ms. Real Montserrat operators are Flow + Digicel.

### Access Communications (319151173350)
- Path: MEDIUM; state="Southern Region" cleared; smaller Malawian B2B ISP; MACRA licensed.

---

## Patterns observed this batch

- **Phase 3 prep international `target_account=true` cohort dominates (all 50)** - same "[Country] [Name], carrier/MNO with external extension motion to business customers" templating bleed continues. Templating cleanup is universal across this cohort.
- **6 hallucinated records → Flagged for deletion this batch** (Hafa Adai SIM brand, Anguilla Telecom, Karib Telecom BVI, Paircom Nigeria, Montserrat Telecom, plus the defunct Smart Telecom Uganda). The pattern of tiny-country "Tier 1 Carrier" records with no matching real entity at the listed domain is accelerating - ~30+ total this sweep.
- **6 segment flips** Network Op → Fiber Operator OR MSP/Aggregator: Zeop, Turknet, Uniti Wireless, DGtek (→ Fiber Op Regional CLEC); IFX Networks Guatemala, Qualitynet Kuwait (→ MSP Cloud+Telecom Hybrid); Basslink Telecoms (→ Fiber Op Dark Fiber Specialist).
- **9 R3 dedup flags raised**: SkyCable→PLDT; SRG→Cable Bahamas; Digicel Martinique/Suriname/TCI/Guyana→Digicel Group; Newcom Honduras→Millicom; IFX Networks Guatemala→IFX parent; Flow Barbados→Liberty LATAM; Qualitynet Kuwait→stc Kuwait; Only Mayotte→TRM/Iliad; Vodafone Greece Wholesale→Vodafone Greece; Kidanet→FINTEL/ATH.
- **5 MISDOMAIN corrections**: Telecom Niue (teliani.nu→telecomniue.com), MTL (malawi-telecom.mw→mtl.mw), bmobile Solomon Islands (bmobilesb.sb→bmobile.com.sb), DGtek (dgtek.com.au→dgtek.net), Only Mayotte (only-mayotte.yt→only.yt), Kidanet (kidanet.fj→kidanet.com.fj). 6 total.
- **Data quality fixes**: Powertel state=Alabama cleared (Zimbabwe entity), Marshall Islands NTA state=California cleared, Vodafone Greece Wholesale state=Stockholm cleared, Access Communications state="Southern Region" cleared, Tonga Communications industry=HIGHER_EDUCATION → TELECOMMUNICATIONS.
- **1 D7 escalation**: LICT (Antigua, lict.net) - entity uncertain, 342 employees suggests real business, but no match to known A&B carriers.

## Continuing patterns from prior batches

- Tier 1 Carrier - Network Op cohort from Phase 3 prep is still being unwound. Many records were templated en-masse on 2026-04-21 with `target_account=true` set en-masse; sweep is the cleanup pass. The volume of `target_account=true` records with templating bleed remains the dominant pattern.
- Hallucinated single-country "Tier 1 Carrier" records continue to surface (now ~30+ this sweep). Recommend Cooper review the source of the 2026-04-21 import batch.
- target_account=true freeze on tier is being honored on every record; segment/sub-segment can still flip when classification evidence is clear.

