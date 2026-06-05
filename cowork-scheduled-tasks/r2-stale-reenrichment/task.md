# Cowork task metadata — R2: Stale Re-Enrichment

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 16 * * 1-5` (UTC) = M-F 11:00 AM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Apollo, Slack |
| **Apollo budget** | Sub-cap 50 credits/run (against shared weekly 850 cap; see `routines/_shared/apollo-weekly-budget-spec.md`). Raised 30 → 50 on 2026-05-21 to support 120-day rotation at 5K active records. |
| **Prompt file** | `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` |

## What it does

Drains the stale-enrichment backlog (companies with `last_enriched_date` >120 days or blank with segment populated). Owns the 120-day re-enrichment rotation. RE_ENRICH_FULL recomputes `account_tier` AND `signal_heat` alongside the 8 enriched fields.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
