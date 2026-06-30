# Cowork task metadata — Weekly Signal Scan

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 18 * * 1` (UTC) = Mon 1:00 PM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 250 credits/run (against shared weekly 850 cap) |
| **Prompt file** | `cowork-scheduled-tasks/weekly-signal-scan/prompt.md` |
| **Helpers** | `cowork-scheduled-tasks/weekly-signal-scan/helpers/` (Stage 1 sub-agent template + source-coverage / volume gate scripts) |

## What it does

Monday-morning signal scrape across all 6 ICPs (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise). 14-day rolling detection window, score floor 8. Stage 5b writes `last_signal_score` / `last_signal_date` / `signal_count_last_30d` + recomputes `account_tier` AND `signal_heat`. Delivers 3 rep DMs (Tim Lieto direct, Ken direct, Tim Z still routed to Cooper) with heat distribution + cascade-by-score.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
