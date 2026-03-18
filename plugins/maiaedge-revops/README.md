# MaiaEdge RevOps Toolkit

A comprehensive Cowork plugin for MaiaEdge that bundles four critical RevOps skills into a coordinated toolkit for HubSpot auditing, pipeline analytics, territory management, and contact discovery.

---

## Overview

The MaiaEdge RevOps Toolkit provides revenue operations teams with integrated commands to:
- **Audit CRM data quality** — Identify and fix duplicates, missing fields, stale records, and enrichment gaps
- **Analyze pipeline health** — Track deal velocity, forecast revenue, identify stuck deals, and compare rep performance
- **Validate territory assignments** — Ensure accounts are assigned to the correct owner based on HQ state
- **Find and map contacts** — Discover the right personas at target accounts and identify coverage gaps

All four skills work together around a shared data model and HubSpot integration, making it easy to surface cross-functional insights (e.g., "this deal is stuck because we only have one contact and they're not the decision maker").

---

## Components

### Skills
Each skill is a specialized module that solves a specific RevOps challenge:

1. **CRM Hygiene** (`skills/crm-hygiene/SKILL.md`)
   - Comprehensive data quality checks
   - Duplicate detection (domain-based and name-similarity)
   - Missing critical fields analysis
   - Stale record identification
   - Enrichment completeness assessment
   - Data completeness scorecard

2. **Pipeline Analytics** (`skills/pipeline-analytics/SKILL.md`)
   - Pipeline snapshots by stage and segment
   - Deal velocity analysis and bottleneck identification
   - Revenue forecasting (best case, weighted, commit scenarios)
   - Stuck deal alerts with recommended actions
   - Win/loss analysis by segment and owner
   - Rep performance comparison

3. **Territory Manager** (`skills/territory-manager/SKILL.md`)
   - Full territory audit across all accounts
   - Single company territory validation
   - Batch validation for imports
   - Territory distribution reports
   - Correction file generation (HubSpot-ready)
   - Missing state research

4. **Contact Discovery** (`skills/contact-discovery/SKILL.md`)
   - HubSpot contact mapping with persona assessment
   - Apollo prospecting for persona gaps
   - Bulk contact coverage analysis
   - Pipeline-wide persona gap identification
   - Title-to-persona matching

### Commands
Quick-start commands that invoke the skills with preset modes:

- **hygiene-check** — Run CRM health checks with modes for duplicates, missing fields, stale accounts, enrichment, or full audit
- **pipeline-snapshot** — Analyze pipeline with modes for snapshot, velocity, forecast, stuck deals, win/loss, or rep performance
- **territory-audit** — Validate territories with modes for full audit, single company check, distribution report, or corrections
- **find-contacts** — Discover contacts with modes for mapping, coverage analysis, prospecting, or segment-wide gap analysis

### References
Background documents that provide context and master data:

- **territory-model.md** — Master territory assignment model with state-to-owner mapping, key markets, and routing rules

---

## Usage Examples

### Example 1: Quick CRM Health Check

```
hygiene-check full
```
Runs all six hygiene checks and produces a consolidated health report with an overall 0-100 score. Best for quarterly reviews or before major initiatives.

```
hygiene-check duplicates
```
Finds domain-based duplicates and name-similarity matches, recommending which records to merge.

---

### Example 2: Pipeline Analysis for Forecasting

```
pipeline-snapshot forecast
```
Generates three forecast scenarios (best case, weighted, commit) with expected close dates for current quarter.

```
pipeline-snapshot stuck
```
Alerts on deals that are past close date, stalled in stage, or silent for 14+ days. Ranks by urgency (value × time overdue).

```
pipeline-snapshot rep-performance
```
Side-by-side rep metrics including pipeline value, open deals, win rate, avg deal size, and recent activity.

---

### Example 3: Territory Validation After Enrichment

```
territory-audit full
```
Audits all companies, identifies misassignments, missing states, and unassigned accounts. Produces detailed report.

```
territory-audit check Brightspeed
```
Quick check: "Who owns this account? Are they assigned correctly?"

```
territory-audit corrections
```
Generates HubSpot-ready XLSX file with all corrections, ready for bulk update.

---

### Example 4: Contact Coverage Before Outreach

```
find-contacts "Equinix"
```
Maps existing HubSpot contacts at Equinix, identifies which persona slots are filled, and recommends Apollo searches for gaps.

```
find-contacts prospect Equinix
```
Searches Apollo for new contacts matching missing personas, with email status and seniority filtering.

```
find-contacts "gaps Colocation"
```
Analyzes all Colocation segment accounts, identifies which are single-threaded or missing key personas, flags deals at risk.

---

## How the Skills Work Together

The four skills are designed to cross-reference and reinforce each other:

### Data Quality → Territory → Contacts Workflow

1. Run **hygiene-check missing-fields** to identify accounts without state or owner
2. Run **territory-audit full** to assign owners based on HQ state
3. Run **find-contacts coverage** to check contact depth at newly assigned accounts
4. Add contacts and run **find-contacts prospect** to fill persona gaps

### Pipeline Health → Contact Strategy Workflow

1. Run **pipeline-snapshot stuck** to identify deals in trouble
2. For each stuck deal, run **find-contacts "[company]"** to check contact coverage
3. If single-threaded or missing Economic Buyer, run **find-contacts prospect [company]**
4. Add new contacts and use other skills (not in this toolkit) for outreach

### Territory Rebalancing Workflow

1. Run **territory-audit distribution** to assess current balance
2. Review **territory-model.md** for state assignments and key markets
3. Run **hygiene-check scorecard** to understand data quality by territory
4. Run **pipeline-snapshot rep-performance** to compare pipeline health by owner

---

## Key Features

### Comprehensive Data Coverage
- Audits companies, contacts, and deals in a single toolkit
- Persona-based contact mapping specific to MaiaEdge's infrastructure segment
- Territory model integrated directly into all assignment logic

### Actionable Output
- Health scores with numeric 0-100 ratings
- Ranked recommendations ("do this first")
- XLSX export for bulk updates and external sharing
- HubSpot record links for quick navigation

### Cross-Functional Intelligence
- Connects CRM quality to pipeline health (e.g., stale accounts by rep)
- Validates territory alignment to deal ownership
- Flags contact risks in active deals
- Surfaces data gaps that block sales velocity

### Segment-Aware
- All skills understand MaiaEdge's market segments: Colocation, Fiber, Network Operators, Neoclouds, MSP/Aggregators
- Persona definitions customized per segment
- Scoring and prioritization account for segment value

---

## Integration with MaiaEdge Systems

### HubSpot (Primary Data Source)
- All skills query the MaiaEdge HubSpot workspace (Hub ID: 242063281)
- Company properties: name, domain, state, segment, owner, phone, employees, revenue
- Contact properties: name, email, title, owner, activity dates
- Deal properties: name, stage, amount, owner, segment, close date

### Apollo (Contact Prospecting)
- Contact Discovery uses Apollo People Search to find new prospects
- Apollo People Enrichment available for email/phone lookup (requires credit confirmation)
- Apollo Contacts API for adding prospects to your database

### Territory Model
- All territory assignments reference the master model in `references/territory-model.md`
- State-to-owner mapping is authoritative source of truth
- Used in Territory Manager for validation and Contacts Discovery for routing

---

## Getting Started

1. **Load the plugin** in Claude Code or your preferred Claude interface
2. **Read the command hints** — Each command file has an argument-hint for quick reference
3. **Start with hygiene-check** — First step is usually data quality assessment
4. **Follow the recommendations** — Each report suggests next steps and prioritizes issues
5. **Use territory-audit** — Ensure account ownership is correct before any outreach
6. **Validate contacts** — Use find-contacts to map existing coverage and identify gaps

---

## Command Reference

### hygiene-check [MODE]
Audit CRM data quality.

| Mode | Trigger | Output |
|------|---------|--------|
| `full` | No arguments | All checks, health score, top priority fixes |
| `duplicates` | "Find duplicates" | Domain matches, name similarity, merge recommendations |
| `missing-fields` | "What fields are missing?" | Breakdown by field and segment |
| `stale` | "Find stale accounts" | By category (never contacted, ghost, gone cold, aging pipeline) |
| `enrichment` | "Which records need re-enrichment?" | Completeness score distribution, below-threshold list |
| `scorecard` | "Data completeness" | Metrics by company, contact, deal |

---

### pipeline-snapshot [MODE]
Analyze deal pipeline.

| Mode | Trigger | Output |
|------|---------|--------|
| `snapshot` | No arguments or "how's our pipeline?" | Pipeline by stage, owner, segment |
| `velocity` | "Deal velocity" | Days in stage, bottlenecks, by segment |
| `forecast` | "What's going to close?" | Best case, weighted, commit scenarios |
| `stuck` | "Which deals are stuck?" | Past due, stalled, silent, with actions |
| `win-loss` | "Win rate" | Overall metrics, by owner/segment, reasons |
| `rep-performance` | "How are reps doing?" | Side-by-side metrics and activity |

---

### territory-audit [MODE]
Validate territory assignments.

| Mode | Trigger | Output |
|------|---------|--------|
| `full` | No arguments or "audit territories" | All audits, misassignments, missing states |
| `check [company]` | "Who owns [company]?" | Single company status and correction |
| `distribution` | "Territory report" | Account count by owner and segment |
| `corrections` | "Generate correction file" | XLSX ready for HubSpot bulk update |

---

### find-contacts [ARGUMENT]
Find and map contacts at accounts.

| Argument | Trigger | Output |
|----------|---------|--------|
| `[company name]` | "Who do we have at [company]?" | HubSpot contacts mapped to personas, gaps |
| `coverage [company]` | "Check coverage at [company]" | Depth analysis, single-thread risk flag |
| `prospect [company]` | "Find contacts to add at [company]" | Apollo prospects for persona gaps |
| `gaps [segment]` | "Persona gaps in [segment]" | Accounts by coverage level, risky deals |

---

## Support & Questions

- **Territory assignments** → Refer to `references/territory-model.md`
- **HubSpot field definitions** → Consult MaiaEdge_HubSpot_Field_Value_Map.md (external reference)
- **Segment definitions** → See icp-sales-playbook.md (external reference)
- **Persona roles** → Built into each skill; see SKILL.md for segment-specific personas

---

## Version History

**v1.0.0** (March 2026)
- Initial release
- Four integrated skills: CRM Hygiene, Pipeline Analytics, Territory Manager, Contact Discovery
- Four quick-start commands
- Territory model reference
