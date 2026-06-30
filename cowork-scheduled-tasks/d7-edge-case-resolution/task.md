# Cowork task metadata — D7: Edge Case Resolution

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 14 * * 3` (UTC) = Wed 9:00 AM CT (Cooper-chosen) |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 (web_fetch + web_search only) |
| **Prompt file** | `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md` |

## What it does

Processes the manual_review queue (>7 days), low_5069 records (>60 days no R2 touch), Unknown/Other with deal activity, crm-hygiene MODE 12-flagged records. Per-run cap 30 records. Hard 14-day max on manual_review_required.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
