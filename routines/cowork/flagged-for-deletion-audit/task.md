# Cowork task metadata — Flagged-for-Deletion Audit

| Field | Value |
|---|---|
| **Platform** | Cowork (manual trigger / Cooper-fired) |
| **Cron** | None — biweekly manual cadence (per Cooper's memory feedback `flagged_for_deletion_manual`) |
| **Enabled** | ✅ AVAILABLE (no schedule; Cooper biweekly review) |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 |
| **Prompt file** | `routines/cowork/flagged-for-deletion-audit/prompt.md` |

## What it does

Biweekly audit of the Flagged-for-deletion pile + R3 dup-pending records. Surfaces them for Cooper to review and bulk-delete manually. Companion to R4 Flagged Consolidation (which preserves valuable contacts before company archive).

## How to update

This is an on-demand prompt; Cooper runs it on a manual biweekly cadence.
