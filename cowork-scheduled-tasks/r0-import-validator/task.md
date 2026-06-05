# Cowork task metadata — R0: Import Validator

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 14 * * 1-5` (UTC) = M-F 9:00 AM CT |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 (Apollo-free by design) |
| **Prompt file** | `cowork-scheduled-tasks/r0-import-validator/prompt.md` |

## What it does

Scans companies imported in the last 24h that haven't been enriched yet, validates HubSpot company NAME matches the entity actually at the domain, fixes mismatches BEFORE downstream Apollo-consuming tasks waste credits. Surfaces hard-flag categories (restaurants, churches, etc.) for auto-deletion-flagging at HIGH confidence.

## How to update

This prompt runs as a Cowork scheduled task, not via a `RemoteTrigger`. The prompt content lives in Cowork's scheduled-task config. To update:

1. Edit `prompt.md` in this folder.
2. Open the scheduled task in Cowork's UI.
3. Paste the new prompt content into the task config.
4. Save.

There is no API push from this repo into Cowork. The file is the source of truth; Cowork's config is the live runtime copy.
