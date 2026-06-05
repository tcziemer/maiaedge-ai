# Cowork task metadata — Signal Scan: Data Center Colo Provider

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 13 * * 1` (UTC) = Mon 8:30 AM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 35 credits/run (against shared 850/week cap; see `routines/_shared/apollo-weekly-budget-spec.md`) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-colo/prompt.md` |

## What it does

Monday-morning signal scrape for the Colo segment only. Runs Stage 0-5c (preflight, source coverage, match, NEW-account creation, score, QA gate, HubSpot narrative write, structured signal field + tier/heat recompute, on-disk audit). **No rep DMs, no canvas Run log, no Cooper run report** — the aggregator at 2:30pm CT handles all three from the HubSpot writes.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28) to give the segment its own context budget, enforce the Source Coverage Mandate on this segment's ~16 documented sources, and run independently of the other 5 segments.

## How to update

This prompt runs as a Cowork scheduled task. To update:

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-colo` with the updated `prompt.md` text.
4. The file on disk is the source of truth; Cowork UI is the live runtime copy.
