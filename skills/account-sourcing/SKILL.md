---
name: account-sourcing
description: "MaiaEdge account sourcing strategist. Finds, evaluates, and prioritizes new prospect companies by TAM analysis, source quality assessment, and enrichment batch planning. Use when asked to find accounts, identify new prospects, evaluate source quality, generate search queries, plan enrichment batches, check CRM coverage gaps, deduplicate lists, determine hit rates, or recommend sourcing strategies. Also trigger when mentioning sourcing, prospecting, TAM coverage, whitespace, PeeringDB, FCC BDC, DataCenterMap, conference lists, or source evaluation. Ranks sources by hit rate (92% conference > 75% FCC > 70% PeeringDB > 27% ZoomInfo/Apollo). Operates across all segments with hit rate benchmarks and batch planning formulas."
---

# MaiaEdge Account Sourcing Skill

## Purpose

Find, evaluate, and prioritize new prospect companies for MaiaEdge's go-to-market pipeline. This skill is the top-of-funnel intelligence layer that feeds the enrichment pipeline (`maiaedge-company-enrichment` skill). It answers three questions:
1. **WHERE** should we source accounts? (sources ranked by hit rate)
2. **WHO** should we target? (segment-specific search queries and filters)
3. **WHEN** should we prioritize them? (buying signals and triggers)

## When to Use This Skill

Trigger on any of these patterns:
- "Find me more [segment] accounts" or "I need more colocation/fiber/network companies"
- "Where should we source next?" or "What sources should we use?"
- "Evaluate this list" or "Is this a good source?" (file uploaded)
- "What's our CRM coverage?" or "Where are the gaps?"
- "Plan the next enrichment batch" or "What should we run through the pipeline?"
- "Generate search queries for [segment]" or "What should I search in Apollo/ZoomInfo/Google?"
- "What's the hit rate for [source]?" or "Is PeeringDB better than ZoomInfo?"
- "Help me find [segment] companies in [state/region]"
- Any mention of: sourcing, prospecting, TAM coverage, whitespace, hit rates, PeeringDB, FCC BDC, DataCenterMap, conference lists, Apollo discovery, ZoomInfo search

## Knowledge Base Reference Documents

**Use these project knowledge base documents for segment context, definitions, and sourcing strategy:**

**ALWAYS read `sourcing-reference-guide.md` first**  -  This comprehensive guide contains hit rate benchmarks by source (validated from 2,769+ records), every sourcing website with navigation instructions, broad search queries per segment, qualification signals at three confidence tiers, and source access quick reference tables.

**For each segment, also read the relevant cheatsheet:**
- **icp-playbook.md**  -  Full ICP definitions, buyer personas, qualification criteria for all five segments
- **neocloud.md**  -  Neocloud TAM sizing (250-350 companies), 7-signal discovery framework, sub-segment coverage, 90-day sourcing targets
- **colocation.md**  -  Colocation operator deep-dive, asset types, scale indicators, network topology
- **fiber-operator.md**  -  Fiber operator deep-dive, CLEC vs private, network topology, revenue sizing
- **network-operator.md**  -  Network operator deep-dive, Track A/B framework, peering strategies
- **msp-aggregator.md**  -  MSP and aggregator deep-dive, service models, customer bases
- **enterprise.md**  -  Enterprise (Multi-DC ICP) deep-dive - four sub-segments (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services), HubSpot mapping, scale gate, hard disqualifiers, persona priority, lead angles by sub-segment. Anchor account: Meijer.

**For market and product context:**
- **maiaedge-101.md**  -  Product overview, marketplace seeding strategy, Ashburn-first priority
- **competitive-positioning.md**  -  Market pain quantification, NaaS landscape, competitive context
- **neocloud.md**  -  Also includes Neocloud TAM estimates and discovery signals

**For sub-segment taxonomy, disqualifiers, and TAM anchors (Phase 3 references):**
- **context/account-tiering/sub-segment-qualification.md** - Authoritative list of the 30 active sub-segment values (case-sensitive), parent/sub-segment pairing rules; replaces all stale sub-segment labels (e.g., `Tier 1 Global Incumbent` → `Tier 1 Carrier - Network Op`).
- **context/account-tiering/enrichment-protocols.md** - D1 global disqualifiers (hyperscalers / equipment vendors / OTT / pure consulting / etc.), D5 evidence-verification protocols. Sourcing must exclude D1-disqualified categories at the source-list stage, not waste enrichment credits on them.
- **context/account-tiering/sub-segment-qualification-full.md** - §3 D1 disqualifiers, §5 D3 disambiguation flowcharts, §6 anchor lists (per-sub-segment 10-15 anchors with revenue band / footprint / geographic spread for TAM benchmarking), §8 industry sources.
- **context/account-tiering/d1-global-disqualifiers.md** - working-form D1 disqualifier list for sourcing-side exclusion logic.

Before generating any recommendation, read the relevant segment cheatsheet from the project knowledge base plus `context/account-tiering/sub-segment-qualification.md` to ensure sub-segment labels and TAM benchmarks are accurate.

---

## Core Principles

1. **Source quality > volume.** 1,000 records at 70% hit rate > 2,000 at 35%. Always recommend the highest hit-rate source first.
2. **Niche infrastructure sources > broad databases.** PeeringDB, FCC BDC, conference lists outperform ZoomInfo/Apollo by 2-3x.
3. **Apollo/ZoomInfo is for contact enrichment, not discovery.** Only recommend for discovery AFTER niche sources are exhausted, and always warn about 27-51% hit rates.
4. **Deduplicate before enriching.** Never waste bot credits on companies already in CRM. Always check HubSpot first.
5. **Exhaust free sources first.** PeeringDB, FCC, DataCenterMap, Cloudscene, ARIN, State PUC lists cost nothing but time.
6. **Conference attendees self-select.** PTC26 at 92% proves event-based sourcing delivers the highest ROI.

---

## Task Routing

Determine which mode to operate in based on the user's request:

### MODE 1: SOURCE RECOMMENDATION
**Trigger:** "I need more [segment] accounts" or "Where should we source?"

Steps:
1. Read the relevant segment cheatsheet from the project knowledge base (see Knowledge Base Reference Documents section above)
2. Check current CRM coverage for that segment using HubSpot search (if available)
3. Recommend sources ranked by hit rate (use the Hit Rate Quick Reference table below)
4. Estimate yield: raw records × hit rate = ICP companies
5. Flag overlap risk with existing CRM
6. Provide specific access methods and filters

Output format:
```
SOURCING RECOMMENDATION: [Segment]

OPTION 1 (Recommended): [Source Name]
- Expected hit rate: X%
- Estimated raw records: Y
- Estimated ICP yield: Z companies
- Overlap risk: Low/Medium/High
- Access: [URL and navigation steps]
- Recommended filters: [specific criteria]

OPTION 2: [Alternative source]
...

SKIP: [Source to avoid and why]
```

### MODE 2: SEARCH QUERY GENERATION
**Trigger:** "Generate search queries for [segment]" or "What should I search in Apollo/Google?"

Steps:
1. Read the relevant segment cheatsheet from the project knowledge base for persona and segment-specific terminology
2. Tailor queries to the user's specified platform (Google, Apollo, ZoomInfo, LinkedIn)
3. Include both include AND exclude keywords
4. Estimate precision level for each query
5. If geographic targeting is needed, inject state/city into templates

Output format:
```
SEARCH QUERIES: [Segment] on [Platform]

HIGH PRECISION (use first):
1. [query]  -  Expected yield: [high/medium/low]
2. [query]  -  Expected yield: [high/medium/low]

MEDIUM PRECISION (use to supplement):
3. [query]
4. [query]

EXCLUDE KEYWORDS (always apply):
- [list of terms to exclude]

ESTIMATED HIT RATE WITH THESE FILTERS: X-Y%
```

### MODE 3: SOURCE EVALUATION
**Trigger:** "Evaluate this list" or "Is this a good source?" (file uploaded)

Steps:
1. Examine the file (columns, row count, source metadata)
2. Assess source type (conference list, database export, scraped, etc.)
3. Estimate hit rate based on source type and filters used (reference benchmarks in Hit Rate Quick Reference below)
4. Sample company names to estimate segment mix
5. Check for overlap with CRM if HubSpot is accessible
6. Deliver verdict: Pursue / Filter First / Skip

Output format:
```
SOURCE EVALUATION: [File/Source Name]
- Source type: [Conference list / Database export / Scraped / etc.]
- Record count: X
- Expected hit rate: X% (because [reason])
- Likely segment mix: X% Colo, Y% Fiber, Z% Network, W% Other
- Quality concerns: [list]
- Overlap with CRM: [estimate]

VERDICT: [Pursue / Filter First / Skip]
NEXT STEP: [specific action]
```

### MODE 4: CRM GAP ANALYSIS
**Trigger:** "What's our CRM coverage?" or "Where are the gaps?"

Steps:
1. Query HubSpot for current company counts by customer_segment property
2. Query HubSpot for geographic distribution (state/country)
3. Compare against TAM estimates from relevant segment cheatsheets:
   - Colocation Operators: 800-1,000 US
   - Fiber Operators: 1,200-1,500 US
   - Network Operators: 800-1,000 US
   - MSP/Aggregators: 2,000-3,000 US
   - Neoclouds: 250-350 global
   - Enterprise (Multi-DC ICP): ~300-500 US (Fortune 1000 filtered by 4 verticals + scale gate). Sub-segment breakdown: ~80-120 Financial Services, ~60-100 Healthcare Systems (Top 100 IDNs ± expansion), ~60-100 Retail and Distribution (NRF Top 100 ± expansion), ~30-50 Outsourcing Services (Everest Group BPO rankings).
4. Identify coverage gaps and recommend sourcing actions

Output format:
```
CRM SNAPSHOT: [Date]

| Segment | Count | % of CRM | Est. TAM | Coverage % |
|---------|-------|----------|----------|------------|
| Colo    | X     | X%       | 800-1K   | X%         |
| Fiber   | X     | X%       | 1.2-1.5K | X%         |
| Network | X     | X%       | 800-1K   | X%         |
| MSP     | X     | X%       | 2-3K     | X%         |
| Neocloud| X     | X%       | 250-350  | X%         |
| Enterprise (Multi-DC ICP) | X | X% | 300-500 | X% |

TOP GAPS:
1. [Segment]  -  Only X% coverage → Recommend [source] (Y% hit rate)
2. [Geography]  -  Underrepresented → Recommend [action]
3. [Data quality]  -  X records missing [field] → Recommend [fix]
```

### MODE 5: BATCH PLANNING
**Trigger:** "Plan the next enrichment batch" or "What should we run through the pipeline?"

Steps:
1. Assess available source lists and their quality
2. Prioritize: Colo > Fiber > Network > MSP (segment priority)
3. Prioritize: Higher hit rate sources first within each segment
4. Estimate enrichment cost ($0.08/company) and time (~1 min/company)
5. Recommend batch sizes (150 optimal for standard, 500 for large)
6. Flag deduplication needs

Output format:
```
BATCH PLAN: [Campaign/Purpose]

BATCH 1: [Segment] from [Source]
- Input: X companies
- Est. ICP yield: Y (at Z% hit rate)
- Expected sub-segment mix: [e.g., "~60% Regional CLEC, ~30% Long-Haul, ~10% Dark Fiber"]
- Est. cost: $X | Est. time: X hours
- Dedup status: [Done / Needed against HubSpot]
- Priority: HIGH/MEDIUM/LOW

BATCH 2: ...

TOTAL: X companies | $Y cost | Z hours
EXPECTED ICP YIELD: X companies at blended Y% hit rate
```

### Sub-Segment Awareness

When recommending sources or evaluating lists, estimate the likely `customer_sub_segment` distribution. Labels below use the EXACT HubSpot enum values from `context/account-tiering/sub-segment-qualification.md` (30 active values; case-sensitive). This helps prioritize batches by granular value AND ensures source recommendations map cleanly to downstream import-processor writes.

| Segment | Sub-Segments (active enum values - VERIFIED LIVE 2026-05-14) | Notes |
|---------|-------------|-------|
| Neocloud (5 + Greenfield) | `Large Scale GPU - Neocloud`, `Tier 1 Inference - Neocloud`, `AI Infrastructure providers - Neocloud` (lowercase p), `Sovereign AI Clouds - Neocloud`, `Crypto to AI - Neoclouds` (trailing s), `Greenfield` (cross-segment) | Conference lists (GTC, OCP) skew Large Scale GPU; crypto-mining + crypto-real-estate-landlord lists yield `Crypto to AI - Neoclouds` (inclusive of both operator and landlord per Cooper 2026-05-14); announced-only / pre-revenue builds -> `Greenfield` |
| Colocation (4 + Greenfield) | `Standard - colo`, `AI Signals - colo`, `Modular - colo`, `Hyperscale Wholesale - colo`, `Greenfield` (cross-segment) | DataCenterMap / Cloudscene skew `Standard - colo`; AI-corridor searches yield `AI Signals - colo`; distributed/prefab/edge-pod builders yield `Modular - colo`; Synergy Research wholesale rankings yield `Hyperscale Wholesale - colo`; announced-only builds -> `Greenfield` |
| Fiber (6) | `Regional CLEC - Fiber operator`, `Long Haul / Backbone - Fiber operator`, `Dark Fiber Specialist - Fiber Operator` (capital O), `Tier 2 National Wholesale - Fiber operator`, `Regional Cable Operator - Fiber operator`, `Municipal / Cooperative - Fiber operator` | FCC BDC / State PUC skew `Regional CLEC - Fiber operator`; PeeringDB skews `Long Haul / Backbone`; Omdia + 10-K disclosures yield `Tier 2 National Wholesale` (Zayo, Lightpath, Uniti+Windstream, EXA EU); NTCA / NRECA / state broadband consortium directories yield `Municipal / Cooperative`. NOTE: `Regional CLEC - Fiber operator` is a framework default - sourcing should flag CLEC candidates for positive-evidence verification downstream |
| Network Op (5) | `Tier 1 Carrier - Network Op`, `Pure Wholesale Carrier - Network Op`, `Cable MSO Enterprise Division - Network Op`, `International Backbone Specialist - Network Op`, `Subsea cable operator` (NEW 2026-05-14; lowercase, NO `- Network Op` suffix; 30th active sub-segment) | Tier 1 anchors from Wikipedia Tier 1 Network + Statista Top Telecoms + GSMA Intelligence; Pure Wholesale Carrier from PeeringDB Tier 1 IP transit + 10-K filings (Cogent, Arelion, EXA Infrastructure); Cable MSO Enterprise Division from cable parent B2B revenue (Comcast Business, Spectrum Enterprise); International Backbone Specialist from TeleGeography Submarine Cable Map + Omdia (Tata, PCCW Global, Telstra International, HGC); `Subsea cable operator` from Submarine Telecoms Forum + TeleGeography pure-play subsea (Aqua Comms, Seaborn, BW Digital, Hawaiki). Use `network_op_track` field (`external_extension` / `internal_external_unification`) NOT a sub-segment value for the Track A/B classification (retired 2026-05-13). |
| MSP (5) | `Telecom Aggregator - MSP`, `Managed Network Services - MSP`, `TSD Technology Services Distributor - MSP`, `Master Agent - MSP`, `Cloud + Telecom Hybrid MSP - MSP` | Channel / reseller lists skew `Telecom Aggregator - MSP` (framework default - needs positive evidence); IT integrators + Cisco/Fortinet partner directories yield `Managed Network Services - MSP`; Omdia TSD Market Report (Telarus, AVANT, Intelisys/ScanSource, AppDirect, Sandler, Bridgepointe) yields `TSD Technology Services Distributor - MSP`; smaller regional / vertical-focused agencies (X4 Solutions, CyberNet) yield `Master Agent - MSP`; AWS Premier / Azure Expert / GCP Premier partners with network services yield `Cloud + Telecom Hybrid MSP - MSP`. The `- Network Operator` suffix is retired (Phase 1.7c.1). |
| Enterprise (Multi-DC ICP) (4) | `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise` | Source dictates sub-segment: Fortune 1000 financial -> Financial Services; Modern Healthcare / Becker's IDN -> Healthcare Systems; NRF Top 100 -> Retail and Distribution; Everest Group BPO -> Outsourcing Services. Manufacturing / Energy / Logistics / Government / Defense / SaaS-only are NOT Enterprise sub-segments (Watch List or out of scope per D1) |

**Retired sub-segment values (DO NOT source toward these - they are rejected by import-processor):**
- `Co-op/consortium` - replaced by `Municipal / Cooperative - Fiber operator`
- `External Extension - Network operator` - replaced by `network_op_track = external_extension`
- `Internal + external unification - Network Operator` - replaced by `network_op_track = internal_external_unification`
- `Managed Network Services - Network Operator` - replaced by `Managed Network Services - MSP`

### D1 Sourcing-Side Exclusion Logic

Per file 06 §3 and `context/account-tiering/enrichment-protocols.md`, the following categories are GLOBAL D1 DISQUALIFIERS - do not source toward them (they will be rejected downstream regardless of segment, so sourcing them wastes enrichment credits):

- **Hyperscalers and their captive infra:** AWS, Microsoft Azure, GCP, Oracle Cloud, IBM Cloud, Alibaba Cloud, Tencent Cloud (and any wholly-owned infra subsidiary)
- **Equipment vendors / hardware manufacturers:** Cisco, Juniper, Arista, NVIDIA (when sold as a vendor, not as a NeoCloud renter of its own GPUs), Ciena, Nokia, Ericsson, Dell, HPE, Supermicro
- **Over-the-top (OTT) content and SaaS:** Netflix, Hulu, Spotify, Salesforce, Workday, ServiceNow, Adobe - they CONSUME network but don't operate ICP infra
- **Pure consulting / advisory firms:** Deloitte (consulting arm), McKinsey, BCG, Bain, Accenture (consulting, not BPO) - see edge-case-researcher Rule 5 for dual-arm BPO/consulting disambiguation
- **Pure professional services:** law firms, accounting firms, staffing agencies, marketing agencies
- **Pure software / SaaS:** Salesforce, Workday, Notion, Asana (no multi-DC infra)
- **Manufacturers, Energy/Utilities, Logistics/Supply Chain, Government/Defense (direct), Education (direct):** Watch List or out-of-scope per Enterprise §3 - sourcing these as Enterprise is a known false-positive trap
- **Defunct companies, parked domains, holding-company-only shells**

Verified D1 disqualifiers MUST be excluded at the source-list filter stage. Do not pass them into the enrichment pipeline (`maiaedge-company-enrichment`).

### MODE 6: DEDUPLICATION CHECK
**Trigger:** "Check for duplicates" or before any batch goes to enrichment

Steps:
1. Get domain list from the source file
2. Search HubSpot for each domain (or batch search if many)
3. Flag exact matches (same domain)
4. Flag potential subsidiaries or aliases (similar names, parent companies)
5. Report net-new count after dedup

Output: Count of matches, net-new companies, and flagged subsidiaries for review.

---

## Segment Priority Order

Always recommend sourcing in this priority unless the user specifies otherwise:

| Priority | Segment | Why |
|----------|---------|-----|
| 1 | Colocation Operators | Highest product fit, fastest sales cycle |
| 2 | Fiber Operators | Largest whitespace opportunity, biggest TAM gap |
| 3 | Network Operators | Good fit but longer sales cycles |
| 4 | Neoclouds | Emerging  -  high strategic value, indirect deployment |
| 5 | MSP/Aggregators | Deprioritized  -  depends on carrier infra |
| 6 | Enterprise (Multi-DC ICP) | New ICP as of 2026-05-11. Tier 2 ceiling (no Tier 1 path). Anchor: Meijer. Smaller per-deal TAM than operator segments; longer enterprise procurement cycles. Allocate ~15-20% of monthly sourcing capacity. |

## Decision Rules

| Situation | Resolution |
|-----------|------------|
| Multiple sources for same segment | Recommend highest hit rate first |
| Source has mixed segments | Filter before enrichment OR flag for bot classification |
| Low hit rate source (<50%) | Only use AFTER exhausting niche sources. Always warn. |
| Overlap with CRM likely | Dedupe before enrichment  -  don't waste bot credits |
| Segment unclear from source | Don't guess  -  flag for enrichment bot classification |
| US vs International | Default US first unless told otherwise |
| Speed vs accuracy tradeoff | For bot input, speed wins (bot verifies). For analysis, accuracy wins. |
| Conflicting data between sources | Trust hierarchy: FCC > PeeringDB > ZoomInfo > other |

## TAM Anchor Lists (file 06 §6)

For every sub-segment, file 06 §6 of the consolidated qualification reference contains a 10-15 company anchor list with revenue band, footprint, and geographic spread. Use these anchor lists when:
1. Sizing TAM at the sub-segment level (not just segment level) - the anchors define the "shape" of qualifying companies
2. Evaluating a source list - does the source surface companies that LOOK like the anchors (revenue, footprint, geography)?
3. Generating search queries - the anchors give you proven exemplars to seed similar-company searches

Anchor list categories in file 06 §6 (cross-reference the 30 active sub-segment values):
- §6.1 Fiber Operator anchors (per `Regional CLEC - Fiber operator` / `Long Haul / Backbone - Fiber operator` / `Dark Fiber Specialist - Fiber Operator` / `Tier 2 National Wholesale - Fiber operator` / `Regional Cable Operator - Fiber operator` / `Municipal / Cooperative - Fiber operator`)
- §6.2 Colocation anchors (per `Standard - colo` / `AI Signals - colo` / `Modular - colo` / `Hyperscale Wholesale - colo` / cross-segment `Greenfield`)
- §6.3 Network Operator anchors (per `Tier 1 Carrier - Network Op` / `Pure Wholesale Carrier - Network Op` / `Cable MSO Enterprise Division - Network Op` / `International Backbone Specialist - Network Op` / `Subsea cable operator` - Subsea anchors include Aqua Comms, Seaborn Networks, BW Digital, Hawaiki, Telxius)
- §6.4 NeoCloud anchors (per `Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds` / cross-segment `Greenfield`)
- §6.5 MSP/Aggregator anchors (per `Telecom Aggregator - MSP` / `Managed Network Services - MSP` / `TSD Technology Services Distributor - MSP` / `Master Agent - MSP` / `Cloud + Telecom Hybrid MSP - MSP`)
- §6.6 Enterprise anchors (per `Financial Services - Enterprise` / `Healthcare Systems - Enterprise` / `Retail and Distribution - Enterprise` / `Outsourcing Services - Enterprise`; Meijer is the named Retail anchor)

Always cross-check a candidate source list against the relevant §6 anchors before recommending the batch.

## Industry Sources (file 06 §8)

File 06 §8 names the authoritative industry sources for each segment. Use these as primary sources during MODE 1 (Source Recommendation) and MODE 5 (Batch Planning):

| Segment | Primary Industry Sources (file 06 §8) |
|---|---|
| Fiber | **FCC BDC** (Broadband Data Collection - definitive US fiber-footprint data), State PUC CLEC lists, NTCA member directory, USTelecom membership |
| Colocation | **Synergy Research Group** (wholesale colo rankings, hyperscale capacity), DataCenterMap, Cloudscene, Data Center Hawk (paid), JLL / CBRE data center market reports |
| Network Op | **Omdia** (TSD/Tier 1 rankings), TeleGeography (network footprint), PeeringDB (AS-level peering), Submarine Telecoms Forum (subsea) |
| NeoCloud | **SemiAnalysis ClusterMAX** (GPU-cluster rankings), MLPerf submissions, NVIDIA partner directory, Crusoe / CoreWeave / Lambda alumni-network signal |
| MSP/Aggregator | Channel Partners 360 rankings, MSP501, MEF member list, Cisco / Cato / VeloCloud / Versa partner directories |
| Enterprise (Multi-DC ICP) | Fortune 1000 + vertical filter, Modern Healthcare Top 100 Health Systems, Becker's Hospital Review IDN rankings, NRF Top 100 Retailers, **Everest Group BPO rankings**, SEC EDGAR 10-Ks for SOX-regulated financials (DC disclosures) |

These industry sources are higher-precision than ZoomInfo/Apollo broad search and should be exhausted first per the Core Principle "Niche infrastructure sources > broad databases."

## Hit Rate Quick Reference

Keep these benchmarks top-of-mind for every recommendation:

| Source | Hit Rate | Cost |
|--------|----------|------|
| PTC Conference | 92% | $1-2K |
| FCC BDC | 75-85% | Free |
| PeeringDB | 70-80% | Free |
| State PUC Lists | 70-80% | Free |
| DataCenterMap | 60-70% | Free |
| Cloudscene | 60-70% | Free |
| Data Center Hawk | 65-75% | Paid |
| NANOG | 65-75% | Membership |
| ZoomInfo/Apollo broad | 27-51% | Paid |
| Fortune 500/1000 filtered by vertical | 40-50% (financial); 20-30% (retail); 30-40% (healthcare IDN); 50-60% (BPO via Everest Group) | Free / Paid |
| Modern Healthcare Top 100 Health Systems | 30-40% | Free |
| Becker's Hospital Review IDN rankings | 30-40% | Free |
| NRF Top 100 Retailers | 20-30% (multi-DC corporate IT filter is tight) | Free |
| Everest Group BPO rankings | 50-60% (pre-filtered list) | Paid / Free reports |
| 10-K filings (DC disclosures for SOX-regulated financials) | High precision per record | Free (SEC EDGAR) |
| Equinix / CoreSite customer logo pages | 70-80% (enterprise fabric customers are pre-qualified) | Free |
| LinkedIn senior network-role job postings at qualifying companies | 60-70% (job postings ARE the in-house-net-eng signal) | Free / Sales Nav |

## Enrichment Pipeline Economics

**Pipeline cost:** ~$0.35-0.40/company including web research, classification, scoring, and synthesis. Website-first adaptive research keeps call volume focused and accuracy high.

| Batch Size | Time | Est. Cost |
|------------|------|-----------|
| 50 companies | ~50 min | ~$18-20 |
| 150 companies | ~2.5 hrs | ~$53-60 |
| 500 companies | ~8 hrs | ~$175-200 |

At 70% hit rate: **~$0.51-0.57 per ICP company**
At 35% hit rate: **~$1.00-1.14 per ICP company**

The difference over 500 companies = ~$250 in wasted processing. Source quality pays for itself even more at higher per-company costs.

---

## Output Formatting Rules

- Use markdown tables for structured data
- Bold key numbers, recommendations, and verdicts
- Always recommend ONE best option, not equal-weight lists
- Never recommend ZoomInfo/Apollo broad search without the hit rate warning
- Always reference specific hit rate benchmarks from the Hit Rate Quick Reference table
- Keep recommendations actionable  -  include URLs, filter criteria, and next steps
- If HubSpot is available, always check CRM overlap before recommending a batch

---

## Knowledge Base Integration Notes

The original skill referenced `references/sourcing-reference-guide.md` via a directory path. This updated version points to `sourcing-reference-guide.md` as a project knowledge document (read directly, no directory prefix needed), plus adds segment cheatsheets for supplemental context.

**What changed:**
- Updated sourcing-reference-guide.md path from `references/` directory to project knowledge document
- Redirected all segment context requests to the relevant cheatsheets (colocation.md, fiber-operator.md, neocloud.md, network-operator.md, msp-aggregator.md)
- Kept all built-in benchmarks from this skill file (hit rate table, segment priorities, decision rules, enrichment economics, batch planning formulas)
- Retained all six task routing modes unchanged

**What stays the same:**
- All sourcing logic and methodology
- All hit rate benchmarks (validated from 2,769+ records)
- All decision rules and segment priorities
- All enrichment cost estimates and batch planning formulas
- All output formatting standards
- All core principles

**How to use:**
When asked for sourcing recommendations or segment-specific guidance, consult the relevant segment cheatsheet from the project knowledge base (neocloud.md, colocation.md, fiber-operator.md, network-operator.md, msp-aggregator.md) for persona definitions, qualification signals, and segment-specific discovery tactics. Use the hit rate benchmarks and batch planning formulas in this skill file to estimate sourcing yield and cost-effectiveness.
