# Mass Re-Enrichment Sweep — 2026-05-18-post-phase-3-framework — Batch 36

**Run date:** 2026-05-19
**Sweep params:** BATCH_SIZE=50, VERIFY_DEPTH=leverage-and-patch, APOLLO_ENFORCEMENT=disabled, SEGMENT_SCOPE=all_active_icp
**Trigger sort:** `hs_object_id ASC` (per memory `hubspot_sweep_pagination.md`)
**Pool at batch start (reported total):** 1,048 records remaining
**Pool projection at batch 35 end:** ~915 — gap of ~133 likely caused by steady-state R0/R1/R2 churning records back into pool during sweep window
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled + Apollo-free path dominant)

## Path mix

- **FULL reclassifications:** 6
- **MEDIUM gap-fill:** 1 (Phibee promoted from prior-batch HOLD)
- **LIGHT date bumps:** 43
- **HOLD:** 0

## Reclassifications (6 FULL)

### 1. General Motors (192916123348)
- Path: FULL
- Domain: gm.com (unchanged)
- Segment: Enterprise-CustomerSegment -> Other
- Sub-segment: (none, was manual_review_required) -> (cleared)
- Confidence: manual_review_required -> high_90
- Tier: tier_3 -> tier_5
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0 (decision derived from CLAUDE.md operating rule)
- Completeness Gate: pass
- Reason: Manufacturing is Watch List per CLAUDE.md, not one of the 4 Enterprise ICP verticals (Financial Services, Healthcare, Retail/Distribution, Outsourcing Services). Retained as Other tier_5 (competitive/partner reference).

### 2. HOT TELECOM (193866158799)
- Path: FULL
- Domain: hottelecom.com (unchanged)
- Segment: Fiber Operator -> MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator -> Telecom Aggregator - MSP
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_2
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Quebec-HQ wholesale DID/SIP/VoIP termination provider (CPaaS-style). Fits operator-notes flagged "CPaaS / voice aggregator misclassified as Fiber Op Regional CLEC" pattern (cum now ~5).

### 3. Telesat (193867595497)
- Path: FULL
- Domain: telesat.com (unchanged)
- Segment: Fiber Operator -> Other
- Sub-segment: Regional CLEC - Fiber operator -> (cleared)
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_5
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Pure satellite operator (GEO fleet + Telesat Lightspeed LEO constellation, $1.1B backlog, Viasat 2025 contract). No terrestrial fiber backbone; satellite is outside the 6 ICPs. Keep as competitive/partner reference for space-segment.

### 4. OPTK Networks (193906531016)
- Path: FULL
- Domain: optk.com (unchanged)
- Segment: Fiber Operator -> Fiber Operator
- Sub-segment: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_2
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Lincoln NE wholesale dark fiber + wavelength carrier; 4,000-mile long-haul network along I-80 (Denver-Omaha-Chicago) with 10K+ wavelength route miles. Route Miles Large (10K-50K) + IRU/dark fiber wholesale model = long-haul. Confirms operator-notes "within-fiber demotions / reclassifications, Long Haul mis-routed" cumulative pattern (now ~22 Long Haul corrections).
- Enum gotcha: First write attempted `Long Haul Wholesale - Fiber operator` — HubSpot 400'd with allowed-list. Correct internal value is `Long Haul / Backbone - Fiber operator` (with spaces around `/`). Saved to memory `hubspot_subsegment_enum_canonical.md`.

### 5. Proximus Group (198375864035)
- Path: FULL
- Domain: proximus.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Belgian state-owned incumbent telco (~45% fixed broadband share, ~30% postpaid mobile). Operator-notes national-operator-under-tiering pattern (cum now ~40). Route Mobile acquisition complete early 2025 (#3 global CPaaS via BICS/Telesign); sold DCs to Datacenter United March 2025.

### 6. Ufinet (199103976181)
- Path: FULL
- Domain: ufinet.com (unchanged)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC - Fiber operator -> International Backbone Specialist - Network Op
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Madrid-HQ Pan-LATAM carrier-of-carriers; 110,000+ km fiber (46.6K route miles) across 17 countries; 26 years wholesale-only. Scale + business model matches Sparkle/PCCW Global pattern, not Regional CLEC. Operator-notes national/multi-country under-tiering pattern (cum now ~41).

## MEDIUM gap-fill (1)

### 7. Phibee Telecom (193062202073)
- Path: MEDIUM (promoted from prior-batch HOLD)
- Domain: phibee.net (unchanged)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: (empty) -> medium_7089
- Tier: tier_2 (unchanged)
- Apollo used: no
- web_searches: 1
- Completeness Gate: pass
- Reason: French wholesale telecom + data capacity aggregator (50,000+ links, ~15 country PoP). Completed all 7 narrative enriched fields. HOLD cleared.
- Enum gotcha: First write rejected `fabric_provisioning_approach` and `hyperscaler_proximity` prose — both fields are HubSpot enums, not free text. Saved to memory `hubspot_enriched_enum_fields.md`. Retried with `manuallegacy_processes` + `None Known`.

## LIGHT date bumps (43)

All 43 had framework-consistent enrichment, 7 enriched fields populated, sub-segment in 30 active values, brief 100-410c (within 2-4 sentence cap). Tier defaults already matched computed tier. Date stamp to 2026-05-19 only.

| # | Company ID | Name | Existing seg / sub / tier |
|---|---|---|---|
| 1 | 192888735460 | Telia Carrier | Network Op / Pure Wholesale Carrier / tier_1 (R3 candidate vs Arelion 174907029202; brief already flags) |
| 2 | 192899501812 | Verizon | Network Op / Tier 1 Carrier / tier_1 |
| 3 | 192916122333 | Altice USA | Network Op / Cable MSO Enterprise Division / tier_1 |
| 4 | 193170019008 | Verizon Enterprise | Network Op / Tier 1 Carrier / tier_1 (R3 candidate vs Verizon 192899501812 — flagged for R3 follow-up) |
| 5 | 193170019009 | PCCW Global | Network Op / International Backbone Specialist / tier_1 |
| 6 | 193858234104 | Vodafone Group Plc | Network Op / Tier 1 Carrier / tier_1 (R3 candidate vs Vodafone UK if present) |
| 7 | 193865437904 | GTT Communications | Network Op / Pure Wholesale Carrier / tier_1 |
| 8 | 193866158789 | Sparkle | Network Op / International Backbone Specialist / tier_1 |
| 9 | 193866158800 | Syringa Networks | Fiber Op / Regional CLEC / tier_3 |
| 10 | 193866158803 | Minnesota VoIP | MSP/Agg / Telecom Aggregator / tier_2 |
| 11 | 193866158820 | Southern Tier Network | Fiber Op / Regional CLEC / tier_3 |
| 12 | 193866159802 | TierPoint | Colo / AI Signals / tier_1 |
| 13 | 193866877684 | Enzu | NeoCloud / AI Infrastructure providers / tier_1 (medium_7089 — flag for D7 deeper research; not BTC heritage) |
| 14 | 193867595491 | Beanfield | Fiber Op / Regional CLEC / tier_3 |
| 15 | 193867595507 | Noramco | MSP/Agg / Telecom Aggregator / tier_2 |
| 16 | 193867595510 | Gigabit Fiber | Fiber Op / Regional CLEC / tier_3 |
| 17 | 193867596483 | MetTel | MSP/Agg / Telecom Aggregator / tier_2 |
| 18 | 193867596494 | TERAGO | Fiber Op / Regional CLEC / tier_3 |
| 19 | 193867596499 | Atlantech Online | Fiber Op / Regional CLEC / tier_3 |
| 20 | 193867596519 | OTAVA | Colo / Standard / tier_3 |
| 21 | 193868315361 | USA Digital Communications | MSP/Agg / Telecom Aggregator / tier_2 |
| 22 | 193906530033 | MDTC.net | Fiber Op / Regional CLEC / tier_3 |
| 23 | 193906531020 | 2pifi | MSP/Agg / Telecom Aggregator / tier_2 |
| 24 | 193906531021 | 11:11 Systems | Colo / Standard / tier_3 |
| 25 | 193906531023 | Massive Networks | MSP/Agg / Telecom Aggregator / tier_2 |
| 26 | 193906531042 | Flexential | Colo / AI Signals / tier_1 |
| 27 | 193906531045 | Cologix | Colo / AI Signals / tier_1 |
| 28 | 193910127303 | Orchest Technologies | MSP/Agg / Telecom Aggregator / tier_2 |
| 29 | 193910127345 | K-PowerNet/KAMO Power | Fiber Op / Municipal / Cooperative / tier_4 |
| 30 | 193910127347 | Essentia | Fiber Op / Regional CLEC / tier_3 (Route Miles Large; watch for Long Haul reclass next pass) |
| 31 | 193910127348 | Valley Fiber | Fiber Op / Regional CLEC / tier_3 |
| 32 | 193910127352 | Zayo | Fiber Op / Tier 2 National Wholesale / tier_2 |
| 33 | 194004502213 | 365 Data Centers | Colo / Standard / tier_3 |
| 34 | 194004502229 | Arvig | Fiber Op / Regional CLEC / tier_3 |
| 35 | 194533878470 | Fullspan Solutions | MSP/Agg / Telecom Aggregator / tier_2 |
| 36 | 195229031121 | DCConnect Global | MSP/Agg / Telecom Aggregator / tier_2 |
| 37 | 198373708525 | Americom Networks | Fiber Op / Regional CLEC / tier_3 |
| 38 | 198403706563 | TD | Enterprise / Financial Services / tier_3 |
| 39 | 198431710965 | Citi | Enterprise / Financial Services / tier_3 |
| 40 | 199240083151 | ConnX | MSP/Agg / Telecom Aggregator / tier_2 |
| 41 | 205913286377 | AlasConnect | MSP/Agg / Telecom Aggregator / tier_2 |
| 42 | 206117947066 | Lincoln Data Centers | Colo / Standard / tier_3 |
| 43 | 206151499474 | ANS Advanced Network Services | MSP/Agg / Telecom Aggregator / tier_2 |

## New patterns / framework learnings this batch

1. **Manufacturing vertical Enterprise misclassification.** GM was classified as Enterprise-CustomerSegment + manual_review_required. Per CLAUDE.md, Manufacturing is Watch List, not in the 4 Enterprise ICP verticals. Cum 1 this batch — first occurrence in sweep. Watch for Ford, Toyota, Volkswagen, Tata Motors, Stellantis, Volvo, GE Manufacturing, etc. in later batches.
2. **Pure satellite operator misclassified as Fiber Op.** Telesat is the first surfaced. Watch for SES, Intelsat, Eutelsat, Inmarsat, Iridium, Globalstar, Viasat itself (though Viasat is hybrid), Hughes/EchoStar.
3. **National-incumbent under-tiering (Proximus).** Continues the cumulative ~40-record pattern. Belgian incumbent landed at Fiber Op Regional CLEC tier_3, should have been Network Op Tier 1 Carrier from day one.
4. **Pan-regional wholesale carrier under-tiering (Ufinet).** International Backbone Specialist pattern — wholesale-only multi-country backbone matching Sparkle/PCCW Global, but landed at Regional CLEC. Watch for similar: Telia/Arelion (already cataloged dupe), Lumen wholesale (verify), Tata Communications, Singtel International, Cinia, Hibernia/GTT subsea, BICS (Proximus subsidiary).
5. **CPaaS voice aggregator pattern (HOT TELECOM).** Cum ~5. Watch for Telnyx (likely already MSP), Bandwidth (already MSP), Inteliquent (already MSP), Vonage Premier (verify), Twilio (likely MSP), Sinch (likely MSP), 8x8 (verify), Voxbone (verify), Plivo (verify), Telesign (Proximus subsidiary).
6. **OPTK Long Haul / Backbone enum.** Internal value is `Long Haul / Backbone - Fiber operator` with spaces around `/`, NOT `Long Haul Wholesale - Fiber operator`. Pattern reinforces the `hubspot_enum_spacing.md` memory rule. Saved canonical 30-value enum list to `hubspot_subsegment_enum_canonical.md` to skip future retry-after-fail cycles.
7. **`fabric_provisioning_approach` + `hyperscaler_proximity` are enums.** Discovered during Phibee MEDIUM write. Both are single-select enums with discrete allowed values, NOT free text. Saved to `hubspot_enriched_enum_fields.md`.

## Carry-forward / open items

- **Verizon Enterprise (193170019008) R3 candidate vs Verizon (192899501812).** Flag for R3 Duplicate Accounts routine. Pair pattern matches Telia Carrier/Arelion (cum dupes ~5 now).
- **Telia Carrier (192888735460) R3 candidate vs Arelion (174907029202).** Already flagged in brief. Carries forward.
- **Vodafone Group Plc (193858234104) — possible dupe with Vodafone UK / earlier Vodafone records.** R3 review.
- **Essentia (193910127347) Route Miles Large but Regional CLEC tier_3.** Possible Long Haul reclass next pass — needs deeper research on actual wholesale vs CLEC posture.
- **Enzu (193866877684) medium_7089 confidence, AI Infrastructure providers.** Small (<5) facilities — verify Neocloud vs Standard Colo on next pass. NOT BTC heritage so NC5 doesn't apply.
- **DCConnect Global (195229031121) Singapore.** APAC SDN/NaaS operator — verify MSP/Aggregator vs Other (NaaS competitor pattern, cum 1 with Console Connect last batch).
- **ConnX (199240083151) connxai.com — domain suggests AI angle on UCaaS/CPaaS posture.** Watch for sub-segment refinement next pass.
- **TERAGO (193867596494) Canadian national SD-WAN.** Currently Fiber Op Regional CLEC — verify MSP next pass (similar to HOT TELECOM pattern).

## Drain status

- Done in this sweep through batch 36: ~1,800 records processed (rough; actual = 50 × 36 batches less Tier 3 holds carried)
- Pool at batch start: 1,048
- Pool projected at batch end (this batch + steady-state inflow): ~1,000 (subtract 50 processed, add small inflow)
- ETA: ~20 more nominal batches at BATCH_SIZE=50

## Run health: GREEN

No fatal errors. Two enum gotchas caught and recovered with retries; both saved to memory for future batches.

