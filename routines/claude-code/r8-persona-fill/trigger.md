# Trigger metadata — Routine 8: Weekly Persona Gap Fill

| Field | Value |
|---|---|
| **Trigger ID** | `trig_011jpGwhJQS8dJY3i7qU1StA` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 14 * * 5` (UTC) = Fri 9:00 AM ET |
| **Enabled** | ✅ ENABLED |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 8: Persona Fill (Fri 9am ET) |
| **MCP connections** | HubSpot, Apollo, Slack |
| **Apollo budget** | Soft 175 credits/run, hard 250 credits/run (against shared monthly 6000 cap) |
| **Prompt file** | `routines/claude-code/r8-persona-fill/prompt.md` |

## Notes

- Day-gates internally to Fri ET.
- Step 1 sorts target accounts by `signal_heat` (`Hot`→`Warm`→`Cool`→`Cold` — Title Case per HubSpot enum) before `account_tier`, so Apollo budget hits highest-intent accounts first.

## How to update the trigger after editing `prompt.md`

See `routines/claude-code/r3-duplicate-accounts/trigger.md` "How to update" — same procedure, just substitute the trigger ID.
