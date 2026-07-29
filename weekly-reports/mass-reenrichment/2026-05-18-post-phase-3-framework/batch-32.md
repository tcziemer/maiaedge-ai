# Mass Re-Enrichment Sweep - Batch 32

**Sweep:** 2026-05-18-post-phase-3-framework
**Date:** 2026-05-19
**Processed:** 50/50
**Path mix:** LIGHT 20 · MEDIUM 26 · FULL 4 · HOLD 0
**Apollo this batch:** 0 credits
**Pool remaining:** 1,195 (was 1,245 pre-batch)

---

## Path summary

### FULL (4)

#### Syntys (Ooredoo) (297892337359)
- Path: FULL
- Domain: ooredoo.com
- Segment: Fiber Operator -> NeoCloud
- Sub-segment: Regional CLEC - Fiber operator -> AI Infrastructure providers - Neocloud (legacy auto-migration: no)
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_1
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0 (account_brief already described Qatari sovereign AI cloud)
- Completeness Gate: pass
- Reason: Account_brief described a Qatar sovereign AI cloud (NVIDIA Hopper, 120MW target, $1B investment, NVIDIA Cloud Partner) but record was classified as Fiber Operator. Segment misclassification corrected to NeoCloud / AI Infrastructure providers.

#### United Fiber & Data (298005834474)
- Path: FULL
- Domain: unitedfd.com
- Segment: Fiber Operator -> Flagged for deletion
- Sub-segment: Long Haul / Backbone - Fiber operator -> (cleared)
- Confidence: high_90 -> (cleared)
- Tier: tier_2 -> (cleared - not ICP)
- Customer protection invoked: no (no closed-won deals visible)
- Apollo used: no
- web_searches: 0
- Completeness Gate: n/a (eviction)
- Reason: Acquired by Lightpath February 2025; 402-mile fiber assets (NYC-Ashburn backbone + NYC/NJ metro) fully integrated into Lightpath. Record consolidates to active ICP (Lightpath).

#### Voyant Communications (297973565132)
- Path: FULL
- Domain: voyant.com
- Segment: Fiber Operator -> MSP/Aggregator
- Sub-segment: Regional CLEC - Fiber operator -> Telecom Aggregator - MSP (legacy auto-migration: no)
- Confidence: high_90 -> high_90
- Tier: tier_3 -> tier_3
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Voyant by Sinch is a CPaaS/UCaaS provider (acquired into Sinch's US Super Network via Inteliquent in 2021). SIP Trunking, UCaaS, CCaaS - not a facilities-based fiber operator. Reclassified to MSP/Aggregator.

#### Casair, Inc. (316148833999)
- Path: FULL
- Domain: casair.net
- Segment: Fiber Operator -> Flagged for deletion
- Sub-segment: Regional CLEC - Fiber operator -> (cleared)
- Confidence: medium_7089 -> (cleared)
- Tier: tier_3 -> (cleared - not ICP)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: n/a (eviction)
- Reason: Broadband/fiber assets acquired by Point Broadband (October 2020). Tower and spectrum assets retained as Casair Towers (separate entity, not a fiber operator). Carrier infrastructure relationship now lives on Point Broadband (active ICP).

### MEDIUM (26)

#### Rutilea (297888732862) - MaiaEdge-angle bleed cleanup
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no
- provisioning_landscape trimmed; "MaiaEdge angle:" sentence removed.

#### OpenMetal (297934868205) - MaiaEdge-angle bleed cleanup + infra_profile correction
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no
- provisioning_landscape trimmed; infrastructure_profile changed from "Facilities: Large (20-49)" to "Facilities: Small (<5)" (OpenMetal leases from Equinix/Digital Realty, doesn't own facilities).

#### 6G AI Sweden (297969950446) - MaiaEdge-angle bleed cleanup
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no
- provisioning_landscape trimmed.

#### Salad Cloud (297982584519) - MaiaEdge-angle bleed cleanup + infra_profile correction
- Path: MEDIUM | Tier: tier_2 -> tier_2 (unchanged) | Apollo: no
- provisioning_landscape trimmed; infrastructure_profile updated to reflect distributed POPs (Enterprise 100+) but Small (<5) facilities (consumer-GPU aggregator model).

#### Neysa (298009434839) - MaiaEdge-angle bleed cleanup
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no
- provisioning_landscape trimmed.

#### hscale (302193490680) - operational shorthand trimmed
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no
- provisioning_landscape rewritten - removed "RECLASSIFIED to AI-Colo: ..." and "Enrichment audit 2026-03-18" operational shorthand. Core build-to-suit description preserved.

#### Denvr Dataworks (303396147961) - MaiaEdge-angle bleed cleanup
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no

#### Atlas Cloud AI (303409448696) - MaiaEdge-angle bleed cleanup
- Path: MEDIUM | Tier: tier_1 -> tier_1 (unchanged) | Apollo: no

#### Westworld Telecom (193906531014) - tier demote
- Path: MEDIUM | Tier: tier_2 -> tier_3 | Apollo: no
- 10-employee MSP, no scale signals justifying tier_2.

#### South Plains Telephone Co-Op (sptc.coop) (316163231453) - MaiaEdge-angle cleanup
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Apollo: no
- DUPLICATE FLAG: record 297989642958 (sptc.net domain) is same entity (rebranded to Horizons Communications). Pre-deletion audit (R3/R4) should consolidate.

#### Cityside Fiber (316154232560) - MaiaEdge-angle cleanup
- Path: MEDIUM | Tier: tier_3 -> tier_3 (unchanged) | Apollo: no

#### City of Ketchikan (316178474727) - MaiaEdge-angle cleanup
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Apollo: no
- Note: 100-mile proposed subsea cable to Prince Rupert BC noted, but primary identity is terrestrial muni utility - does NOT qualify as Subsea cable operator (per the verified-operator policy; pure-play subsea operators only).

#### Cable One (316168617715) - MaiaEdge-angle cleanup
- Path: MEDIUM | Tier: tier_3 -> tier_3 (unchanged) | Apollo: no

#### Hargrayfiber (316174876405) - MaiaEdge-angle cleanup
- Path: MEDIUM | Tier: tier_3 -> tier_3 (unchanged) | Apollo: no
- Note: HubSpot name field is "hargrayfiber.com" - data quality artifact, brand operates as Hargray Fiber. Left as-is, R6 hygiene routine to address.

#### Polar Connect (316173011643) - sub-segment correction + geo fix
- Path: MEDIUM | Sub-segment: Regional CLEC -> Municipal / Cooperative | Tier: tier_3 -> tier_4 | Apollo: no
- account_brief describes member-owned cooperative; existing classification wrong. geographic_focus was "International - Arctic routes" (also wrong) - changed to rural ND/MN.

#### Liquid Telecom ZM (303417877204) - sub-segment promote + tier promote
- Path: MEDIUM | Sub-segment: Regional CLEC -> Long Haul / Backbone | Tier: tier_3 -> tier_2 | Apollo: no
- 110,000km+ pan-African fiber + 5 subsea cable connections + 1,610 employees. National/regional carrier under-tiered as Regional CLEC.

#### Wiktel (297782865624) - within-fiber demote
- Path: MEDIUM | Sub-segment: Long Haul / Backbone -> Regional CLEC | Tier: tier_2 -> tier_3 | Apollo: no
- MN family-owned local provider since 1947, not Long Haul.

#### PC Telcom (297888732864) - template-bleed remediation
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Apollo: no
- account_brief and provisioning_landscape were placeholder "research needed" - filled from recent_news_or_trigger_event data (CO co-op, $3.2M Advance Colorado Broadband Grant, Kevin Lybrand CEO).

#### KMTelecom (297906089707) - within-fiber demote
- Path: MEDIUM | Sub-segment: Long Haul / Backbone -> Regional CLEC | Tier: tier_2 -> tier_3 | Apollo: no
- MN family-owned local CLEC since 1901, not Long Haul.

#### ENMR Telephone Cooperative (298002235110) - template-bleed remediation + infra fix
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Apollo: no
- Template-bleed cleaned; infrastructure_profile corrected from Route Miles: Enterprise (50K+) to Mid-Size (1K-10K) (~8000 miles total).

#### Hawaii Dialogix Telecom (298009434831) - within-fiber demote
- Path: MEDIUM | Sub-segment: Long Haul / Backbone -> Regional CLEC | Tier: tier_2 -> tier_3 | Apollo: no
- Hawaii CLEC, multi-island. Not Long Haul.

#### City of Coffeyville (298005835453) - template-bleed remediation + low-confidence flag
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Confidence: high_90 -> low_5069 | Apollo: no
- Template-bleed cleaned; CMLP (Coffeyville Municipal Light & Power) may operate fiber but domain coffeyville.com is city government. Identity verification flagged for D7.

#### Johnson Telephone (298009434834) - within-fiber demote
- Path: MEDIUM | Sub-segment: Long Haul / Backbone -> Regional CLEC | Tier: tier_2 -> tier_3 | Apollo: no
- MN family-owned local CLEC, ~2,743 households served. Not Long Haul.

#### Dixie Electric Power Association (297934868212) - template-bleed remediation
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Apollo: no
- DE Fastlink fiber subsidiary; active 2025 expansion.

#### Cap Rock Telephone Cooperative (297936668403) - template-bleed remediation + low-confidence flag
- Path: MEDIUM | Tier: tier_4 -> tier_4 (unchanged) | Confidence: high_90 -> low_5069 | Apollo: no
- Tiny coop (11 employees) with "Large (10K-50K)" route miles claim - likely overstated. D7 verification.

#### WOW! (297973565131) - sub-segment correction
- Path: MEDIUM | Sub-segment: Regional CLEC -> Regional Cable Operator | Tier: tier_3 -> tier_3 (unchanged) | Apollo: no
- Cable operator historically; sub-segment was wrong. Take-private to DigitalBridge+Crestview closed Dec 2025, new CEO Frank van der Post Jan 2026.

### LIGHT (20)

Date-bump only (already framework-consistent, no MaiaEdge-angle bleed, sub-segment in 30 active values, narrative fields within 2-4 sentence cap):

- Telenor Norge (303440311006)
- Range Telephone Cooperative (154278570716)
- Flat Rock Telephone Co-Op (297982584518)
- Wabash Communications CO-OP (297877949122)
- Vernon Communications Cooperative (297858169560)
- Foothills Telephone Cooperative (297858169561)
- West River Cooperative Telephone (297858169559)
- SpringNet (297894134521)
- Stayton Cooperative Telephone Co (297906089708)
- South Plains Telephone Cooperative (sptc.net) (297989642958) - duplicate of 316163231453
- Eastex Telephone Cooperative (298009434827)
- Wes-Tex Telephone Cooperative (298005834475)
- Richland-Grant Telephone Cooperative (298005834478)
- Farmers Telecommunications Cooperative (298009434829)
- K-Powernet (297940265682) - genuinely a regional backbone (4-state, 60 POPs, 4000 fiber miles)
- BEK Communications Cooperative (297940265678)
- SwiftCurrent Connect (297944750824)
- Grant PUD (297969950437)
- United Cooperative Services (297969950438)
- Citizens Telephone Cooperative (297975387873)

### HOLD (0)

Per operating notes ("HOLD policy = NONE"), no records held this batch.

---

## Pattern observations

| Pattern | This batch | Cumulative (provisional) |
|---|---|---|
| MaiaEdge-angle bleed in provisioning_landscape (NEW pattern; carry-forward from JarvisLabs/Shadeform) | 14 | ~31 |
| Within-Fiber demotions (Long Haul -> Regional CLEC) | 4 (Wiktel, KMTelecom, Hawaii Dialogix, Johnson Telephone) | ~18 cum |
| Within-Fiber demotions (Regional CLEC -> Municipal / Cooperative) | 1 (Polar Connect) | ~15 cum |
| Template-bleed remediation ("research needed" placeholders) | 5 (PC Telcom, ENMR, City of Coffeyville, Dixie Electric, Cap Rock) | ~22 cum |
| Segment misclassification (Fiber Operator -> NeoCloud) | 1 (Syntys) | 1 |
| Segment misclassification (Fiber Operator -> MSP/Aggregator) | 1 (Voyant by Sinch) | 1 |
| Acquired-entity eviction (Flagged for deletion) | 2 (UFD->Lightpath, Casair->Point Broadband) | (carry-forward; varies) |
| National/regional carrier under-tiering | 1 (Liquid Telecom ZM) | ~31 cum |
| Subsea cable operator candidates (the 30th sub-segment) | 0 - City of Ketchikan does NOT qualify (terrestrial primary identity) | 1 cum (Tampnet) |
| Greenfield colo candidates | 0 | 1 cum (Beacon Data Centers) |
| MaiaEdge value-prop bleed in account_brief | 0 | 1 cum (Voxtelesys) |

## Tier movement summary

- Promotions toward T1: 2 (Syntys Fiber tier_3 -> NeoCloud tier_1; Liquid Telecom ZM tier_3 -> tier_2)
- Demotions toward T5: 6 (Westworld T2->T3; Polar Connect T3->T4; Wiktel T2->T3; KMTelecom T2->T3; Hawaii Dialogix T2->T3; Johnson Telephone T2->T3)
- Net Flagged for deletion: 2 (UFD, Casair)
- Skipped (hs_is_target_account=true): 0 detected this batch

## Data quality follow-ups for Cooper

1. **Duplicate pair: South Plains Telephone Co-Op (sptc.coop, 316163231453) vs South Plains Telephone Cooperative (sptc.net, 297989642958)** - same entity (rebranded to Horizons Communications). R3 Duplicate Accounts should consolidate. Both processed individually in this batch; consolidating later won't lose enrichment.

2. **Hargrayfiber.com (316174876405) - name field is literally "hargrayfiber.com"** - data quality artifact. Brand is Hargray Fiber, parent Cable One. R6 hygiene candidate.

3. **City of Coffeyville (298005835453)** - flagged low_5069 - domain coffeyville.com is city government; fiber service (if it exists) would be at CMLP. Identity needs D7 verification.

4. **Cap Rock Telephone Cooperative (297936668403)** - 11 employees with claimed Route Miles: Large (10K-50K) - likely overstated. D7 verification.

5. **Polar Connect (316173011643)** - geographic_focus was "International - Arctic routes" (the company is rural ND/MN). Fixed this batch; flag bug in enrichment data source.

6. **MaiaEdge-angle bleed pattern is widespread.** Provisional cumulative ~31 instances over sweep. Suggests a single template/prompt iteration injected this phrasing into provisioning_landscape across batches. Continue catching and trimming.

## Apollo budget impact

- This batch: 0 credits (APOLLO_ENFORCEMENT="disabled" + no records required Apollo refresh since narrative-only patches dominated).
- Sweep cumulative: per prior tracker.
