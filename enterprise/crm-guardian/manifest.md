# MaiaEdge CRM Guardian — Enterprise Project Manifest

> Workflow: Scheduled CRM maintenance → data hygiene → enrichment → territory validation → account sourcing → contact gap fill → job change detection → auto-correct with change log

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

## Knowledge Files — Skills (upload as .md)
- skills/crm-guardian/SKILL.md → upload as `maiaedge-crm-guardian.md`
- skills/crm-hygiene/SKILL.md → upload as `maiaedge-crm-hygiene.md`
- skills/company-enrichment/SKILL.md → upload as `maiaedge-company-enrichment.md`
- skills/segment-classification/SKILL.md → upload as `maiaedge-segment-classification.md`
- skills/territory-manager/SKILL.md → upload as `maiaedge-territory-manager.md`
- skills/account-sourcing/SKILL.md → upload as `maiaedge-account-sourcing.md`
- skills/import-processor/SKILL.md → upload as `maiaedge-enrichment-import-processor.md`
- skills/edge-case-researcher/SKILL.md → upload as `maiaedge-edge-case-researcher.md`
- skills/contact-discovery/SKILL.md → upload as `maiaedge-contact-discovery.md`

## Knowledge Files — Context (upload as .md)
### HubSpot (all)
- context/hubspot/* (property-schema, hubspot-values, territory-model, contact-schema, deals-schema, poc-schema, call-schema)

### Core (all)
- context/core/* (maiaedge-101, icp-playbook, segment-qualification, competitive-positioning, messaging-framework, terminology-glossary)

### Segments (all 6 as of 2026-05-11)
- context/segments/* (colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise** [Multi-DC ICP, anchor: Meijer], plus enterprise-use-cases.md — required for R1/R2 Enterprise scale-gate classification, R7 Enterprise allocation, R8 Enterprise persona patterns, R9 Enterprise exec-change monitoring)

### Signals (all)
- context/signals/* (includes new enterprise-signals.md — added 2026-05-11; consumed by weekly-signal-scan Stage 1.F Enterprise sub-stage)

### Enrichment (all)
- context/enrichment/* (sourcing-reference-guide, research-routes, output-schemas)

### Product
- context/product/proof-points.md
- context/product/ai-market-positioning.md

### Sales
- context/sales/neocloud-strategy-brief.md
- context/sales/use-case-taxonomy.md

## What This Project Does

**Data hygiene (weekly Monday):** Duplicate detection, missing field gap filling, deprecated enum migration, Cooper-owned account routing, contact owner/segment sync, stale lead detection, completeness scoring. Auto-corrects with safety tiers.

**Enrichment (weekly Wednesday):** Enriches new accounts (created last 14 days with missing segment/tier). Re-enriches stale accounts (last_enriched_date 6+ months ago). Full field overwrite with website-first adaptive research.

**Territory validation (daily weekdays):** Validates state-to-owner mapping, auto-corrects misassigned accounts, cascades owner changes to contacts. Skips strategic exceptions.

**Account sourcing (monthly 1st):** CRM gap analysis focused on colo AI + neocloud segments. Produces review list of candidates — does not auto-create.

**Contact persona gaps (weekly Friday):** Audits Tier 1/2 accounts for missing buying committee personas. Apollo search + LinkedIn validation for quality contacts. Auto-creates with verified email. Flags remaining gaps for reps with specific LinkedIn search instructions.

**Job change detection (quarterly):** Checks key contacts via Apollo for employment changes. Marks departures, finds replacements, flags persona gaps.

## NOT included (not needed for CRM maintenance)
- ~~context/outreach/*~~ (Guardian maintains data, does not write emails)
- ~~context/copy-strategy/*~~ (no content scoring/critique)
- ~~context/marketing/*~~ (no marketing content)

## MCP Requirements
- **HubSpot MCP** — read/write companies, contacts, deals, notes
- **Apollo MCP** — search people by company/title/email, filter by verification status

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; CRM Guardian now manages 6 ICP segments + critical pre-deletion-audit defensive check protects pre-promotion Enterprise records like Meijer)
