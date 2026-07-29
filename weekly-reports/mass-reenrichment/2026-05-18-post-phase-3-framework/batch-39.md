# Mass Re-Enrichment Sweep - Batch 39

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 39
**Date:** 2026-05-19
**Processed:** 50 / 50
**Path mix:** LIGHT 37 · MEDIUM 1 · RECLASSIFY 4 · HOLD 8
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Pool drain:** 901 -> ~851 remaining

---

## Reclassifications (4)

### Aqua Comms (251593554633)
- Path: RECLASSIFY (light-FULL, framework decision)
- Domain: aquacomms.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Long Haul / Backbone - Fiber operator -> Subsea cable operator
- Confidence: high_90 -> high_90
- Tier: tier_2 -> tier_2 (unchanged)
- Reason: Pure-play subsea cable operator (AEC1/AEC2 transatlantic systems). Per Phase 3 framework, "Subsea cable operator" is the 30th sub-segment under Network Operator parent (added 2026-05-14). Acquired by EXA Dec 2025 but still operates as a subsea-specialist subsidiary. CLAUDE.md lists Aqua Comms as a verified HIGH anchor for this sub-segment.
- Apollo used: no  ·  web_searches: 0  ·  Completeness Gate: pass

### GCX - Flag Telecom (251593618169)
- Path: RECLASSIFY
- Domain: globalcloudxchange.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Tier 2 National Wholesale - Fiber operator -> Subsea cable operator
- Confidence: high_90 -> high_90
- Tier: tier_2 -> tier_2 (unchanged)
- Reason: GCX (Global Cloud Xchange) operates FLAG and FALCON subsea cable systems globally (RCom/Reliance-owned). Per Phase 3, GCX is the OPERATOR of these cables (not the consortium - consortiums like FLAG-the-consortium are D1-evicted). Operator-of-record entities classify as Subsea cable operator. Recent ECHO subsea fiber-pair acquisition (2025-12-15) reinforces subsea-specialist positioning.
- Apollo used: no  ·  web_searches: 0  ·  Completeness Gate: pass

### DayOne (251659209448)
- Path: RECLASSIFY
- Domain: dayone.global (unchanged)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo -> Hyperscale Wholesale - colo
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Reason: Singapore-HQ hyperscale DC platform spun out of GDS Jan 2025. $2.0B+ Series C announced 2026-01-13. Hyperscale-only customer base across APAC + Europe. Aligns with Hyperscale Wholesale - colo per Phase 3 framework. The existing brief already noted "Tier upgrade T2->T1 DCCP" intent but the sub-segment hadn't been moved.
- Apollo used: no  ·  web_searches: 0  ·  Completeness Gate: pass

### SUBCO (251725788868)
- Path: RECLASSIFY
- Domain: sub.co (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional Cable Operator - Fiber operator -> Subsea cable operator
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_3 (unchanged)
- Reason: Bevan Slattery-founded subsea cable developer/operator (SMAP hypercable, Oman Australia Cable). "Regional Cable Operator" sub-segment was a misclassification - that label is for cable MSO/HFC operators (Comcast/Charter type), not submarine cable. Per Phase 3, SUBCO is a textbook Subsea cable operator anchor. Small operator (10-66 emp) so tier_3 retained.
- Apollo used: no  ·  web_searches: 0  ·  Completeness Gate: pass

---

## MEDIUM (1)

### EcoDataCenter (251593660098)
- Path: MEDIUM (state correction)
- Domain: ecodatacenter.se (unchanged)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo (unchanged)
- Tier: tier_3 (unchanged)
- State patch: "State of Rio de Janeiro" -> "Dalarna County" (Falun is in Dalarna County, Sweden; the Brazilian state was a stale Apollo artifact from a prior MISDOMAIN incident)
- Reason: Country was already Sweden; state field was the only inconsistency.
- Apollo used: no  ·  web_searches: 0

---

## LIGHT (37) - date bump only, no other changes

All 37 records below were enriched within the last 7-14 days under the current Phase 3 framework. Sub-segments are in the 30 active values, tier matches defaults, 7 enriched fields are present. Tier recompute is a no-op (no signal modifiers active per query). `last_enriched_date` stamped to 2026-05-19.

| ID | Name | Segment | Sub-segment | Tier |
|---|---|---|---|---|
| 251591673533 | Sony Network Communications Inc | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251592703686 | Edged Energy | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 251593480892 | Bulk Fiber Networks AS | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 |
| 251593480895 | Tuvalu Telecommunication Corporation | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593480896 | Vodafone Fiji Pte Limited | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593520881 | CCI | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593520885 | Telecom Fiji | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593554626 | Chief Telecom Inc. | Data Center Colo Provider | Standard - colo | tier_3 |
| 251593554628 | Bridge Data Centres | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 251593554629 | CITIC Telecom CPC | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593554630 | Takoda Data Centers | Data Center Colo Provider | Standard - colo | tier_3 |
| 251593554632 | Vodafone Cook Islands | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593594606 | TELY AMERICAS | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593594608 | Yondr Group | Data Center Colo Provider | Hyperscale Wholesale - colo | tier_1 |
| 251593594609 | NGN Fibernetwork | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593618167 | HFCL | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593618168 | Axtel | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251593660095 | Colovore | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 251593660097 | American Tower | Data Center Colo Provider | Standard - colo | tier_3 |
| 251593660101 | TOKAI Communications Corporation | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251595451115 | Apelby Communications | MSP/Aggregator | Telecom Aggregator - MSP | tier_2 |
| 251595451117 | True Internet Data Center | Data Center Colo Provider | Standard - colo | tier_3 |
| 251597249227 | JASTEL NETWORK COMPANY LTD. | Data Center Colo Provider | Standard - colo | tier_3 |
| 251599045320 | Lightstorm | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251600877273 | Campana Group | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251600877274 | ARTERIA Networks Corporation | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251600877276 | Fiji International Telecommunications | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251651866344 | Sify Technologies Ltd. | Data Center Colo Provider | AI Signals - colo | tier_1 |
| 251653663426 | Cocoa Oriental | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251655462616 | C3ntro Telecom | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251659209445 | Bitera Data Center | Data Center Colo Provider | Standard - colo | tier_3 |
| 251659209446 | Bharti Airtel Ltd | Network Operator(Tier 1 / VNO) | Tier 1 Carrier - Network Op | tier_1 |
| 251661009602 | Iristel Inc. | Fiber Operator | Regional CLEC - Fiber operator | tier_3 |
| 251661009604 | EXA Infrastructure | Network Operator(Tier 1 / VNO) | Pure Wholesale Carrier - Network Op | tier_1 |
| 252094741203 | Liberty Latin America | Network Operator(Tier 1 / VNO) | Cable MSO Enterprise Division - Network Op | tier_1 |
| 252507461351 | Intermountain Infrastructure Group, LLC | Fiber Operator | Long Haul / Backbone - Fiber operator | tier_2 |
| 253067607790 | CleanArc Data Centers | Data Center Colo Provider | AI Signals - colo | tier_1 |

---

## HOLDs (8) - escalate to canvas F0B0AFSB9LN / D7

No writes. Records keep their existing `last_enriched_date`.

### OADC (251593480894) - identity confusion
- HubSpot name "OADC" suggests Open Access Data Centres (WIOCC's Pan-African DC platform)
- Domain `adc.am` is the Armenian Data Center (national DC in Yerevan, ~16 emp, $500K rev)
- `geographic_focus` field describes the Pan-African operator; `account_brief` describes the Armenian operator. Self-contradictory record.
- Two distinct entities collapsed into one record. Need Cooper decision: split into two records, or correct identity to the dominant entity.

### China Telecm Americas (251593594605) - name typo + wrong domain + sanctions
- HubSpot name has typo "Telcm" (should be "Telecom")
- Domain `sbtelecom.net` is unrelated SB Telecom
- Real China Telecom Americas operates at `chinatelecomamericas.com`
- Sanctions context: FCC revoked China Telecom Americas' Section 214 authorization in Jan 2022; limited US operations remain. Phase 3 D1 sanctioned-country guidance applies.
- Need Cooper decision on identity correction AND whether sanctions status warrants `customer_segment = "Flagged for deletion"` or `customer_segment = "Other"`.

### Pacific Dataport Inc. (251593619130) - pure satellite operator framework gap
- Anchorage AK satellite middle-mile operator (Astranis GEO + Aurora LEO via Starlink)
- Currently classified as Fiber Operator / Regional CLEC - but Pacific Dataport is purely satellite (Aurora LEO Nome Gateway 2025-06 launch)
- Same framework gap as Kacific Broadband (batch 38 HOLD) and RBC Signals (carryover)
- Cum 3 records now flagged as pure satellite operators with no current ICP fit. Recommend Cooper add either: (a) new "Satellite Operator" sub-segment, OR (b) explicit policy to classify as "Other" + Tier 5.

### PLDTUS LTD (251593619131) - duplicate-pair candidate + wrong domain
- Domain `pldthome.com` is PLDT consumer broadband (Home Fibr/DSL) - not the US wholesale subsidiary
- Likely duplicate with parent PLDT record (also in CRM)
- State `Cordillera Administrative Region` Philippines is corrupted - should be US-based if this is the wholesale arm
- Existing R3 (Duplicate Accounts) carryover note in brief
- Need Cooper decision: merge with parent PLDT, OR keep as US subsidiary and correct domain to PLDT Global / `pldtglobal.com`.

### Vodafone Kiribati (251651478242) - wrong domain
- Domain `vodafone.com.mt` is Vodafone Malta (completely unrelated)
- Real Vodafone Kiribati operates under ATH consortium (similar to Vodafone Fiji / Cook Islands / Samoa). Domain likely `vodafone.com.ki` or via ATH parent
- Account_brief already documents the error but domain still incorrect
- Need Cooper approval for domain correction (low-confidence candidate domains).

### AVAIO (251651866345) - identity / domain mismatch
- HubSpot name "AVAIO" implies AVAIO Digital (hyperscale DC developer; sites in CA, MS, VA, Killala Ireland, Algete Spain)
- Domain `navarino.co.uk` is Navarino (Greek maritime VSAT operator) - unrelated
- Real AVAIO Digital domain is `avaiodigital.com` or `avaiocapital.com`
- Account_brief acknowledges AVAIO is hyperscale DC developer; state/country/employee count reflect Navarino's profile
- Note: Operating notes mention "AVAIO Digital from Standard - batch 38" reclass to AI Signals - colo - that may have been a different/separate record. This one needs identity correction first.

### NORDUnet (251655462617) - R&E network framework gap
- NORDUnet is the Nordic Research & Education Network (NREN) consortium (DK/FI/IS/NO/SE)
- Connects to GEANT (Europe), Internet2 (US), FUJI XP (Asia)
- Currently classified as Fiber Operator / Regional CLEC - but R&E networks are non-commercial; they don't sell to enterprise/wholesale customers
- Framework gap: Phase 3 doesn't have an explicit R&E network sub-segment
- Similar to Netnod (IX/Internet Exchange policy gap from batch 38)
- Recommend Cooper decision: classify R&E networks (NORDUnet, GEANT-NREN, Internet2) as "Other" with Tier 5, OR add explicit "Research & Education Network" treatment policy.

### TEECOM (251661009608) - non-ICP, name+domain mismatch
- HubSpot name "TEECOM" maps to teecom.com (US AV/IT integration consultancy) - non-ICP
- Domain `gtelecom.com.au` is Greenway Telecom Australia (small AU fiber operator) - unrelated
- Account_brief already flags this as HELD for Cooper review
- Cleanest resolution: flag for deletion (TEECOM the AV consultancy is non-ICP; Greenway is a different entity that may merit its own record).

---

## Data quality patterns this batch

- **State/country mismatches from Apollo MISDOMAIN-corrected records (~9 records this batch)**: EcoDataCenter (Brazil state on Sweden record - PATCHED), Sony Network (Tokyo state on Singapore country), Lightstorm (Haryana India state on Singapore country), Sify (Tamil Nadu on India), Bitera (Jakarta state - correct), Axtel (Beirut Lebanon on Mexico HQ), Vodafone Cook Islands (County Dublin state), TELY Americas (Florida state on Brazil country), DayOne (Jakarta state on Indonesia, but Singapore-HQ). These are stale Apollo artifacts from prior domain corrections. Suggest a future R6 (Territory & Hygiene) sweep specifically for state cleanup post-MISDOMAIN.
- **Subsea cable operator backlog continues to drain**: 3 more promotions this batch (Aqua Comms, GCX, SUBCO). Cum total: 5 (Samoa SCC batch 38 + 3 this batch + Aqua Comms).
- **Pure satellite operator framework gap deepens**: Pacific Dataport now 3rd flagged (Kacific batch 38, RBC Signals carryover). Recommend Cooper framework decision before batch 41.
- **R&E network framework gap (new pattern)**: NORDUnet is the 1st R&E (NREN) network flagged. Watch for GEANT, Internet2, AARNet, JANET, SURFnet in future batches.

## Carryover holds preserved

Prior batch HOLDs not seen in this batch's pool of 50 (hs_object_id range 251591673533 - 253067607790): Tekpoint identity, Global Secure Layer domain, MedOne name+domain, Netnod IX policy, Goodman Group, SB Communications, ING-Ting, TGT Global. These remain on canvas F0B0AFSB9LN for D7 weekly resolution.
