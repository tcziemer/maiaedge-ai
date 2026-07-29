# Batch 13 - Mass Re-Enrichment Sweep 2026-05-18-post-phase-3-framework

**Date:** 2026-05-18
**Records processed:** 50 / 50
**Path mix:** LIGHT 5 · MEDIUM 33 · FULL 12 · HOLD 0
**Apollo this batch:** 0 credits
**Pool remaining after batch:** ~2,104
**Sweep cumulative drain:** ~631 / ~2,735 (~23%)
**ETA:** ~42 more batches at BATCH_SIZE=50

---

## Sub-batch A (records 1-10)

### Truvista Fiber (320874452690)
- Path: LIGHT
- Domain: truvista.biz (no correction)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional Cable Operator - Fiber operator (unchanged)
- Confidence: high_90 (unchanged)
- Tier: tier_3 (unchanged)
- Apollo used: no  ·  web_searches: 0
- Reason: Fresh news within 7 days, fields clean. Date bump only.

### Johnson County Fiber Network (297934868204)
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 (unchanged)
- Reason: Stale 2024 news cleared per >90-day policy.

### CC Communications (300406714053)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Undated news cleared.

### Imperial Technologies (297918677701)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: medium_7089 -> high_90
- Reason: Web research confirmed small-business technology reseller in Macon GA bundling internet/VoIP/mobile/security/GPS fleet tracking. Not an operator; retail/services model. Yelp-listed business. Aggressive Flag per Operating Principle #7.

### Power Protection Products (277390632690)
- Path: LIGHT
- Reason: 2,000 sq ft LoCoCoLo colo at HQ, 12 employees - marginal but defensible Standard - colo. Web confirmed; date bump.

### FPUAnet Communications (297888732866)
- Path: LIGHT
- Reason: Fields clean; date bump.

### Broadlinc (292767321826)
- Path: MEDIUM
- Reason: Thin brief beef-up; stale 2022 news cleared.

### Bonfire Infrastructure Group (292754055916)
- Path: MEDIUM
- Reason: Web confirmed legitimate open-access fiber operator (Southern Ute Tribe partnership). Stale 2024 news cleared.

### Hyperscale Data (266900721400)
- Path: MEDIUM
- Brief refresh: NVIDIA H100/B200/B300 GPU cloud launch H1 2026 (Michigan AI campus via Sentinum subsidiary, Alliance Cloud Services). $35.4M Series D ATM Feb 2026.
- Sub-segment: AI Signals - colo (held; conservative - hybrid colo + crypto-to-AI candidate but defensible as colo with GPU offering)
- Tier: tier_1 (unchanged)
- Reason: Material recent news refresh.

### Crystal Peaks Data Centers (292440195816)
- Path: FULL
- Sub-segment: Standard - colo -> **Greenfield**
- Geographic_focus fixed: "HQ: Unknown" -> "HQ: Washington | Scope: National | Multi-state pipeline"
- Reason: Web confirmed pre-operational; pre-leasing program, no operational facilities yet. Per Operating Principle #8.

## Sub-batch B (records 11-20)

### Carat Networks (298005834485)
- Path: LIGHT
- Reason: Toronto Standard - colo, fields clean.

### BluSky AI (268197561043)
- Path: FULL
- Sub-segment: AI Signals - colo -> **Greenfield**
- Tier: tier_1 -> tier_3 (Greenfield default)
- Reason: Pre-operational modular AI DC (SkyMods); LOIs only at Nephi UT + Mulhall OK, no operational sites.

### Form8tion (266840765116)
- Path: FULL
- Sub-segment: AI Signals - colo -> **Greenfield**
- Tier: tier_1 -> tier_3
- Reason: Madrid One 100+ MW campus under construction, pre-operational.

### SBA Communications (277426587368)
- Path: MEDIUM
- Infrastructure_profile: Facilities: Enterprise (50+) -> Facilities: Small (<5)
- Reason: Profile was conflating 39K tower sites with colo facilities. Tower REIT with nascent SBA Edge colo initiative; reset to actual operational DC count.

### Cross Telephone Co (298011233991)
- Path: MEDIUM
- Reason: Undated news cleared.

### Southeast Nebraska Communications (298005835455)
- Path: MEDIUM
- State: Arizona -> **Nebraska** (data quality fix)
- Reason: State field wrong; domain and brief confirm Nebraska. Undated news cleared.

### Inland Fiber Networks (297770284746)
- Path: MEDIUM
- State: California -> **Washington** (data quality fix)
- Reason: State field wrong; Palouse WA operator per brief and domain. Undated news cleared.

### CTP / Chirisa Technology Parks (277406845663)
- Path: FULL
- Sub-segment: Standard - colo -> **Hyperscale Wholesale - colo**
- Tier: tier_3 -> tier_1
- Reason: 850K+ sq ft, 1 GW+ under development, 534K sq ft / 360 MW Richmond VA flagship, CoreWeave anchor tenant. Misclassification corrected per operating notes "AI Signals -> Hyperscale Wholesale for large multi-GW operators".

### ISPN (322843549387)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator -> **Managed Network Services - MSP**
- Tier: tier_3 -> tier_2
- Reason: Not a fiber operator - they are a managed services provider FOR fiber operators (NOC outsourcing for 140+ broadband customers, 1M+ subscribers under management). Acquired by Align Capital Dec 2024.

### IsoFusion (322837059314)
- Path: MEDIUM
- Infrastructure_profile: Facilities: Small (<5) -> Facilities: Mid-Size (5-19)
- Reason: 5 Puget Sound facilities crosses Small boundary (<5). Stale 2024 news cleared.

## Sub-batch C (records 21-30)

### VX Fiber (291518076618)
- Path: MEDIUM
- Reason: Thin brief beef-up; recent_news kept (fresh Fiber Connect 2026 attendance).

### T-Mobile (268250706641)
- Path: MEDIUM
- Reason: provisioning_landscape gap ("Research needed") filled with proper hybrid OSS/BSS description. Recent_news already fresh (Apr 28 fiber JV announcement).

### IREN / Iris Energy (240444244684)
- Path: MEDIUM
- Geographic_focus reformatted to standard "HQ: ... | Scope: ... | states" pattern.
- Brief refreshed with $9.7B Microsoft contract, NVIDIA $2.1B warrant, 140K GPU target.
- Tier: tier_1 (unchanged)

### Switch (303849415381)
- Path: FULL
- Sub-segment: AI Signals - colo -> **Hyperscale Wholesale - colo**
- Tier: tier_1 (unchanged)
- Reason: GW-scale hyperscale colo operator (4 campuses: NV, Tahoe Reno, Grand Rapids MI, Atlanta + Austin TX). Stale "ongoing" news cleared.

### Firmus (239793615562)
- Path: MEDIUM
- Reason: Brief refresh; stale 2025-09 funding news cleared.

### Gcore (253733597934)
- Path: MEDIUM
- Reason: Brief refresh; undated news cleared.

### Together AI (239751073470)
- Path: MEDIUM
- Reason: Brief refresh; stale 2025 funding news cleared.

### Core Scientific (240415542983)
- Path: MEDIUM
- Brief includes corrected status: "Stockholders rejected CoreWeave acquisition October 2025; remains independent."
- Reason: Verified via web - shareholders voted NO on CoreWeave $9B all-stock deal Oct 30, 2025. Core Scientific still independent NASDAQ-listed. Stale 2025-02 news cleared.

### Bitdeer Technologies (240442367678)
- Path: MEDIUM
- Reason: Brief refresh; stale "2025-26" ambiguous-date news cleared.

### Zadara, Inc. (303849415365)
- Path: MEDIUM
- Reason: Brief cleaned - removed internal "Borderline NeoCloud" annotation that was leaking into customer-facing copy. Stale news cleared.

## Sub-batch D (records 31-40)

### Hydra Host (298002235111)
- Path: MEDIUM
- Reason: Brief refresh clarifying aggregator model (40+ DCs managed via Brokkr, not owned). Undated news cleared.

### GMI Cloud (298009434842)
- Path: MEDIUM
- Reason: Brief refresh; stale 2024-10 funding news cleared.

### DigitalOcean (298011233986)
- Path: MEDIUM
- Reason: Brief refresh; stale 2025-03 Flexential news cleared.

### E2E Networks (298009434837)
- Path: MEDIUM
- Reason: Brief refresh; stale 2024-11 IPO news cleared.

### Core42 (303842934518)
- Path: MEDIUM
- Geographic_focus reformatted to standard pattern.
- Reason: Brief refresh; undated news cleared.

### Nebius (240440573644)
- Path: MEDIUM
- Reason: Brief reformatted to remove internal signal codes (NC-A4, NC-A7) leaking into customer-facing copy. Eigen AI $643M acquisition + Meta backlog $50B detail retained.

### VAST Data (301889214188)
- Path: FULL
- Segment: NeoCloud -> **Other** (Partner Target)
- Tier: tier_1 -> tier_5
- Reason: AI data platform vendor selling storage/software to NeoCloud operators (CoreWeave $1.17B agreement). Not an infrastructure operator themselves; co-vendor at our ICP accounts. Other (Partner Target) per Operating Principle #7.

### Yotta / Shakti Cloud (297877949140)
- Path: MEDIUM
- Reason: Brief refresh; undated news cleared.

### NTT DATA (208857135824)
- Path: MEDIUM
- Geographic_focus: "HQ: United States | Global" -> **"HQ: Japan | Scope: Global | Multiple continents"** (data quality fix; NTT DATA is HQ in Tokyo)
- Brief refresh with JINX 400G upgrade.
- Reason: Fresh recent_news from April 2026 kept (JINX 400G). Geographic_focus had wrong HQ country.

### Bulk Infrastructure (300329661172)
- Path: MEDIUM
- Reason: Brief tightened from 5 to 4 sentences. CoreWeave GB200 NVL72 deployment + Stargate Norway context retained. Undated "Nordic AI expansion" news cleared.

## Sub-batch E (records 41-50)

### Vultr (240392240847)
- Path: MEDIUM
- Reason: Brief refresh; undated news cleared.

### Indigo Telecom / Wind (251659209447)
- Path: MEDIUM
- HEAVY marketing bleed strip in BOTH provisioning_landscape AND account_brief ("MaiaEdge offers a strategic fit", "Network Isolation", "modern orchestration dissolves into manual coordination" all removed).
- Geographic_focus reformatted.
- Stale 2025-12 partnership news cleared (>90 days).

### Transworld Associates / TWA (318205926078)
- Path: MEDIUM
- Reason: Empty brief; stub brief added. Pakistan Long Haul / Backbone operator.

### Nextlink Internet (320811765445)
- Path: MEDIUM (no tier write - hs_is_target_account = true)
- Brief tightened from 3 paragraphs to 4 sentences; provisioning_landscape tightened.
- Reason: Overlong narrative. Tier untouched per target_account freeze.

### Easy Fibre (318097753797)
- Path: MEDIUM
- Reason: Empty brief; stub brief added. Sweden Dark Fiber Specialist.

### Seychelles Cable Systems Company / SCCS (319145726687)
- Path: FULL (no tier write - hs_is_target_account = true)
- Segment: Fiber Operator -> **Network Operator(Tier 1 / VNO)**
- Sub-segment: Long Haul / Backbone - Fiber operator -> **Subsea cable operator**
- Tier: tier_1 (frozen, target_account)
- Reason: Pure-play submarine cable landing operator (owns SEAS, co-owns PEACE). Matches 30th sub-segment added 2026-05-14. Borderline SPV but distinct operational footprint (cable ownership + landing stations) qualifies as operator not consortium.

### Etisalat (316526298836)
- Path: MEDIUM
- Reason: Empty brief; brief added. Tier 1 Carrier UAE incumbent (e&), $14.3B revenue.

### Mediafon Technology UAB (316529844935)
- Path: MEDIUM
- Reason: Empty brief; stub brief added. Lithuanian Regional CLEC.

### Peerless Network (296851879631)
- Path: FULL
- Segment: Fiber Operator -> **MSP/Aggregator**
- Sub-segment: Regional CLEC - Fiber operator -> **Telecom Aggregator - MSP**
- Reason: VoIP/SIP wholesale aggregator owned by Infobip (2022 acquisition). Nationwide IP voice network serves 49 states + 3 countries. Not a fiber operator - bulk voice/SIP aggregator with single 12.6K sq ft DC. Matches operating-notes VoIP/SIP-aggregator-under-Fiber-Op flip pattern.

### 4U Telecom (297777475288)
- Path: FULL
- Segment: Fiber Operator -> **Flagged for deletion**
- Confidence: low_5069 -> high_90
- Reason: Small UK telecom services reseller in Lancashire; leases capacity from carriers, no owned fiber/POPs, no NaaS, no self-service. Reseller/services model, not an operator. Aggressive Flag per Operating Principle #7.

---

## Patterns observed this batch (carry forward)

- **Marketing bleed continued at scale.** 4 records this batch had explicit "MaiaEdge offers", "Network Isolation", "modern orchestration dissolves into manual coordination" language in customer-facing fields (Indigo Telecom heaviest hit). All stripped.
- **AI Signals -> Hyperscale Wholesale flip continues** for multi-GW operators (Switch, CTP). Pattern matches batch 12 notes.
- **Standard -> Greenfield flip continues** for pre-operational AI/colo developers (Crystal Peaks, BluSky AI, Form8tion - 3 this batch, biggest greenfield migration yet).
- **VoIP/SIP-only -> MSP/Aggregator flip** active this batch (Peerless Network - large 49-state VoIP wholesaler, ISPN - NOC services aggregator).
- **Subsea cable operator sub-segment first use** in sweep (SCCS - landing-station SPV with cable ownership). 30th sub-segment added 2026-05-14 now active.
- **Storage/data-platform vendors as Other (Partner Target)** - VAST Data flipped from NeoCloud to Other. Pattern likely to repeat (Pure Storage, Hammerspace, WEKA, similar candidates in pool).
- **State data quality fixes** - 2 misaligned states this batch (SE Nebraska Communications: AZ->NE, Inland Fiber: CA->WA). Apollo backfill drift, defer territory recompute to R6.
- **NTT DATA HQ country fix** - geographic_focus said "United States" but NTT DATA is Tokyo-headquartered ($22B Japanese IT giant). Apollo state/country fields were actually correct (Tokyo/Japan); geographic_focus was the drift.
- **Tower REIT infrastructure_profile bleed** - SBA Communications had 39K cell towers conflated as 50+ colo facilities. Corrected to Small (<5) edge-DC count. Watch for American Tower, Crown Castle similar errors.
- **Empty briefs on records created during Phase 3 migration (April 14-21)** - Transworld, Easy Fibre, Mediafon, Etisalat all had no account_brief. Stub briefs added; will fill on next full enrichment cycle.
- **D7 escalation queue: 0 new records** (HOLD policy = NONE).

## Apollo budget tracker

- This batch: 0 credits
- APOLLO_ENFORCEMENT = "disabled" - sweep is outside weekly cap, no JSON update.

## Errors / failures

None. All 50 writes succeeded.
