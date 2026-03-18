# MaiaEdge Account Sourcing Reference Guide

**Sources, Signals, Search Queries & Intelligence by Customer Segment**

February 2026 | Confidential | Go-to-Market Operations

---

> **How to Use This Document**
>
> This guide organizes every sourcing channel, intelligence website, search query strategy, and buying signal by customer segment. Use it to: (1) Find new accounts using the highest-yield sources and search queries, (2) Monitor signals that indicate timing and urgency for existing CRM accounts, (3) Validate segment classification during enrichment, and (4) Brief reps on where to look and what to watch for in each territory.

---

## Table of Contents

1. [Sourcing Philosophy & Hit Rate Benchmarks](#1-sourcing-philosophy--hit-rate-benchmarks)
2. [Segment 1: Colocation Operators](#2-segment-1-colocation-operators)
3. [Segment 2: Fiber Operators](#3-segment-2-fiber-operators)
4. [Segment 3: Network Operators](#4-segment-3-network-operators)
5. [Segment 4: MSP / Aggregators](#5-segment-4-msp--aggregators)
6. [Segment 5: Neoclouds / AI Infrastructure (Emerging)](#6-segment-5-neoclouds--ai-infrastructure-emerging)
7. [Cross-Segment Sources & Signals](#7-cross-segment-sources--signals)
8. [Buying Signal Integration Framework](#8-buying-signal-integration-framework)
9. [Source Access Quick Reference](#9-source-access-quick-reference)

---

## 1. Sourcing Philosophy & Hit Rate Benchmarks

MaiaEdge sells carrier infrastructure to companies that own and operate physical network assets. The fundamental sourcing challenge is separating **infrastructure owners** from **infrastructure consumers**. Broad industry databases (ZoomInfo, Apollo) capture both populations, yielding 27-51% hit rates. Niche infrastructure-specific sources pre-filter for ownership, delivering 60-92% hit rates at half the enrichment cost.

> **CORE PRINCIPLE:** Source quality beats source volume. 1,000 records at 70% hit rate > 2,000 records at 35%. Infrastructure registrations (PeeringDB, FCC filings, ASN registries) require actual infrastructure ownership to list. Conference attendees self-select by industry relevance. Exhaust these sources first.

### Hit Rate Benchmarks by Source Type

| Source | Hit Rate | Best Segments | Why It Works |
|--------|----------|---------------|--------------|
| Conference attendees (PTC, NANOG, Capacity) | **85-92%** | All segments | Self-selecting audience — attendees ARE the industry |
| FCC Broadband Data Collection | **75-85%** | Fiber Operators | Legal requirement to file if you own fiber infrastructure |
| PeeringDB Facilities | **70-80%** | Colo, Network | Requires actual facility or network to register |
| State PUC CLEC/IXC Lists | **70-80%** | Fiber Operators | Licensed carriers only — regulatory barrier filters non-operators |
| DataCenterMap | **60-70%** | Colocation | Facility-focused with ownership tracking |
| Cloudscene | **60-70%** | Colo, Network | Data center + network presence mapping |
| Trade Association Directories | **55-75%** | Varies by assoc. | Membership indicates active industry participation |
| ZoomInfo/Apollo (broad filters) | **27-51%** | Last resort only | Too broad — captures consumers + providers equally |

### Why Broad Filters Fail — Validated Data

A January 2026 ZoomInfo search using Industry = "Telecommunications" + description keywords yielded:
- 544 total records processed
- Only **47 (8.6%)** classified as Colocation Operators
- **232 (43%)** classified as Enterprise consumers — NOT infrastructure providers
- Misclassified companies included: AI compute buyers (Together AI, Vast AI), telecom software vendors, research firms, banks, law firms, and healthcare organizations

**The takeaway:** "Telecommunications" as an industry filter captures everyone who *uses* telecom, not just who *provides* it. The broad search queries in each segment section below are designed to mitigate this by combining industry filters with infrastructure-ownership keywords.

### Cost Economics

Each company processed through the 5-bot enrichment pipeline costs ~$0.08. At a 70% hit rate (niche source), the cost per qualified ICP company is **$0.11**. At a 35% hit rate (broad source), it doubles to **$0.23**. Over a 500-company batch, that difference is $60 in wasted processing.

---

## 2. Segment 1: Colocation Operators

**Definition:** Companies that own data center facilities, meet-me rooms, and sell space/power/cross-connects.

**TAM Estimate:** 800-1,000 US companies | **Priority:** TIER 1 (highest) | **Scale:** 1-50+ facilities, 20-500 employees, $10M-$500M revenue

---

### 2.1 Broad Search Queries (Google, Apollo, ZoomInfo, LinkedIn)

Use these queries when niche sources are exhausted or when you need to supplement with broader discovery. Listed from most precise to broadest.

#### Google Search Queries

| Query | Expected Yield | Why It Works |
|-------|---------------|--------------|
| `"colocation provider" "data center" -jobs -news` | High precision | Direct keyword match for operators, not consumers |
| `"carrier neutral" "data center" "cross connect"` | High precision | Carrier-neutral + cross-connect = infrastructure owner |
| `"meet-me room" "colocation" site:.com` | High precision | Meet-me room is an operator-only term |
| `"data center operator" "cabinet" OR "rack" OR "cage" -cloud -AWS` | Medium precision | Physical infrastructure language, excludes cloud |
| `"colocation" "interconnection" "[STATE]"` | Good for state-by-state | Geographic targeting for territory research |
| `"carrier hotel" "[CITY]"` | High precision | Carrier hotel is a colo-specific term |
| `"data center" "space and power" "cross-connect"` | Good precision | Revenue model language specific to colos |
| `site:peeringdb.com "facility" "[STATE]"` | Very high precision | PeeringDB-indexed facilities in specific states |
| `"colocation" "MW" OR "megawatt" site:.com -news` | Medium precision | Power capacity = facility operator |
| `"data center" "tenant" "interconnection" -"managed services"` | Medium precision | Multi-tenant colo language, excludes MSPs |

#### Apollo / ZoomInfo Optimized Filters

> **WARNING:** Broad database searches yield 27-51% hit rate even with good filters. Use ONLY after exhausting PeeringDB, DataCenterMap, Cloudscene, and conference lists.

**Best Filter Combination (est. 45-55% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Data Center & Colocation Infrastructure |
| Keywords (description) | "colocation" OR "carrier hotel" OR "meet-me room" OR "cross-connect" OR "carrier neutral" |
| Keywords EXCLUDE | "managed services" AND "consulting" AND "software" AND "cloud computing" AND "AI" |
| Employee Count | 20-2,000 |
| Revenue | $5M-$500M |
| HQ Country | United States |

**Backup Filter (broader, est. 35-45% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Telecommunications; Data Center & Colocation Infrastructure |
| Keywords (description) | "data center" AND ("facility" OR "facilities") |
| Keywords EXCLUDE | "consulting" AND "software" AND "staffing" AND "recruiting" |
| Employee Count | 20-2,000 |

**Keywords That Improve Hit Rate in Any Database:**
- **Include (operator signals):** "colocation provider," "carrier hotel," "meet-me room," "carrier neutral," "cross-connect," "cabinet rental," "data center operator," "interconnection facility," "data hall"
- **Exclude (consumer/noise signals):** "managed IT," "cybersecurity," "software development," "consulting," "staffing," "cloud computing provider," "artificial intelligence," "machine learning platform"

#### LinkedIn Sales Navigator Searches

| Search Strategy | Filters |
|-----------------|---------|
| **Company search — direct** | Industry: Telecommunications + Keywords: "colocation" OR "data center operator" + Company size: 11-500 |
| **People search — reverse engineer companies** | Title: "VP Data Center Operations" OR "Director of Colocation" OR "VP Interconnection" → export their companies |
| **Job posting search** | Search: "cross-connect technician" OR "data center technician" OR "colocation" → companies posting these roles are operators |

---

### 2.2 Primary Sourcing Websites (Ranked by Hit Rate)

#### PeeringDB Facilities (peeringdb.com) — GOLD STANDARD

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 70-80% |
| **Estimated Volume** | ~1,200 US facility listings |
| **Cost** | Free (API or web export) |
| **Access** | peeringdb.com/advanced_search → Filter: info_type = Facility, Country = US |
| **API Access** | peeringdb.com/api — Programmatic export for bulk pulls |
| **Why It Works** | You cannot list a facility on PeeringDB without it existing. Registration requires technical details (IX presence, carrier count). This is infrastructure-verified data. |
| **What You Get** | Facility name, operating company, address, city/state, carrier count, IX presence, website |
| **Navigation Tips** | Use Advanced Search to filter by country and facility type. Export results as CSV. Cross-reference company names against existing CRM before enrichment. |
| **Overlap Risk** | Medium-High — Many already in CRM from previous pulls. Always dedupe first. |

#### DataCenterMap (datacentermap.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 60-70% |
| **Estimated Volume** | ~1,000 US listings |
| **Cost** | Free |
| **Access** | datacentermap.com → Browse by country → United States → Browse by state |
| **Why It Works** | Facility-focused listings that track ownership. Less rigorous than PeeringDB but broader coverage of smaller operators. |
| **What You Get** | Facility name, operator, location, facility type indicators |
| **Navigation Tips** | Browse state-by-state for systematic coverage. Useful for finding small/independent colos not on PeeringDB. Cross-reference ownership carefully — some listings show the facility name, not the operating company. |
| **Overlap Risk** | Medium — Significant overlap with PeeringDB. Run dedup before enrichment. |

#### Cloudscene (cloudscene.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 60-70% |
| **Estimated Volume** | ~900 US data center listings |
| **Cost** | Freemium (free tier available, paid for full exports) |
| **Access** | cloudscene.com → Data Centers → Filter by country/region |
| **Why It Works** | Maps both data center presence AND network provider presence at each facility. Useful for understanding interconnection density. |
| **What You Get** | Data center name, operator, location, network providers present, carrier density score |
| **Navigation Tips** | The network provider overlay is the unique value here. Filter for facilities with 5+ network providers for highest-priority prospects. |
| **Unique Signal** | Carrier density score — Higher density = more interconnection potential = stronger MaiaEdge fit |

#### SubmarineCable (submarinecable.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 65-75% |
| **Estimated Volume** | ~200 US cable landing stations |
| **Cost** | Free |
| **Access** | submarinecable.com → Landing Stations → Filter United States |
| **Why It Works** | Cable landing stations are premium colocation/carrier hotel facilities. Companies operating these are high-value colo targets. |
| **What You Get** | Landing station name, operator, cables served, location |
| **Unique Signal** | Submarine cable presence = international traffic hub = high interconnection value |

#### Data Center Hawk (datacenterhawk.com) — PAID

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 65-75% |
| **Estimated Volume** | ~800 US tracked facilities |
| **Cost** | Subscription required |
| **Why It Works** | Tracks facility-level data including power capacity (MW), square footage, and ownership. Best source for understanding facility scale. |
| **What You Get** | Facility details, owner/operator, power capacity, square footage, market analysis |
| **Unique Signal** | Power capacity (MW) is a strong scale indicator — >2MW suggests mid-size+ operator worth pursuing |

#### Baxtel (baxtel.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 55-65% |
| **Estimated Volume** | ~600 US facilities |
| **Cost** | Free |
| **Why It Works** | Curated list of data center facilities. Smaller than PeeringDB but may catch operators others miss, particularly edge/smaller facilities. |

#### Data Center World Attendees (datacenterworld.com) — PAID

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 55-65% |
| **Estimated Volume** | ~500/event |
| **Cost** | $1-2K for attendee/badge scan lists |
| **Access** | Contact event organizer post-event for attendee list purchase |
| **Why It Works** | Self-selecting audience of data center professionals. Lower hit rate than PTC because audience includes facility consumers (enterprises), not just operators. |
| **Filter Strategy** | Filter by job title (VP/Dir Operations, Engineering, Network) and company type (exclude enterprise IT/finance companies) before enrichment. |

---

### 2.3 Qualification & Infrastructure Signals

#### ✅ Definitive Indicators (95%+ confidence — this IS a colo operator)
- Listed on PeeringDB as a Facility (not just Network)
- Listed on DataCenterMap or Cloudscene as colocation provider
- Website has a "Facilities" or "Locations" page with physical data center addresses
- Services page lists: Space, Power, Cabinets, Racks, Cross-connects, Cabinet rental

#### 🟡 Strong Indicators (80-95% confidence)
- Website explicitly mentions: "colocation," "data center," "colo," "carrier hotel," "meet-me room"
- Company description includes: "data center operator," "colocation provider"
- Carrier-neutral positioning (multiple carrier options for tenants)
- Job postings for: Data Center Technician, Cross-Connect Technician, Facility Engineer

#### ❌ Disqualifying Signals (Not a colo — reclassify or exclude)
- Measures network by route miles → **Fiber Operator**
- Primary business is managed services/reselling → **MSP**
- Builds software/platforms, not infrastructure → **Software Vendor (Exclude)**
- "Data center" in description but no owned facilities → **Cloud Consumer (Exclude)**
- AI compute buyer (Together AI, Vast AI, etc.) → **Neocloud or Enterprise (Separate)**

#### Instant Classification Keywords
`"colocation provider"` · `"carrier hotel"` · `"interconnection facility"` · `"data center operator"` · `"meet-me room"` · `"carrier neutral"` · `"interconnection fabric"`

---

### 2.4 Scale Indicators

| Metric | Small | Mid-Size (Sweet Spot) | Large | Enterprise |
|--------|-------|-----------------------|-------|------------|
| Facilities | <5 | 5-19 | 20-49 | 50+ |
| Employees | 20-50 | 50-200 | 200-500 | 500+ |
| Revenue | <$25M | $25M-$100M | $100M-$300M | $300M+ |
| MW Capacity | <2MW | 2-10MW | 10-50MW | 50MW+ |

**Note:** Colocation operators are NOT measured by route miles. Route miles = Fiber Operator signal. Look for: square footage, MW capacity, cabinet count, tenant count.

---

### 2.5 Buying Triggers & Timing Signals

#### Tier 1 Triggers (Immediate Outreach Priority)

| Signal | Where to Monitor | Why It Matters |
|--------|-----------------|----------------|
| New CTO/VP Engineering hired (last 90 days) | LinkedIn Sales Navigator, ZoomInfo Alerts | 90-day evaluation window — new leaders greenlight new initiatives |
| Hyperscaler region announced within 50 miles | AWS/Azure/GCP region announcements, press releases | Immediate cloud on-ramp revenue opportunity for nearby colos |
| Facility expansion announcement | Company press releases, Data Center Hawk, industry press | Investment in growth = budget for new capabilities |
| M&A activity (acquisition or being acquired) | Crunchbase, SEC filings, press releases | Integration needs + network consolidation = automation demand |
| Job posting: "Network Automation" or "SDN" | LinkedIn, Indeed, company careers page | Active investment in automation capability |

#### Tier 2 Triggers (Standard Outreach)

| Signal | Where to Monitor | What It Means |
|--------|-----------------|---------------|
| New service launch (cloud connectivity, SD-WAN) | Company press releases, LinkedIn | Expanding beyond space/power = MaiaEdge fit |
| Conference speaking engagement | Event agendas, LinkedIn | Thought leadership budget indicates investment appetite |
| Mentions Megaport/Equinix challenges on social | LinkedIn, industry forums | Pain point validation — margin leakage to NaaS |
| Tenant growth announcements | Press releases, facility reports | More tenants = more cross-connect demand |
| Currently using Megaport or Equinix Fabric | Website, press releases, PeeringDB | Margin recapture + sovereignty opportunity |

#### What to Look for on Their Website
- **Services page:** Do they list "interconnection" or "cross-connects" as a service? If yes → strong fit. If only space/power → greenfield opportunity.
- **Partners/Carriers page:** How many carriers are in their facility? More carriers = more interconnection potential.
- **Cloud connectivity:** Do they mention AWS Direct Connect, Azure ExpressRoute? If "contact Megaport" appears → direct pain point.
- **Self-service portal:** Do they have one? If not → MaiaEdge white-label portal is a differentiator.
- **Revenue model language:** "Competing on price for space and power" = commodity trap. MaiaEdge helps them compete on connectivity.

---

## 3. Segment 2: Fiber Operators

**Definition:** Companies that own 500+ route miles of fiber and sell dark/lit fiber services.

**TAM Estimate:** 1,200-1,500 US companies | **Priority:** TIER 1 (highest) | **Scale:** 50-2,000 employees, $50M-$1B revenue, 2-10 state footprint

> **LARGEST WHITESPACE OPPORTUNITY:** Fiber operators represent the biggest gap in current CRM coverage relative to TAM. The FCC Broadband Data Collection alone provides 2,500+ potential records at a 75-85% hit rate. Prioritize fiber sourcing to close the coverage gap.

---

### 3.1 Broad Search Queries (Google, Apollo, ZoomInfo, LinkedIn)

#### Google Search Queries

| Query | Expected Yield | Why It Works |
|-------|---------------|--------------|
| `"fiber operator" "route miles" -jobs -news` | High precision | Route miles is the defining metric for fiber operators |
| `"dark fiber" "provider" OR "operator" "[STATE]"` | High precision | Dark fiber = infrastructure owner |
| `"lit services" OR "lit fiber" "wavelength" site:.com` | High precision | Lit services + wavelength = fiber operator language |
| `"CLEC" "fiber" "[STATE]"` | High precision | CLEC designation = licensed carrier |
| `"metro fiber" OR "metro ring" "operator" -jobs` | Good precision | Metro ring = owned fiber infrastructure |
| `"wholesale fiber" OR "wholesale transport" "[STATE]"` | Good precision | Wholesale = selling capacity, not just consuming |
| `"fiber network" "route miles" OR "fiber miles" site:.com` | Good precision | Route mile counts on websites = confirmed fiber owner |
| `"regional fiber" "dark fiber" OR "DWDM" OR "wavelength"` | Medium precision | Technology terms specific to fiber operators |
| `site:ntca.org "[COMPANY]"` OR `site:fiberbroadband.org "[COMPANY]"` | Very high precision | Trade association member verification |
| `"[STATE] broadband" "fiber" "provider" -residential -FTTH` | Medium precision | State-level fiber provider discovery, excludes pure residential |
| `"fiber IRU" OR "indefeasible right of use" "[STATE]"` | High precision | IRU is a dark fiber lease term — only fiber operators use it |
| `"DWDM" OR "dense wavelength" "provider" "[STATE]"` | High precision | DWDM technology = optical fiber network operator |

#### Apollo / ZoomInfo Optimized Filters

**Best Filter Combination (est. 50-60% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Telecommunications |
| Keywords (description) | "fiber" AND ("route miles" OR "dark fiber" OR "wholesale" OR "CLEC" OR "lit services" OR "wavelength") |
| Keywords EXCLUDE | "managed services" AND "consulting" AND "software" AND "wireless only" AND "satellite" |
| Employee Count | 50-5,000 |
| Revenue | $10M-$1B |
| HQ Country | United States |

**Alternative: Job Title Reverse Search (higher precision, lower volume):**
| Filter | Value |
|--------|-------|
| Job Title | "VP Network" OR "VP Operations" OR "VP Transport" OR "Director Fiber" OR "OSP Manager" |
| Industry | Telecommunications |
| Employee Count | 50-5,000 |
| → Then export their companies |

**Keywords That Improve Hit Rate in Any Database:**
- **Include (operator signals):** "route miles," "fiber network operator," "dark fiber provider," "wholesale fiber," "lit services," "metro rings," "DWDM," "wavelength services," "fiber IRU," "outside plant," "CLEC"
- **Exclude (noise signals):** "wireless only," "satellite," "managed IT," "cybersecurity," "software," "consulting," "cable TV only," "FTTH residential only"

#### LinkedIn Sales Navigator Searches

| Search Strategy | Filters |
|-----------------|---------|
| **Company search — direct** | Industry: Telecommunications + Keywords: "fiber" AND ("route miles" OR "dark fiber" OR "wholesale") + Company size: 51-5,000 |
| **People search — reverse engineer companies** | Title: "VP Network" OR "VP Transport" OR "Director of OSP" OR "VP Fiber" OR "Optical Network Engineer" → export their companies |
| **Job posting search** | Search: "OSP technician" OR "fiber splicer" OR "DWDM engineer" OR "optical engineer" → companies posting these are fiber operators |
| **Trade association members** | Search companies that follow NTCA, Fiber Broadband Association, or ACA Connects pages |

---

### 3.2 Primary Sourcing Websites (Ranked by Hit Rate)

#### FCC Broadband Data Collection (broadbandmap.fcc.gov) — GOLD STANDARD

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 75-85% |
| **Estimated Volume** | ~2,500 US filers |
| **Cost** | Free |
| **Access** | broadbandmap.fcc.gov → Download bulk data files. Replaced Form 477 in 2023. |
| **Why It Works** | Legal requirement: you cannot file with the FCC unless you own broadband infrastructure. This is the most authoritative fiber operator registry in the US. |
| **What You Get** | Provider name, technology type (fiber/cable/fixed wireless), geographic coverage areas, brand names used |
| **Navigation Tips** | Filter for technology_code = Fiber (50/60 series). Focus on providers with "fiber" as primary technology. Cross-reference brand names — some file under parent company while operating under a DBA. |
| **Key Caveat** | Includes ISPs that deliver fiber to homes (FTTH). Filter for wholesale/commercial providers vs. purely residential ISPs. Look for providers serving business/enterprise, not just residential. |

#### State PUC CLEC/IXC Lists (varies by state)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 70-80% |
| **Estimated Volume** | ~1,500 US total across all states |
| **Cost** | Free |
| **Access** | Search: "[State] Public Utility Commission CLEC list" or "[State] PUC IXC carriers". Varies significantly by state. |
| **Why It Works** | CLEC (Competitive Local Exchange Carrier) and IXC (Interexchange Carrier) licensing requires actual carrier operations. These are verified, licensed carriers. |
| **What You Get** | Carrier name, license type (CLEC/IXC), service territory, sometimes contact information |
| **Navigation Tips** | Labor-intensive but high-quality. Prioritize top-10 states by fiber density: Texas, California, Florida, New York, Ohio, Pennsylvania, Illinois, Georgia, Virginia, North Carolina. Many states publish PDFs — extract to spreadsheet for processing. |
| **Overlap Risk** | Low — Many small/regional carriers on PUC lists are NOT in PeeringDB or major databases. High net-new potential. |

#### Fiber Locator (fiberlocator.com) — PAID

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 70-80% |
| **Estimated Volume** | ~1,000 US providers mapped |
| **Cost** | Subscription required |
| **Why It Works** | Interactive fiber route maps that show actual fiber routes on a map. You can see WHO has fiber WHERE. Essential for geographic coverage analysis. |
| **What You Get** | Fiber provider name, route maps, building connectivity, lit building locations |
| **Unique Signal** | Route density analysis — shows where fiber operators have concentrated infrastructure. Useful for territory planning. |

#### Trade Association Directories

| Association | Hit Rate | Volume | Focus | Access |
|-------------|----------|--------|-------|--------|
| NTCA (ntca.org) | 65-75% | ~850 members | Rural broadband/fiber/telcos | Member directory; membership may be required |
| Fiber Broadband Assoc (fiberbroadband.org) | 60-70% | ~400 members | Fiber-first companies | Directory on website |
| ACA Connects (acaconnects.org) | 60-70% | ~600 members | Independent carriers/cable operators | Member directory |

Trade association membership indicates active participation in the fiber industry. NTCA members are particularly valuable — these are rural fiber operators often missed by larger databases. Many are family-owned or cooperative-model companies with 500-10,000 route miles.

#### PeeringDB Networks — Filtered for Fiber (peeringdb.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 55-65% |
| **Estimated Volume** | ~800 US network listings (filtered) |
| **Cost** | Free |
| **Access** | peeringdb.com/advanced_search → Filter: info_type = NSP or Cable, Country = US |
| **Why It Works** | NSP and Cable registrations capture many fiber operators with network presence. Lower hit rate than FCC because it also captures transit/CDN companies. |
| **Filter Strategy** | Cross-reference with FCC BDC data. Companies appearing in BOTH are very high confidence fiber operators. |

#### Capacity Conference Attendees (capacitymedia.com) — PAID

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 55-65% |
| **Estimated Volume** | ~400/event |
| **Cost** | $1-2K for attendee list |
| **Why It Works** | Wholesale/carrier-focused conference. Attracts fiber operators who sell capacity to other carriers. Strong fiber + network operator mix. |
| **Filter Strategy** | Filter by job title (VP Network, VP Sales, VP Operations) and company description. Exclude pure enterprise/IT companies. |

---

### 3.3 Qualification & Infrastructure Signals

#### ✅ Definitive Indicators (95%+ confidence)
- FCC Broadband Data Collection filer with fiber technology code
- State PUC CLEC or IXC license holder
- Website explicitly states route miles (e.g., "5,000 route miles of fiber")
- Listed on PeeringDB as NSP with fiber-specific description
- NTCA or Fiber Broadband Association member

#### 🟡 Strong Indicators (80-95% confidence)
- Website mentions: "route miles," "fiber network," "metro rings," "lit services," "dark fiber," "wholesale fiber"
- Services page lists: Dark fiber leases, Wavelengths, DWDM, Lit Ethernet, DIA, Wholesale transport
- Network map showing owned fiber routes on their website
- Regional coverage (typically 2-10 states)
- Job postings for: Optical Engineer, DWDM Engineer, OSP (Outside Plant) Technician, Fiber Splicer

#### ❌ Disqualifying Signals
- No owned fiber; resells carrier capacity → **MSP/Aggregator**
- Primary business is data center facilities → **Colocation Operator**
- 100,000+ route miles with national coverage → **Network Operator (Tier 1/2)**
- Purely residential FTTH with no business/wholesale → **Lower priority** (still ICP but weaker fit)
- Internal-use-only fiber (university, utility, railroad) → **Exclude**

#### Instant Classification Keywords
`"lit fiber services"` · `"fiber to the premise"` · `"facilities-based broadband"` · `"fiber network operator"` · `"dark fiber provider"` · `"wholesale fiber"` · `"regional fiber operator"` · `"route miles"`

---

### 3.4 Scale Indicators

| Metric | Small | Mid-Size (Sweet Spot) | Large | Enterprise |
|--------|-------|-----------------------|-------|------------|
| Route Miles | <1,000 | 1,000-10,000 | 10,000-50,000 | 50,000+ |
| Employees | 50-100 | 100-500 | 500-2,000 | 2,000+ |
| Revenue | <$25M | $25M-$200M | $200M-$500M | $500M+ |
| State Coverage | 1-2 | 2-5 | 5-10 | 10+ |

**Sweet spot for MaiaEdge:** 500-50,000 route miles (regional operators). Fiber utilization of 30-70% represents significant stranded capacity — monetization is a key value proposition.

---

### 3.5 Buying Triggers & Timing Signals

| Signal | Where to Monitor | Why It Matters |
|--------|-----------------|----------------|
| NNI/partnership announcement | Press releases, LinkedIn, industry news | Active federation = direct MaiaEdge use case |
| Lost multi-state deal (mentioned in earnings/calls) | SEC filings, earnings calls, industry reports | Footprint limitation pain — federation solves this |
| Type 2 circuit procurement increase | Industry reports, job postings for circuit provisioning | Leased capacity growing = visibility black hole growing |
| 30-70% fiber utilization mentioned | Earnings calls, investor presentations, press | Stranded capacity = monetization opportunity |
| New CTO/VP Network hire | LinkedIn Sales Navigator | 90-day window for new technology decisions |
| Enterprise customer requesting cloud on-ramps | Social media, conference talks, press | Cloud demand they can't serve alone = MaiaEdge entry |
| Fiber build/expansion announcement | Press releases, state broadband offices, NTCA news | Growth investment = budget for new platform capabilities |

#### What to Look for on Their Website
- **Network map:** Shows owned fiber routes. Look at geographic density vs. gaps — gaps indicate where they need partners (federation opportunity).
- **"Partners" or "Wholesale" page:** Do they have carrier-to-carrier relationships? Existing NNIs = federation pain point validation.
- **Services:** Dark fiber + lit services + wavelengths = full-service fiber operator. Dark fiber only = simpler operator, still good fit.
- **Route mile count:** 500-50,000 is the sweet spot. <500 may be too small. >100K = Network Operator.
- **Cloud connectivity:** If absent from services page → greenfield cloud on-ramp opportunity.

---

## 4. Segment 3: Network Operators

**Definition:** Tier 1/2 carriers with national/global footprint and complex multi-domain networks.

**TAM Estimate:** 800-1,000 US companies | **Priority:** TIER 2 (standard) | **Scale:** 500+ employees, 50K+ route miles, 100+ PoPs, $500M+ revenue

---

### 4.1 Broad Search Queries (Google, Apollo, ZoomInfo, LinkedIn)

#### Google Search Queries

| Query | Expected Yield | Why It Works |
|-------|---------------|--------------|
| `"Tier 1 carrier" OR "Tier 2 carrier" "network operator"` | High precision | Direct classification terms |
| `"national carrier" "enterprise MPLS" OR "enterprise WAN" -jobs` | High precision | Enterprise MPLS = carrier-grade service |
| `"global network" "PoP" OR "points of presence" site:.com` | Good precision | PoP counts = carrier-scale infrastructure |
| `"backbone network" "carrier" "[REGION]" -news` | Good precision | Backbone language = national-scale operator |
| `"mobile backhaul" "carrier" OR "operator"` | Medium precision | Mobile backhaul is a network operator use case |
| `"multi-domain" "network" "orchestration" OR "automation"` | Medium precision | Finds operators actively thinking about automation |
| `"SD-WAN" "managed" "carrier" -enterprise -branch` | Medium precision | Carrier-provided SD-WAN = network operator service |
| `"ASN" "[COMPANY NAME]" site:bgp.he.net` | Very high precision | Direct ASN verification for known companies |
| `"internet exchange" "member" "[CITY]" OR "[STATE]"` | Good precision | IX members are network operators |
| `"wholesale carrier" OR "wholesale connectivity" "[STATE]"` | Medium precision | Wholesale = infrastructure owner selling to other carriers |

#### Apollo / ZoomInfo Optimized Filters

**Best Filter Combination (est. 40-50% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Telecommunications |
| Keywords (description) | "carrier" AND ("MPLS" OR "backbone" OR "enterprise WAN" OR "Tier 1" OR "Tier 2" OR "national network" OR "global network") |
| Keywords EXCLUDE | "reseller" AND "managed services only" AND "software" AND "consulting" |
| Employee Count | 500+ |
| Revenue | $100M+ |
| HQ Country | United States |

**Keywords That Improve Hit Rate:**
- **Include (operator signals):** "Tier 1 carrier," "Tier 2 carrier," "national backbone," "global carrier," "enterprise WAN," "MPLS," "IP transit," "mobile backhaul," "VNO," "multi-domain orchestration," "wholesale carrier"
- **Exclude (noise signals):** "managed IT," "cybersecurity," "software," "consulting," "reseller," "cloud computing provider"

#### LinkedIn Sales Navigator Searches

| Search Strategy | Filters |
|-----------------|---------|
| **People search — reverse engineer** | Title: "VP Network Engineering" OR "Chief Network Officer" OR "VP Transport" OR "Director Network Architecture" at companies with 500+ employees in Telecommunications |
| **Job posting search** | Search: "BGP engineer" OR "MPLS engineer" OR "network architect" + company size 500+ → companies posting these are carriers |
| **Group membership** | Members of NANOG, MEF, or PTC groups on LinkedIn |

---

### 4.2 Primary Sourcing Websites (Ranked by Hit Rate)

#### PTC Conference Attendees (ptc.org) — HIGHEST PROVEN HIT RATE

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | **92%** (validated across 959 companies) |
| **Estimated Volume** | ~500 carrier/operator companies per event |
| **Cost** | $1-2K for attendee/badge scan lists |
| **Why It Works** | Pacific Telecommunications Council attracts carrier executives, network operators, and infrastructure providers. The audience IS MaiaEdge's ICP. Proven with PTC26 data. |
| **Filter Strategy** | Filter by job title and company type. Even unfiltered, 92% hit rate makes this the single best source ever tested. |

#### PeeringDB Networks — Filtered for Carriers (peeringdb.com)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 70-80% |
| **Estimated Volume** | ~600 US networks (filtered) |
| **Cost** | Free |
| **Access** | peeringdb.com/advanced_search → Filter: info_type = NSP, traffic levels > 100Gbps, Country = US |
| **Why It Works** | NSP classification + high traffic levels filters for actual network operators vs. small ISPs. Traffic level is a proxy for operational scale. |
| **Navigation Tips** | Sort by traffic level descending. Companies with >1Tbps are almost certainly Tier 1/2 carriers. |

#### ARIN ASN Registry (whois.arin.net)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 65-75% |
| **Estimated Volume** | ~800 US organizations with ASNs |
| **Cost** | Free |
| **Access** | whois.arin.net for lookups, ftp.arin.net for bulk downloads |
| **Why It Works** | You must operate a network to have an ASN. This is a technical barrier that filters out non-operators. |
| **Navigation Tips** | Focus on organizations with multiple ASNs (indicates scale). Cross-reference with HE BGP Toolkit for peering relationships. |

#### Hurricane Electric BGP Toolkit (bgp.he.net)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 65-75% |
| **Estimated Volume** | ~1,000 US networks |
| **Cost** | Free |
| **Access** | bgp.he.net → Search by ASN, organization name, or IP prefix |
| **Why It Works** | Shows actual BGP peering relationships and network topology. |
| **What You Get** | ASN details, peering relationships, prefixes announced, IX memberships, upstream/downstream |
| **Unique Signal** | Peering count and IX membership count indicate sophistication. 20+ peers = significant network operator. |

#### NANOG Attendees (nanog.org) — PAID/MEMBERSHIP

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 65-75% |
| **Estimated Volume** | ~300/event |
| **Cost** | Membership; attendee lists may be available |
| **Why It Works** | North American Network Operators Group — attendees are network engineers and operators at carriers. |

#### MEF Member Directory (mef.net)

| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 55-65% |
| **Estimated Volume** | ~200 members |
| **Cost** | Directory available; membership for full access |
| **Why It Works** | MEF members are carriers committed to Carrier Ethernet standards. Strong network operator indicator. |
| **Unique Signal** | MEF certification (CE 2.0) indicates investment in standards-based networking. |

---

### 4.3 Qualification & Infrastructure Signals

#### ✅ Definitive Indicators (95%+ confidence)
- Listed on PeeringDB as Tier 1 or Tier 2 carrier
- 100,000+ route miles with national/international coverage
- 100+ PoPs across multiple regions/countries
- FCC telecommunications license holder
- Owns ASN(s) with significant BGP peering relationships

#### 🟡 Strong Indicators (80-95% confidence)
- Website mentions: "Tier 1 carrier," "national carrier," "global network," "enterprise WAN"
- Services page lists: Enterprise MPLS, SD-WAN, Global connectivity, Mobile backhaul
- Multiple acquired companies/networks mentioned in history
- 2,000+ employees
- Complex multi-domain network architecture referenced

#### ❌ Disqualifying Signals
- Regional-only footprint (<10 states) → **Fiber Operator**
- <500 employees with simple network → **Likely Fiber or MSP**
- Pure software/platform company → **Exclude**

#### Instant Classification Keywords
`"Tier 1 carrier"` · `"Tier 2 carrier"` · `"national backbone"` · `"global carrier"` · `"incumbent carrier"` · `"managed connectivity services"` · `"multi-domain orchestration"`

---

### 4.4 Buying Triggers

| Signal | Where to Monitor | Why It Matters |
|--------|-----------------|----------------|
| New PoP activation project | Press releases, job postings, industry news | PoP activation pain is direct MaiaEdge use case — months to days |
| M&A / acquired network integration | SEC filings, Crunchbase, press | Acquired networks need integration = multi-domain orchestration |
| Enterprise customers demanding cloud-like speed | Earnings calls, press releases | Competitive pressure from hyperscalers validates urgency |
| Lumen PCF or AWS Interconnect mentioned as threat | Earnings calls, industry analysis | Direct competitive pressure — MaiaEdge enables them to compete |
| Mobile backhaul expansion | Press releases, 5G deployment news | Cell tower connectivity at scale = MaiaEdge IENTC use case |
| Job postings for SDN/automation engineers | LinkedIn, Indeed | Active investment in network modernization |

---

## 5. Segment 4: MSP / Aggregators

**Definition:** Managed Service Providers who aggregate and resell connectivity from multiple upstream carriers.

**TAM Estimate:** 2,000-3,000 US companies | **Priority:** TIER 3 (lower) | **Scale:** 50-500 employees, 3-10+ carrier relationships, $20M-$500M revenue

> **SOURCING STRATEGY NOTE:** MSP/Aggregators are deprioritized because they depend on carrier infrastructure rather than owning it. MaiaEdge's value proposition is strongest for infrastructure owners. Recommended approach: **Passive + Selective Active.** Do NOT actively source via ZoomInfo/Apollo for this segment. Focus on inbound leads, referrals, and targeted conference lists.

---

### 5.1 Broad Search Queries (Google, Apollo, ZoomInfo, LinkedIn)

> **Use sparingly** — active sourcing for MSPs is deprioritized. These queries are for supplemental discovery only.

#### Google Search Queries

| Query | Expected Yield | Why It Works |
|-------|---------------|--------------|
| `"carrier aggregator" "multi-carrier" "managed network"` | Medium precision | Aggregator-specific language |
| `"managed service provider" "carrier" "enterprise connectivity"` | Lower precision | MSP + carrier = connectivity MSP, not IT MSP |
| `"SD-WAN" "managed" "multi-carrier" -enterprise -branch` | Medium precision | Managed SD-WAN with multi-carrier = aggregator |
| `"master agent" "telecom" OR "carrier"` | Good precision | Master agent networks are MSP sourcing channels |
| `"single point of contact" "carrier" OR "carriers" "enterprise"` | Medium precision | "Single point of contact" is classic MSP positioning |
| `"network aggregator" "enterprise" -news -jobs` | Medium precision | Direct term for the segment |

#### Apollo / ZoomInfo — Use Only for Contact Enrichment

**If you must search (est. 25-35% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Telecommunications |
| Keywords (description) | "managed service provider" AND ("carrier" OR "multi-carrier" OR "aggregator") |
| Keywords EXCLUDE | "IT support" AND "cybersecurity" AND "software" AND "cloud provider" |
| Employee Count | 50-500 |

**Keywords That Improve Hit Rate:**
- **Include:** "carrier aggregator," "multi-carrier," "managed network," "white label provider," "B2B marketplace," "network aggregator"
- **Exclude:** "managed IT," "IT help desk," "cybersecurity MSP," "endpoint management," "cloud provider"
- **CRITICAL DISTINCTION:** Connectivity MSP/Aggregator ≠ IT MSP. The keyword "managed services" alone captures both. Always combine with carrier/connectivity terms.

---

### 5.2 Sourcing Websites

#### Channel Partners Conference (channelpartnersconference.com) — PAID
| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 50-60% |
| **Volume** | Large attendee base; filter heavily |
| **Cost** | $1-2K for attendee lists |
| **Filter Strategy** | Focus on "managed service provider," "aggregator," or "multi-carrier." Exclude pure VARs, software resellers. |

#### MSP 501 / CRN Rankings (crn.com)
| Attribute | Detail |
|-----------|--------|
| **Hit Rate** | 40-50% |
| **Volume** | 501 companies (annual ranking) |
| **Cost** | Free to view |
| **Navigation Tips** | Filter for companies emphasizing multi-carrier connectivity vs. pure IT managed services. |

#### Agent/Master Agent Networks
Key master agents in telecom: Telarus, Avant, Intelisys, Sandler Partners, AppSmart. These organizations and their larger sub-agents can be MSP/Aggregator prospects.

---

### 5.3 Qualification Signals

#### ✅ Definitive Indicators (95%+ confidence)
- Listed on MSP 501 ranking or similar MSP directories
- Website explicitly positions as "managed service provider" or "aggregator"
- Partners page listing 10+ carrier/vendor logos (AT&T, Verizon, Lumen, etc.)

#### 🟡 Strong Indicators (80-95% confidence)
- Services: Managed SD-WAN, Managed Security, UCaaS, Cloud Services, Managed Network
- Emphasizes "single point of contact" and "vendor management"
- Does NOT emphasize owned infrastructure (no route miles, no facilities)
- Channel/partner program for resellers

#### ❌ Disqualifying Signals
- Owns 5,000+ route miles → **Fiber Operator**
- Owns data center facilities → **Colocation Operator**
- National carrier with extensive owned infrastructure → **Network Operator**
- Pure VAR/reseller with no recurring services → **Exclude**

#### Instant Classification Keywords
`"carrier broker"` · `"white label provider"` · `"B2B marketplace"` · `"carrier aggregator"` · `"network aggregator"`

---

### 5.4 Buying Triggers

| Signal | Where to Monitor | Why It Matters |
|--------|-----------------|----------------|
| Tier 1 carrier going direct to their enterprise customers | Industry news, earnings calls | Existential threat — MSPs must differentiate on speed/visibility |
| Carrier SLA violations/disputes | Industry forums, social media | Visibility pain across leased infrastructure |
| New carrier relationship onboarded | Press releases, LinkedIn | More carrier complexity = more MaiaEdge value |
| Enterprise customer churn due to slow provisioning | Conference talks, social | Speed-to-service is key differentiator MaiaEdge enables |

---

## 6. Segment 5: Neoclouds / AI Infrastructure (Emerging)

**Definition:** Companies providing GPU cloud compute, AI inference platforms, or repurposed infrastructure for AI/HPC workloads.

**TAM Estimate:** 250-350 companies globally (142 currently identified) | **Priority:** EMERGING (high strategic value, indirect deployment model)

> **KEY INSIGHT FROM DATUM.NET:** Neoclouds are compute companies that accidentally became networking companies. They have no WAN teams, no Kentik, no PRTG. They don't know they have a network problem — they know they're slow. Lead with observability and cloud on-ramp acceleration, not deterministic paths. Neoclouds create demand for MaiaEdge at the colocation operators hosting their GPU clusters.

---

### 6.1 Broad Search Queries (Google, Apollo, ZoomInfo, LinkedIn)

#### Google Search Queries

| Query | Expected Yield | Why It Works |
|-------|---------------|--------------|
| `"GPU cloud" "compute" -news -review` | High precision | Direct term for the segment |
| `"GPU-as-a-service" OR "GPUaaS" site:.com` | High precision | Specific neocloud business model |
| `"AI infrastructure" "cloud" "GPU" -jobs -course` | Good precision | AI infra + GPU = neocloud |
| `"inference cloud" OR "inference platform" -tutorial` | Good precision | Inference-as-a-service is a fast-growing sub-segment |
| `"bare metal GPU" OR "dedicated GPU" "cloud"` | Good precision | Bare metal GPU hosting = neocloud |
| `"NVIDIA DGX" "cloud" OR "hosting" OR "provider"` | Good precision | DGX Cloud partners are validated GPU infrastructure providers |
| `"AI compute" "data center" "colocation" -news` | Medium precision | Finds neoclouds at colo facilities (deployment points) |
| `"crypto" "AI" "pivot" "data center" OR "GPU"` | Medium precision | Crypto-to-AI pivots are a major sub-segment |
| `"sovereign AI" "cloud" "[COUNTRY]"` | Medium precision | Sovereign AI programs spawn new GPU cloud operators |
| `"liquid cooling" "GPU" "data center" -HVAC -residential` | Good precision | Liquid cooling = high-density AI compute infrastructure |

#### Apollo / ZoomInfo Optimized Filters

**Best Filter Combination (est. 35-45% hit rate):**
| Filter | Value |
|--------|-------|
| Industry | Cloud Computing; Data Center & Colocation Infrastructure |
| Keywords (description) | "GPU" AND ("cloud" OR "compute" OR "infrastructure" OR "hosting") |
| Keywords EXCLUDE | "consulting" AND "software development" AND "training" AND "course" |
| Employee Count | 10-2,000 |
| Funding | Series A+ (use if available) |

**Keywords That Improve Hit Rate:**
- **Include:** "GPU cloud," "GPU-as-a-service," "AI cloud provider," "inference cloud," "ML infrastructure," "bare metal GPU," "HPC cloud," "AI compute"
- **Exclude:** "AI consulting," "AI training courses," "software development," "SaaS," "marketing AI," "conversational AI"

#### LinkedIn Sales Navigator Searches

| Search Strategy | Filters |
|-----------------|---------|
| **Company search** | Keywords: "GPU cloud" OR "AI infrastructure" OR "GPU compute" + Industry: Information Technology & Services; Computer Hardware |
| **People search — reverse engineer** | Title: "VP Infrastructure" OR "Head of Cloud" OR "CTO" at companies with keywords "GPU" AND ("cloud" OR "compute") |
| **Funding signals** | Use Crunchbase integration to filter for recently funded AI infrastructure companies |

---

### 6.2 Sourcing Websites & Discovery Channels

#### Neocloud.world
| Attribute | Detail |
|-----------|--------|
| **Volume** | 187 companies listed (broadest open directory) |
| **Cost** | Free |
| **Why It Works** | Open directory specifically cataloging GPU cloud and AI infrastructure companies. Broadest coverage for discovering smaller/newer players. |
| **Navigation Tips** | Browse by category. Cross-reference against CRM — current coverage is ~40-55% of estimated TAM. |

#### SemiAnalysis ClusterMAX
| Attribute | Detail |
|-----------|--------|
| **Volume** | 60-80 providers benchmarked |
| **Cost** | Paid subscription |
| **Why It Works** | Most rigorous GPU cloud rating system. Benchmarks actual performance. If rated here, they have real deployed infrastructure. |

#### Crunchbase / PitchBook — Filtered for AI Infra
| Attribute | Detail |
|-----------|--------|
| **Filters** | Tags: "GPU cloud," "AI infrastructure," "inference platform," "AI compute." Series A+ rounds. |
| **Cost** | Paid subscription |
| **Why It Works** | Funding rounds are the strongest leading indicator. Any Series A+ in GPU/AI infrastructure = company we should know. |

#### CoinShares Mining Reports / WGMI ETF
| Attribute | Detail |
|-----------|--------|
| **Focus** | Crypto-to-AI pivot tracking |
| **Cost** | Free quarterly reports |
| **Why It Works** | Miners announced $65B in AI/HPC contracts by Oct 2025. WGMI ETF holdings = ready prospect list. |
| **Companies to Watch** | Applied Digital, Galaxy Digital, Stronghold, Argo Blockchain, Mawson, Northern Data Group, IREN, Core Scientific, Hut 8, TeraWulf |

#### NVIDIA Newsroom + GTC Conference
| Attribute | Detail |
|-----------|--------|
| **Why It Works** | NVIDIA's GPU allocation announcements are the single best leading indicator. Every company named is a potential target. |
| **What to Monitor** | NVIDIA newsroom, GTC keynotes (March, San Jose), regional AI factory announcements. 18+ telco partnerships in last 18 months. |
| **Key Events** | GTC (March, San Jose), OCP Global Summit, SC/Supercomputing, AI Infrastructure Day |

#### Additional Trackers
| Source | What It Covers |
|--------|---------------|
| DataCentre Magazine / InterGlobix | Industry press covering neocloud launches and facility announcements |
| Data Centre World Conference | Exhibitor/speaker lists for AI-focused colos |
| Datacloud Global Congress | European AI infrastructure focus — sovereign cloud opportunities |

---

### 6.3 Neocloud Sub-Segments & Coverage

| Sub-Segment | Current Coverage | Est. TAM | Gap | Key Source |
|-------------|-----------------|----------|-----|-----------|
| GPU Cloud Majors (CoreWeave, Lambda, etc.) | Good (~65%) | 25-35 | Low | SemiAnalysis, Crunchbase |
| Hyperscaler GPU Services | Good (~75%) | 5-7 | Low | Direct monitoring |
| AI Chip + Cloud (Cerebras, Groq, etc.) | Good (~65%) | 10-15 | Low | Crunchbase |
| Crypto-to-AI Pivots (IREN, Hut 8, etc.) | Moderate (~50%) | 20-25 | Medium | CoinShares, WGMI ETF |
| Sovereign/Telco GPU Clouds | Thin (~25%) | 30-40 | **High** | NVIDIA Newsroom, gov't announcements |
| Serverless/Inference-as-a-Service | Thin (35-45%) | 25-35 | **High** | Crunchbase, ProductHunt |
| GPU Marketplaces/Aggregators | Moderate (~50%) | 15-20 | Medium | Neocloud.world |
| Regional/Emerging Market | Thin (~35%) | 50-70 | **High** | NVIDIA AI Nations, gov't programs |
| European Bare Metal (Hetzner, OVH) | Thin (~40%) | 15-25 | Medium | Euro-IX, RIPE NCC |

---

### 6.4 Neocloud Buying Signals

| Signal | Where to Monitor | Why It Matters |
|--------|-----------------|----------------|
| GPU cluster deployment at colocation facility | Press releases, colo tenant lists | They need private connectivity between clusters and cloud |
| Egress cost complaints on social media | Twitter/X, LinkedIn, HN | Public internet egress at $0.05-0.09/GB; Direct Connect = $0.02/GB |
| Slow training runs mentioned | Technical blogs, social media | Network bottleneck they may not diagnose correctly |
| Network engineer hire (first one) | LinkedIn | Company just realized they have a network problem |
| Multi-site expansion to second facility | Press, job postings | Inter-facility connectivity now needed |
| Colocation tenant list inclusion | PeeringDB, Cloudscene, colo provider websites | Confirms physical presence; colo is the deployment point |

---

## 7. Cross-Segment Sources & Signals

Several sources and signal channels apply across multiple ICP segments. Use these as supplemental intelligence layers on top of segment-specific primary sources.

### 7.1 LinkedIn Sales Navigator

| Use Case | How to Use | Segments |
|----------|-----------|----------|
| Leadership change alerts | Set alerts for CTO/VP Eng/VP Network title changes at target companies | All |
| Job posting monitoring | Track "network automation," "SDN," "DWDM" job postings | All |
| Company news alerts | Monitor expansion, M&A, partnership announcements | All |
| Contact discovery | Find and map decision-maker org charts at target accounts | All |
| Competitor engagement tracking | See who's engaging with Megaport, Lumen, Equinix content | Colo, Fiber |

### 7.2 SEC Filings / Earnings Calls

| Signal | What to Search For | Segments |
|--------|-------------------|----------|
| M&A announcements | 10-K/10-Q filings for acquisition language | Network, Fiber |
| Network investment language | CapEx breakdowns mentioning "network modernization" | Network, Fiber |
| Competitive pressure mentions | References to cloud providers, NaaS, or instant provisioning | All |
| Pivot language (crypto-to-AI) | Change in business description, GPU procurement mentions | Neocloud |
| Revenue mix shifts | Connectivity vs. space/power revenue trends | Colo |

### 7.3 Industry Press & News

| Publication | Focus | Best For |
|-------------|-------|----------|
| Light Reading (lightreading.com) | Telecom carrier news, technology trends | Network Operators, Fiber |
| Fierce Telecom (fiercetelecom.com) | Competitive telecom, carrier news | Fiber, Network |
| Data Center Knowledge (datacenterknowledge.com) | Data center operations, builds, trends | Colocation, Neocloud |
| Capacity Media (capacitymedia.com) | Wholesale, carrier, subsea, infrastructure | Fiber, Network |
| Datacenter Dynamics (datacenterdynamics.com) | DC operations, builds, AI infrastructure | Colocation, Neocloud |
| InterGlobix (interglobix.com) | Subsea, international connectivity | Network (Int'l) |
| Broadband Communities (bbcmag.com) | Fiber deployment, FTTH, rural broadband | Fiber Operators |
| ISP Planet / TMCnet | ISP/carrier industry news | Fiber, MSP |

### 7.4 Hyperscaler Region Announcements

Monitor AWS, Azure, and GCP new region/availability zone announcements. Every new cloud region creates demand for private connectivity at nearby colos and through regional fiber operators.

| Provider | Where to Monitor |
|----------|-----------------|
| AWS | aws.amazon.com/about-aws/global-infrastructure/regions_az/ + press releases |
| Azure | azure.microsoft.com/en-us/explore/global-infrastructure + blog |
| Google Cloud | cloud.google.com/about/locations + blog |

### 7.5 International Sources

| Source | Access | Coverage |
|--------|--------|----------|
| RIPE NCC (stat.ripe.net) | Free | EMEA network operator data — ASN, routing, peering |
| Euro-IX (euro-ix.net) | Free | European Internet Exchange data — IX members are network operators |
| Sovereign AI Programs | Government websites, NVIDIA AI Nations | Canada ($2B), India ($1.25B), EU AI Factories, Saudi (HUMAIN), UAE (Core42) |
| APNIC (apnic.net) | Free | Asia-Pacific network operator registry |

---

## 8. Buying Signal Integration Framework

**Sourcing identifies WHO to target. Buying signals identify WHEN to prioritize them.** Layer these signals onto sourced records to create tiered outreach priority.

### Universal Good Fit Signals (All Segments)

| Signal | Why It Matters | How to Detect |
|--------|---------------|---------------|
| Provisioning takes 30-90+ days | Direct pain MaiaEdge solves | Discovery calls, conference talks, social media |
| Currently using Megaport/Equinix Fabric | Margin recapture opportunity | Website, PeeringDB, press releases |
| Mentions "visibility" or "blind spot" problems | Hop-by-hop telemetry is direct value | Conference talks, LinkedIn posts, discovery |
| Has Type 2 circuits or partner NNIs | Federation value proposition | Website, PeeringDB peering data |
| Within 200 miles of hyperscaler announcement | Cloud on-ramp demand incoming | Hyperscaler region announcements + geo mapping |
| Stranded fiber/underutilized capacity | Monetization opportunity | Earnings calls, investor presentations |
| New CTO/VP Engineering (last 12 months) | New leader = new budget = new priorities | LinkedIn Sales Navigator alerts |

### Account Tiering Logic

| Tier | Criteria | Action |
|------|----------|--------|
| **Tier 1 (High)** | Colo + Mid-Size + Hyperscaler <50mi; Fiber + Using NaaS; Leadership change in last 90 days; Neocloud with 5+ facilities | Active outreach, multi-touch, executive engagement |
| **Tier 2 (Standard)** | Colo/Fiber mid-size without trigger; Large Network Operator; Neocloud 2-4 facilities; MSP with significant scale | Standard outreach sequence, monitor for triggers |
| **Tier 3 (Low)** | Small scale; MSP/Aggregator; Early-stage neocloud; Fiber outside AI corridors | Nurture, trigger-based outreach only |

### Universal Disqualification Criteria

**IMMEDIATE DISQUALIFICATION — If ANY of these are true, exclude:**
- No owned or operated infrastructure (pure software company or enterprise consumer)
- Already deployed Lumen Private Connectivity Fabric (competitor lock-in)
- Budget holder says "we're not looking at this for 18+ months"
- Company in bankruptcy or acquisition limbo
- Pure cloud provider (AWS, Azure, GCP) — route to partnerships
- Pure reseller/VAR with no recurring services

---

## 9. Source Access Quick Reference

### Free Sources

| Source | URL / Access Method | Primary Segment |
|--------|-------------------|-----------------|
| PeeringDB | peeringdb.com/api or peeringdb.com/advanced_search | Colo + Network |
| FCC Broadband Data Collection | broadbandmap.fcc.gov (download bulk data) | Fiber |
| DataCenterMap | datacentermap.com (browse by state/region) | Colo |
| Cloudscene | cloudscene.com (free tier) | Colo + Network |
| Submarinecable.com | submarinecable.com (browse landing stations) | Colo |
| ARIN ASN Registry | whois.arin.net or ftp.arin.net (bulk downloads) | Network |
| HE BGP Toolkit | bgp.he.net (ASN lookup, peering) | Network |
| State PUC Lists | "[State] Public Utility Commission CLEC list" | Fiber |
| Neocloud.world | neocloud.world (open directory) | Neocloud |
| Baxtel | baxtel.com | Colo |
| RIPE NCC | stat.ripe.net (EMEA) | Network (Int'l) |
| Euro-IX | euro-ix.net (European IX) | Network (Int'l) |

### Paid / Relationship Sources

| Source | Access Method | Primary Segment |
|--------|-------------|-----------------|
| Data Center Hawk | datacenterhawk.com (subscription) | Colo |
| Fiber Locator | fiberlocator.com (subscription) | Fiber |
| SemiAnalysis ClusterMAX | semianalysis.com (subscription) | Neocloud |
| Crunchbase / PitchBook | crunchbase.com / pitchbook.com (subscription) | Neocloud |
| Conference Attendee Lists | Contact event organizers post-event ($1-2K) | All |
| Trade Associations (NTCA, FBA, ACA, MEF) | Membership directories | Fiber, Network |

### Key Conferences by Segment

| Conference | Proven Hit Rate | Best Segments | Timing |
|-----------|----------------|---------------|--------|
| PTC (Pacific Telecom Council) | **92%** | All (especially Network, Fiber) | January, Honolulu |
| NANOG | 65-75% | Network Operators | Multiple per year |
| Capacity Conference | 55-65% | Fiber, Network | Multiple global events |
| Data Center World | 55-65% | Colocation | Annual, varies |
| Channel Partners Conference | 50-60% | MSP/Aggregators | Annual |
| NVIDIA GTC | Emerging | Neocloud | March, San Jose |
| OCP Global Summit | Emerging | Neocloud | Annual |

---

**MAIAEDGE** | Confidential | February 2026 | Go-to-Market Operations
