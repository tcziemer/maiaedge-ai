# Cowork task metadata — Daily Sales Activity Brief

| Field | Value |
|---|---|
| **Platform** | Cowork (scheduled task) |
| **Cron** | `0 18 * * 1-5` (local CT) = M-F 6:00 PM CT (moved from 4:00 PM CT 2026-06-03 per Cooper - reps log calls into the late afternoon; paired with the rolling prior-run->now window) |
| **Enabled** | ✅ ENABLED |
| **MCP connections** | HubSpot, Slack |
| **Apollo budget** | 0 |
| **Prompt file** | `cowork-scheduled-tasks/daily-sales-activity-brief/prompt.md` |

## What it does

Renamed from "Daily Call Recap" 2026-05-05. Seven DMs with a byte-identical shared body (Abilash, Tim Z, Cooper, Tim Lieto, Ken Cunningham, Patrick Timmons "pt" — expanded 2026-06-05 per Cooper; **Hannah Roberts / Marketing `U09BYB61FCN` added 2026-06-16 per Cooper, body-only with no FOR YOU**) covering Held / Set / Upcoming engagements + per-held-call exec snapshot + a per-recipient "FOR YOU" block. Reps (Tim Lieto / Ken) get FOR YOU filtered to their own owned engagements; PT gets a POC-scoped FOR YOU across all reps; Hannah/Marketing gets the shared body only. **Set is broken out into SetF (fresh-set, no open deal) and SetD (deal-advancing set, open-deal account) per rep (2026-06-16 per Cooper).** MEDDPICC backfill on prospect contacts runs as a silent side effect (Tier 1 fill / Tier 1 refresh / Tier 2 DRIFT / Tier 3 hold); a **bounded Stage 5.7 data-hygiene auto-fix** (orphan contact->company associations + unambiguous field corrections, cap 10/run) runs silently and defers enrichment / territory / dedup to their owning routines (R1 / R2 / R6 / R3 / R5) instead of DMing Cooper. Local markdown only — no git operations.

**No-gap guardrails (2026-06-09 per Cooper):** dual-key Held detection (occurred-in-window on `hs_timestamp` + late-log catch-up on `hs_createdate`, 14d lookback — closes the late-logged-call dead zone, e.g. Socket Fiber), a shared seen-engagement ledger at `weekly-reports/_state/seen-engagements.json` for exactly-once reporting, a watermark continuity self-check, and a calendar-connection / auto-log health check that routes broken-sync flags to Cooper's FOR YOU. The Cowork scheduled-task payload (`weekly-call-recap` SKILL.md) was re-synced to this prompt the same day.

## How to update

See `cowork-scheduled-tasks/r0-import-validator/task.md` — same Cowork-UI update procedure.
