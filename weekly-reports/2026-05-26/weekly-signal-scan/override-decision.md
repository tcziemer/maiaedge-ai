# Weekly Signal Scan - Off-Cadence Override Decision

**Date:** Tuesday 2026-05-26 (09:26 ET / 08:26 CT)
**Decision authority:** Cooper Kennedy (RevOps, `U0A24D9RJLS`)
**Override target:** Preflight C in `routines/cowork/weekly-signal-scan/prompt.md`

## Background

Preflight C reads:

> Verify today is Monday in America/New_York timezone. If not, STOP with a report "not a Monday run - aborting." The cron can trigger on the wrong day during DST transitions.

Today is Tuesday 2026-05-26. The scheduled cron `0 18 * * 1` UTC would have fired Mon 2026-05-25 1pm CT, but Monday was Memorial Day (US Federal holiday). Reps were out; firing into a holiday window with the cascade-by-score DMs would have landed in cold inboxes. The Mon-cadence run was effectively skipped.

Last actual Signal Scan output in `weekly-reports/` is from Mon 2026-05-11 (`detected_signals.json`). The Mon 2026-05-18 folder only contains `calls/` from the Daily Sales Activity Brief - no signal-scan artifact, suggesting the 2026-05-18 run either did not fire or did not produce its output. That makes today's run the recovery for the past two skipped Mondays.

## Decision

**Override APPROVED.** Cooper instructed (via in-chat AskUserQuestion 2026-05-26 09:27 ET) to override Preflight C and fire the routine today.

The override:
- Treat today as the Memorial-Day-shifted Monday run.
- Log this decision in the Cooper run-report DM at Stage 7.
- Pre-flight A/B already verified in chat: HubSpot MCP available (Cooper owner 160267902), Apollo profile returns 10,864 / 12,110 monthly credits remaining (90% headroom).
- Apollo budget tracker `weekly-reports/apollo-budget.json` confirms ISO week 2026-W22 consumed = 0, weekly cap = 850, full 250-cr Weekly Signal Scan sub-cap headroom available.
- WoW baseline: read `weekly-reports/2026-05-11/detected_signals.json` (last actual Signal Scan run) for NEW/CARRIED tagging. Any account on the 2026-05-11 rep xlsx that fires again today is `CARRIED`; otherwise `NEW`.

## Execution model

The full Phase 3 pipeline (Stage 1 serial per-segment scrape across ~160 sources + Stage 3 R1 5-stage enrichment on net-new + Stage 5/5b HubSpot writes + Stage 6 rep xlsx + Stage 7 DMs + canvas append) does not fit in a single chat turn. Cooper acknowledged this in the override choice.

The run is being scheduled as a Cowork **one-time scheduled task** firing today, with the override note above prepended to the prompt so the scheduled-task runtime knows to bypass Preflight C and log the override in the Cooper run-report DM.

## Audit trail downstream

The scheduled-task runtime will produce:

- `weekly-reports/2026-05-26/weekly-signal-scan/cooper-run-report.md`
- `weekly-reports/2026-05-26/weekly-signal-scan/timlieto-east.xlsx`
- `weekly-reports/2026-05-26/weekly-signal-scan/kencunningham-west.xlsx`
- `weekly-reports/2026-05-26/weekly-signal-scan/timziemer-international.xlsx`
- `weekly-reports/2026-05-26/weekly-signal-scan/signals-audit.md`
- Slack DMs to Tim Lieto `U0A973L1HFF`, Ken Cunningham `U0AE1PGCB6C`, Cooper `U0A24D9RJLS` (Tim Z international cascade still routes to Cooper)
- Canvas `F0B0AFSB9LN` append: 1 row in Run log table + any new Tier 3 holds
- Apollo budget tracker updated post-run

This file is the chat-side artifact pinning the override decision.
