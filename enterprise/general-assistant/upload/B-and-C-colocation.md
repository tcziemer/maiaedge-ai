# Phase B + C — Colocation ICP Sub-Segment Research

**Scope:** 4 active HubSpot `company_sub_segment` values under `customer_segment = "Data Center Colo Provider"` (503 records). All four are CASE-SENSITIVE internal strings — never paraphrase or recapitalize when writing classifier logic.

1. `Standard - colo`
2. `AI Signals - colo`
3. `Modular - colo`
4. `Hyperscale Wholesale - colo` (newest, added Phase 1.1; NOT yet in `context/segments/colocation.md` cheatsheet)

**Sources consulted (2026-05-14 web pass):** Synergy Research Group (Colocation Market Tracker + capacity-share articles), JLL 2025/2026 Global Data Center Outlook + North America Year-End 2025, CBRE H1/H2 2025 North American Data Center Trends, Structure Research 2025 DCI report ($92.4B market, 64% hyperscale / 36% retail), Uptime Institute Tier Classification System (facility-level), Dell'Oro liquid cooling market, dgtlinfra Top 250 Data Center Companies, Data Center Frontier industry coverage, Data Center Dynamics M&A coverage, individual operator newsrooms (Crusoe, Aligned, Vantage, DataBank, EdgeConneX, Iron Mountain, CoreSite, Switch, Compass), SEC filings (Equinix xScale JV), 451 Research Datacenter KnowledgeBase prefabricated-modular definition, Vertiv/Schneider modular product literature, ENCOR Advisors 2025 Modular Data Center Guide, BlackRock/MGX/GIP $40B Aligned announcement, KKR+GIP CyrusOne close, Blackstone QTS close, DigitalBridge/IFM Switch close (Tier 5 designation language confirmed).

**Source files cross-referenced:** `05 - Sub-segment definitions for cheatsheets.md` (Phase 3.5 canonical Hyperscale Wholesale + anchor corrections), `context/segments/colocation.md` (Standard / AI Signals / Modular existing deep-dives lines 435-477, power-queue play, tenant concentration risk, colo-vs-neocloud disambig, modular DC variant, greenfield disambiguation), `context/signals/colocation-signals.md` (full signal catalog C-A0..C-C5), `working/00-hubspot-enum-verification.md` (live HubSpot enum state, 29 active sub-segments, 503 colo records).

---

## Top section — Industry taxonomy alignment

### Synergy / Structure / JLL / CBRE → MaiaEdge 4-way mapping

The industry consensus splits colocation into **two primary buckets** plus a recognized **edge / modular** adjacency:

| Industry tier (consensus) | Industry definition | Per-tenant deployment | Pricing unit | Term length | MaiaEdge sub-segment(s) |
|---|---|---|---|---|---|
| **Hyperscale / Wholesale** (Synergy "Hyperscale + Wholesale"; Structure "Hyperscale" = 64% of $92.4B DCI market 2025) | Multi-MW build-to-suit or shell-and-core for cloud/hyperscaler tenants; 3-10 anchor tenants per portfolio | 10MW+ per deployment, 100MW+ campuses standard | $/kW/month wholesale rate ($195.94/kW/mo CBRE H2 2025 national avg; $200+/kW/mo primary markets; 10MW+ deals +13.8% YoY in NoVA) | 5-15 years, ROFR/ROFO clauses | `Hyperscale Wholesale - colo` |
| **Retail Multi-Tenant / Interconnection** (Synergy "Retail Carrier-Neutral + Bandwidth Provider"; Structure "Retail" = 36% of DCI market, 7.7% CAGR vs hyperscale 16.9%) | Cabinet/rack/cage tenancy in carrier-neutral facilities; revenue mix biased to cross-connects + interconnection | Sub-MW per tenant typical (300kW threshold often used as retail-wholesale divider; some operators set 500kW or 1MW) | $/cabinet + $/kW + $/cross-connect | 1-3 years | `Standard - colo` and (when GPU-tenant overlay is present) `AI Signals - colo` |
| **Edge / Modular / Prefabricated** (Synergy treats as adjacent, not a primary tier; 451 Research Pathfinder defines prefab-modular as a distinct build typology; Vertiv/Schneider/Dell/Eaton/ABB/Stulz dominate as suppliers) | Containerized or ISO/skid-mounted pods at distributed sites; growth by site-count not campus-size | Sub-MW per pod typical; deployments scale by adding pods | $/pod + power + connectivity | Variable; partner-site-driven | `Modular - colo` (operator-side; vendor-side is excluded ICP) |

**Synergy's quarterly Colocation Market Tracker explicitly carries two sub-views: Retail Colocation (Carrier-Neutral + Bandwidth Provider) and Wholesale Colocation (Hyperscale + Enterprise/Service Provider).** MaiaEdge's split of Wholesale into `Hyperscale Wholesale - colo` (pure-wholesale operator with hyperscaler concentration) is one level finer than Synergy publishes — but Synergy's internal "Hyperscale share of Wholesale" sub-view, plus Structure Research's 64/36 split, validates that the operator archetype is industry-coherent.

### Uptime Institute Tier ≠ MaiaEdge account_tier — FLAG

**Uptime Institute Tier I/II/III/IV is FACILITY-level certification of redundancy and concurrent maintainability:**
- Tier I = Basic Capacity (single path; protects against human error, not failure)
- Tier II = Redundant Capacity Components (partial N+1, single distribution path)
- Tier III = Concurrently Maintainable (N+1 redundancy, dual delivery paths, maintenance without downtime)
- Tier IV = Fault Tolerant (2N+1, no impact from single failure)

**MaiaEdge `account_tier` is OPERATOR-level commercial priority (Tier 1 = highest, Tier 5 = lowest — INVERTED from HubSpot's UI which says "1 lowest, 5 highest").**

A Tier IV-certified facility can be operated by a Tier 5 MaiaEdge account (e.g., a single-facility colo with no AI tenants and no signal activity). Conversely, a Tier 1 MaiaEdge account can include Tier II-certified facilities (early-stage operator with strong AI Signals). **Do not let enrichment bots conflate them.** Switch's marketing of "Tier 5" infrastructure is a Switch-branded extension (Tier IV + additional uptime/security claims), not an Uptime Institute classification — Switch's Tier 5 language confirmed in DigitalBridge/IFM acquisition press but is not a standardized industry tier.

The signal catalog (`colocation-signals.md` lines 218-225) correctly flags Uptime Tier certification as a trailing indicator (12-18 mo lag from design), useful for qualification not buying-trigger scoring. Preserve that exclusion.

### Is "Modular - colo" industry-recognized or MaiaEdge framing?

**Answer: Both — with a precise distinction.**

- **The build typology** ("prefabricated modular data center," "containerized DC," "ISO-container DC," "skid-mounted DC") IS industry-recognized. 451 Research's Pathfinder Report defines it explicitly. The modular DC market is sized at $34.84B in 2025 → $143.08B by 2034 (17.2% CAGR per InsightAce). Major equipment suppliers — Vertiv, Schneider Electric, Dell, Johnson Controls, Eaton, Delta, Huawei, ABB, Stulz, Rittal, Hubbell — all sell prefabricated modules as a primary product line. Schneider holds 21% market share in PFM.
- **The operator archetype** ("colo operator whose growth model is site-count via prefab pods at partner power sites") is NOT formally named by Synergy, Structure, JLL, or CBRE as a separate tier. Industry coverage scatters these operators across "edge colocation" (DataBank's "modular edge data center platform"), "containerized edge" (Armada Leviathan), and "edge colocation" within retail. There is no published market-share table for modular-operator-colos.
- **MaiaEdge's `Modular - colo` is therefore a MaiaEdge-specific operator framing on top of the industry-recognized build typology.** It is justified internally because the buying motion (founder/COO-level; first-multi-site fabric decision; site-count growth not campus-size) is materially different from Standard or AI Signals colo. But classifier reasoning strings should explicitly note "MaiaEdge framing — no Synergy/Structure published market tier for this archetype" so reps don't accidentally cite a non-existent industry ranking.

**Anchor examples per `context/segments/colocation.md` line 467:** Nodiac (modular containerized DCs at renewable energy sites, 500+ site pipeline, 800+ MW), EdgePresence (acquired by Ubiquity 2023; small edge pods), Armada (containerized edge — Tampnet offshore oil rigs, US Navy, Aramco, Newlab; Leviathan MW-scale product launched 2025 with $131M raise), Compass Datacenters (note: Compass is primarily Hyperscale Wholesale not Modular — its prefab-build methodology is a delivery approach, not its operator archetype; verify before classifying).

### Reverse-mapping — operators spanning 2+ MaiaEdge sub-segments

The following operators publicly run BOTH retail/Standard AND Hyperscale Wholesale books, or BOTH Hyperscale Wholesale AND AI Signals tenant overlays. **Default policy: `manual_review_required` with reasoning string capturing the split, then classify to the LARGER book per published revenue mix.**

| Operator | Sub-segments straddled | Recommended HubSpot handling |
|---|---|---|
| **Equinix** | `Standard - colo` (core IBX retail business) + `Hyperscale Wholesale - colo` (xScale JV with GIC + CPP + PGIM — $15B+ pre-2024 JV expansion to >$15B in 2024; 25/37.5/37.5 equity split with Equinix retaining 25%) | **Recommendation:** Single primary HubSpot record on `Standard - colo` (Equinix's $9B+ retail interconnection book vastly exceeds xScale revenue). Create a separate child record "Equinix xScale" on `Hyperscale Wholesale - colo` with explicit reasoning string. Sub-record convention: parent record holds Tim-Lieto-/-Ken-/-Tim-Z territory ownership; xScale child record carries hyperscaler-tenant deal pipeline. Flag this as a Phase 3 policy decision for Cooper. |
| **Iron Mountain Data Centers** | `Standard - colo` (retail enterprise colo) + `Hyperscale Wholesale - colo` (build-to-suit with MODs for wholesale tenants; geothermal cooling) — 1.3GW global, 1,300+ customers, 5M sqft | **Recommendation:** `manual_review_required` until revenue split published in 10-K. Default to `Hyperscale Wholesale - colo` if buildout pipeline is >50% pre-leased to hyperscalers; `Standard - colo` otherwise. Iron Mountain's 2025 Phoenix/Denver/Columbus/San Antonio/Boise expansion is wholesale-anchored per CBRE/JLL coverage. |
| **Vantage Data Centers** | `Hyperscale Wholesale - colo` (primary; DigitalBridge majority + Silver Lake $6.4B JV 2024; $25B Frontier mega-campus 1.4GW Texas, 1,200 acres, first building H2 2026, supports 250kW+ racks with liquid cooling) — straddles `AI Signals - colo` due to AI-tenant overlay | **Recommendation:** `Hyperscale Wholesale - colo` PRIMARY; flag manual review if Frontier campus gets named GPU/neocloud tenant publicly (would tip toward AI Signals). |
| **Aligned Data Centers** | `Hyperscale Wholesale - colo` (primary; pending sale to BlackRock GIP + MGX + AIP at $40B EV — announced Oct 2025, expected close H1 2026, exits Macquarie Asset Management ownership from 2018) + `AI Signals - colo` (DeltaFlow liquid cooling launched Jan 2024; 5GW+ operational/planned across US/MX/BR/CL/CO) | **Recommendation:** `Hyperscale Wholesale - colo` PRIMARY until BlackRock/MGX close completes; reasoning string should note the AI-tenant overlay. Per Cooper's M&A policy, classify per current legal state (Macquarie-owned); RevOps re-assigns post-close H1 2026. |
| **NTT Global Data Centers Americas** | `Hyperscale Wholesale - colo` (20% YoY 2024) + `Standard - colo` (legacy retail book outside US) | `Hyperscale Wholesale - colo` for Americas entity; flag parent NTT for multi-segment review. |
| **DataBank** | `Standard - colo` (60+ DCs, 20 interconnection hubs, 30+ markets enterprise edge) + `Modular - colo` (advertises a "modular edge data center platform") | **Recommendation:** `Standard - colo` PRIMARY; modular platform is delivery mechanism inside Standard book, not a separate operator archetype. |
| **EdgeConneX** | `Hyperscale Wholesale - colo` (EQT acquired 2020; 80 DCs in 50+ markets; Jakarta 200MW+ expansion 2024; Sixth Street minority 2024) + `AI Signals - colo` (AI investing strategy with EQT launched 2024) | `Hyperscale Wholesale - colo` PRIMARY; AI-tenant signal triggers manual review. |
| **Compass Datacenters** | `Hyperscale Wholesale - colo` (Brookfield Infra + Ontario Teachers acquired March 2025 from RedBird/Azrieli; 1.25GW pipeline; 6 hyperscale DCs ABS securitization $830M Phoenix + Toronto, 100% leased to 4 investment-grade hyperscaler tenants) | `Hyperscale Wholesale - colo` clean fit. |
| **QTS** | `Hyperscale Wholesale - colo` (Blackstone $10B take-private 2021; 4,752 MW disclosed) | `Hyperscale Wholesale - colo` clean fit. |
| **CyrusOne** | `Hyperscale Wholesale - colo` (KKR + GIP $15B take-private 2022; 55+ DCs) | `Hyperscale Wholesale - colo` clean fit. Note 2025 10-hour outage testing KKR/GIP. |

**Policy needed (Cooper decision required):** Sub-record handling convention for Equinix-class operators with material xScale-style wholesale JVs. Options: (A) single record + reasoning string only, (B) parent + child records with explicit linkage, (C) parent record only with `manual_review_required` permanent flag and quarterly RevOps review.

---

## `Standard - colo`

### Definition (sharpened — 4 distinguishing axes)

| Axis | Standard - colo |
|---|---|
| Deployment scale per tenant | Sub-MW typical (cabinet → cage → small private suite). Per-tenant footprint <300kW typical; some operators set the wholesale dividing line at 500kW or 1MW. |
| Anchor tenant concentration | LOW — hundreds to low-thousands of tenants per facility. Top tenant typically <5% of facility revenue. Carrier-neutral, network-dense. |
| Sale unit | Per-rack + per-kW + per-cross-connect. Revenue mix: 60-80% space/power (low margin), 10-20% cross-connects, 0-5% cloud on-ramps (per `colocation.md` lines 10-12). Interconnection attach rate is the differentiator vs. landlord positioning. |
| AI vs general workload | General enterprise workload primary. Some accommodation for AI-retrofit (selective liquid cooling deployment per rack), but the operator's go-to-market identity is interconnection-led, not GPU-tenant-led. |

### Quantitative markers

- **Per-tenant deployment:** 1 cabinet to 300kW typical; cap at the operator's wholesale dividing line.
- **Pricing:** $195.94/kW/mo national avg (CBRE H2 2025) for 250-500kW retail; $200+/kW/mo in primary markets. Heavy variance below 100kW (operators bundle managed services).
- **Lease terms:** 1-3 years typical.
- **Tenant count:** hundreds to low-thousands per facility.
- **Operator scale:** $10M-$500M revenue, 1-10+ facilities, 20-500 employees (per `colocation.md` line 13). Includes larger Tier 1 operators like Equinix (>$9B retail book) and Digital Realty for the retail-IBX portion of their portfolios.
- **Cross-connects:** Equinix at 500K+ globally (460,500 per dgtlinfra), Digital Realty at 218,000, CoreSite at 30 DCs/4.5M sqft. Cross-connect economics: ~$400/mo each, scale linearly with customers — single PBC ($2,125-$4,250/mo) replaces multiple cross-connects + unlocks dynamic NNI creation per `colocation.md` lines 428-431.

### Required signals

`colocation-signals.md` Tier A applicable: **C-A0** (Greenfield S2/S3 permit + utility), **C-A1** (site count 1→2 transition — single highest-leverage moment for regional Standard colos), **C-A4** (VP/Director of Interconnection / Network / Fabric hire — primary trigger), **C-A5** (network engineering job-req surge), **C-A7** (M&A / PE recap — both announcement and close events).

Tier B: **C-B1** (8-K interconnection miss language for public REITs DLR, EQIX, IRM, COR), **C-B4** (conference speaking slot on interconnection / fabric / AI), **C-B5** (sovereignty / data-residency announcement).

Tier C: **C-C1** (hyperscaler-adjacent <50 miles claim — wedge for cloud on-ramp as a product), **C-C2** (carrier-neutral / meet-me-room expansion), **C-C3** (tenant churn to Equinix Fabric or Megaport — inverse read).

### Disqualifiers

- Single anchor tenant >40% of facility revenue → `Hyperscale Wholesale - colo`
- Named GPU/neocloud tenant (Lambda, Crusoe, Nebius, Nscale, Together AI, Fluidstack, RunPod, Vultr) + liquid cooling + 30kW+ racks → `AI Signals - colo`
- Containerized / modular pod-based deployment as primary build typology → `Modular - colo`
- Sub-rack tenancy / "bare metal MSP" model with no facility ownership → not colo (likely MSP)

### Anchor companies (mixed geographies, M&A verified 2026-05-14)

**Tier 1 retail-heavy (US):**
- **Equinix** — public (EQIX). Retail IBX portfolio is `Standard - colo`; xScale JV is separate. 460,500 interconnections globally.
- **Digital Realty** — public (DLR). 312 DCs, 2,431 MW, 39.5M sqft, 5,000+ customers, 218,000 cross-connects. Retail portion = Standard; wholesale book = Hyperscale Wholesale; flag for split-record handling.
- **CoreSite (American Tower)** — acquired by American Tower for $10.1B, closed 2021. 30 DCs, 4.5M sqft, 11 US markets. SV9 Santa Clara opened July 2025. Open Cloud Exchange (OCX) is their interconnection platform.
- **Iron Mountain Data Centers** — public (IRM). 1.3GW global, 1,300+ customers; split book — flag for manual review.
- **DataBank** (DigitalBridge portfolio; SoftBank pending acquisition of DigitalBridge announced Dec 2025 at $4B) — 60+ DCs, 20 interconnection hubs, 30+ markets, $2.0B equity raise Oct 2024 led by AustralianSuper $1.5B.
- **Switch** (DigitalBridge + IFM took private $11B 2022) — 5 PRIMES campuses, 16 facilities, 508MW, 32.4k cabinets, 5.1M GSF, 1,350+ customers. Switch's own positioning is RETAIL ENTERPRISE colocation (Tier 5 brand language, CEO publicly avoided hyperscale-wholesale-only deals). `Standard - colo` per Phase 3.5 correction; previously misclassified.

**Tier 2-3 regional retail (US):**
- **Cologix** — 30+ network-dense interconnection facilities, North America focus.
- **Flexential** — 40+ facilities, US national, retail + hybrid cloud.
- **EvoSwitch / Iron Mountain Amsterdam** — EMEA retail.
- **365 Data Centers** — 20+ regional US.
- **TierPoint** — 40+ US facilities, managed services + colo.

**International retail:**
- **Telehouse / KDDI** — global retail interconnection hubs (London, NYC, Paris, Tokyo).
- **Global Switch** — wholesale-leaning but operates retail-style interconnection in core markets.
- **Maincubes** — DE/NL retail enterprise.
- **NorthC** — Benelux + DE regional retail.

### Confusable-with comparison

| Compared to | Distinguishing test |
|---|---|
| `Hyperscale Wholesale - colo` | Deployment scale: <300kW/tenant = Standard; >1MW/tenant typical = HW. Term: 1-3yr = Standard; 5-15yr ROFR/ROFO = HW. Revenue mix: cross-connects + retail = Standard; multi-MW wholesale = HW. |
| `AI Signals - colo` | Standard has interconnection-first identity; AI Signals has GPU-tenant-first identity. Standard may have liquid cooling deployments but no named anchor GPU/neocloud tenants. Per `colocation.md` AI Signal Detection Quick Reference (lines 220-243): STRONG = named GPU cloud tenants + liquid cooling + 30kW+; NONE = traditional enterprise tenants + standard density = Standard. |
| `Modular - colo` | Standard operators grow campus-size; Modular operators grow site-count via prefab pods at partner power sites. Standard ~10 large facilities; Modular ~50-500+ small pods. |
| NeoCloud `Crypto to AI - Neoclouds` | Standard sells space to GPU tenants; Crypto-to-AI Neocloud sells GPU compute itself. Per `colocation.md` lines 524-529: "sells space/power/cooling to GPU tenants" = AI Colo; "sells compute" = Neocloud. |

### Selling angle

Lead with **interconnection-attach-rate vs. landlord frame** (Sidecar §4.1.A per `colocation.md` line 451). Cold-email banned phrases: "fabric-in-a-box" (use only in cheatsheet / discovery / live conversations). Core message:

"Most colos sell space and power while Equinix captures the interconnection revenue. Build your own fabric — automated cross-connects, virtual meet-me room, cloud on-ramp as a product — without years of development. Keep the customer, margin, and roadmap."

Power-queue leverage play (per `colocation.md` lines 479-487) applies when colo is in NoVA / Phoenix / Dublin / Singapore / Frankfurt / Santa Clara: "Pack more tenants into the MW you already have by using the network as the scarcity control layer, not power."

### HubSpot fields R1/R2 must populate

| Field | Standard - colo value |
|---|---|
| `customer_segment` | `Data Center Colo Provider` |
| `company_sub_segment` | `Standard - colo` |
| `account_tier` | Tier 1 (top-25 anchor) / Tier 2 (regional multi-facility) / Tier 3 (single-facility regional) — INVERTED HubSpot convention |
| `hs_is_target_account` | `true` for Tier 1-2 |
| `recent_news_or_trigger_event` | Stamped by signal scan on C-A0/A1/A4/A5/A7 hits |
| `infrastructure_profile` | Free-text: facility count, MW capacity per facility, cross-connect count if disclosed, primary metros, carrier count in MMR |
| `segmentation_confidence` | `high_90` requires: ICP-segment match + anchor-pattern match + ≥2 quantitative markers + explicit operator positioning |
| `last_enriched_date` | Stamped only on full pipeline pass + Completeness Gate pass |

### Signal source coverage

Robust tier (single-source HIGH): DCF, DCD, DCK, Bisnow Data Center, PR Newswire + Business Wire Appointments tag, StockTitan SEC 8-K mirror (DLR / EQIX / IRM / DBRG / COR / CONE-equiv), SEC EDGAR backup, Greenhouse/Lever/Ashby for C-A5, Apollo MCP enrichment.

Medium tier (cross-source preferred): Crunchbase, PTC + Capacity + ITW + Datacloud + AI Infrastructure Summit agendas (C-B4 context only), AFCOM/7x24 Exchange.

Excluded: county permitting portals, utility queue PDFs, state econ-dev press, local business journals, Reddit, Wayback Machine, Glassdoor, Indeed. (Per `colocation-signals.md` lines 258-271.)

### Contact personas

**Large public / Tier 1 (Equinix-class, DLR-class, IRM-class retail):**
- **VP Interconnection / Head of Fabric Services** (PRIMARY) — owns cross-connect velocity, interconnection revenue %, fabric platform roadmap. The buyer for MaiaEdge.
- VP Data Center Operations — facility-side technical validation.
- CRO — commercial cosignatory; cross-connect attach-rate-vs-landlord pitch is a CRO conversation in disguise.

**Regional multi-facility ($100M-$500M):**
- VP Operations — operational owner of cross-connect provisioning pain.
- VP Commercial / Head of Wholesale — commercial cosignatory.
- CTO / VP Engineering — technical buyer when no dedicated VP Interconnection exists.

**Per `colocation.md` line 446:** Standard sells to VP Interconnection (large) or VP Operations (regional). NOT a founder-led sale (those are Modular). NOT a Chief Network Engineer + CFO co-sale (those are AI Signals).

### Confidence scoring rules

Per Phase 3.5 framework (file 05 lines 35-40):

- `high_90` Standard - colo: (1) anchor pattern match (Equinix retail / DLR retail / CoreSite / Cologix / Flexential / Switch / TierPoint / 365 / regional Tier-2 archetype within 1 std dev) + (2) ≥2 quantitative markers (revenue band, facility count, cross-connect count if public, primary metros) + (3) explicit operator positioning on website / 10-K / analyst report (e.g., "interconnection-led," "carrier-neutral," "cross-connect attach").
- `medium_7089`: two of three above, OR all three with weak corroboration on one.
- `low_5069`: one of three OR ambiguous between Standard and AI Signals (no named GPU tenant but liquid cooling deployments) OR ambiguous between Standard and Hyperscale Wholesale (operator has both books, retail-primary unclear).
- `manual_review_required`: anchor straddles 2+ sub-segments (Equinix, IRM, Vantage, DataBank, Iron Mountain); recent M&A within 12 months not yet integrated; revenue-band breach >2x upper / <50% lower.

### Industry sources for ongoing validation

Synergy Research Group Colocation Market Tracker (quarterly; Retail Carrier-Neutral + Bandwidth Provider sub-views), Structure Research Global DCI Report (annual; 36% retail share 2025), JLL Global Data Center Outlook (semiannual), CBRE North American Data Center Trends (H1 + H2), 451 Research Datacenter KnowledgeBase via S&P Global (12,960+ facilities tracked across 2,700+ providers, 131 countries), dgtlinfra Top 250 Data Center Companies (annual), Data Center Frontier, Data Center Dynamics, Uptime Institute Annual Industry Survey, PeeringDB facilities directory.

---

## `AI Signals - colo`

### Definition (sharpened — 4 distinguishing axes)

| Axis | AI Signals - colo |
|---|---|
| Deployment scale per tenant | Mid-MW to 10MW+ per anchor GPU tenant deployment; some retrofit operators have sub-MW AI overlays in otherwise standard facilities |
| Anchor tenant concentration | HIGH — single GPU cloud tenant or hyperscaler can represent 40-80% of facility revenue. Tenant concentration disclosed in public filings is a HIGH-confidence signal (per `colocation.md` lines 491-498). |
| Sale unit | Hybrid: per-MW for the anchor + retail cross-connect cabinet for east-west tenant-to-tenant paths. Networking SLA embedded into tenant MSA rather than priced separately. |
| AI vs general workload | AI/inference workload primary identity. NVIDIA GB200 NVL72 = 120kW/rack standard. Vera Rubin NVL144 = 600kW/rack target 2026. Direct-to-chip liquid cooling default for new builds. Per `colocation.md` lines 506-507: Equinix reports 60% of largest Q4 2025 deals were AI-driven with 33% higher density. |

### Quantitative markers

- **Confirmed GPU cloud tenant** (Lambda Labs, Crusoe, Nebius, Nscale, Together AI, Fluidstack, RunPod, Vultr, CoreWeave) — NAMED in operator press release or tenant's own filing.
- **Liquid cooling deployment** — direct-to-chip (D2C), rear-door heat exchanger, CDU, or immersion — tied to a specific named facility (per `colocation-signals.md` C-A3 validation rule).
- **30kW+/rack density** — 50-100kW current standard for AI, 250-600kW target by 2026.
- **Hyperscaler customer concentration** — when public colo discloses single tenant >40% of revenue (per `colocation.md` lines 491-495).
- **AI-specific buildout language** in marketing — "AI factory," "AI campus," "AI-ready," "GPU-optimized."
- **Anchor lease structure** — 10-15 year terms with tenant-backed financing co-mingled into capex.

### Required signals

`colocation-signals.md` Tier A: **C-A2** (GPU cloud tenant anchor announcement — meeting-ready the week of press release; PRIMARY trigger), **C-A3** (liquid cooling / D2C deployment), **C-A6** (anchor tenant signing — broader than C-A2), **C-A0** (greenfield S2/S3 with AI-ready language).

Tier B: **C-B3** (power capacity uprate / PPA — combined with C-A2 = Tier 1 trigger), **C-B5** (sovereignty / data-residency for regulated AI workloads).

Tier C: **C-C1** (hyperscaler-adjacent <50 miles for cloud on-ramp wedge).

### Disqualifiers

- "AI-ready" marketing without named tenant or facility-specific buildout → MEDIUM signal at best (per C-A3 validation rule and `colocation-signals.md` False Positive Patterns)
- Per-rack/cabinet retail-only sales motion → `Standard - colo` (even if some AI tenants present)
- Operator sells GPU compute itself (not just space to GPU operators) → NeoCloud, not Colo (per `colocation.md` lines 524-529)
- Containerized prefab pods at distributed sites with GPU overlay → `Modular - colo` with AI overlay note in reasoning string

### Anchor companies (mixed geographies, M&A verified 2026-05-14)

**AI-native operators:**
- **Crusoe** — independent. Lancium Clean Campus Abilene TX: 1.2GW expanding 2→8 buildings; $11.6B debt+equity May 2025; 100% leased to Fortune 100 hyperscaler tenant; 100,000 GPUs at completion; $3.4B JV with Blue Owl Capital + Primary Digital Infrastructure Oct 2024; $400M AMD deal; expanding Iceland with atNorth + $175M Victory Park credit facility.
- **Applied Digital** — public (APLD). North Dakota HPC + AI hosting; CoreWeave anchor tenant; bitcoin → AI pivot canonical case.
- **Colovore** — Santa Clara liquid-cooled colo; emerging player per JLL coverage.
- **Prometheus Hyperscale** — emerging US AI buildout per Data Center Construction Market Outlook 2026-31.
- **Lambda** — primarily neocloud (their own GPU cloud) but with colocation overlap; classify carefully — Lambda operating their own racks is `AI Signals - colo` only if they're the LANDLORD; if Lambda IS the tenant, the colo hosting Lambda is the `AI Signals - colo` account.

**Retrofitted/hybrid operators:**
- **Aligned Data Centers** — DeltaFlow liquid cooling Jan 2024; pending sale to BlackRock GIP + MGX + AIP at $40B (Oct 2025 announce, H1 2026 close from Macquarie). Hyperscale Wholesale PRIMARY but AI-tenant overlay tips for manual review.
- **Vantage Data Centers** — Frontier 1.4GW Texas supports 250kW+ racks with liquid cooling; expected hyperscaler anchor named in 2026; manual review when named.
- **EdgeConneX** — EQT AI investing strategy 2024 + Jakarta 200MW+ campus.
- **Iron Mountain Data Centers** — MODs (modular dedicated wholesale + AI-ready buildouts in Phoenix/Denver).
- **NTT Global Data Centers Americas** — 20% YoY 2024; sub-segment overlap.
- **Stack Infrastructure** — IPI Partners / Blue Owl majority; $3B green financing Aug 2024; hyperscale + AI overlay.

**International AI Signals:**
- **AirTrunk** — Blackstone acquired AU$24B (US$15.6B) 2024; APAC hyperscale + AI.
- **Yondr** — UK-based hyperscale + AI.
- **STT GDC, NEXTDC, GDS Holdings** — APAC hyperscale operators with AI overlay.

### Confusable-with comparison

| Compared to | Distinguishing test |
|---|---|
| `Hyperscale Wholesale - colo` | AI Signals has NAMED GPU/neocloud tenant (Lambda/Crusoe/Nebius/Nscale/etc); Hyperscale Wholesale has hyperscaler anchor (AWS/Azure/Google/Meta/Oracle). When operator has BOTH (Vantage, Aligned, NTT, Iron Mountain, EdgeConneX) → manual review; default to larger book. |
| `Standard - colo` | AI Signals has named GPU tenant + liquid cooling + 30kW+; Standard may have liquid cooling deployments but no named anchor GPU tenant. |
| `Modular - colo` | AI Signals scales via campus power upgrades; Modular scales via prefab pods at distributed partner power sites. |
| NeoCloud `Crypto to AI - Neoclouds` | **CRITICAL DISTINCTION** — IREN leasing power capacity to Microsoft = AI Colo landlord model (`AI Signals - colo`). IREN's own GPU cloud product = Neocloud (`Crypto to AI - Neoclouds`). When the same company sells BOTH compute AND landlord-style power lease (IREN, Core Scientific) → primary revenue model wins. Per `colocation.md` line 528: "Does both: lead with primary revenue model. If unclear, colo angle is usually safer." |
| NeoCloud `Large Scale GPU - Neocloud` | Lambda/Crusoe/Nebius/CoreWeave when operating their OWN facilities = Neocloud not AI Colo. They become AI Colo's TENANT, not the AI Colo account. |

### Selling angle

Lead with **deterministic-paths-for-AI-tenants frame** per `colocation.md` lines 463-464. Inference is now 55% of AI spend (2026), projected 75-80% by 2030 (per line 522). H100 rental prices crashed 64-75% Q4'24→Q1'26 ($8-10 → $2.99/hr). Token-latency SLAs replace bulk-training egress.

Core message: "Deterministic paths between your AI tenants' clusters. Multi-region GPU-to-GPU, GPU-to-cloud, and inter-facility failover — as a marketed SLA, not a best-effort cross-connect."

Tenant concentration reframe (per `colocation.md` lines 491-498): "MaiaEdge lets you onboard 2-3 additional hyperscalers into the same physical building by guaranteeing them isolated network paths from your existing tenant. Tenant diversification with the same capex base. Concentration risk declines; revenue per MW goes up." Pair with power-queue leverage play.

### HubSpot fields R1/R2 must populate

| Field | AI Signals - colo value |
|---|---|
| `customer_segment` | `Data Center Colo Provider` |
| `company_sub_segment` | `AI Signals - colo` |
| `account_tier` | Tier 1 default (anchor-tenant AI operators are highest-priority) |
| `hs_is_target_account` | `true` |
| `recent_news_or_trigger_event` | Heavy stamp from C-A2/A3/A6 signal scan |
| `infrastructure_profile` | Free-text: named GPU/neocloud tenants, liquid cooling type, rack density kW, anchor lease term, facility MW capacity, total fleet MW |
| `segmentation_confidence` | `high_90` requires named GPU tenant + liquid cooling + 30kW+ explicitly disclosed |
| `last_enriched_date` | Stamped only on full pipeline pass + Completeness Gate pass |

### Signal source coverage

Robust tier: NVIDIA newsroom + GTC press (NAMES colo partners in AI factory announcements — high-conviction source for AI Signals), Crusoe newsroom (multi-press-release weekly cadence), DCF AI Buildouts + AI Workloads tags, DCD AI tag, hyperscaler announcement feeds (AWS / Azure / Google Cloud blog new-region maps to anchor signals), operator press releases (Lambda / Crusoe / Nebius / Applied Digital).

Medium tier: AI Infrastructure Summit agenda, GTC speaker lists, Crunchbase Data Center tag + Crunchbase News funding events.

### Contact personas

**Anchor-tenant model (Applied Digital / Crusoe / IREN archetype):**
- **Chief Network Engineer / VP Infrastructure** (PRIMARY technical buyer) — owns the network SLA being marketed to GPU tenants.
- **CFO** (CO-SIGNATORY) — material because MaiaEdge OpEx embeds into tenant MSA pricing; anchor lease economics depend on this.
- **CTO** — strategic validation, particularly for first-time-AI operators.

**AI-retrofit regional (traditional colo with AI tenants):**
- VP Interconnection + VP Data Center Operations (same as Standard, but with AI-specific talk track per `colocation.md` line 463 AI variant).

**Per `colocation.md` lines 460-461:** AI Signals is a dual-buyer sale — technical (Chief Network Engineer) + financial (CFO). This is materially different from Standard (single buyer: VP Interconnection) and Modular (single buyer: Founder/COO).

### Confidence scoring rules

- `high_90`: named GPU cloud tenant in operator press OR tenant's own filing + liquid cooling tied to specific facility + 30kW+ disclosed.
- `medium_7089`: 2 of 3 above; named tenant + liquid cooling but no density disclosed; OR 30kW+ with AI marketing but no named tenant.
- `low_5069`: "AI-ready" marketing without facility specifics; liquid cooling in product literature but not deployed; ambiguous between Standard with AI tenants and AI Signals.
- `manual_review_required`: operator straddles Hyperscale Wholesale + AI Signals (Vantage, Aligned, NTT, Iron Mountain, EdgeConneX); crypto-to-AI pivot with unclear landlord vs operator status; tenant churn rumored.

### Industry sources for ongoing validation

NVIDIA newsroom + GTC press, Dell'Oro Group AI Datacenter Liquid Cooling Market reports ($3B in 2025, $7B forecast by 2029), JLL AI-specific colo coverage, CBRE AI demand reporting, Synergy Research Hyperscale Market Tracker, Crusoe / Applied Digital / IREN press releases, Lambda / Nebius / Nscale / Together AI / Fluidstack tenant announcements, Data Center Frontier AI Buildouts tag.

---

## `Modular - colo`

### Definition (sharpened — 4 distinguishing axes)

| Axis | Modular - colo |
|---|---|
| Deployment scale per tenant | Sub-MW per pod typical; some MW-scale containerized products (Armada Leviathan) emerging |
| Anchor tenant concentration | Variable — pod-by-pod tenant relationships; some operators have 1-2 GPU tenants per pod; site-count growth dilutes concentration |
| Sale unit | Per-pod + power + connectivity; growth model is site-count NOT campus-size (per `colocation.md` lines 467-469, 532-542) |
| AI vs general workload | Mixed — modular DC build typology is segment-agnostic, but in 2025-2026 most NEW modular deployments are GPU-tenant-driven (Crusoe Spark "modular edge compute at hundreds of kilowatts per deployment" per `colocation.md` line 555) |

### Quantitative markers

- **Pod count > facility count** — operator scales by adding sites not expanding campuses
- **Partner power site model** — deploys at renewable energy sites, utility substations, telco huts, or industrial locations (NOT operator-built shells)
- **Prefab/containerized build typology** — ISO containers, skid-mounted enclosures, semi/fully-prefab modules per 451 Research definition
- **Sub-MW to single-MW per pod** typical; some MW-scale (Armada Leviathan)
- **Distributed metro/edge footprint** — 5+ pods across secondary/tertiary metros
- **Power range:** "hundreds of kilowatts to single-megawatts per deployment" (Crusoe Spark thesis)

### Required signals

`colocation-signals.md` Tier A: **C-A0** (greenfield S2/S3 — modular operators often skip permitting if deploying inside existing partner sites; flag low-confidence detection), **C-A1** (site count 1→2 transition — CRITICAL trigger for modular as well as standard; first-multi-site fabric decision is the moment).

Tier C: **C-C5** (modular / edge pod deployment at new power site — explicit Modular trigger per `colocation-signals.md` line 211: "Nodiac-type operators adding pod #N+1 — fresh window between pod #1 and pod #2").

Cross-segment metro-edge diffusion trend (per `colocation.md` line 555): regional colos with sub-MW to mid-MW footprints in DFW/Columbus/Atlanta/Phoenix/Chicago = modular delivery point if they can offer deterministic paths between distributed inference sites.

### Disqualifiers

- Single large campus / no distributed deployment model → `Standard - colo` or `Hyperscale Wholesale - colo`
- Operator sells GPU compute (not just power/space) → NeoCloud (Duos Edge AI archetype per `colocation.md` line 527)
- Equipment vendor only (Vertiv / Schneider / Dell selling prefab modules) → EXCLUDE (not an operator; supplier)
- Single-site startup with one prefab deployment → too early; revisit at site #2 announcement

### Anchor companies (mixed geographies, M&A verified 2026-05-14)

**Operator-side modular colos:**
- **Nodiac** — modular containerized DCs at renewable energy sites, 500+ site pipeline, 800+ MW per `colocation.md` line 526. Canonical anchor.
- **EdgePresence** — acquired by Ubiquity 2023; small edge pods scalable to limited spaces.
- **Armada** — containerized edge ($131M raise + Leviathan MW-scale launch 2025); deployments with Tampnet (offshore oil rigs), US Navy South Carolina, Aramco Saudi Arabia, Newlab Detroit/Riyadh.
- **DataBank** — modular edge data center platform within its 60+ DC portfolio (Modular delivery within Standard operator identity; manual review for sub-segment assignment).
- **Colony Compute** — modular DC operator per `colocation.md` line 532.
- **Crusoe Spark** — modular-edge-compute thesis publicly stated April 2026; not a separate company but a product line.
- **AtlasEdge** — DigitalBridge portfolio; European edge pods.

**Adjacent / classification-ambiguous:**
- **Compass Datacenters** — uses prefab/modular BUILD methodology but is a Hyperscale Wholesale operator (Brookfield/Ontario Teachers 2025 acquisition). Build method ≠ operator archetype. Classify as `Hyperscale Wholesale - colo`.
- **Duos Edge AI** — sells GPU capacity → Neocloud, not Modular colo.

### Confusable-with comparison

| Compared to | Distinguishing test |
|---|---|
| `Standard - colo` | Standard has 1-10 large facilities; Modular has 5-500+ small pods. Standard sells per-rack from MMR; Modular sells per-pod at distributed sites. |
| `AI Signals - colo` | AI Signals has named GPU tenant at campus-scale; Modular has named GPU tenant per pod with site-count growth model. Significant overlap when modular operator anchors GPU tenants (Crusoe Spark, Nodiac with neocloud tenants). |
| `Hyperscale Wholesale - colo` | Compass uses modular BUILD method but operates Hyperscale Wholesale (single-tenant hyperscaler campuses). Test: does growth scale by pod-at-partner-site (Modular) or campus-build-to-suit (HW)? |
| NeoCloud `Crypto to AI - Neoclouds` | Modular operator hosts GPU tenants in its pods; Crypto-to-AI neocloud operates GPUs in its own pods. Test per `colocation.md` line 525: "are they selling space, or selling compute?" |
| Equipment vendors | Vertiv / Schneider / Dell / Eaton / ABB / Stulz / Rittal sell prefab modules to operators — EXCLUDE as suppliers, not in ICP. |

### Selling angle

Lead with **first-multi-site fabric decision frame** per `colocation.md` lines 469, 540-541. Core message: "Every new pod at a new power site is either a separate networking project or a day-one join to your fabric. Make it the second one. One fabric across every pod, whatever the location."

Tenant-portability angle: "Your GPU tenants don't want to care which of your pods they're in. One fabric across all of them makes that true."

Inter-pod connectivity angle: "Power is solved at the site level. Connectivity between sites is the part that decides whether you keep the tenant."

### HubSpot fields R1/R2 must populate

| Field | Modular - colo value |
|---|---|
| `customer_segment` | `Data Center Colo Provider` |
| `company_sub_segment` | `Modular - colo` |
| `account_tier` | **Tier 1 default** (per `05 - Sub-segment definitions.md` line 331: "Update Modular Colo default to Tier 1 per Cooper's framework correction; was Tier 2 in framework signoff doc; resolved to Tier 1") |
| `hs_is_target_account` | `true` |
| `recent_news_or_trigger_event` | Stamped on C-A1 and C-C5 site-count transitions and pod deployments |
| `infrastructure_profile` | Free-text: pod count, partner-site model (renewable / industrial / telco hut), pod power range, geographic distribution, primary tenant types (GPU vs enterprise edge) |
| `segmentation_confidence` | `high_90` requires explicit modular/containerized build typology + distributed site footprint + site-count growth model |
| `last_enriched_date` | Stamped only on full pipeline pass |

### Signal source coverage

Robust tier: Operator press releases (Nodiac, Armada, EdgePresence/Ubiquity), DCD Edge tag, DCF Edge Computing, Bisnow Data Center (modular DC announcements typically surface here).

Medium tier: Crunchbase News (modular DC funding rounds), Edge Industry Review, EdgeIR Modular DC service directory.

Excluded: Equipment-vendor press (Vertiv/Schneider/Dell/Stulz) when describing module SALES rather than operator deployments — equipment-vendor signals don't predict operator buying-windows.

### Contact personas

**Early-stage (<50 employees, 1-2 pods):**
- **Founder / CEO** (PRIMARY) — centralized decision authority; technical delegation often to systems integrators or hyperscaler partners.
- **COO** — operational owner if dual-leader structure.

**Mid-growth (50-250 employees, 3-10 pods):**
- **COO** + **VP Engineering** + **Head of Infrastructure** — three-way technical/operational consensus typical at this scale.

**Per `colocation.md` lines 471-473:** Modular sells to founder/COO. NOT a VP Interconnection sale (those are Standard). NOT a Chief Network Engineer + CFO sale (those are AI Signals). This makes the contact discovery motion materially different — find the FOUNDER, not the VP layer.

### Confidence scoring rules

- `high_90`: explicit modular/containerized build language + distributed multi-site footprint + site-count growth narrative on website / press / Crunchbase profile.
- `medium_7089`: 2 of 3 above; OR pod-based deployment confirmed but site count <3.
- `low_5069`: single modular deployment without distributed-site growth narrative; OR DataBank-style operator with modular "platform" inside primarily-Standard identity.
- `manual_review_required`: operator straddles Modular and AI Signals (Crusoe Spark, Nodiac with named GPU tenants); equipment-vendor partnership-driven deployment unclear whether operator or vendor owns customer relationship.

### Industry sources for ongoing validation

451 Research Datacenter KnowledgeBase (prefabricated modular DC definition + global database), InsightAce Analytic Prefabricated Modular Data Center Market reports, Markets and Markets Modular Data Center Market, Edge Industry Review Modular DC service directory, ENCOR Advisors Modular Data Center Ultimate Guide (2025), Vertiv / Schneider / Dell modular product literature for operator-partner identification, DCD Edge tag.

---

## `Hyperscale Wholesale - colo` (NEW — not yet in cheatsheet)

### Definition (sharpened — 4 distinguishing axes)

| Axis | Hyperscale Wholesale - colo |
|---|---|
| Deployment scale per tenant | **10MW+ standard; 100MW+ campuses common; up to 1.4GW (Vantage Frontier) or 5GW+ portfolio scale (QTS at 4.75GW, Aligned at 5GW+, Compass at 1.25GW pipeline)** |
| Anchor tenant concentration | **VERY HIGH — 3-10 anchor tenants per portfolio; 60%+ revenue from AWS / Azure / Google / Meta / Oracle hyperscalers; build-to-suit or shell-and-core lease structures** |
| Sale unit | **Per-MW with 5-15 year terms; ROFR / ROFO arrangements with anchor tenants; $/kW/mo wholesale band $195.94/kW/mo national avg, $200+/kW/mo primary markets, 10MW+ NoVA +13.8% YoY 2025 (CBRE H2 2025)** |
| AI vs general workload | **Hyperscaler cloud capacity primarily — not GPU-tenant-specific. But: recent buildouts (Vantage Frontier 250kW+ racks + liquid cooling, Aligned DeltaFlow Jan 2024, Iron Mountain MODs, Stack $3B green financing) increasingly AI-ready in design even when not GPU-tenant-named** |

### Quantitative markers

- **10MW+ single deployments standard** (deployment scale is the sharpest distinguishing axis vs. Standard)
- **5-15 year terms** with ROFR/ROFO clauses (vs. Standard 1-3 year, AI Signals 10-15 year tenant-backed)
- **$2k-$3.5k/kW pricing band** per `05 - Sub-segment definitions.md` line 340 (validate against CBRE H2 2025: $195.94/kW/mo retail, premium for wholesale primary; pricing shifted UPWARD 2024-26 due to power constraints — per file 05 line 340 verify before publishing)
- **60%+ revenue from hyperscaler tenants** (AWS / Azure / Google / Meta / Oracle / Apple)
- **3-10 anchor tenants per portfolio** (vs. retail's hundreds-to-thousands)
- **Portfolio power capacity 100MW-5GW** (QTS 4,752 MW disclosed; Aligned 5GW+ operational+planned)

### Required signals

`colocation-signals.md` Tier A: **C-A6** (anchor tenant signing — broader than C-A2 GPU-specific; hyperscaler build-to-suit lease IS C-A6's primary fire pattern; SEC 8-K Item 1.01 + tenant's own announcement = HIGH confidence), **C-A7** (M&A / PE recap — Hyperscale Wholesale operators are PE-target-rich; Blackstone QTS / KKR+GIP CyrusOne / Brookfield+OTPP Compass / DigitalBridge+IFM Switch / BlackRock+MGX+AIP Aligned pending — all $10B+ transactions), **C-A0** (greenfield S2/S3 at hyperscale buildout scale).

Tier B: **C-B1** (8-K interconnection language for public REITs), **C-B3** (PPA / power capacity uprate — critical for hyperscale buildouts), **C-B5** (sovereignty — hyperscalers asking colo to prove jurisdiction for AI Act compliance).

### Disqualifiers

- Sells primarily per-rack or per-cabinet → `Standard - colo`
- Named GPU/neocloud tenant (Lambda, Crusoe, etc.) anchoring the buildout → `AI Signals - colo`
- Sub-10MW typical deployment size → `Standard - colo`
- Mainly serves retail / SMB / mid-market → `Standard - colo`
- Containerized prefab pods at distributed partner power sites → `Modular - colo`

### Anchor companies (target 10-15, M&A verified 2026-05-14)

**US-headquartered hyperscale wholesale:**
- **QTS Wholesale** — Blackstone $10B take-private 2021 (BREIT + BIP). 4,752 MW disclosed.
- **CyrusOne** — KKR + GIP $15B take-private 2022 ($90.50/share). 55+ DCs. Note 10-hour 2025 outage testing sponsors.
- **Compass Datacenters** — Brookfield Infrastructure + Ontario Teachers acquired March 2025 from RedBird + Azrieli. 1.25GW pipeline; 6 hyperscale DCs ABS securitization $830M Phoenix + Toronto.
- **Vantage Data Centers** — DigitalBridge majority + Silver Lake $6.4B JV 2024. Frontier $25B Texas mega-campus 1.4GW, 1,200 acres, 3.7M sqft, supports 250kW+ racks, first building H2 2026, LEED-pursuing.
- **Aligned Data Centers** — pending sale to BlackRock GIP + MGX + AIP at $40B EV (announced Oct 2025; H1 2026 close from Macquarie 2018-2026 ownership). DeltaFlow liquid cooling Jan 2024. 5GW+ operational/planned, 50 DCs US/MX/BR/CL/CO.
- **Stack Infrastructure** — IPI Partners / Blue Owl majority. $3B green financing Aug 2024.
- **EdgeConneX** — EQT Infra acquired 2020 (grew 20x); Sixth Street minority 2024. 80 DCs in 50+ markets across N.America, Europe, APAC, S.America. Jakarta 200MW+.

**Equinix split:**
- **Equinix xScale** — Equinix's hyperscale-wholesale JV with GIC + CPP (37.5% / 37.5% / 25% Equinix; >$15B JV expansion 2024 to US, on top of pre-2024 JV portfolio $7.5B+ in UK / Japan / France / Brazil / Korea; also $600M JV with PGIM for Silicon Valley + Sydney first xScale opened with PGIM). Operates parallel to Equinix's core retail IBX business which is `Standard - colo`.

**Iron Mountain / DataBank wholesale books:**
- **Iron Mountain Data Centers** wholesale book (1.3GW global, MODs for dedicated wholesale, geothermal cooling, 100% renewable; Phoenix/Denver/Columbus/San Antonio/Boise 2025 buildouts).
- **NTT Global Data Centers Americas** — 20% YoY growth 2024.
- **DataBank** wholesale extensions (less primary than retail identity but Plano DFW3 expansion 2025 + Pyramid Campus Q2 2025 expansion track wholesale).

**International hyperscale wholesale:**
- **AirTrunk** — Blackstone AU$24B (US$15.6B) 2024 acquisition. APAC anchor.
- **GDS Holdings** — public (GDS). China + SE Asia hyperscale.
- **Global Switch** — pan-European wholesale.
- **STT GDC** (ST Telemedia Global Data Centres) — APAC pan-regional.
- **NEXTDC** — Australia.
- **Data4** — France/EU.
- **Yondr** — UK pan-EU AI-wholesale focus.

### Confusable-with comparison

| Compared to | Distinguishing test |
|---|---|
| `Standard - colo` | Deployment scale: >10MW typical = HW; <300kW = Standard. Term: 5-15yr ROFR = HW; 1-3yr = Standard. Tenant count: 3-10 anchors = HW; hundreds-to-thousands = Standard. |
| `AI Signals - colo` | HW sells to hyperscaler cloud capacity (AWS/Azure/Google); AI Signals sells to named GPU/neocloud tenants (Lambda/Crusoe/Nebius). Some operators have BOTH books (Vantage, Aligned, NTT, Iron Mountain, EdgeConneX). Manual review default. |
| `Modular - colo` | Compass uses prefab BUILD method but operator archetype is HW (single-tenant hyperscaler campuses). Test: pod-at-partner-site growth (Modular) vs. campus-build-to-suit (HW). |
| NeoCloud `Sovereign AI Clouds` | HW landlord operator; Sovereign AI Cloud is the tenant. HUMAIN / Center3 / Tonomus / G42 lease wholesale capacity from HW operators (often via subsidiaries); the operator is HW, the cloud is the tenant. |

### Selling angle

**Critical positioning shift vs. retail-side colo selling motion** — Hyperscale Wholesale operators sell SPACE and POWER. Hyperscaler tenants bring their own orchestration. Selling MaiaEdge directly to the wholesale operator is the wrong sale.

**Instead (per `05 - Sub-segment definitions.md` line 375):** "Hyperscale Wholesale operators sell space and power. Hyperscaler tenants bring their own orchestration. So the MaiaEdge fit isn't with the wholesale operator directly — it's with the operator's non-hyperscaler anchor tenants who need cross-cloud fabric without operating it. Position MaiaEdge as the value-add: 'build a richer in-building marketplace by giving your non-hyperscaler tenants instant private paths to Azure / GCP.'"

In other words: Hyperscale Wholesale operators are LANDLORDS for MaiaEdge's actual targets (their tenants). The MaiaEdge sale through a HW account is the operator helping convince their non-hyperscaler tenants to onboard MaiaEdge, or the operator offering MaiaEdge as part of an enriched in-building marketplace to attract mid-tier wholesale (enterprise service provider) tenants. Tenant concentration reframe still applies: HW operators are increasingly disclosing single-tenant concentration risk and would value tools that diversify their tenant base.

### HubSpot fields R1/R2 must populate

| Field | Hyperscale Wholesale - colo value |
|---|---|
| `customer_segment` | `Data Center Colo Provider` |
| `company_sub_segment` | `Hyperscale Wholesale - colo` |
| `account_tier` | Tier 1 (large public + PE-portfolio HW operators) / Tier 2 (regional or single-campus HW) |
| `hs_is_target_account` | `true` for Tier 1 |
| `recent_news_or_trigger_event` | Heavy stamp from C-A6 anchor tenant signings + C-A7 M&A/PE recaps |
| `infrastructure_profile` | Free-text: total MW capacity, named hyperscaler tenants if public, campus sizes, anchor lease durations, ROFR/ROFO clauses, sponsor ownership |
| `segmentation_confidence` | `high_90` requires explicit "wholesale" or "hyperscale" operator self-identification + named hyperscaler anchor + 10MW+ deployment evidence |
| `last_enriched_date` | Stamped only on full pipeline pass |

### Signal source coverage

Robust tier: SEC 8-K Item 1.01 + S-4 + 2.01 (StockTitan mirror + EDGAR backup) for public HW REITs (DLR, EQIX, IRM, DBRG, COR-equiv) + acquirer side, sponsor press releases (Blackstone, KKR, GIP, Brookfield, DigitalBridge, IPI, Stonepeak, EQT, Macquarie, BlackRock GIP, MGX), DCF Hyperscale tag + Transactions section, DCD M&A tag, hyperscaler announcement feeds (AWS / Azure / Google new region / new AZ).

Medium tier: Infrastructure Investor, Bisnow Data Center, PitchBook public pages, Mergr.

### Contact personas

**Per `05 - Sub-segment definitions.md` line 375 reframe + this scope:**

**Operator-side (the HW account itself):**
- **VP Sales / Head of Wholesale Sales** — owns the anchor-tenant relationship and the marketplace/ecosystem expansion narrative.
- **VP Real Estate / VP Asset Management** — capital decisions, but rarely the MaiaEdge buyer.
- **CTO / CIO of the operator** — technical validation but not the buyer because the tenant brings the network stack.

**Tenant-side (the actual MaiaEdge buyer through an HW account):**
- **Tenant CFO** — when the MaiaEdge offer is "lower your in-building cross-cloud connectivity cost via the operator's marketplace."
- **Tenant VP Infrastructure / VP Network** — when the offer is technical (private paths to Azure/GCP without operating their own orchestration).

**Per scope rubric:** Hyperscale Wholesale sells to VP Sales (operator-side, marketplace expansion conversation) + tenant CFO (when MaiaEdge is in-building marketplace product). This is materially different from Standard (VP Interconnection at operator), AI Signals (Chief Network Engineer + CFO at operator), and Modular (Founder/COO at operator).

### Confidence scoring rules

- `high_90`: explicit wholesale/hyperscale operator self-id + named hyperscaler anchor tenant (AWS/Azure/Google/Meta/Oracle/Apple) + 10MW+ deployment confirmed + 5-15yr lease terms disclosed.
- `medium_7089`: 2 of 3 above; OR named PE sponsor (Blackstone/KKR/GIP/Brookfield/DigitalBridge/Stonepeak/IPI/I Squared/Macquarie/BlackRock GIP/EQT) holds the asset + wholesale revenue mix unclear.
- `low_5069`: 1 of 3 above; OR operator straddles Standard + HW (Equinix, IRM, NTT, DataBank, Vantage, Aligned) — default to manual review.
- `manual_review_required`: Equinix-class (need sub-record decision for xScale split), Vantage / Aligned / NTT / Iron Mountain / EdgeConneX (split-book operators), or M&A activity within 12 months not yet integrated.

### Industry sources for ongoing validation

Synergy Research Group Hyperscale Market Tracker + Colocation Market Tracker (Wholesale = Hyperscale + Enterprise/Service Provider sub-view), Structure Research Global DCI Report (64% hyperscale share 2025; 16.9% 5yr CAGR), Dell'Oro Group Data Center Reports, JLL Global Data Center Outlook (semiannual), CBRE North American Data Center Trends (wholesale pricing primary), dgtlinfra Top 250 Data Center Companies (annual), Data Center Frontier Transactions section, Data Center Dynamics M&A tag, Infrastructure Investor, PitchBook, SEC EDGAR (8-K Items 1.01/2.01/5.02, S-4).

---

## Cross-cutting summary for Cooper

### Ambiguity flags requiring Cooper decision

1. **Modular - colo industry recognition.** The build typology IS industry-recognized (451 Research, $34B+ market by 2025, major equipment-vendor category). The operator archetype is NOT formally named by Synergy / Structure / JLL / CBRE — this is MaiaEdge framing on top of industry build typology. Reasoning strings in classifier output must note this explicitly. (Documented in top section under "Is Modular - colo industry-recognized?")
2. **Equinix xScale handling.** Three options: (A) single record + reasoning string only, (B) parent + child records, (C) parent record only with permanent manual review flag. Recommend option (B) with explicit linkage and territory-ownership split (parent record carries rep ownership; xScale child carries hyperscaler-tenant deal pipeline). Same convention should apply to Vantage AI campuses, Iron Mountain MODs, Aligned post-BlackRock close.
3. **Crypto-to-AI overlap.** Phase 3.5 file 05 says "AI colo (landlord model)" for IREN leasing power to Microsoft. `colocation.md` line 528 reinforces: "lead with primary revenue model. If unclear, the colo angle is usually safer." But the cheatsheet places IREN/Core Scientific in NeoCloud `Crypto to AI - Neoclouds` per HubSpot enum. Policy recommendation: when the SAME company sells both compute (GPU cloud product) AND landlord-style power lease, classify by majority revenue mix; default to `AI Signals - colo` if landlord book >50%, default to `Crypto to AI - Neoclouds` if compute book >50%. IREN currently has the Microsoft landlord deal + its own GPU cloud product running in parallel → manual review.
4. **AI Signals vs Hyperscale Wholesale boundary.** Manual-review trigger needed when operator has BOTH books. Recommended trigger: `manual_review_required` when any TWO of these conditions: (a) named GPU/neocloud tenant in any facility, (b) named hyperscaler anchor in any facility, (c) liquid cooling deployed AND multi-MW wholesale terms disclosed. Default classification under manual review = larger book by published revenue mix; if revenue mix unpublished, default to `Hyperscale Wholesale - colo`.

### Anchor changes (vs. prior versions)

- **Switch removed from Hyperscale Wholesale** (confirmed; Switch is `Standard - colo` per Tier 5 retail-enterprise positioning + DigitalBridge/IFM acquisition language).
- **xScale, EdgeConneX, DataBank, Iron Mountain Data Centers added to Hyperscale Wholesale** (confirmed via Equinix JV announcements, EQT-EdgeConneX, DigitalBridge-DataBank, Iron Mountain wholesale MODs language).
- **Aligned status: Macquarie ownership confirmed for current legal state**; BlackRock GIP + MGX + AIP $40B deal announced Oct 2025, close H1 2026 — per Cooper's M&A policy classify per current legal state, reassign post-close.
- **Compass clarified as Hyperscale Wholesale not Modular** (uses prefab build method but operates HW campus model; Brookfield + Ontario Teachers 2025 acquisition).
- **CoreSite confirmed as Standard - colo** under American Tower since 2021 $10.1B acquisition.
- **AirTrunk confirmed as Hyperscale Wholesale** (Blackstone 2024 acquisition AU$24B / US$15.6B).

### Taxonomy gaps

- No published industry market-share table for Modular operator archetype. Quarterly RevOps anchor refresh per file 05 line 653 should source anchor companies via Crunchbase + DCD Edge + EdgeIR + Edge Industry Review service directory, not Synergy / Structure.
- Hyperscale Wholesale operators with sub-MW AI overlay (Iron Mountain MODs, DataBank modular platform) lack a clean classifier — defaulting to manual review is correct.
- Greenfield enum value (`Greenfield`, 0 records post-migration per `00-hubspot-enum-verification.md` line 73) functions as pre-classification state marker. Recommend archiving in next Phase 1.6 sweep; segment-classification skill should never output `Greenfield` as a final value.
