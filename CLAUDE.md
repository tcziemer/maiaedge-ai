# MaiaEdge AI Toolkit

Sales AI toolkit for MaiaEdge — carrier infrastructure for federated private networking.

## Repo Structure

- `context/` — Reference documents (knowledge base). Single source of truth for all shared context.
- `skills/` — Skill logic (SKILL.md files). Each skill = one folder with one SKILL.md.
- `plugins/` — Plugin packaging for Cowork (manifests + commands + static assets).
- `enterprise/` — Cloud project manifests for Claude.ai enterprise Projects.
- `builds/` — Generated output from build.sh (gitignored).
- `build.sh` — Assembles plugins and standalone skill zips from source.

## How to Use a Skill

1. Read the SKILL.md: `skills/<skill-name>/SKILL.md`
2. The skill will reference context files — read those from `context/` as needed
3. Follow the skill's instructions

## Available Skills

### Enrichment Pipeline
| Skill | Path | Function |
|-------|------|----------|
| account-sourcing | skills/account-sourcing/ | Find prospect companies, evaluate sources, generate search queries |
| company-enrichment | skills/company-enrichment/ | Research, classify, score companies; produce HubSpot import |
| import-processor | skills/import-processor/ | Transform enrichment output to HubSpot format, flag edge cases |
| edge-case-researcher | skills/edge-case-researcher/ | Deep-dive on excluded accounts to recover false negatives |

### Outreach
| Skill | Path | Function |
|-------|------|----------|
| cold-email | skills/cold-email/ | Angle-first cold emails (Tim Lieto / Ken Cunningham) |
| linkedin-outreach | skills/linkedin-outreach/ | 300-char LinkedIn connection requests |
| prospect-research | skills/prospect-research/ | Pre-outreach company + contact research |
| segment-classification | skills/segment-classification/ | Classify companies into ICP segments |
| sdr-pipeline | skills/sdr-pipeline/ | End-to-end batch: company list → 3-email sequences + Smartlead XLSX |
| account-brief | skills/account-brief/ | 10-section strategy briefs for high-value prospects |
| copy-strategist | skills/copy-strategist/ | Critique, score, rewrite cold emails/sequences |

### RevOps
| Skill | Path | Function |
|-------|------|----------|
| contact-discovery | skills/contact-discovery/ | Find people + persona gap analysis |
| crm-hygiene | skills/crm-hygiene/ | CRM health checks + data quality |
| pipeline-analytics | skills/pipeline-analytics/ | Pipeline snapshots + velocity + forecasts |
| territory-manager | skills/territory-manager/ | Territory assignment validation |

### Sales Support
| Skill | Path | Function |
|-------|------|----------|
| sales-docs | skills/sales-docs/ | Order Forms, MSAs, POC Agreements, NDAs |
| sales-enablement | skills/sales-enablement/ | Battle cards, discovery guides, collateral |
| call-prep | skills/call-prep/ | Pre-call briefing + talking points |
| competitive-intel | skills/competitive-intel/ | Competitive briefs + positioning |

### Events & Networking
| Skill | Path | Function |
|-------|------|----------|
| event-intelligence | skills/event-intelligence/ | Conference prep, attendee processing, follow-up |
| icp-networking | skills/icp-networking/ | LinkedIn networking automation |

## Key Rules (apply to ALL skills)

- **Speed language:** Always pair speed with ownership ("your team provisions in minutes") EXCEPT for Neoclouds (they ARE the customer — drop sovereignty)
- **Territory:** East = Tim Lieto, West = Ken Cunningham, International = Tim Ziemer
- **Account tiers are INVERTED:** Tier 1 = highest priority, Tier 5 = lowest
- **AI Colo segment:** Use "Data Center Colo Provider" + sub-segment "AI Infrastructure" (deprecated: "AI - Colocation Operator")
- **MSP/Aggregator:** HubSpot internal value is `Enterprise` (legacy naming)
- **No em dashes** in any customer-facing content
- **Credibility anchors:** Do NOT use in cold emails or LinkedIn. Reserve for discovery calls and follow-ups.
- **Category descriptor:** "Carrier infrastructure" is the ONLY acceptable term (never IaaS, NaaS, platform)

## Context Categories

| Category | Path | What's Inside |
|----------|------|---------------|
| Core | context/core/ | Company identity, messaging, competitive, qualification, ICP, glossary |
| Segments | context/segments/ | Cheatsheets for: colocation, fiber, neocloud, network-op, MSP |
| HubSpot | context/hubspot/ | Property schema, territory model, field values, deal schema |
| Outreach | context/outreach/ | Email rules, fallback messaging, sender profiles |
| Enrichment | context/enrichment/ | Research routes, output schemas, sourcing guide |
| Product | context/product/ | Datasheets, proof points, AI positioning, cloud on-ramp |
| Sales | context/sales/ | Account brief template, call intel, pricing, neocloud strategy, marketplace seeding |
| Marketing | context/marketing/ | Copywriting guidelines, LinkedIn framework, media consumption |
| Copy Strategy | context/copy-strategy/ | Outbound playbook, scoring rubric, segment language/messaging |

## Building Plugins

Run `./build.sh` to assemble all plugins and standalone skill zips into `builds/`.

## Team

| Person | Role | Territory | HubSpot Owner ID |
|--------|------|-----------|-----------------|
| Tim Lieto | AVP, North America Sales | East (30 states) | 161889085 |
| Ken Cunningham | Sales, East Region | West (20 states + DC) | 162339176 |
| Timothy Ziemer | CRO & Co-Founder | International | 159350430 |
| Cooper Kennedy | RevOps | — | 160267902 |
| Abilash Menon | CEO & Co-Founder | Strategic | 159974715 |
| Kyle Blackwell | Sales Engineering | — | 159701452 |
| Woody Acosta | Sales Support | — | 162281129 |
