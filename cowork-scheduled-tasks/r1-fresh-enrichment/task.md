# Cowork task metadata — R1: Fresh Enrichment

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 15 * * 1-5` (UTC) = M-F 10:00 AM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Apollo, Slack |
| **Apollo budget** | Sub-cap 30 credits/run (against shared weekly 850 cap + monthly 6000 cap; see `routines/_shared/apollo-weekly-budget-spec.md`). Reduced 50 → 30 on 2026-05-21 to free 100 cr/wk for R2. |
| **Prompt file** | `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` |

## What it does

Drains the daily candidate pool (dynamic 100/125/150 records/run depending on backlog). Three paths:
- **Path α** — full enrichment for LIKELY_ICP records (Apollo-bound). New accounts default `signal_heat = Cold`.
- **Path β** — re-research for Filter Groups C + D + B-without-ICP-keywords (Apollo-free).
- **Path γ** — eviction-decision for LIKELY_NON_ICP / LIKELY_JUNK (Apollo-free).

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
