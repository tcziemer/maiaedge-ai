# CRM Ops Daily Digest (Cowork scheduled task)

You are running the **end-of-day digest** for MaiaEdge's CRM-maintenance fleet. The ops routines (R0–R9 + R-Tier-Audit + D7 + the Monday signal scan) ran through the day, each writing an on-disk run report and a Run-log row to the working ledger canvas `F0B0AFSB9LN`, and stamping HubSpot.

Your job: read what actually happened (HubSpot is ground truth), refresh Cooper's **dashboard canvas** to current state, send **one short DM**, and write a disk audit. **You do NOT write to HubSpot, do NOT scrape the web, do NOT consume Apollo.** Read-only on HubSpot; on Slack you read the working ledger and write the dashboard canvas + one DM + one Run-log row.

This is the single daily ops surface for Cooper. The only action it ever asks of him is reviewing the **Flagged for deletion** queue. Everything else is status he can glance at, not a to-do.

## Apollo budget

**0 credits.** No Apollo MCP calls. Read-only HubSpot + Slack + filesystem.

## Dashboard canvas

The dashboard lives at canvas `F0B7YMN4XEG` (workspace `maia-edge.slack.com`, URL https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B7YMN4XEG). This is a different canvas from the working ledger `F0B0AFSB9LN` — never overwrite the ledger.

The id is hardcoded (set 2026-06-02, bootstrap run). No reminder, no create/search — each run just refreshes canvas `F0B7YMN4XEG` to current state (Stage 4). If that canvas is ever deleted, create a fresh one via `slack_create_canvas` titled `MaiaEdge CRM Ops Dashboard`, paste its id here, and DM Cooper the new id.

## Window

- **Tue–Fri:** since yesterday 4:45 PM CT (prior ~24h).
- **Monday:** since **Friday** 4:45 PM CT — covers weekend R3 (daily 2 AM ET), R6 (daily 1 AM ET), and R5 (Sun 1 AM ET). Mirrors the Daily Sales Activity Brief's Monday catch-up.

Call the window start `WINDOW_START` (a date) for the HubSpot delta queries below.

---

## Stage 0 — Preflight

1. **MCP health check** — HubSpot + Slack. If **HubSpot is unreachable**, abort and send the one-line failure ping to Cooper (`U0A24D9RJLS`): `:red_circle: CRM Ops Daily Digest ABORTED — HubSpot MCP unreachable.` Do not write a partial dashboard. Slack-read failures degrade gracefully (fall back to a fuller DM at Stage 5).
2. **Resolve today (CT)** and `WINDOW_START` per the Window rules.
3. **Read the working ledger** `F0B0AFSB9LN` via `slack_read_canvas`: the Run-log rows in the window, the Tier 3 / manual-review backlog section, and the status-emoji conventions (use ONLY those emojis).
4. **Optional cross-check** — if the scheduled-tasks MCP is available, call `list_scheduled_tasks` to read each task's `lastRunAt` / `nextRunAt`. Use it to corroborate "did it fire" in Stage 2; never block on it.

---

## Stage 1 — Ground-truth deltas (HubSpot, authoritative)

Query HubSpot companies for the window. HubSpot is the source of truth; routine self-reports are not trusted for counts. MaiaEdge own record `124293230301` is always excluded.

Compute these counts (counts only — no per-record listing):
- **Enriched / re-enriched:** `last_enriched_date >= WINDOW_START`.
- **Newly flagged for deletion:** `customer_segment = "Flagged for deletion"` AND `hs_lastmodifieddate >= WINDOW_START`. Group by parsing the leading reason code in `flagged_for_deletion_reason` (substring before the first colon) into the 7 codes (`Dead domain`, `Hard junk / non-business`, `D1 disqualified (no reference value)`, `No ICP fit`, `Duplicate (merged)`, `Defunct / out of business`, `Stalled greenfield`); count any empty-reason flags separately.
- **Signal writes:** `last_signal_date >= WINDOW_START` (Monday signal scan + outreach push-backs).
- **Tier / heat / segment / confidence changes:** count records whose `account_tier`, `signal_heat`, `customer_segment`, or `segmentation_confidence` were modified in the window (use `hs_lastmodifieddate >= WINDOW_START` as the gate, then attribute by which field is freshest where the API allows).
- **NEW accounts created:** companies with `createdate >= WINDOW_START`.
- **Contacts touched:** contacts with `lastmodifieddate >= WINDOW_START` (rough activity gauge) and `flagged_for_deletion = true` count.

These power "Today at a glance" on the dashboard.

---

## Stage 2 — Fleet health

For each routine in the roster below, derive `{last run, status, records touched, Apollo used vs sub-cap}` from three sources, in priority order: (a) the working-ledger Run-log rows in the window, (b) the Stage 1 HubSpot deltas, (c) the on-disk run report at `weekly-reports/<date>/<folder>/<file>` + `weekly-reports/apollo-budget.json`.

**Status** uses the ledger's emoji conventions: ✅ healthy · ⚠️ degraded/partial · 🔴 blocked/error · ⏭ skipped (precondition not met). A routine that was **expected to fire** in the window but has **no Run-log row AND no HubSpot delta** = 🔴/⏭ "did not run" → it becomes an **Attention** item (Stage 3 / dashboard §5).

### Roster (expected fire; CT)

| Routine | Cadence / expected fire | Disk report | Apollo sub-cap |
|---|---|---|---|
| R0 Import Validator | Daily M-F 9:00 AM | `weekly-reports/<date>/r0-import-validator/run-report.md` | 0 |
| R1 Fresh Enrichment | Daily M-F 10:00 AM | `…/r1-fresh-enrichment/run-report.md` | 30/run |
| R2 Stale Re-Enrichment | Daily M-F 11:00 AM | `…/r2-stale-reenrichment/run-report.md` | 50/run |
| R4 Flagged Consolidation | Daily M-F 12:00 PM | `…/r4-flagged-consolidation/audit.md` | 0 |
| R-Tier-Audit | Daily M-F 3:00 PM | `weekly-reports/tier-audit/<date>-tier-audit.md` | 0 |
| R10 Completeness Sweep | Daily M-F 1:30 PM (pending enablement) | `…/r10-completeness-sweep/run-report.md` | 25/run |
| R3 Duplicate Accounts | Daily 2:00 AM ET | (ledger row) | 0 |
| R6 Territory & Hygiene | Daily 1:00 AM ET | (ledger row) | 5/run |
| D7 Edge Case Resolution | Wed 9:00 AM | `…/d7-edge-case-resolution/` | 0 |
| R5 Contact Dedup | Sun 1:00 AM ET | (ledger row) | 0 |
| R8 Persona Fill | Fri 9:00 AM ET | (ledger row) | 175/run |
| Signal Scan (6 + aggregator) | Mon 8:30 AM–2:30 PM | `weekly-reports/<date>/signal-scan/**` | 250 total |
| R7 Monthly Sourcing | 1st of month 9 AM ET | (ledger row) | spare |
| R9 Quarterly Job Changes | Quarterly | (ledger row) | spare |

Only judge a routine "did not run" against its **expected** cadence (e.g., don't flag R5 on a Tuesday, or R8 on a non-Friday). **R10 (Completeness Sweep) is quiet-on-success and reports ONLY through this digest** (Cooper 2026-06-04 — it sends no standalone DM): fold its run report + ledger row into the fleet table and the Stage-1 enrichment deltas, and surface its frozen-blank-tier seeds + any partials-held under Attention only when non-zero. **Until R10 is enabled, do NOT flag it as "did not run"** (it's registered but paused). The rep-facing deliverables (Daily Sales Activity Brief, signal-scan rep DMs, Weekly Market News) are not ops routines — confirm in one line whether the day's expected deliverable dispatched, but do not health-grade them here.

---

## Stage 3 — Action queue (the one human task)

Query HubSpot for the full standing **Flagged for deletion** pool (not just the window):
- Companies: `customer_segment = "Flagged for deletion"` (exclude `124293230301`). Total + breakdown by the 7 reason codes (parse `flagged_for_deletion_reason` before the first colon; empty-reason counted separately).
- Contacts: `flagged_for_deletion = true` count.

Where cheap, split the company pool by a lightweight pre-deletion-audit read — **SAFE_TO_DELETE** (no open/closed-won deals, no important attachments, ≤4 contacts, no recent activity) vs **needs-review** — so Cooper can clear the safe pile in one sweep. If that split is too expensive this run, surface the total + reason breakdown only and note "verdict split not computed this run."

Include the exact HubSpot filters Cooper uses: Companies → `customer_segment = "Flagged for deletion"`; Contacts → `flagged_for_deletion = true`.

---

## Stage 4 — Refresh the dashboard canvas

Overwrite the dashboard canvas `F0B7YMN4XEG` to current state via `slack_update_canvas` (replace content; this canvas is always current, never append-only). Sections:

1. **Header** — `MaiaEdge CRM Ops Dashboard — as of <YYYY-MM-DD HH:MM CT>`.
2. **Fleet health** — table: Routine · Last run · Status (✅/⚠️/🔴/⏭) · Records touched · Apollo used/cap. One row per roster routine expected in the window.
3. **Today at a glance** — the Stage 1 counts: enriched / re-enriched · newly flagged (with the 7-code split) · signal writes · tier Δ · heat Δ · segment Δ · NEW accounts · contacts touched.
4. **⚑ Your queue — Flagged for deletion** — total companies + 7-reason breakdown + flagged-contacts count + the SAFE_TO_DELETE vs needs-review split (if computed) + the HubSpot filters. This is the only action section.
5. **⚠ Attention** — only genuine blockers: a routine that didn't fire, errored (🔴), Apollo weekly cap hit, or the manual-review backlog over threshold. Render `All clear` when empty.
6. **Manual-review backlog** — count from the ledger Tier 3 section + a 7-day trend (compare to the count recorded in prior digests' disk audits). Awareness only — D7 drains this; never a Cooper to-do unless it stops shrinking (then it is an Attention line in §5).

---

## Stage 5 — Short DM to Cooper

Send ONE DM to Cooper (`U0A24D9RJLS`) via `slack_send_message`. 4–6 lines, counts only, link to the dashboard:

```
:bar_chart: CRM Ops Daily — [YYYY-MM-DD]
Fleet: [N of M routines green; "all green" / "N need attention"].
Today: [X enriched · Y newly flagged · Z deduped · T tier moves · H heat moves · N new accts].
:triangular_flag_on_post: Flagged for deletion: [N] companies to review ([top reason breakdown]) · [C] contacts.
Attention: [All clear / N issues — see dashboard].
Dashboard ⤵ <canvas link>
```

Never put per-record detail in the DM — that lives on the canvas. If Slack DM fails, retry once, then leave the disk audit (Stage 6) as the record.

---

## Stage 6 — Disk audit + ledger row

1. Write `weekly-reports/<today CT YYYY-MM-DD>/ops-digest/digest.md` capturing: the Stage 1 counts, the fleet-health table, the flagged-for-deletion totals + reason breakdown, the manual-review backlog count (so tomorrow's run can compute the trend), and any anomalies.
2. Append ONE Run-log row to the working ledger `F0B0AFSB9LN` via `slack_update_canvas` (append, do not replace): `| YYYY-MM-DD HH:MM CT | CRM Ops Daily Digest | <status emoji> | <one-sentence summary> | <dashboard link + digest.md path> |`. Status: ✅ normal, ⚠️ if any data gap (missing disk reports / canvas-write fallback), 🔴 if it had to abort earlier.

---

## Failure handling

- **HubSpot unreachable at Stage 0/1:** abort + one-line failure ping (Stage 0). The dashboard cannot be trusted without ground truth.
- **Working-ledger read fails:** proceed on HubSpot deltas + disk reports; note "ledger unread" as a data gap on the dashboard and in the DM.
- **1–2 disk run reports missing:** note as a data gap in the affected fleet-health rows (status from ledger/HubSpot still stands); still ship.
- **Dashboard canvas write fails:** retry once. On second failure, send a fuller DM (inline the fleet-health + flagged-for-deletion sections) so Cooper still gets the day, and surface the canvas failure in the disk audit.
- **DM dispatch fails:** retry once; the disk audit at `weekly-reports/<date>/ops-digest/digest.md` is the fallback record.

## End-of-run footer

Log one line to Cowork chat:
```
[Ops Digest] window=WINDOW_START→today fleet_green=N/M flagged_for_deletion=N attention=N dashboard=<canvas_id> audit=weekly-reports/<date>/ops-digest/digest.md
```
