# New-Computer Setup Driver — CRM Guardian Cowork fleet

Paste the block below into a **fresh chat inside the CRM Guardian project in Cowork on the new computer**, with the `maiaedge-ai` repo folder attached as **Context**. It drives the agent to register + activate every scheduled task from the repo (or, if Cowork requires UI creation, to hand you a complete paste-ready pack per task).

> Prereq: the `maiaedge-ai` repo is cloned/pulled on the new machine and attached as Context. HubSpot + Apollo + Slack MCP should be connected in that machine's Cowork (the agent will flag any that aren't).

---

You are setting up the MaiaEdge **CRM Guardian** scheduled-task fleet on this machine's Cowork. The attached `maiaedge-ai` repo folder is the single source of truth — read from it, do not invent tasks, schedules, or prompt text.

GOAL: register (or update) and ACTIVATE every scheduled task defined under `cowork-scheduled-tasks/`, each with the correct schedule, MCP connections, and prompt content, and set the project Instructions.

STEP 1 — Project Instructions
Read `cowork-scheduled-tasks/CRM-Guardian-Project-Instructions.md`. That is this project's Instructions. If you can set project instructions in this session, set them to that file's content verbatim; otherwise output the full content in a clearly-marked block for me to paste into the project's Instructions field.

STEP 2 — Enumerate the task list
List every subfolder of `cowork-scheduled-tasks/` that contains a `prompt.md`. Those folders ARE the authoritative task list. For each, read its `task.md` (cron + the local-CT time, MCP connections, Apollo budget) and its `prompt.md` (the payload to run). Skip `CRM-Guardian-Project-Instructions.md` and this `NEW-COMPUTER-SETUP-PROMPT.md` — they are not tasks.

STEP 3 — Determine your capability, then act
First determine whether you can programmatically create/update Cowork scheduled tasks in this session.
- If YES: for each task folder, create or update a scheduled task with — name = the task's display name, schedule = the **local-CT time** from its `task.md`, prompt = the full `prompt.md` content, MCP connections = those listed in its `task.md`, status = **ACTIVE**.
- If NO (Cowork requires the UI): for each task, output a SETUP CARD — `Task name | Schedule (local CT) | MCP connections` followed by the full `prompt.md` content in a fenced block — and tell me to create each via the "+ Scheduled" button. Order them by fire time.

STEP 4 — MCP connections
Each `task.md` lists its MCPs (HubSpot / Apollo / Slack). They must be authenticated in THIS machine's Cowork. Flag any task whose MCPs are not connected.

STEP 5 — Verify + report
Output one table: `Task | Schedule (local CT) | MCPs | Status (Active / Needs-UI / MCP-missing)`. Confirm the row count equals the number of task folders you found.

RULES
- Read schedules from each `task.md` — do not guess. Use the local-CT time shown there.
- Do NOT recreate R3 / R5 / R6 / R7 / R8 / R9 — those run as Claude Code cloud triggers, not Cowork tasks. They are NOT in `cowork-scheduled-tasks/`.
- The old monolithic "Weekly Signal Scan" is RETIRED — it is not in the folder; if a paused "Weekly signal scan" task already exists in this Cowork, LEAVE IT PAUSED.
- The two manual-trigger tasks in `routines/cowork/` (flagged-for-deletion-audit, mass-reenrichment) are fired on demand, NOT scheduled — do not put them on a cron.
- Do NOT fire any task now — only register/activate it on its schedule.
- If a `task.md` is missing or unreadable, fall back to the task table in `CRM-Guardian-Project-Instructions.md` and say so.

---

## Expected task list (17 scheduled, all local CT)

| Task | Schedule | Prompt |
|---|---|---|
| R0 Import Validator | 9:00 AM M-F | `r0-import-validator/prompt.md` |
| R1 Fresh Enrichment | 10:00 AM M-F | `r1-fresh-enrichment/prompt.md` |
| R2 Stale Re-Enrichment | 11:00 AM M-F | `r2-stale-reenrichment/prompt.md` |
| R4 Flagged Consolidation | 12:00 PM M-F | `r4-flagged-consolidation/prompt.md` |
| R10 Field Completeness Sweep | 1:30 PM M-F | `r10-completeness-sweep/prompt.md` |
| Signal Scan: Colo | Mon 8:30 AM | `signal-scan-colo/prompt.md` |
| Signal Scan: Fiber | Mon 9:30 AM | `signal-scan-fiber/prompt.md` |
| Signal Scan: NeoCloud | Mon 10:30 AM | `signal-scan-neocloud/prompt.md` |
| Signal Scan: Network Op | Mon 11:30 AM | `signal-scan-networkop/prompt.md` |
| Signal Scan: MSP/Aggregator | Mon 12:30 PM | `signal-scan-msp/prompt.md` |
| Signal Scan: Enterprise | Mon 1:00 PM | `signal-scan-enterprise/prompt.md` |
| Signal Scan: Aggregator | Mon 2:30 PM | `signal-scan-aggregator/prompt.md` |
| R-Tier-Audit | 3:00 PM M-F | `r-tier-audit/prompt.md` |
| CRM Ops Daily Digest | 4:45 PM M-F | `crm-ops-daily-digest/prompt.md` |
| Daily Sales Activity Brief | 6:00 PM M-F | `daily-sales-activity-brief/prompt.md` |
| D7 Edge Case Resolution | Wed 9:00 AM | `d7-edge-case-resolution/prompt.md` |
| Weekly Market News | Fri 1:00 PM | `weekly-market-news/prompt.md` |

> This table is a cross-check for the agent's folder scan; `task.md` in each folder is authoritative if they ever disagree. Reminder: **disable these on the OLD machine** if it still runs them, so both don't fire against the same HubSpot.
