# Trigger metadata — Routine 9: Quarterly Job Changes

| Field | Value |
|---|---|
| **Trigger ID** | `trig_01Uw6RXKwGbjZfS2WaPeudKw` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 14 1 1,4,7,10 *` (UTC) = quarterly (Jan/Apr/Jul/Oct 1st), 9:00 AM ET |
| **Enabled** | ✅ ENABLED |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 9: Job Changes (Quarterly) |
| **MCP connections** | HubSpot, Apollo, Slack |
| **Apollo budget** | Spare-capacity at quarterly fire week (uses whatever's left in shared monthly cap) |
| **Prompt file** | `routines/claude-code/r9-quarterly-job-changes/prompt.md` |

## How to update the trigger after editing `prompt.md`

See `routines/claude-code/r3-duplicate-accounts/trigger.md` "How to update" — same procedure, just substitute the trigger ID.
