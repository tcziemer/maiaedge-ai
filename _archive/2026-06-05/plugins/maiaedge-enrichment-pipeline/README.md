# MaiaEdge Enrichment Pipeline Plugin

A coordinated Cowork plugin that bundles four specialized skills into a complete account sourcing, enrichment, and qualification pipeline for MaiaEdge's go-to-market operations.

**Version:** 1.0.0
**Author:** MaiaEdge RevOps
**Keywords:** enrichment, sourcing, hubspot, import, classification, prospecting, pipeline

---

## Overview

The MaiaEdge Enrichment Pipeline is a four-skill orchestration for sourcing, researching, classifying, and importing prospect accounts into HubSpot. The pipeline moves companies from discovery → research → classification → import with no manual editing required.

### Pipeline Capabilities

- **Source new accounts** by ICP segment with hit rate analysis
- **Enrich companies** using website-first adaptive research (6-8 searches vs. 25+ in legacy pipeline)
- **Classify** into 5 customer segments + 15 sub-segments
- **Score and tier** on 4 dimensions: Strategic Fit, Problem Awareness, Timing/Urgency, Outreach Quality
- **Produce HubSpot-ready files** with exact property mapping (zero manual editing)
- **Identify and research edge cases** to recover false negatives from initial enrichment

### Key Advantages Over Legacy Pipeline

| Dimension | Legacy n8n | New Claude Pipeline |
|-----------|-----------|-------------------|
| **Speed** | 25+ searches/company | 6-8 searches/company |
| **Cost** | $0.08/company | $0.35-0.40/company |
| **Accuracy** | Limited by blind search | Website-first adaptive strategy |
| **Website access** | No | Yes — reads actual company sites |
| **Edge case recovery** | No second chance | Dedicated edge case research skill |
| **Hit rate** | 27-51% (ZoomInfo/Apollo) | 70-85% (niche sources) |

---

## Components

### 1. **Account Sourcing Skill** (`account-sourcing/SKILL.md`)
Find new prospect companies by ICP segment.

**When to use:**
- Need to source a segment you're underrepresented in
- Want to evaluate the quality of a source file
- Need segment-specific search queries
- Want gap analysis on current CRM coverage

**Outputs:**
- Recommended sources ranked by hit rate (validated from 2,769+ records)
- Segment-specific search queries (for Apollo, ZoomInfo, Google, LinkedIn)
- Batch plans with cost/time estimates
- CRM coverage analysis

**Key framework:** Source quality > volume. PeeringDB/FCC/conference lists > Apollo/ZoomInfo by 2-3x.

---

### 2. **Company Enrichment Skill** (`company-enrichment/SKILL.md`)
Research, classify, and score companies for HubSpot import.

**When to use:**
- Have a list of companies to research
- Need HubSpot-ready import files
- Want classification into customer segments + sub-segments
- Need outreach priority scoring

**Research methodology:**
- **Phase 1**: Read company website (homepage + services page)
- **Phase 2**: Run segment-specific searches based on Phase 1 routing
- **Phase 3**: Fill gaps and verify exclusions

**Outputs:**
- **Qualified Accounts XLSX** with two tabs:
  - Tab 1: HubSpot Import (14 columns, zero manual edits needed)
  - Tab 2: Companion Data (scores, email context, research metadata)
- **Excludes Log** (company names, domains, exclusion reasons)

**Average research depth:** 5-6 searches for clear qualifiers, 6-8 for thin websites, 2 for obvious excludes.

---

### 3. **Import Processor Skill** (`import-processor/SKILL.md`)
Transform enrichment output into HubSpot-optimized import files.

**When to use:**
- Processing enrichment output from the enrichment skill
- Need exact HubSpot property value mapping
- Want to identify edge cases for deeper research
- Need audit trail of excludes

**Transformations:**
- Segment mapping (e.g., "Colocation Operator" → "Data Center Colo Provider")
- Property name mapping (enrichment columns → HubSpot internal names)
- Multi-select formatting (semicolon-separated, no spaces)
- Domain cleaning (strip http://, www.)
- Tier assignment (Tier 1/2/3 based on priority score)

**Outputs:**
- **hubspot_import_qualified.xlsx** (ready to upload, zero edits)
- **edge_cases_for_research.xlsx** (flagged for manual review)
- **definitive_excludes.xlsx** (normalized exclusion categories)

**Edge case detection:** 6 rules to catch accounts that may have been incorrectly excluded:
1. Retail ISP with infrastructure signals (may be wholesale fiber operator)
2. Low employee count with infra metrics (data error or cooperative)
3. Insufficient data but identifiable business
4. Vendor/contractor that also operates infrastructure
5. Enterprise/utility with telecom-adjacent business
6. Bot processing failures

---

### 4. **Edge Case Researcher Skill** (`edge-case-researcher/SKILL.md`)
Deep-dive research on edge cases to determine reclassification or confirmation.

**When to use:**
- Have edge case file from the import processor
- Want to recover false negatives from initial enrichment
- Need to validate excluded accounts
- Targeting Retail ISP → Wholesale Fiber Operator reclassifications

**Research per rule:**
- **Rule 1**: Check for wholesale/B2B division (often Retail ISP + Fiber hybrid)
- **Rule 2**: Verify employee count with multiple sources (cooperatives, municipalities)
- **Rule 3**: Deep research on generic names (add state/domain to queries)
- **Rule 4**: Check for operator division alongside vendor business
- **Rule 5**: Verify open-access fiber for utilities and municipalities
- **Rule 6**: Run full enrichment methodology for bot failures
- **Rule 7**: Distinguish neoclouds from colos and vendors (what do they sell?)

**Outputs:**
- **reclassified_hubspot_import.xlsx** (reclassified accounts, HubSpot-ready)
- **confirmed_excludes.xlsx** (validated exclusions with stronger evidence)
- **edge_case_research_log.xlsx** (full audit trail)

**Recovery rates:** Rule 1: 20-40%, Rule 2: 30-50%, Rule 6: 50%+, Rule 7: 40-60%

---

## Reference Documents

Located in `references/` directory:

### Core Reference Files

1. **hubspot-values.md** — Exact HubSpot property values, dropdown options, multi-select bucketing thresholds, and formatting rules
2. **output-schemas.md** — JSON schemas for research output and email_context structure
3. **research-routes.md** — Phase 2 search templates for each segment route (Colocation, Fiber, Network, MSP, Neocloud, Exclude Verification, ISP, Fallback)
4. **fallback-messaging.md** — Segment-specific messaging angles, core problems, and value proposition templates
5. **sourcing-reference-guide.md** — Comprehensive sourcing playbook with 2,769+ validated hit rate benchmarks, sourcing websites, search queries, and buying signals by segment

### Segment Cheatsheets (referenced as project knowledge documents)

- **neocloud-cheatsheet.md** — TAM sizing, sub-segment profiles, 7-signal discovery framework
- **colocation-cheatsheet.md** — Operator context, AI infrastructure criteria, facility benchmarks
- **fiberoperator-cheatsheet.md** — CLEC vs private, route mile benchmarks, wholesale detection
- **networkoperator-cheatsheet.md** — Track A/B signals, backbone infrastructure criteria
- **msp-aggregator-cheatsheet.md** — Aggregation signals, margin dynamics, carrier ecosystem

### Supplemental References

- **icp-sales-playbook.md** — Full ICP definitions, buyer personas, qualification criteria
- **competitive-positioning.md** — Market pain quantification, NaaS landscape, competitive context
- **maiaedge-101.md** — Product overview, marketplace seeding strategy

---

## Usage Guide

### Quick Start: 3-Step Pipeline

```
Step 1: SOURCE ACCOUNTS
$ /source-accounts [segment or "all"] [optional: state]
→ CRM gap analysis + recommended sources + search queries

Step 2: ENRICH BATCH
$ /enrich-batch [company list, CSV, or XLSX]
→ Qualified Accounts XLSX + Excludes Log

Step 3a: PROCESS IMPORT
$ /process-import [enrichment output file]
→ HubSpot-ready import + edge cases file + definitive excludes

Step 3b: RESEARCH EDGE CASES (optional, if using edge cases)
$ /research-edge-cases [edge cases file]
→ Reclassified import + confirmed excludes + audit log
```

### Full Pipeline Example

**Goal:** Source 200 colocation operators, enrich them, and prepare for HubSpot import.

```
1. /source-accounts colocation
   → Get recommended sources (PeeringDB at 75-80%, DataCenterMap at 65-70%)
   → Get search queries for Apollo/ZoomInfo
   → Get batch plan: 200 companies expected → ~140-160 ICP yield

2. [User sources 200 colocation companies from recommended sources]

3. /enrich-batch [colocation_200.csv]
   → Research 200 companies (8 hrs, ~$70-80)
   → Outputs: enriched_accounts.xlsx + excludes_log.xlsx
   → Results: 130 qualified, 70 excluded

4. /process-import [enriched_accounts.xlsx]
   → Transform to HubSpot format
   → Flag edge cases: 12 Retail ISPs with infra signals, 8 low employee count with infrastructure
   → Outputs: hubspot_import_qualified.xlsx (130 accounts, ready)
             + edge_cases_for_research.xlsx (20 accounts)
             + definitive_excludes.xlsx (50 accounts)

5. /research-edge-cases [edge_cases_for_research.xlsx]
   → Deep-dive on 20 edge cases (2-4 searches each)
   → Results: 8 reclassified as Fiber Operators (wholesale divisions found)
   → Outputs: reclassified_hubspot_import.xlsx (8 accounts)
             + confirmed_excludes.xlsx (12 accounts)
             + edge_case_research_log.xlsx (audit trail)

6. [User uploads hubspot_import_qualified.xlsx (130) + reclassified_hubspot_import.xlsx (8)]
   → 138 qualified accounts ready for outreach
   → Expected improvement: +38 accounts recovered from initial exclusions (29%)
```

---

## Pipeline Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│ SOURCING & DISCOVERY PHASE                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Segment Gap Analysis] ──→ [Source Evaluation] ──→ [Hit Rate Plan] │
│       /source-accounts            (user chooses)       (cost/ROI)   │
│                                                                      │
│  OUTPUT: Search queries + batch plans ready to execute              │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ RESEARCH & CLASSIFICATION PHASE                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Company List] ──→ [Website-first research] ──→ [Segment routing]  │
│   /enrich-batch     (6-8 searches per company)      & classification│
│                                                                      │
│  ┌────────────────────────────────────────┐                        │
│  │ RESEARCH PHASES:                       │                        │
│  │ 1. Website read (homepage + services)  │                        │
│  │ 2. Segment-specific searches           │                        │
│  │ 3. Gap fill & exclusion verification   │                        │
│  └────────────────────────────────────────┘                        │
│                                                                      │
│  [Scoring & Synthesis]                                             │
│  ├─ Strategic Fit (0-35)                                           │
│  ├─ Problem Awareness (0-25)                                       │
│  ├─ Timing/Urgency (0-25)                                          │
│  └─ Outreach Quality (0-15)                                        │
│                                                                      │
│  OUTPUT: Qualified Accounts (XLSX, 2 tabs) + Excludes Log          │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ IMPORT PREPARATION PHASE                                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Qualified Accounts] ──→ [HubSpot Property Mapping]               │
│   /process-import           ├─ Segment mapping                      │
│                             ├─ Property name mapping               │
│                             ├─ Value transformations               │
│                             └─ Domain cleaning                     │
│                                                                      │
│  [Edge Case Detection]                                             │
│  ├─ Rule 1: Retail ISP + infra                                    │
│  ├─ Rule 2: Low employee count + infra                            │
│  ├─ Rule 3: Insufficient data but identifiable                    │
│  ├─ Rule 4: Vendor + infra overlap                                │
│  ├─ Rule 5: Enterprise + telecom-adjacent                         │
│  └─ Rule 6: Bot processing failures                               │
│                                                                      │
│  OUTPUT: HubSpot import file + edge cases file + definitive excludes│
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ EDGE CASE RECOVERY PHASE (OPTIONAL)                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Edge Cases File] ──→ [Targeted Deep Research]                   │
│   /research-edge-cases      (2-4 rule-specific searches)           │
│                                                                      │
│  [Reclassification Decisions]                                      │
│  ├─ Check for wholesale divisions (Rule 1)                        │
│  ├─ Verify with multiple sources (Rule 2)                         │
│  ├─ Deep search with state/domain (Rule 3)                        │
│  ├─ Check for operator division (Rule 4)                          │
│  ├─ Check for open-access fiber (Rule 5)                          │
│  ├─ Run full research methodology (Rule 6)                        │
│  └─ Distinguish neoclouds from colos (Rule 7)                     │
│                                                                      │
│  OUTPUT: Reclassified accounts (HubSpot-ready) + confirmed excludes │
│          + full audit trail                                         │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ HUBSPOT IMPORT                                                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [Qualified Accounts XLSX] ──→ [HubSpot] ✓ Import complete         │
│   (zero manual edits needed)                                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Commands

### /source-accounts
Find new prospect companies by ICP segment.

**Usage:**
```
/source-accounts colocation
/source-accounts fiber california
/source-accounts all
/source-accounts neocloud
```

**Outputs:**
- CRM coverage snapshot (if HubSpot available)
- Coverage gaps identified
- Recommended sources ranked by hit rate
- Segment-specific search queries
- Batch plan with cost/time/expected yield

---

### /enrich-batch
Research and classify a batch of companies.

**Usage:**
```
/enrich-batch [CSV or XLSX file with company names]
/enrich-batch company1.com, company2.com, company3.com
```

**Outputs:**
- Enriched Accounts XLSX (2 tabs: HubSpot Import + Companion Data)
- Excludes Log (companies that didn't qualify)
- Summary report (counts by tier, data quality metrics)

---

### /process-import
Transform enrichment output into HubSpot-ready files.

**Usage:**
```
/process-import [enrichment output file]
```

**Outputs:**
- hubspot_import_qualified.xlsx (ready to upload)
- edge_cases_for_research.xlsx (flagged for deeper review)
- definitive_excludes.xlsx (validated exclusions)
- Summary report (transformation counts and warnings)

---

### /research-edge-cases
Deep-dive research on edge cases.

**Usage:**
```
/research-edge-cases [edge cases file from process-import]
```

**Outputs:**
- reclassified_hubspot_import.xlsx (reclassified accounts)
- confirmed_excludes.xlsx (validated exclusions)
- edge_case_research_log.xlsx (full audit trail)
- Summary report (reclassification counts by rule)

---

## Segment Definitions

| Segment | Definition | Sub-Segments |
|---------|-----------|--------------|
| **Data Center Colo Provider** | Owns/operates data center facilities, sells space/power/cross-connects | Standard, AI Infrastructure |
| **Fiber Operator** | Owns fiber network (500+ route miles), sells connectivity | Regional CLEC, Long-Haul/Backbone, Dark Fiber Specialist |
| **Network Operator (Tier 1 / VNO)** | Tier 1/2 carrier, 100K+ route miles, national/global backbone | Track A (external extension), Track B (internal + external unification) |
| **NeoCloud** | IS a GPU cloud provider (CoreWeave, Lambda Labs, Crusoe, etc.) | Large-Scale GPU, Tier 1 Inference, AI Infrastructure Providers, Sovereign AI, Crypto-to-AI Pivots |
| **Enterprise (MSP)** | Aggregates carrier services (no owned infrastructure) | Telecom Aggregator, Managed Network Services |

---

## Key Metrics & Economics

### Sourcing Hit Rates (validated from 2,769+ records)

| Source | Hit Rate | Cost |
|--------|----------|------|
| PTC Conference | 92% | $1-2K |
| FCC BDC | 75-85% | Free |
| PeeringDB | 70-80% | Free |
| State PUC Lists | 70-80% | Free |
| DataCenterMap | 60-70% | Free |
| Cloudscene | 60-70% | Free |
| ZoomInfo/Apollo broad | 27-51% | Paid |

### Enrichment Cost

| Batch Size | Time | Cost | Per Company |
|------------|------|------|------------|
| 50 | ~50 min | ~$18-20 | ~$0.36-0.40 |
| 150 | ~2.5 hrs | ~$53-60 | ~$0.35-0.40 |
| 500 | ~8 hrs | ~$175-200 | ~$0.35-0.40 |

At 70% hit rate: **~$0.51-0.57 per ICP company**
At 35% hit rate: **~$1.00-1.14 per ICP company**

**Key insight:** High-quality sources save $250+ on 500 companies due to better hit rates.

### Edge Case Recovery Rates

| Rule | Recovery Rate | Notes |
|------|---------------|-------|
| Rule 1: Retail ISP + infra | 20-40% | Most common: ISP + wholesale fiber hybrid |
| Rule 2: Low employee count | 30-50% | Data errors, cooperatives undercount staff |
| Rule 3: Insufficient data | 10-30% | Bot missed signals, generic names |
| Rule 4: Vendor + infra | 5-15% | Dual business models |
| Rule 5: Enterprise + telecom | 5-15% | Municipal utilities with fiber |
| Rule 6: Bot failures | 50%+ | Bot didn't run properly |
| Rule 7: Neocloud | 40-60% | Misclassified as colo or excluded |

---

## Integration Notes

### HubSpot Requirements

- Hub ID: 242063281 (MaiaEdge)
- Properties needed:
  - `customer_segment` (dropdown) — maps to 5 main segments
  - `customer_sub_segment` (dropdown) — 15 sub-segment values
  - `infrastructure_profile` (multi-select) — facility/route mile/POP buckets
  - `fabric_provisioning_approach` (multi-select) — NaaS platforms, internal approach
  - `account_tier` (dropdown) — Tier 1/2/3 based on priority score
  - `segmentation_confidence` (dropdown) — High/Medium/Low/Manual Review
  - And 8 more text fields for account brief, triggers, etc. (see hubspot-values.md)

### Apollo/ZoomInfo Integration

- Sourcing skill generates ready-to-use search queries for both platforms
- Can evaluate Apollo/ZoomInfo exports (hit rate calculation, overlap detection)
- Recommends niche sources (PeeringDB, FCC, DataCenterMap) before broad Apollo/ZoomInfo searches

### Email Outreach Integration

- Enrichment skill produces `email_context` JSON in companion data tab
- Provides company snapshots, personalization hooks, segment-specific messaging angles
- Can be passed directly to maiaedge-email-bot skill (separate) for automated outreach

---

## Common Workflows

### Workflow 1: Fast Track (High Confidence)
Use when sourcing from high-hit-rate sources (PTC, FCC, PeeringDB).

```
1. /source-accounts [segment] → Get recommendations
2. /enrich-batch [high-hit-rate source] → Enrich
3. /process-import [enrichment output] → Clean up
4. Import to HubSpot (130 qualified, skip edge case research for speed)
```

**Time:** 24-48 hours for 150 companies
**Quality:** 70-80% hit rate with minimal false negatives

---

### Workflow 2: Quality Focus (Deep Research)
Use when need maximum hit rate recovery (more time, better results).

```
1. /source-accounts [segment] → Get recommendations
2. /enrich-batch [mixed sources] → Enrich
3. /process-import [enrichment output] → Flag edge cases
4. /research-edge-cases [edge cases] → Deep-dive
5. Import to HubSpot (qualified + reclassified)
```

**Time:** 3-5 days for 150 companies (includes edge case research)
**Quality:** 80-90% hit rate with 20-50% more accounts recovered from edge cases

---

### Workflow 3: GAP FILL (Coverage Analysis)
Use when need to identify which segments are underrepresented.

```
1. /source-accounts all → CRM snapshot + segment coverage
2. For each gap segment:
   a. /source-accounts [segment] → Get best sources
   b. [User sources from recommendations]
   c. /enrich-batch [segment companies] → Enrich
   d. /process-import → Prepare for import
3. /research-edge-cases [if needed] → Recover false negatives
4. Import to HubSpot
```

**Time:** 2-4 weeks for complete coverage build-out
**Result:** Balanced portfolio across all segments

---

## Troubleshooting

### "HubSpot dedup check unavailable"
**Cause:** HubSpot MCP tools not connected
**Impact:** Enrichment will process all companies, may create duplicates
**Fix:** Connect HubSpot in Cowork settings before running /enrich-batch

---

### "Company domain not found, flagged for manual review"
**Cause:** Domain discovery search returned ambiguous results
**Impact:** Company skipped to excludes log
**Fix:** Check excludes log, provide domain or company name variation to /enrich-batch in separate batch

---

### "Value mapping warning: [segment] not recognized"
**Cause:** Enrichment output uses non-standard segment name
**Impact:** Segment won't import to HubSpot (missing from dropdown)
**Fix:** Verify segment is one of: Colocation Operator, Fiber Operator, Network Operator, MSP/Aggregator, Neocloud

---

### "Too many edge cases (50+) for manual review"
**Cause:** High initial exclusion rate indicates sourcing quality issue
**Impact:** Large follow-up research effort needed
**Fix:** Research top 20 by rule priority (Rule 6, 7, 1 first). Consider higher-hit-rate sources in next batch.

---

## Support & Documentation

All four skills include inline documentation with:
- Task routing modes (when to use each)
- Knowledge base references (for segment context)
- Input/output schemas (exact file formats)
- Decision rules and classification logic
- Output formatting standards

Refer to skill files in `skills/` directory for complete methodology.

---

## Version History

**v1.0.0** (March 2026)
- Complete pipeline with 4 skills
- Website-first research methodology
- 6-7 rule edge case detection
- Full HubSpot integration
- Comprehensive reference guides
