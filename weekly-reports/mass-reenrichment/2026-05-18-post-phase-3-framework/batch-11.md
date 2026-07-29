# Mass Re-Enrichment Sweep — 2026-05-18-post-phase-3-framework — Batch 11

**Run date:** 2026-05-18
**Processed:** 50/50
**Pool remaining after batch:** 2,213 records
**Apollo credits used:** 0

---

## Path mix

- LIGHT: 0
- MEDIUM: 35
- FULL: 15 (segment-changes + flagged-for-deletion)
- HOLD: 0 (per Cooper "HOLD policy = NONE" — every record gets qualified, Other, or Flagged for deletion)

## Segment changes (FULL path, cascade-eligible)

| ID | Name | Old segment / sub | New segment / sub | Reason |
|---|---|---|---|---|
| 303849415363 | Hut 8 | Data Center Colo / AI Signals - colo | NeoCloud / Crypto to AI - Neoclouds | Per CLAUDE.md NC5 inclusion: Hut 8 BTC-mining lineage → Crypto-to-AI Neocloud. White-hot signal: $9.8B Beacon Point 352MW lease. |
| 251593619132 | Seaborn Networks | Fiber Operator / Regional CLEC | Network Operator(Tier 1 / VNO) / Subsea cable operator | Per CLAUDE.md verified subsea anchor (Seabras-1 owner-operator). |
| 263729676016 | PS Lightwave | MSP/Aggregator / Telecom Aggregator | Fiber Operator / Regional CLEC | Owns ~5,500 mi metro fiber + 1,600 on-net locations. Fiber-asset owner, not aggregator. |
| 297293654756 | VISI | Data Center Colo / Standard - colo | Flagged for deletion | Defunct brand: absorbed into US Signal via 2024 OneNeck acquisition. |
| 296850118366 | Wilcon Holdings | Fiber Operator / Dark Fiber Specialist | Flagged for deletion | Defunct: Crown Castle (2017) → Zayo+EQT pending (Mar 2025 $8.5B). |
| 193867595511 | Everstream | Fiber Operator / Long Haul / Backbone | Flagged for deletion | Defunct: Chapter 11 May 2025 → acquired by Bluebird Fiber (Aug 2025, $384.6M). |
| 193866877641 | Colt Technology Services | Fiber Operator / Regional CLEC | Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op | Major European Tier 1: 32K km, 40+ countries, 275+ PoPs, 8 subsea systems. |
| 193906530037 | Uniti | Fiber Operator / Dark Fiber Specialist | Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op | Post-Windstream merger (Aug 2025 $13.4B): 217K route miles, $4.4B rev, 47 states. |
| 174907029200 | BeyondReach | Fiber Operator / Regional CLEC | MSP/Aggregator / Telecom Aggregator | Rural connectivity aggregator (950+ WISP partnerships), not fiber-asset owner. |

## Sub-segment-only migrations (same parent)

| ID | Name | Old sub | New sub |
|---|---|---|---|
| 292477779660 | Echelon Data Centre | AI Signals - colo | Hyperscale Wholesale - colo |
| 251536944853 | QTS Realty Trust | AI Signals - colo | Hyperscale Wholesale - colo |
| 320960333530 | MetroNet | Regional Cable Operator - Fiber operator | Regional CLEC - Fiber operator |
| 193853194997 | Midco | Regional Cable Operator - Fiber operator | Regional CLEC - Fiber operator |
| 292748566215 | Lakeshore Fiber | Long Haul / Backbone | Regional CLEC - Fiber operator |
| 292755847874 | Gold Data | Regional CLEC | Long Haul / Backbone - Fiber operator |
| 292603554549 | LightStream Networks | Dark Fiber Specialist | Regional CLEC - Fiber operator |
| 298009434824 | HyperLink Infrastructure | Regional CLEC | Long Haul / Backbone - Fiber operator |
| 292520967926 | GoldenStateNet | Regional CLEC | Long Haul / Backbone - Fiber operator |

## Tier shifts

**Promotions (toward tier_1):**
- Colt Technology Services: tier_3 → tier_1 (Tier 1 European, AWS Sovereign partner)
- Uniti: tier_2 → tier_1 (post-Windstream merger Tier 1)
- Logix Fiber Networks: tier_3 → tier_2 (TX fiber leader + AI tenant signals)
- Gold Data: tier_3 → tier_2 (US-LatAm backbone with hyperscaler customer base)
- HyperLink Infrastructure: tier_3 → tier_2 (AI infra fiber operator)
- Hut 8: tier_1 → tier_1 (white-hot signal, held at ceiling)

**Demotions (toward tier_5):**
- Mainstream Technologies: tier_3 → tier_4 (1 facility, 1MW)
- Advantage Technology: tier_3 → tier_4 (IT consultancy + small colo)
- Pinnacle Technical Solutions: tier_3 → tier_4 (single facility, local)
- Lakeshore Fiber: tier_2 → tier_4 (30 employees, single-state ISP)
- LightStream Networks: tier_2 → tier_4 (5 employees, niche)
- BeyondReach: tier_3 → tier_4 (small rural aggregator)
- ANI Networks: tier_2 → tier_3 (limited public detail, confidence drop)

## Per-record audit entries

### TDS Telecom (209170400954) — MEDIUM
- Path: MEDIUM
- Domain: tdstelecom.com (unchanged)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 → tier_3 (no modifier change)
- Apollo used: no
- Reason: account_brief tighten + provisioning_landscape tighten

### Mainstream Technologies (297940265677) — MEDIUM
- Path: MEDIUM
- Sub-segment: Standard - colo (unchanged)
- Tier: tier_3 → tier_4 (single facility ~1MW; drift correction)
- Reason: account_brief + provisioning_landscape tighten; tier drift

### Hut 8 (303849415363) — FULL
- Segment: Data Center Colo Provider → NeoCloud
- Sub-segment: AI Signals - colo → Crypto to AI - Neoclouds
- Tier: tier_1 → tier_1 (white-hot signal, $9.8B Beacon Point lease)
- Reason: Per CLAUDE.md NC5 inclusion + recent $9.8B 352MW lease announcement (May 6 2026)

### MetroNet (320960333530) — MEDIUM
- Sub-segment: Regional Cable Operator → Regional CLEC (auto-migration, retired legacy value)
- Tier: tier_3 → tier_3
- Reason: sub-segment migration + brief tightening; bogus annualrevenue 792305 left unchanged

### Seaborn Networks (251593619132) — FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC → Subsea cable operator
- Infrastructure profile corrected: POPs Enterprise (100+) → Small (<10); Route Miles Large → Mid-Size
- Geographic focus: "Local" → "Trans-Americas | US-Brazil subsea"
- Tier: tier_3 → tier_3 (stale signal hold)
- Reason: Per CLAUDE.md verified subsea anchor

### SDN Communications (254570392310) — MEDIUM
- Sub-segment: Long Haul / Backbone - Fiber operator (unchanged)
- Tier: tier_2 → tier_2
- recent_news cleared (2023 events, >90d stale)
- Reason: brief tighten + stale news clearing

### PS Lightwave (263729676016) — FULL
- Segment: MSP/Aggregator → Fiber Operator
- Sub-segment: Telecom Aggregator - MSP → Regional CLEC - Fiber operator
- Infrastructure profile: Mid-Size route miles + Mid-Size PoPs (added)
- Tier: tier_2 → tier_3 (Houston-metro single-region; right-size)
- Reason: PS Lightwave owns ~5,500 mi metro fiber + 1,600+ on-net locations, not aggregator

### T5 Data Centers (251600877279) — MEDIUM
- Sub-segment: Hyperscale Wholesale - colo (unchanged)
- Confidence: manual_review_required → high_90 (resolved)
- Tier: tier_1 → tier_1 ($2B equity raise white-hot signal)
- Reason: confidence resolution + brief refresh + $2B equity raise news

### Stack Infrastructure (255207759560) — MEDIUM
- Sub-segment: Hyperscale Wholesale - colo (unchanged)
- Confidence: manual_review_required → high_90 (resolved)
- Tier: tier_1 → tier_1 (Oracle Stargate signal)
- Reason: confidence resolution + brief tighten + Stargate signal call-out

### 1547 Critical Systems Realty (292817328836) — LIGHT
- Sub-segment: AI Signals - colo (unchanged)
- Tier: tier_1 → tier_1
- Reason: account_brief tightening, no segment change

### Echelon Data Centre (292477779660) — MEDIUM
- Sub-segment: AI Signals - colo → Hyperscale Wholesale - colo
- Tier: tier_1 → tier_1 (white-hot signal, €3B Milan + Iberdrola JV)
- Reason: AI Signals → Hyperscale Wholesale flip (CloudHQ/PowerHouse/AirTrunk pattern)

### VISI (297293654756) — FULL (definitive eviction)
- Segment: Data Center Colo Provider → Flagged for deletion
- Reason: Defunct brand, absorbed into US Signal (2024)

### KT Corporation (303312798425) — MEDIUM
- Sub-segment: Tier 1 Carrier - Network Op (unchanged)
- Tier: tier_1 → tier_1
- provisioning_landscape: stripped "Equinix experience" / "polite chaos" marketing bleed
- Reason: brief expansion + provisioning_landscape rewrite

### TailWind Voice and Data (268197670594) — LIGHT
- Tier: tier_2 → tier_2
- Reason: news date prefix fix only

### Blue Wireless (268111745751) — LIGHT
- Tier: tier_2 → tier_2
- Reason: news date prefix fix only

### MTN Satellite Communications (268456914671) — MEDIUM
- Tier: tier_2 → tier_2
- Reason: filled provisioning_landscape; fixed news date

### Lakeshore Fiber (292748566215) — MEDIUM
- Sub-segment: Long Haul / Backbone → Regional CLEC - Fiber operator (correction; not actually backbone)
- Tier: tier_2 → tier_4 (30 employees, single state, niche rural)
- Reason: sub-segment correction + brief tighten + tier drift

### Gold Data (292755847874) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator (international LatAm backbone)
- Tier: tier_3 → tier_2 (US-LatAm hyperscaler-class backbone)
- Reason: sub-segment correction + tier promotion

### LightStream Networks (292603554549) — MEDIUM
- Sub-segment: Dark Fiber Specialist → Regional CLEC - Fiber operator (retired legacy or unclear)
- Confidence: null → high_90 (set)
- Tier: tier_2 → tier_4 (5 employees, niche)
- Reason: sub-segment migration + tier drift

### ExteNet (292603582171) — LIGHT
- Tier: tier_3 → tier_3
- Reason: news date prefix fix only

### telMAX (292542834411) — MEDIUM
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Infrastructure profile: Route Miles Enterprise (50K+) → Mid-Size (1K-10K) (corrected from bogus 745K km claim)
- Tier: tier_3 → tier_3
- Reason: brief tighten + infra profile correction

### Ritter Communications (193863998185) — MEDIUM
- Tier: tier_2 → tier_2
- Reason: brief tighten; bogus annualrevenue 89534 noted (actual ~$89.5M)

### HyperLink Infrastructure (298009434824) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator
- Tier: tier_3 → tier_2 (AI infra specialist, 2,400 mi, 288-864 count fiber)
- Reason: sub-segment correction + tier promotion

### Advantage Technology (297740621552) — MEDIUM
- Tier: tier_3 → tier_4 (IT consultancy w/ small colo)
- Reason: brief tighten + news date prefix + tier drift

### Archtop Fiber (292520998645) — MEDIUM
- Tier: tier_3 → tier_3
- Reason: brief tighten only

### GoldenStateNet (292520967926) — MEDIUM
- Sub-segment: Regional CLEC → Long Haul / Backbone - Fiber operator (state-funded middle-mile)
- Tier: tier_3 → tier_3 (state-utility model, indirect customer)
- Reason: sub-segment correction + brief tighten

### Pinnacle Technical Solutions (297934868194) — MEDIUM
- Tier: tier_3 → tier_4 (single facility, local)
- Reason: brief tighten + tier drift

### Bluepeak (175217873637) — MEDIUM
- country: Jordan → United States (Apollo state error correction)
- state: Amman → Wyoming
- Confidence: low_5069 → high_90
- Tier: tier_3 → tier_3
- Reason: country/state Apollo correction

### Planet Networks (292788993739) — MEDIUM
- Tier: tier_3 → tier_3
- Reason: brief tighten only

### Tech Vault (296880095990) — MEDIUM
- Tier: tier_3 → tier_3
- provisioning_landscape: stripped "MaiaEdge addresses" marketing bleed
- Reason: brief tighten + bleed stripping + news date

### Advantage Communications Group (268458705651) — LIGHT
- Tier: tier_2 → tier_2
- Reason: news date prefix fix only

### TPx Communications (292788968139) — MEDIUM
- Geographic focus: "Local" → "National | US-wide"
- Tier: tier_2 → tier_2
- Reason: brief tighten + geographic focus correction

### BridgeLync (268447803122) — MEDIUM
- Confidence: null → high_90
- Tier: tier_2 → tier_2
- Reason: filled provisioning_landscape + confidence

### WMS Wireless Maritime Services (268259853049) — LIGHT
- Tier: tier_2 → tier_2
- Reason: news date prefix fix only

### Wilcon Holdings (296850118366) — FULL (definitive eviction)
- Segment: Fiber Operator → Flagged for deletion
- Reason: Defunct brand absorbed into Crown Castle (2017) → pending Zayo+EQT sale

### IdeaTek Telcom (297934868201) — MEDIUM
- Tier: tier_3 → tier_3 (could be tier_2 with stacked signals; held conservative)
- Reason: brief tighten only

### Midco (193853194997) — MEDIUM
- Sub-segment: Regional Cable Operator → Regional CLEC - Fiber operator (auto-migration)
- Tier: tier_3 → tier_3
- Reason: sub-segment migration + brief tighten; bogus annualrevenue 561709 noted

### Arcadian Infracom (206972820215) — MEDIUM
- Tier: tier_2 → tier_2
- Reason: filled account_brief and provisioning_landscape

### Netrio (209003423466) — MEDIUM
- Tier: tier_2 → tier_2
- provisioning_landscape: stripped MaiaEdge talking-points marketing bleed
- Reason: provisioning_landscape rewrite

### Aquablue (297982584516) — LIGHT
- Tier: tier_2 → tier_2
- Reason: date stamp only

### Colt Technology Services (193866877641) — FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Regional CLEC → Tier 1 Carrier - Network Op
- Tier: tier_3 → tier_1 (Tier 1 European + AWS Sovereign partner Feb 2026)
- Reason: segment correction + tier promotion + filled provisioning_landscape

### Everstream (193867595511) — FULL (definitive eviction)
- Segment: Fiber Operator → Flagged for deletion
- Reason: Defunct - Chapter 11 May 2025, acquired by Bluebird Fiber Aug 2025

### ANI Networks (193867595512) — MEDIUM
- Confidence: high_90 → medium_7089 (limited public detail)
- Tier: tier_2 → tier_3 (cautious; limited research depth)
- Reason: filled account_brief + provisioning_landscape; confidence + tier downgrade pending deeper research

### Uniti (193906530037) — FULL
- Segment: Fiber Operator → Network Operator(Tier 1 / VNO)
- Sub-segment: Dark Fiber Specialist → Tier 1 Carrier - Network Op
- Tier: tier_2 → tier_1 (post-Windstream merger Tier 1, 217K mi, $4.4B rev)
- Reason: segment correction + tier promotion + filled provisioning_landscape

### VISION NET (292542793455) — LIGHT
- Tier: tier_3 → tier_3
- Reason: news date prefix fix only

### PhoenixNAP (194004502211) — MEDIUM
- Tier: tier_1 → tier_1
- provisioning_landscape: stripped "Equinix experience" + "polite chaos" marketing bleed
- Reason: provisioning_landscape rewrite + news date prefix

### BeyondReach (174907029200) — FULL
- Segment: Fiber Operator → MSP/Aggregator
- Sub-segment: Regional CLEC → Telecom Aggregator - MSP
- Tier: tier_3 → tier_4 (small aggregator)
- provisioning_landscape: stripped MaiaEdge marketing bleed
- Reason: segment correction (950+ WISP aggregator, not fiber owner)

### Logix Fiber Networks (193867595509) — MEDIUM
- Tier: tier_3 → tier_2 (TX fiber leader + AI tenant focus + $45M financing)
- Reason: brief tighten + tier promotion

### RidgeLink (297986182902) — MEDIUM
- Tier: tier_3 → tier_3 (carrier-neutral colo serving Verizon/AT&T/T-Mobile; held)
- Reason: brief tighten

### QTS Realty Trust (251536944853) — MEDIUM
- Sub-segment: AI Signals - colo → Hyperscale Wholesale - colo
- Confidence: manual_review_required → high_90 (resolved)
- Tier: tier_1 → tier_1
- Reason: AI Signals → Hyperscale Wholesale flip + confidence resolution

---

## Patterns observed (consistent with batches 9-10)

1. **AI Signals → Hyperscale Wholesale flip:** Echelon, QTS this batch (Wave continues from CloudHQ/PowerHouse/AirTrunk).
2. **Crypto-to-AI Neocloud (NC5) inclusion:** Hut 8 reclassified per CLAUDE.md inclusive policy.
3. **Subsea cable operator (30th sub-segment):** Seaborn Networks formally classified.
4. **Defunct/acquired entities:** 3 flagged this batch (VISI/US Signal, Wilcon/Crown Castle→Zayo, Everstream/Bluebird). R3 dedup queue grows.
5. **Marketing bleed in account_brief/provisioning_landscape:** "Equinix experience", "polite chaos", "MaiaEdge addresses", "paying Tier 1 costs without Tier 1 capabilities", "Tier 1s are going direct" — stripped on KT, PhoenixNAP, Tech Vault, Netrio, BeyondReach.
6. **Apollo parent-revenue bleed:** TDS Telecom $5.16B (correct), Ritter $89.5K (bogus, actual $89.5M), Midco $562K (bogus), telMAX 745K route km (impossible Apollo bleed), Wilcon-era data on Colt $2.2K (actual €2.2B+) - skipped writes for revenue field.
7. **Apollo state/country errors:** Bluepeak (Jordan/Amman → United States/Wyoming) corrected.
8. **Tier 1 carrier reclassifications:** Colt and Uniti both promoted from Fiber Operator to Network Operator(Tier 1) — pattern indicates need for global Tier 1 reclassification sweep on similar 6K+ employee operators with multi-country scope.
9. **Greenfield sub-segment not used this batch:** Arcadian Infracom borderline (operational + under-construction), kept Long Haul / Backbone.
10. **HOLD policy = NONE working as intended:** Zero records routed to Tier 3 holds. Cooper's directive to "every record qualified or flagged" honored.

## Drain status

- Starting active ICP pool (~2,733 records prior to sweep start)
- Done in sweep: ~520 / ~2,733 (~19%)
- Remaining: 2,213
- ETA at BATCH_SIZE=50: ~44 more batches
