# Founder Outreach — Enterprise Project Manifest

> Workflow: Same as Sales Outreach but with founder voice (Timothy Ziemer / Abilash Menon)

## System Prompt
Paste Project Instructions directly in Claude.ai (maintained in-app, not in this repo)

> **Source of truth:** run `bash build.sh`, then upload the full contents of `enterprise/founder-outreach/upload/`. That built folder is the authoritative, complete file set; the per-file lists below are a human reference and can lag the build. When in doubt, upload everything in `upload/`.

## Knowledge Files — Skills (upload as .md)
- skills/cold-email/SKILL.md → upload as `maiaedge-cold-outreach-writer.md`
- skills/linkedin-outreach/SKILL.md → upload as `maiaedge-linkedin-outreach.md`
- skills/warm-follow-up/SKILL.md → upload as `maiaedge-warm-follow-up.md`
- skills/prospect-research/SKILL.md → upload as `maiaedge-prospect-research.md`
- skills/segment-classification/SKILL.md → upload as `maiaedge-segment-classification.md`
- skills/company-enrichment/SKILL.md → upload as `maiaedge-company-enrichment.md`
- skills/contact-discovery/SKILL.md → upload as `maiaedge-contact-discovery.md`
- skills/account-brief/SKILL.md → upload as `maiaedge-account-brief.md`
- skills/copy-strategist/SKILL.md → upload as `copystrategistskill.md`

## Knowledge Files — Context (upload as .md)
Same as Sales Outreach MINUS:
- ~~skills/sdr-pipeline~~ (founders do individual outreach)
- ~~skills/import-processor~~ (founders don't do enrichment imports)
- ~~context/enrichment/output-schemas.md~~ (not needed)

### Core
- context/core/* (all 6)

### Segments (all 6 as of 2026-05-11)
- context/segments/* (all 6 — colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise** [Multi-DC ICP added 2026-05-11; 4 sub-segments — Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services; anchor: Meijer], plus enterprise-use-cases.md for 8 priority use cases)

### Outreach
- context/outreach/* (all 3)

### Enrichment
- context/enrichment/research-routes.md

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
- context/copy-strategy/* (all 4)

## Last Synced: 2026-05-11 (Enterprise ICP promotion — Phase 6 rollout complete)
