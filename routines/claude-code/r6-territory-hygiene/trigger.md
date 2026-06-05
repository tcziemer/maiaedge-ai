# Trigger metadata — Routine 6: Territory & Hygiene

| Field | Value |
|---|---|
| **Trigger ID** | `trig_01BmhnoyxFVrNXuqGcNnW6FV` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 6 * * *` (UTC) = daily 1:00 AM ET |
| **Enabled** | ✅ ENABLED |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 6: Territory & Hygiene (daily 1am ET) |
| **MCP connections** | HubSpot, Apollo (state verification only), Slack |
| **Apollo budget** | Soft 5 credits/run, hard 20 credits/run (counted against shared monthly 6000 cap, no weekly tracker) |
| **Prompt file** | `routines/claude-code/r6-territory-hygiene/prompt.md` |

## Step 5.5 specials

R6's prompt **inlines** the canonical `compute_tier` spec (§1-§10) and the `compute_signal_heat` algorithm in Step 5.5 because the Claude Code runtime cannot resolve repo paths. **When `context/account-tiering/tier-compute-spec.md` changes, the inlined section in `prompt.md` MUST be re-synced** and the trigger re-pushed.

Latest sync: 2026-05-20 (added `signal_heat` recompute alongside tier in Step 5.5).

## How to update the trigger after editing `prompt.md`

See `routines/claude-code/r3-duplicate-accounts/trigger.md` "How to update" — same procedure, just substitute the trigger ID.
