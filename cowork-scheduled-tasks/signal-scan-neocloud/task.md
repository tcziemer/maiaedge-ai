# Cowork task metadata — Signal Scan: NeoCloud

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 15 * * 1` (UTC) = Mon 10:30 AM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 55 credits/run (highest among 6 segments — NeoCloud has the most NEW-account discovery volume) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-neocloud/prompt.md` |

## What it does

Monday-morning signal scrape for the NeoCloud segment only. Highest-velocity segment with broadest source coverage (~24 documented sources including IX member-list pages, NVIDIA partner pages, crypto-to-AI outlets, per-NeoCloud IR pages). Signal codes use `NC-` prefix to disambiguate from Network Operator's `NO-` prefix. **No rep DMs, no canvas, no Cooper run report** — aggregator at 2:30pm CT handles those.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28).

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-neocloud` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
