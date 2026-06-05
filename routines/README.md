# Routines — master registry

Each routine lives in its own subfolder containing:
- **`prompt.md`** — the operational prompt (full payload).
- **`trigger.md`** *(Claude Code only)* — trigger ID, cron, environment ID, MCP connections, update procedure.
- **`task.md`** *(Cowork only)* — schedule, MCP connections, Apollo budget, update procedure.

## Active routines

### Claude Code (RemoteTrigger-fired, HubSpot-internal)

| Folder | Trigger ID | Cron (UTC) | Local | Apollo |
|---|---|---|---|---|
| [`claude-code/r3-duplicate-accounts/`](claude-code/r3-duplicate-accounts/) | `trig_01XTjFhegfVTCtSpZXEDY5Ce` | `0 7 * * *` | daily 2am ET | 0 |
| [`claude-code/r5-contact-dedup/`](claude-code/r5-contact-dedup/) | `trig_01Rw3KUsEXj2eoKKRKRCgGCZ` | `0 6 * * 0` | Sun 1am ET | 0 |
| [`claude-code/r6-territory-hygiene/`](claude-code/r6-territory-hygiene/) | `trig_01BmhnoyxFVrNXuqGcNnW6FV` | `0 6 * * *` | daily 1am ET | soft 5 / hard 20 |
| [`claude-code/r7-monthly-sourcing/`](claude-code/r7-monthly-sourcing/) | `trig_01WyVys2Jpi88JsoU5Pa4qve` | `0 14 1 * *` | 1st of month 9am ET | 0 |
| [`claude-code/r8-persona-fill/`](claude-code/r8-persona-fill/) | `trig_011jpGwhJQS8dJY3i7qU1StA` | `0 14 * * 5` | Fri 9am ET | soft 175 / hard 250 |
| [`claude-code/r9-quarterly-job-changes/`](claude-code/r9-quarterly-job-changes/) | `trig_01Uw6RXKwGbjZfS2WaPeudKw` | `0 14 1 1,4,7,10 *` | Quarterly 9am ET | spare-capacity |

All on environment `env_018AmYCxSHNPrHk4q3ofk9hm`. The prompt content is stored inline in the trigger; updating `prompt.md` on disk does NOT automatically push to the live trigger — see each `trigger.md` for the `RemoteTrigger.update` recipe.

### Cowork scheduled tasks (cron-fired, web/Apollo-intensive)

Cowork scheduled tasks now live in the sibling top-level [`cowork-scheduled-tasks/`](../cowork-scheduled-tasks/) folder (next to `routines/`). They are *not* routines — they're cron-fired prompts with no persistent state across runs. Kept separate so the distinction between scheduled vs. manual Cowork work, and Cowork vs. Claude Code, is unambiguous.

| Folder | Schedule | Apollo |
|---|---|---|
| [`cowork-scheduled-tasks/r0-import-validator/`](../cowork-scheduled-tasks/r0-import-validator/) | M-F 9am CT | 0 |
| [`cowork-scheduled-tasks/r1-fresh-enrichment/`](../cowork-scheduled-tasks/r1-fresh-enrichment/) | M-F 10am CT | sub-cap 30/run |
| [`cowork-scheduled-tasks/r2-stale-reenrichment/`](../cowork-scheduled-tasks/r2-stale-reenrichment/) | M-F 11am CT | sub-cap 50/run |
| [`cowork-scheduled-tasks/r4-flagged-consolidation/`](../cowork-scheduled-tasks/r4-flagged-consolidation/) | M-F 12pm CT | 0 |
| [`cowork-scheduled-tasks/r-tier-audit/`](../cowork-scheduled-tasks/r-tier-audit/) | M-F 3pm CT | 0 |
| [`cowork-scheduled-tasks/d7-edge-case-resolution/`](../cowork-scheduled-tasks/d7-edge-case-resolution/) | Wed 9am CT | 0 |
| [`cowork-scheduled-tasks/signal-scan-colo/`](../cowork-scheduled-tasks/signal-scan-colo/) | Mon 8:30am CT | sub-cap 35/run |
| [`cowork-scheduled-tasks/signal-scan-fiber/`](../cowork-scheduled-tasks/signal-scan-fiber/) | Mon 9:30am CT | sub-cap 35/run |
| [`cowork-scheduled-tasks/signal-scan-neocloud/`](../cowork-scheduled-tasks/signal-scan-neocloud/) | Mon 10:30am CT | sub-cap 55/run |
| [`cowork-scheduled-tasks/signal-scan-networkop/`](../cowork-scheduled-tasks/signal-scan-networkop/) | Mon 11:30am CT | sub-cap 50/run |
| [`cowork-scheduled-tasks/signal-scan-msp/`](../cowork-scheduled-tasks/signal-scan-msp/) | Mon 12:30pm CT | sub-cap 20/run |
| [`cowork-scheduled-tasks/signal-scan-enterprise/`](../cowork-scheduled-tasks/signal-scan-enterprise/) | Mon 1:00pm CT | sub-cap 55/run |
| [`cowork-scheduled-tasks/signal-scan-aggregator/`](../cowork-scheduled-tasks/signal-scan-aggregator/) | Mon 2:30pm CT | 0 |
| [`cowork-scheduled-tasks/weekly-market-news/`](../cowork-scheduled-tasks/weekly-market-news/) | Fri 1pm CT | 0 |
| [`cowork-scheduled-tasks/daily-sales-activity-brief/`](../cowork-scheduled-tasks/daily-sales-activity-brief/) | M-F 4pm CT | 0 |

Cowork prompts live in Cowork's scheduled-task UI. Updating `prompt.md` on disk does NOT automatically sync — you must paste the new content into the scheduled task. The file is the source of truth; Cowork's config is the live runtime copy.

### Cowork manual-trigger tasks (Cooper-fired, no cron)

| Folder | Cadence | Apollo |
|---|---|---|
| [`cowork/mass-reenrichment/`](cowork/mass-reenrichment/) | On-demand (framework changes) | draws from monthly cap |
| [`cowork/flagged-for-deletion-audit/`](cowork/flagged-for-deletion-audit/) | Biweekly Cooper manual | 0 |

## Shared assets

- [`_shared/apollo-weekly-budget-spec.md`](_shared/apollo-weekly-budget-spec.md) — the 850 credits/week shared cap, per-routine sub-caps, tracker-file format, pre-flight + post-run logic. Referenced by R1, R2, R8, Weekly Signal Scan.

## Outreach helpers (moved to `cowork-project-instructions/` 2026-06-02)

Both list-driven outreach prompts moved out of `routines/outreach-helpers/` and now live as Cowork project instructions at the repo root. Each reconciles with the `cold-email` / `linkedin-outreach` / `sdr-pipeline` skills and carries a Research Quality gate (brief validation, fresh-signal-as-reason-to-meet at ≤90d event date, no stale signals, no wrong facts).

- [`cowork-project-instructions/Cold-Outreach-Project-Instructions.md`](../cowork-project-instructions/Cold-Outreach-Project-Instructions.md)
- [`cowork-project-instructions/Tradeshow-Outreach-Project-Instructions.md`](../cowork-project-instructions/Tradeshow-Outreach-Project-Instructions.md)

## Archive — disabled / superseded Claude Code prompts

[`archive/claude-code-disabled/`](archive/claude-code-disabled/) holds the original Claude Code routine prompts that were disabled on 2026-04-30 when their workload moved to Cowork (the egress-proxy block on Claude Code's CCR runtime broke web-scraping for R0/R1/R2/R4 + the three weekly cron prompts). Kept as historical reference per CLAUDE.md.

Specifically:
- `r0-import-validator.md`, `r1-fresh-enrichment.md`, `r2-stale-reenrichment.md`, `r4-flagged-consolidation.md` → superseded by the matching `cowork-scheduled-tasks/r*/` tasks.
- `weekly-signal-scan.md`, `weekly-market-news.md`, `weekly-call-recap.md` → superseded by the matching Cowork scheduled tasks (Daily Sales Activity Brief replaced Weekly Call Recap, renamed 2026-05-05).
- `crm-guardian-orchestrator.md` → original CRM Guardian top-level orchestrator prompt; routines are independent now.

**Do NOT re-enable** the disabled triggers in claude.ai without Cooper's explicit direction.
