# Trigger metadata — Routine 3: Duplicate Accounts

| Field | Value |
|---|---|
| **Trigger ID** | `trig_01XTjFhegfVTCtSpZXEDY5Ce` |
| **Platform** | Claude Code (RemoteTrigger) |
| **Cron** | `0 7 * * *` (UTC) = daily 2:00 AM ET |
| **Enabled** | ✅ ENABLED |
| **Environment ID** | `env_018AmYCxSHNPrHk4q3ofk9hm` |
| **claude.ai name** | MaiaEdge CRM Guardian — Routine 3: Duplicate Accounts (daily 2am ET) |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 (HubSpot-internal, no web/Apollo) |
| **Prompt file** | `routines/claude-code/r3-duplicate-accounts/prompt.md` |

## How to update the trigger after editing `prompt.md`

1. Edit `prompt.md` in this folder.
2. Push the new content into the trigger using `RemoteTrigger.update` with body:

```json
{
  "job_config": {
    "ccr": {
      "environment_id": "env_018AmYCxSHNPrHk4q3ofk9hm",
      "events": [{
        "data": {
          "message": {"content": "<full prompt.md content>", "role": "user"},
          "parent_tool_use_id": null,
          "session_id": "",
          "type": "user"
        }
      }]
    }
  }
}
```

3. Verify via `RemoteTrigger.get` that `updated_at` advanced.

## Notes

- The prompt content is stored inline in the trigger. Editing `prompt.md` on disk does NOT automatically update the live trigger — you must push the change.
- `enabled_plugins`, `session_context.allowed_tools`, and `mcp_connections` are managed in the claude.ai UI when the trigger was created; partial updates here preserve them.
- Sometimes the trigger needs to be re-created when the schema version changes (`job_config v1→v2` migration). The current schema requires `environment_id` in every update payload.
