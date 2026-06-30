# MaiaEdge Sales Outreach — Enterprise Project Manifest

> Workflow: Raw name → enrichment → CRM → segment classification → contact discovery → email/LinkedIn → account briefs

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/sales-outreach/upload/`. That built folder is the authoritative, complete file set. The per-file lists below are a human reference and can lag the build (the build also ships the full `context/signals/` set — including `outreach-signal-pushback.md` — plus `voice-gold-standard.md`, `persona-targeting-blocklist.md`, and the `account-tiering/` files). When in doubt, upload everything in `upload/`.

## Knowledge Files — Skills (upload as .md)
- skills/cold-email/SKILL.md → upload as `maiaedge-cold-outreach-writer.md`
- skills/linkedin-outreach/SKILL.md → upload as `maiaedge-linkedin-outreach.md`
- skills/warm-follow-up/SKILL.md → upload as `maiaedge-warm-follow-up.md`
- skills/prospect-research/SKILL.md → upload as `maiaedge-prospect-research.md`
- skills/segment-classification/SKILL.md → upload as `maiaedge-segment-classification.md`
- skills/company-enrichment/SKILL.md → upload as `maiaedge-company-enrichment.md`
- skills/import-processor/SKILL.md → upload as `maiaedge-enrichment-import-processor.md`
- skills/contact-discovery/SKILL.md → upload as `maiaedge-contact-discovery.md`
- skills/account-brief/SKILL.md → upload as `maiaedge-account-brief.md`
- skills/sdr-pipeline/SKILL.md → upload as `maiaedge-sdr-pipeline.md`
- skills/copy-strategist/SKILL.md → upload as `copystrategistskill.md`

## Knowledge Files — Context (upload as .md)
### Core
- context/core/maiaedge-101.md
- context/core/messaging-framework.md
- context/core/competitive-positioning.md
- context/core/segment-qualification.md
- context/core/icp-playbook.md
- context/core/terminology-glossary.md

### Segments (6 ICP segments as of 2026-05-11)
- context/segments/colocation.md
- context/segments/fiber-operator.md
- context/segments/neocloud.md
- context/segments/network-operator.md
- context/segments/msp-aggregator.md
- context/segments/enterprise.md (Multi-DC ICP, added 2026-05-11; 4 sub-segments — Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services; anchor: Meijer)
- context/segments/enterprise-use-cases.md (8 priority Enterprise use cases × sub-segment fit × persona × insider phrases × lead-angle templates)

### Outreach
- context/outreach/email-writing-rules.md
- context/outreach/fallback-messaging.md
- context/outreach/sender-profiles.md

### Enrichment
- context/enrichment/research-routes.md
- context/enrichment/output-schemas.md

### HubSpot
- context/hubspot/hubspot-values.md
- context/hubspot/territory-model.md

### Sales
- context/sales/account-brief-template.md
- context/sales/call-intelligence.md
- context/sales/neocloud-strategy-brief.md
- context/sales/email-bot-supplemental.md

### Product
- context/product/proof-points.md

### Copy Strategy
- context/copy-strategy/outbound-playbook.md
- context/copy-strategy/scoring-rubric.md
- context/copy-strategy/segment-language.md
- context/copy-strategy/segment-messaging.md

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete; Enterprise added as 6th ICP segment with Meijer as anchor account)
