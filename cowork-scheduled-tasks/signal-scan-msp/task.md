# Cowork task metadata — Signal Scan: MSP/Aggregator

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 17 * * 1` (UTC) = Mon 12:30 PM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 20 credits/run (lowest — MSP is thinnest segment for NEW-account discovery) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-msp/prompt.md` |

## What it does

Monday-morning signal scrape for the MSP/Aggregator segment (telecom/network aggregators ONLY — NOT IT MSPs). Lowest-velocity segment; thinnest source registry (~20 documented sources including Channel Futures, ChannelE2E, TSD press pages, ScanSource/TD SYNNEX investor pages, Megaport/Console Connect partner announcements).

Critical IT MSP Test runs at every detection: helpdesk/cybersecurity MSPs are EXCLUDED.

48-hour priority signals (M-A1, M-A2, M-A4, M-A5, M-A6, M-A7, M-B4, M-C5) get tagged `priority: 48h` for the aggregator to surface at the top of rep DM cascade.

**No rep DMs, no canvas, no Cooper run report** — aggregator at 2:30pm CT handles those.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28).

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-msp` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
