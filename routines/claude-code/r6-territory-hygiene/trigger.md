# Trigger metadata — Routine 6: Territory & Hygiene

| Field | Value |
|---|---|
| **Trigger ID** | `trig_01BmhnoyxFVrNXuqGcNnW6FV` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 6 * * *` (UTC) = daily 1:00 AM ET |
| **Enabled** | ✅ ENABLED (re-pushed with the 5-region territory-only prompt + re-enabled 2026-06-18) |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 6: Territory & Hygiene (daily 1am ET) |
| **MCP connections** | HubSpot, Apollo (state verification only), Slack |
| **Apollo budget** | Soft 5 credits/run, hard 20 credits/run (counted against shared monthly 6000 cap, no weekly tracker) |
| **Prompt file** | `routines/claude-code/r6-territory-hygiene/prompt.md` |

## Scope (rev. R7.0, 2026-06-04)

R6 is **territory-only**: validate HQ country/state, set/correct `hubspot_owner_id` per the 5-region model (first-touch gated), cascade owner to contacts. It does NOT compute tier or `signal_heat`, migrate enums, fill `account_tier`, or do contact hygiene — those were re-homed (tier/heat drift → R-Tier-Audit; enum/sub-segment/orphan → R1/R2/crm-hygiene). There is no longer an inlined `compute_tier` spec or Step 5.5 in this prompt.

## Step 1 specials (territory map)

R6's prompt **inlines the 5-region territory map** (state -> region -> owner + Europe/International rules + first-touch owner-write gate) in Step 1, for the same path-resolution reason. **When `context/hubspot/territory-model.md`, the `territory-manager` skill, or the keeper workflow's `REGION_OF` / `REGION_OWNER` (flow `4405143279`) change, the inlined Step 1 map MUST be re-synced and the trigger re-pushed.**

Territory map sync: 2026-06-17 (migrated the 2-region East/West map -> 5-region NE/SE/Central/West + Europe + International + Tier 1 SP + Unassigned; added the first-touch owner-write gate so R6 matches the keeper and never reverts a manual placement). **Trigger re-pushed + re-enabled 2026-06-18** — deployed copy now carries the 5-region territory-only prompt, verified byte-identical to `prompt.md`. Trigger is `enabled: true`; next run 2026-06-19 1:02 AM ET.

## How to update the trigger after editing `prompt.md`

See `routines/claude-code/r3-duplicate-accounts/trigger.md` "How to update" — same procedure, just substitute the trigger ID.
