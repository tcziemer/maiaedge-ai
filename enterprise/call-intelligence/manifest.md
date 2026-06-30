# MaiaEdge Call Intelligence — Enterprise Project Manifest

> Workflow: Deep analysis of HubSpot call summaries → use-case extraction → segment classification → PMF signals → messaging alignment audits → contact-level intel

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/call-intelligence/upload/`. That built folder is the authoritative, complete file set; the per-file lists below are a human reference and can lag the build. When in doubt, upload everything in `upload/`.

## Knowledge Files — Skills (upload as .md)
- skills/call-analysis/SKILL.md → upload as `maiaedge-call-analysis.md`
- skills/pipeline-discipline/SKILL.md → upload as `maiaedge-pipeline-discipline.md`
- skills/call-reporting/SKILL.md → upload as `maiaedge-call-reporting.md`
- skills/pipeline-analytics/SKILL.md → upload as `maiaedge-pipeline-analytics.md`

## Knowledge Files — Context (upload as .md)
### Core (all)
- context/core/* (maiaedge-101, icp-playbook, segment-qualification, competitive-positioning, messaging-framework, terminology-glossary, revops-copilot)

### Segments (all 6 as of 2026-05-11)
- context/segments/* (colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise** [Multi-DC ICP, anchor: Meijer], plus enterprise-use-cases.md for call-analysis Enterprise use-case extraction — Enterprise-specific use cases #22-29 added to use-case-taxonomy.md)

### HubSpot (all — calls associate with every object)
- context/hubspot/* (property-schema, territory-model, hubspot-values, contact-schema, deals-schema, poc-schema, call-schema)

### Sales
- context/sales/use-case-taxonomy.md
- context/sales/call-intelligence.md
- context/sales/pricing-reference.md
- context/sales/neocloud-strategy-brief.md
- context/sales/edge-ai-thesis-montauk.md

### Product
- context/product/proof-points.md
- context/product/ai-market-positioning.md

### Copy Strategy (for messaging alignment modes)
- context/copy-strategy/segment-language.md
- context/copy-strategy/segment-messaging.md

### Assets
- context/sales/call-report-styles.css (report styling)

## What This Project Does

**Contact-level call analysis:** Extracts structured intel from HubSpot call summaries — use cases mentioned, segments discussed, objections, competitive mentions, pain validation, buying signals.

**PMF and messaging alignment:** Compares what prospects say on calls vs. our current messaging. Flags drift, surfaces validated patterns, identifies language we should adopt or retire.

**Pipeline discipline:** 3-column pipeline board (accounts → POC, POC → PO, PO → expansion) built from call evidence, not stage hygiene.

**Dashboards and briefings:** Monthly call dashboards, multi-month trend analysis, audience-specific briefings for CEO, CRO, and reps.

## Relationship to Revenue Reporting

This project and **Revenue Reporting** share all four skills. The split:
- **Call Intelligence** = transcript-heavy work: contact-level analysis, use-case extraction, PMF signals, messaging audits. The "listening" project.
- **Revenue Reporting** = forecast-heavy work: pipeline snapshots, POC-adjusted forecasts, deal narratives, leadership reporting. The "numbers" project.

Both are live. Use Call Intelligence when the question is about what prospects are saying. Use Revenue Reporting when the question is about pipeline health or forecast.

## NOT included (not needed for this workflow)
- ~~context/outreach/*~~ (this project analyzes calls, does not write outreach)
- ~~context/enrichment/*~~ (not enriching companies)
- ~~context/marketing/*~~ (not creating marketing content)
- ~~copy-strategy/outbound-playbook, scoring-rubric~~ (cold email critique lives in Sales Outreach)

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; Enterprise added as 6th ICP for call-analysis use-case extraction)
