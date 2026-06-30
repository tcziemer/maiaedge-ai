# Cowork task metadata — R-Tier-Audit: Daily Tier + Heat Drift Correction

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 20 * * 1-5` (UTC) = M-F 3:00 PM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 (pure HubSpot read/compute/write) |
| **Prompt file** | `cowork-scheduled-tasks/r-tier-audit/prompt.md` |
| **Last cadence change** | 2026-05-21: weekly Fri → daily M-F per Cooper, 10% circuit breaker (was 5%) |

## What it does

Daily drift correction sweep over all active ICP records. Recomputes `account_tier` AND `signal_heat` per `context/account-tiering/tier-compute-spec.md`. 10% circuit breaker pauses on mass-change. Heat writes proceed regardless of `hs_is_target_account` (heat is not frozen).

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
