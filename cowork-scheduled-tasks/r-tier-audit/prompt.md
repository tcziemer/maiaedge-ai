# R-Tier-Audit - Daily Tier + Signal Heat Drift Correction (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget, idempotent, stateless across runs. Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Daily, M-F 3:00 PM CT (changed 2026-05-21 from weekly per Cooper - daily cadence catches open-deal Hot transitions within 24h instead of 7 days). Cron: `0 15 * * 1-5` (local CT — Cowork's `create_scheduled_task` interprets cron in the user's local timezone, not UTC).
**Owner:** Cooper Kennedy (Slack DM: U0A24D9RJLS)
**Platform:** Cowork-only
**Apollo budget:** 0 (HubSpot reads + writes only; no web fetching)
**LLM cost:** Minimal (deterministic compute; can run on Haiku)
**Created:** 2026-05-14 (Phase 3 of Account Tiering & Segmentation Overhaul). Cadence: monthly → weekly 2026-05-14; weekly Fri → daily M-F 2026-05-21 per Cooper. Reframed as scheduled task (not routine) 2026-05-14. **`signal_heat` recompute added 2026-05-20** alongside tier — same inputs, same sweep, two outputs.

## What this scheduled task does

Daily drift correction sweep. Catches tier AND signal-heat drift across all active ICP accounts that other scheduled tasks (R1, R2, Signal Scan, R6) didn't touch since the previous run. Re-runs `compute_tier()` AND `compute_signal_heat()` over every active ICP record; applies tier changes only where current ≠ computed AND `hs_is_target_account ≠ true`; applies heat changes wherever current ≠ computed (heat is NOT frozen by `hs_is_target_account`). 10% circuit breaker pauses on anomalous mass-change (combined tier + heat count).

Pure HubSpot read/compute/write. No web research, no classification re-work - that's R2's job. R-Tier-Audit only corrects tier and heat drift driven by signal decay (stale +1, sustained quiet +1; heat dropping from warm to cool as 60d window slides; cool to cold as 180d window slides) and open-deal modifiers (-1 tier, push to heat hot) that other scheduled tasks missed.

**Why a scheduled task, not a routine:** R-Tier-Audit is intentionally simple. Each run reads HubSpot, computes tiers, writes deltas, writes an on-disk audit log + a ledger Run-log row (and pings Cooper ONLY on a hard failure / circuit-breaker pause), and exits. No persistent state, no cross-run agentic behavior, no orchestration. The Cowork scheduled-task primitive (cron-fired prompt) matches the design exactly; using the heavier Cowork "routine" abstraction adds machinery this task doesn't need.

**Why daily (was weekly):** Daily catches open-deal-driven heat transitions within 24h instead of the prior 7-day weekly lag. Task is Apollo-free + idempotent (no-op when computed_tier == current_tier AND computed_heat == current_heat), so daily-cadence cost is ~1 min HubSpot reads/writes. 10% circuit breaker (500 changes at 5K records) is loose enough that normal drift flows through; only catches catastrophic anomalies suggesting upstream routine bugs.

## Required reading at run start

Read these files in order BEFORE any HubSpot calls. The runtime MUST load them every run - caching is free, re-reading is cheap, wrong tier writes are expensive.

1. **`CLAUDE.md`** - repo conventions, inverted tier convention, Apollo budget, last_enriched_date stamping policy
2. **`context/account-tiering/tier-compute-spec.md`** - canonical compute_tier algorithm + defaults table + modifier table + null/unknown-pair fallbacks + manual override behavior
3. **`context/hubspot/property-schema.md`** Sections 2.5 (sub-segment), 3 (account_tier), 16 (network_op_track), 17 (signal persistence), 18 (hs_is_target_account)
4. **`context/hubspot/hubspot-values.md`** - case-sensitive internal values

## Operating principles (Cooper Feedback 2026-05-14)

1. **No-default-manual-review.** R-Tier-Audit doesn't classify. It tier + heat only.
2. **Honor `hs_is_target_account = true` for tier ONLY.** Freezes `account_tier`. Does NOT freeze `signal_heat` - heat always reports the truth. Skip tier write on target-account records but still recompute + write heat.
3. **Idempotent.** If `computed_tier == current_tier` AND `computed_heat == current_heat`, no-op. Running R-Tier-Audit twice in a row produces the same end state.
4. **10% circuit breaker.** If projected (tier_changes + heat_changes) > 10% of total active accounts, PAUSE and ask Cooper.

## Workflow

### Phase 1 - Read all active ICP accounts

Query HubSpot for all companies where:

```
customer_segment IN (
  "NeoCloud",
  "Data Center Colo Provider",
  "Fiber Operator",
  "Network Operator(Tier 1 / VNO)",
  "MSP/Aggregator",
  "Enterprise-CustomerSegment"
)
AND type != "Customer"
```

Read these properties per record:
- `customer_segment`, `company_sub_segment`
- `segmentation_confidence`
- `account_tier`
- `signal_heat`
- `hs_is_target_account`
- `last_signal_score`, `last_signal_date`, `signal_count_last_30d`
- Associated deals (count of deals past `appointmentscheduled` not in `closedwon` / `closedlost`)
- Last engagement date (most recent activity per HubSpot)

Expected: ~2,700 active ICP records (post-migration 2026-05-13).

### Phase 2 - Compute target tier per spec

For each account, apply the `compute_tier()` algorithm from `context/account-tiering/tier-compute-spec.md` inline:

1. **Step A0 - Pre-classification disqualifier guard.** Skip if `customer_segment` is not in the 6 ICPs (shouldn't happen since Phase 1 filter excludes them, but defensive).
2. **Step A - Manual override.** If `hs_is_target_account = true`, return current `account_tier` with reason "Manual override locked". Mark this record as `skipped_target_account` in the dry-run report.
3. **Step B - Defaults lookup.** Find `(customer_segment, company_sub_segment)` in the canonical defaults table (§5 of tier-compute-spec). Get `starting_tier`, `ceiling`, `floor`.
4. **Step C - Null + unknown-pair fallback.** If `company_sub_segment` null, use segment null fallback. If pair unknown (e.g., Mapletree on MSP/Aggregator parent with colo sub-segment), use segment null fallback + log warning.
5. **Step D - Apply signal modifiers in order:**
   - Hot signal (score 27-44 in last 60d): -1
   - White-hot signal (score >=45 in last 60d): -2 (caps at ceiling)
   - Stacked signals (signal_count_last_30d >= 2): -1 additional
   - Open deal past `appointmentscheduled` not closed-lost: -1
   - Stale signal (>90d AND no engagement <=30d): +1
   - Sustained quiet (>180d AND no engagement <=180d): +1 additional
6. **Step E - Clamp** to `[ceiling, floor]`.
7. **Step F - Build reason string** citing file 06 §6 or D5 protocol + modifiers applied.

Record per-account:
- `current_tier`
- `computed_tier`
- `delta` (new − old)
- `reason`
- `skipped_target_account` (boolean - tier write skipped on this record)
- `current_heat`
- `computed_heat`
- `heat_changed` (boolean)

### Phase 2b - Compute target signal heat per spec (added 2026-05-20)

For each account, also apply `compute_signal_heat()` from `context/account-tiering/tier-compute-spec.md` §11.5. **Freshness anchor (post-2026-05-28):** `last_signal_date` stores the EVENT DATE (when the news/funding/hire actually happened), not detection date. **HubSpot enum is Title Case:** `Hot` / `Warm` / `Cool` / `Cold`. Inlined here so this prompt is self-contained:

```
signal_heat is computed top-down, first match wins:

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Override behavior:
- hs_is_target_account = true does NOT freeze signal_heat.
  Tier is rep-locked; heat always reports the truth.

Inputs: last_signal_score, last_signal_date (event date), signal_count_last_30d, open-deal state.
Output: enum `Hot` | `Warm` | `Cool` | `Cold` (Title Case per HubSpot).
```

Heat compute runs on EVERY record in the active ICP pool, including `hs_is_target_account = true` records. Heat is NOT frozen by the target-account flag - tier is the only frozen output.

### Phase 3 - Circuit breaker check

Calculate: `change_count = sum(1 for r in records if (r.computed_tier != r.current_tier AND NOT r.skipped_target_account) OR r.computed_heat != r.current_heat)`. Heat changes count toward the threshold because mass heat drift would also indicate something is wrong (e.g., a system clock bug, a corrupt signal field).

If `change_count > 0.10 * total_active_accounts`:
1. PAUSE - do NOT write any tier changes.
2. Save full dry-run report to `weekly-reports/tier-audit/YYYY-MM-DD-DRY-RUN.md` with all proposed changes.
3. **The circuit-breaker pause is a hard-failure-class event - it pings Cooper** (per the Delivery rule in the "Output / Delivery" section below). Send the one-line failure ping to Cooper at `U0A24D9RJLS`:

   ```
   :red_circle: R-Tier-Audit PAUSED - circuit breaker tripped at <X.X>% > 10% (would change <N> of <total>). Dry-run at weekly-reports/tier-audit/YYYY-MM-DD-DRY-RUN.md; reply :white_check_mark: to approve or :x: to abort.
   ```

   Retry the ping once (1s → 2s). Also append a ⚠️ Run-log row to canvas `F0B0AFSB9LN` noting the pause + dry-run path.
4. Stop execution. Wait for Cooper's response.

### Phase 4 - Apply tier + heat changes

If circuit breaker passes:

For each account where `computed_tier != current_tier AND NOT hs_is_target_account`:

1. Write new `account_tier` via HubSpot MCP (`manage_crm_objects` updating the company record).
2. Add HubSpot company note: `"Tier <X> -> <Y> on YYYY-MM-DD by R-Tier-Audit: <reason>"`.
3. Log every change to `weekly-reports/tier-audit/YYYY-MM-DD-tier-audit.md`:

For each account where `computed_heat != current_heat` (REGARDLESS of `hs_is_target_account`):

1. Write new `signal_heat` via HubSpot MCP. Heat writes are NOT gated on the target-account flag - heat tells the truth even on rep-pinned accounts.
2. Add HubSpot company note: `"Heat <X> -> <Y> on YYYY-MM-DD by R-Tier-Audit: <reason citing the trigger>"`. Reasons typical at this routine: `"last_signal_date crossed 60d boundary, no stack, no open deal -> warm to cool"`, `"last_signal_date crossed 180d boundary -> cool to cold"`, `"new open deal past appointmentscheduled detected -> warm to hot"`.
3. Log heat changes to the same audit file as tier changes (separate table below).

Then continue:

   ```markdown
   ## R-Tier-Audit YYYY-MM-DD

   - Total active accounts reviewed: N
   - Tier changes written: M
   - Heat changes written: H
   - Manual override skips (tier writes only): K
   - Heat writes on target-account records (not skipped): T
   - Circuit breaker triggered: NO (or YES)

   ### Per-record tier changes

   | Company ID | Domain | Segment | Sub-segment | Old | New | Delta | Reason |
   |---|---|---|---|---|---|---|---|
   | ... | ... | ... | ... | ... | ... | ... | ... |

   ### Per-record heat changes

   | Company ID | Domain | Old Heat | New Heat | Reason |
   |---|---|---|---|---|
   | ... | ... | ... | ... | ... |
   ```

4. **Do NOT bump `last_enriched_date`.** Per CLAUDE.md Unified Stamping Policy, R-Tier-Audit tier AND heat writes do not bump `last_enriched_date`. R2's 120-day rotation owns that.

### Phase 5 - Run summary (on-disk + ledger, NO success DM)

**Delivery - quiet on success, ping only on hard failure.** Do NOT DM Cooper a per-run debrief. On a clean run (including a no-op run where nothing drifted), the full record is: (1) the on-disk audit log at `weekly-reports/tier-audit/YYYY-MM-DD-tier-audit.md` (the summary block below is written into that report, NOT sent as a DM), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's tier + heat changes from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack MCP unreachable, an abort, OR the 10% circuit-breaker pause (handled in Phase 3 above) - as ONE line:

`:red_circle: R-Tier-Audit [FAILED/ABORTED/PAUSED] - [one-clause reason].`

(The circuit-breaker pause uses the PAUSED variant per Phase 3.) Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk audit log + Run-log row are the fallback.

Write this summary block into the on-disk audit log (`weekly-reports/tier-audit/YYYY-MM-DD-tier-audit.md`), appended after the per-record change tables:

```
R-Tier-Audit - YYYY-MM-DD (daily M-F)

Total active accounts reviewed: <N>

Tier changes written: <M>
  Promotions (lower tier number, toward Tier 1): <P>
  Demotions (higher tier number, toward Tier 5): <D>

Heat changes written: <H>
  Hot/Warm -> cooler: <HD>
  Cool/Cold -> hotter: <HU>
  Heat writes on target-account records (not skipped): <HT>

Heat distribution after this run (across all active ICP):
  :red_circle: Hot: <h>
  :large_orange_circle: Warm: <w>
  :large_yellow_circle: Cool: <c>
  :white_circle: Cold: <k>

Manual override skips (hs_is_target_account=true, tier only): <K>
Stale signals decayed (+1 tier): <S>
Sustained quiet decayed (+1 tier additional): <Q>
Open-deal promotions (-1 tier): <O>

Top 10 tier changes by delta:
1. <Company> (<segment>): T<X> -> T<Y> -- <reason>
2. ...

Top 10 heat changes:
1. <Company> (<segment>): <old> -> <new> -- <reason>
2. ...

Unknown (segment, sub-segment) pair warnings: <U>
  (records using segment null fallback per tier-compute-spec §6)

Next run: <next M-F 3pm CT>
```

**Ledger Run-log append (every run, success or failure):** append ONE row to the "Run log" table on canvas `F0B0AFSB9LN` via `slack_update_canvas`:

`| YYYY-MM-DD | R-Tier-Audit | <status emoji> | <one-sentence summary: M tier + H heat changes> | weekly-reports/tier-audit/YYYY-MM-DD-tier-audit.md |`

Status emojis: ✅ success · ⚠️ partial (or circuit-breaker pause) · ❌ failed · ⏭ skipped. This row is what the CRM Ops Daily Digest reads to surface the run; it is the durable cross-task record alongside the on-disk audit log.

## Quality checks at end of run

Before finalizing the on-disk audit log + Run-log row, R-Tier-Audit self-validates:

1. **All eligible records processed.** Phase 1 record count == Phase 4 record count + skip count.
2. **No tier writes with `hs_is_target_account=true`.** Manual overrides honored 100%.
3. **All writes have HubSpot notes.** Audit trail per record.
4. **Circuit breaker threshold == 10%.** Computed correctly against total active ICP records.
5. **Local audit log persisted.** This file is the durable record the CRM Ops Daily Digest reads from.

If any check fails, write a warning to the audit log (and, if it rises to a hard failure, fire the failure ping per Phase 5) but proceed with writes that did succeed.

## Reliability mechanisms

- **Circuit breaker (10%)** prevents runaway changes.
- **`hs_is_target_account = true` respected** - manual overrides honored.
- **Every change writes a HubSpot note** for audit trail.
- **Local file backup** at `weekly-reports/tier-audit/YYYY-MM-DD-tier-audit.md`.
- **Idempotent:** running twice in a row produces same end state.
- **No Apollo, no web research** - pure HubSpot compute. Cheap to run, cheap to retry.
- **Does NOT classify.** Does NOT touch `customer_segment`, `company_sub_segment`, or any enriched field. Only `account_tier`.

## Coordination with other routines

Order of operations on a single account across a typical week:

```
M-F daily   R0/R1/R2 enrich + classify; R1/R2 write tier at Stage 4 per compute_tier
Mon 1pm     Weekly Signal Scan Stage 5b writes 3 signal persistence fields + recomputes tier
M-F daily   R6 (next day) applies open-deal modifier + recomputes tier if changed
M-F 3pm     R-Tier-Audit (daily) - catches drift from the day's R0/R1/R2/R6 + Signal Scan writes. Heat decay boundaries (60d / 180d) cross daily, so daily cadence catches them within 24h. Clean tiers + fresh heat go into next-day's routines.
Weekly      D7 Edge Case Resolution - re-classifies stale records; if sub-segment changes, recomputes tier
```

If R6 just wrote `tier_2` and R-Tier-Audit computes the same `tier_2`, no second write happens (no-op).

## Known data quality flags (per CLAUDE.md)

5 records have `(customer_segment, company_sub_segment)` pairs not in the canonical defaults table (Mapletree, Montera Infrastructure, PTS Data Center Solutions, Lonestar Data Holdings, LS Power on MSP/Aggregator parent with colo sub-segment values). R-Tier-Audit applies the segment null fallback (MSP/Aggregator: T2, ceiling 1, floor 4) and logs a warning. Cooper's data-quality follow-up will reclassify these eventually.

## Failure handling

- HubSpot MCP rate limit / 5xx: retry with exponential backoff (1s, 2s, 5s, 10s). After 3 retries, write to `failed-writes-YYYY-MM-DD.md` and continue with remaining records.
- Failure ping send fails: retry once (1s → 2s), then write a local error log + the ❌/⚠️ Run-log row and continue. The disk audit log + Run-log row are the fallback record.
- Cooper not responding to circuit breaker pause: routine stays paused. Next Sunday's run will redo the dry-run (idempotent).

---

**End of R-Tier-Audit prompt.** Tier-only writes; honors manual overrides; circuit-breaker gated; pure HubSpot compute. Apollo budget 0.
