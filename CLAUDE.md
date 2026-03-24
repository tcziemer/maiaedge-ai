# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

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
| bizcase | skills/bizcase/ | Cloud on-ramp business case Excel models (NeoCloud, Fiber Operator, Wholesale Carrier) |

### Call Intelligence
| Skill | Path | Function |
|-------|------|----------|
| call-analysis | skills/call-analysis/ | Extract use cases, segments, signals from HubSpot call summaries |
| pipeline-discipline | skills/pipeline-discipline/ | 3-column pipeline board: accounts->POC, POC->PO, PO->expansion |
| call-reporting | skills/call-reporting/ | Call dashboards, trend analysis, audience-specific briefings |

### Events & Networking
| Skill | Path | Function |
|-------|------|----------|
| event-intelligence | skills/event-intelligence/ | Conference prep, attendee processing, follow-up |
| icp-networking | skills/icp-networking/ | LinkedIn networking automation |

## Key Rules (apply to ALL skills)

- **Speed language:** Always pair speed with ownership ("your team provisions in minutes") EXCEPT for Neoclouds (they ARE the customer — drop sovereignty)
- **Territory:** East = Tim Lieto, West = Ken Cunningham, International = Tim Ziemer
- **Account tiers are INVERTED:** Tier 1 = highest priority, Tier 5 = lowest
- **AI Colo segment:** Use `customer_segment` = "Data Center Colo Provider" + `company_sub_segment` = "AI Signals - colo" (deprecated: "AI - Colocation Operator")
- **MSP/Aggregator:** HubSpot internal value is `Enterprise` (legacy naming)
- **No em dashes** in any customer-facing content
- **Credibility anchors:** Do NOT use in cold emails or LinkedIn. Reserve for discovery calls and follow-ups.
- **Category descriptor:** "Carrier infrastructure" is the ONLY acceptable term (never IaaS, NaaS, platform)

## Context Categories

| Category | Path | What's Inside |
|----------|------|---------------|
| Core | context/core/ | Company identity, messaging, competitive, qualification, ICP, glossary |
| Segments | context/segments/ | Cheatsheets for: colocation, fiber, neocloud, network-op, MSP |
| HubSpot | context/hubspot/ | Property schema, territory model, field values, deal schema, call schema, POC schema |
| Outreach | context/outreach/ | Email rules, fallback messaging, sender profiles |
| Enrichment | context/enrichment/ | Research routes, output schemas, sourcing guide |
| Product | context/product/ | Datasheets, proof points, AI positioning, cloud on-ramp |
| Sales | context/sales/ | Account brief template, call intel, use-case taxonomy, pricing, neocloud strategy, marketplace seeding |
| Marketing | context/marketing/ | Copywriting guidelines, LinkedIn framework, media consumption |
| Copy Strategy | context/copy-strategy/ | Outbound playbook, scoring rubric, segment language/messaging |

## Building Plugins

Run `./build.sh` to assemble all plugins and standalone skill zips into `builds/`.

The build script:
1. Reads each `plugins/*/plugin-manifest.json` to know which skills and context files to bundle
2. Copies `skills/<name>/SKILL.md` + declared `context/` files into a staged folder per plugin
3. Zips plugins → `builds/plugins-zipped/`, standalone skills → `builds/skills-zipped/`
4. Flattens everything into `enterprise/*/upload/` folders (renaming skills to their upload filenames per the `SKILL_RENAME` map in build.sh)

**Plugin manifest fields:** `skills` (list of skill folder names), `context` (relative paths from `context/`), `static` (extra files from the plugin dir).

**Standalone skill zips** (defined in `build.sh`): `account-brief`, `copy-strategist`, `sales-enablement`, `call-prep`, `competitive-intel`. The `copy-strategist` zip also bundles `context/copy-strategy/` as references.

**Enterprise Projects** (5 targets in `enterprise/`):
- `sales-outreach/` — outreach + enrichment skills, core/segments/outreach/copy-strategy context
- `founder-outreach/` — subset of sales-outreach (no sdr-pipeline/import-processor)
- `account-intelligence/` — RevOps + enrichment skills, all context categories
- `call-intelligence/` — call analysis + pipeline discipline + reporting, HubSpot/segments/sales context
- `general-assistant/` — every skill + every context file

Each enterprise folder has a `manifest.md` (upload instructions for Claude.ai) and `upload/` (pre-built files from `build.sh`).

## Creating & Organizing Content

When asked to create new skills, context files, or plugins, follow these conventions.

### Creating a New Skill

1. Create `skills/<skill-name>/SKILL.md` with this structure:
   ```markdown
   ---
   name: <skill-name>
   description: <one-line description>
   ---

   # <Skill Title>

   ## Purpose
   What this skill does and when to use it.

   ## Reference Files
   List the context/ files this skill needs (read these before executing).

   ## Workflow
   Step-by-step instructions Claude follows when running this skill.
   ```
2. Add an entry to the `SKILL_RENAME` map in `build.sh` (~line 166): `"<skill-name>":"maiaedge-<skill-name>"`
3. Add a row to the **Available Skills** table above in the appropriate category
4. To include in an enterprise project, add the skill name to the relevant `for s in ...` loop in `build.sh`
5. The **General Assistant** project auto-discovers all skills in `skills/` (no change needed)

### Creating a New Context File

1. Place the .md file in the appropriate `context/<category>/` folder
2. Existing categories: `core`, `segments`, `hubspot`, `outreach`, `enrichment`, `product`, `sales`, `marketing`, `copy-strategy`
3. If no existing category fits, create a new subfolder under `context/`
4. The file auto-appears in the **General Assistant** enterprise project
5. To include in other enterprise projects, add a `cp` line in the relevant section of `build.sh`
6. To include in a Cowork plugin, add its path to the plugin's `plugin-manifest.json` under `"context"`

### Creating a New Cowork Plugin

1. Create `plugins/<plugin-name>/`
2. Create `plugins/<plugin-name>/plugin-manifest.json`:
   ```json
   {
     "name": "<plugin-name>",
     "version": "1.0.0",
     "skills": ["skill-a", "skill-b"],
     "context": ["category/filename.md", "category/other-file.md"],
     "static": []
   }
   ```
3. Create `plugins/<plugin-name>/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "<Plugin Display Name>",
     "version": "1.0.0",
     "description": "<What this plugin does>"
   }
   ```
4. `build.sh` auto-discovers new plugin folders (no `build.sh` edits needed)
5. Run `bash build.sh` and the new plugin zip appears in `builds/plugins-zipped/`

### Creating a New Enterprise Project

1. Create `enterprise/<project-name>/`
2. Add a new section in `build.sh` following the pattern of existing projects (set up a variable, loop over skills with `copy_skill`, copy context with `copy_context_dir` or individual `cp` lines)
3. Create `enterprise/<project-name>/manifest.md` documenting what skills and context files are included

### After Any Content Change

1. Run: `bash build.sh`
2. **Cowork:** install updated zip from `builds/plugins-zipped/`
3. **Claude.ai Projects:** upload updated files from `enterprise/<project>/upload/`
4. **Commit:** `git add -A && git commit -m "description of change"`

## Team

| Person | Role | Territory | HubSpot Owner ID |
|--------|------|-----------|-----------------|
| Tim Lieto | AVP, North America Sales | East (30 states) | 161889085 |
| Ken Cunningham | Sales, West Region | West (20 states + DC) | 162339176 |
| Timothy Ziemer | CRO & Co-Founder | International | 159350430 |
| Cooper Kennedy | RevOps | — | 160267902 |
| Abilash Menon | CEO & Co-Founder | Strategic | 159974715 |
| Kyle Blackwell | Sales Engineering | — | 159701452 |
| Woody Acosta | Sales Support | — | 162281129 |
