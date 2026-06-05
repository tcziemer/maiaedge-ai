# MaiaEdge Branded Content — Enterprise Project Manifest

> Workflow: Branded deliverable studio. Produces partner-grade PDFs (one-pagers, cheat sheets, playbooks, battle cards, technical briefs) using the MaiaEdge design system AND in-depth, segment-specific business cases that quantify the buyer's situation, pain, ROI, and decision path. Also advises on PowerPoint/Keynote slide design so non-PDF deliverables stay visually consistent.

## System Prompt
See [enterprise-prompts/branded-content.md](../../enterprise-prompts/branded-content.md). Paste into the Claude.ai Project Instructions field.

## Knowledge Files — Skills (resolve at Claude.ai instance level by name)
- skills/branded-doc/SKILL.md → `maiaedge-branded-doc.md` (primary — branded PDF generator with Tomorrow font, gold/orange/black palette, eyebrow-numbered sections, doc-style covers, table styling, ASCII-to-SVG diagram swaps)
- skills/account-brief/SKILL.md → `maiaedge-account-brief.md` (10-section strategy briefs feeding account-specific business cases)
- skills/sales-enablement/SKILL.md → `maiaedge-sales-enablement.md` (battle cards, one-pagers, discovery guides, talk tracks)
- skills/competitive-intel/SKILL.md → `maiaedge-competitive-intel.md` (competitive positioning sections in any deliverable)
- skills/call-prep/SKILL.md → `maiaedge-call-prep.md` (per-account framing for prospect-specific business cases)

## Knowledge Files — Context (upload as .md)

This project ships the **full repo context** (all `context/*.md` plus `partner-assets/`). The branded-doc skill and segment-specific business case work both require deep familiarity with messaging, segments, signals, product, sales economics, and copy strategy — everything the toolkit has.

### Core
- context/core/* (all 7 — maiaedge-101, messaging-framework, competitive-positioning, segment-qualification, icp-playbook, terminology-glossary, revops-copilot)

### Account Tiering
- context/account-tiering/* (tier-compute-spec, sub-segment-qualification, enrichment-protocols — used when tailoring business cases by tier)

### Segments (all 6 ICPs as of 2026-05-11)
- context/segments/* (colocation, fiber-operator, neocloud, network-operator, msp-aggregator, **enterprise**, plus enterprise-use-cases — drives the 6 segment business case framings)

### Signals (all per-segment catalogs)
- context/signals/* (signal-framework, universal-platform-signals, 6 per-segment signal catalogs — used to anchor business cases in current cataloged trigger events)

### HubSpot
- context/hubspot/* (property-schema, hubspot-values, territory-model, contact-schema, deals-schema, poc-schema, call-schema — for account-specific business cases pulling real CRM data)

### Enrichment
- context/enrichment/* (research-routes, output-schemas, sourcing-reference-guide — used when business cases require deeper account research)

### Product (all)
- context/product/* (proof-points, ai-market-positioning, integrated-switch-datasheet, pbc-pce-datasheet, cloud-onramp-business-case — required for ROI sections, technical sections, and the existing cloud-onramp economic model)

### Sales
- context/sales/* (account-brief-template, call-intelligence, use-case-taxonomy, pricing-reference, marketplace-seeding-strategy, neocloud-strategy-brief, edge-ai-thesis-montauk, golden-pitch-key-slides, end-of-network-silos-blog, email-bot-supplemental — the strategic + economic spine of every business case)

### Marketing
- context/marketing/* (ai-copywriting-guidelines, linkedin-framework, sovereign-routing-explainer, plus media-consumption/)

### Copy Strategy
- context/copy-strategy/* (outbound-playbook, scoring-rubric, segment-language, segment-messaging, ab-test-plan — for tone, vocabulary lock, and segment-specific phrasing across deliverables)

### Partner Assets (source markdowns for the existing branded PDF set)
- context/partner-assets/* (maiaedge-101 partner edition, 6 segment cheatsheets, product-quick-reference — the reference examples the branded-doc skill is calibrated against)

## What This Project Does

**Branded PDF generation:** One-pagers, segment cheat sheets, playbooks, battle cards, technical briefs, partner-facing handouts — anything that should look visually consistent with MaiaEdge 101 and the existing partner cheatsheet set. Tomorrow font embedded, gold/orange/black palette, eyebrow-numbered sections, branded tables, component cards, anti-position cards, status-quo hero blocks, ASCII-to-SVG diagram swaps. Output is partner-grade PDF via WeasyPrint.

**In-depth segment business cases:** Rigorous, segment-specific economic narratives for each of the 6 ICPs (Colocation, Fiber Operator, Neocloud, Network Operator, MSP/Aggregator, Enterprise). Built around a 10-section framework: situation, quantified pain, status-quo cost, MaiaEdge approach, use cases, ROI model, risk + mitigation, implementation path, decision criteria, next steps. Pulls from segment cheatsheets, signal catalogs, pricing reference, use-case taxonomy, cloud-onramp business case, edge-AI thesis, and competitive positioning.

**Account-specific business cases:** Combines `account-brief` output with the segment business case framework to produce a tailored deliverable for a named prospect. Pulls account metadata via HubSpot, current signals from the segment catalog, and the segment pillar framework.

**Slide-deck guidance:** The branded-doc skill renders PDFs, not PowerPoint files. For decks, the project produces a slide-by-slide outline that follows the brand visual system (palette, font, eyebrow numbering, no em dashes, peer-tone copy), plus the markdown source the user can paste into a PowerPoint/Keynote/Google Slides template that matches the existing deck system.

**Customized one-pagers:** Pulls the relevant segment cheatsheet structure, swaps in account- or campaign-specific framing, renders to branded PDF.

## How This Differs from `sales-docs`

- **sales-docs** = legal docs (Order Forms, MSAs, POC Agreements, NDAs) + general sales collateral + call prep + competitive intel. Output is .xlsx / .docx / open-form markdown.
- **branded-content** = visually-branded deliverables (PDFs with the Tomorrow brand system) + analytical business case generation. Output is partner-grade PDF + segment business case markdown.

Use **branded-content** when the deliverable needs to look like MaiaEdge 101 / the partner cheatsheets, or when the request is "build me a business case for [segment / account]". Use **sales-docs** when the deliverable is a legal contract or open-format collateral.

## NOT included (intentional scope cut)
- Outreach skills (cold-email / linkedin-outreach / sdr-pipeline) — those live in Sales Outreach / Founder Outreach
- CRM hygiene / enrichment routines — those live in CRM Guardian / Account Intelligence
- Reporting (pipeline / call analytics) — those live in Revenue Reporting / Call Intelligence

## MCP Requirements
- **HubSpot MCP** — pull account / contact / deal metadata when building account-specific business cases
- **Web search** — recent signals, financials, market context for business case ROI sections

## Project-Level Uploads (not in repo)
- Existing branded PDF reference set (MaiaEdge-101.pdf, Cheat-Sheet-*.pdf, Product-Quick-Reference.pdf) — upload as visual references so Claude can verify new deliverables match the existing design language
- Customer logos / partner co-brand assets when building co-branded deliverables
- PowerPoint / Keynote template files when producing slide-deck outlines

## Last Synced: 2026-05-18 (initial build)
