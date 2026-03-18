---
name: edge-case-researcher
description: "MaiaEdge edge case research agent. Deep-dive investigator for excluded accounts from enrichment pipeline. Takes edge case file from import processor and performs targeted research to reclassify as qualified OR confirm exclusion with stronger evidence. Use when given edge case files, asked to re-evaluate excludes, deep dive excluded accounts, check if any excludes should be qualified, or perform second-pass research on questionable companies. Uses web_fetch, multi-source verification, wholesale/B2B detection, and adaptive query refinement. Catches false negatives from single-pass enrichment — especially retail ISP/wholesale hybrids, low employee count errors, and insufficient data edge cases."
---

# MaiaEdge Edge Case Research Agent

## Skill Name: `maiaedge-edge-case-researcher`
## Call Action: Use when asked to "research edge cases", "deep dive excluded accounts", "re-evaluate excludes", "check if any excludes should be qualified", or when given an edge case file from the import processor skill

## Purpose
Take the edge case file produced by the `maiaedge-enrichment-import-processor` skill and perform deep-dive research on each account to determine if they should be:
1. **RECLASSIFIED** as a qualified account → produce a HubSpot-ready import file with all values mapped identically to the import processor skill
2. **CONFIRMED EXCLUDED** with stronger evidence and an audit trail

### Improvements Over n8n Pipeline
The original n8n bot excluded accounts in a single pass with no second chance. This skill exists specifically to catch the false negatives that single-pass architecture creates:
1. **Targeted research per exclusion type**: Different edge case rules get different research strategies — not one-size-fits-all
2. **Website crawling**: Uses `web_fetch` on company domains to read actual services/about pages, which the n8n bot could not do
3. **Multi-source employee verification**: The #1 false exclusion in the n8n bot was bad employee data — this skill cross-references multiple sources
4. **Adaptive query refinement**: If initial searches fail, tries alternate names, trade names, or domain-based searches
5. **Wholesale/B2B detection**: Specifically designed to catch companies that are BOTH retail ISPs AND wholesale fiber operators — the most common misclassification in the n8n output

## Input
An XLSX/CSV file with edge case accounts (typically the `edge_cases_for_research.xlsx` output from the import processor). Must contain at minimum:
- `company_name`
- `company_domain`
- `edge_case_rule` (from import processor)
- `edge_case_reason`
- `recommended_research`
- Original enrichment fields

---

## RESEARCH METHODOLOGY

### General Research Approach (applies to ALL rules)
Before running rule-specific searches:
1. **Always start with `web_fetch` on `company_domain`** — read the homepage and services page. This alone often resolves the edge case. The n8n bot could NOT do this.
2. **Check for parent/subsidiary relationships** — a company with 5 employees might be a subsidiary of a larger operator. Search `[company_name] parent company` or `[company_name] subsidiary of`.
3. **Try alternate names** — if searches on `company_name` return nothing, look at what name the website uses and search with that instead.

### Rule 1 — Retail ISP with Infrastructure Signals
**Primary question**: Does this company sell wholesale/B2B connectivity or just residential broadband?

**Research actions:**
1. `web_fetch` on company domain — look for: "wholesale", "carrier", "enterprise", "dark fiber", "lit services", "transport", "wavelength", "B2B" pages/menu items
2. Search: `[company_name] wholesale fiber services`
3. Search: `[company_name] enterprise business services`
4. Search: `[company_name] carrier services dark fiber`
5. If the website shows separate residential vs. business divisions, `web_fetch` the business/wholesale page
6. Search: `[company_name] NTCA member` or `[company_name] cooperative` — cooperatives almost always have wholesale fiber

**Decision criteria:**
- **RECLASSIFY as Fiber Operator** if: Company has wholesale/carrier/B2B division selling fiber, transport, wavelengths, dark fiber, or lit services to other carriers or enterprises. Even if they also do residential ISP, the B2B infrastructure side makes them a Fiber Operator.
- **CONFIRM EXCLUDE** if: Purely residential broadband with no wholesale, carrier, or enterprise infrastructure sales. No evidence of selling to other operators.

**Common pattern**: Rural telcos and cooperatives are frequently Retail ISP + Fiber Operator hybrids. If the company is NTCA member or a cooperative with 500+ route miles, almost always reclassify as Fiber Operator.

### Rule 2 — Low Employee Count with Infrastructure Metrics
**Primary question**: Is the employee count accurate, and does this company operate real infrastructure?

**Research actions:**
1. `web_fetch` on company domain — check About/Team pages for actual staff
2. Search: `[company_name] employees team staff size`
3. Search: `[company_name] LinkedIn` — look for employee count mentions in search snippets
4. Search: `[company_name] annual report revenue` — revenue indicates real business scale
5. Check if cooperative, municipal entity, or holding company — these systematically show low/zero employee counts in data providers because they report differently
6. Search: `[company_name] cooperative` or `[company_name] municipal broadband`

**Decision criteria:**
- **RECLASSIFY** if: Company clearly operates infrastructure (fiber, data centers, POPs) and the low employee count is a data error, OR the company is a cooperative/municipal/holding entity where employee count data is unreliable by nature.
- **CONFIRM EXCLUDE** if: Company genuinely is very small with no meaningful infrastructure, is defunct, or is inactive.

**Key insight**: Telecom cooperatives almost NEVER show accurate employee counts in data providers. If company name contains "cooperative", "coop", "mutual", "telephone association", or "rural", the employee count is almost certainly wrong — focus on infrastructure evidence instead.

### Rule 3 — Insufficient Data with Identifiable Business
**Primary question**: Can we find the data the original bot missed?

**Research actions:**
1. `web_fetch` on company domain — often the website has everything the bot missed
2. Search: `[company_name] fiber network`
3. Search: `[company_name] data center colocation`
4. Search: `site:[company_domain]` to index the website
5. Search: `[company_name] PeeringDB`
6. Search: `[company_name] NTCA` or `[company_name] telecom`
7. If company name is generic or ambiguous, search: `[company_name] [headquarters_state] telecom`

**Decision criteria:**
- **RECLASSIFY** if: Research reveals the company fits a valid segment (Colo, Fiber, Network Op, MSP, Neocloud) with at least MEDIUM confidence.
- **CONFIRM EXCLUDE** if: Even with deeper research, the company doesn't fit any ICP segment, domain is dead, or company is genuinely unrelated to telecom/infrastructure.

**Key insight**: The n8n bot's most common failure mode was generic company names returning results for the wrong company. Adding the state or domain to the search query usually resolves this.

### Rule 4 — Vendor/Contractor with Infrastructure Overlap
**Primary question**: Does this company operate infrastructure in addition to being a vendor?

**Research actions:**
1. `web_fetch` on company domain — look for services beyond construction/equipment
2. Search: `[company_name] network operations managed services`
3. Search: `[company_name] fiber network owns operates`
4. Search: `[company_name] dark fiber lease`
5. Look for dual business models (e.g., fiber construction company that retains ownership of some routes)

**Decision criteria:**
- **RECLASSIFY as MSP/Aggregator or Fiber Operator** if: Company operates infrastructure in addition to being a vendor. Dual business model makes them a legitimate prospect.
- **CONFIRM EXCLUDE** if: Company is ONLY a vendor/contractor with no infrastructure ownership or operations.

---

## OUTPUT

For each edge case:

1. **Research Summary** — What you found and why
2. **Decision** — RECLASSIFY or CONFIRM EXCLUDE
3. **If RECLASSIFY** — Produce a properly formatted HubSpot import row using exact same mapping as the import processor skill
4. **If CONFIRM EXCLUDE** — Document reason with stronger evidence than the original exclusion

Deliver:
- **Reclassified Accounts** (XLSX) — HubSpot-ready import file for qualified edge cases
- **Confirmed Excludes** (XLSX) — Audit trail for companies that remain excluded
