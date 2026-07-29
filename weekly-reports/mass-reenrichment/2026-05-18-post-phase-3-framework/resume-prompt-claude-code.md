# Resume Claude Code Routines — Post-Sweep

Paste this entire prompt into Claude Code, run from the `maiaedge-ai` repo root.

---

You are resuming the Claude Code routines after the Account Tiering & Segmentation Overhaul project's Mass Re-Enrichment Sweep closed on 2026-05-19. All routines were paused at project kickoff. The sweep is done and the verification pass is closed. Time to turn everything back on.

## Your job

Check the enablement status of every Claude Code routine listed below. If any routine is disabled, re-enable it. If any routine is already enabled, leave it alone. Report exact state changes at the end.

## Routines that should be ENABLED on Claude Code (post-2026-04-30 platform split)

Per `CLAUDE.md` → "Scheduled Routines - Platform Split" → "Stay on Claude Code Routines" table:

| Routine | Trigger ID | Expected cron (UTC) | Local (ET) |
|---|---|---|---|
| Routine 3: Duplicate Accounts | `trig_01XTjFhegfVTCtSpZXEDY5Ce` | `0 7 * * *` | 2am daily |
| Routine 5: Contact Dedup | `trig_01Rw3KUsEXj2eoKKRKRCgGCZ` | `0 6 * * 0` | Sun 1am |
| Routine 6: Territory & Hygiene | `trig_01BmhnoyxFVrNXuqGcNnW6FV` | `0 6 * * *` | 1am daily |
| Routine 7: Monthly Sourcing | `trig_01WyVys2Jpi88JsoU5Pa4qve` | `0 14 1 * *` | 1st of month, 9am |
| Routine 8: Persona Fill | `trig_011jpGwhJQS8dJY3i7qU1StA` | `0 14 * * 5` | Fri 9am |
| Routine 9: Job Changes (Quarterly) | `trig_01Uw6RXKwGbjZfS2WaPeudKw` | `0 14 1 1,4,7,10 *` | Quarterly |

## Routines that should STAY DISABLED on Claude Code (migrated to Cowork 2026-04-30)

Do NOT re-enable these — they run on Cowork now and their Claude Code copies are intentionally off:

- R0 Import Validator
- R1 Fresh Enrichment
- R2 Stale Re-Enrichment
- R4 Flagged Consolidation
- Weekly Signal Scan
- Weekly Market News
- Daily Sales Activity Brief
- (and the new R-Tier-Audit + D7 — these were authored as Cowork scheduled tasks from day one)

If any of these are currently enabled on Claude Code, that's a bug — DISABLE them and flag in your report.

## Workflow

1. For each of the 6 routines above, call `RemoteTrigger.get` (or the equivalent) to read current `enabled` status, `cron`, and `prompt path`.
2. Build a current-state table.
3. For each routine where `enabled = false`: call `RemoteTrigger.update` with `enabled = true`. Keep cron unchanged.
4. For any Cowork-migrated routine that's accidentally enabled on Claude Code: call `RemoteTrigger.update` with `enabled = false`.
5. After all updates, re-read the 6 active triggers to verify the writes landed.
6. Report a final table showing:
   - Routine name
   - Trigger ID
   - `enabled` before → `enabled` after
   - Cron (confirm unchanged)
   - Action taken (no-op / enabled / disabled)

## Safety

- Do NOT change the cron string on any routine. Only flip `enabled`.
- Do NOT enable any routine NOT in the 6-routine table above.
- If you can't find a trigger by ID (returns 404), don't create it — flag it in the report so Cooper can investigate.
- If any trigger has a cron that differs from the expected cron in the table above, leave it but flag the mismatch.

## Reference

- `CLAUDE.md` → "Scheduled Routines - Platform Split" section (around line 196)
- Routine prompts live in `Claude routine prompts/` (canonical reference; the Cowork copies live in `cowork prompts/`)

Fire when ready. Report results back to Cooper as a single chat message — no Slack DM needed for this resume task.
