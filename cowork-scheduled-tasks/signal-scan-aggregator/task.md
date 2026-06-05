# Cowork task metadata — Signal Scan: Aggregator

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 19 * * 1` (UTC) = Mon 2:30 PM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 (read-only HubSpot + Slack + filesystem) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` |

## What it does

Aggregates the 6 per-segment scans into the rep-facing weekly briefing. Runs 1h 15m after the last per-segment scan (Enterprise at 1:00pm) — 3-hour cushion absorbing platform variance + ~3x runtime overrun on any per-segment scan.

Sequence:
1. **Stage 0** — preflight; verify 6 per-segment audit files exist (informational, NOT gating). Abort only if 3+ are missing.
2. **Stage 1** — read HubSpot for all company records with `last_signal_date = today (CT)` AND `hubspot_owner_id IS NOT NULL`. **HubSpot is source of truth** — missing per-segment audit files don't block rep DMs.
3. **Stage 2** — NEW vs CARRIED vs LIGHT vs CARRYOVER tagging from prior Monday's rep xlsx files.
4. **Stage 3** — territory split (Tim Lieto East / Ken West / Tim Z Int'l) + 50 cap + three-tier fill-down (Primary ≥12 → LIGHT 8-11 → Carryover News when natural pool < 25).
5. **Stage 4** — 3 rep DM cascade dispatch (Slack DMs + per-territory xlsx). Tim Z routes to Cooper per Phase 0 partial lift.
6. **Stage 5** — append ONE canvas Run log row to `F0B0AFSB9LN` summarizing the 6-segment + aggregator run.
7. **Stage 6** — write Cooper's cross-ICP run report to `weekly-reports/YYYY-MM-DD/signal-scan/cooper-run-report.md`.

**Graceful degradation:** the aggregator builds rep DMs from HubSpot, not from per-segment audit files. So a missing audit file degrades Cooper's cross-ICP report (gap noted), not rep delivery.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28) along with the 6 per-segment scan tasks.

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-aggregator` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
