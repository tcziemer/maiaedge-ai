# CRM Guardian — Scheduled Tasks Self-Setup Prompt

> Paste the section below ("PROMPT STARTS HERE") into a new conversation in the CRM Guardian Claude.ai project (or into a Cowork session that has the scheduled-tasks MCP). Claude will read the latest Cowork prompt files from disk, then create / update / enable every scheduled task to match the post-migration spec. One paste, one approval flow per task.

---

## What this prompt does (overview, for your reference — do NOT include in the paste)

Brings the entire Cowork scheduled-task fleet to a known-good state in one run: disables the monolithic `weekly-signal-scan` (preserved, not deleted) and creates / refreshes / enables 16 tasks — the daily CRM Guardian routines, the 7 per-ICP signal scans + aggregator, the rep-facing deliverables, R-Tier-Audit, D7, and the CRM Ops Daily Digest. (This folds in what used to be a separate signal-scan-split rollout.)

> **Fleet delivery model:** the ops routines (R0/R1/R2/R4/R-Tier-Audit/D7 here, plus the Claude Code routines R3/R5/R6/R7/R8/R9) are **quiet on success** — they write an on-disk run report + one Run-log row to the working-ledger canvas `F0B0AFSB9LN`, and DM Cooper only on a hard failure (one `:red_circle:` line). The `crm-ops-daily-digest` task (row 10) is the single daily ops surface: it reads HubSpot + the ledger and renders the fleet on a dashboard canvas + one short DM. The rep-facing deliverables (`weekly-call-recap` / Daily Sales Activity Brief, the signal-scan rep DMs, `weekly-market-news`) keep sending their own DMs — they are not ops clutter. Re-reading each prompt fresh from disk (Step 3) deploys this model automatically.

> **Cron timezone (corrected 2026-05-30):** Cowork's `create_scheduled_task` interprets cron expressions in the user's **LOCAL timezone (America/Chicago, CT)**, NOT UTC. The cron values below are LOCAL CT — use them verbatim, no offset math. Verified against the live fleet: `weekly-call-recap` is registered as `0 16 * * 1-5` and fires at 4:00pm CT; `crm-guardian-import-validator` is `0 9 * * 1-5` and fires at 9:00am CT — both only consistent with local-time interpretation. (A prior version of this file claimed UTC and listed crons 5-6h ahead; that was wrong and, if followed, would have fired the entire fleet ~5h late. Do not re-introduce the offset.)

| # | taskId | Cron (local CT) | Source prompt file | Action |
|---|---|---|---|---|
| 1 | `crm-guardian-import-validator` | `0 9 * * 1-5` (M-F 9am CT) | `cowork-scheduled-tasks/r0-import-validator/prompt.md` | refresh prompt + re-enable |
| 2 | `crm-guardian-fresh-enrichment` | `0 10 * * 1-5` (M-F 10am CT) | `cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md` | refresh prompt + re-enable |
| 3 | `crm-guardian-stale-re-enrichment` | `0 11 * * 1-5` (M-F 11am CT) | `cowork-scheduled-tasks/r2-stale-reenrichment/prompt.md` | refresh prompt + re-enable |
| 4 | `crm-guardian-flagged-consolidation` | `0 12 * * 1-5` (M-F 12pm CT) | `cowork-scheduled-tasks/r4-flagged-consolidation/prompt.md` | refresh prompt + re-enable |
| 5a | `signal-scan-colo` | `30 8 * * 1` (Mon 8:30am CT) | `cowork-scheduled-tasks/signal-scan-colo/prompt.md` | **CREATE NEW** (replaces monolithic `weekly-signal-scan`, archived 2026-05-28) |
| 5b | `signal-scan-fiber` | `30 9 * * 1` (Mon 9:30am CT) | `cowork-scheduled-tasks/signal-scan-fiber/prompt.md` | **CREATE NEW** |
| 5c | `signal-scan-neocloud` | `30 10 * * 1` (Mon 10:30am CT) | `cowork-scheduled-tasks/signal-scan-neocloud/prompt.md` | **CREATE NEW** |
| 5d | `signal-scan-networkop` | `30 11 * * 1` (Mon 11:30am CT) | `cowork-scheduled-tasks/signal-scan-networkop/prompt.md` | **CREATE NEW** |
| 5e | `signal-scan-msp` | `30 12 * * 1` (Mon 12:30pm CT) | `cowork-scheduled-tasks/signal-scan-msp/prompt.md` | **CREATE NEW** |
| 5f | `signal-scan-enterprise` | `0 13 * * 1` (Mon 1:00pm CT) | `cowork-scheduled-tasks/signal-scan-enterprise/prompt.md` | **CREATE NEW** |
| 5g | `signal-scan-aggregator` | `30 14 * * 1` (Mon 2:30pm CT) | `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` | **CREATE NEW** (Apollo budget 0; reads HubSpot + builds rep DMs + canvas Run log + Cooper run report) |
| ~~5~~ | ~~`weekly-signal-scan`~~ | ~~`0 13 * * 1`~~ (Mon 1pm CT) | ~~archived 2026-05-28~~ | **DISABLE** if currently registered (monolithic prompt retired; 5a-5g replace it) |
| 6 | `weekly-call-recap` | `0 16 * * 1-5` (M-F 4pm CT) | `cowork-scheduled-tasks/daily-sales-activity-brief/prompt.md` | refresh prompt only (already enabled) |
| 7 | `weekly-market-news` | `0 13 * * 5` (Fri 1pm CT) | `cowork-scheduled-tasks/weekly-market-news/prompt.md` | refresh prompt + re-enable |
| 8 | `crm-guardian-tier-audit` | `0 15 * * 1-5` (M-F 3pm CT) | `cowork-scheduled-tasks/r-tier-audit/prompt.md` | **CREATE NEW** + enable |
| 9 | `crm-guardian-edge-case-resolution` | `0 9 * * 3` (Wed 9am CT) | `cowork-scheduled-tasks/d7-edge-case-resolution/prompt.md` | **CREATE NEW** + enable |
| 10 | `crm-ops-daily-digest` | `45 16 * * 1-5` (M-F 4:45pm CT) | `cowork-scheduled-tasks/crm-ops-daily-digest/prompt.md` | **CREATE NEW** + enable (Apollo 0; reads HubSpot + ledger + disk; refreshes the ops dashboard canvas + sends one DM to Cooper) |

`smartlead-health-check` (Tue/Thu 8:45 AM CT) is unrelated to the migration overhaul and is intentionally left untouched. Its independent operating state is preserved.

---

## PROMPT STARTS HERE — copy everything below this line

You are setting up MaiaEdge's Cowork scheduled tasks after the Account Tiering & Segmentation Overhaul migration. Cooper has finished Phases 1, 2, and 3. The Cowork prompts in `C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\` were updated to reflect the new framework (`customer_segment` + `company_sub_segment` + signal modifiers + `hs_is_target_account` freeze rule + `tier-compute-spec.md`). Your job: disable the archived monolithic `weekly-signal-scan` (preserve its history), then create / refresh / enable the full fleet — the daily CRM Guardian routines, the 7 per-ICP signal scans + aggregator, the rep-facing deliverables, R-Tier-Audit, D7, and the CRM Ops Daily Digest — with the latest prompt content.

You re-read every task's prompt fresh from disk in Step 3, so each task gets the current payload verbatim — copy it exactly, do not edit content.

## Constraints

- **Cron expressions are evaluated in the user's LOCAL timezone (CT)** (per Cowork's `create_scheduled_task` tool semantics — verified 2026-05-30 against the live `weekly-call-recap` task which is registered as `0 16 * * 1-5` and fires at 4pm CT, and `crm-guardian-import-validator` registered as `0 9 * * 1-5` firing at 9am CT). Use the cron strings exactly as listed below — they are already in local CT, so do NOT apply any UTC offset. (Cowork displays `nextRunAt` as a UTC ISO timestamp, but the cron you submit is interpreted in local time; do not let the UTC `nextRunAt` mislead you into offsetting the cron.)
- **Each task's `prompt` argument MUST be the FULL contents of its source file**, freshly read at setup time. Do NOT paraphrase, summarize, or truncate. The prompt is the entire payload that runs each fire.
- **Never re-enable without first refreshing the prompt content.** The Cowork-cached SKILL.md may be the pre-migration version.
- **`smartlead-health-check` is out of scope.** Do not touch it.
- **Ask Cooper for go/no-go before each circuit breaker action.** Specifically: if any task currently exists with `enabled = true`, confirm with Cooper before overwriting its prompt. Otherwise proceed.

## Step 1 — Inventory current state

Call `mcp__scheduled-tasks__list_scheduled_tasks`. Cross-reference against the table below. Note for each row whether it (a) exists and is enabled, (b) exists and is disabled, or (c) does not exist.

## Step 2 — Disable the monolithic `weekly-signal-scan` first

If the Step 1 inventory shows `weekly-signal-scan` exists and is enabled, disable it before processing the create/refresh list: call `mcp__scheduled-tasks__update_scheduled_task` with `taskId = weekly-signal-scan`, `enabled = false`, and leave its `cronExpression` / `description` / `prompt` unchanged (this preserves its prior-run history; the 7 `signal-scan-*` tasks below replace it). If it doesn't exist or is already `enabled: false`, skip and note it in the report. Never delete it.

## Step 3 — For each of the 16 create/refresh tasks below, in this order

For each row:

1. **Read the source file** with the `Read` tool at the absolute path given.
2. **If the task does not exist**, call `mcp__scheduled-tasks__create_scheduled_task` with:
   - `taskId` = exactly as listed
   - `cronExpression` = exactly as listed (local CT)
   - `description` = exactly as listed
   - `prompt` = the FULL contents of the source file (entire file body)
3. **If the task exists**, call `mcp__scheduled-tasks__update_scheduled_task` with:
   - `taskId` = exactly as listed
   - `cronExpression` = exactly as listed (local CT; forces correction if it had drifted)
   - `description` = exactly as listed
   - `prompt` = the FULL contents of the source file
   - `enabled` = `true`
4. **Confirm success** by re-running `list_scheduled_tasks` and checking the row appears with `enabled: true` and the cron you set.

### The 16 create/refresh tasks

```
1. crm-guardian-import-validator
   cron:        0 9 * * 1-5      # local CT; M-F 9am CT
   description: CRM Guardian — Import Validator (Mon-Fri 9am CT). Validates fresh HubSpot company imports against actual entity at the domain.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\r0-import-validator\prompt.md

2. crm-guardian-fresh-enrichment
   cron:        0 10 * * 1-5     # local CT; M-F 10am CT
   description: CRM Guardian — Fresh Enrichment (Mon-Fri 10am CT). Drives every HubSpot company in the active candidate pool to a definitive segment+sub_segment+tier+brief. Three-path workflow (α full enrichment, β re-research, γ eviction). Apollo sub-cap 50/run, dynamic record cap 100/125/150 by backlog.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\r1-fresh-enrichment\prompt.md

3. crm-guardian-stale-re-enrichment
   cron:        0 11 * * 1-5     # local CT; M-F 11am CT
   description: CRM Guardian — Stale Re-Enrichment (Mon-Fri 11am CT). Re-enriches companies whose data exceeds the 120-day staleness threshold. Step 0B MISDOMAIN check, account_brief regen guarantee, recent_news staleness clearing, Apollo sub-cap 30/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\r2-stale-reenrichment\prompt.md

4. crm-guardian-flagged-consolidation
   cron:        0 12 * * 1-5     # local CT; M-F 12pm CT
   description: CRM Guardian — Flagged Consolidation (Mon-Fri 12pm CT). Gates "Flagged for deletion" decisions: dedup check, contact consolidation to ICP primary, 90-day activity preservation.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\r4-flagged-consolidation\prompt.md

5a. signal-scan-colo
   cron:        30 8 * * 1       # local CT; Mon 8:30am CT
   description: Signal Scan — Data Center Colo Provider (Mon 8:30am CT). One of 6 per-ICP weekly signal scans. Stages 0-5c: preflight + source-coverage scrape (~16 sources) + match + NEW-account creation + score + Sub-Agent QA Gate + HubSpot narrative write (pure prose, no date prefix) + structured signal field + tier/heat recompute + on-disk audit. No rep DMs, no canvas Run log, no Cooper run report — aggregator at 2:30pm CT handles those. Apollo sub-cap 35/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-colo\prompt.md

5b. signal-scan-fiber
   cron:        30 9 * * 1       # local CT; Mon 9:30am CT
   description: Signal Scan — Fiber Operator (Mon 9:30am CT). Stages 0-5c for the Fiber segment only (~22 sources including BEAD subgrants, SEC ABS prospectuses, vendor customer-win press). Apollo sub-cap 35/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-fiber\prompt.md

5c. signal-scan-neocloud
   cron:        30 10 * * 1      # local CT; Mon 10:30am CT
   description: Signal Scan — NeoCloud (Mon 10:30am CT). Stages 0-5c for the NeoCloud segment only. Highest-velocity segment with broadest source registry (~24 sources including IX member-list pages, NVIDIA partner pages, crypto-to-AI outlets, per-NeoCloud IR pages). Signal codes use NC- prefix to disambiguate from Network Op NO- prefix. Apollo sub-cap 55/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-neocloud\prompt.md

5d. signal-scan-networkop
   cron:        30 11 * * 1      # local CT; Mon 11:30am CT
   description: Signal Scan — Network Operator (Mon 11:30am CT). Stages 0-5c for the Network Operator segment (customer_segment = "Network Operator(Tier 1 / VNO)", NO space before paren). Signal codes use NO- prefix. ~22 sources including Tier 1 carrier IR pages, GitHub commit feeds for CAMARA/Nephio/ONAP/OpenConfig/Sylva, FedBizOpps RFI/RFP feeds, MEF/Mplify newsroom. Subsea cable operator (30th sub-segment) routes here. Apollo sub-cap 50/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-networkop\prompt.md

5e. signal-scan-msp
   cron:        30 12 * * 1      # local CT; Mon 12:30pm CT
   description: Signal Scan — MSP/Aggregator (Mon 12:30pm CT). Stages 0-5c for telecom/network aggregators ONLY (NOT IT MSPs — strict IT MSP Test on every detection). Lowest-velocity segment (~20 sources including Channel Futures, ChannelE2E, TSD press pages, ScanSource/TD SYNNEX investor pages). 48-hour priority signals tagged for aggregator. Apollo sub-cap 20/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-msp\prompt.md

5f. signal-scan-enterprise
   cron:        0 13 * * 1       # local CT; Mon 1:00pm CT
   description: Signal Scan — Enterprise (Multi-DC ICP) (Mon 1:00pm CT). Stages 0-5c for customer_segment = "Enterprise-CustomerSegment" (display "Enterprise"). Newest ICP (anchor Meijer). Hard sourcing gate: vertical (Fin Svcs / Healthcare Systems / Retail and Distribution / Outsourcing Services) AND scale ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR in-house network engineering). Largest source registry (~34 sources). Apollo sub-cap 55/run.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-enterprise\prompt.md

5g. signal-scan-aggregator
   cron:        30 14 * * 1      # local CT; Mon 2:30pm CT
   description: Signal Scan Aggregator (Mon 2:30pm CT). 1h 15m cushion after Enterprise nominal finish. Reads HubSpot for company records with last_signal_date = today (HubSpot is source of truth; missing per-segment audit files don't block rep DMs). Builds 3 territory-consolidated Slack DMs (Tim Lieto East U0A973L1HFF, Ken West U0AE1PGCB6C, Tim Z Int'l routed to Cooper U0A24D9RJLS per Phase 0 partial lift). Appends 1 canvas Run log row to F0B0AFSB9LN. Writes Cooper's cross-ICP run report. Apollo budget 0; read-only HubSpot + Slack.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\signal-scan-aggregator\prompt.md

6. weekly-call-recap
   cron:        0 16 * * 1-5     # local CT; M-F 4pm CT
   description: Daily Sales Activity Brief (Mon-Fri 4pm CT). Daily exec brief on sales activity (meetings set + held + upcoming) delivered to Abilash, Tim Z, and Cooper. MEDDPICC backfill runs as silent side effect. Renamed from "Daily Call Recap" 2026-05-05; taskId preserved for path stability.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\daily-sales-activity-brief\prompt.md

7. weekly-market-news
   cron:        0 13 * * 5       # local CT; Fri 1pm CT
   description: Weekly Market News (Friday 1pm CT). Friday-morning awareness digest covering all 6 ICPs (Enterprise added 2026-05-11). Top 3 stories per ICP with article-grounded summary + MaiaEdge angle, plus Cross-ICP Themes + Exec Moves callout. Read-only, no HubSpot writes. Cooper-only delivery in Phase 0.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\weekly-market-news\prompt.md

8. crm-guardian-tier-audit                 *** NEW — created Phase 3 of overhaul ***
   cron:        0 15 * * 1-5     # local CT; M-F 3pm CT
   description: R-Tier-Audit (M-F 3pm CT). Daily drift correction sweep over all active ICP records. Re-runs compute_tier() AND compute_signal_heat(); applies tier changes only where current ≠ computed AND hs_is_target_account ≠ true; applies heat changes regardless of hs_is_target_account. 10% circuit breaker. Apollo budget 0. Idempotent.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\r-tier-audit\prompt.md

9. crm-guardian-edge-case-resolution       *** NEW — created Phase 3 of overhaul ***
   cron:        0 9 * * 3        # local CT; Wed 9am CT
   description: D7 Edge Case Resolution (Wed 9am CT). Resolves the manual_review_required queue + stale low_5069 records + Unknown/Other escalations with deep web research. Per-run cap 30 records. 14-day max in manual_review_required. Apollo budget 0 (web_fetch + web_search only).
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\d7-edge-case-resolution\prompt.md

10. crm-ops-daily-digest
   cron:        45 16 * * 1-5    # local CT; M-F 4:45pm CT
   description: CRM Ops Daily Digest (Mon-Fri 4:45pm CT). End-of-day fleet digest. Reads HubSpot deltas (ground truth) + the working ledger F0B0AFSB9LN + on-disk run reports + apollo-budget.json; refreshes the ops dashboard canvas and sends ONE short DM to Cooper. The only action it surfaces is the Flagged-for-deletion queue. Read-only on HubSpot, Apollo budget 0.
   source file: C:\Users\coopf\OneDrive\Desktop\maiaedge-ai\cowork-scheduled-tasks\crm-ops-daily-digest\prompt.md
```

## Step 4 — Final verification

After the Step 2 disable + all 16 create/refresh tasks are processed:

1. Call `list_scheduled_tasks` one final time.
2. For each of the 16 create/refresh taskIds above, confirm:
   - exists
   - `enabled: true`
   - `cronExpression` matches the table exactly
   - `nextRunAt` is in the future (not stuck on a past timestamp). The 7 `signal-scan-*` tasks should show next Monday at their listed CT times. (`nextRunAt` is reported as a UTC ISO timestamp — during CDT it reads 5h ahead of the CT fire time, e.g. a Mon 8:30am CT task shows `...T13:3x:..Z`. That is expected and confirms the local-time cron resolved correctly; it is NOT a sign the cron needs offsetting.)
3. Confirm `weekly-signal-scan` is `enabled: false` with no future `nextRunAt` queued (still present for run-history audit — not deleted).
4. Confirm `smartlead-health-check` is still present, still enabled, and was not modified.

## Step 5 — Report to Cooper via Slack DM

Send a single Slack DM to Cooper at `U0A24D9RJLS` using `mcp__db777ba9-7b5e-45f1-9dd8-ca6b74958100__slack_send_message`. Use this template:

```
:gear: Scheduled tasks setup complete — full fleet baseline

Disabled (1): weekly-signal-scan (monolithic; preserved for run-history audit, replaced by the 7-task split below)
Created + enabled (10): signal-scan-colo, signal-scan-fiber, signal-scan-neocloud, signal-scan-networkop, signal-scan-msp, signal-scan-enterprise, signal-scan-aggregator, crm-guardian-tier-audit, crm-guardian-edge-case-resolution, crm-ops-daily-digest
Refreshed + re-enabled (5): crm-guardian-import-validator, crm-guardian-fresh-enrichment, crm-guardian-stale-re-enrichment, crm-guardian-flagged-consolidation, weekly-market-news
Refreshed only (1): weekly-call-recap (was already live)
Untouched (1): smartlead-health-check (not part of overhaul)

Next runs (local CT):
- crm-guardian-import-validator        → <nextRunAt>
- crm-guardian-fresh-enrichment        → <nextRunAt>
- crm-guardian-stale-re-enrichment     → <nextRunAt>
- crm-guardian-flagged-consolidation   → <nextRunAt>
- signal-scan-colo                     → <nextRunAt>
- signal-scan-fiber                    → <nextRunAt>
- signal-scan-neocloud                 → <nextRunAt>
- signal-scan-networkop                → <nextRunAt>
- signal-scan-msp                      → <nextRunAt>
- signal-scan-enterprise               → <nextRunAt>
- signal-scan-aggregator               → <nextRunAt>
- weekly-call-recap                    → <nextRunAt>
- weekly-market-news                   → <nextRunAt>
- crm-guardian-tier-audit              → <nextRunAt>
- crm-guardian-edge-case-resolution    → <nextRunAt>
- crm-ops-daily-digest                 → <nextRunAt>

The fleet is quiet-on-success: ops routines write a run report + a ledger Run-log row and DM Cooper only on hard failure; the CRM Ops Daily Digest (4:45pm CT) is the single daily ops surface. Framework live: customer_segment + company_sub_segment + signal modifiers + hs_is_target_account freeze + tier-compute-spec + signal_heat + flagged_for_deletion_reason on eviction.

Reply :white_check_mark: to acknowledge or flag any task that should be paused.
```

Replace `<nextRunAt>` placeholders with the actual ISO timestamps from `list_scheduled_tasks`. Replace `<today's date>` with the current date.

## Failure handling

| If this happens | Do this |
|---|---|
| `Read` returns "file not found" on a source path | STOP. Do not create/update the task with a placeholder. DM Cooper with the missing path. |
| `create_scheduled_task` returns "taskId already exists" | Switch to `update_scheduled_task` for that row and continue. |
| `update_scheduled_task` returns 4xx | Retry once. Still failing → DM Cooper with the exact error. |
| `list_scheduled_tasks` shows a task with stale `lastRunAt` and `nextRunAt` in the past after enable | Call `update_scheduled_task` again with the same `cronExpression` to force re-arm. |
| Any task ends up with `enabled: false` after Step 2 | Call `update_scheduled_task` with `enabled: true` explicitly. |
| Any unexpected error | STOP. Do not skip silently. DM Cooper with the row, the action attempted, and the error. |

## Done when

- All 9 scheduled tasks listed in Step 2 exist, are enabled, have the correct cron, and have a `nextRunAt` in the future.
- `smartlead-health-check` is unchanged.
- Slack DM sent to Cooper at `U0A24D9RJLS`.

— END PROMPT —
