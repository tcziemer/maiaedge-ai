# Mass Re-Enrichment Sweep — Batch 10

**Sweep:** `2026-05-18-post-phase-3-framework`
**Batch:** 10
**Run date:** 2026-05-18
**Operator:** CRM Guardian (Cowork)
**Apollo this batch:** 0 credits
**Records processed:** 50 / 50
**Pool remaining (post-batch):** 2,265

## Summary

| Path | Count |
|---|---:|
| LIGHT | 0 |
| MEDIUM | 47 |
| FULL | 3 |
| HOLD | 0 |

**Tier promotions (toward T1):** 11
**Tier demotions (toward T5):** 3
**Skipped (hs_is_target_account=true):** 1 (Cable Bahamas)
**Sub-segment migrations:** 14
**Segment changes (cascade fired):** 7
**Flagged-for-deletion writes:** 2 (Atherton Fiber, Shaw)
**Customer-protection HOLDs:** 0
**Completeness Gate fails:** 0
**Manual-review HOLDs:** 0
**Write failures (retried successfully):** 4 (3 hyperscaler_proximity enum + 1 fabric_provisioning_approach enum)

## Per-record changes

### Chunk 1 (records 1-10)

#### Sterling Communications (268204721856) — MEDIUM
- Path: MEDIUM
- Domain: sterling.net
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_2 (unchanged)
- Apollo: no  ·  web_searches: 0
- Reason: brief regenerated to strip "Network Isolation"/"polite chaos"/"MaiaEdge offers" marketing bleed; provisioning_landscape tightened to 3 sentences; filled hyperscaler_proximity (None Known) and fabric_provisioning_approach (manuallegacy_processes).

#### OCOSA Communication (268250706654) — MEDIUM
- Segment: Data Center Colo Provider (unchanged)
- Sub-segment: Standard - colo (unchanged)
- Tier: tier_3 (unchanged)
- Reason: brief regenerated to strip marketing bleed; provisioning_landscape tightened; filled hyperscaler_proximity.

#### Claro Puerto Rico (267927865026) — FULL — *segment change*
- Path: FULL
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC - Fiber operator -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> **tier_1** (2-tier promotion)
- Confidence: medium_7089 -> high_90
- Reason: 4,649 employees, $1.2B revenue, 10K route miles, 250 facilities, mobile + fixed + fiber + 5G, América Móvil subsidiary - national Tier 1 incumbent in Puerto Rico, not Regional CLEC. Cascade fires.

#### GiGstreem (266871288513) — MEDIUM — *sub-segment fix*
- Sub-segment: Long Haul / Backbone - Fiber operator -> **Regional CLEC - Fiber operator**
- Tier: tier_2 -> **tier_3** (demotion)
- Reason: multifamily-focused MDU fiber ISP (100K+ households across 26 states), not long-haul backbone.

#### Atherton Fiber (268073696977) — FULL — *eviction*
- Segment: Fiber Operator -> **Flagged for deletion**
- Reason: defunct as standalone - acquired by Race Communications August 2025. Flagged for R3 consolidation under primary Race Communications record.

#### Salish Networks (268241646266) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Municipal / Cooperative - Fiber operator**
- Tier: tier_3 -> **tier_4** (demotion)
- Reason: Tulalip Tribes owned and operated tribal cooperative pattern matches Municipal / Cooperative classification.

#### Hydro One Telecom (268208411378) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: 5,406 route miles, 80 POPs across Canadian Northeast - long-haul backbone scale, not regional CLEC. Operates as Acronym Solutions following 2022 rebrand. Name + domain left as-is pending D7 verification.

#### Tierzero (268210252475) — MEDIUM — *segment change*
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator -> **Telecom Aggregator - MSP**
- Tier: tier_3 -> **tier_2** (promotion)
- Confidence: high_90 -> medium_7089
- Reason: VoIP-heavy + Hosted PBX + 14 employees + 60K users + managed services - matches Teliax / Ringer voice-aggregator pattern. Cascade fires.

#### Shaw (268241651447) — FULL — *eviction*
- Segment: Fiber Operator -> **Flagged for deletion**
- Reason: defunct as standalone - integrated into Rogers Communications April 2023. Flagged for R3 consolidation under primary Rogers record.

#### Neutral Networks (267969423053) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: 5,000km cross-border Mexico-US backbone buildout, $35M SummitIG partnership, multiple cross-border crossings - wholesale backbone pattern. Filled fabric_provisioning_approach (manuallegacy_processes).

### Chunk 2 (records 11-20)

#### Point Broadband (266871288512) — MEDIUM — *sub-segment fix*
- Sub-segment: Long Haul / Backbone - Fiber operator -> **Tier 2 National Wholesale - Fiber operator**
- Tier: tier_2 (unchanged)
- infrastructure_profile: Route Miles Mid-Size -> **Route Miles: Large (10K-50K)** (12,704 route miles)
- Reason: rural FTTH consolidator with 12,700 route miles + Clearwave Fiber merger January 2026.

#### Galaxy Broadband Communications (268250706651) — MEDIUM
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Reason: brief tightened, provisioning concise. Canadian satellite + wireless + fibre MSP, classification correct.

#### CoreTel (268215653050) — MEDIUM
- Confidence: high_90 -> medium_7089
- Reason: brief regenerated (was 1 sentence); flagged for D7 deeper research on Mid-Atlantic CLEC footprint and scale.

#### Mark Twain Rural Telephone Company (268243489495) — MEDIUM
- Sub-segment: Municipal / Cooperative - Fiber operator (unchanged)
- Tier: tier_4 (unchanged)
- Reason: brief expanded to reflect cooperative model + Edina FTTH USDA RUS grant.

#### UScellular (266871288515) — MEDIUM
- Sub-segment: Standard - colo (unchanged)
- Confidence: high_90 -> medium_7089
- Reason: brief regenerated to reflect Array Digital Infrastructure rebrand post-T-Mobile wireless sale. Tower-to-colo pivot mid-flight; flagged for D7 deeper research.

#### Empire Access (268250706638) — MEDIUM
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Reason: brief tightened from 5-paragraph overlong to 4 sentences.

#### GalaxyVisions (268210252480) — MEDIUM
- Confidence: high_90 -> **low_5069**
- Reason: prior enrichment likely conflated record with Galaxy Digital's data center business (Helios campus, CoreWeave lease). Brief stripped of fabricated content. recent_news annotated with D7 escalation flag.

#### Cable Bahamas (320874452689) — MEDIUM — *tier write SKIPPED*
- `hs_is_target_account = true` -> tier write skipped per Step A of compute_tier
- Confidence: medium_7089 -> high_90
- Reason: brief tightened, marketing bleed stripped. Liberty Newco merger noted. All other writes proceeded; account_tier left unchanged at tier_1.

#### Capcon Networks (268250706648) — MEDIUM
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Reason: brief tightened, classification correct.

#### Countryside Broadband (268073704129) — MEDIUM
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Reason: brief tightened, classification correct.

### Chunk 3 (records 21-30)

#### Cobalt Ridge (268241646269) — MEDIUM — *Apollo data fix*
- state: **Ile-de-France** -> **Texas** (Apollo data error - HQ is North Texas, not France)
- country: stays United States
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Reason: state fixed, brief regenerated, filled fabric_provisioning_approach.

#### QuestBlue (251587604214) — MEDIUM
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Reason: brief tightened, classification correct.

#### Syniverse Technologies (268012614344) — MEDIUM
- Sub-segment: Pure Wholesale Carrier - Network Op (unchanged)
- Tier: tier_1 (unchanged)
- Reason: brief tightened to focus on 100+ POPs, $4.15B revenue, Iridium D2D partnership.

#### SG.GS (268208452327) — MEDIUM — *segment change*
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator -> **Telecom Aggregator - MSP**
- Tier: tier_3 -> **tier_2** (promotion)
- Confidence: medium_7089 (unchanged)
- Reason: 15 employees + claimed 200+ POPs is structurally inconsistent with operating a true global wholesale carrier; matches Apollo data hallucination + virtual-aggregator pattern. Cascade fires.

#### CBC Tech (268208411376) — MEDIUM — *sub-segment fix*
- Sub-segment: Telecom Aggregator - MSP -> **Cloud + Telecom Hybrid MSP - MSP**
- Tier: tier_2 (unchanged)
- Reason: China NaaS provider with SD-WAN + multi-cloud + SASE + 80+ POPs + eNet Connect Portal - hybrid cloud + telecom model.

#### M3COM of Virginia (268195762878) — MEDIUM — *sub-segment fix*
- Sub-segment: Telecom Aggregator - MSP -> **Cloud + Telecom Hybrid MSP - MSP**
- Tier: tier_2 (unchanged)
- Reason: VNO with 160+ carriers + Private/Public/Hybrid Cloud + PaaS + Colocation + MPLS + SDWAN/SASE - cloud + telecom hybrid model.

#### Zayo Europe (268250706647) — MEDIUM — *sub-segment fix + enum retry*
- Sub-segment: Tier 2 National Wholesale - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_2 (unchanged)
- fabric_provisioning_approach: corrected `equinix_fabric` (invalid) -> `equinix_ecx_fabric` (allowed enum)
- Reason: 1.4M route miles + pan-European backbone + Iberia 400GE wavelength + Equinix AI Infrastructure Blueprint - long-haul backbone scale.

#### Internet Initiative Japan (268241646268) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Tier 2 National Wholesale - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: Japan's first ISP + national + 16 facilities + 5,221 employees + $450M revenue + multi-service - national wholesale + retail scope.

#### Astound Business Solutions (268070011605) — MEDIUM
- Confidence: high_90 -> medium_7089
- Reason: multi-service (fiber + colo + cloud + security) blurs primary classification; flagged for D7 deeper research on whether to remain Colo or reclassify under parent Astound Broadband.

#### Telehouse Deutschland (268111627983) — MEDIUM
- Sub-segment: Standard - colo (unchanged)
- Reason: brief tightened; classification correct. Megaport + PacketFabric integrations preserved.

### Chunk 4 (records 31-40)

#### PEG TECH (268070011603) — MEDIUM
- Confidence: high_90 -> medium_7089
- Reason: hosting-heavy product mix (Raksmart, PetaExpress brands) - flagged for D7 to verify colo vs hosting-reseller classification.

#### RETELIT (268111627986) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: 47,000 route miles + 286 POPs + national Italian B2B backbone + MavianMax + BT Italia acquisitions.

#### TELCABLES EUROPE (267927865024) — MEDIUM — *segment change*
- Segment: Data Center Colo Provider -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Standard - colo -> **Subsea cable operator** (Phase 3 new sub-segment)
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: Angola Cables European subsidiary - subsea cable systems (SACS, MONET) connecting Europe/Africa/Americas with cable landing operations in Sines and Lisbon. Cleared inflated 960-facility infrastructure_profile. Cascade fires.

#### Blue Stream Fiber (132992626399) — MEDIUM — *Apollo data fix*
- state: **Massachusetts** -> **Florida** (HQ Coral Springs, FL)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Reason: state corrected; brief tightened. 500+ employees, $750M revenue, FL+TX, Sixth Street/GI Partners backing - sizable regional fiber operator.

#### DC BLOX (193867596501) — MEDIUM — *enum retry*
- Sub-segment: AI Signals - colo (unchanged)
- Tier: tier_1 (unchanged)
- hyperscaler_proximity: enum corrected from "Confirmed: <10 miles" (invalid) -> "Existing Facility Nearby" (allowed)
- Reason: brief tightened. Google, Meta tenants + AI-ready capacity + 11 DCs + 600-mile fiber across 6 SE states - AI Signals classification correct.

#### Great Plains Communications (193856074473) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional Cable Operator - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: 20,000+ route miles fiber (not cable) across 13 states, $500M financing, hyperscaler customer base, Aphorio Carter Kentucky colo partnership.

#### Smithville Communications (193906531018) — MEDIUM
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Reason: brief tightened; classification correct.

#### US Signal (193853195963) — MEDIUM — *sub-segment fix*
- Sub-segment: Regional CLEC - Fiber operator -> **Long Haul / Backbone - Fiber operator**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: 14,000 route miles + 16 data centers + 225 POPs across 10 states + $200M capex + OneNeck acquisition. Igneo Infrastructure portfolio asset.

#### Vantage Data Centers (300406714054) — MEDIUM — *contamination cleanup + enum retry*
- Sub-segment: Hyperscale Wholesale - colo (unchanged)
- Tier: tier_1 (unchanged)
- Confidence: manual_review_required -> **high_90**
- hyperscaler_proximity: enum corrected "Confirmed: <10 miles" (invalid) -> "Existing Facility Nearby"
- infrastructure_profile: Mid-Size (5-19) -> **Large (20-49)** (35 global campuses)
- Reason: prior record contaminated with AtlasEdge tenant pain-point content (different company); cleaned up to focus on Vantage's $13B financing, $25B Frontier Texas campus, OpenAI/Oracle Stargate Port Washington 1GW partnership.

#### Netrality (194005222091) — MEDIUM — *Apollo data fix + enum retry*
- state: **Florida** -> **Pennsylvania** (HQ Philadelphia)
- Sub-segment: Standard - colo (unchanged)
- hyperscaler_proximity: enum corrected "Confirmed: <10 miles" (invalid) -> "Existing Facility Nearby"
- Reason: state corrected; provisioning_landscape filled (was "Research needed"); brief expanded with carrier hotel + Meet Me Rooms + 100+ MW + 18 properties context. $605M financing July 2025 noted.

### Chunk 5 (records 41-50)

#### DOCOMO PACIFIC (251526039249) — FULL — *segment change + revenue fix*
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Regional CLEC - Fiber operator -> **Tier 1 Carrier - Network Op**
- Tier: tier_3 -> **tier_1** (2-tier promotion)
- Confidence: medium_7089 -> high_90
- annualrevenue: $52.6B (NTT parent bleed) -> cleared
- Reason: regional Tier 1 incumbent of Guam/CNMI/Micronesia (NTT DOCOMO subsidiary, 5G LTE leader, multi-gig fiber, all triple-play + wholesale). Cascade fires.

#### Deutsche Telekom AI Cloud (303925580502) — FULL — *segment change + scale fix*
- Segment: Network Operator(Tier 1 / VNO) -> **NeoCloud**
- Sub-segment: Tier 1 Carrier - Network Op -> **Sovereign AI Clouds - Neocloud**
- Tier: tier_1 (unchanged - within ceiling)
- annualrevenue: $113.3B (parent bleed) -> cleared
- numberofemployees: 217,000 (parent bleed) -> cleared
- geographic_focus: "National, Europe, North America, Asia, Africa" -> "Germany; European data sovereignty focus"
- Reason: record name identifies AI cloud venture, not parent telco. EUR 1B NVIDIA joint investment, 10,000 Blackwell GPUs, 0.5 exaFLOPS Q1 2026, SAP + Polarise partners - sovereign AI cloud business. Cascade fires.

#### Spectrum Business (175162002126) — MEDIUM
- Sub-segment: Cable MSO Enterprise Division - Network Op (unchanged)
- Tier: tier_1 (unchanged)
- fabric_provisioning_approach: added `equinix_ecx_fabric` to existing approach
- Reason: brief tightened; Charter-Cox $34.5B merger approved April 2026 noted in brief.

#### AirTrunk (251591500490) — MEDIUM — *sub-segment fix*
- Sub-segment: AI Signals - colo -> **Hyperscale Wholesale - colo**
- Tier: tier_1 (unchanged)
- Confidence: manual_review_required -> **high_90**
- Reason: 1.2GW+ APMEA hyperscale wholesale, 5 campuses, A$5B+ planned expansion, Blackstone/CPPIB ownership - classic hyperscale wholesale model, not AI-density retail colo. Continues the AI Signals -> Hyperscale Wholesale flip pattern (CloudHQ, PowerHouse in batch 9).

#### Khazna Data Centers (251535204081) — MEDIUM
- Sub-segment: AI Signals - colo (unchanged)
- Tier: tier_1 (unchanged)
- Reason: brief tightened. NVIDIA-certified Blackwell AI factories + 70% UAE capacity + Dammam land acquisition + 1GW target = clean AI Signals classification. Apollo headcount of 30 noted as likely error.

#### Quantica Infrastructure (251526039255) — MEDIUM — *sub-segment fix (Greenfield)*
- Sub-segment: AI Signals - colo -> **Greenfield**
- Tier: tier_1 -> **tier_2** (demotion to Greenfield default within ceiling)
- Reason: launched July 2025, EnCap Investments backed, 5,000-acre Montana site with NorthWestern Energy LOI, no operational facility yet - clean Greenfield play per Operating Principle 8. Auto-migrate to operational sub-segment when first site goes live.

#### Globalinx Data Centers (263729676020) — MEDIUM
- Sub-segment: Standard - colo (unchanged)
- Tier: tier_3 (unchanged)
- Reason: provisioning_landscape filled (was "Research needed"); brief expanded to capture MAREA/BRUSA subsea cable landing role + 2025 Sandbridge bore expansion.

#### Lightedge Solutions (193854635706) — MEDIUM — *segment change*
- Segment: Data Center Colo Provider -> **MSP/Aggregator**
- Sub-segment: Standard - colo -> **Cloud + Telecom Hybrid MSP - MSP**
- Tier: tier_3 -> **tier_2** (promotion)
- Reason: primary product is hybrid cloud management (IBM i/AIX, VMware, Nutanix, AWS/Azure) with colo as supporting infrastructure - matches Cloud + Telecom Hybrid MSP profile. Cascade fires.

#### 1623 Farnam (193867596523) — MEDIUM — *sub-segment fix*
- Sub-segment: Modular - colo -> **AI Signals - colo**
- Tier: tier_1 (unchanged)
- Reason: AI workload demand + Google Papillion proximity + $40M+ expansion + 60+ carriers + OmahaIX - AI Signals positioning, not modular.

#### 5C Data Centers (264355635939) — MEDIUM
- Sub-segment: AI Signals - colo (unchanged)
- Tier: tier_1 (unchanged)
- Confidence: manual_review_required -> **high_90**
- Reason: brief regenerated to clean framework-consistent statement on Brookfield/Deutsche Bank $835M funding + Hypertec acquisition + 5-state US presence + AI-ready positioning. Confidence cleared after framework alignment.

## Drain progress

- Batches completed so far: 10
- Records processed in this sweep: ~468 (~17% of estimated ~2,800 starting pool)
- Pool remaining (verified post-batch query): 2,265
- ETA: ~46 more batches at BATCH_SIZE=50

## Patterns and notes for continuation

1. **New enum cheatsheet (apply next batches):**
   - `hyperscaler_proximity` allowed: `Announced: <50 miles`, `Announced: 50-200 miles`, `Existing Facility Nearby`, `None Known` (do NOT use "Confirmed: <10 miles" or similar)
   - `fabric_provisioning_approach` allowed: `megaport`, `packetfabric`, `equinix_ecx_fabric` (NOT `equinix_fabric`), `console_connect`, `other_external_naas`, `lumen_private_connectivity_fabric`, `other_competitor_fabric`, `homegrownproprietary_platform`, `standard_ossbss_stack`, `manuallegacy_processes`, `none_identified`
2. **AI Signals -> Hyperscale Wholesale flip pattern continues** - AirTrunk this batch joins CloudHQ + PowerHouse (batch 9). Large multi-GW hyperscale operators with global cloud-provider tenant rosters are consistently misclassified as AI Signals.
3. **Greenfield as a real classification continues paying off** - Quantica Infrastructure this batch is a clean Greenfield play (launched July 2025, EnCap-backed, no operational site yet). Per Operating Principle 8.
4. **Apollo parent-revenue bleed pattern persistent** - $52.6B on DOCOMO Pacific (NTT parent), $113.3B on Deutsche Telekom AI Cloud (DT parent), $1.2B on Claro Puerto Rico (matches América Móvil arm, kept). Continue clearing parent bleed when detected on small operators.
5. **Apollo state errors persistent** - Cobalt Ridge state was Ile-de-France (should be Texas), Blue Stream Fiber state was Massachusetts (should be Florida), Netrality state was Florida (should be Pennsylvania). Continue cross-checking state vs geographic_focus when they conflict.
6. **VoIP-aggregator pattern under Fiber Op** - Tierzero this batch joins Teliax (batch 9) in flipping from Fiber Op to MSP/Aggregator Telecom Aggregator. VoIP-heavy + Hosted PBX + small headcount + retail subscriber model is the giveaway.
7. **Defunct/acquired entities** - 2 evictions this batch (Atherton Fiber -> Race Communications 2025-08; Shaw -> Rogers 2023). Flagged for R3 consolidation.
8. **Sub-segment ambiguity on multi-service operators** - Astound Business (fiber+colo+cloud+security), PEG TECH (hosting reseller pattern), UScellular (tower REIT pivot), CoreTel (limited disclosure), GalaxyVisions (Galaxy Digital conflation) all set to medium_7089 with D7 escalation. Expect D7 caseload to grow on this batch.
9. **`hs_is_target_account` tier freeze worked correctly** - Cable Bahamas tier write skipped per Step A; all other writes proceeded normally.
10. **Subsea cable operator sub-segment in active use** - TelCables Europe this batch is the second sweep classification under this Phase 3 new sub-segment.

## Run health

- Status: GREEN
- Errors: 4 enum-value rejections (all retried successfully on second call)
- Fatal aborts: none
- HubSpot 429s: none
- Concurrent batch detection: clean
- Framework reference last-modified check: no changes since SWEEP_KICKOFF_DATE
