# Cowork task metadata — R4: Flagged Consolidation

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 17 * * 1-5` (UTC) = M-F 12:00 PM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 |
| **Prompt file** | `cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md` |

## What it does

Consolidates contacts from companies marked `customer_segment = "Flagged for deletion"` — reassociates valuable contacts to ICP primaries via the pre-deletion-audit gate before companies get archived. Companion to Cooper's biweekly manual cleanup of the Flagged-for-deletion pile.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
