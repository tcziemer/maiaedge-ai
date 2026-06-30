# MaiaEdge HubSpot Property Schema  -  Unified Reference

> Last updated: March 2026
> CRM Instance: app-na2.hubspot.com | Hub ID: 242063281
> **This is the single source of truth for all HubSpot property mappings.** All skills, plugins, and enrichment workflows reference this file.

---

## 1. Territory Model  -  Owner Assignments

The US territory splits on the Mississippi River. Account ownership is determined by **HQ state**.

### Owner IDs (Active, Sales-Relevant)

| Owner | HubSpot Owner ID | Role | Territory |
|-------|----------------:|------|-----------|
| **Tim Lieto** | `161889085` | AE, East | 30 US states |
| **Ken Cunningham** | `162339176` | AE, West | 20 US states + DC |
| **Timothy Ziemer** | `159350430` | CRO / International | All non-US |
| Cooper Kennedy | `160267902` | RevOps | Internal/unassigned |
| Abilash Menon | `159974715` | CEO | Strategic accounts |
| Hannah Roberts | `159875488` | (Inactive  -  replaced by Ken) |  -  |

### State-to-Owner Mapping

**Tim Lieto (East  -  30 states):**
`AL, AR, CT, DE, FL, GA, IA, IL, IN, KY, LA, MA, MD, ME, MI, MN, MO, MS, NC, NH, NJ, NY, OH, PA, RI, SC, VA, VT, WI, WV`

**Ken Cunningham (West  -  20 states + DC):**
`AK, AZ, CA, CO, DC, HI, ID, KS, MT, ND, NE, NM, NV, OK, OR, SD, TN, TX, UT, WA, WY`

**Tim Ziemer (International):**
All non-US countries

### Multi-State Operator Rules

| Scenario | Resolution |
|----------|------------|
| HQ in known state | HQ state determines owner |
| HQ unknown | First meaningful engagement wins (must log in HubSpot) |
| Non-US HQ | Tim Ziemer (International) |
| Strategic exception | Leadership can reassign with documented reason |

### Key Markets by Territory

| Territory | Top Colo Markets | Key Fiber | Carrier HQs |
|-----------|------------------|-----------|-------------|
| **Tim Lieto** | NoVA (#1), Chicago (#3), Atlanta (#5) | altafiber (OH), Hoosier Net (IN), Bluebird (MO/IL) | Verizon (NY), Lumen (LA), Frontier (CT), Windstream (AR) |
| **Ken Cunningham** | Dallas (#2), Phoenix (#4), Austin (#6), Silicon Valley, Nashville | Texas CLECs, SDN Communications (SD), ALLO (NE/CO) | T-Mobile (WA), AT&T (TX) |

---

## 2. Customer Segment (`customer_segment`)

**Property name:** `customer_segment`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | ICP? | Priority | Notes |
|----------------|--------------|------|----------|-------|
| `Data Center Colo Provider` | Colocation Operator | ✅ | 1 | Core ICP  -  owns DC facilities, meet-me rooms |
| `Fiber Operator` | Fiber Operator (Tier 2/Regional) | ✅ | 2 | Owns >500 route miles, sells dark/lit fiber |
| `Network Operator(Tier 1 / VNO)` | Network Operator (Tier 1) | ✅ | 3 | Tier 1/2 carrier, 10+ states, >2K employees |
| `MSP/Aggregator` | MSP/Aggregator | ✅ | 4 | Aggregates 3+ upstream carriers, <10% owned infra |
| `NeoCloud` | NeoCloud | ✅ | 1-2 | AI cloud infrastructure (Lambda Labs, Nebius, CoreWeave, Crusoe  -  Crusoe routes to `Crypto to AI - Neoclouds` sub-segment per BTC mining heritage). |
| `Enterprise-CustomerSegment` | Enterprise | ✅ | 5 | Multi-DC enterprises with in-house network engineering teams. Four sub-segments: Financial Services, Healthcare Systems, Retail and Distribution, Outsourcing Services. Promoted to ICP May 2026; lowest-priority ICP but qualified and sellable. Anchor: Meijer. |
| `Partner Target` | Partner Target | ❌ |  -  | Route to Partnerships |
| `Other` | Other | ❌ |  -  | Needs classification |
| `Unknown` | Unknown | ❌ |  -  | Needs enrichment |
| `Flagged for deletion` | Flagged for deletion | ❌ |  -  | Pending removal from CRM |

### Import Mapping Quick-Reference

When building HubSpot import files, use the **Internal Value** column exactly:

```
customer_segment = "Data Center Colo Provider"    ← Colo
customer_segment = "Fiber Operator"               ← Fiber
customer_segment = "Network Operator(Tier 1 / VNO)" ← Network Operator
customer_segment = "MSP/Aggregator"               ← MSP/Aggregator
customer_segment = "NeoCloud"                     ← NeoCloud
customer_segment = "Enterprise-CustomerSegment"   ← Enterprise (multi-DC ICP, pair with one of four Enterprise sub-segments)
```

> ⚠️ **CHANGE (March 2026):** `AI - Colocation Operator` is NO LONGER a main segment. AI colos now use `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. The `AI - Colocation Operator` value still exists in HubSpot but should not be used for new imports.

---

## 2.1 Flagged for Deletion Reason (`flagged_for_deletion_reason`)

**Property name:** `flagged_for_deletion_reason`
**Object:** Company
**Type:** Multi-line text
**Conditional on:** `customer_segment = "Flagged for deletion"`

The audit companion to the `Flagged for deletion` segment value. Whenever a skill/routine/scheduled task sets `customer_segment = "Flagged for deletion"`, it MUST in the same write populate `flagged_for_deletion_reason` so Cooper can filter the deletion pool by reason and bulk-delete with confidence.

**Write format:** lead with ONE of the 7 canonical reason codes, then a colon and one concrete sentence of evidence. The scannable code lives here; the 2-4 sentence prose rationale stays in `account_brief`. No em dashes inside the reason string - use a colon.

| Reason code (lead with this) | When it applies |
|---|---|
| `Dead domain` | DNS NXDOMAIN / parked / for-sale / persistent destination 4xx-5xx (NOT a proxy block). |
| `Hard junk / non-business` | Non-business or hard-flag category (restaurant, church, school, personal site), junk TLD (.tk/.ml/.ga), spoofed-brand or test record. |
| `D1 disqualified (no reference value)` | Matched a D1 global disqualifier (gov / academic / pure-SaaS / logistics / equipment-vendor, etc.) with NO competitive/partner reference value. If it DOES carry reference value, use `customer_segment = "Other"` instead - not Flagged. |
| `No ICP fit` | Researched but no positive evidence for any of the 6 ICP sub-segments, and not a partner/competitor reference either. |
| `Duplicate (merged)` | Duplicate of an existing record; contacts reassociated to the primary. Cite primary name + record ID. |
| `Defunct / out of business` | Confirmed defunct, ceased operations, or absorbed post-acquisition. Cite the event. |
| `Stalled greenfield` | Greenfield record with no construction progress or relevant signal in 18+ months; web-verified stalled. |

**Examples:**

```
Dead domain: acme-test.tk returns NXDOMAIN; no live site or business entity behind it.
No ICP fit: regional IT staffing firm; no infrastructure ownership and no positive evidence for any ICP sub-segment.
Duplicate (merged): merged into Verizon (record 12345) per R3 dedup; contacts reassociated.
Stalled greenfield: 2024 build announcement, no construction progress or funding in 18+ months; D7 web-verified stalled.
```

**Clear-on-exit (conditional-field hygiene):** if a record moves OFF `customer_segment = "Flagged for deletion"` into any other segment (reclassification / un-flag / upgrade), clear `flagged_for_deletion_reason` to empty in the same write. The reason is conditional on the flag and must never be left stale on a now-active record.

**Writers** (set it alongside the flag): R0 Import Validator, R1 Fresh Enrichment (Path γ + Stage 2 pre-gate fail), R2 Stale Re-Enrichment (RE_ENRICH_FULL + RE_ENRICH_LIGHT + Greenfield auto-migration), R3 Duplicate Accounts, D7 Edge Case Resolution, Mass Re-Enrichment, and the `company-enrichment` / `segment-classification` / `pre-deletion-audit` / `crm-guardian` skills. **Readers** (surface it, never set): R4 Flagged Consolidation, Flagged-for-Deletion Audit, pre-deletion-audit review output.

---

## 2.5 Company Sub-Segment (`company_sub_segment`)

**Property name:** `company_sub_segment`
**Type:** Enumeration (single-select)
**Active values:** 30 (verified via HubSpot MCP 2026-05-14). 3 retired values archived 2026-05-13 (Phase 1.6) - see "Retired" subsection below. `import-processor` rejects writes to retired values.

This field provides granular classification within each main segment. Each value includes the parent segment suffix for clarity. **Internal values are CASE-SENSITIVE - see the Enum Case-Sensitivity Reference appendix.**

For classification logic + per-sub-segment evidence questions + tiebreaker rules, see [`context/account-tiering/sub-segment-qualification.md`](../core/sub-segment-qualification.md) (pointer) -> file 06 (primary source) + [`context/account-tiering/enrichment-protocols.md`](../core/enrichment-protocols.md) (D5 v2 operational layer).

### Network Operator(Tier 1 / VNO) - 5 sub-segments

| Internal Value | Display Label | Description |
|---|---|---|
| `Tier 1 Carrier - Network Op` | Tier 1 Carrier - Network Op | State-protected former incumbents / post-Bell System nationals. $20B+ revenue, 50+ countries, multi-segment activity. AT&T, Verizon, Deutsche Telekom, NTT, Orange archetypes. |
| `Pure Wholesale Carrier - Network Op` | Pure Wholesale Carrier - Network Op | 100% B2B wholesale carriers - capacity/transit/ports to other carriers + hyperscalers. $200M-$5B revenue. Cogent, Arelion, EXA Infrastructure, Hurricane Electric, Sparkle. |
| `Cable MSO Enterprise Division - Network Op` | Cable MSO Enterprise Division - Network Op | Business/enterprise arm of cable parent. Distinct B2B brand, $1.5B+ B2B revenue. Comcast Business, Spectrum Enterprise, Cox Business, Optimum Business. |
| `International Backbone Specialist - Network Op` | International Backbone Specialist - Network Op | Carriers whose primary business is international long-haul / subsea backbone with significant terrestrial component. Tata, PCCW Global, Telstra International, HGC Global, EXA Infrastructure, Sparkle. |
| `Subsea cable operator` | Subsea cable operator | **New 2026-05-14.** Pure-play subsea cable operators with minimal terrestrial backbone. Aqua Comms, Seaborn Networks, BW Digital, Hawaiki, Telxius. No `- Network Op` suffix. |

### Fiber Operator - 6 sub-segments

| Internal Value | Display Label | Description |
|---|---|---|
| `Regional CLEC - Fiber operator` | Regional CLEC - Fiber operator | Multi-state CLECs, PE-backed regional platforms. $120M-$600M revenue, 2K-30K route miles, 3-12 states. Catch-all default for ambiguous mid-size fiber. ~1,008 records post-migration. |
| `Long Haul / Backbone - Fiber operator` | Long Haul / Backbone - Fiber operator | National/multi-national backbones. $500M+ revenue, 1,000+ route miles cross-metro. Lumen (parent overlap), Cogent (boundary), Zayo (post-CCF). |
| `Dark Fiber Specialist - Fiber Operator` | Dark Fiber Specialist - Fiber operator | Primarily dark fiber / wavelength sales. 80%+ revenue from IRUs. FiberLight, Stealth Communications, Allied Fiber, ITS Fiber, Conterra. **Note case mismatch:** internal value uses capital "O" in `Operator`; display label uses lowercase. |
| `Tier 2 National Wholesale - Fiber operator` | Tier 2 National Wholesale - Fiber operator | National or near-national pure wholesale fiber. $300M-$5B revenue, 20K-300K route miles, 80%+ wholesale. Zayo (post-CCF acquisition 2025), Lightpath (Altice + Morgan Stanley Infrastructure JV), Uniti Group (post-Windstream merger 2025-08), EXA Infrastructure (post-Aqua-Comms acquisition 2024). |
| `Regional Cable Operator - Fiber operator` | Regional Cable Operator - Fiber operator | Regional cable companies with growing commercial fiber arms. Parent B2B sub-$1B, 3-22 states. Breezeline, WOW!, Mediacom Business, Midco Business, Cable ONE / Sparklight (borderline). |
| `Municipal / Cooperative - Fiber operator` | Municipal / Cooperative - Fiber operator | Municipal utility fiber, electric co-ops, community-owned, multi-operator consortia. EPB Chattanooga, UTOPIA Fiber, Diamond State Networks. Renamed from `Co-op/consortium` 2026-05-13. |

### Data Center Colo Provider - 4 sub-segments

| Internal Value | Display Label | Description |
|---|---|---|
| `Standard - colo` | Standard - colo | Traditional interconnection colos. Per-rack/per-cabinet sales, high XC volume, hundreds of tenants. Equinix parent, Digital Realty parent, CoreSite, Cologix, Switch. ~318 records post-migration. |
| `AI Signals - colo` | AI Signals - colo | AI-native or AI-retrofit colos. Confirmed GPU tenants, liquid cooling, 30kW+ racks, anchor-tenant economics. Anchors require NO Bitcoin mining heritage: Colovore (Santa Clara, liquid-cooled), NTT Global DC Americas (AI side), Nexus Data Centers. **Crusoe, Applied Digital, Prometheus Hyperscale, IREN, Core Scientific route to `Crypto to AI - Neoclouds` instead** per Cooper 2026-05-14 (Bitcoin mining heritage is load-bearing). ~160 records. |
| `Modular - colo` | Modular - colo | Distributed/prefabricated/edge-pod operators. Growth = site count, not campus size. >=3 sites, containerized deployments. Nodiac (500+ sites, 800+ MW pipeline), EdgePresence/Ubiquity, Armada, Colony Compute. ~10 records. |
| `Hyperscale Wholesale - colo` | Hyperscale Wholesale - colo | Wholesale-only or wholesale-anchored colos. 10MW+ deployments, 5-15 year terms, 60%+ hyperscaler revenue, per-MW sales. Compass, Aligned, Stack Infrastructure, NTT GDCA, QTS, Vantage, EdgeConneX, AirTrunk, Equinix xScale child. ~12 records. |

### NeoCloud - 5 sub-segments

| Internal Value | Display Label | Description |
|---|---|---|
| `Large Scale GPU - Neocloud` | Large Scale GPU - Neocloud | Bare-metal GPU compute for LLM training. 20+ facilities, >100MW disclosed GPU capacity. Anchors require NO Bitcoin mining heritage: Nebius, Lambda Labs (15+ US DCs, 320MW), Voltage Park, CoreWeave (ClusterMAX Platinum). **Crusoe routes to `Crypto to AI - Neoclouds`** (flared-gas BTC mining lineage). |
| `Tier 1 Inference - Neocloud` | Tier 1 Inference - Neocloud | Distributed inference endpoints at 20-50+ edge cities. Sub-100ms token latency SLA, per-million-tokens pricing. Together.ai (25+ cities, 200MW), Groq (35 Equinix POPs), Cirrascale, DeepInfra, Fireworks AI, Mistral La Plateforme (boundary - foundation-model lab with own inference API; medium_7089 confidence), SambaNova, Baseten. **Sakana AI is NOT an anchor** - it is an AI research / foundation-model company that consumes GPU compute rather than provides it; route to `Other`. |
| `AI Infrastructure providers - Neocloud` | AI Infrastructure providers - Neocloud | Mid-market cloud providers adding GPU compute. Per-GPU-hour pricing, broad customer mix. Vultr, DigitalOcean GPU (post-Paperspace), Fluidstack, Modal, RunPod, OVHcloud (boundary with Sovereign), Scaleway (boundary with Sovereign), Linode (Akamai). **Note case mismatch:** internal value uses lowercase "p" in `providers`; display label uses uppercase. |
| `Sovereign AI Clouds - Neocloud` | Sovereign AI Clouds - Neocloud | Built for data sovereignty (GDPR/DPDP/national AI/GAIA-X). Triple-signal qualifier preferred. Nscale ($14.6B valuation, UK/EU), Firmus (Norway), E2E Networks (India), Yotta (India, 20k Blackwell Ultra Aug 2026), G42/Inception (UAE - Stargate $30B 1GW Abu Dhabi), BSC (Barcelona Supercomputing Center), Stargate UAE. **Sakana AI is NOT an anchor** - same rationale as NC2; AI research lab, not sovereign-cloud operator. |
| `Crypto to AI - Neoclouds` | Crypto to AI - Neocloud | Former Bitcoin miners pivoting to AI infrastructure. **REVISED Cooper 2026-05-14: inclusive of operator AND landlord** - defining trait is Bitcoin mining past + AI pivot, regardless of current business model. Crusoe Energy (flared-gas BTC, Stargate Abilene 200+MW JV), IREN (Microsoft $9.7B/200MW landlord), Core Scientific (CoreWeave host), Galaxy Digital (Helios 393MW CoreWeave host), Bitfarms, TeraWulf, APLD / Applied Digital (Polaris Forge 200MW Oct 2025 hyperscaler lease), Northern Data Group, Prometheus Hyperscale (Hut 8 AI subsidiary), Hut 8 ($7B Google-backed deal Q1 2026). **Note case mismatch:** internal value has trailing "s" on `Neoclouds`; display label drops the "s". |

### MSP/Aggregator - 5 sub-segments

| Internal Value | Display Label | Description |
|---|---|---|
| `Telecom Aggregator - MSP` | Telecom Aggregator - MSP | Traditional channel aggregators / telecom brokers reselling carrier connectivity to enterprises. Direct sales, no sub-agent layer. Granite ($1.85B 2024), Nitel. ~288 records. |
| `Managed Network Services - MSP` | Managed Network Services - MSP | MSPs/integrators/VARs whose primary offering is managed network services (NOT commission resell). 70%+ managed services contracts. Open Systems, Hughes, Logicalis, Presidio, GTT. Post-Phase 1.7c.1 rename (`- Network Operator` suffix archived). |
| `TSD Technology Services Distributor - MSP` | TSD Technology Services Distributor - MSP | Distribution-tier orgs with sub-agent/1099 channels of 100+ active agents. Gross billings $1B+. Telarus ($2.9B), AVANT ($2.1B), Intelisys/ScanSource ($2.7B), AppDirect ($2.0B), Sandler Partners (~$209M), Bridgepointe (firmly TSD post-2026 recap). |
| `Master Agent - MSP` | Master Agent - MSP | Smaller, often regional or vertical-focused master agencies with sub-agent networks. Net commission $5M-$100M, 10-50 sub-agents. X4 Solutions confirmed; CyberNet Communications medium. Cooper 2026-05-14: classify best-fit (no default manual_review). |
| `Cloud + Telecom Hybrid MSP - MSP` | Cloud + Telecom Hybrid MSP - MSP | MSPs spanning cloud reselling AND telecom managed services. >=30% cloud revenue, AWS Premier / Azure Expert / GCP Premier partner. AHEAD ($3B), CDW (post-Mission), Insight (post-SADA), WWT, ePlus, Effectual Cloud, RapidScale. |

### Enterprise-CustomerSegment - 4 sub-segments

Hard gate: vertical (one of the 4 below) AND scale ($1B+ revenue AND (3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house network engineering team)).

| Internal Value | Display Label | Description |
|---|---|---|
| `Financial Services - Enterprise` | Financial Services - Enterprise | Banks, investment firms, insurers, payment networks, capital markets infrastructure. JPMorgan, Goldman Sachs, BNY Mellon, State Street, Visa, Mastercard, BoA, Wells Fargo, Citi, BlackRock, Schwab, HSBC, Barclays, BNP Paribas, Mizuho, Nomura. Defense contractors with commercial procurement (Lockheed, RTX, Northrop, BAE, L3Harris) land here. |
| `Healthcare Systems - Enterprise` | Healthcare Systems - Enterprise | Multi-hospital IDNs and large health systems. >=3 hospitals OR >=$5B + EHR/imaging/clinic networks + HITRUST/HIPAA. HCA, Ascension, CommonSpirit, Kaiser Permanente, Cleveland Clinic, NewYork-Presbyterian, Trinity, Adventist, Banner, Providence. |
| `Retail and Distribution - Enterprise` | Retail and Distribution - Enterprise | Multi-DC national retailers with multi-DC CORPORATE IT (not just multi-warehouse). $5B+ retail revenue OR >=100 stores. Meijer (anchor), Walmart, Kroger, Target, Costco, Home Depot, Lowe's, Albertsons, Publix. |
| `Outsourcing Services - Enterprise` | Outsourcing Services - Enterprise | BPO / outsourced operations providers running multi-site delivery centers on ONGOING OPERATIONAL basis. NOT project consulting. $1B+ revenue, multi-country/multi-state. Cognizant, Genpact, Concentrix, TaskUs, Conduent, Capgemini, Wipro BPS, TCS BPS, Infosys BPM, HCL Tech. **Hard-excluded:** Deloitte, McKinsey, BCG, Bain, Accenture Strategy. |

### Cross-segment - 1 sub-segment

| Internal Value | Display Label | Description |
|---|---|---|
| `Greenfield` | Greenfield | **REAL sub-segment per Cooper feedback 2026-05-14.** Pre-operational or actively-in-build colocation or neocloud companies. Series A-C funded, sites under construction, no operational customer base yet (or only LOI customers). **Pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` customer_segment parent.** Auto-migration rule: R2 reclassifies into the operational sub-segment when the first operational site goes live (recent_news mentions "first site operational" / "ribbon cutting" / first revenue milestone). |

### Retired (archived 2026-05-13, Phase 1.6 - DO NOT USE)

| Internal Value | Reason | Replacement |
|---|---|---|
| `Co-op/consortium` | Renamed for clarity | `Municipal / Cooperative - Fiber operator` |
| `External Extension - Network operator` | Migrated to dedicated field | `network_op_track = external_extension` |
| `Internal + external unification - Network Operator` | Migrated to dedicated field | `network_op_track = internal_external_unification` |
| `Managed Network Services - Network Operator` (pre-Phase 1.7c.1) | Suffix renamed | `Managed Network Services - MSP` |

`import-processor` rejects writes to retired values with error: `"Retired enum value - archived 2026-05-13 Phase 1.6"`. Pre-Phase-1.7c.1 `Managed Network Services - Network Operator` is also rejected.

### Import Mapping Quick-Reference

```
# Network Operator(Tier 1 / VNO) - 5
company_sub_segment = "Tier 1 Carrier - Network Op"
company_sub_segment = "Pure Wholesale Carrier - Network Op"
company_sub_segment = "Cable MSO Enterprise Division - Network Op"
company_sub_segment = "International Backbone Specialist - Network Op"
company_sub_segment = "Subsea cable operator"

# Fiber Operator - 6
company_sub_segment = "Regional CLEC - Fiber operator"
company_sub_segment = "Long Haul / Backbone - Fiber operator"
company_sub_segment = "Dark Fiber Specialist - Fiber Operator"          # capital O
company_sub_segment = "Tier 2 National Wholesale - Fiber operator"
company_sub_segment = "Regional Cable Operator - Fiber operator"
company_sub_segment = "Municipal / Cooperative - Fiber operator"

# Data Center Colo Provider - 4
company_sub_segment = "Standard - colo"
company_sub_segment = "AI Signals - colo"
company_sub_segment = "Modular - colo"
company_sub_segment = "Hyperscale Wholesale - colo"

# NeoCloud - 5
company_sub_segment = "Large Scale GPU - Neocloud"
company_sub_segment = "Tier 1 Inference - Neocloud"
company_sub_segment = "AI Infrastructure providers - Neocloud"          # lowercase p
company_sub_segment = "Sovereign AI Clouds - Neocloud"
company_sub_segment = "Crypto to AI - Neoclouds"                        # trailing s

# MSP/Aggregator - 5
company_sub_segment = "Telecom Aggregator - MSP"
company_sub_segment = "Managed Network Services - MSP"                  # - MSP suffix (post-Phase 1.7c.1)
company_sub_segment = "TSD Technology Services Distributor - MSP"
company_sub_segment = "Master Agent - MSP"
company_sub_segment = "Cloud + Telecom Hybrid MSP - MSP"

# Enterprise-CustomerSegment - 4
company_sub_segment = "Financial Services - Enterprise"
company_sub_segment = "Healthcare Systems - Enterprise"
company_sub_segment = "Retail and Distribution - Enterprise"
company_sub_segment = "Outsourcing Services - Enterprise"

# Cross-segment - 1 (pairs with Data Center Colo Provider OR NeoCloud)
company_sub_segment = "Greenfield"
```

---

## 3. Account Tier (`account_tier`)

**Property name:** `account_tier`
**Type:** Enumeration (single-select)
**Computed by:** the `compute_tier()` algorithm defined in [`context/account-tiering/tier-compute-spec.md`](../account-tiering/tier-compute-spec.md). Every routine that writes tier (R1 Fresh Enrichment, R2 Stale Re-Enrichment, Weekly Signal Scan, R6 Territory & Hygiene, R-Tier-Audit weekly, D7 Edge Case Resolution weekly) inlines that spec. Effective 2026-05-14 per Phase 3 of the Account Tiering & Segmentation Overhaul.

> ⚠️ **Tier 1 = highest priority.** This is inverted from HubSpot's default property description (says "1 (lowest) to 5 (highest)"). Our convention: Tier 1 = best, Tier 5 = worst. Optional fix to HubSpot description planned per Phase 3 Step 15.

| Internal Value | Display Label | Meaning |
|---|---|---|
| `tier_1` | Tier 1 | Highest priority - white-glove rep weekly attention |
| `tier_2` | Tier 2 | Strong ICP fit - rep 1:1 attention |
| `tier_3` | Tier 3 | Qualified but smaller scale or medium confidence - BDR/mass outreach |
| `tier_4` | Tier 4 | Low confidence or signal-quiet - nurture |
| `tier_5` | Tier 5 | Lowest priority - mass outreach / nurture only |

Tier 1 + Tier 2 = rep 1:1 attention pool (~1,137 records post-migration 2026-05-13). Tier 3-5 = BDR / mass outreach. Target accounts (`hs_is_target_account = true`, ~382 records) sit independent of tier - answering "is a rep actively working this?" while tier answers "what does the data say?"

### Canonical defaults table

This is the authoritative truth. Encoded identically in [`context/account-tiering/tier-compute-spec.md`](../core/tier-compute-spec.md) §5 and [`context/hubspot/hubspot-values.md`](hubspot-values.md). Internal values are case-sensitive.

| Segment | Sub-segment | Default | Ceiling | Floor |
|---|---|---:|---:|---:|
| `Network Operator(Tier 1 / VNO)` | `Tier 1 Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Pure Wholesale Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Cable MSO Enterprise Division - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `International Backbone Specialist - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Subsea cable operator` | 2 | 1 | 3 |
| `Data Center Colo Provider` | `AI Signals - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Standard - colo` | 3 | 1 | 5 |
| `Data Center Colo Provider` | `Modular - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Hyperscale Wholesale - colo` | 1 | 1 | 3 |
| `NeoCloud` | `Large Scale GPU - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Sovereign AI Clouds - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Tier 1 Inference - Neocloud` | 2 | 1 | 2 |
| `NeoCloud` | `AI Infrastructure providers - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Crypto to AI - Neoclouds` | 1 | 1 | 2 |
| `Fiber Operator` | `Tier 2 National Wholesale - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Long Haul / Backbone - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Dark Fiber Specialist - Fiber Operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Regional CLEC - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Regional Cable Operator - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Municipal / Cooperative - Fiber operator` | 4 | 2 | 5 |
| `MSP/Aggregator` | `Telecom Aggregator - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `Managed Network Services - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `TSD Technology Services Distributor - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Master Agent - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Cloud + Telecom Hybrid MSP - MSP` | 2 | 1 | 4 |
| `Enterprise-CustomerSegment` | (any of 4 vertical sub-segments) | 3 | 2 | 4 |
| `Data Center Colo Provider` OR `NeoCloud` | `Greenfield` | 2 | 1 | 3 |

### Signal modifiers (additive, bounded by ceiling and floor)

| Modifier | Delta | Source fields |
|---|---:|---|
| Hot signal score 27-44 with event in last 60d | -1 (toward Tier 1) | `last_signal_score` 27-44 AND `last_signal_date` <= 60d |
| White-hot signal score >=45 with event in last 60d | -2 (capped at ceiling) | `last_signal_score` >= 45 AND `last_signal_date` <= 60d |
| Stacked signals (2+ events scoring >=8 in trailing 30d) | -1 additional | `signal_count_last_30d` >= 2 |
| Open deal past `appointmentscheduled` | -1 | Any associated deal past `appointmentscheduled` not in {`closedwon`, `closedlost`} |
| Stale signal (event >90d ago) AND no rep activity <=30d | +1 (toward Tier 5) | `last_signal_date` > 90d AND no engagement <=30d |
| Sustained quiet (event >180d ago AND no activity <=180d) | +1 additional | `last_signal_date` > 180d AND no engagement <=180d |

**Freshness anchor:** modifiers key off `last_signal_date`, which as of 2026-05-28 stores the **event date** (the date the news/funding/hire actually happened) — NOT the detection date. A 6-month-old funding round caught by Signal Scan today is not "hot" — the event itself is stale, even if our detection is fresh. The semantic shift is on the SAME field; no new property was created.

Tier numbers are INVERTED: Tier 1 = highest priority. A "+1 promotion" in human-readable copy means "tier number goes DOWN by 1." This table uses arithmetic.

### Null + unknown-pair fallbacks

When `company_sub_segment` is null OR the `(segment, sub-segment)` pair is unknown (5 known records as of Phase 2 audit - Mapletree, Montera, PTS, Lonestar, LS Power on MSP/Aggregator parent with colo sub-segment values):

| Segment | Null fallback (starting_tier, ceiling, floor) |
|---|---|
| `NeoCloud` | T2 (1, 2) |
| `Fiber Operator` | T3 (1, 4) |
| `Data Center Colo Provider` | T3 (1, 5) - Standard fallback |
| `Network Operator(Tier 1 / VNO)` | T1 (1, 2) |
| `MSP/Aggregator` | T2 (1, 4) |
| `Enterprise-CustomerSegment` | T3 (2, 4) |

Apply segment null fallback AND log warning. Do not throw.

### Manual override (`hs_is_target_account = true`)

Freezes `account_tier` ONLY. Segment, sub-segment, signal field, and enriched field writes ALL proceed normally. Every routine reads `hs_is_target_account` BEFORE the `account_tier` write step. If true, skip the tier write and log skip reason. When the rep clears `hs_is_target_account = false`, the next routine touch resumes algorithmic tier control.

### Tier 1 + Tier 2 pool (rep attention)

Reps work Tier 1 + Tier 2 accounts 1:1. The framework's intended bias is toward signal-aware prioritization - accounts with recent trigger events move up; quiet accounts decay down. Post-migration 2026-05-13: 1,137 records in Tier 1+2 (+17% vs pre-migration baseline of 960).

---

## 4. ICP Tier (`hs_ideal_customer_profile`)

**Property name:** `hs_ideal_customer_profile`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Meaning |
|----------------|--------------|---------|
| `tier_1` | Tier 1 | Great fit  -  matches ICP strongly |
| `tier_2` | Tier 2 | Good fit  -  some qualification signals |
| `tier_3` | Tier 3 | Acceptable but low priority |

---

## 5. Segmentation Confidence (`segmentation_confidence`)

**Property name:** `segmentation_confidence`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | When to Use |
|----------------|--------------|-------------|
| `high_90` | High (90%+) | Bot classification confirmed by known signals |
| `medium_7089` | Medium (70-89%) | Bot classification, some ambiguity |
| `low_5069` | Low (50-69%) | Weak signals, may need manual review |
| `manual_review_required` | Manual review required | Bot couldn't classify confidently |

---

## 6. Lifecycle Stage (`lifecyclestage`)

**Property name:** `lifecyclestage`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Pipeline Position |
|----------------|--------------|-------------------|
| `subscriber` | Prospect | Top of funnel  -  sourced, not yet engaged |
| `lead` | Lead | Identified, initial qualification done |
| `2098366179` | Engaged | Responded to outreach or showed intent |
| `marketingqualifiedlead` | Marketing Qualified Lead | Meets marketing criteria |
| `salesqualifiedlead` | Sales Qualified Lead | Sales-validated, ready for opportunity |
| `opportunity` | Opportunity | Active deal in pipeline |
| `customer` | Customer | Closed-won |
| `2099121898` | Unqualified - bad fit | Does not meet ICP criteria |
| `other` | Other | Catch-all |

### Import Mapping for New Accounts

Most enrichment imports should use:
```
lifecyclestage = "subscriber"    ← New sourced accounts (Prospect)
```

---

## 7. Lead Status (`hs_lead_status`)

**Property name:** `hs_lead_status`
**Type:** Enumeration (single-select)

| Internal Value | Display Label |
|----------------|--------------|
| `NEW` | New |
| `OPEN` | Open |
| `IN_PROGRESS` | In Progress |
| `OPEN_DEAL` | Open Deal |
| `UNQUALIFIED` | Unqualified |
| `ATTEMPTED_TO_CONTACT` | Attempted to Contact |
| `CONNECTED` | Connected |
| `BAD_TIMING` | Bad Timing |

---

## 8. Company Type (`type`)

**Property name:** `type`
**Type:** Enumeration (single-select)

| Internal Value | Display Label |
|----------------|--------------|
| `PROSPECT` | Prospect |
| `PARTNER` | Partner |
| `RESELLER` | Reseller |
| `OTHER` | Other |
| `Customer` | Customer |
| `Disqualified - bad fit` | Disqualified - bad fit |

---

## 9. Infrastructure Profile (`infrastructure_profile`)

**Property name:** `infrastructure_profile`
**Type:** Enumeration (**multi-select**)

Select all that apply per company:

### Facilities (Data Centers)
| Internal Value | Display Label |
|----------------|--------------|
| `Facilities: Small (<5)` | Facilities: Small (<5) |
| `Facilities: Mid-Size (5-19)` | Facilities: Mid-Size (5-19) |
| `Facilities: Large (20-49)` | Facilities: Large (20-49) |
| `Facilities: Enterprise (50+)` | Facilities: Enterprise (50+) |

### Route Miles (Fiber)
| Internal Value | Display Label |
|----------------|--------------|
| `Route Miles: Small (<1K)` | Route Miles: Small (<1K) |
| `Route Miles: Mid-Size (1K-10K)` | Route Miles: Mid-Size (1K-10K) |
| `Route Miles: Large (10K-50K)` | Route Miles: Large (10K-50K) |
| `Route Miles: Enterprise (50K+)` | Route Miles: Enterprise (50K+) |

### POPs (Points of Presence)
| Internal Value | Display Label |
|----------------|--------------|
| `POPs: Small (<10)` | POPs: Small (<10) |
| `POPs: Mid-Size (10-49)` | POPs: Mid-Size (10-49) |
| `POPs: Large (50-99)` | POPs: Large (50-99) |
| `POPs: Enterprise (100+)` | POPs: Enterprise (100+) |

| `None Identified` | None Identified |

> **Multi-select import format:** Separate values with semicolons:
> `Facilities: Mid-Size (5-19);Route Miles: Small (<1K);POPs: Mid-Size (10-49)`

---

## 10. Hyperscaler Proximity (`hyperscaler_proximity`)

**Property name:** `hyperscaler_proximity`
**Type:** Enumeration (single-select)

| Internal Value | Display Label | Tier Impact |
|----------------|--------------|-------------|
| `Announced: <50 miles` | Announced: <50 miles | Tier 1 trigger for colos |
| `Announced: 50-200 miles` | Announced: 50-200 miles | Tier 2 signal |
| `Existing Facility Nearby` | Existing Facility Nearby | Strong signal |
| `None Known` | None Known | Neutral |

---

## 10.5 Fabric Provisioning Approach (`fabric_provisioning_approach`)

**Property name:** `fabric_provisioning_approach`
**Type:** Enumeration (**multi-select**)

Select ALL that apply per company. Semicolon-separated in output.

> ⚠️ **Internal values are lowercase snake_case, NOT the title-case display labels.** This is the property that bit Routine 1 on 2026-04-28 (write of `'None Identified'` was rejected; lowercase `none_identified` succeeded). HubSpot will reject any title-case write with a 400 enum-mismatch error. See the **Enum Case-Sensitivity Reference** appendix at the bottom of this file for the full per-property convention.

| Category | Internal Value | Display Label |
|----------|----------------|--------------|
| External NaaS | `megaport` | Megaport |
| External NaaS | `packetfabric` | PacketFabric |
| External NaaS | `equinix_ecx_fabric` | Equinix ECX Fabric |
| External NaaS | `console_connect` | Console Connect |
| External NaaS | `other_external_naas` | Other External NaaS |
| Competitor | `lumen_private_connectivity_fabric` | Lumen Private Connectivity Fabric |
| Competitor | `other_competitor_fabric` | Other Competitor Fabric |
| Internal | `homegrownproprietary_platform` | Homegrown/Proprietary Platform |
| Internal | `standard_ossbss_stack` | Standard OSS/BSS Stack |
| Internal | `manuallegacy_processes` | Manual/Legacy Processes |
| None | `none_identified` | None Identified |

> **Multi-select import format:** `megaport;packetfabric` (semicolons, no spaces, lowercase values).
> **Note on the slash-stripped values:** `homegrownproprietary_platform`, `standard_ossbss_stack`, and `manuallegacy_processes` are HubSpot's slug-collapsed forms of the labels (the "/" character gets dropped, not converted to underscore). These are the only values HubSpot's API accepts - verified against `/properties/v2/companies/properties/named/fabric_provisioning_approach` on 2026-04-28.

---

## 11. Key Tenant Segments (`key_tenant_segments__cloned_`)

**Property name:** `key_tenant_segments__cloned_`
**Type:** Enumeration (multi-select)

| Internal Value | Display Label |
|----------------|--------------|
| `cloud_providers` | Cloud Providers |
| `enterprises` | Enterprises |
| `carriers` | Carriers |
| `content__hyperscale` | Content & Hyperscale |
| `financial_services` | Financial Services |
| `other` | Other |

> Used primarily for Colo operators to track what types of tenants they serve.

---

## 12. Enrichment Properties (the 8 enriched fields the bot populates)

Per Cooper feedback 2026-05-14: the enrichment bot populates **8 fields** during research (Stage 1b of the 5-stage research-first workflow). `maiaedge_value_proposition` is RETIRED (Cooper 2026-05-26): the field still exists in HubSpot but NO skill writes it - not enrichment, not outreach. Leave it alone. **Conciseness cap: 2-4 sentences each on narrative fields.** At thousands-of-records scale, brevity beats completeness.

| # | Property Name | Label | Type | Length cap (Cooper 2026-05-14) | Description |
|---|---|---|---|---|---|
| 1 | `account_brief` | Company brief | String | **2-4 sentences** (overrides HubSpot 3-6 hint) | Company overview - what they do, who they serve, notable context. Primary narrative source for classification. Excludes geography. |
| 2 | `geographic_focus` | Geographic focus | String | **1-2 sentences / 1 line** | Natural language scope description (e.g., "HQ: Washington \| Scope: Global \| 4 states"). Enables geographic personalization in emails and reference matching. |
| 3 | `infrastructure_profile` | Infrastructure profile | Enumeration (MULTI-SELECT) | Enum (no length) | Bands for Facilities / Route Miles / POPs or "None Identified". **PRIMARY structured signal for classification** - see `context/account-tiering/enrichment-protocols.md` §4 for canonical patterns per sub-segment. See Section 9 below for the 13 enum values. |
| 4 | `hyperscaler_proximity` | Hyperscaler Proximity | Enumeration (single-select) | Enum | "Announced: <50 miles" / "Announced: 50-200 miles" / "Existing Facility Nearby" / "None Known". Primarily a Colocation classification signal. See Section 10 below. |
| 5 | `fabric_provisioning_approach` | Fabric & provisioning approach | Enumeration (MULTI-SELECT) | Enum | 11 options. Detects Network Op Track A (Homegrown) vs Track B (Manual/Legacy) + competitor adoption. See Section 10.5 below. |
| 6 | `provisioning_landscape` | Provisioning landscape | String | **2-4 sentences** | Narrative companion to `fabric_provisioning_approach` - platforms, tools, processes the operator uses, and a messaging angle for MaiaEdge. |
| 7 | `recent_news_or_trigger_event` | Recent News / Trigger Events | String | **2-4 sentences, pure narrative** | Most recent news / funding / leadership / signal. Surfaces Greenfield funding rounds, M&A drift, anchor drift, operational-status transitions. **Do NOT date-prefix the narrative** (post-2026-05-28) — the event date lives in `last_signal_date` for filterability. The narrative is plain prose describing what happened. |
| 8 | `last_enriched_date` | Last enriched date | **Date** (HubSpot date-type; returns + accepts `YYYY-MM-DD`) |  -  | Auto-populated at Stage 5 on a passing definitive gate (see CLAUDE.md Unified `last_enriched_date` Stamping Policy). Gates R2 120-day re-enrichment cadence. **Live HubSpot type verified 2026-05-14: `date` (NOT string).** HubSpot's search API filter operators (`LT` / `GT` / `LTE` / `GTE`) accept `YYYY-MM-DD` string values directly against date-type properties (verified live with `last_enriched_date LT "2026-02-01"` returning 442 records), so routine queries using ISO date strings continue to work without conversion to epoch milliseconds. |

### Retired property (do not write)

| Property Name | Label | Status |
|---|---|---|
| `maiaedge_value_proposition` | MaiaEdge value proposition | **RETIRED 2026-05-26.** The field still exists in HubSpot but NO skill writes it (neither enrichment nor outreach). Earlier (2026-05-14) it was scoped to outreach skills; that was reversed. Do not write it; do not surface it as a gap in completeness audits. |

### Identifier fields (not in enrichment scope but used by enrichment)

| Property Name | Label | Type | Description |
|---|---|---|---|
| `domain` | Company Domain Name | String | Primary company domain (e.g., `equinix.com`) |
| `linkedin_company_page` | LinkedIn Company Page | String | LinkedIn company page URL. Apollo `linkedin_url` is the authoritative source on BOTH new-account creation AND re-enrichment - overwrite when Apollo returns a non-empty value that differs from HubSpot (companies change LinkedIn handles after rebrands / M&A). Used by weekly-signal-scan Excel output column and outreach personalization flows. |

---

## 13. Geographic Properties

| Property Name | Label | Notes |
|--------------|-------|-------|
| `state` | State/Region | Free-text  -  use full state name or 2-letter abbreviation consistently |
| `hs_state_code` | State/Region Code | 2-letter code (auto-populated by HubSpot in some cases) |
| `country` | Country/Region | Free-text |
| `hs_country_code` | Country/Region Code | 2-letter ISO code |

> **Territory routing depends on `state`.** Ensure this reflects **HQ location**, not operational footprint.

---

## 14. Standard Import Template  -  Column Headers

For HubSpot company imports, use these exact column headers:

```csv
Company Domain Name,Name,Customer segment,Company Sub Segment,Account Tier,Lifecycle Stage,Company owner,State/Region,Country/Region,Company brief,MaiaEdge value proposition,Geographic focus,Provisioning landscape,Infrastructure profile,Hyperscaler Proximity,Segmentation confidence,Target Account,Lead Status
```

### Default Values for New Sourced Accounts

| Property | Default Value | Notes |
|----------|--------------|-------|
| `lifecyclestage` | `subscriber` | All new sourced accounts start as Prospect |
| `hs_lead_status` | `NEW` | Fresh, no outreach attempted |
| `type` | `PROSPECT` | Until qualified otherwise |
| `hs_is_target_account` | `true` | If ICP-qualified |
| `segmentation_confidence` | Per bot output | `high_90`, `medium_7089`, or `low_5069` |

---

## 15. Quick Reference: Owner Assignment for Imports

Use this lookup when building import files:

```python
TERRITORY_MAP = {
    # Tim Lieto (East)  -  Owner ID: 161889085
    'AL': '161889085', 'AR': '161889085', 'CT': '161889085', 'DE': '161889085',
    'FL': '161889085', 'GA': '161889085', 'IA': '161889085', 'IL': '161889085',
    'IN': '161889085', 'KY': '161889085', 'LA': '161889085', 'MA': '161889085',
    'MD': '161889085', 'ME': '161889085', 'MI': '161889085', 'MN': '161889085',
    'MO': '161889085', 'MS': '161889085', 'NC': '161889085', 'NH': '161889085',
    'NJ': '161889085', 'NY': '161889085', 'OH': '161889085', 'PA': '161889085',
    'RI': '161889085', 'SC': '161889085', 'VA': '161889085', 'VT': '161889085',
    'WI': '161889085', 'WV': '161889085',

    # Ken Cunningham (West)  -  Owner ID: 162339176
    'AK': '162339176', 'AZ': '162339176', 'CA': '162339176', 'CO': '162339176',
    'DC': '162339176', 'HI': '162339176', 'ID': '162339176', 'KS': '162339176',
    'MT': '162339176', 'ND': '162339176', 'NE': '162339176', 'NM': '162339176',
    'NV': '162339176', 'OK': '162339176', 'OR': '162339176', 'SD': '162339176',
    'TN': '162339176', 'TX': '162339176', 'UT': '162339176', 'WA': '162339176',
    'WY': '162339176',
}

# International → Tim Ziemer: 159350430
# Unknown state → Leave unassigned for manual routing
```

---

## 16. Network Op Track (`network_op_track`)

**Property name:** `network_op_track`
**Type:** Enumeration (single-select)
**Active values:** 2 (verified via HubSpot MCP 2026-05-14). 678 records populated post-Phase 2.7 migration (561 `external_extension` + 117 `internal_external_unification`).

Replaces the retired sub-segment values `External Extension - Network operator` and `Internal + external unification - Network Operator` (archived Phase 1.6 2026-05-13). Track A vs Track B reflects the operator's external-network automation maturity - what the bot should LEAD with in messaging.

| Internal Value | Display Label | Messaging Track | What to detect |
|---|---|---|---|
| `external_extension` | External Extension (Track A) | Lead with cross-carrier extension - operator already has internal automation | Homegrown/proprietary platform in `fabric_provisioning_approach`; sophisticated internal OSS/BSS; portal/API/self-service visible on website |
| `internal_external_unification` | Internal + External Unification (Track B) | Lead with internal unification first - operator hasn't built fabric yet | Manual/Legacy Processes in `fabric_provisioning_approach`; no portal; manual quoting / circuit ordering |

Track value is informational about the operator's external-network exposure and is retained on records even after their `customer_segment` or `company_sub_segment` changes (e.g., Spectrum, Stealth Communications still carry track values after their sub-segment moved to Cable MSO or Dark Fiber).

---

## 17. Signal Persistence Fields

**Created Phase 1; semantics refined 2026-05-28 signal-engine unification.** 3 structured fields that drive `compute_tier` modifiers + `compute_signal_heat`. Written by Signal Scan Stage 5b + the 5 outreach skill push-backs. Together with `recent_news_or_trigger_event` (narrative) + `signal_heat` (rollup), these are the 5 fields that constitute the signal engine.

| Property Name | Label | Type | Description |
|---|---|---|---|
| `last_signal_score` | Last signal score | Number | Highest signal score (per Signal Scan rubric: Tier × Freshness × Confidence) attached to the event in `recent_news_or_trigger_event`. Read by `compute_tier` for hot (-1, score 27-44) and white-hot (-2, score >=45) modifiers. Also drives `signal_heat` Hot/Warm bucketing. Numeric range typically 0-60. |
| `last_signal_date` | Last signal date | Date (YYYY-MM-DD) | **Event date** (semantics narrowed 2026-05-28 — Cooper unified the field rather than creating a duplicate). The date the event in `recent_news_or_trigger_event` actually happened (funding announced, exec hired, etc.) — NOT the engine's detection date. **Primary freshness anchor for `compute_tier` modifiers + `compute_signal_heat`.** Written by Signal Scan Stage 5b + outreach skill push-backs alongside the other persistence fields. Existing pre-2026-05-28 values approximate event dates within ±14d (Signal Scan's detection window) and remain valid — no data migration required. |
| `signal_count_last_30d` | Signal count last 30d | Number | Count of distinct events (scoring >=8) where `last_signal_date` (event date) falls within the trailing 30 days. Read by `compute_tier` for stacked signals modifier (-1 if >=2). Also pushes `signal_heat` to Hot when >=2. Maintained via Signal Scan Stage 5b increment-or-reset logic anchored on event date. Numeric, typically 0-5. |

These fields enable the dynamic layer of tier computation - signals move tier up; sustained quiet moves tier down. See [`context/account-tiering/tier-compute-spec.md`](../core/tier-compute-spec.md) §7 for the modifier table.

---

## 17.5 Signal Heat (`signal_heat`)

**Property name:** `signal_heat`
**Type:** Enumeration (single-select)
**Created:** 2026-05-20 (Phase 3 of Account Tiering & Segmentation Overhaul)
**Computed by:** `compute_signal_heat()` algorithm defined in [`context/account-tiering/tier-compute-spec.md`](../account-tiering/tier-compute-spec.md) §11.5. Same inputs as `compute_tier` signal modifiers; written by the same routines.

`signal_heat` is the rep-facing 4-bucket rollup of signal score + recency + deal context. **Orthogonal to `account_tier`**: tier = strategic value (segment-anchored, floor/ceiling clamped); heat = current intent (decays automatically as the signal date window slides). Reps sort their daily prioritization by heat; analytical work still uses the raw `last_signal_score` views.

### Values

**Internal values are Title Case** (verified via HubSpot MCP 2026-05-28). Writes must use `Hot` / `Warm` / `Cool` / `Cold` exactly — lowercase is rejected.

| Internal Value | Display Label | Meaning |
|---|---|---|
| `Hot` | Hot | Score >=45 with `last_signal_date` (event) in last 60d, OR 2+ events scoring >=8 in last 30d, OR any associated open deal past `appointmentscheduled` |
| `Warm` | Warm | Score 27-44 with `last_signal_date` (event) in last 60d |
| `Cool` | Cool | Any `last_signal_date` (event) in last 180d, not already Hot/Warm |
| `Cold` | Cold | No event in last 180d, OR `last_signal_date` IS NULL |

### Compute logic (top-down, first match wins)

See [`context/account-tiering/tier-compute-spec.md`](../account-tiering/tier-compute-spec.md) §11.5 for the canonical algorithm + override behavior + audit format.

### Inputs (identical to `compute_tier` signal modifier inputs)

- `last_signal_score` (Section 17 above)
- `last_signal_date` (Section 17 above — **primary freshness anchor**, semantics narrowed to event date 2026-05-28)
- `signal_count_last_30d` (Section 17 above)
- Associated open deals (deal past `appointmentscheduled` not in {`closedwon`, `closedlost`})

### Computed by (routines that write `signal_heat`)

- **Weekly Signal Scan Stage 5b** - alongside the 3 signal persistence field writes + tier recompute
- **R-Tier-Audit (daily M-F)** - alongside the tier drift sweep; idempotent no-op if `computed_heat == current_heat`
- **R1 Fresh Enrichment (Path α)** - Stage 5 default assignment for new accounts: `signal_heat = Cold` (no signal history yet)
- **R2 Stale Re-Enrichment (RE_ENRICH_FULL)** - alongside Stage 4 tier recompute
- **R0 Import Validator (MATCH path)** - if record is new to the active pool, default `signal_heat = Cold`
- **R6 Territory & Hygiene (Step 5.5)** - alongside tier maintenance for accounts R6 touched
- **5 outreach skills push-back** - cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline write `signal_heat` as the final step when a fresher event is discovered during outreach research (per CLAUDE.md Signal Engine Unification 2026-05-28). `call-prep` is excluded.

### Override behavior

`hs_is_target_account = true` does NOT freeze `signal_heat`. Tier is rep-locked; heat always reports the truth. This is intentional - reps need to see when a target account has gone cold even though they've pinned its tier.

### Stamping policy

Heat-only recomputes (e.g., R-Tier-Audit recomputing heat with no tier change) do NOT bump `last_enriched_date`, same as tier-only writes. See the CLAUDE.md Unified `last_enriched_date` Stamping Policy table.

### Enum casing

`Hot`, `Warm`, `Cool`, `Cold` - **Title Case** (verified via HubSpot MCP 2026-05-28). Listed in the Enum Case-Sensitivity Reference appendix below.

---

---

## 18. Manual Override / Target Account (`hs_is_target_account`)

**Property name:** `hs_is_target_account`
**Type:** Boolean (HubSpot built-in ABM)
**Active values:** 382 records carry `true` post-migration 2026-05-13.

When `hs_is_target_account = true`:
- `account_tier` is FROZEN. `compute_tier` exits at Step A and returns the current `account_tier` with reason "Manual override locked via hs_is_target_account=true".
- All other writes proceed normally: `customer_segment`, `company_sub_segment`, `segmentation_confidence`, all 8 enriched fields, and the 3 signal persistence fields.
- All routines READ tier for reports / briefings normally.

When the rep clears `hs_is_target_account = false`, the next routine touch resumes algorithmic tier control.

The legacy property name `target_account` was renamed to `hs_is_target_account` (HubSpot's built-in ABM property name). All skills and routines reference `hs_is_target_account` exclusively post-Phase 3.

---

## 19. Archived Properties (DO NOT USE)

| Property Name | Status | Replacement |
|---|---|---|
| `account_tier_legacy` | **Archived 2026-05-13 (Phase 1.3).** Created and then archived per Cooper's direction during Phase 1. Audit logs on disk + dry-run reports are the rollback mechanism. | Read `account_tier` directly. Never write `account_tier_legacy`. |
| `account_tier_manual_override` | **Never created.** The Phase 1 framework signoff proposed this boolean field, but it was superseded by `hs_is_target_account` (HubSpot's built-in ABM property). | Use `hs_is_target_account = true` to freeze tier. |
| `target_account` | Property name (not a separate field) - renamed to `hs_is_target_account` 2026-05-13. Skills referencing `target_account` were updated Phase 3 2026-05-14. | `hs_is_target_account` |

---

## Appendix: Data Quality Flags

| Issue | How to Detect | Resolution |
|-------|--------------|------------|
| Missing `customer_segment` | `customer_segment` = `Unknown` or blank | Run through enrichment pipeline |
| Missing `state` | `state` is blank | Research HQ location for territory routing |
| Wrong territory owner | `state` doesn't match `hubspot_owner_id` per map | Reassign owner per territory map |
| Stale enrichment | `last_enriched_date` > 120 days ago | Re-enrich through pipeline |
| Low confidence segment | `segmentation_confidence` = `low_5069` or `manual_review_required` | Manual review or re-enrich |
| Legacy `Enterprise` value (pre-May-2026) | Should now be `MSP/Aggregator` | If you see a stale write to `Enterprise`, replace with `MSP/Aggregator`. Note: `Enterprise-CustomerSegment` (display "Enterprise") is the multi-DC Enterprise ICP segment promoted May 2026 - do NOT remap that value. |
| `Enterprise-CustomerSegment` without sub-segment | `customer_segment = "Enterprise-CustomerSegment"` AND `company_sub_segment` is blank or not one of the four Enterprise values | Re-classify into Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services. If no fit, demote to `Other` and revisit. |
| `Enterprise-CustomerSegment` failing scale gate | `customer_segment = "Enterprise-CustomerSegment"` AND `infrastructure_profile` shows `Facilities: Small (<5)` or `None Identified` AND no in-house network engineering signal | Failing scale gate ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). Demote to `Other` until stronger signals emerge. |

---

## Appendix: Enum Case-Sensitivity Reference

> **Why this exists.** HubSpot's `manage_crm_objects` API rejects enum writes with `400 PROPERTY_VALUE_NOT_RECOGNIZED` when the value's case or punctuation doesn't exactly match the property's `options[].value` (the *internal* value, not the *display label*). On 2026-04-28, Routine 1 wrote `fabric_provisioning_approach='None Identified'` (the label) and got rejected; lowercase `none_identified` (the value) succeeded on retry. **This is silent for routines that don't retry - partial enrichment writes appear to succeed but the enum field stays blank.** Every routine that writes an enum field MUST consult this table or pipe through `skills/import-processor/` enum mapping.
>
> **Verification.** Values below were retrieved from live HubSpot via `mcp__claude_ai_HubSpot__get_properties` on 2026-04-28. To re-verify on schema drift, run that tool against the property name. If a value here disagrees with what the API returns, the API wins - update this file.

### Casing convention by property (single source of truth)

| Property | Case Convention | Example Value | Sample Wrong Value |
|---|---|---|---|
| `customer_segment` | **Title Case with spaces and special chars** (preserved verbatim) | `Data Center Colo Provider`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, `Enterprise-CustomerSegment`, `Flagged for deletion` | `data center colo provider` (lowercase rejected); `Colocation Operator` (label not value); `Enterprise` (deleted May 2026 - replaced by `MSP/Aggregator`); `Enterprise` written for the multi-DC Enterprise ICP (use `Enterprise-CustomerSegment` instead) |
| `company_sub_segment` | **Title Case with spaces, dashes, slashes** (preserved verbatim). 30 active values 2026-05-14. | `AI Signals - colo`, `Standard - colo`, `Hyperscale Wholesale - colo`, `Modular - colo`, `Tier 1 Carrier - Network Op`, `Pure Wholesale Carrier - Network Op`, `Cable MSO Enterprise Division - Network Op`, `International Backbone Specialist - Network Op`, `Subsea cable operator` (NEW 2026-05-14, no `- Network Op` suffix), `Regional CLEC - Fiber operator`, `Long Haul / Backbone - Fiber operator`, `Dark Fiber Specialist - Fiber Operator` (capital O), `Tier 2 National Wholesale - Fiber operator`, `Regional Cable Operator - Fiber operator`, `Municipal / Cooperative - Fiber operator`, `Large Scale GPU - Neocloud`, `Tier 1 Inference - Neocloud`, `AI Infrastructure providers - Neocloud` (lowercase p), `Sovereign AI Clouds - Neocloud`, `Crypto to AI - Neoclouds` (trailing s), `Telecom Aggregator - MSP`, `Managed Network Services - MSP`, `TSD Technology Services Distributor - MSP`, `Master Agent - MSP`, `Cloud + Telecom Hybrid MSP - MSP`, `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`, `Greenfield` (cross-segment - pairs with Data Center Colo Provider OR NeoCloud parent) | `ai_signals_colo` (snake-case rejected); `Co-op/consortium` (archived 2026-05-13 - use `Municipal / Cooperative - Fiber operator`); `External Extension - Network operator` (archived - use `network_op_track` field); `Internal + external unification - Network Operator` (archived - use `network_op_track`); `Managed Network Services - Network Operator` (pre-Phase 1.7c.1 suffix - use `Managed Network Services - MSP`); `Tier 1 Global Incumbent - Network Op` (stale spec name - use `Tier 1 Carrier - Network Op`); `Enterprise - Financial Services` (wrong order - suffix is the parent segment) |
| `account_tier` | **lowercase snake_case** | `tier_1`, `tier_2`, `tier_3`, `tier_4`, `tier_5` | `Tier 1` (label rejected); `tier1` (no underscore rejected) |
| `hs_ideal_customer_profile` | **lowercase snake_case** | `tier_1`, `tier_2`, `tier_3` | same gotchas as `account_tier` |
| `segmentation_confidence` | **lowercase snake_case + digit suffix** | `high_90`, `medium_7089`, `low_5069`, `manual_review_required` | `high (90%+)` (label rejected); `HIGH_90` (uppercase rejected); `medium_70_89` (extra underscore rejected) |
| `lifecyclestage` | **lowercase + numeric custom-stage IDs** (mixed) | `subscriber`, `lead`, `marketingqualifiedlead`, `salesqualifiedlead`, `opportunity`, `customer`, `other`, `2098366179` (Engaged), `2099121898` (Unqualified) | `Subscriber` (uppercase rejected); `MQL` (alias rejected) |
| `hs_lead_status` | **UPPER_SNAKE_CASE** | `NEW`, `OPEN`, `IN_PROGRESS`, `OPEN_DEAL`, `UNQUALIFIED`, `ATTEMPTED_TO_CONTACT`, `CONNECTED`, `BAD_TIMING` | `New` (title-case rejected); `In Progress` (space rejected) |
| `type` (company type) | **Mixed UPPER and Title Case** (legacy) | `PROSPECT`, `PARTNER`, `RESELLER`, `OTHER` (uppercase) AND `Customer`, `Disqualified - bad fit` (title-case) - the values are NOT consistent across this property | `prospect` (lowercase rejected); `customer` (lowercase rejected) |
| `infrastructure_profile` | **Title Case with colons and parens** (preserved verbatim, multi-select semicolon-separated) | `Facilities: Small (<5)`, `Route Miles: Mid-Size (1K-10K)`, `POPs: Enterprise (100+)`, `None Identified` | `facilities_small` (snake-case rejected); `Facilities: Small <5` (missing parens rejected) |
| `fabric_provisioning_approach` | **lowercase snake_case** (multi-select semicolon-separated) | `megaport`, `packetfabric`, `equinix_ecx_fabric`, `console_connect`, `other_external_naas`, `lumen_private_connectivity_fabric`, `other_competitor_fabric`, `homegrownproprietary_platform`, `standard_ossbss_stack`, `manuallegacy_processes`, `none_identified` | `Megaport` (title-case rejected - this is the bug from 2026-04-28); `Homegrown/Proprietary Platform` (preserved punctuation rejected - slashes get stripped, not converted to underscore) |
| `hyperscaler_proximity` | **Title Case with spaces, colons, and special chars** (preserved verbatim) | `Announced: <50 miles`, `Announced: 50-200 miles`, `Existing Facility Nearby`, `None Known` | `announced_lt_50_miles` (snake-case rejected) |
| `signal_heat` | **Title Case** (verified via HubSpot MCP 2026-05-28) | `Hot`, `Warm`, `Cool`, `Cold` | `hot` (lowercase rejected); `HOT` (uppercase rejected) |

### Universal rules

1. **Always write the `value`, never the `label`.** When in doubt, query the property: `mcp__claude_ai_HubSpot__get_properties({objectType: "companies", propertyNames: ["<name>"]})` returns `options[].value` (write target) and `options[].label` (display). Never substitute one for the other.
2. **Slash and punctuation are unpredictable.** `Homegrown/Proprietary Platform` becomes `homegrownproprietary_platform` (slash stripped) - but `Co-op/consortium` is preserved as-is in `company_sub_segment`. There is no universal rule. Always check live values before constructing a write.
3. **Multi-select is semicolon-separated, no spaces around the semicolons.** `megaport;packetfabric` is correct. `megaport; packetfabric` and `megaport,packetfabric` both fail.
4. **Trailing/leading whitespace fails silently.** `' tier_1'` and `'tier_1 '` are rejected as invalid enum values, but the error message can be misleading. Trim values before writing.
5. **Case-sensitivity is per-property, not global.** Don't assume "we use snake_case" or "we use Title Case" - different properties on the same object follow different conventions. The table above is the only reliable reference.
6. **`import-processor` skill owns the canonical mapping.** Routines that need to translate human-readable input ("High confidence" → `high_90`, "Tier 1" → `tier_1`) should call into `skills/import-processor/` rather than inlining the conversion. That skill is the single point of update if HubSpot adds a new enum value.

### When you encounter a `400 PROPERTY_VALUE_NOT_RECOGNIZED` error

1. The error message includes the rejected value AND the property name. Capture both.
2. Query the live property: `get_properties({objectType, propertyNames: ["<name>"]})`. Compare your write value against `options[].value` (NOT `options[].label`).
3. If the live values disagree with this appendix, **the API is authoritative** - update this appendix to match and add a note in the change log below.
4. If the live values match this appendix but your write still fails, check for trailing whitespace, label/value swaps, and multi-select delimiter format.

### Change log (track schema drift)

| Date | Property | Change | Caught by |
|------|----------|--------|-----------|
| 2026-04-28 | `fabric_provisioning_approach` | Internal values discovered to be lowercase snake_case (`megaport`, `none_identified`, etc.), NOT title-case as previously documented. Doc was wrong since first written. | Routine 1 production run hit `400 PROPERTY_VALUE_NOT_RECOGNIZED` on `'None Identified'`; retry with lowercase succeeded. |
| 2026-05-07 | `customer_segment` | The option whose internal value was `Enterprise` (display label "MSP/Aggregator") was renamed so the internal value now matches the display label: `MSP/Aggregator`. The option `Dark Fiber - Commercial Enterprise` was deleted entirely. `Enterprise-CustomerSegment` (display "Enterprise") was non-ICP at this date but unchanged in HubSpot enum form (it was promoted to ICP on 2026-05-11 - see next row). | Manual rename in HubSpot UI; verified via `get_properties` on 2026-05-07. |
| 2026-05-11 | `customer_segment` + `company_sub_segment` | **Enterprise promoted to ICP.** `Enterprise-CustomerSegment` is now an ICP segment (priority 5 - lowest of the ICPs but qualified and sellable). Four new `company_sub_segment` values added: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Scope: multi-DC enterprises with in-house network engineering teams. Hard sourcing qualification gate: vertical gate (one of four sub-segments) AND scale gate ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR confirmed in-house net eng). Manufacturing, Energy/Utilities, Logistics/Supply Chain explicitly out of scope (Watch List / Future Expansion). Government/Defense FedRAMP-gated and not pursued. Anchor account: Meijer (retail/distribution, Ken Cunningham + Woody Acosta). | Strategic decision approved May 2026 per GTM Reference doc; sub-segment values added in HubSpot UI ahead of this rollout. |
| 2026-05-13 | `company_sub_segment` + `account_tier_legacy` + `network_op_track` + signal persistence fields | **Phase 1 + Phase 2 of Account Tiering & Segmentation Overhaul.** 13 new sub-segment values added (Tier 1 Carrier, Pure Wholesale Carrier, Cable MSO Enterprise Division, International Backbone Specialist, Hyperscale Wholesale - colo, Tier 2 National Wholesale - Fiber operator, Regional Cable Operator - Fiber operator, Municipal / Cooperative - Fiber operator, TSD Technology Services Distributor - MSP, Master Agent - MSP, Cloud + Telecom Hybrid MSP - MSP, Managed Network Services - MSP). 3 retired sub-segment values archived (Co-op/consortium, External Extension - Network operator, Internal + external unification - Network Operator). Active enum count: 32 → 29 → 30 (Subsea cable operator added 2026-05-14). `network_op_track` field created with 2 enum values (external_extension, internal_external_unification). 3 signal persistence fields created (`last_signal_score`, `last_signal_date`, `signal_count_last_30d`). `account_tier_legacy` created and immediately archived (rollback mechanism is on-disk audit). Data migration of 2,700 active prospects completed via Cowork. | Phase 1 schema + Phase 2 data migration via Cowork. Audits at `weekly-reports/migration/2026-05-13-*.md`. |
| 2026-05-14 | `company_sub_segment` | **`Subsea cable operator` added (30th sub-segment).** Cooper added Subsea cable operator as a new sub-segment under Network Operator(Tier 1 / VNO) parent. Lowercase `c` and `o`; no `- Network Op` suffix. Pure-play subsea cable operators with minimal terrestrial backbone - Aqua Comms, Seaborn Networks, BW Digital, Hawaiki, Telxius. Tiebreaker vs International Backbone Specialist: subsea-primary with minimal terrestrial -> Subsea cable operator; subsea + significant terrestrial -> International Backbone Specialist. | Cooper Feedback 2026-05-14 during pre-Phase-3 research pass. |
| 2026-05-14 | `company_sub_segment` (`Greenfield`) | **`Greenfield` confirmed as REAL sub-segment.** Cooper reversed earlier proposed deprecation. Greenfield is the active sub-segment for pre-operational or actively-in-build colocation + neocloud companies. Series A-C funded, sites under construction, <2 operational sites. Pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` customer_segment parent. Auto-migration rule encoded in R2: when first operational site goes live (recent_news mentions "first site operational" / "ribbon cutting" / first revenue milestone), R2 reclassifies into the operational sub-segment. | Cooper Feedback 2026-05-14. |
| 2026-05-14 | `company_sub_segment` (`Crypto to AI - Neoclouds`) | **Crypto to AI - Neoclouds REDEFINED as INCLUSIVE of operator AND landlord.** Cooper: "Companies that used to mine for Bitcoin that have since pivoted to being more of a neocloud / co-location operator." The defining trait is BITCOIN MINING PAST + AI PIVOT, regardless of current business model (operator OR landlord). IREN (Microsoft $9.7B/200MW landlord), Core Scientific (CoreWeave host landlord), Galaxy Digital, Bitfarms (operator), TeraWulf (hybrid), APLD all land here. No new `crypto_pivot_model` field needed. | Cooper Feedback 2026-05-14. |
| 2026-05-20 | `signal_heat` | **`signal_heat` property created in HubSpot.** New 4-bucket enum (`hot` / `warm` / `cool` / `cold`) - the rep-facing rollup of signal score + recency + deal context. Orthogonal to `account_tier` (which is segment-anchored). Computed by `compute_signal_heat` in `context/account-tiering/tier-compute-spec.md` §11.5. Written by Weekly Signal Scan Stage 5b, R-Tier-Audit, R0 (new-account default `cold`), R1 Path α (new-account default `cold`), R2 RE_ENRICH_FULL, R6 Step 5.5. `hs_is_target_account = true` does NOT freeze this field - tier is rep-locked, heat always reports the truth. Heat-only recomputes do NOT bump `last_enriched_date`. | Property created in HubSpot 2026-05-20 by Cooper; encoded across repo same date (Phase 3 follow-on). |
| 2026-05-14 | `account_tier` framework | **Phase 3 of Account Tiering & Segmentation Overhaul.** New tier framework rolled out across repo. `compute_tier()` algorithm canonicalized at `context/account-tiering/tier-compute-spec.md`. 30-row defaults table with per-sub-segment default/ceiling/floor. 6 signal modifiers (hot/white-hot/stacked/open deal/stale/sustained quiet). Manual override via `hs_is_target_account = true` freezes `account_tier` only. R-Tier-Audit Cowork scheduled task created for drift correction. Originally monthly 2026-05-14 → weekly Fri 2026-05-15 → daily M-F 2026-05-21 per Cooper (Apollo-free + idempotent). Current cron `0 20 * * 1-5` UTC (= 3pm CT during CDT). D7 Edge Case Resolution weekly Cowork scheduled task created for manual_review queue processing (hard 14-day max; suggested cron `0 14 * * 3` UTC = Wed 9am CT during CDT). Both reframed as Cowork scheduled tasks (not routines) 2026-05-14 per Cooper - fire-and-forget, stateless across runs, no persistent task-local state. All segment cheatsheets, skills, routines, and CLAUDE.md updated to reference the canonical spec. `target_account` renamed to `hs_is_target_account` globally. `account_tier_legacy` references removed. | Phase 3 of 3 in the Account Tiering & Segmentation Overhaul (completed 2026-05-14). |
| 2026-05-28 | `last_signal_date` semantic shift + `signal_heat` case + signal engine unification | **Signal Engine Unification.** (1) **`last_signal_date` semantics narrowed to EVENT DATE** (was previously written by Signal Scan as the run/detection date). Going forward this field stores the date the event actually happened (funding announced, exec hired, etc.). Cooper briefly created a separate `recent_news__trigger_event_date` field to hold this; on review the existing `last_signal_date` is semantically equivalent, so the new field was deleted and `last_signal_date` was unified for both roles. Existing data approximates event dates within ±14d (Signal Scan's detection window) — no migration required. (2) **`compute_tier` modifiers + `compute_signal_heat`** key off `last_signal_date` (event date semantics). (3) **`signal_heat` enum case correction**: HubSpot has Title Case (`Hot` / `Warm` / `Cool` / `Cold`); repo previously documented lowercase, which would have been silently rejected on write. All routine + skill + spec references updated to Title Case. (4) **`recent_news_or_trigger_event` narrative drops the `[YYYY-MM-DD]` date prefix** — the date lives structurally in `last_signal_date`. Narrative is plain prose. (5) **Outreach signal push-back**: 5 outreach skills (cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline) added a "Final step: Signal Push-Back to HubSpot" stage. `call-prep` excluded (workflow-time-sensitive, low marginal value). Push-back is the absolute last step; failures never block the rep-facing primary output. Same scoring rubric as Signal Scan (score ≥8 floor). **Final field set (5 fields total):** `recent_news_or_trigger_event`, `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`. | Signal Engine Unification 2026-05-28 — Cooper's three asks (engine cohesion + outreach push-back + event-date semantics) bundled as one rework. |
