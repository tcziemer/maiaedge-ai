# Trigger metadata — Routine 7: Monthly New Account Sourcing

| Field | Value |
|---|---|
| **Trigger ID** | `trig_01WyVys2Jpi88JsoU5Pa4qve` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 14 1 * *` (UTC) = 1st of month, 9:00 AM ET |
| **Enabled** | ✅ ENABLED |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 7: Monthly Sourcing (1st of month 9am ET) |
| **MCP connections** | HubSpot (read-only), Slack |
| **Apollo budget** | 0 (does NOT use Apollo — web research only) |
| **Prompt file** | `routines/claude-code/r7-monthly-sourcing/prompt.md` |

## Notes

- Day-gates internally: exits cleanly with a one-line DM if today's ET date isn't the 1st (guards against DST / scheduler bugs).
- Read-only — surfaces candidates to a Slack Tier 3 review queue. Cooper creates the HubSpot records manually.
- Candidates carry recommended `signal_heat = Cold` default (sourced records have no signal history yet).

## How to update the trigger after editing `prompt.md`

See `routines/claude-code/r3-duplicate-accounts/trigger.md` "How to update" — same procedure, just substitute the trigger ID.
