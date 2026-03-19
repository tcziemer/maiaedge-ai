---
name: company-enrichment
description: "MaiaEdge company enrichment and classification bot. Research companies, classify into customer segments (Colocation, Fiber Operator, Network Operator, MSP/Aggregator, Neocloud), score/tier, and produce HubSpot-ready import files. Use when asked to enrich companies, research accounts, run enrichment pipeline, classify companies for MaiaEdge, create HubSpot import files, or segment analysis. Uses website-first adaptive research strategy (6-8 calls per company vs 25+ legacy). Input: company names or domains. Output: qualified accounts XLSX + excludes log with audit trail. Handles deduplication, domain discovery, deep investigation, edge case flagging, and HubSpot data transformation."
---

# MaiaEdge Account Enrichment Bot

## Skill Name: `maiaedge-enrichment-bot`
## Call Action: Use when asked to "enrich companies", "research accounts", "run enrichment", or "classify companies for MaiaEdge"

## Purpose
Research companies, classify into MaiaEdge customer segments, score/tier, and produce HubSpot-ready import files. Uses a website-first, adaptive search strategy that averages 6-8 total calls per company (vs. 25+ in legacy n8n pipeline) while producing more accurate results.

**This skill produces two output files:**
1. **Qualified Accounts** — Import-ready XLSX using exact HubSpot property internal names and valid dropdown/multi-select values. Can be imported directly into HubSpot with no transformation step.
2. **Excludes Log** — Separate file documenting excluded companies with reasons, for audit trail and occasional review.

**Skill 2 (Import Processor) is NOT needed when this skill runs.** Skill 2 only exists for processing legacy n8n pipeline output. This skill handles the full pipeline end-to-end.

---

## Input

**Only `company_name` is truly required.** Everything else is discovered through research.

A list of companies with:
- `company_name` (REQUIRED — the only mandatory field)
- `company_domain` (optional — if not provided, Step 0 discovers it)

The input may be a CSV, XLSX, or just a list of company names. Do not assume any other fields exist. Treat every data point as something to be researched and verified, even if the input includes partial data like state or segment — verify it independently.

---

## STEP 0: Domain Discovery & Dedup Check

### 0A: HubSpot Deduplication Check (recommended)

Before enriching, check if the company already exists in HubSpot to avoid wasting research effort and overwriting existing data:

1. If HubSpot MCP tools are available, search by `company_domain` (or `company_name` if no domain) using `search_crm_objects`
2. If a match is found with `customer_segment` already populated:
   - **Skip enrichment** for this company — it's already been processed
   - Log it: `"SKIPPED — already in HubSpot as [segment], enriched [date]"`
3. If a match is found but `customer_segment` is empty:
   - **Proceed with enrichment** — the company exists but hasn't been classified yet
4. If no match → proceed with enrichment as normal

Report dedup results before starting research: "Found X of Y companies already in HubSpot — skipping those, enriching Z net-new companies."

If HubSpot tools are unavailable, skip this step and proceed. Note: "HubSpot dedup check unavailable — processing all companies."

### 0B: Domain Discovery (only when domain is missing)

**Skip this step entirely if `company_domain` is provided.**

When a company has no domain:

1. `web_search` for `[company_name] official website`
   - Look for the company's actual website in search results
   - Prefer .com, .net, .io domains over social media profiles or directory listings
   - Watch for disambiguation — "Summit" could be 50 companies. Use any context clues from the input (state, industry, etc.)

2. If the search returns a clear match → set `company_domain` and proceed to Stage 1
3. If ambiguous (multiple companies with same name) → try `[company_name] [any available context like state or industry] telecom fiber data center`
4. If still no match → flag `needs_manual_review = TRUE` with note "Could not determine company domain" and skip to excludes log

**Cost: 1-2 additional searches per domain-less company.**

---

## STAGE 1: Adaptive Deep Investigation

### Design Philosophy
The legacy n8n pipeline fires 25+ blind searches per company because it cannot visit websites or adapt based on findings. This skill uses a 3-phase approach:
1. **Phase 1**: Read the company's actual website — this alone answers ~50% of research questions
2. **Phase 2**: Run ONLY the searches needed based on what Phase 1 revealed (segment-specific)
3. **Phase 3**: Fill gaps, verify exclusions, and resolve edge cases

Every search must earn its place. If the website already answered a question, don't search for it again.

---

### PHASE 1: Website + Identity (2-3 calls)

**Step 1: `web_fetch` on `https://[company_domain]`**
Extract: description/tagline, nav menu items, infrastructure language (fiber/DC/colo/network), customer types (residential/enterprise/wholesale/carrier), portal/platform mentions, AI/GPU language, geographic clues, customer logos.

**Step 2: `web_fetch` on services/solutions page** (if linked from homepage)
Look for: specific products, wholesale vs. retail divisions, dark fiber/lit/wavelength offerings, colo/interconnection services, self-service portal or API, NaaS badges (Megaport, PacketFabric, Equinix, etc.)

**Step 3: `web_search` for `[company_name] company overview`** — ONLY if website was thin/down/uninformative.

**PHASE 1 CHECKPOINT: Route the company.**

| Website signals | Likely classification | → Phase 2 route |
|---|---|---|
| Data center, colocation, cross-connect, rack space, power | **Colocation Operator** | → Colo research |
| Fiber, route miles, network, transport, wavelength, lit buildings | **Fiber Operator** | → Fiber research |
| National backbone, Tier 1/2, global network, massive scale | **Network Operator** | → Network Op research |
| Aggregator, multi-carrier, no owned infrastructure | **MSP/Aggregator** | → MSP research |
| IS a GPU cloud provider (CoreWeave, Lambda, Crusoe, Together.ai, RunPod, Modal, Applied Digital, Hut 8, etc.) | **Neocloud** | → Neocloud research |
| Staffing, software, consulting, manufacturing, construction | **Likely exclude** | → Exclude verification |
| Residential broadband, ISP, "sign up for internet" | **Likely Retail ISP** | → ISP verification (check for wholesale) |
| Website down, parked domain, or completely unrelated | **Insufficient data** | → Broad search fallback |
| Can't determine from website alone | **Ambiguous** | → Broad search fallback |

---

## STAGE 2: Segment-Specific Deep Dive

Each segment has its own research pathway based on Phase 1 routing.

---

## STAGE 3: Edge Case Identification & HubSpot Readiness

At the end of enrichment, flag any companies that don't fit clear QUALIFIED or EXCLUDED buckets. These edge cases get documented for the edge-case-researcher skill to review later.

---

## OUTPUT

Generate two files:

### File 1: Qualified Accounts (HubSpot Import Ready)
XLSX with columns mapped to HubSpot property names. Ready for drag-and-drop import with no transformation. Includes:
- `domain`, `name`, `customer_segment`, `customer_sub_segment`
- `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`
- `account_tier`, `account_brief`, `provisioning_landscape`
- `maiaedge_value_proposition`, `recent_trigger`, `segmentation_confidence`
- `last_enriched_date`

### File 2: Excludes Log
Documents all excluded companies with:
- Company name, domain, reason for exclusion
- Exclusion rule (if it's an edge case, flag here for potential reclassification)
- Audit trail for manual review

---

## Account Tier Assignment

Assign `account_tier` based on these criteria (Tier 1 = highest priority):

**TIER_1_STRATEGIC** — Timing + fit are both strong:
- NeoCloud (any sub-segment)
- Colocation with sub-segment = AI Infrastructure (confirmed GPU tenants or liquid cooling)
- Any ICP segment with a recent trigger event (expansion, funding, leadership change in past 6 months) AND segmentation_confidence = HIGH

**TIER_2_CORE** — Strong fit, no urgency trigger:
- Standard Colo with HIGH confidence and Mid-Size or larger infrastructure
- Fiber Operator with HIGH confidence
- Network Operator (either track) with HIGH confidence

**TIER_3_EMERGING** — Qualified but smaller or less certain:
- Any ICP segment with MEDIUM confidence
- Small-scale accounts (infrastructure_profile = Small in all dimensions)
- MSP/Aggregator (any confidence)

**UNRANKED** — Not enough signal:
- LOW confidence or MANUAL_REVIEW confidence
- Qualified segment but no observable use case signal

---

## Key Enrichment Rules

1. **Website-first, adaptive approach.** Always start with the company website.
2. **Every search earns its place.** Don't search for what the website already answered.
3. **Segment confidence matters.** Flag edge cases, don't force bad classifications.
4. **Preserve the audit trail.** Document what you found and why you classified (or excluded) each company.
5. **HubSpot ready from the start.** Format output so it needs zero transformation.
