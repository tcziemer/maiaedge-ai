# File 06 — Sub-Segment Qualification Reference (Consolidated)

**Version:** v2, 2026-05-14 (revised same day per Cooper feedback)
**Status:** Primary source material for Phase 3 (Claude Code repo update). Supersedes `05 - Sub-segment definitions for cheatsheets.md` for classification logic; file 05 remains the canonical anchor-list document and persona detail reference. Updates and corrections from Phase B+C research + Cooper feedback are integrated below.
**Live HubSpot state:** **30 active** `company_sub_segment` enum values verified via MCP 2026-05-14 against portal 242063281 (na2). Includes `Subsea cable operator` (Cooper-added 2026-05-14).

**Cooper feedback resolutions (2026-05-14, applied throughout):**
- Subsea cable operator: added as 30th sub-segment under Network Operator parent
- Crypto to AI - Neoclouds: REDEFINED as inclusive of operator AND landlord models (former bitcoin miners pivoting to AI infrastructure, regardless of business model)
- Master Agent default policy: REVERSED — no default manual_review; classify best-fit with calibrated confidence
- NaaS Platform Operators: classify as `Other` (competitive reference) or `Flagged for deletion` (no value)
- Greenfield: REAL sub-segment, NOT deprecated — for actively-being-built Colo + NeoCloud
- Multi-marker classification: lean on `infrastructure_profile` (multi-select bands) over revenue
- **8 enriched fields in enrichment scope** (`account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`) — D5 protocols read from these, not HubSpot `description`/`industry` defaults
- **Conciseness rule (Cooper 2026-05-14):** all narrative fields capped at **2-4 sentences each** for scalability at thousands-of-records volume
- **maiaedge_value_proposition NOT in enrichment scope** — Cooper 2026-05-14: "we figure this out when we are doing outreach to them anyways." Outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) populate this field on-demand at outreach time using segment-specific messaging
- **Workflow ordering:** Bot populates 7 enriched fields during research (Stage 1b), THEN classifies customer_segment + sub-segment + tier as a verdict on the completed profile (Stages 2-4), THEN writes HubSpot at Stage 5. No separate value_proposition generation stage.
- Edge case resolution: new D7 weekly routine spec (`cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md`)
- No-default-manual-review principle: classification routes to a sub-segment (best-fit + tiebreaker) OR Flagged for deletion; manual_review only for genuine multi-classification ambiguity

## 1. Executive summary

This document is the authoritative source for sub-segment classification logic across all 6 MaiaEdge ICPs (Network Operator, Fiber Operator, Data Center Colo Provider, NeoCloud, MSP/Aggregator, Enterprise) post-Phase-2 + Phase-1.6 migration. It encodes:

- The verified 29-value sub-segment enum (case-sensitive internal strings)
- Global disqualifier rules that run BEFORE any sub-segment routing
- Wholesale-arm-vs-parent policy resolving the 263-record Phase 2.3 corrective dilemma
- Decision-tree flowcharts (≤7 deep) for all 6 ICPs
- Per-sub-segment classification headers (definitions + markers + anchors) — full 12-section deep dives in `context/account-tiering/icp-deep-dives/B-and-C-{icp}.md`
- Contact persona mapping (29 × 4 personas)
- Industry taxonomy alignment (FCC BDC, PeeringDB, Synergy Research, Omdia TSD, NAICS, etc.)
- Per-routine at-scale readiness assessment with specific Phase 3 deltas

**Gaps closed by Phase B+C research:** 14 anchor corrections to Network Op, ~15 to Fiber, ~10 to Colo, ~12 to NeoCloud, anchor + classification policy for Master Agent + IT integrators, 60 verified Enterprise anchors with hard-exclusion list. **Gaps opened for Cooper decision:** Subsea cable operator bucket policy, IREN/Core Scientific classification (currently AI Signals colo not Crypto-to-AI), GPU pricing trend refresh (recently reversed — file 05 cites stale "still falling"), 6-7 Enterprise edge cases (CVS, UnitedHealth, McKesson, etc.).

**Phase 3 will consume:** this file + working files A, B-and-C-{icp}.md × 6, D1, D2, D3, D4, E, and the existing context/segments/ cheatsheets. File 07 (companion) lists specific prompt deltas.

---

## 2. Live HubSpot enum state (verified 2026-05-14)

Full table with case-sensitive internal strings, display labels, and naming inconsistencies in `working/00-hubspot-enum-verification.md`. Headline:

| Segment | Sub-segments | Count |
|---|---|---:|
| Network Operator(Tier 1 / VNO) | Tier 1 Carrier, Pure Wholesale Carrier, Cable MSO Enterprise Division, International Backbone Specialist, **Subsea cable operator (new 2026-05-14)** | 5 |
| Fiber Operator | Regional CLEC, Long Haul / Backbone, Dark Fiber Specialist, Tier 2 National Wholesale, Regional Cable Operator, Municipal / Cooperative | 6 |
| Data Center Colo Provider | Standard, AI Signals, Modular, Hyperscale Wholesale | 4 |
| NeoCloud | Large Scale GPU, Tier 1 Inference, AI Infrastructure providers, Sovereign AI Clouds, Crypto to AI | 5 |
| MSP/Aggregator | Telecom Aggregator, Managed Network Services, TSD Technology Services Distributor, Master Agent, Cloud + Telecom Hybrid MSP | 5 |
| Enterprise-CustomerSegment | Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services | 4 |
| Cross-segment | **Greenfield (REAL sub-segment per Cooper 2026-05-14 — pairs with Colo or NeoCloud customer_segment parent for in-build companies)** | 1 |
| **Total active** | | **30** |

**Case-sensitive quirks to encode in `import-processor`:**
- `Dark Fiber Specialist - Fiber Operator` — capital "O" in Operator
- `AI Infrastructure providers - Neocloud` — lowercase "p"
- `Crypto to AI - Neoclouds` — trailing "s"
- `Network Operator(Tier 1 / VNO)` — no space before open paren
- `Managed Network Services - MSP` — "- MSP" suffix (post-Phase 1.7c.1; legacy "- Network Operator" archived)
- `Subsea cable operator` — lowercase "c" and "o" + no "- Network Op" suffix (sits under Network Op parent without the suffix convention)

---

> **Mandatory `flagged_for_deletion_reason` companion write (applies to EVERY `Flagged for deletion` outcome in this document).** Wherever a protocol, tiebreaker, or disqualifier in this file routes a record to `customer_segment = "Flagged for deletion"`, the same HubSpot update MUST also set `flagged_for_deletion_reason`, leading with ONE of the 7 canonical reason codes + a colon + one concrete evidence sentence (no em dashes; the scannable code lives here, the 2-4 sentence prose rationale stays in `account_brief`). The 7 codes: `Dead domain`, `Hard junk / non-business`, `D1 disqualified (no reference value)`, `No ICP fit`, `Duplicate (merged)`, `Defunct / out of business`, `Stalled greenfield`. On any path that moves a record OFF "Flagged for deletion" back into an active segment, clear `flagged_for_deletion_reason` to empty in the same write (clear-on-exit). Full spec: `context/hubspot/property-schema.md` §2.1; operational reason-code mapping in `context/account-tiering/enrichment-protocols.md` §1.

## 3. Global disqualifier rules (from D1)

**Apply BEFORE any sub-segment routing.** If a match, set `customer_segment = "Other"` (or `"Flagged for deletion"` for defunct/retired-brand cases) and skip sub-segment classification. Full details in `context/account-tiering/d1-global-disqualifiers.md`.

Top disqualifier classes:

1. **Hyperscalers** — Amazon/AWS, Microsoft/Azure, Google/Cloud, Meta, Oracle Cloud, Tencent, Alibaba, Yandex, Baidu, IBM Cloud, NVIDIA Lepton/owned-cloud. Exception: DigitalOcean retained in NeoCloud `AI Infrastructure providers`.
2. **Equipment vendors and silicon** — Cisco, Juniper, Nokia, Ericsson, Huawei, ZTE, Arista, Calix, Adtran, Ribbon, Mavenir, Ciena, Infinera, Intel, AMD, NVIDIA (chip side), Broadcom, Marvell, Qualcomm, MediaTek.
3. **OTT and pure content platforms** — Netflix, Hulu, Roku, Disney+, Paramount+, Max; Meta apps, TikTok/ByteDance, Reddit, Discord, Pinterest, Snap, X; Valve, Epic Games, Sony PSN, Xbox Live; Spotify, Apple Music, Tidal.
4. **Submarine cable consortia (pure)** — FLAG, SEA-ME-WE 4/5/6, ACE, EIG; pure-play subsea operators without terrestrial backbone (Aqua Comms pre-EXA, Seaborn, BW Digital, hyperscaler subsea SPVs) — **Cooper decision pending** on new sub-segment vs Other.
5. **Pure software/SaaS without network ops** — pure cloud MSPs (post-acquisition Mission, SADA), IoT/eSIM platforms (Aeris, EMnify, Wireless Logic, KORE, Soracom), pure observability SaaS, pure security platforms.
6. **Logistics / shipping** — GAC (Gulf Agency Co), Maersk, DHL, FedEx parent, 3PLs without multi-DC corporate IT.
7. **Government / military / embassy** — `.gov`, `.mil`, state/local, embassy domains, foreign government national-cloud entities. FedRAMP-gated; out of scope until authorization.
8. **Academic / research / non-profit** — Internet2, JANET, GÉANT, ESnet, NORDUnet, public broadcasting.
9. **Defunct / inactive** — active bankruptcy with no operations, retired brand with no successor entity, expired domain 90+ days.
10. **Misclassified data-center adjacencies** — power utility (NextEra, Duke, Constellation), cooling/HVAC (Vertiv, Schneider, Stulz), pure-real-estate parent leasing to colos (Prologis, Mapletree), pure crypto exchanges without GPU pivot (Coinbase, Marathon Digital pre-pivot).

**Special case:** If a disqualifier would evict a record that is `type = "Customer"` or has any associated deal past `closedwon`, halt and flag for Cooper review. Customer relationship overrides cleanup.

---

## 4. Wholesale arm vs parent entity policy (from D2)

Full details in `context/account-tiering/d2-wholesale-arm-policy.md`. Headline:

**Default policy:** One HubSpot record per legal entity that has its own DUNS / tax ID. Wholesale activity within a single parent entity is captured via `network_op_track` field + notes, NOT a separate record.

**Two-record cases (when wholesale arm has separate DUNS):**
- Parent → typically `Tier 1 Carrier - Network Op`
- Wholesale arm → `Pure Wholesale Carrier - Network Op` (domestic wholesale) OR `International Backbone Specialist - Network Op` (international wholesale)
- Cross-link via HubSpot association

**Tier assignment:** independent per record per framework. `hs_is_target_account` independent per record.

**Canonical entity list** (excerpted; full in D2 file):

| Parent | Treatment | Wholesale-arm sub-segment |
|---|---|---|
| Orange S.A. | Single record | n/a (wholesale via network_op_track) |
| Orange Wholesale International | Separate record if found | International Backbone Specialist - Network Op |
| NTT Group + NTT Global Data Centers | Separate (already 2 records per Phase 2 audit) | NTT Global Data Centers → `AI Signals - colo` |
| BT + BT Wholesale | Separate if found | BT Wholesale → Pure Wholesale Carrier - Network Op |
| Telstra + Telstra International | Separate | Telstra International → International Backbone Specialist - Network Op |
| Telecom Italia + Sparkle | Separate (pending Italian state sale H1 2026) | Sparkle → International Backbone Specialist - Network Op |
| Bharti Airtel + Bharti Airtel International | Separate | International → International Backbone Specialist - Network Op |
| Tata Communications | Single (parent IS wholesale) | `International Backbone Specialist - Network Op` (manual_review_required per file 05) |
| Verizon + Verizon Enterprise | **Duplicate pair** (Phase 2 audit) — recommend dedup | Both → Tier 1 Carrier - Network Op |
| Vodafone Group + Vodafone UK | Separate (legitimate two-record) | Both → Tier 1 Carrier - Network Op |
| China Telecom + China Telecom Global | Separate | Global → International Backbone Specialist - Network Op |
| Comcast + Comcast Business | Separate (already 2 records) | Both → Cable MSO Enterprise Division - Network Op |
| Spectrum + Spectrum Enterprise | Separate | Both → Cable MSO Enterprise Division - Network Op |
| Lumen Technologies | Single | `Tier 1 Carrier - Network Op` (post-divestitures, drifting toward Pure Wholesale — flag quarterly) |

---

## 5. Per-ICP disambiguation flowcharts (from D3)

Full details + edge cases in `context/account-tiering/d3-disambiguation-flowcharts.md`. All 6 flowcharts ≤7 decisions deep. Each runs AFTER D1 disqualifier check and D2 wholesale-arm resolution.

### 5.1 Network Operator flowchart (7 decisions)

```
Pre-gate: Revenue ≥$200M AND at least one of {national licensed carrier, IP transit, subsea cable IRU}? NO → Fiber flow.
1. Meaningful retail (consumer wireless/wireline/TV)?  YES→Decision 2; NO→Decision 5
2. Cable/HFC legacy?  YES→Decision 3; NO→Decision 4
3. National cable + B2B ≥$1.5B?  YES → Cable MSO Enterprise Division; NO → Fiber flow (Regional Cable Operator)
4. Multinational reach ≥10 countries + parent rev ≥$15B?  YES → Tier 1 Carrier; NO → manual_review_required
5. Wholesale activity primarily international?  YES→Decision 6; NO→Decision 7
6. Subsea ownership OR ≥3 cable IRU positions?  YES → International Backbone Specialist; NO → manual_review_required
7. Pure-wholesale + Tier 1 IP transit + rev $200M-$5B?  YES → Pure Wholesale Carrier; NO → manual_review_required
```

### 5.2 Fiber Operator flowchart (7 decisions, with sub-branches)

```
Pre-gate: Owns/operates fiber + rev ≥$30M?
1. Residential cable/HFC legacy?  YES→Decision 2; NO→Decision 3
2. National + B2B ≥$1.5B?  YES → Cable MSO Network Op (re-route); NO → Regional Cable Operator
3. Wholesale-only?  YES→Decision 4; NO→Decision 6
4. International?  YES → International Backbone Specialist Network Op; NO→Decision 5
5. IP transit primary?  YES → Pure Wholesale Carrier Network Op; NO → Decision 5a-5c
   5a. National US/EU + 20K+ route miles + wholesale-only $300M-$5B?  YES → Tier 2 National Wholesale
   5b. Long-haul dark fiber primary?  YES → Long Haul / Backbone
   5c. Metro/specific dark fiber?  YES → Dark Fiber Specialist (capital O)
6. Municipal utility/co-op/community-owned?  YES → Municipal / Cooperative
7. CLEC or fiber-overbuilder $30M-$1B?  YES → Regional CLEC (default for ambiguous mid-size); NO → manual_review_required
```

### 5.3 Colocation flowchart (6 decisions)

```
Pre-gate: Operates physical DCs + sells space/power/cooling?
1a. Former crypto miner pivoted to AI as LANDLORD (no own GPU compute)?  YES → AI Signals - colo (landlord model — catches IREN, Core Scientific)
1. Confirmed GPU tenants + liquid cooling + 30kW+ racks?  YES→Decision 2; NO→Decision 4
2. Distributed modular operator (containerized pods, growth = sites not campus)?  YES → Modular - colo
3. ≥60% hyperscaler cloud capacity, 10MW+ wholesale terms?  YES→Decision 5; NO → AI Signals - colo
4. Per-MW wholesale (10MW+, 5-15yr, anchor tenant)?  YES → Hyperscale Wholesale - colo; NO→Decision 6
5. (Dec-3 YES) Hyperscaler vs GPU tenant revenue split?  HS>GPU → Hyperscale Wholesale; GPU>HS → AI Signals; 60-40 → manual_review_required
6. Standard retail/multi-tenant (per-rack, MMR, high XC volume)?  YES → Standard - colo; NO → manual_review_required
```

### 5.4 NeoCloud flowchart (6 decisions)

```
Pre-gate: Sells GPU compute as a service (NOT space)?
1. Built for data sovereignty (GDPR/DPDP/national AI/GAIA-X)?  YES→Decision 2; NO→Decision 3
2. Triple-signal (explicit sovereign marketing + regulator compliance + ≥1 sovereign-mandated customer ref)?  ≥2/3 → Sovereign AI Clouds; 0-1 → Decision 3
3. Former crypto miner running OWN GPU compute (not just landlord)?  YES → Crypto to AI - Neoclouds (trailing "s"); NO→Decision 4
4. Bare-metal GPU clusters for LLM training (20+ facilities OR hyperscaler+enterprise training customers)?  YES → Large Scale GPU; NO→Decision 5
5. Distributed inference endpoints (20+ edge cities, sub-100ms SLA, per-million-tokens pricing)?  YES → Tier 1 Inference; NO→Decision 6
6. Mid-market cloud with GPU compute, broad customer mix, per-GPU-hour pricing?  YES → AI Infrastructure providers (lowercase p); NO → manual_review_required
```

### 5.5 MSP/Aggregator flowchart (6 decisions)

```
Pre-gate: Sells managed network/connectivity OR aggregates carrier products + rev ≥$20M?
1. Sub-agent/1099 channel network ≥50 active agents?  YES→Decision 2; NO→Decision 3
2. Gross billings ≥$1B + ≥100 sub-agents + national?  YES → TSD Technology Services Distributor; NO → Master Agent (DEFAULT manual_review_required per consolidation reality)
3. Primary marketing: BOTH cloud AND network services (AWS Premier/Azure Expert/GCP Premier)?  YES→Decision 4; NO→Decision 5
4. Cloud revenue ≥30%?  YES → Cloud + Telecom Hybrid MSP; NO→Decision 5
5. ≥70% revenue from managed network services contracts (not commission)?  YES → Managed Network Services - MSP; NO→Decision 6
6. Direct sales of carrier products to enterprise, no sub-agent layer?  YES → Telecom Aggregator - MSP; NO → manual_review_required
```

### 5.6 Enterprise flowchart (6 decisions)

```
Pre-gate: BOTH gates pass — vertical (one of 4 sub-segments) AND scale ($1B+ rev AND (3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng))?
1. Hard disqualifier (network fully outsourced / single DC / pure SaaS / no direct carrier contracts)?  YES → Other; NO→Decision 2
2. Multi-hospital IDN ≥3 hospitals OR ≥$5B + EHR/imaging/clinic networks?  YES → Healthcare Systems
3. Banking/investment/insurance/payment/capital markets + multi-DC corporate IT?  YES → Financial Services (defense contractors w/ commercial procurement land here)
4. National retailer with multi-DC corporate IT (≥100 stores OR ≥$5B retail) + corporate IT not just warehouses?  YES → Retail and Distribution
5. BPO/outsourcing with ongoing operational multi-site delivery (NOT project consulting)?  YES→Decision 6; NO → manual_review_required
6. Hard-excluded as project consulting (Deloitte/McKinsey/BCG/Bain/Accenture Strategy)?  YES → Other; NO → Outsourcing Services
```

---

## 6. Per-sub-segment deep dives (compact headers — full content in `context/account-tiering/icp-deep-dives/B-and-C-{icp}.md`)

For each sub-segment below: 4-section headline (Definition, Quantitative markers, Top 3-5 anchors, Confidence rule). Full 12-section deep-dives in working files.

### 6.1 Network Operator (4 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-network-op.md`

#### `Tier 1 Carrier - Network Op`
- **Definition:** Largest national/multinational incumbent carriers; vertically integrated retail+enterprise+wholesale+international. State-protected legacy operators or post-Bell System nationals.
- **Quantitative:** Consolidated revenue $20B+; 50+ countries; subsea ownership/co-ownership; ASN 10-100+; 50,000+ employees.
- **Anchors (top):** AT&T, Verizon, Deutsche Telekom, NTT Group, Telefónica, Orange, KDDI, BT, Telstra (borderline), China Telecom/Mobile/Unicom, Singtel, Vodafone, América Móvil, T-Mobile US (mobile-first flag).
- **Confidence:** high_90 — anchor + $20B+ rev + ≥4 markers + 0 disqualifiers; medium_7089 — anchor archetype + ≥3 markers; manual_review_required — mobile-first >70% retail OR post-divestiture drift (Lumen).

#### `Pure Wholesale Carrier - Network Op`
- **Definition:** Wholesale-only carriers; capacity/transit/ports to other carriers + hyperscalers + large enterprises. No consumer/SMB.
- **Quantitative:** Revenue $200M-$5B; 100% B2B; Tier 1 IP transit or markets as such; multi-country footprint common.
- **Anchors:** Cogent, Arelion (formerly Telia Carrier), EXA Infrastructure, Hurricane Electric, Sparkle (TIM), Liberty Networks. Removed per Phase B: Lumen Wholesale (no separable entity), GTT (now Managed Network Services), Zayo (now Tier 2 National Wholesale post-CCF).
- **Confidence:** high_90 — anchor match + 100% B2B + Tier 1 IP transit + rev band; manual_review_required — overlap with Tier 1 Carrier (Lumen, Telstra) or Tier 2 Wholesale Fiber (Zayo, Cogent boundary).

#### `Cable MSO Enterprise Division - Network Op`
- **Definition:** Business/enterprise/commercial fiber arm of cable parent. Sells fiber/Ethernet/MPLS/SD-WAN to mid-market and enterprise. Distinct from residential parent.
- **Quantitative:** B2B revenue $1.5B+; parent residential cable in 10+ states; 5,000+ route miles fiber + HFC; distinct sales org.
- **Anchors:** Comcast Business ($9.7B), Spectrum Enterprise (~$7-9B; pending Charter-Cox), Cox Business (~$3-4B; pending Charter merger), Optimum Business (Altice USA).
- **Confidence:** high_90 — anchor + national cable parent + B2B ≥$1.5B + distinct B2B brand; manual_review_required — regional cable below $1B B2B (route to Regional Cable Operator Fiber).

#### `International Backbone Specialist - Network Op`
- **Definition:** Carriers whose primary business is international long-haul / subsea backbone WITH significant terrestrial component. Anchor between continents.
- **Quantitative:** Revenue $100M-$5B; HQ ≠ US; subsea ownership or IRU positions on ≥3 cable systems; 60-80% revenue from international.
- **Anchors:** Tata Communications, PCCW Global, Telstra International, HGC Global, Epsilon (KT-owned per Phase B correction; not Bharti-related), Console Connect (HKT-owned; Infratil deal cancelled Oct 2024 per Phase B), Bharti Airtel International, EXA Infrastructure, Sparkle.
- **Tiebreaker (vs Subsea cable operator):** Subsea + significant terrestrial backbone = International Backbone Specialist. Subsea-only with minimal terrestrial = Subsea cable operator.
- **Confidence:** high_90 — anchor + subsea ownership + international primary + terrestrial backbone presence; medium_7089 — anchor archetype but terrestrial component uncertain.

#### `Subsea cable operator` (NEW 2026-05-14)
- **Definition:** Pure-play subsea cable operators whose primary business is owning/operating/selling capacity on submarine fiber cables. Minimal or no terrestrial backbone.
- **Quantitative:** Revenue $20M-$500M; owns ≥1 named cable system (verifiable via TeleGeography Submarine Cable Map); landing stations as facilities; customer base = hyperscalers + content providers + regional carriers buying capacity.
- **Anchors:** Aqua Comms (pre-EXA acquisition; flag if record post-acquisition), Seaborn Networks, BW Digital, Hawaiki Submarine Cable, Telxius (borderline — has some terrestrial), some hyperscaler subsea SPVs (Anjana, Cap-1 — flag for D1 review whether they're sellable entities).
- **Tiebreaker:** Pure consortium without operating entity (FLAG, SEA-ME-WE) → D1.4 disqualifier, not this sub-segment.
- **Confidence:** high_90 — anchor + subsea ownership + minimal terrestrial; medium_7089 — anchor archetype confirmed via TeleGeography; manual_review_required is rare — only for genuinely contradictory evidence.

### 6.2 Fiber Operator (6 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-fiber-operator.md`

#### `Regional CLEC - Fiber operator`
- **Definition:** Multi-state CLECs, PE-backed regional platforms. Fiber-island unification core pain. Framework default for ambiguous mid-size.
- **Quantitative:** Revenue $120M-$600M; 2,000-30,000 route miles; 3-12 states; 3,500-15,000 on-net buildings; 200-1,500 employees.
- **Anchors:** Consolidated Communications (upper edge), Lumos, Crown Castle Fiber (defunct April 2026 — absorbed by Zayo), Bluebird Fiber (post-Everstream, 36K miles), FirstLight, GTT (legacy), Lit Communities, Ritter Communications, Hargray.
- **Confidence:** high_90 — single-state or multi-state CLEC + $30M-$1B + non-cable parentage; default sub-segment for ambiguous mid-size.

#### `Long Haul / Backbone - Fiber operator`
- **Definition:** National/multi-national backbones. Often run incumbent automation (DynamicLink, RapidRoutes). MaiaEdge layers federation on top, doesn't replace.
- **Quantitative:** Revenue $500M+; national or multi-national; primarily dark fiber + long-haul.
- **Anchors:** Lumen (parent overlap), Cogent (boundary with Pure Wholesale Carrier), Zayo (post-CCF expansion).
- **Confidence:** high_90 — large national + long-haul focus + 1,000+ route miles cross-metro; manual_review_required — Lumen/Cogent overlap with Network Op buckets.

#### `Dark Fiber Specialist - Fiber Operator` (capital "O" in internal value)
- **Definition:** Primarily dark fiber / wavelength sales. Long hold times between IRU signings. Metro+specific-route focus.
- **Quantitative:** Revenue $50M-$1B; 80%+ revenue from dark fiber IRUs.
- **Anchors:** FiberLight (200-mile Virginia Beach-Richmond corridor with Metro Fiber Networks 2026), Stealth Communications, Allied Fiber, ITS Fiber, Conterra.
- **Confidence:** medium_7089 default; high_90 if explicit "dark fiber primary" positioning + verified IRU revenue concentration.

#### `Tier 2 National Wholesale - Fiber operator`
- **Definition:** National or near-national pure wholesale fiber. Sells dark fiber + lit transport + waves + IRUs. Smaller than Tier 1 Globals but bigger than Regional CLECs.
- **Quantitative:** Revenue $300M-$5B; national US/EU; 20,000-300,000 route miles; 80%+ wholesale; PE-owned typical.
- **Anchors:** Zayo (post-CCF, $2.5B+, 224,000 route miles), Lightpath ($468M FY2025 + $362M AI contracts), Uniti+Windstream merged (240K route miles, 47 states post-Aug 2025), EXA Infrastructure (EU-focused).
- **Confidence:** high_90 — anchor or revenue band + 20K+ route miles + 80%+ wholesale; manual_review_required — CLEC-vs-Wholesale boundary ($100M+ wholesale AND meaningful direct-enterprise).

#### `Regional Cable Operator - Fiber operator`
- **Definition:** Regional cable companies with growing commercial fiber arms. Parent under $1.5B B2B (otherwise Cable MSO Network Op).
- **Quantitative:** Parent B2B $30M-$1B; 3-22 states; mostly residential cable with growing fiber book.
- **Anchors:** Breezeline (Cogeco US, 13 states), WOW! ($629M 2024), Mediacom Business (22 states), Midco Business, Service Electric, GCI (Alaska — special case), Cable ONE / Sparklight (~$1.7B — borderline Cable MSO).
- **Confidence:** high_90 — anchor + regional multi-state + B2B sub-$1B; manual_review_required — Cable ONE/Astound borderline.

#### `Municipal / Cooperative - Fiber operator` (renamed from Co-op/consortium 2026-05-13)
- **Definition:** Municipal utility fiber, rural electric co-ops, community-owned, multi-operator consortia. Federation-ready by design.
- **Quantitative:** Varies widely — sub-$10M (small muni) to $1B+ (large consortia like Diamond State Networks at $1.66B, 50K miles, 13 AR co-ops).
- **Anchors:** EPB Chattanooga, UTOPIA Fiber, Diamond State Networks, NEMR Telecom, NRECA member operators, NTCA member operators, USDA RUS-funded co-ops.
- **Confidence:** high_90 — community-owned/utility legacy + co-op governance + member directory presence; manual_review_required — middle-mile-only operators (EXCLUDE per file 05).

### 6.3 Colocation (4 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-colocation.md`

#### `Standard - colo`
- **Definition:** Traditional interconnection colos. Retail cross-connect margin focus. Per-rack/per-cabinet/per-kW sales.
- **Quantitative:** High XC volume per facility; large MMR; tenant count in hundreds; sub-10MW typical deployment size.
- **Anchors:** Equinix (parent — separate xScale child for Hyperscale Wholesale), Digital Realty (parent), CoreSite (American Tower 2021), Cologix, Iron Mountain (retail side), DataBank (retail side), Switch.
- **Confidence:** high_90 — anchor or "interconnection colo" primary positioning + per-rack/per-cabinet sales; default for ambiguous traditional colos.

#### `AI Signals - colo`
- **Definition:** AI-native or AI-retrofit colos. Confirmed GPU tenants, liquid cooling, 30kW+ racks. Anchor-tenant economics.
- **Quantitative:** Multi-year tenant leases; 60-80% revenue from named GPU/AI tenants; liquid cooling + high-density racks.
- **Anchors:** Crusoe, Applied Digital, Prometheus Hyperscale, Colovore, Nodiac (modular AI variant), NTT Global Data Centers Americas (AI side), Nexus Data Centers. Per NeoCloud Phase B: IREN, Core Scientific reclassified HERE (landlord model with Microsoft / CoreWeave deals).
- **Confidence:** high_90 — confirmed GPU/AI tenant + liquid cooling + density markers; manual_review_required — split-book operators (Vantage, Aligned, NTT, Iron Mountain) with both AI Signals and Hyperscale Wholesale books.

#### `Modular - colo`
- **Definition:** Distributed, prefabricated, or edge-pod operators. Growth = site count, not campus size. Industry-recognized BUILD typology + MaiaEdge-framed OPERATOR archetype.
- **Quantitative:** ≥3 sites; containerized/prefab deployments; <50 employees early-stage; founder-led decision authority.
- **Anchors:** Nodiac (500+ sites pipeline, 800+ MW), EdgePresence/Ubiquity, Armada, Colony Compute.
- **Confidence:** medium_7089 default given industry-recognition ambiguity; high_90 — explicit modular DC build language + multi-site footprint + per-site growth model.

#### `Hyperscale Wholesale - colo`
- **Definition:** Wholesale-only or wholesale-anchored colos. Multi-MW, multi-year, build-to-suit / shell-and-core. Per-MW sales (vs Standard per-rack).
- **Quantitative:** 10MW+ standard deployments; 5-15 year terms; 60%+ revenue from hyperscalers; 100MW-5GW per portfolio.
- **Anchors:** Compass, Aligned (Macquarie; BlackRock H1 2026 pending), Stack Infrastructure (IPI+Blue Owl), NTT Global Data Centers Americas, QTS (Blackstone, 4,752 MW), CyrusOne (KKR+GIP), Vantage (DigitalBridge+Silver Lake $25B Frontier campus), DataBank, Iron Mountain, Equinix xScale (child record), EdgeConneX (EQT), AirTrunk (Blackstone 2024).
- **Confidence:** high_90 — anchor + 60%+ hyperscaler revenue + multi-MW deployments; manual_review_required — split-book (xScale carve recommendation: parent + child records).

### 6.4 NeoCloud (5 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-neocloud.md`

#### `Large Scale GPU - Neocloud`
- **Definition:** Specialized cloud providers for GPU-as-a-Service for LLM training. Bare-metal multi-facility footprint (20-50+ locations).
- **Quantitative:** 20+ facilities; >100MW disclosed GPU capacity; named hyperscaler + enterprise customer base.
- **Anchors:** Nebius, Lambda (15+ US DCs, 320MW), Crusoe, Voltage Park, Cirrascale (boundary case), Northern Data AI / Taiga Cloud (dual-class with Crypto-to-AI), CoreWeave (ClusterMAX Platinum tier).
- **Confidence:** high_90 — 20+ facilities + named GPU clusters + training-primary; medium_7089 — emerging at 10-20 facilities.

#### `Tier 1 Inference - Neocloud`
- **Definition:** Providers with distributed inference endpoints at 20-50+ edge cities. Sub-100ms token latency SLAs. Per-million-tokens pricing model.
- **Quantitative:** 20+ edge cities; per-million-tokens pricing; minimal on-site staff; often Equinix carrier hotel deployments.
- **Anchors:** Together.ai (25+ cities, 200MW), Groq (35 Equinix POPs; NVIDIA acqui-hire Dec 2025 $20B), Cirrascale, DeepInfra ($107M Series B May 2026), Fireworks, Mistral La Plateforme, SambaNova (SN50 Feb 2026, 405B record), Sakana AI, Baseten.
- **Confidence:** high_90 — anchor + 20+ edge cities + per-token pricing; manual_review_required — custom-silicon hybrids (SambaNova, Cerebras boundary).

#### `AI Infrastructure providers - Neocloud` (lowercase "p")
- **Definition:** Mid-market cloud providers adding GPU compute to existing customer base. Per-GPU-hour pricing typical.
- **Quantitative:** 5-30 locations; per-GPU-hour pricing; broad customer mix (developers + SMBs + enterprises); ~$50M-$500M revenue.
- **Anchors:** Vultr, DigitalOcean, Fluidstack, Modal, RunPod, OVHcloud (boundary with Sovereign), Scaleway (boundary), Linode (Akamai).
- **Confidence:** high_90 — existing mid-market cloud + GPU compute add + per-GPU-hour; medium_7089 — emerging AI focus.

#### `Sovereign AI Clouds - Neocloud`
- **Definition:** Built for data sovereignty (GDPR/DPDP/national AI programs). Triple-signal qualifier required (per Phase B NeoCloud).
- **Quantitative:** ≥1 national program affiliation; in-country marketing; ≥1 regulated customer reference.
- **Anchors:** Nscale ($14.6B valuation; UK/EU), Firmus (Norway), E2E Networks (India), Yotta (India; 20k Blackwell Ultra Aug 2026), G42 / Inception (UAE; Stargate $30B 1GW Abu Dhabi March 2026), BSC (Barcelona Supercomputing Center, €200M EuroHPC), Sakana (Japan).
- **Confidence:** high_90 — triple signal (sovereign marketing + regulator compliance + customer ref); medium_7089 — 2/3 signals; low_5069 — 1 signal.

#### `Crypto to AI - Neoclouds` (trailing "s") — REVISED per Cooper feedback 2026-05-14
- **Definition (Cooper-revised):** Companies that used to mine for Bitcoin that have since pivoted to being more of a neocloud / co-location operator. The defining trait is BITCOIN MINING PAST + AI PIVOT, regardless of current business model (operator OR landlord).
- **Quantitative:** ≤$0.05/kWh power; immersion/liquid cooling; 100kW+/rack density; pivot announcement ≥6 months old; verifiable bitcoin mining history.
- **Anchors:** IREN (Microsoft $9.7B/200MW landlord), Core Scientific (CoreWeave host landlord), Galaxy Digital, Bitfarms (operator), TeraWulf (operator + landlord hybrid), APLD, Northern Data Group.
- **Tiebreaker (vs Large Scale GPU / AI Signals colo):** Bitcoin mining history confirmed → Crypto to AI - Neoclouds wins (regardless of operator vs landlord). No mining history + GPU compute operator → Large Scale GPU. No mining history + landlord-only with GPU tenants → AI Signals colo.
- **Confidence:** high_90 — bitcoin mining history confirmed + AI pivot confirmed + pivot ≥6 months old; medium_7089 — pivot announcement recent (<6 months) or mining history partially confirmed.
- **No `crypto_pivot_model` field needed** — Cooper feedback eliminated this distinction.

#### Boundary case FLAG — dedicated / reserved bare-metal private-AI (e.g. Cirrascale)
- **Pattern:** 100% dedicated, non-virtualized, long-term-contract (2-5yr) GPU infrastructure sold to regulated-vertical customers as private AI (e.g. a private-Gemini agreement for healthcare / financial services). Customer sometimes OWNS the hardware and the provider manages it in colo. Colo-anchored: owns no data centers, runs as primary tenant in third-party DCs.
- **Why it's a problem:** This fails all three `Tier 1 Inference - Neocloud` tests (no 20-50 edge-city distribution, no sub-100ms token-latency SLA, no per-million-tokens pricing) and is not the 20-50-facility training-primary `Large Scale GPU - Neocloud` pattern either. Cirrascale is currently carried as a boundary anchor in BOTH (lines above) and as an NC2 anchor in `enrichment-protocols.md`.
- **Interim rule:** Classify on `infrastructure_profile` (managed bare metal in leased colo), NOT disclosed GPU MW or revenue. The dual customer-owned-hardware model risks mis-tagging as MSP or Colo; the multi-marker rule (`infrastructure_profile` wins over revenue/MW) is the guard.
- **NEEDS COOPER / HUBSPOT REVIEW** before any sub-segment move or new marker (no-new-enum policy). Open question: does a dedicated / private-AI pattern warrant a redesign turn, or does it stay a `Tier 1 Inference` boundary classified on infrastructure_profile.

### 6.5 MSP/Aggregator (5 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-msp-aggregator.md`

#### `Telecom Aggregator - MSP`
- **Definition:** Traditional channel aggregators / telecom brokers reselling carrier connectivity to enterprises. Direct sales (no sub-agent layer).
- **Quantitative:** Revenue $20M-$2B; 30-100 carrier vendors; US-focused; W-2 or 1099-hybrid sales force.
- **Anchors:** Granite Telecommunications ($1.85B 2024 — scale anchor), Nitel (post-Hypercore 2022). To validate: CCS Global Tech, Comm One, Aretha Communications.
- **Confidence:** high_90 — anchor + direct enterprise sales + multi-carrier portfolio + no sub-agent layer; manual_review_required — IoT/eSIM (Aeris, EMnify) → EXCLUDE.

#### `Managed Network Services - MSP`
- **Definition:** MSPs/integrators/VARs whose primary offering is managed network services (not commission resell). Includes SD-WAN, NOC, FWaaS, SASE management.
- **Quantitative:** Revenue $50M-$10B; 70%+ managed services contracts; vendor-neutral or vendor-specific (Cisco/Fortinet partner).
- **Anchors:** Open Systems, Hughes Network Systems (EchoStar; pending DISH merger), Logicalis (Datatec), Presidio (BC Partners 2019, ~$5B+), GTT (post-2021 divestiture managed services); IT integrators (CDW, Insight, ePlus, WWT — boundary cases).
- **Confidence:** high_90 — 70%+ managed services + multi-vendor + enterprise customer base; manual_review_required — IT integrators (boundary with Cloud + Telecom Hybrid).

#### `TSD Technology Services Distributor - MSP`
- **Definition:** Distribution-tier orgs with sub-agent/1099 channels of 50-500+ active agents. Aggregate carrier contracts via sub-agent network. Centralized quote desks.
- **Quantitative:** Gross billings $1B+; 100+ active sub-agents; 100+ carrier vendors; US national + Canada/EU.
- **Anchors (Omdia CY2024):** Telarus ($2.9B GB), AVANT ($2.1B), Intelisys/ScanSource ($2.7B; net agency $84.7M ScanSource), AppDirect ($2.0B), Sandler Partners (~$209M revenue; UPWARD revision from file 05's $25M), Bridgepointe ($755M GB; firmly TSD-tier post April 2026 Charlesbank+Carlyle recap at $1B+ valuation).
- **Confidence:** high_90 — anchor + $1B+ gross billings + ≥100 sub-agents + Omdia listing.

#### `Master Agent - MSP`
- **Definition:** Smaller, often regional or vertical-focused master agencies with sub-agent networks. Boutique cousins of TSDs.
- **Quantitative:** Net commission $5M-$100M; 10-50 sub-agents; 20-80 carrier vendors.
- **Anchors (post-consolidation, per Phase B):** X4 Solutions (confirmed independent 2025; 35+ carriers, founded 2004), CyberNet Communications (medium confidence; regional, scale unverified). Per Phase B: only 2 verified independents. **Policy: defaults to `segmentation_confidence = manual_review_required`** until 5+ anchors verified.
- **Confidence:** Per policy — manual_review_required default; high_90 only if all 5 verification criteria met (independent + verified ≥10 sub-agents + revenue band + carrier portfolio + post-2022 operating history).

#### `Cloud + Telecom Hybrid MSP - MSP`
- **Definition:** MSPs whose business spans cloud reselling AND telecom managed services. 30-60% cloud / 30-60% network.
- **Quantitative:** Revenue $30M-$5B; ≥30% cloud revenue; AWS Premier / Azure Expert / GCP Premier partner status.
- **Anchors:** AHEAD ($3B 2024 est., reportedly exploring sale), CDW (post-Mission Cloud Dec 2024 — boundary case), Insight Enterprises (post-SADA Dec 2023 — boundary case), WWT, ePlus, Effectual Cloud, RapidScale (Cox/RapidScale; pending Charter merger).
- **Confidence:** high_90 — anchor + AWS Premier/Azure Expert + ≥30% cloud revenue + network services primary marketing; manual_review_required — pure cloud MSPs (post-acquisition Mission, SADA → EXCLUDE).

### 6.6 Enterprise (4 sub-segments) — full file: `context/account-tiering/icp-deep-dives/B-and-C-enterprise.md`

#### `Financial Services - Enterprise`
- **Definition:** Banks, investment firms, insurers, payment networks, capital markets infra. Commercial-procurement defense contractors land here.
- **Quantitative:** $1B+ revenue; 3+ DCs; in-house net eng team; direct carrier contracts; Equinix Fabric/Megaport port common.
- **Anchors (15+ verified):** JPMorgan, Goldman Sachs, BNY Mellon, State Street, Visa, Mastercard, Bank of America, Wells Fargo, Citi, BlackRock, Schwab; UK/EU: HSBC, Barclays, BNP Paribas; APAC: Mizuho, Nomura; Defense (commercial procurement): Lockheed Martin, RTX, Northrop Grumman, BAE Systems, L3Harris.
- **Confidence:** high_90 — Fortune 500 financial + 3+ DCs + in-house team + direct carrier contracts; manual_review_required — diversified industrials (Honeywell, GE, 3M) with corporate IT but Manufacturing NAICS.

#### `Healthcare Systems - Enterprise`
- **Definition:** Multi-hospital IDNs and large health systems. EHR DCs, imaging archives, regional clinic networks.
- **Quantitative:** $1B+ revenue; 3+ hospitals; in-house net eng; HITRUST/HIPAA in-scope systems.
- **Anchors (15+ verified):** HCA Healthcare, Ascension, CommonSpirit, Kaiser Permanente, Cleveland Clinic, NewYork-Presbyterian, Trinity Health, Adventist Health, Banner Health, Providence; EMEA: NHS England (special case — government), Karolinska Institutet (research-adjacent); APAC: Bumrungrad International.
- **Confidence:** high_90 — IDN + 3+ hospitals + EHR DC + in-house net eng; manual_review_required — CVS Health (retail-pharmacy + insurance hybrid), UnitedHealth (Optum split), McKesson/Cardinal/AmerisourceBergen (pharma distribution).

#### `Retail and Distribution - Enterprise`
- **Definition:** Multi-DC national retailers with multi-DC CORPORATE IT (not just multi-warehouse) and distribution-center networks. Meijer anchor.
- **Quantitative:** $5B+ retail revenue OR 100+ stores; 3+ DCs corporate IT; in-house net eng.
- **Anchors (15+ verified):** Meijer (anchor), Walmart, Kroger, Target, Costco, Home Depot, Lowe's, Albertsons, Publix; UK: Tesco, Sainsbury's; APAC: Aeon (Japan); Wholesale edge: Sysco, US Foods.
- **Confidence:** high_90 — anchor + 100+ stores + multi-DC corporate IT + direct carrier contracts; manual_review_required — restaurant chains (McDonald's, Yum, Chick-fil-A — Watch List); 3PLs (XPO, GXO — Watch List).

#### `Outsourcing Services - Enterprise`
- **Definition:** BPO / outsourced operations providers running multi-site delivery centers on ONGOING OPERATIONAL basis. NOT project consulting.
- **Quantitative:** $1B+ revenue; multi-country/multi-state delivery; regulated client data; in-house net eng.
- **Anchors (15+ verified):** Cognizant, Genpact, Concentrix (post-Webhelp), TaskUs, Conduent; EMEA-HQ: Capgemini; India-HQ: Wipro BPS, TCS BPS, Infosys BPM, HCL Tech; PH-anchored: Teleperformance Manila, Cognizant Manila; LATAM: Atento; Specialty: Firstsource (borderline scale gate), Sutherland Global Services.
- **Confidence:** high_90 — anchor + multi-site + ongoing operational + $1B+; manual_review_required — Kyndryl / NTT Data Services / DXC (MSP/Aggregator vs Outsourcing contested); IBM Consulting (dual-arm); Firstsource ($750M — borderline).
- **Hard-excluded:** Deloitte, McKinsey, BCG, Bain, Accenture Strategy & Consulting (project consulting, not operational delivery).

### 6.7 Cross-segment — Greenfield (REAL sub-segment per Cooper 2026-05-14)

#### `Greenfield`
- **Definition (Cooper):** Pre-operational or actively-in-build colocation or neocloud companies. "Companies coming out of the woodworks that are raising money and building new sites from the ground up." Series A-C funded, sites under construction, no operational customer base yet (or only LOI customers).
- **Customer_segment parent:** EITHER `Data Center Colo Provider` (Greenfield colo) OR `NeoCloud` (Greenfield neocloud). Not its own customer_segment.
- **Quantitative:** Funding round announced ≤24 months; ≥1 site under construction announced; <2 operational sites; pre-revenue or low-revenue; <100 employees typical.
- **Required signals:** Recent funding press; construction announcements ("groundbreaking," "first site," planned operational date); founder/exec LinkedIn profiles indicating industry veterans.
- **Anchor examples:** Stargate UAE pre-operational build (G42/OpenAI consortium, broke ground March 2026 — though G42 itself is Sovereign AI today); various AI campus builders mid-construction announced 2025-26 that don't yet have operational sites.
- **Auto-migration rule:** When the company opens its first operational site at scale (recent_news mentions "live customer" / "first site operational" / first revenue milestone), R2 reclassifies into the appropriate operational sub-segment (AI Signals colo / Modular colo / Hyperscale Wholesale / Large Scale GPU Neocloud / etc.).
- **Tiebreaker:** Bitcoin mining history + AI pivot → Crypto to AI - Neoclouds wins (not Greenfield, even if pre-operational).
- **Confidence:** high_90 — funding + construction announcements confirmed + clear parent segment; medium_7089 — funding confirmed but construction signals partial; low_5069 — funding signal only; `Flagged for deletion` — no funding AND no construction (not actually greenfield).

---

## 7. Contact persona mapping (from E)

Headline: 29 sub-segments × 4 personas (Technical Champion / Business Sponsor / Economic Buyer / Procurement) with specific title patterns.

Persona target seniority by ICP:
- Network Op / Fiber (Tier 1): VP+, C-level
- Network Op / Fiber (Tier 2/Regional): Director+ acceptable for Technical Champion
- Colocation (AI Signals, Hyperscale Wholesale anchor-tenant model): C-level + VP
- NeoCloud (early stage): Founder / VP+
- MSP/Aggregator: VP+ for TSD; Founder for Master Agent
- Enterprise: VP+ Network, Principal+ on technical side, C-level for sponsor

**Multi-thread minimum** for Tier 1 + Tier 2: ≥3 of 4 personas before hard-pursuing.

---

## 8. Industry taxonomy alignment (compressed; full per-ICP detail in `context/account-tiering/icp-deep-dives/B-and-C-{icp}.md`)

| ICP | Primary taxonomy | Status / mapping |
|---|---|---|
| Network Op | TeleGeography Submarine Cable Map + Wikipedia Tier 1 Network + Statista Top Telecoms + GSMA Intelligence | Maps cleanly except SUBSEA CABLE OPERATORS as separate bucket (decision pending) |
| Fiber Op | FCC BDC + USAC RLEC/CLEC/ILEC + NTCA/NRECA member directories + Vertical Systems Group Carrier Ethernet Leaderboard | FCC BDC doesn't classify wholesale-only; Tier 2 National Wholesale relies on VSG Challenge Tier |
| Colocation | Synergy Research (Top 25 Hyperscale / Top 50 Wholesale / Retail Multi-Tenant) + Structure Research + JLL Data Center Outlook + CBRE NA Trends | Modular operator archetype is MaiaEdge framing (build typology industry-recognized via 451 Research $34B+) |
| NeoCloud | SemiAnalysis ClusterMAX + Token Terminal + GAIA-X membership + Tom's Hardware AI benchmarks | ClusterMAX is quality-graded not segment-graded; sovereignty taxonomy varies by national program |
| MSP/Aggregator | Omdia TSD Market Report + Channel Futures MSP501 + Gartner MNS Magic Quadrant + CRN Solution Provider 500 | TSD anchors authoritative via Omdia; Master Agent landscape collapsed by 2018-24 consolidation |
| Enterprise | NAICS codes (52, 62, 44-45, 5614/5616) + Fortune 500 + Forbes Global 2000 + Equinix Fabric/Megaport customer directories + FedRAMP authorized list | Maps cleanly; government/defense FedRAMP-gated until authorization |

---

## 9. At-scale classification readiness assessment (from D4 + D5)

**Operational enrichment protocols + no-silent-failures guarantee in `context/account-tiering/enrichment-protocols.md`.**

D5 closes the 6 silent-failure modes:

1. Segment but no sub-segment → enforced: every ICP record gets explicit sub-segment OR null + `manual_review_required` + reasoning string
2. Catch-all default (Regional CLEC, Standard - colo, Telecom Aggregator) written without evidence → enforced: catch-all protocols require positive-evidence questions, not just negative-exclusion
3. Multi-classification missed → enforced: 12+ named overlap triggers in D5 §3-§8 (Tata, Lumen, Equinix xScale, IT integrators, IREN, CVS, Bharti Airtel, etc.)
4. Confidence written without evidence → enforced: deterministic thresholds per protocol + alignment audit check
5. D1 disqualifier missed → enforced: Stage 1.5 mandatory; D1 rule citation required in eviction audit
6. Data drift over time → enforced: quarterly anchor refresh + R2 120-day re-enrichment + R-Tier-Audit weekly (every Sunday 11pm CT - widened from monthly 2026-05-14 per Cooper)

Headline readiness table:

| Routine/Skill | Current avg | Post-Phase-3 target | Primary Phase 3 fix |
|---|---:|---:|---|
| R1 Fresh Enrichment | 2.6 | 4.5 | Add D1 pre-check, embed D3 flowcharts, apply Phase C confidence rules |
| R2 Stale Re-Enrichment | 2.6 | 4.5 | Same as R1 + recompute tier on sub-segment change |
| Weekly Signal Scan | 4.0 | 4.5 | Stage 5b tier recompute; D1 on Stage 3 NEW accounts |
| R-Tier-Audit (new) | 0 | 4.5 | Create per v4 master prompt §Step 8 (weekly cadence as of 2026-05-14; v4 supersedes v3) |
| segment-classification SKILL | 2.8 | 4.5 | Reference file 06 §5; encode confidence rules; reference D1+D2 |
| edge-case-researcher SKILL | 3.2 | 4.5 | Add 5 missing flowcharts; reference Phase C anchor lists |
| company-enrichment SKILL | 3.0 | 4.5 | Stage 1.5 D1 check; Stage 2.5 D3 traversal; Phase C confidence at Stage 3 |
| account-sourcing SKILL | 3.0 | 4.0 | Update to 29 values; reference D1 + anchor lists |
| import-processor SKILL | 4.0 | 4.5 | 29-value validation; case-sensitivity error messages; retired-value rejection |

---

## 10. Recommended Phase 3 deliverables

Based on the Phase A-E + D1-D4 research, Phase 3 should produce or update the following files. File 07 lists prompt-specific deltas; this section lists files to touch.

### New files Phase 3 creates

1. **`context/account-tiering/tier-compute-spec.md`** — per v4 master prompt §Step 1. Single source of truth for compute_tier() algorithm. References file 06 §5 (flowcharts) + §6 (sub-segments). (Authored at `context/core/` then moved to `context/account-tiering/` mid-execution 2026-05-14 per Cooper.)
2. **`context/account-tiering/sub-segment-qualification.md`** — new pointer file that explicitly references file 06 as primary source. Read by R1/R2/Signal Scan/R-Tier-Audit at startup.
3. **`context/account-tiering/enrichment-protocols.md`** — self-contained operational protocols (consumed by company-enrichment, R0, R1, R2, D7). Inlines all 30 per-sub-segment protocols + NC threshold matrix + Greenfield catalog at §6 / §6a / §7 (Cooper 2026-05-14).
4. **`cowork-scheduled-tasks/r-tier-audit/prompt.md`** — R-Tier-Audit per v3 §Step 8.
5. **`cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md`** — D7 weekly edge-case-resolution routine. Per Cooper feedback 2026-05-14. Reads manual_review queue + stale low_5069 + Unknown/Other escalations. Resolves with upgraded classification OR Flagged for deletion. Hard rule: nothing in manual_review more than 14 days.

### Files Phase 3 updates

| File | Phase 3 update |
|---|---|
| `context/hubspot/property-schema.md` | Section 2: list 29 enum values per file 06 §2; Section 3: rewrite for new tier framework; new sections for `network_op_track` + 3 signal persistence fields |
| `context/hubspot/hubspot-values.md` | Update sub-segment value table to 29 values with case-sensitivity notes; retire 3 archived values to "Retired" section |
| `context/segments/network-operator.md` | Add 4 sub-segment deep-dives from working file B-and-C-network-op.md; rename Track A/B to "Network Op Tracks"; reference file 06 §6.1 |
| `context/segments/fiber-operator.md` | Add 2 new sub-segments + Municipal/Cooperative rename; refresh anchors per working file B-and-C-fiber-operator.md; reference file 06 §6.2 |
| `context/segments/colocation.md` | Add Hyperscale Wholesale; update Modular Colo default to Tier 1; add IREN/Core Scientific reclassification per Phase B; reference file 06 §6.3 |
| `context/segments/msp-aggregator.md` | RESTRUCTURE 5 sub-segments; redistribute existing Subtype 1/2 content; reference file 06 §6.5 |
| `context/segments/neocloud.md` | Update Tier 1 Inference to Tier 2 default; refresh GPU pricing trend (recently reversed per Phase B); reference file 06 §6.4 |
| `context/segments/enterprise.md` | Confirm 4 sub-segments; encode confidence rules; reference file 06 §6.6 |
| `CLAUDE.md` | Add R-Tier-Audit to scheduled routines; add file 06 to required-reading hierarchy; document 7 known data quality follow-ups; rename `target_account` → `hs_is_target_account` globally |
| `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` (R1) | Add D1 pre-check Step 1.5; embed D3 flowchart; apply Phase C confidence; tier recompute step |
| `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` (R2) | Same + tier recompute on sub-segment change |
| `cowork-scheduled-tasks/signal-scan-*` (6 per-segment + aggregator, 2026-05-28 split) | Stage 5b signal field writes + tier recompute (each per-segment scan; aggregator does no HubSpot writes) |
| `Claude routine prompts/<R6 prompt>` | Tier maintenance step per v3 §Step 9 |
| `skills/segment-classification/SKILL.md` | Reference file 06 §3 (D1) + §5 (D3) + §6 (Phase C confidence); inline-link to D5 §3-§8 protocols |
| `skills/edge-case-researcher/SKILL.md` | Add 5 missing flowcharts (Network Op, Colo, NeoCloud, Fiber, MSP); reference file 06 §5 + D5 protocols for evidence verification |
| `skills/company-enrichment/SKILL.md` | **Replace freeform classification with D5 per-sub-segment protocols.** Stage 1.5 D1; Stage 2.5 D3 traversal → Stage 3 D5 protocol execution (5-8 questions per sub-segment, deterministic confidence thresholds, explicit fall-through to manual_review_required). End-of-pipeline verification queries (D5 §9). |
| `skills/import-processor/SKILL.md` | 29-value validation + case-sensitivity + retired-value rejection. Catch-all default flagging per D5 §10. |
| `skills/account-sourcing/SKILL.md` | Update to 29 values; reference anchor lists |
| `skills/crm-hygiene/SKILL.md` | Weekly audit per D5 §9: records on framework defaults without protocol evidence; records on manual_review_required for >30 days; records with confidence written but no reasoning string. |

### HubSpot UI write (optional per v3 §Step 15)

Update `account_tier` property description in HubSpot to match framework convention (Tier 1 = highest priority). Single permitted HubSpot MCP write in Phase 3.

### Decisions Cooper has resolved (2026-05-14)

1. ~~**Subsea cable operator bucket**~~ — RESOLVED. Cooper added as 30th sub-segment under Network Op parent. D5 protocol N5 + flowchart Decision 6 cover it.
2. ~~**`crypto_pivot_model` HubSpot field**~~ — RESOLVED. Crypto to AI - Neoclouds redefined as inclusive (operator OR landlord). No new field needed.
3. ~~**Greenfield enum archive**~~ — REVERSED. Cooper confirmed Greenfield is a REAL sub-segment for actively-being-built Colo + NeoCloud. D5 protocol G + auto-migration rule encoded.
4. ~~**NaaS Platform Operator subtype retirement**~~ — RESOLVED. NaaS platforms classify as `Other` (competitive reference) or `Flagged for deletion`. Broader principle: any account not matching ICP buckets → `Flagged for deletion`.
5. **GPU pricing trend refresh** — STILL OPEN. Phase 3 updates neocloud.md cheatsheet to reflect 2026 reversal ($1.70→$2.35/hr).
6. ~~**Equinix xScale parent + child record convention**~~ — RESOLVED via tiebreaker. Parent (Equinix) → Standard - colo. Child (Equinix xScale, if separate record) → Hyperscale Wholesale. No manual_review default. Same logic for Vantage / Aligned / NTT / Iron Mountain / QTS split-book operators.
7. ~~**`Master Agent - MSP` default policy**~~ — REVERSED. Cooper feedback: classify best-fit; no manual_review default. D5 protocol M4 revised; low_5069 acceptable for thin-anchor records.

### Decisions still open

- **GPU pricing trend refresh** (item 5 above) — Phase 3 cheatsheet content update.
- **D7 weekly cadence scheduling** — Cooper runs manually OR schedules via Cowork. Spec is in `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md`; Phase 3 creates the cowork prompt file.

---

**End of file 06.** Companion file 07 lists specific deltas to the v3 master prompt.
