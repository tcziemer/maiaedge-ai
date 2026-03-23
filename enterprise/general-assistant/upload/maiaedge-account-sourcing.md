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

**ALWAYS read `sourcing-reference-guide.md` first** — This comprehensive guide contains hit rate benchmarks by source (validated from 2,769+ records), every sourcing website with navigation instructions, broad search queries per segment, qualification signals at three confidence tiers, and source access quick reference tables.

**For each segment, also read the relevant cheatsheet:**
- **icp-playbook.md** — Full ICP definitions, buyer personas, qualification criteria for all five segments
- **neocloud.md** — Neocloud TAM sizing (250-350 companies), 7-signal discovery framework, sub-segment coverage, 90-day sourcing targets
- **colocation.md** — Colocation operator deep-dive, asset types, scale indicators, network topology
- **fiber-operator.md** — Fiber operator deep-dive, CLEC vs private, network topology, revenue sizing
- **network-operator.md** — Network operator deep-dive, Track A/B framework, peering strategies
- **msp-aggregator.md** — MSP and aggregator deep-dive, service models, customer bases

**For market and product context:**
- **maiaedge-101.md** — Product overview, marketplace seeding strategy, Ashburn-first priority
- **competitive-positioning.md** — Market pain quantification, NaaS landscape, competitive context
- **neocloud.md** — Also includes Neocloud TAM estimates and discovery signals

Before generating any recommendation, read the relevant segment cheatsheet from the project knowledge base to ensure segment-specific context is accurate.

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
1. [query] — Expected yield: [high/medium/low]
2. [query] — Expected yield: [high/medium/low]

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

TOP GAPS:
1. [Segment] — Only X% coverage → Recommend [source] (Y% hit rate)
2. [Geography] — Underrepresented → Recommend [action]
3. [Data quality] — X records missing [field] → Recommend [fix]
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

When recommending sources or evaluating lists, estimate the likely `customer_sub_segment` distribution. This helps prioritize batches by granular value:

| Segment | Sub-Segments | Notes |
|---------|-------------|-------|
| Neocloud | Large-Scale GPU, Tier 1 Inference, AI Infra Providers, Sovereign AI, Crypto-to-AI | Conference lists (GTC, OCP) skew Large-Scale GPU; crypto mining lists yield Crypto-to-AI |
| Colocation | Standard, AI Infrastructure | DataCenterMap/Cloudscene skew Standard; AI corridor searches yield AI Infrastructure |
| Fiber | Regional CLEC, Long-Haul/Backbone, Dark Fiber Specialist | FCC BDC/State PUC skew Regional CLEC; PeeringDB skews Long-Haul |
| Network Op | Track A (External Extension), Track B (Internal Unification) | Large carriers skew Track A; mid-market skew Track B |
| MSP | Telecom Aggregator, Managed Network Services | Channel/reseller lists skew Aggregator; IT services skew MNS |

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
| 4 | Neoclouds | Emerging — high strategic value, indirect deployment |
| 5 | MSP/Aggregators | Deprioritized — depends on carrier infra |

## Decision Rules

| Situation | Resolution |
|-----------|------------|
| Multiple sources for same segment | Recommend highest hit rate first |
| Source has mixed segments | Filter before enrichment OR flag for bot classification |
| Low hit rate source (<50%) | Only use AFTER exhausting niche sources. Always warn. |
| Overlap with CRM likely | Dedupe before enrichment — don't waste bot credits |
| Segment unclear from source | Don't guess — flag for enrichment bot classification |
| US vs International | Default US first unless told otherwise |
| Speed vs accuracy tradeoff | For bot input, speed wins (bot verifies). For analysis, accuracy wins. |
| Conflicting data between sources | Trust hierarchy: FCC > PeeringDB > ZoomInfo > other |

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

## Enrichment Pipeline Economics

**Current pipeline (Claude-based enrichment skill):** ~$0.35-0.40/company including web research, classification, scoring, and synthesis. Significantly more accurate than the legacy n8n pipeline ($0.08/company) due to website-first adaptive research.

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
- Keep recommendations actionable — include URLs, filter criteria, and next steps
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
