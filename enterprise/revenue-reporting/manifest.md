# MaiaEdge Revenue Reporting — Enterprise Project Manifest

> Workflow: HubSpot pipeline + call data → pipeline forecast with POC-adjusted probabilities → deal-by-deal narratives → call intelligence → trend reports → audience briefings

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/revenue-reporting/upload/`. That built folder is the authoritative, complete file set; the per-file lists below are a human reference and can lag the build. When in doubt, upload everything in `upload/`.

## Knowledge Files — Skills (upload as .md)
- skills/pipeline-analytics/SKILL.md → upload as `maiaedge-pipeline-analytics.md`
- skills/call-reporting/SKILL.md → upload as `maiaedge-call-reporting.md`
- skills/call-analysis/SKILL.md → upload as `maiaedge-call-analysis.md`
- skills/pipeline-discipline/SKILL.md → upload as `maiaedge-pipeline-discipline.md`

## Knowledge Files — Context (upload as .md)
### Core
- context/core/maiaedge-101.md
- context/core/icp-playbook.md
- context/core/segment-qualification.md

### HubSpot
- context/hubspot/call-schema.md
- context/hubspot/deals-schema.md
- context/hubspot/poc-schema.md
- context/hubspot/property-schema.md
- context/hubspot/hubspot-values.md
- context/hubspot/territory-model.md

### Segments (all 6 as of 2026-05-11)
- context/segments/* (all 6 — colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise** [Multi-DC ICP, anchor: Meijer], plus enterprise-use-cases.md for pipeline-analytics segment slicing — Enterprise added as 6th segment column in segment-coverage matrix)

### Sales
- context/sales/use-case-taxonomy.md
- context/sales/call-intelligence.md

## What This Project Does

**Pipeline reporting:** Ask for a forecast, pipeline report, or deal review and get a single comprehensive HTML report — pipeline health by stage/rep, 5-tier forecast categories with POC-adjusted probabilities, Conservative/Likely/Optimistic scenarios, close-date timeline, deal-by-deal summary with live narratives, rep performance, deal velocity, and stale deal flags. No mode selection needed.

**Call intelligence:** Ask about call trends, use case frequency, segment conversations, rep activity, or specific company discussions. Extracts structured intelligence from HubSpot call summaries.

**Dashboards and briefings:** Monthly call dashboards, multi-month trend analysis, deals vs. POCs call comparison, and audience-specific briefings for CEO, CRO, and reps.

**Unified context:** Pipeline-analytics pulls call summaries for deal narratives. Call-reporting's CRO briefing builds the 3-column pipeline board using pipeline-discipline. These skills work together — ask any reporting question and get a complete answer.

## NOT included (not needed for this workflow)
- ~~context/outreach/*~~ (this project reports, not outreach writing)
- ~~context/copy-strategy/*~~ (scoring/critique not relevant here)
- ~~context/enrichment/*~~ (not enriching companies)
- ~~context/marketing/*~~ (not creating marketing content)
- ~~context/product/*~~ (product details not needed for reporting)

## Note on call-intelligence project
The existing `call-intelligence` enterprise project has the same four skills. This project (`revenue-reporting`) is the intended replacement with a clearer name for leadership use and the updated pipeline-analytics skill (forecast system rewrite, POC signal matrix, unified report output).

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; Enterprise added as 6th segment in pipeline-analytics + pipeline-discipline reports)
