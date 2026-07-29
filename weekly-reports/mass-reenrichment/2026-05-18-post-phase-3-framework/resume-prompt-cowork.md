# Resume Cowork Scheduled Tasks — Post-Sweep

Paste this entire prompt into a new chat inside the **CRM Guardian** Cowork project (the project that holds all the scheduled tasks).

---

You are resuming the Cowork scheduled tasks after the Account Tiering & Segmentation Overhaul project's Mass Re-Enrichment Sweep closed on 2026-05-19. All Cowork scheduled tasks were paused at project kickoff. The sweep + verification pass are done. Time to turn everything back on and confirm Apollo budget enforcement is restored.

## Your job

Use `mcp__scheduled-tasks__list_scheduled_tasks` to inventory every scheduled task in this Cowork project. For each task that should be ENABLED but is currently disabled, re-enable it via `mcp__scheduled-tasks__update_scheduled_task`. Then patch the Apollo budget tracker to restore enforcement. Report final state.

## Scheduled tasks that should be ENABLED in CRM Guardian Cowork

Per `CLAUDE.md` → "Scheduled Routines - Platform Split" → "Run on Cowork" table:

| Task | Prompt file (in repo) | Expected schedule (local CT) | Cron |
|---|---|---|---|
| Import Validator (R0) | `cowork prompts/Import_Validator_Prompt.md` | 9:00 AM M-F | `0 9 * * 1-5` |
| Fresh Enrichment (R1) | `cowork prompts/Fresh_Enrichment_Prompt.md` | 10:00 AM M-F | `0 10 * * 1-5` |
| Stale Re-Enrichment (R2) | `cowork prompts/Stale_Re_Enrichment_Prompt.md` | 11:00 AM M-F | `0 11 * * 1-5` |
| Flagged Consolidation (R4) | `cowork prompts/Flagged_Consolidation_Prompt.md` | 12:00 PM M-F | `0 12 * * 1-5` |
| Weekly Signal Scan | `cowork prompts/Weekly_Signal_Scan_Prompt.md` | 1:00 PM Monday | `0 13 * * 1` |
| Weekly Market News | `cowork prompts/Weekly_Market_News_Prompt.md` | 1:00 PM Friday | `0 13 * * 5` |
| Daily Sales Activity Brief | `cowork prompts/Daily_Sales_Activity_Brief_Prompt.md` | 4:00 PM M-F | `0 16 * * 1-5` |
| R-Tier-Audit (NEW 2026-05-14) | `cowork prompts/Tier_Audit_Prompt.md` | 3:00 PM Friday | `0 15 * * 5` |
| D7 Edge Case Resolution (NEW 2026-05-14) | `cowork prompts/Edge_Case_Resolution_Prompt.md` | 9:00 AM Wed (suggested) | `0 9 * * 3` |

**9 tasks total.** Cron strings above use local CT (Cooper's machine). If `mcp__scheduled-tasks__list_scheduled_tasks` returns them in UTC, expect a +5 or +6 hour offset depending on DST.

## Workflow

1. Call `mcp__scheduled-tasks__list_scheduled_tasks` to inventory everything in this Cowork project.
2. Build a current-state table — task name, enabled status, cron, prompt path.
3. For each task in the 9-task table above where `enabled = false` (or missing): call `mcp__scheduled-tasks__update_scheduled_task` to set `enabled = true`. Keep cron + prompt path unchanged.
4. If R-Tier-Audit or D7 don't exist yet (they were added 2026-05-14), STOP and ask Cooper whether to create them — don't assume their existence.
5. Re-read the list to verify writes landed.
6. Patch the Apollo budget tracker to re-enable enforcement:
   - Read `weekly-reports/apollo-budget.json` (path on Cooper's mounted folder, accessible via Bash)
   - If a field like `enforcement` / `paused` / `disabled` exists, flip it to enabled
   - If no such field, append a note that enforcement is restored as of 2026-05-19
   - The sweep ran with `APOLLO_ENFORCEMENT = "disabled"` per its prompt parameter; that parameter only lived in the sweep prompt and doesn't persist in the tracker, but verify the tracker isn't carrying a stale "paused" state from any prior coordination
7. Report a final table to Cooper as a single chat message showing per-task:
   - Task name
   - Cron (confirm unchanged)
   - `enabled` before → `enabled` after
   - Action taken (no-op / enabled / created-and-flagged)

## Safety

- Do NOT change cron strings — only flip `enabled` to true.
- Do NOT enable any task NOT in the 9-task table above. If you find extra scheduled tasks (e.g. left over from old routines), flag them but don't touch them.
- Do NOT trigger any of these tasks to run immediately on enable — that risks a double-fire if today's scheduled window already passed. Just enable; let the next cron tick handle it.
- Concurrency check: confirm Cooper has no other active sweeps or migrations running before re-enabling. If anything looks like it's still mid-batch, pause and ask.

## After re-enabling

Tell Cooper:
1. Which tasks were already enabled (no-op)
2. Which tasks were re-enabled this run
3. Apollo budget tracker state (enforcement restored / already enforced / N/A)
4. Any anomalies (missing tasks, cron mismatches, extras to investigate)

## Reference

- `CLAUDE.md` → "Scheduled Routines - Platform Split" section
- `cowork prompts/Apollo_Weekly_Budget_Spec.md` → budget tracker schema
- All Cowork prompt files live in `cowork prompts/` on the mounted maiaedge-ai folder

Fire when ready. No Slack DM needed — report inline in this chat.
