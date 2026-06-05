# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# MaiaEdge AI Toolkit

Sales AI toolkit for MaiaEdge - carrier infrastructure for federated private networking. This repo is the **company brain for maiaedge.io on the GTM / revenue side of the business**: sourcing, enrichment, segmentation, signals, outreach, call intelligence, pipeline reporting, RevOps hygiene, and branded sales collateral. Skills + context + routines + enterprise-project bundles all assemble out of the same canonical knowledge base under `context/`.

## Repo Structure

**Core source (checked-in, edited by hand):**
- `context/` - Reference documents (knowledge base). Single source of truth for all shared context.
- `skills/` - Skill logic (SKILL.md files). Each skill = one folder with one SKILL.md.
- `plugins/` - Plugin packaging for Cowork (manifests + commands + static assets).
- `enterprise/` - Cloud project manifests for Claude.ai enterprise Projects (`upload/` folders populated by `build.sh`).
- `enterprise-prompts/` - System prompts pasted into each Claude.ai enterprise Project's Instructions field. One file per project in `enterprise/`.
- `routines/` - Scheduled and manual-trigger task prompts (split: `claude-code/`, `cowork/`, `outreach-helpers/`, `_shared/`, `archive/`). See "Scheduled Routines - Platform Split" below.
- `cowork-project-instructions/` - System prompts for long-running Cowork projects (e.g. `List-Builder-Project-Instructions.md` - the front-half-of-outbound list builder).
- `scripts/` - Python utility scripts that support routine maintenance (trigger audits, R6/R8 update bodies, source-coverage gates, headline extraction).
- `build.sh` - Assembles plugins and standalone skill zips, and flattens content into `enterprise/*/upload/`.
- `CHANGELOG.md` - Repo-level changelog (messaging reworks, framework migrations, etc.).

**Operational runtime (read/written during scheduled and manual runs):**
- `weekly-reports/` - On-disk artifacts from routines: per-date subfolders (`YYYY-MM-DD/`), `apollo-budget.json` (weekly Apollo cap tracker per `routines/_shared/apollo-weekly-budget-spec.md`), and named subfolders for recurring sweeps (`tier-audit/`, `edge-case-resolution/`, `flagged-deletion-audit/`, `mass-reenrichment/`, `signal-heat-backfill/`, `migration/`).
- `outputs/` - Generated artifacts that are NOT routine reports: `smartlead-health/last-snapshot.json`, `linkedin ads/` deliverables, etc.
- `builds/` - Generated output from `build.sh` (gitignored).


## How to Use a Skill

1. Read the SKILL.md: `skills/<skill-name>/SKILL.md`
2. The skill will reference context files - read those from `context/` as needed
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
| pre-deletion-audit | skills/pre-deletion-audit/ | Gates `customer_segment = "Flagged for deletion"` decisions: dedup check, contact consolidation to ICP primary, 90-day activity preservation |
| crm-guardian | skills/crm-guardian/ | Autonomous CRM maintenance orchestrator - split into **10 independent routines**. **Platform split (2026-04-30):** Routines 0/1/2/4 run on Cowork (web-fetch + Apollo intensive - Cowork has no egress proxy block); Routines 3/5/6/7/8/9 stay on Claude Code (HubSpot-internal, no web dependency). See "Scheduled Routines - Platform Split" section below. Cross-routine Slack canvas ledger (`F0B0AFSB9LN`) holds Tier 3 items across both platforms so they don't accumulate. Routine prompts split across three locations: `routines/claude-code/` (Claude Code routines), `cowork-scheduled-tasks/` (Cowork scheduled tasks, sibling of `routines/`), and `routines/cowork/` (Cowork manual-trigger tasks). Each folder contains a `prompt.md` + sidecar `trigger.md` / `task.md`. **R1 Fresh Enrichment redesign (2026-05-06):** trigger query expanded from 2 filter groups (catching ~391 daily candidates including ~84/100 noise reappearances) to **4 logical filter groups** (5 HubSpot filterGroups, dry-test confirmed ~97 candidates) - A blank-segment, B ICP-partial-fill, C `Unknown` segment (any confidence), D low-confidence Other/Partner Target. Three processing paths: **α full enrichment** (LIKELY_ICP, Apollo-bound 50/run), **β re-research** (Filter Groups C + D + B-without-ICP-keywords, Apollo-free, NEVER outputs "Unknown"), **γ eviction-decision** (LIKELY_NON_ICP/JUNK, Apollo-free). Differentiated Completeness Gates (ICP / Non-ICP / Eviction / Tier 3 Hold) - `last_enriched_date` stamps only on a passing definitive gate; Tier 3 holds keep the record in the active pool with `segmentation_confidence = manual_review_required`. Pre-flight Tier 3 hold exclusion reads canvas F0B0AFSB9LN (R0/R1/R2/R4 sections) to prevent same-day cross-routine collisions (the 2026-05-06 g.softbank.co.jp pattern). Dynamic per-run cap 100/125/150 records based on backlog. Apollo sub-cap raised 30 → 50/run alongside global weekly cap raise 750 → 850. Git commit downgraded to best-effort to handle `.git/index.lock` contention from concurrent routines. Updated DM template surfaces path-by-path counts + drain projection + named α writes + top 5 β reclassifications + γ eviction summary. |
| weekly-signal-scan | skills/weekly-signal-scan/ | Monday signal scrape across all 6 ICPs (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / **Enterprise**). **SPLIT 2026-05-28 into 7 Cowork scheduled tasks:** the monolithic prompt at `cowork-scheduled-tasks/weekly-signal-scan/` was hitting context-budget walls mid-run (Source Coverage Mandate unenforceable; reduced-scope fallback observed 2026-05-25). Now: 6 per-segment scans (`signal-scan-colo` 8:30am, `signal-scan-fiber` 9:30am, `signal-scan-neocloud` 10:30am, `signal-scan-networkop` 11:30am, `signal-scan-msp` 12:30pm, `signal-scan-enterprise` 1:00pm) each write Stage 0-5c for their segment (preflight + source scrape + match + NEW-account creation + score + QA gate + HubSpot narrative write + 5 structured signal fields + tier/heat recompute + on-disk audit). Aggregator (`signal-scan-aggregator` 2:30pm) reads HubSpot for `last_signal_date = today` records, builds 3 territory-consolidated rep DMs (Tim Lieto East `U0A973L1HFF`, Ken West `U0AE1PGCB6C`, Tim Z International routed to Cooper `U0A24D9RJLS`), appends 1 canvas Run log row to `F0B0AFSB9LN`, writes Cooper's cross-ICP run report. **Aggregator graceful degradation:** rep DMs build from HubSpot (source of truth), so 1-2 missing per-segment audit files don't block delivery; only Cooper's run report shows the gap. Schedule interleaves with existing routines (R0 9am, R1 10am, R2 11am, R4 12pm, R-Tier-Audit 3pm, Daily Brief 4pm) at 30-min half-hour marks — no existing routine moves. Signal codes use `NC-` prefix for NeoCloud and `NO-` prefix for Network Op (catalog files use bare `N-`; runtime disambiguates). All Phase 3 rules carried over: 14-day detection window, score floor 8 (LIGHT 8-11 / Worth Reviewing 12-17 / Strong 18-26 / Highest 27+), Title Case heat enum, pure-prose narrative (no date prefix), search-anchor source-coverage pattern, 50-cap per rep, three-tier fill-down (Primary → LIGHT → Carryover News), Tier A + B active + C paired-only, target list = Tier 1+2+3 ICP, hard-cap 50 per rep, no git operations, on-disk audit at `weekly-reports/YYYY-MM-DD/signal-scan/[segment]/segment-run-report.md`. Apollo sub-caps re-allocated across 6 per-segment tasks: Colo 35 / Fiber 35 / NeoCloud 55 / Network Op 50 / MSP 20 / Enterprise 55 = 250 cr/run total (same as monolithic). Monolithic prompt archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/`. **Cowork-only.** |

### Sales Support
| Skill | Path | Function |
|-------|------|----------|
| sales-docs | skills/sales-docs/ | Order Forms, MSAs, POC Agreements, NDAs |
| sales-enablement | skills/sales-enablement/ | Battle cards, discovery guides, collateral |
| call-prep | skills/call-prep/ | Pre-call briefing + talking points |
| competitive-intel | skills/competitive-intel/ | Competitive briefs + positioning |
| branded-doc | skills/branded-doc/ | Generates partner-grade PDFs in the MaiaEdge brand system (Tomorrow font embedded, gold/orange/black palette, doc-style covers, eyebrow-numbered sections, anti-position cards, status-quo hero blocks, table styling, ASCII-to-SVG diagram swaps). Bundles brand.css, all 9 Tomorrow weights, build.py, cover-template.html, segment icons, and the architecture / activation-flow / cloud-on-ramp SVG diagrams. Use for any new partner doc, segment cheat sheet, battle card, playbook, or branded handout that should look like MaiaEdge 101 and the cheat sheets. |

### Call Intelligence
| Skill | Path | Function |
|-------|------|----------|
| call-analysis | skills/call-analysis/ | Extract use cases, segments, signals from HubSpot call summaries |
| pipeline-discipline | skills/pipeline-discipline/ | 3-column pipeline board: accounts->POC, POC->PO, PO->expansion |
| call-reporting | skills/call-reporting/ | Call dashboards, trend analysis, audience-specific briefings |
| daily-sales-activity-brief | (routine only - uses call-analysis Mode 1) | Daily exec sales activity brief delivered to founders + RevOps (Abilash `U06RVK9NTQR`, Tim Z `U08CMD5PMQE`, Cooper `U0A24D9RJLS`). Three identical scannable Slack DMs cover: (1) Headline (what founders need in 90s), (2) Activity-by-rep table (Set / Held / Upcoming-7d per owner), (3) Per-held-call exec snapshot (Headline / Use Cases / Pain on-or-off-thesis / Trajectory / MEDDPICC delta / Next step - 6 lines each), (4) What needs your attention (AT-RISK, STALLING, drift). Pulls THREE engagement pools: Held (calls in last 24h, Mon=72h weekend catch-up), Set (engagements created in same window), Upcoming (scheduled over next 7 days). Internal-Only Filter is intentionally permissive - only obvious internal team syncs (all-MaiaEdge attendees + no external company) are dropped. Non-ICP, partner, and exploratory external calls all surface. **MEDDPICC backfill + refresh runs as a silent side effect** on prospect contacts (same Tier 1 fill / Tier 1 refresh / Tier 2 DRIFT / Tier 3 hold policy as the prior recap routine - contact-level writes ONLY, deal-level MEDDPICC is sync-mirrored from contacts and direct deal-level writes are blocked by HubSpot's calculated-property restriction). Writes are not surfaced in the brief itself - they land in HubSpot quietly with a Cooper audit table on disk. **Renamed 2026-05-05** from "Daily Call Recap" → "Daily Sales Activity Brief". Replaced 4-DM rep cascade with 3 identical exec DMs. **Git operations dropped** - local markdown only at `weekly-reports/YYYY-MM-DD/calls/`, no commits or pushes (orphan `.git/index.lock` was a recurring failure mode and the GitHub raw URLs were a deep-link hack now superseded by self-contained DM bodies). Cadence: Mon-Fri 4:00 PM CT. Scheduled task `taskId = weekly-call-recap` (legacy id retained for path stability), cron `0 21 * * 1-5` UTC (= 4pm CT during CDT). **Cowork-only**. Prompt: `cowork-scheduled-tasks/daily-sales-activity-brief/prompt.md`. Legacy `weekly-call-recap.md` is at `routines/archive/claude-code-disabled/weekly-call-recap.md` (retired same date). |
| weekly-market-news | (routine only - read-only web scraping) | Friday-morning market awareness digest covering all 6 ICPs (5 operator segments + Enterprise as 6th, added 2026-05-11). Per-segment Stage 1 sub-stages mirror Weekly Signal Scan Phase 2 - leverages the SAME comprehensive Source Registries from each `context/signals/[segment]-signals.md` catalog (~160 sources total across reliability tiers - was ~125 before Enterprise catalog addition). Top 3 stories per ICP with article-grounded summary + opinionated "what this means for MaiaEdge" angle, plus Cross-ICP Themes meta-section + Exec Moves callout (buying-persona seniority only). Pure awareness, not action: no HubSpot reads/writes, no scoring, no rep-territory filtering. **Phase 0 mode** - Cooper-only delivery (digest + audit DMs to `U0A24D9RJLS`); Cooper validates voice + source coverage + MaiaEdge angle quality across 2-4 runs, then flips to rep-direct routing. **Migrated to Cowork 2026-04-30** - runs Fri 1pm CT. Cowork prompt: `cowork-scheduled-tasks/weekly-market-news/prompt.md`. |

### Events & Networking
| Skill | Path | Function |
|-------|------|----------|
| event-intelligence | skills/event-intelligence/ | Conference prep, attendee processing, follow-up |
| icp-networking | skills/icp-networking/ | LinkedIn networking automation |

## Scheduled Routines - Platform Split (2026-04-30; R-Tier-Audit + D7 added as Cowork scheduled tasks 2026-05-14)

> **Terminology note:** Many of the table rows below say "routine" - this is grandfathered language from the original Claude Code routine model. R0-R9 + Signal Scan + Weekly Market News + Daily Sales Activity Brief all run as **Cowork scheduled tasks** (cron-fired prompts) regardless of how the docs refer to them. R-Tier-Audit + D7 are explicitly labeled as scheduled tasks below because they were authored from the start with that execution model in mind (fire-and-forget, stateless across runs, no agentic orchestration).


The 15 scheduled routines split across two runtimes based on workload characteristics:

### Run on Cowork (`cowork-scheduled-tasks/`) - daily 9am-3pm CT M-F window + R-Tier-Audit daily M-F + D7 weekly

**Folder location (2026-05-28):** Cowork scheduled tasks live in the top-level `cowork-scheduled-tasks/` folder, a **sibling of `routines/`**. They are explicitly NOT routines — they're cron-fired prompts with no persistent state across runs. Cowork **manual-trigger** tasks (which DO live in `routines/cowork/`) are the separate non-cron pool.

These tasks are web-scraping / Apollo-intensive and were degraded on Claude Code's CCR runtime by an egress-proxy block (`web_fetch` returning HTTP 403 `host_not_allowed`). Cowork has no equivalent block, so they run reliably there. Each task folder contains `prompt.md` (the payload) + `task.md` (schedule, MCP, Apollo budget, update procedure).

| Task | Cowork Prompt | Recommended Schedule (CT) |
|---|---|---|
| Import Validator (R0) | `cowork-scheduled-tasks/r0-import-validator/prompt.md` | 9:00 AM daily M-F |
| Fresh Enrichment (R1) | `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` | 10:00 AM daily M-F |
| Stale Re-Enrichment (R2) | `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` | 11:00 AM daily M-F |
| Flagged Consolidation (R4) | `cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md` | 12:00 PM daily M-F |
| **Signal Scan: Colo (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-colo/prompt.md` | **8:30 AM Monday** (split from monolithic weekly-signal-scan) |
| **Signal Scan: Fiber (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-fiber/prompt.md` | **9:30 AM Monday** |
| **Signal Scan: NeoCloud (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-neocloud/prompt.md` | **10:30 AM Monday** |
| **Signal Scan: Network Op (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-networkop/prompt.md` | **11:30 AM Monday** |
| **Signal Scan: MSP/Aggregator (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-msp/prompt.md` | **12:30 PM Monday** |
| **Signal Scan: Enterprise (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-enterprise/prompt.md` | **1:00 PM Monday** (uses slot freed by archived monolithic) |
| **Signal Scan: Aggregator (NEW 2026-05-28)** | `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` | **2:30 PM Monday** (reads HubSpot for `last_signal_date = today` records; builds 3 rep DMs + canvas Run log + Cooper run report; 1h 15m cushion absorbs per-segment runtime overruns; Apollo budget 0; archived monolithic at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/`) |
| Weekly Market News | `cowork-scheduled-tasks/weekly-market-news/prompt.md` | 1:00 PM Friday |
| Daily Sales Activity Brief | `cowork-scheduled-tasks/daily-sales-activity-brief/prompt.md` | 4:00 PM daily M-F (renamed from "Daily Call Recap" 2026-05-05; reframed as exec brief to Abilash + Tim Z + Cooper, MEDDPICC backfill kept as silent side effect, git operations dropped) |
| **R-Tier-Audit (NEW 2026-05-14)** | `cowork-scheduled-tasks/r-tier-audit/prompt.md` | **Daily M-F, 3:00 PM CT (cron `0 20 * * 1-5` UTC = 3pm CT during CDT; daily cadence rolled out 2026-05-21 to tighten open-deal Hot detection from 7-day to 24h. 10% circuit breaker.) Daily drift correction sweep over all active ICP records; honors `hs_is_target_account` freeze on tier (NOT on heat); idempotent no-op if computed_tier == current_tier AND computed_heat == current_heat. Cadence history: monthly 2026-05-14 → weekly Fri 2026-05-15 → daily M-F 2026-05-21 per Cooper - task is Apollo-free + idempotent so daily-cadence cost is ~1 min/run. Stateless across runs, no agentic orchestration.** |
| **D7 Edge Case Resolution (NEW 2026-05-14)** | `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md` | **Weekly (Cooper-chosen day; suggested Wed 9am CT, cron `0 14 * * 3` UTC = Wed 9am CT during CDT). Processes manual_review queue >7 days, low_5069 >60 days, Unknown/Other with deal activity, crm-hygiene flagged records; per-run cap 30 records; hard 14-day max for manual_review_required; Apollo budget 0. HubSpot is source of truth for the queue; no persistent task-local state across runs.** |
| **CRM Ops Daily Digest** | `cowork-scheduled-tasks/crm-ops-daily-digest/prompt.md` | **Daily M-F 4:45 PM CT (cron `45 21 * * 1-5` UTC during CDT). End-of-day fleet digest: the single ops surface for Cooper. Reads HubSpot deltas (ground truth) + the working-ledger canvas `F0B0AFSB9LN` Run log + on-disk run reports + `apollo-budget.json`; refreshes a dedicated ops dashboard canvas to current state and sends ONE short DM to Cooper. The only action it surfaces is the Flagged-for-deletion queue (by reason code); everything else is glanceable status. Read-only on HubSpot, Apollo budget 0. Ops routines stay quiet on success and ping immediately only on hard failure; their full debriefs are replaced by this digest + the dashboard.** |

### Cowork manual-trigger tasks (`routines/cowork/`) - no cron, fired by Cooper inside the CRM Guardian Cowork project

| Task | Cowork Prompt | When to fire |
|---|---|---|
| Flagged-for-Deletion Audit | `routines/cowork/flagged-for-deletion-audit/prompt.md` | Whenever Cooper wants to validate the `customer_segment = "Flagged for deletion"` pool before bulk-deleting. READ-ONLY by default; writes only when `WRITE_BACK = "enabled"` and verdicts are approved. Apollo budget 0. |
| Mass Re-Enrichment Sweep | `routines/cowork/mass-reenrichment/prompt.md` | Whenever the enrichment framework changes meaningfully and the active pool needs revalidation. Self-resumes across Cowork chats via `last_enriched_date` + sweep kickoff date. Apollo uncapped during the sweep window; restore 850/wk after. |

The corresponding Claude Code routines were **disabled** on 2026-04-30 (`enabled: false` via `RemoteTrigger.update`). The Claude routine prompt files are archived at `routines/archive/claude-code-disabled/` as the canonical historical reference; the Cowork prompts inline the operational rules and are self-contained for Cowork's runtime. **Do not re-enable** the disabled Claude Code routines without Cooper's explicit direction.

### Stay on Claude Code Routines

These are HubSpot-internal, no web dependency, run cleanly under CCR. Each routine folder under `routines/claude-code/` contains `prompt.md` (the payload) + `trigger.md` (trigger ID, cron, environment, MCP, update procedure).

| Routine | Folder | Claude Code Trigger | Schedule (UTC) | Local (ET) |
|---|---|---|---|---|
| Routine 3: Duplicate Accounts | `routines/claude-code/r3-duplicate-accounts/` | `trig_01XTjFhegfVTCtSpZXEDY5Ce` | `0 7 * * *` | 2am daily |
| Routine 5: Contact Dedup | `routines/claude-code/r5-contact-dedup/` | `trig_01Rw3KUsEXj2eoKKRKRCgGCZ` | `0 6 * * 0` | Sun 1am |
| Routine 6: Territory & Hygiene | `routines/claude-code/r6-territory-hygiene/` | `trig_01BmhnoyxFVrNXuqGcNnW6FV` | `0 6 * * *` | 1am daily |
| Routine 7: Monthly Sourcing | `routines/claude-code/r7-monthly-sourcing/` | `trig_01WyVys2Jpi88JsoU5Pa4qve` | `0 14 1 * *` | 1st of month, 9am |
| Routine 8: Persona Fill | `routines/claude-code/r8-persona-fill/` | `trig_011jpGwhJQS8dJY3i7qU1StA` | `0 14 * * 5` | Fri 9am |
| Routine 9: Job Changes (Quarterly) | `routines/claude-code/r9-quarterly-job-changes/` | `trig_01Uw6RXKwGbjZfS2WaPeudKw` | `0 14 1 1,4,7,10 *` | Quarterly |

### Outreach helpers (`cowork-project-instructions/`) - manual, list-driven (moved from `routines/outreach-helpers/` 2026-06-02)

Not scheduled. Cooper / reps run these as Cowork project instructions when processing a specific list. Each file is a self-contained processing protocol that reconciles with and consumes the outreach skills (`cold-email`, `linkedin-outreach`, `sdr-pipeline`). Both carry a Research Quality gate: validate the Account Brief against current research, only reference FRESH signals (event date ≤90d, ideally ≤60) as the reason to meet, no stale signals cited as current, no wrong facts (`infrastructure_profile` beats revenue on conflict).

| Helper | Path | Use when |
|---|---|---|
| Cold List Outreach | `cowork-project-instructions/Cold-Outreach-Project-Instructions.md` | Processing a cold contact list (no event anchor) into send-ready 3-email + optional LinkedIn outreach. |
| Tradeshow Outreach | `cowork-project-instructions/Tradeshow-Outreach-Project-Instructions.md` | Event-anchored outreach (any show — ITW, PTC, Metro Connect, etc.) where the shared moment carries the relevance. Parameterized via an Event Configuration Block. |

### Cooper's only manual step

Filter HubSpot Contacts → `flagged_for_deletion = true` → review and bulk-delete. Then filter Companies → `customer_segment = "Flagged for deletion"` → archive (severs stale associations from R3/R4 reassociations). Everything else is automated.

---

## Key Rules (apply to ALL skills)

- **Speed language:** Always pair speed with ownership ("your team provisions in minutes") EXCEPT for Neoclouds (they ARE the customer - drop sovereignty)
- **Territory:** East = Tim Lieto, West = Ken Cunningham, International = Tim Ziemer
- **Account tiers are INVERTED:** Tier 1 = highest priority, Tier 5 = lowest. Tier computation lives in `context/account-tiering/tier-compute-spec.md` - every routine that writes tier (R1, R2, Weekly Signal Scan Stage 5b, R6, R-Tier-Audit daily M-F, D7 weekly) inlines that spec. See "Account Tier Computation" rule below.
- **Account Tier Computation:** Canonical algorithm at `context/account-tiering/tier-compute-spec.md`. Reads `(customer_segment, company_sub_segment)` from a 30-row defaults table; applies 6 signal modifiers (hot/white-hot/stacked/open deal/stale/sustained quiet); clamps to ceiling/floor; honors `hs_is_target_account = true` (freezes `account_tier` only). Inverted convention: Tier 1 = highest priority.
- **Sub-segment qualification:** Single source of truth is `context/account-tiering/sub-segment-qualification-full.md` (the consolidated reference). Short pointer file: `context/account-tiering/sub-segment-qualification.md` lists the 30 active sub-segment values (verified via HubSpot MCP 2026-05-14). Companion docs in the same folder: `d1-global-disqualifiers.md`, `d2-wholesale-arm-policy.md`, `d3-disambiguation-flowcharts.md`, `icp-deep-dives/` (6 per-ICP deep-dives). Quarterly anchor refresh per RevOps calendar; next refresh 2026-08-14.
- **Enrichment protocols:** Operational D5 v2 protocols at `context/account-tiering/enrichment-protocols.md` — **self-contained as of 2026-05-14**: all 30 protocols (one per sub-segment: N1-N5, F1-F6, C1-C4, NC1-NC5, M1-M5, E1-E4, G) inlined in §6 with full 5-question evidence tables + anchors + tiebreakers; NC1 vs NC3 vs NC2 deterministic threshold matrix in §6a (disclosed GPU MW + facility count + pricing model + customer profile); Greenfield migration patterns + D7 fallback in §7 (4-tier pattern catalog: operational milestone / abandonment / construction-progress / stalled). 5-stage research-first workflow (Stage 0 Identity -> Stage 1a D1 quick check -> Stage 1b deep research populating 7 enriched fields -> Stage 1c D1 deep check -> Stage 2 segment routing -> Stage 3 D3 flowchart + D5 protocol -> Stage 4 compute_tier -> Stage 5 HubSpot write). Best-fit classification with calibrated confidence; NO default `manual_review_required` (Cooper 2026-05-14). Multi-marker classification using `infrastructure_profile` as primary structured signal. 2-4 sentence conciseness cap on narrative fields.
- **AI Colo segment:** Use `customer_segment` = "Data Center Colo Provider" + `company_sub_segment` = "AI Signals - colo" (deprecated: "AI - Colocation Operator")
- **MSP/Aggregator:** HubSpot internal value is `MSP/Aggregator` (matches display label as of 2026-05-07; previously `Enterprise`, now retired).
- **Enterprise (Multi-DC ICP):** HubSpot internal value `Enterprise-CustomerSegment` is an ICP segment as of 2026-05-11 (priority 5 - lowest of the ICPs but qualified and sellable). Scope is multi-DC enterprises with in-house network engineering teams. Four `company_sub_segment` values: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Hard gate: vertical (one of the four) AND scale ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR in-house net eng). Manufacturing, Energy/Utilities, Logistics/Supply Chain are Watch List, not Enterprise. Government/Defense is FedRAMP-gated. Anchor account: Meijer.
- **`hs_is_target_account` (manual override):** Freezes `account_tier` ONLY. Segment, sub-segment, signal field, enriched field, AND `signal_heat` writes all proceed normally. Legacy property name `target_account` was renamed to `hs_is_target_account` (HubSpot built-in ABM property) 2026-05-13. 382 records carry `true` post-migration. Skills + routines reference `hs_is_target_account` exclusively post-Phase 3.
- **`signal_heat` (rep-facing intent rollup):** 4-bucket enum (`Hot` / `Warm` / `Cool` / `Cold` — **Title Case** per HubSpot, verified via MCP 2026-05-28) computed by `compute_signal_heat` in `context/account-tiering/tier-compute-spec.md` §11.5. Same inputs as `compute_tier` signal modifiers (`last_signal_score`, `last_signal_date` — **event date** semantics post-2026-05-28, `signal_count_last_30d`, open-deal state). Created in HubSpot 2026-05-20. Written by Weekly Signal Scan Stage 5b, R-Tier-Audit, R0 (new-account default `Cold`), R1 Path α (new-account default `Cold`), R2 RE_ENRICH_FULL, R6 Step 5.5, and the 5 outreach skill push-backs (cold-email / linkedin-outreach / account-brief / prospect-research / sdr-pipeline — `call-prep` excluded per Cooper 2026-05-28). **NOT frozen by `hs_is_target_account`** - tier is rep-locked; heat always reports the truth. Heat-only recomputes do NOT bump `last_enriched_date`.
- **`account_tier_legacy` is ARCHIVED 2026-05-13.** Created Phase 1.3 then archived per Cooper's direction. Rollback mechanism is on-disk audit at `weekly-reports/migration/2026-05-13-*.md`. NEVER write to this field. NEVER reference it in skills, routines, or context files.
- **`maiaedge_value_proposition` is OUT OF ENRICHMENT SCOPE.** Per Cooper 2026-05-14: populated by outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) on-demand at outreach time using customer_segment-specific messaging template. Enrichment bot does NOT write this field.
- **No em dashes** in any customer-facing content
- **Credibility anchors:** Do NOT use in cold emails or LinkedIn. Reserve for discovery calls and follow-ups.
- **Category descriptor:** "Carrier infrastructure" is the ONLY acceptable term (never IaaS, NaaS, platform)
- **HubSpot writes go through MCP, not import files.** Enrichment, sourcing, contact creation, deal creation, segment/owner/tier updates - all happen via direct HubSpot MCP calls. Only produce a CSV/XLSX when the user explicitly asks for a file or when the source material the user hands you is already a file (see `import-processor`).
- **New deals default to `appointmentscheduled`.** When asked to create a deal in HubSpot, set `dealstage` = `appointmentscheduled` ("Appointment Scheduled") unless the user explicitly specifies a later stage. Full defaults and rationale in `context/hubspot/deals-schema.md` → "Deal Creation Defaults".
- **`flagged_for_deletion_reason` is a MANDATORY companion to `customer_segment = "Flagged for deletion"`.** Any skill/routine/scheduled task that sets `customer_segment = "Flagged for deletion"` on a Company MUST in the same write set `flagged_for_deletion_reason` (multi-line text). Lead the value with ONE of the 7 canonical reason codes, then a colon and one concrete sentence of evidence: `Dead domain` / `Hard junk / non-business` / `D1 disqualified (no reference value)` / `No ICP fit` / `Duplicate (merged)` / `Defunct / out of business` / `Stalled greenfield`. The scannable code lives in this field; the 2-4 sentence prose rationale stays in `account_brief`. **Clear-on-exit:** when a record is moved back OFF `Flagged for deletion` into any active segment, clear `flagged_for_deletion_reason` to empty in the same write. Writers: R0/R1/R2/R3/D7/mass-reenrichment + `company-enrichment`/`segment-classification`/`pre-deletion-audit`/`crm-guardian`. Readers (surface, never set): R4, Flagged-for-Deletion Audit. Full spec + examples: `context/hubspot/property-schema.md` §2.1; companion-write rule inlined in `context/account-tiering/enrichment-protocols.md` §1.

## Operating Principles (Cooper Feedback 2026-05-14)

These 12 principles, distilled from Cooper's 2026-05-14 feedback (principles 1-10) + the 2026-05-20 `signal_heat` rollout (principle 11) + the 2026-05-28 Signal Engine Unification (principle 12), govern all enrichment / classification / tier / heat work:

1. **No-default-manual-review.** Classification routes to a sub-segment (best-fit + tiebreaker) OR `Flagged for deletion`. `manual_review_required` is reserved for genuine multi-classification ambiguity (clear positive evidence for 2+ sub-segments AND tiebreaker fails). Target manual_review population <5% of records.
2. **Multi-marker classification.** `infrastructure_profile` (multi-select enum with bands for Facilities / Route Miles / POPs) is the PRIMARY structured signal. Each sub-segment has a canonical pattern (file 06 §5 + D5 §5 / `context/account-tiering/enrichment-protocols.md` §4). When `infrastructure_profile` conflicts with `annualrevenue`, `infrastructure_profile` wins. Revenue data is dirty more often than infrastructure.
3. **Read from 8 enriched fields, not HubSpot defaults.** Classification reads `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`. HubSpot `description` and `industry` are last-resort only.
4. **2-4 sentence conciseness cap** on narrative enriched fields (`account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`). At thousands-of-records scale, brevity beats completeness. **Pure prose, NO metadata prefix.** No leading `[Routine N]` tag, no leading `[YYYY-MM-DD]:` date prefix, no bracketed audit metadata of any kind. The routine that wrote the field is recoverable from `last_enriched_date` + the on-disk per-run report + git history; the date is structured in `last_enriched_date` (and in `last_signal_date` for the signal field). On eviction paths the brief describes WHAT the entity is and adds a trailing clause noting the flag — the flag itself is structured by `customer_segment = "Flagged for deletion"`. Audit trail of which routine touched what lives in `weekly-reports/YYYY-MM-DD/` + the per-run Slack DM, NOT inside the field.
5. **Research-first workflow (5 stages).** Bot populates 7 enriched fields during research (Stage 1b) BEFORE classification (Stages 2-3). Tier compute at Stage 4. HubSpot write at Stage 5. NO separate `maiaedge_value_proposition` generation stage.
6. **`maiaedge_value_proposition` is NOT in enrichment scope.** Outreach skills populate this field on-demand at outreach time. Enrichment bot leaves it alone.
7. **Aggressive `Flagged for deletion` for non-fits.** Records with no positive evidence for ANY ICP sub-segment -> `Flagged for deletion` (not parked in `Other`). `Other` is reserved for D1 disqualifier matches that are useful as competitive/partner references.
8. **`Greenfield` is a REAL sub-segment.** For actively-being-built Colo + NeoCloud companies (Series A-C funded, sites under construction). Pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` parent. Auto-migrates to operational sub-segment when first operational site goes live.
9. **`Crypto to AI - Neoclouds` is INCLUSIVE** of operator AND landlord models. Former bitcoin miners pivoting to AI infrastructure regardless of business model. Crusoe (flared-gas BTC mining lineage), IREN, Core Scientific, Galaxy Digital, Bitfarms, TeraWulf, APLD / Applied Digital, Northern Data Group, Prometheus Hyperscale / Hut 8 lineage all land here. **Companies previously listed as Large Scale GPU - Neocloud or AI Signals - colo anchors but with BTC mining heritage now route to NC5 instead** (Crusoe, Applied Digital, Prometheus Hyperscale moved 2026-05-14).
10. **`Subsea cable operator` is the 30th sub-segment** under Network Operator parent. Pure-play subsea operators with minimal terrestrial backbone. Verified HIGH anchors: Aqua Comms (now EXA-owned — verify operating-status), Seaborn Networks, Hawaiki Submarine Cable / BW Digital. BORDERLINE: Telxius (Telefónica subsidiary, has terrestrial), PLDC. D1-evicted: pure consortiums (FLAG, SEA-ME-WE, ACE, EIG) + cable vendors/manufacturers (ASN, HMN Tech, NEC OCC, SubCom) + pure-financing hyperscaler SPVs. Verified-operator pool is genuinely small (~3-5 globally) — most "subsea" candidates classify at `low_5069` until D7 web-research re-validates.
11. **`signal_heat` is the rep-facing rollup of signal score + recency + deal context.** Tier = strategic value (segment-anchored, floor/ceiling clamped). Heat = current intent (decays automatically with the signal date window). Same inputs, both computed in every routine that writes signal fields. `hs_is_target_account` freezes tier but NOT heat — heat always tells the truth. Compute spec at `context/account-tiering/tier-compute-spec.md` §11.5. Property created in HubSpot 2026-05-20.
12. **Signal Engine Unification (2026-05-28) — locked 5-field set.** The signal engine has **exactly 5 HubSpot company fields, no more, no fewer**: `recent_news_or_trigger_event` (narrative, pure prose, no date prefix), `last_signal_date` (date — **event date**, when the news/funding/hire actually happened, NOT detection date — semantics narrowed 2026-05-28), `last_signal_score` (number), `signal_count_last_30d` (number), `signal_heat` (enum, **Title Case**: `Hot` / `Warm` / `Cool` / `Cold`). Canonical inventory at `context/account-tiering/tier-compute-spec.md` §11.6. `compute_tier` modifiers + `compute_signal_heat` key off `last_signal_date` (event date). The narrative drops its legacy `[YYYY-MM-DD]` date prefix — the date lives structurally. Writers: Signal Scan + R0/R1/R2/R6/R7/D7/R-Tier-Audit/mass-reenrichment, plus 5 outreach skill push-backs (cold-email / linkedin-outreach / account-brief / prospect-research / sdr-pipeline — `call-prep` excluded). Outreach push-backs run as the **absolute final step** after the rep-facing primary output is delivered; failures never block. **Do not add new signal-engine fields without an explicit redesign turn.**

## Known Data Quality Follow-ups (post-2026-05-13 migration)

Outstanding items flagged during the Account Tiering & Segmentation Overhaul migration:

1. **5 MSP/Aggregator records carry colo sub-segment values** - Mapletree, Montera Infrastructure, PTS Data Center Solutions, Lonestar Data Holdings, LS Power. Phase 2.8 skipped these as `no_default`. Recommend either (a) reclassify as Colo with appropriate colo sub-segment, or (b) reclassify the sub-segment to an MSP value. R-Tier-Audit handles these via the segment null fallback + warning log.
2. **0 records on `TSD Technology Services Distributor - MSP`** - Canonical TSD brands (TD SYNNEX, ScanSource, Intelisys, AppDirect) are not currently in the MSP/Aggregator population. Either absent from CRM or classified elsewhere. Account-sourcing follow-up.
3. **Verizon / Verizon Enterprise + Vodafone UK / Vodafone Group Plc + China Telecom / China Telecom Global + NTT / NTT Global Data Centers duplicate-pair candidates.** Run Routine 3 (Duplicate Accounts) over Tier 1 records to validate or merge per the D2 wholesale-arm policy in file 06.
4. **Suspect annual revenue data** on NaviSite ($211.9B - matches Spectrum, likely copy/paste) and GAC ($19.1B - Gulf Agency Co, shipping logistics not telecom). Flag for data quality cleanup. Multi-marker classification (infrastructure_profile primary) avoids tier mistakes from dirty revenue.
5. **GPU pricing trend refresh (RESOLVED 2026-05-14):** H100 1-year contract pricing reversal (+40% Oct 2025 -> Mar 2026, $1.70 -> $2.35/hr) is documented in `context/segments/neocloud.md` at lines 579, 594, 597, 668. The prior assumption that GPU prices were collapsing in a straight line has been invalidated; pricing reversal rewards operators with locked-in capacity and high utilization.
6. **Master Agent independent-anchor list thin** - only 2 verified independents post-2018-2024 consolidation (X4 Solutions confirmed; CyberNet Communications medium). Cooper 2026-05-14 reversed prior default-manual-review policy - classify best-fit with `low_5069` for thin anchor verification; D7 re-validates.
7. **Subsea cable operator policy (NEW 2026-05-14 - added as 30th sub-segment).** Phase 3 encodes the protocol; quarterly refresh will validate anchor list.

## Unified `last_enriched_date` Stamping Policy (effective 2026-05-03)

`last_enriched_date` is the field that gates the 120-day re-enrichment rotation in R2. It must reflect ONLY runs through the full enrichment pipeline (Stages 1-3 of company-enrichment + Apollo + segment-classification + Completeness Gate pass), or definitive eviction resolutions. Targeted/partial writes do NOT bump.

| Routine | Path / scenario | Bump? |
|---|---|---|
| R0 Import Validator | MISDOMAIN / RENAMABLE / MATCH / AMBIGUOUS | NO (R1 picks up) |
| R0 Import Validator | HARD_FLAG / DEAD_DOMAIN eviction | YES |
| R1 Fresh Enrichment | LIKELY_ICP full enrichment + gate pass | YES |
| R1 Fresh Enrichment | Gate fail / Tier 3 hold | NO |
| R1 Fresh Enrichment | LIKELY_NON_ICP / LIKELY_JUNK eviction | YES |
| R2 Stale Re-Enrichment | RE_ENRICH_FULL + gate pass | YES |
| R2 Stale Re-Enrichment | RE_ENRICH_LIGHT eviction (PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN) | YES |
| R2 Stale Re-Enrichment | Tier 3 / inconclusive | NO |
| R3 Duplicate Accounts | dedup primary selection | NO |
| R4 Flagged Consolidation | contact reassociation / flag | NO |
| R5 Contact Dedup | contact-only writes | NO |
| **Signal Scan** | **Stage 5 partial writes (news / brief / infra) - NO** |
| Signal Scan | Stage 3 NEW-account creation (full pipeline ran) | YES |
| R6 Territory & Hygiene | territory / hygiene / sub_segment / tier corrections | NO |
| R8 Persona Fill | contact-only writes | NO |
| R9 Quarterly Job Changes | contact-only writes | NO |
| Daily Call Recap | MEDDPICC contact-only writes | NO |
| **R-Tier-Audit (daily M-F)** | **tier-only writes (no enrichment)** | **NO** |
| **R-Tier-Audit (daily M-F)** | **`signal_heat`-only recomputes (no tier or enrichment)** | **NO** |
| **Signal Scan Stage 5b** | **`signal_heat` recompute alongside tier/signal-field writes** | **NO** |
| **R6 Step 5.5** | **`signal_heat` recompute alongside tier maintenance** | **NO** |
| **D7 Edge Case Resolution (weekly)** | **PASS resolution (sub-segment upgrade after deep research)** | **YES** |
| **D7 Edge Case Resolution (weekly)** | **D1 eviction surfaced via D7 research** | **YES** |
| **D7 Edge Case Resolution (weekly)** | **Stale low_5069 carry (no resolution this run)** | **NO** |
| **D7 Edge Case Resolution (weekly)** | **Manual-review escalation to Cooper (no write)** | **NO** |
| **cold-email signal push-back (NEW 2026-05-28)** | **Final-step signal write at outreach time (recent_news + last_signal_date + score + count + heat + tier)** | **NO** |
| **linkedin-outreach signal push-back (NEW 2026-05-28)** | **Final-step signal write at outreach time** | **NO** |
| **account-brief signal push-back (NEW 2026-05-28)** | **Final-step signal write at outreach time** | **NO** |
| **prospect-research signal push-back (NEW 2026-05-28)** | **Final-step signal write at outreach time (alongside the existing maiaedge_value_proposition write)** | **NO** |
| **sdr-pipeline signal push-back (NEW 2026-05-28)** | **Per-company final-step signal write at outreach time** | **NO** |
| **Signal Engine Backfill (one-time, optional)** | **Narrative cleanup + null `last_signal_date` backfill from legacy prefix** | **NO** |

The biggest behavioral fix is Signal Scan (changed 2026-05-03). Previously stamped on every signal-touched account, which hid hot accounts from R2's 120-day rotation. Now stamps only on Stage 3 NEW-account creates. R2 owns the rotation guarantee - every active account gets a full segment / sub_segment / Apollo / brief refresh at minimum every 120 days regardless of signal activity.

Companion freshness mechanisms in R2 (added 2026-05-03):
- **account_brief regeneration on every FULL pass** (not the prior >30-day staleness check). 120-day rotation guarantees a content audit at this cadence.
- **recent_news_or_trigger_event staleness clearing**: if `last_signal_date` (event date) >90 days old AND no Signal Scan write in last 7 days → clear both `recent_news_or_trigger_event` AND `last_signal_date` so the structured + narrative pair stay consistent. Simplified 2026-05-28 — was previously parsing a `[YYYY-MM-DD]` prefix string from the narrative; now reads `last_signal_date` directly. Stale news showing as current is worse than no news.
- **Step 0B MISDOMAIN check** in RE_ENRICH_FULL path: catches longstanding wrong domains on ICP records that R0's 24-hour window missed. Re-enriches against the corrected domain.

## Apollo Weekly Budget Cap (effective 2026-05-06; supersedes 2026-05-03 750-cap)

**Hard cap of 850 Apollo credits per ISO week** across all routines. Tracked via `weekly-reports/apollo-budget.json` per `routines/_shared/apollo-weekly-budget-spec.md`. Each Apollo-consuming routine reads the tracker at run start, scales its budget to `min(sub_cap, available)`, and updates the tracker post-run with actual consumption + best-effort git commit (see note below).

| Routine | Cadence | Sub-cap (per run) | Weekly draw | % of 850 |
|---|---|---|---|---|
| **Signal Scan: Colo** | Mon | 35 | 35 | 4% |
| **Signal Scan: Fiber** | Mon | 35 | 35 | 4% |
| **Signal Scan: NeoCloud** | Mon | 55 | 55 | 6% |
| **Signal Scan: Network Op** | Mon | 50 | 50 | 6% |
| **Signal Scan: MSP/Aggregator** | Mon | 20 | 20 | 2% |
| **Signal Scan: Enterprise** | Mon | 55 | 55 | 6% |
| **Signal Scan: Aggregator** | Mon | 0 | 0 | 0% |
| **Signal Scan total** | Mon | — | **250** | **29%** (same as monolithic; just re-allocated across 6 per-segment tasks) |
| R1 Fresh Enrichment | M-F | 30 | 150 | 18% |
| R8 Persona Fill | Fri | 175 | 175 | 21% |
| R2 Stale Re-Enrichment | M-F | 50 | 250 | 29% |
| R6 Territory & Hygiene | M-F | 5 | 25 | 3% |
| **Steady-state weekly** |  |  | **850** | **100%** |
| R9 Quarterly Job Changes | quarterly | spare-capacity | varies | n/a |

R9 takes whatever's available in the spare capacity of its quarterly fire week. R0, R3, R4, R5, Daily Call Recap, Weekly Market News, **R-Tier-Audit (daily M-F)**, and **D7 Edge Case Resolution (weekly)** do not consume Apollo and are out of scope for the cap. R-Tier-Audit is pure HubSpot read/compute/write. D7 uses web_fetch + web_search only (Apollo budget 0).

**2026-05-06 change rationale:** R1 Fresh Enrichment redesigned with a 4-filter-group trigger query (cuts daily candidate pool from 391 → ~97 by excluding `Other`/`Partner Target` records that already have `high_90` confidence) and a three-path workflow (Path α full enrichment Apollo-bound 50/run; Path β re-research Apollo-free; Path γ eviction Apollo-free). Bumping R1 sub-cap from 30/run to 50/run and the global cap from 750 to 850 funds Path α at the new dynamic record cap (100/125/150 records/run depending on backlog). R1 monthly Apollo draw rises from ~600 to ~1,000, total routine-driven Apollo consumption from ~3,225/month to ~3,650/month - still leaves ~2,350/month headroom in the 6,000/month global allocation.

**2026-05-21 change rationale:** Sized the fleet for the 5,000-record steady-state target. R1 sub-cap reduced 50 → 30/run (peak observed daily was 22 on 2026-05-12, average 5-10/day - 30/day stays 36% over peak); the freed 100 cr/wk transfers to R2 (sub-cap 30 → 50/run) to support the 120-day re-enrichment rotation at 5,000 active records (break-even is ~42 records/day FULL; 50/day buys 67% headroom). Global weekly cap unchanged at 850; net Apollo impact zero. Same change also moved R-Tier-Audit weekly Fri → daily M-F to catch open-deal Hot transitions within 24h, with the circuit breaker loosened 5% → 10% so normal drift flows through at daily cadence.

**Git commit policy (R1 specific, 2026-05-06):** Apollo budget post-run write to JSON is REQUIRED. The follow-on `git add/commit/push` is best-effort with a 10s timeout - on `.git/index.lock` held by a concurrent routine or non-zero git exit, log `Git commit deferred (concurrent routine); JSON updated locally` to the Slack DM and continue. Slack DM is the Apollo audit trail of record. Other routines may adopt the same pattern at their authors' discretion.

## Context Categories

| Category | Path | What's Inside |
|----------|------|---------------|
| Core | context/core/ | Company identity, messaging, competitive, qualification, ICP, glossary |
| Account Tiering | context/account-tiering/ | Canonical tier-compute spec, sub-segment qualification pointer (30 values), D5 v2 enrichment protocols (§6 inlined per-sub-segment + §6a NC threshold matrix + §7 Greenfield catalog) |
| Segments | context/segments/ | Cheatsheets for: colocation, fiber, neocloud, network-op, MSP |
| HubSpot | context/hubspot/ | Property schema, territory model, field values, deal schema, call schema, POC schema |
| Outreach | context/outreach/ | Email rules, fallback messaging, sender profiles |
| Enrichment | context/enrichment/ | Research routes, output schemas, sourcing guide |
| Product | context/product/ | Datasheets, proof points, AI positioning, cloud on-ramp |
| Sales | context/sales/ | Account brief template, call intel, use-case taxonomy, pricing, neocloud strategy, marketplace seeding |
| Marketing | context/marketing/ | Copywriting guidelines, LinkedIn framework, media consumption |
| Copy Strategy | context/copy-strategy/ | Outbound playbook, scoring rubric, segment language/messaging |
| Signals | context/signals/ | Signal framework (scoring, sources, delivery) + per-segment signal catalogs for weekly-signal-scan |
| Partner Assets | context/partner-assets/ | Source markdowns for partner-facing PDFs (MaiaEdge 101, 5 segment cheatsheets, Product Quick Reference). Consumed by the `branded-doc` skill. |
| Customer Facing Documents | context/Customer Facing Documents/ | Live, published customer-facing collateral (PDFs + infographics + decks) used as reference for tone, design, and approved positioning. Not used as Claude context input - this is the human-grade output library. |

## Building Plugins

Run `./build.sh` to assemble all plugins and standalone skill zips into `builds/`.

The build script:
1. Reads each `plugins/*/plugin-manifest.json` to know which skills and context files to bundle
2. Copies `skills/<name>/SKILL.md` + declared `context/` files into a staged folder per plugin
3. Zips plugins → `builds/plugins-zipped/`, standalone skills → `builds/skills-zipped/`
4. Flattens everything into `enterprise/*/upload/` folders (renaming skills to their upload filenames per the `SKILL_RENAME` map in build.sh)

**Plugin manifest fields:** `skills` (list of skill folder names), `context` (relative paths from `context/`), `static` (extra files from the plugin dir).

**Cowork plugins** (10 targets in `plugins/`):
- `maiaedge-outreach/` - cold-email, linkedin-outreach, prospect-research, segment-classification (outbound writing surface for AEs)
- `maiaedge-sdr-pipeline/` - end-to-end sdr-pipeline batch (company list → 3-email sequences + Smartlead XLSX)
- `maiaedge-enrichment-pipeline/` - account-sourcing, company-enrichment, import-processor, edge-case-researcher (sourcing + enrichment loop)
- `maiaedge-revops/` - contact-discovery, crm-hygiene, pipeline-analytics, territory-manager, pre-deletion-audit, crm-guardian (RevOps operations surface)
- `maiaedge-call-intelligence/` - call-analysis, pipeline-discipline, call-reporting (HubSpot call intel + dashboards)
- `maiaedge-weekly-signals/` - weekly-signal-scan (Monday signal scrape; Cowork-only execution)
- `maiaedge-sales-support/` - account-brief, call-prep, competitive-intel, sales-enablement (deal-cycle prep + collateral)
- `maiaedge-sales-docs/` - sales-docs (Order Forms / MSAs / POCs / NDAs)
- `maiaedge-events/` - event-intelligence + company-enrichment + segment-classification + import-processor + contact-discovery + edge-case-researcher (event-centric enrichment + contact mapping bundle)
- `linkedin-network-builder/` - icp-networking (LinkedIn networking automation)

**Standalone skill zips** (defined in `build.sh`): `account-brief`, `copy-strategist`, `sales-enablement`, `call-prep`, `competitive-intel`. The `copy-strategist` zip also bundles `context/copy-strategy/` as references.

**Enterprise Projects** (9 targets in `enterprise/`):
- `sales-outreach/` - outreach + enrichment skills, core/segments/outreach/copy-strategy context
- `founder-outreach/` - subset of sales-outreach (no sdr-pipeline/import-processor)
- `account-intelligence/` - RevOps + enrichment skills, all context categories
- `call-intelligence/` - call analysis + PMF signals + messaging alignment (the "listening" project)
- `revenue-reporting/` - pipeline analytics + forecast + CRO briefings (the "numbers" project)
- `crm-guardian/` - CRM maintenance orchestrator + RevOps skills, HubSpot/segments/enrichment context
- `sales-docs/` - legal docs (Order Forms/MSAs/POCs/NDAs) + sales enablement + call prep + competitive intel
- `branded-content/` - branded PDF studio (`branded-doc`) + segment + account-specific business cases; ships the full repo context
- `general-assistant/` - every skill + every context file

Each enterprise folder has a `manifest.md` (upload instructions for Claude.ai) and `upload/` (pre-built files from `build.sh`).

**System prompts for each Project** live in `enterprise-prompts/<project>.md` - paste these into Claude.ai Project Instructions.

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
| Cooper Kennedy | RevOps | - | 160267902 |
| Abilash Menon | CEO & Co-Founder | Strategic | 159974715 |
| Kyle Blackwell | Sales Engineering | - | 159701452 |
| Woody Acosta | Sales Support | - | 162281129 |
