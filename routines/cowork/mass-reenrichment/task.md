# Cowork task metadata — Mass Re-Enrichment

| Field | Value |
|---|---|
| **Platform** | Cowork (manual trigger / Cooper-fired) |
| **Cron** | None — manual trigger only |
| **Enabled** | ✅ AVAILABLE (no schedule; Cooper kicks off when framework changes) |
| **MCP connections** | HubSpot, Apollo, Slack |
| **Apollo budget** | Drawn from monthly 6000 cap; per-sweep budget set in the prompt at run time |
| **Prompt file** | `routines/cowork/mass-reenrichment/prompt.md` |

## What it does

Cooper-triggered full sweep when the framework (tier-compute-spec / sub-segment-qualification / enrichment-protocols / Operating Principles in CLAUDE.md) changes meaningfully and existing records need re-validation under the new model. Same 5-stage workflow as R2 RE_ENRICH_FULL, applied across a defined record set. Recomputes both `account_tier` and `signal_heat` per Step 7.6 + 7.6b.

## How to trigger a run

1. Edit `prompt.md` in this folder if needed (e.g., bump SWEEP_NAME, batch size, candidate filter).
2. Open Cowork, start a new chat or use the saved task, paste the prompt + your run-specific parameters.
3. Cowork runs the sweep; results land in `weekly-reports/mass-reenrichment/<SWEEP_NAME>/`.

## How to update

This task lives as an on-demand prompt rather than a scheduled task. The file in this repo IS the source-of-truth document; whenever Cooper runs a new sweep, they paste the current content.
