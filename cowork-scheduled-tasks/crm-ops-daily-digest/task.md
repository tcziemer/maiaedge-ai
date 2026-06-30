# Cowork task metadata — CRM Ops Daily Digest

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `45 21 * * 1-5` (UTC) = M-F 4:45 PM CT during CDT (shift to `45 22 * * 1-5` during CST, Nov-March) |
| **Enabled** | (Cooper registers in Cowork UI) |
| **MCP connections** | HubSpot (read), Slack |
| **Apollo budget** | 0 (read-only HubSpot + Slack + filesystem) |
| **Prompt file** | `cowork-scheduled-tasks/crm-ops-daily-digest/prompt.md` |

## What it does

The single end-of-day ops surface for Cooper. Fires at 4:45 PM CT after the day's CRM-maintenance writers (R0 9 AM, R1 10 AM, R2 11 AM, R4 12 PM, R10 1:30 PM, R-Tier-Audit 3 PM CT; Monday also after the signal-scan aggregator 2:30 PM CT). The Daily Sales Activity Brief (6 PM CT) is a rep-facing deliverable that fires *after* this digest and is not an ops writer - the digest confirms its dispatch in one line but does not health-grade or depend on it. Reads ground truth and produces one dashboard + one DM instead of ~8 separate routine self-DMs.

Sequence:
1. **Stage 0** — preflight; resolve the since-last-digest window (Monday reaches back to Friday); read the working ledger `F0B0AFSB9LN`. Abort + one-line ping if HubSpot is unreachable.
2. **Stage 1** — HubSpot delta counts for the window (enriched, newly flagged by reason, signal writes, tier/heat/segment changes, new accounts, contacts touched). **HubSpot is source of truth.**
3. **Stage 2** — fleet health for ~13 ops routines from ledger Run-log rows + HubSpot deltas + on-disk reports + `apollo-budget.json`. "Did not run" when expected → Attention.
4. **Stage 3** — the standing Flagged-for-deletion queue (companies by 7 reason codes + flagged contacts + optional SAFE_TO_DELETE split). The only action section.
5. **Stage 4** — overwrite the dashboard canvas to current state.
6. **Stage 5** — one short DM to Cooper (`U0A24D9RJLS`) pointing at the dashboard.
7. **Stage 6** — disk audit `weekly-reports/<date>/ops-digest/digest.md` + one Run-log row to `F0B0AFSB9LN`.

**Dashboard canvas:** separate from the working ledger `F0B0AFSB9LN`. First run bootstraps it via `slack_create_canvas` and DMs Cooper the new `canvas_id` to paste into `prompt.md` as `DASHBOARD_CANVAS_ID`.

**Read-only on the CRM:** the digest writes nothing to HubSpot and consumes no Apollo. Its only writes are the dashboard canvas, one DM, one ledger Run-log row, and the disk audit.

## Rollout

Runs in parallel with the existing routine self-DMs for ~1 week so Cooper can confirm the dashboard counts reconcile against the routine DMs (counts come from HubSpot, so they should match). Once validated, the ops routines are switched to quiet-on-success / ping-on-hard-failure (separate change to each routine's Delivery section), leaving the digest as the single daily ops channel.

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `crm-ops-daily-digest` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
