# Cowork task metadata — Daily Sales Activity Brief

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 18 * * 1-5` (local CT) = M-F 6:00 PM CT (moved from 4:00 PM CT 2026-06-03 per Cooper - reps log calls into the late afternoon; paired with the rolling prior-run->now window) |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 |
| **Prompt file** | `cowork-scheduled-tasks/daily-sales-activity-brief/prompt.md` |

## What it does

Renamed from "Daily Call Recap" 2026-05-05. Three identical exec DMs (Abilash, Tim Z, Cooper) covering Held / Set / Upcoming engagements + per-held-call exec snapshot + "What needs your attention." MEDDPICC backfill on prospect contacts runs as a silent side effect (Tier 1 fill / Tier 1 refresh / Tier 2 DRIFT / Tier 3 hold). Local markdown only — no git operations.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
