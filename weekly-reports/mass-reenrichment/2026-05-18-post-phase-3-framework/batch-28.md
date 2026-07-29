# Mass Re-Enrichment Sweep — Batch 28

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 28
**Date:** 2026-05-18
**Pool remaining at batch start:** 1,439
**Records pulled:** 50 (offsets 0/10/20/30/40)
**Unique records (after dedup):** 40
**VERIFY_DEPTH:** leverage-and-patch
**APOLLO_ENFORCEMENT:** disabled

## Path mix preview

- LIGHT: 22
- MEDIUM: 10
- FULL: 8
- HOLD: 0 (HOLD policy = NONE per operating notes)

---

## Per-record audit

### Cerebrium (297918677725)
- Path: FULL
- Domain: cerebrium.ai (no change)
- Segment: NeoCloud -> Flagged for deletion
- Sub-segment: Tier 1 Inference - Neocloud -> (cleared)
- Confidence: high_90 -> high_90 (eviction)
- Tier: tier_2 -> (cleared via segment change)
- Customer protection invoked: no (no closed-won deal)
- Apollo used: no
- web_searches: 0 (provisioning_landscape already evidences SaaS layer; "serverless GPU across multiple cloud regions" = uses other clouds, doesn't own GPU infra)
- Completeness Gate: N/A (eviction)
- Reason: Serverless inference SaaS layer. 30 employees, Y Combinator seed, runs across multiple cloud regions. Does NOT own GPU infrastructure. Pattern matches FPX AI / Saturn Cloud SaaS-misclassified-as-NeoCloud eviction pattern.

### Inferless (297918677724)
- Path: FULL
- Domain: inferless.com (no change)
- Segment: NeoCloud -> Flagged for deletion
- Sub-segment: Tier 1 Inference - Neocloud -> (cleared)
- Confidence: high_90 -> high_90 (eviction)
- Tier: tier_2 -> (cleared)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: N/A (eviction)
- Reason: Serverless GPU SaaS wrapper. 30 employees, Sequoia-backed, "minimal DevOps overhead for inference workloads" = abstraction layer over hyperscaler GPU. Does NOT own underlying compute. Same SaaS-as-NeoCloud pattern.

### NewYork GreenCloud (300340117192)
- Path: LIGHT
- Domain: nygreencloud.com (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0 (record current per Apr 2026 enrichment)
- Completeness Gate: pass
- Reason: Carbon-negative biomass-powered AI factories in NY + CA. Owns infrastructure. AI Infrastructure providers - Neocloud holds.

### Exoscale (298009434843)
- Path: MEDIUM
- Domain: exoscale.com (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud -> Sovereign AI Clouds - Neocloud
- Confidence: medium_7089 -> high_90
- Tier: tier_1 (unchanged; both sub-segments default T1)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: 8 DCs across Switzerland/Germany/Austria/Bulgaria/Croatia with explicit EU sovereignty positioning. "All infrastructure based in EU" + GDPR-compliant + data sovereignty pitch. Sovereign AI Clouds fits the canonical pattern better than generic AI Infrastructure providers.

### Novita AI (300372855493)
- Path: FULL
- Domain: novita.ai (no change)
- Segment: NeoCloud -> Flagged for deletion
- Sub-segment: Tier 1 Inference - Neocloud -> (cleared)
- Confidence: high_90 -> high_90 (eviction)
- Tier: tier_2 -> (cleared)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: N/A (eviction)
- Reason: 30 employees + "200+ AI model APIs" + pay-per-token + "global GPU deployment across 20+ locations" = inference-as-a-service SaaS aggregator, not GPU owner. COMPUTER_SOFTWARE industry. Same SaaS-as-NeoCloud pattern as Cerebrium/Inferless.

### Freyr (300361949930)
- Path: LIGHT
- Domain: freyr-ai.sg (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: $1.4B Gorilla SEA DC network contract is a real infrastructure play. NVIDIA Preferred Partner. Holds.

### AceCloud (298005835458)
- Path: LIGHT
- Domain: acecloud.ai (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: 350 employees, India-first GPU cloud (H100/A100/L40S). Real infrastructure. Holds.

### TensorDock (297987984067)
- Path: FULL
- Domain: tensordock.com (no change)
- Segment: NeoCloud -> Flagged for deletion
- Sub-segment: AI Infrastructure providers - Neocloud -> (cleared)
- Confidence: high_90 -> high_90 (eviction; verified)
- Tier: tier_1 -> (cleared)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified Voltage Park acquisition Mar 2025)
- Completeness Gate: N/A (eviction)
- Reason: Confirmed acquired by Voltage Park 2025-03-26 (Crunchbase + Yahoo Finance + Business Wire). 30 employees. Marketplace aggregator across 100+ third-party locations, does not own underlying GPU compute. Same SaaS-marketplace-as-NeoCloud pattern. **R3 dedup flag for Cooper:** check if Voltage Park exists as a separate HubSpot record - TensorDock now operates as a Voltage Park brand per acquisition press release.

### Swisscom AI (303848694494)
- Path: LIGHT
- Domain: swisscom.com (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: Sovereign AI Clouds - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Swisscom subsidiary, Switzerland's first NVIDIA SuperPOD, sovereign data residency. Tier 1 holds.

### Fastweb AI (303926291174)
- Path: LIGHT
- Domain: fastweb.it (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: Sovereign AI Clouds - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Fastweb subsidiary, Italian sovereign GenAI platform, NVIDIA DGX SuperPOD. Tier 1 holds.

### Subsea Cloud (316164220624)
- Path: MEDIUM
- Domain: subseacloud.com (no change)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo -> Modular - colo
- Confidence: medium_7089 -> medium_7089
- Tier: tier_3 -> tier_1 (Modular - colo algorithmic default; no signal modifiers fire)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified mixed operational + announced site status)
- Completeness Gate: pass
- Reason: 30-employee subsea container-pod colo with proprietary nonconductive liquid cooling (PUE 1.01). Mixed operational + announced sites in North Sea, Port Angeles, Gulf of Mexico. Container pods + 800 servers per pod + per-site form factor = canonical Modular - colo (operational milestone reached, so NOT Greenfield per §7 migration). Infrastructure_profile Facilities: Small mismatches canonical Mid-Size/Large -> confidence held at medium_7089.

### Telkomnet (316237316830)
- Path: LIGHT
- Domain: (no domain field set; verify in HubSpot)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Long Haul / Backbone - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: 176K+ km national backbone (Indonesia). Spin-off PT Telkom Infrastruktur Indonesia in progress. **R3 dedup flag raised:** check Telkom Indonesia / PT Telkom parent record - if present, this record represents the wholesale-arm under D2 policy and may need cross-parent promotion (Network Operator(Tier 1 / VNO) / Pure Wholesale Carrier - Network Op).

### farmGPU (311548817115)
- Path: LIGHT (+ data quality patch)
- Domain: farmgpu.com (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: (was unset) -> medium_7089
- Tier: tier_1 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified 10 employees, Conscious Capital DC colo)
- Completeness Gate: pass
- Reason: Small NeoCloud colocated at Conscious Capital Data Center (Rancho Cordova, 7MW). Tokenized GPU marketplace via Silicon Protocol NFT partnership. Owns GPUs (not third-party aggregation) so survives SaaS-eviction check. **Data quality patch:** numberofemployees 22000 -> 10 (web-verified; was Apollo copy/paste error). Industry FOOD_PRODUCTION is also wrong but not patched (would require Apollo refresh; flagged for Cooper).

### LS Power (311418164947)
- Path: FULL
- Domain: lspower.com (no change)
- Segment: MSP/Aggregator -> Flagged for deletion
- Sub-segment: Standard - colo -> (left as-is; non-ICP)
- Confidence: manual_review_required -> high_90 (eviction)
- Tier: tier_3 -> (cleared via non-ICP segment)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: N/A (eviction)
- Reason: Independent power company - 23,000 MW generation + 780 miles transmission lines. $12B NRG acquisition pending. NOT a data center, fiber, MSP, or network ICP. Phase 2 audit (CLAUDE.md "Known Data Quality Follow-ups" #1) flagged this as 1 of 5 MSP/Aggregator records with mismatched colo sub-segment. Resolved: hard evict per Cooper "aggressive Flagged for deletion for non-fits" operating principle.

### Lonestar Data Holdings (311409164986)
- Path: FULL
- Domain: lonestarlunar.com (no change)
- Segment: MSP/Aggregator -> Flagged for deletion
- Sub-segment: Standard - colo -> (left as-is; non-ICP)
- Confidence: manual_review_required -> high_90 (eviction)
- Tier: tier_3 -> (cleared)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: N/A (eviction)
- Reason: 21-employee experimental lunar data storage company (St Petersburg FL). $15.5M raised. "Demonstrated live data storage on Moon via Intuitive Machines lander." Not a commercial-scale terrestrial DC, fiber, or MSP. Same Phase 2 audit cohort as LS Power. Hard evict.

### PTS Data Center Solutions (311385168607)
- Path: MEDIUM
- Domain: ptsdcs.com (no change)
- Segment: MSP/Aggregator -> Data Center Colo Provider (CROSS-PARENT)
- Sub-segment: Standard - colo (unchanged - sub-segment was already correct)
- Confidence: manual_review_required -> medium_7089
- Tier: tier_3 (unchanged - Standard - colo default = T3)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Oakland NJ colocation provider, $20.3M revenue, 35-person team. Custom design/build/operate model with Grid7 microgrid integration. Phase 2 audit cohort. Resolution: parent segment corrected to Data Center Colo Provider (was the right answer all along; sub-segment was already correct - parent was misaligned).

### Telin (320811765444)
- Path: LIGHT (target_account frozen)
- Domain: telin.com (no change)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: medium_7089 (unchanged)
- Tier: tier_3 (FROZEN by hs_is_target_account=true; skipped per Step A of compute_tier)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: US-based UCaaS distributor for MSPs (Texas). 3CX cloud hosting, SIP trunks. Note in record disambiguates from Indonesian PT Telin parent. Cooper override locked tier.

### InfiniVAN (316133717741)
- Path: LIGHT
- Domain: infinivan.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Long Haul / Backbone - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Japanese-Filipino telecom with 2,500 km submarine + nationwide terrestrial fiber. Mixed pure-play vs hybrid - has BOTH submarine AND terrestrial, so NOT Subsea cable operator (which is pure-play). Landmark Luzon Bypass Infrastructure lease 2026-03 is recent. Long Haul / Backbone holds.

### RidgeLink (314333478624)
- Path: LIGHT
- Domain: ridgelinkllc.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Dark Fiber Specialist - Fiber Operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Subsidiary of Blue Ridge Energy (NC). Dark fiber + colocation via LIT Networks consortium reaching Atlanta + Northern Virginia peering. Holds.

### Fiberlux (316133717744)
- Path: LIGHT
- Domain: fiberlux.pe (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_3 (unchanged)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Peru regional fiber operator. 14K km network, 92 cities, 5K corporate customers. $60M expansion + 2026 DC build. Capitalizing on Telefonica Peru exit. Holds.

### 3DS Communications (268241646270)
- Path: LIGHT
- Domain: 3dsc.co (no change)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Texas-based aggregator with 70+ carrier relationships. Classic Telecom Aggregator pattern. Holds.

### QuestZones (268210252477)
- Path: LIGHT
- Domain: questzones.com (no change)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Managed Network Services - MSP (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: North American MNSP (Canada/US/UK/Germany) serving multi-location retail. Holds.

### Fidalia Networks (268252506816)
- Path: LIGHT
- Domain: fidalia.com (no change)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Managed Network Services - MSP (unchanged)
- Confidence: medium_7089 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Mississauga ON MSP. 3CX partner, 7K endpoints. Resells biz internet + phone systems + Office 365. Holds.

### Domyn (322837059308)
- Path: MEDIUM (geo correction + sub-segment shift)
- Domain: domyn.io (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud -> Sovereign AI Clouds - Neocloud
- Confidence: medium_7089 -> high_90
- Tier: tier_1 (unchanged - both default T1)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified Italian HQ via NVIDIA + Vertiv press releases)
- Completeness Gate: pass
- Reason: Formerly iGenius, rebranded Domyn. Italian sovereign AI cloud building Colosseum NVIDIA DGX SuperPOD (115 exaflops, Italy-based, renewable-powered). G42 strategic partner + lead financier. Explicit sovereign AI positioning. **Apollo geo error patch:** country France -> Italy, state Ile-de-France -> Lombardy (Milan area, iGenius HQ). Owner unchanged (Tim Z International). Pattern: SaaS-as-NeoCloud false-positive avoided - this one OWNS the infrastructure (Colosseum supercomputer).

### Sharon AI (322836352708)
- Path: LIGHT
- Domain: sharonai.com.au (no change)
- Segment: NeoCloud (unchanged)
- Sub-segment: AI Infrastructure providers - Neocloud (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Australian GPUaaS deploying 1000 B200 GPUs at NEXTDC M3 Melbourne. $500M debt facility, 20K+ GPU target. Owns GPUs (colocates at NEXTDC). Holds.

### Media Commerce (316283788004)
- Path: MEDIUM (sub-segment promotion within Fiber parent)
- Domain: mc.net.co (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator -> Long Haul / Backbone - Fiber operator
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_2 (Long Haul / Backbone default T2)
- web_searches: 0
- Completeness Gate: pass
- Reason: Colombian fiber operator with 14K km network across 300+ cities + 87% national GDP coverage + multi-country footprint (Colombia + Peru + Ecuador) + 1250 employees + Enterprise POPs (100+). National-scale operator pattern - "Regional CLEC" understates the scope. Pattern: National operator under-tiering.

### Rohl Gateway Fiber (316210812650)
- Path: LIGHT
- Domain: rohlgatewayfiber.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Dark Fiber Specialist - Fiber Operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Western Canada dark fiber operator. 1200+ km plant, expanding 400G wavelength. Subsidiary of ROHL Global Networks. Holds.

### Turkcell (316278520569)
- Path: FULL (cross-parent reclassification)
- Domain: turkcell.com.tr (no change)
- Segment: Fiber Operator -> Network Operator(Tier 1 / VNO) (CROSS-PARENT)
- Sub-segment: Regional CLEC - Fiber operator -> Tier 1 Carrier - Network Op
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_1 (Tier 1 Carrier default T1, ceiling 1, floor 2)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0 (Turkcell is a verified Tier 1 carrier anchor)
- Completeness Gate: pass
- Reason: Major Turkish telecom - $4B revenue, 26000 employees, 6M fiber homes across 28 provinces, multiple data centers (Gebze, Temelli, Izmir, Europe), Tier-1 global interconnections via Superonline subsidiary, ops in Turkey + Belarus + Northern Cyprus + Netherlands. This is textbook national incumbent / Tier 1 Carrier. Massive under-tier (T3 -> T1) as Regional CLEC. Pattern: National operator under-tiering (cumulative ~23 across sweep).

### HyperLink Infrastructure, LLC (316164220626)
- Path: LIGHT
- Domain: hyperlink-networks.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Dark Fiber Specialist - Fiber Operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Vertically integrated dark fiber for hyperscalers / AI infrastructure. Purpose-built routes with in-house design + construction + maintenance. Florida HQ. Holds.

### LG Uplus (320811765448)
- Path: LIGHT
- Domain: lguplus.com (no change)
- Segment: Network Operator(Tier 1 / VNO) (unchanged)
- Sub-segment: Tier 1 Carrier - Network Op (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: South Korea's 2nd-largest wireless carrier. 18.4M subscribers, $10.9B revenue. LG Corp subsidiary. Tier 1 holds.

### Yondr (316194606814)
- Path: LIGHT
- Domain: overyondr.com (no change)
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Hyperscale Wholesale - colo (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_1 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Hyperscale DC developer/operator, 878MW contracted (58MW operational), DigitalBridge-owned (acquired 2025). Multi-region Americas/Europe/Asia. Hyperscale Wholesale holds.

### GDS (316179533504)
- Path: LIGHT
- Domain: gds.com.lb (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: medium_7089 (unchanged)
- Tier: tier_3 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Lebanon's GlobalCom Data Services. National wireless microwave + DSL. 20 employees, POPs Mid-Size. Small national operator but only 20 employees keeps it at Regional CLEC scale. Holds.

### Netvata (268210252479)
- Path: LIGHT
- Domain: netvata.com (no change)
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: St. Petersburg FL MDU broadband + smart home + IoT for apartments. Reseller layer pattern. Holds.

### Fidelity Communications (297918677709)
- Path: LIGHT (+R3 dedup flag)
- Domain: fidelitycommunications.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Long Haul / Backbone - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Sparklight family brand owned by Cable One (national cable MSO). 22K+ route miles across 5 states (AR/LA/MO/OK/TX). Cable One is a recognized national cable MSO that, if represented separately in CRM, takes precedence under D2 (wholesale-arm policy). **R3 dedup flag raised** for Cable One / Sparklight parent check.

### Spry Servers (268208452323)
- Path: FULL
- Domain: spryservers.net (no change)
- Segment: MSP/Aggregator -> Flagged for deletion
- Sub-segment: Telecom Aggregator - MSP -> (left as-is; non-ICP)
- Confidence: medium_7089 -> high_90 (eviction)
- Tier: tier_2 -> (cleared)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified shutdown via LowEndTalk + Crunchbase + Spry's own 2023-08-25 announcement)
- Completeness Gate: N/A (eviction)
- Reason: Confirmed shutdown August 25, 2023 - "life as a hosting company has come to an end." Phoenix datacenter services became unavailable and unrecoverable. Network + select client accounts sold to private party. The remaining "asset-light entity" is a shell, not a viable MaiaEdge target. Hard evict.

### EMPOWER Broadband (297984383729)
- Path: FULL (template-bleed regen + sub-segment reclassification)
- Domain: empowermec.net (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator -> Municipal / Cooperative - Fiber operator
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_4 (Municipal / Cooperative default T4, ceiling 2, floor 5)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 1 (verified cooperative status + service area + scale)
- Completeness Gate: pass
- Reason: Wholly-owned broadband subsidiary of Mecklenburg Electric Cooperative (MEC) - founded 1938 electric coop migrating into broadband. 2,900 miles fiber across Southside VA + Northern NC counties (Halifax/Charlotte/Mecklenburg/Brunswick/Greensville). 5,000+ retail customers. Cooperative ownership = textbook Municipal / Cooperative sub-segment. **Template-bleed remediation:** prior account_brief was "research needed for account brief" placeholder - regenerated.

### Ponderosa Telephone (297944750823)
- Path: LIGHT
- Domain: goponderosa.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_3 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Family-owned California ILEC since 1908. Sierra Nevada rural fiber + DSL + fixed wireless. iVUE portal. USDA ReConnect III funded. Holds.

### Silver Star Communications (297782865621)
- Path: LIGHT
- Domain: silverstar.com (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_3 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Family-owned WY/ID rural telecom since 1912. 1,800+ miles owned fiber. SmartHub portal + API + auto-provisioning. Holds.

### Bristol Tennessee Essential Services (320873732836)
- Path: MEDIUM (sub-segment within parent)
- Domain: btes.net (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional Cable Operator - Fiber operator -> Municipal / Cooperative - Fiber operator
- Confidence: high_90 (unchanged)
- Tier: tier_3 -> tier_4 (Municipal / Cooperative default T4)
- Customer protection invoked: no
- Apollo used: no
- web_searches: 0
- Completeness Gate: pass
- Reason: Municipally-owned utility since 1945 (City of Bristol TN). Provides electricity + fiber + cable TV + phone across 280 sq mi. 34K electric + 19K fiber customers. Cooperative/municipal ownership pattern - reclassify from Regional Cable Operator to Municipal / Cooperative.

### Leaco Rural Telephone Cooperative (303912468211)
- Path: LIGHT
- Domain: leaco.org (no change)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Municipal / Cooperative - Fiber operator (unchanged)
- Confidence: (unset/null - no change written)
- Tier: tier_4 (unchanged)
- web_searches: 0
- Completeness Gate: pass
- Reason: Member-owned regional cooperative serving southeast New Mexico since 1954 (Hobbs/Lovington/Tatum). Holds.

---

## Batch summary

- Processed: 40/40 unique records (50 pulled, 10 duplicates via offset wrap-around)
- Path mix: LIGHT 22 · MEDIUM 7 · FULL 11 · HOLD 0
- HubSpot writes: 4 batches of 10 (10/10/10/10)
- Apollo used: 0
- web_searches: 6 total (Spry, EMPOWER, farmGPU, Subsea Cloud, Domyn, TensorDock)

### Notable changes
1. **Cross-parent reclassifications (3):** Turkcell (Fiber -> Network Op / Tier 1 Carrier T3->T1), PTS DCS (MSP -> Data Center Colo Provider T3 holds), LS Power + Lonestar (MSP -> Flagged for deletion)
2. **Within-parent sub-segment shifts (5):** Subsea Cloud (Standard -> Modular - colo, T3->T1), Exoscale (AI Infra -> Sovereign AI), Domyn (AI Infra -> Sovereign AI), Media Commerce (Regional CLEC -> Long Haul/Backbone T3->T2), EMPOWER Broadband (Regional CLEC -> Municipal/Coop T3->T4), BTES (Regional Cable -> Municipal/Coop T3->T4)
3. **Evictions to Flagged for deletion (7):** Cerebrium, Inferless, Novita AI, TensorDock (4 SaaS-as-NeoCloud pattern); LS Power, Lonestar Data Holdings (2 Phase 2 audit cohort - power utility / lunar experimental); Spry Servers (shutdown 2023)
4. **Confidence upgrades (3):** Exoscale, Domyn, farmGPU all moved to high_90 / medium_7089 with stronger evidence basis
5. **Apollo geo error patches (1):** Domyn country France -> Italy, state Ile-de-France -> Lombardy (verified via NVIDIA + Vertiv press releases)
6. **Data quality patches (1):** farmGPU numberofemployees 22000 -> 10 (web-verified; Apollo copy/paste error)
7. **Template-bleed remediations (1):** EMPOWER Broadband (placeholder "research needed for account brief" regenerated)
8. **R3 dedup flags raised (2):** Telkomnet (PT Telkom Indonesia parent), Fidelity Communications (Cable One / Sparklight parent), TensorDock (Voltage Park acquirer)

### Patterns continued from prior batches
- **SaaS misclassified as NeoCloud:** 4 evictions this batch (Cerebrium, Inferless, Novita AI, TensorDock). Cumulative ~7 across sweep including prior FPX/Saturn Cloud + Conexum.
- **National operator under-tiering:** 2 promotions (Turkcell -> Tier 1 Carrier T3->T1; Media Commerce -> Long Haul/Backbone T3->T2). Cumulative ~24 across sweep including prior Terranet Lebanon.
- **Apollo geo error patches:** 1 patch (Domyn FR->IT). Cumulative ~3 across sweep.
- **Template-bleed remediation:** 1 regen (EMPOWER Broadband). Cumulative ~3 across sweep.
- **Phase 2 audit MSP+colo cohort:** 3 of 5 records processed this batch (LS Power, Lonestar, PTS DCS - resolved 2 evictions + 1 cross-parent fix). Remaining: Mapletree, Montera Infrastructure (Montera already processed in earlier batch).

### Data quality follow-ups for Cooper
1. **farmGPU industry:** Apollo set FOOD_PRODUCTION; should be COMPUTER_HARDWARE or INFORMATION_TECHNOLOGY_AND_SERVICES. Not patched (would require Apollo refresh).
2. **Domyn domain check:** HubSpot has `domyn.io` but the company website is `domyn.com`. Verify in HubSpot.
3. **Telkomnet domain field:** appears unset in HubSpot search response. Verify directly.

### Drain projection
- Pool before batch 28: 1,439
- Records stamped 2026-05-18 this batch: 40
- Pool after batch 28: ~1,399
- ETA: ~28 more batches at BATCH_SIZE=50 (40 effective unique)

