# MaiaEdge Routines -- Executive Summary

Claude Code now supports Routines: autonomous tasks that run on a schedule, fire from GitHub events, or trigger via API. No cron jobs, no infrastructure to manage. We configure a prompt and a trigger, and Claude Code executes it against our repo and connected tools (HubSpot, Apollo, GitHub) on autopilot.

Below are the 8 routines we're planning to deploy against our existing skill library. Every skill referenced here is already built and tested -- Routines just makes them run without someone remembering to invoke them.

---

## Scheduled Routines (5)

### 1. CRM Guardian -- Nightly at 2 AM ET

Runs 6 maintenance jobs against HubSpot every night: fills missing fields, enriches new accounts, re-enriches stale ones, validates territory assignments, identifies persona gaps at active accounts, and detects key contact job changes. Uses a 3-tier safety system -- low-risk fixes happen automatically, medium-risk fixes are applied but flagged for Cooper's review, and high-risk changes (like merging duplicates or modifying accounts with open deals) are held for human approval. This is the single highest-impact routine because it prevents data rot from compounding day over day.

### 2. Pipeline Monday Brief -- Weekly, Monday at 7 AM ET

Generates the 3-column conversion board that tracks every account through the full revenue lifecycle: accounts converting to POC, POCs converting to purchase orders, and initial orders expanding. Each account shows the rep owner, deal stage, days in stage, last activity date, POC health score (for Column 2), and a recommended next action. The brief lands before Monday standup so Tim Z, Tim L, and Ken walk in knowing exactly what needs attention -- no one has to pull it live.

### 3. Stale Deal Watchdog -- Nightly at 6 AM ET

Scans every open deal for staleness signals: time in current stage exceeding thresholds (14 days early-stage, 30 days mid-pipeline, 45 days late-stage), no activity in 14+ days, close dates that have already passed, and MEDDPICC qualification gaps on deals past discovery. Only alerts on deals that crossed a new threshold in the last 24 hours so reps don't get alert fatigue. The goal is to catch deals that are quietly dying before they go fully cold -- a deal with no activity for 3 weeks is salvageable, but 6 weeks is usually not.

### 4. Weekly Call Digest -- Friday at 4 PM ET

Pulls every call logged in HubSpot over the past 7 days, extracts the AI-generated summaries, and classifies each call against our 21-use-case taxonomy. The output is a formatted HTML report showing: which use cases came up most often (and with real quotes), recurring pain points by segment, every competitive mention (who was named, in what context), and rep activity stats. This turns raw call data into systematic market intelligence -- instead of insights living in individual reps' heads, the whole team sees what's resonating and what's blocking.

### 5. Territory Drift Check -- Weekly, Sunday at 9 PM ET

Audits all company records created or modified in the past week to verify territory assignments match the HQ state-to-owner mapping (Tim Lieto = East 30 states, Ken Cunningham = West 20 states + DC, Tim Ziemer = International). Also catches US companies with blank state fields and accounts still sitting under Cooper's placeholder ownership that need routing. This is an audit-only routine -- it produces a correction list for Cooper to review rather than auto-fixing, since territory exceptions sometimes exist for strategic reasons.

---

## Webhook Routines -- GitHub (2)

### 6. Repo Build Validator -- On PR to main

When anyone opens a pull request against the main branch, this routine runs the build script and verifies that all 9 plugins, 5 standalone skill zips, and 7 enterprise project uploads assemble cleanly. It checks that the skill counts inside each plugin zip match the manifest declarations and that no enterprise upload folder is empty. If anything breaks, it comments directly on the PR with the specific failure. This is an insurance policy -- as the knowledge base grows past 25 skills and 49 context files, a bad merge in one file can silently break downstream builds.

### 7. Context Drift Detector -- On PR touching context/

When a PR modifies files in the context/ directory (territory model, HubSpot schemas, segment cheatsheets, etc.), this routine cross-references every skill that references the changed file and checks whether any hardcoded values in those skills are now stale. For example, if someone updates territory-model.md to reassign a state, the territory-manager skill's hardcoded state list would need updating too. Most skills read context dynamically at runtime so drift is rare, but catching the exceptions automatically prevents subtle bugs.

---

## API Routines -- On-Demand (1)

### 8. Enrichment Chain -- POST to trigger

After running a company-enrichment batch, today you manually kick off import-processor to transform the output into HubSpot format, then manually run edge-case-researcher on the flagged accounts. This routine chains those two steps automatically: POST the enrichment output file path, and it runs import processing (value transforms, qualified/excluded separation), then deep-dive research on edge cases, then merges recovered accounts back into the final qualified import file. Eliminates the manual handoff between three skills and produces a single HubSpot-ready file.

---

## Implementation Priority

| Priority | Routine | Effort | Impact |
|----------|---------|--------|--------|
| 1 | CRM Guardian (nightly) | Low -- skill fully built | Very High |
| 2 | Stale Deal Watchdog (nightly) | Low -- simple queries | High |
| 3 | Pipeline Monday Brief (weekly) | Low -- skill fully built | High |
| 4 | Territory Drift Check (weekly) | Very Low -- simple audit | Medium |
| 5 | Weekly Call Digest (Friday) | Medium -- aggregation + formatting | High |
| 6 | Repo Build Validator (webhook) | Low -- shell validation | Medium |
| 7 | Context Drift Detector (webhook) | Medium -- cross-referencing | Medium |
| 8 | Enrichment Chain (API) | Medium -- multi-step orchestration | Medium |

Typical weekday usage: 2-5 routine runs. Well within the 15/day limit on a Max plan.

---

*Full implementation prompts, connector requirements, and setup instructions are in [ROUTINES-BLUEPRINT.md](./ROUTINES-BLUEPRINT.md).*
