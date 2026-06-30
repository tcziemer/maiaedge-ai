# Cowork task metadata — Signal Scan: Enterprise (Multi-DC ICP)

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 18 * * 1` (UTC) = Mon 1:00 PM CT |
| **Enabled** | (Cooper registers in Cowork UI; default disabled until rollout date) |
| **MCP connections** | HubSpot, Apollo, Slack, web_fetch, web_search |
| **Apollo budget** | Sub-cap 55 credits/run (tied with NeoCloud for highest — newest ICP; scale-gate verification drives Apollo volume) |
| **Prompt file** | `cowork-scheduled-tasks/signal-scan-enterprise/prompt.md` |

## What it does

Monday-morning signal scrape for the Enterprise (Multi-DC ICP) segment (`customer_segment = "Enterprise-CustomerSegment"`, display label "Enterprise"). Newest ICP (promoted 2026-05-11). Anchor account: Meijer.

Hard sourcing gate: vertical (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services) AND scale ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR in-house network engineering).

Largest source registry of the 6 segments (~34 documented sources spanning trade press, SEC filings, regulator portals, vendor customer-success pages).

**No rep DMs, no canvas, no Cooper run report** — aggregator at 2:30pm CT handles those.

Splits out from the monolithic weekly-signal-scan (archived 2026-05-28). Inherits the Enterprise ICP scope from the 2026-05-11 promotion.

## How to update

1. Edit `prompt.md` in this folder.
2. Open Cowork UI → CRM Guardian project → Scheduled Tasks.
3. Replace the prompt content for `signal-scan-enterprise` with the updated `prompt.md` text.
4. The file on disk is the source of truth.
