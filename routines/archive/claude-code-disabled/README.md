# Archive — disabled Claude Code routine prompts

These are the **disabled / superseded** Claude Code (CCR) routine prompts. They were the original CRM Guardian sub-routines authored when the entire system ran on Claude Code. On 2026-04-30 the web-fetch / Apollo-intensive routines moved to Cowork (Claude Code's CCR runtime has an egress proxy that returns HTTP 403 `host_not_allowed` on news/source domains, which crippled Stage 1 scraping for R0/R1/R2/R4 + the three weekly cron prompts). The original CC triggers were disabled (`enabled: false` via `RemoteTrigger.update`); the files below are kept as **canonical historical reference**.

**Do NOT re-enable without Cooper's explicit direction.**

For the **active** routines see [`routines/README.md`](../../README.md).

## Files in this archive

| Archived file | Live replacement |
|---|---|
| [r0-import-validator.md](r0-import-validator.md) | [../../../cowork-scheduled-tasks/r0-import-validator/](../../../cowork-scheduled-tasks/r0-import-validator/) |
| [r1-fresh-enrichment.md](r1-fresh-enrichment.md) | [../../../cowork-scheduled-tasks/r1-fresh-enrichment/](../../../cowork-scheduled-tasks/r1-fresh-enrichment/) |
| [r2-stale-reenrichment.md](r2-stale-reenrichment.md) | [../../../cowork-scheduled-tasks/r2-stale-reenrichment/](../../../cowork-scheduled-tasks/r2-stale-reenrichment/) |
| [r4-flagged-consolidation.md](r4-flagged-consolidation.md) | [../../../cowork-scheduled-tasks/r4-flagged-consolidation/](../../../cowork-scheduled-tasks/r4-flagged-consolidation/) |
| [weekly-signal-scan.md](weekly-signal-scan.md) | [../../../cowork-scheduled-tasks/weekly-signal-scan/](../../../cowork-scheduled-tasks/weekly-signal-scan/) |
| [weekly-market-news.md](weekly-market-news.md) | [../../../cowork-scheduled-tasks/weekly-market-news/](../../../cowork-scheduled-tasks/weekly-market-news/) |
| [weekly-call-recap.md](weekly-call-recap.md) | [../../../cowork-scheduled-tasks/daily-sales-activity-brief/](../../../cowork-scheduled-tasks/daily-sales-activity-brief/) (renamed + reframed 2026-05-05) |
| [crm-guardian-orchestrator.md](crm-guardian-orchestrator.md) | n/a — original consolidated CRM Guardian prompt that the 10-routine split was derived from; reference-only |

## Inlining pattern (still canonical for the active R6/R7/R8/R9 prompts)

Claude Code routine runtime **cannot resolve repo paths at fire time**. The runtime has no checkout of the repo, only the trigger's stored prompt body. Therefore every routine prompt **must inline all operational rules it needs to execute** — never `read context/foo.md` at runtime.

When a spec file (e.g., `context/account-tiering/tier-compute-spec.md`) changes, the corresponding routine prompts must be **re-inlined and re-pushed** via `RemoteTrigger.update`. Updating only the repo file is documentation, not deployment. See [`routines/claude-code/r6-territory-hygiene/prompt.md`](../../claude-code/r6-territory-hygiene/prompt.md) §"Inlined Tier Compute Spec" for the canonical inlining pattern (last refreshed 2026-05-20 with `signal_heat` added to Step 5.5).

## Updating a live routine

See each active routine's sidecar `trigger.md` for the `RemoteTrigger.update` recipe (trigger ID, environment, body shape).
