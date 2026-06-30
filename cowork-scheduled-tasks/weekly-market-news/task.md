# Cowork task metadata — Weekly Market News

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 18 * * 5` (UTC) = Fri 1:00 PM CT |
| **Enabled** | ✅ ENABLED (Phase 0 = Cooper-only delivery) |
| **MCP connections** | Slack, web_fetch, web_search |
| **Apollo budget** | 0 (no HubSpot, no Apollo) |
| **Prompt file** | `cowork-scheduled-tasks/weekly-market-news/prompt.md` |

## What it does

Friday-morning market awareness digest covering all 6 ICPs. Pure awareness (no HubSpot reads/writes, no scoring). Top 3 stories per ICP + Cross-ICP Themes + Exec Moves callout. Cooper validates voice + source coverage + MaiaEdge-angle quality for 2-4 runs, then flips to rep-direct routing.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
