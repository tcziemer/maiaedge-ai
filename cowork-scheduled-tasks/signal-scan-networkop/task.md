# Cowork task metadata — Signal Scan: Network Operator

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `30 16 * * 1` (UTC) = Mon 11:30 AM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 50 credits/run (second highest — GitHub commits + procurement portals drive NEW-account volume) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-networkop/prompt.md` |

## What it does

Monday-morning signal scrape for the Network Operator segment (`customer_segment = "Network Operator(Tier 1 / VNO)"`). Signal codes use `NO-` prefix to disambiguate from NeoCloud's `NC-` prefix. ~22 documented sources including Tier 1 carrier IR pages, GitHub commit feeds for CAMARA/Nephio/ONAP/OpenConfig/Sylva, FedBizOpps RFI/RFP feeds, MEF/Mplify newsroom, TM Forum announcements.

Subsea cable operator (30th sub-segment, added 2026-05-14) routes under this segment.

**No rep DMs, no canvas, no Cooper run report** — aggregator at 2:30pm CT handles those.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28).

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-networkop` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
