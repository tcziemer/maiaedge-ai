# Mass Re-Enrichment Sweep - Batch 25
**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 25
**Date:** 2026-05-18
**Processed:** 40/50 (HubSpot offset wrap at page 5 due to identical `last_enriched_date=2026-04-01` causing sort instability - returned page 2 duplicates; 40 unique records processed)
**Pool remaining (pre-batch):** 1,572
**Pool remaining (post-batch est.):** ~1,532

## Path mix
- LIGHT: 0
- MEDIUM: 28
- FULL: 12 (7 segment-change Tier 1 incumbent reclassifications + 5 Flag for deletion)
- HOLD: 0

## Apollo this batch: 0 credits (no Apollo calls; existing data sufficient for all classifications)

## Tier writes
- Promotions (toward T1): 5 (Telekom Malaysia, Telkom Kenya, Telecom Egypt, Airtel Business, Bouygues Telecom)
- Demotions (toward T5): 2 (prtc.org tier_3->tier_4, Evoque tier_1->tier_3)
- Tier writes for sub-segment shifts: 4 (AFR-IX, IELO-Liazo, UPIX, Turk Telekom Intl)
- Skipped (hs_is_target_account=true): 2 (Telmex, Softnet)

## Sub-segment auto-migrations: 0
## Greenfield migrations: 0
## Segment changes (cascade fired): 12
## Customer-protection HOLDs: 0
## Completeness Gate fails (held for next batch): 0
## Manual-review HOLDs (true 2+ ambiguity): 0

## Per-record summary

### Redeia (316283788009) - MEDIUM
- Segment: Fiber Operator (no change)
- Sub-segment: Dark Fiber Specialist - Fiber Operator (no change)
- Tier: tier_2 (no change)
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Tawasul (268208411377) - MEDIUM
- Segment: MSP/Aggregator (no change)
- Sub-segment: Managed Network Services - MSP (no change)
- Tier: tier_2 (no change)
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Telmex (320960333515) - MEDIUM (hs_is_target_account=true)
- Segment/sub-segment: no change
- Tier: tier_1 frozen (hs_is_target_account)
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Softnet (320873732835) - MEDIUM (hs_is_target_account=true)
- Segment/sub-segment: no change (Network Op / Tier 1 Carrier kept despite 45-emp scale mismatch - hs_is_target_account override respected)
- Tier: tier_3 frozen
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date
- Note: 45-emp regional VNO using Tier 1 Carrier sub-segment is borderline; respecting Cooper's target_account flag

### Anthem Broadband (314346084052) - MEDIUM
- Segment/sub-segment/tier: no change
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### AxNet / Axtel Networks (316210759372) - MEDIUM
- Segment/sub-segment/tier: no change
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### E-Networks (316194744046) - MEDIUM
- Segment/sub-segment/tier: no change
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date

### PRTC (prtc.org) (303892661976) - MEDIUM + tier drop
- Tier: tier_3 -> tier_4 (2-county Kentucky coop with 20 emp is below tier_3 floor for Regional CLEC default)
- Writes: hyperscaler_proximity="None Known", account_tier=tier_4, last_enriched_date

### GlobalCom Holding (316133717743) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### FriendliAI (301240503024) - MEDIUM
- Infrastructure profile correction: Facilities Large (20-49) -> Facilities Small (<5) (FriendliAI is SaaS inference platform; previous bands wrong)
- Writes: infrastructure_profile (corrected), hyperscaler_proximity="None Known", last_enriched_date

### Telekom Malaysia (316203554529) - FULL (national incumbent under-tiering)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1
- Confidence: high_90 (kept)
- Reason: 24,000 employees, Malaysia's national incumbent, TM Global wholesale in 50+ countries, subsea cables, Tier-III DCs

### Jaintel (316208998104) - FULL -> Flagged for deletion
- 6-employee London wholesale VoIP, no owned network, resells Tier 1 carrier capacity
- Pattern: voice wholesale mass eviction (<500 emp, voice-only, no infra, no anchor customers)

### AFR-IX Telecom (316210812647) - MEDIUM (sub-segment shift)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator (Medusa subsea 8,700km + 100+ pan-African PoPs)
- Tier: tier_3 -> tier_2 (Long Haul default)
- Note: NOT pure-play subsea (substantial pan-African terrestrial - Telxius pattern); stays in Fiber Operator

### SGS Telekom (316212615887) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Eletronet (316210759370) - MEDIUM
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date

### Telkom Kenya (316283788016) - FULL (national incumbent under-tiering)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1
- Reason: 1,433 emp, owns NOFBI (Kenya national backbone), 22.5% EASSy, 10% LION2, TEAMS access

### Think Tel (316283788019) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Scopesky Communications (316296615617) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Sipartech (316287384265) - MEDIUM
- Writes: provisioning_landscape (filled), hyperscaler_proximity="Existing Facility Nearby" (Ile-de-France DCs), last_enriched_date

### Qsera Telenet (316298284738) - FULL -> Flagged for deletion
- NY-based small MSP, voice/connectivity reseller, "Limited infrastructure ownership"
- Apollo 3,884 emp suspect (description says "small NY-based MSP")
- Pattern: voice wholesale mass eviction

### Telecom Egypt (316282051269) - FULL (national incumbent under-tiering)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1
- Reason: 53,332 emp, sole national fixed-line monopoly, 24 subsea cable connections, 10 landing stations

### WIN Technology (316278520568) - MEDIUM
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date

### IELO-Liazo Services (316283788005) - MEDIUM (sub-segment shift)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator (3rd largest French wholesale, 2,800 km)
- Tier: tier_3 -> tier_2

### Airtel Business (316280383164) - FULL (national incumbent / wholesale arm of Bharti Airtel)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1
- Reason: B2B arm of Bharti Airtel (India's largest telecom), 34,958 emp, 12 large DCs + 120+ edge DCs, subsea+terrestrial
- **R3 dedup flag:** check for separate Bharti Airtel parent record

### INTERNEXA S.A (316237371071) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### UPIX Networks (316280383162) - MEDIUM (sub-segment shift)
- Sub-segment: Regional CLEC -> Long Haul / Backbone - Fiber operator (25,000 km LATAM/US wholesale, 100+ PoPs)
- Tier: tier_3 -> tier_2

### Stella Communications (316283788010) - FULL -> Flagged for deletion
- Stamford CT global voice-services aggregator, 300M+ international voice minutes/year, no owned network
- Pattern: voice wholesale mass eviction

### Unifi (316282051272) - FULL -> Flagged for deletion (retail consumer brand + duplicate)
- Consumer/business broadband brand of Telekom Malaysia (TM); not a separate operator
- **R3 dedup flag:** duplicate of Telekom Malaysia (316203554529)
- Industry "ANIMATION" in Apollo is an obvious data quality error

### Bouygues Telecom (316298283761) - FULL (national incumbent under-tiering)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_1
- Reason: 8,937 emp, $45.7B revenue, 32.3M customers, French Tier 1 MNO with Nexloop/SDAIF JVs

### Turk Telekom International (316237316828) - FULL (wholesale arm of Tier 1)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO)
- Sub-segment: Regional Cable Operator -> Tier 1 Carrier - Network Op
- Tier: tier_3 -> tier_2 (wholesale arm convention - matches A1 Wholesale/Bayobab precedent)
- Reason: 40,000+ km dark fiber EMEA-Turkey, wholesale IP transit, 19 countries, 150+ interconnection points
- **R3 dedup flag:** check for Turk Telekom parent record

### BentoCloud (297936669377) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Cassava Technologies (300347451125) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Evoque Data Center Solutions (264592334566) - FULL (template bleed + sub-segment correction)
- Sub-segment: AI Signals - colo -> Standard - colo (no AI/GPU signal evidence in record)
- Tier: tier_1 -> tier_3 (Standard colo default; low_5069 confidence stays but bumped to medium_7089 with brief regen)
- account_brief: REGENERATED (was template-bleed: "polite chaos", "Network Isolation problem", "stranded capacity")
- provisioning_landscape: REGENERATED (was template-bleed)
- geographic_focus: corrected from "Not found" to "United States - 20-49 colocation facilities"

### Adacen (264192113374) - MEDIUM (template bleed regen)
- account_brief: REGENERATED (was template-bleed: "Network Isolation problem", "MaiaEdge angle")
- provisioning_landscape: REGENERATED (was template-bleed)
- recent_news_or_trigger_event: re-formatted with [YYYY-MM-DD] prefix

### NAP Caribe (316133717745) - MEDIUM
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date

### Hawe Telekom (316224565951) - MEDIUM
- Writes: hyperscaler_proximity="None Known", last_enriched_date

### Dorados Cloud (311385168586) - FULL -> Flagged for deletion
- El Dorado Hills CA SaaS network automation vendor (CruzNow platform); not a neocloud
- Misclassified as NeoCloud / AI Infrastructure providers - tier_1 at low_5069 confidence
- No infrastructure ownership; sells SaaS for multi-vendor IT stack monitoring

### Teledata ICT (316219896514) - MEDIUM
- Writes: provisioning_landscape (filled), hyperscaler_proximity="None Known", last_enriched_date

### G42 (301316953844) - MEDIUM
- Writes: hyperscaler_proximity="Announced: <50 miles" (Microsoft 200MW Abu Dhabi DC), recent_news_or_trigger_event (Stargate UAE), last_enriched_date

### Lightning AI (300724801231) - MEDIUM (brief regen + stale news clear)
- account_brief: REGENERATED (was 7 words: "AI dev platform. $50M Series B. NVIDIA/Cisco investors.")
- provisioning_landscape: REGENERATED (was 5 words: "Cloud-based. No NaaS.")
- recent_news_or_trigger_event: CLEARED (was 2024-11 Series B, >18 months old, no Signal Scan in 7d)

## Notable patterns this batch

1. **National incumbent under-tiering (7 records reclassified):** Telekom Malaysia, Telkom Kenya, Telecom Egypt, Airtel Business, Bouygues Telecom all sat at Fiber Operator / Regional CLEC / tier_3 despite being major national/Tier 1 telcos. Plus Turk Telekom Intl (wholesale arm of Tier 1, classified as Regional Cable Operator). Pattern continues from prior batches' 7 records. Sweep-wide grep candidate stands: `customer_segment = "Fiber Operator" AND company_sub_segment = "Regional CLEC - Fiber operator" AND (numberofemployees > 5000 OR annualrevenue > 500000000)`.

2. **Voice wholesale / mobile-only retail mass eviction (3 records this batch):** Jaintel (London 6-emp VoIP), Qsera Telenet (NY voice + MSP reseller), Stella Communications (Stamford CT voice aggregator). All flag pattern: <500 employees + voice-only + no wholesale fabric + no anchor brand customers. Continues prior batch's 9-record pattern.

3. **Retail consumer brand duplicate:** Unifi flagged as duplicate of Telekom Malaysia (Unifi is TM's consumer brand). R3 dedup candidate.

4. **Misclassified SaaS as NeoCloud:** Dorados Cloud (CruzNow network automation SaaS vendor at low_5069 confidence). Flagged.

5. **Sub-segment within-parent reclassification (3 records):** AFR-IX, IELO-Liazo, UPIX Networks all sat at Regional CLEC despite being wholesale/long-haul fiber operators. Reclassified to Long Haul / Backbone - Fiber operator.

6. **Template-bleed remediation (2 brief regens + 2 provisioning regens):** Evoque + Adacen had "polite chaos" / "Network Isolation problem" / "MaiaEdge angle" template language. Lightning AI had impossibly thin briefs (5-7 words). All regenerated to framework-aligned 2-4 sentence narrative. Sweep-wide grep candidate stands: `account_brief CONTAINS "polite chaos" OR "Network Isolation" OR "stops at the network edge"`.

7. **Apollo data quality:** Unifi industry="ANIMATION" (Telekom Malaysia consumer broadband brand). E-Networks numberofemployees=3 (likely undercount - they're Guyana's largest digital services provider). Qsera Telenet numberofemployees=3,884 (suspect for "small NY-based MSP" per description).

## R3 dedup flags (3 raised this batch)
1. **Bharti Airtel parent vs Airtel Business subsidiary** (316280383164) - check for separate Bharti Airtel record
2. **Telekom Malaysia parent (316203554529) vs Unifi retail brand (316282051272)** - duplicate confirmed via flag
3. **Turk Telekom parent vs Turk Telekom International wholesale arm (316237316828)** - check for separate Turk Telekom parent record

## Owner mismatch fixes this batch: 0 (no state/territory changes triggered owner re-derive)

## Drain status
- Pre-batch pool: 1,572
- Records processed this batch: 40 (10 short of 50 due to HubSpot offset wrap)
- Pool remaining (post-batch est.): ~1,532
- Sweep cumulative drain: ~28 batches processed, ~46% of original pool through
- ETA: ~30 more batches at BATCH_SIZE=50 (effectively ~38 at observed 40/batch throughput)

## Errors: None. 40/40 HubSpot writes succeeded.

## Run health: GREEN
