# Cowork task metadata — Signal Scan: Fiber Operator

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 14 * * 1` (UTC) = Mon 9:30 AM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 35 credits/run (against shared 850/week cap) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-fiber/prompt.md` |

## What it does

Monday-morning signal scrape for the Fiber Operator segment only. Runs Stage 0-5c for ~22 documented sources (BEAD subgrants, SEC ABS prospectuses, vendor customer-win press, etc.). **No rep DMs, no canvas, no Cooper run report** — aggregator at 2:30pm CT handles those.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28).

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-fiber` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
