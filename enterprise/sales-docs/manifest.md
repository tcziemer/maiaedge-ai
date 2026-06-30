# MaiaEdge Sales Docs — Enterprise Project Manifest

> Workflow: Legal doc generation (Order Forms, MSAs, POC Agreements, NDAs) + sales collateral (battle cards, one-pagers, discovery guides) + call prep + competitive briefs

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/sales-docs/upload/`. That built folder is the authoritative, complete file set (it also ships the `partner-assets/` cheatsheet sources); the per-file lists below are a human reference and can lag the build. When in doubt, upload everything in `upload/`.

## Knowledge Files — Skills (upload as .md)
- skills/sales-docs/SKILL.md → upload as `maiaedge-sales-docs.md`
- skills/sales-enablement/SKILL.md → upload as `maiaedge-sales-enablement.md`
- skills/call-prep/SKILL.md → upload as `maiaedge-call-prep.md`
- skills/competitive-intel/SKILL.md → upload as `maiaedge-competitive-intel.md`

## Knowledge Files — Context (upload as .md)
### Core (all)
- context/core/* (maiaedge-101, icp-playbook, segment-qualification, competitive-positioning, messaging-framework, terminology-glossary, revops-copilot)

### Segments (all 6 as of 2026-05-11)
- context/segments/* (colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise** [Multi-DC ICP, anchor: Meijer], plus enterprise-use-cases.md — required for sales-enablement battle cards + call-prep + competitive-intel briefs covering Enterprise sub-segments)

### Product (all)
- context/product/* (proof-points, ai-market-positioning, integrated-switch-datasheet, pbc-pce-datasheet, cloud-onramp-business-case)

### HubSpot (partial — for legal doc field lookup and account data)
- context/hubspot/hubspot-values.md
- context/hubspot/deals-schema.md
- context/hubspot/poc-schema.md
- context/hubspot/property-schema.md

### Sales
- context/sales/account-brief-template.md
- context/sales/call-intelligence.md
- context/sales/use-case-taxonomy.md
- context/sales/pricing-reference.md
- context/sales/marketplace-seeding-strategy.md
- context/sales/neocloud-strategy-brief.md
- context/sales/edge-ai-thesis-montauk.md
- context/sales/golden-pitch-key-slides.md
- context/sales/end-of-network-silos-blog.md

### Marketing
- context/marketing/ai-copywriting-guidelines.md
- context/marketing/linkedin-framework.md
- context/marketing/sovereign-routing-explainer.md

## What This Project Does

**Legal doc generation:** Order Forms, MSAs, POC Agreements, NDAs — populate variable fields against exact templates without modifying boilerplate. Handles SKU pricing, discount math, term lengths (12/36/60 mo or 60-day POC). Templates, logos, and price lists live directly in the Project (not this repo).

**Sales collateral:** Battle cards, discovery guides, one-pagers, objection responses, talking points, proof-point artifacts. Segment-aware (colo/fiber/neocloud/network-op/MSP), persona-aware, aligned to core messaging.

**Call & meeting prep:** Pre-call briefings, discovery question sets, persona talk tracks, objection handling, proof points tied to a specific prospect.

**Competitive intel:** Positioning vs. Megaport, Equinix, Lumen, SD-WAN, orchestration platforms. Battle cards, objection responses, differentiation narratives.

## NOT included (not needed for this workflow)
- ~~context/outreach/*~~ (this project builds collateral and legal docs, not cold emails)
- ~~context/copy-strategy/*~~ (cold email scoring/critique — handled in Sales Outreach / Founder Outreach)
- ~~context/enrichment/*~~ (no company enrichment in this project)
- ~~skills/call-analysis, call-reporting, pipeline-*~~ (reporting lives in Revenue Reporting / Call Intelligence)

## Project-Level Uploads (not in repo)
- Template files (`order_form_template_1.xlsx`, `msa_template.docx`, `poc_agreement_template.docx`, `nda_template.docx`)
- Logos, fonts, brand assets
- `price_list.md` (if pricing diverges from `context/sales/pricing-reference.md`, update both)
- Per-doc spec files (`order_form_specs.md`, `msa_specs.md`, `poc_specs.md`, `nda_specs.md`)

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; sales collateral now covers Enterprise sub-segments with sub-segment-specific battle cards / discovery guides per `context/segments/enterprise-use-cases.md`)
