# Cowork task metadata — R10 Field Completeness Sweep

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 18 * * 1-5` (UTC) = M-F 1:30 PM CT during CDT (shift to `30 19 * * 1-5` during CST, Nov-March) |
| **Enabled** | (Cooper registers in Cowork UI) |
| **MCP connections** | HubSpot (read/write), Apollo (enrich), Slack |
| **Apollo budget** | 25 credits / run (drawn from the shared 850 / ISO-week cap per `routines/_shared/apollo-weekly-budget-spec.md`) |
| **Prompt file** | `cowork-scheduled-tasks/r10-completeness-sweep/prompt.md` |

## What it does

Fills enriched-field / blank-`account_tier` gaps on classified-but-incomplete records that fall between R1 (fresh), R2 (stale rotation), and R-Tier-Audit (tier/heat drift). Enabled 2026-06-04. Runs at 1:30 PM CT, after R4 (12 PM) and before R-Tier-Audit (3 PM), so the tier audit sees completed records.

**Quiet-on-success:** reports ONLY through the CRM Ops Daily Digest (no standalone DM, per Cooper 2026-06-04). Its run report + ledger row are folded into the digest's fleet table + Stage-1 enrichment deltas. DM Cooper only on hard failure.

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `r10-completeness-sweep` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
