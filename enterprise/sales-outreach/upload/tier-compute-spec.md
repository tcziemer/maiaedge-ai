# Tier + Signal Heat Compute Specification (`compute_tier` + `compute_signal_heat`)

**Status:** Canonical. Single source of truth for BOTH `account_tier` and `signal_heat` computation. Effective 2026-05-14 (Phase 3 of Account Tiering & Segmentation Overhaul); `signal_heat` added 2026-05-20; **Signal Engine Unification 2026-05-28** narrowed `last_signal_date` semantics to event date (was detection date) and corrected `signal_heat` enum case to Title Case.
**Supersedes:** Per-segment "Account Tiering" tables previously inlined in `context/core/icp-playbook.md`, `context/core/segment-qualification.md`, and the segment cheatsheets in `context/segments/`.

This file specifies **two computed outputs** that share the same input fields:

- **`account_tier`** - strategic value (segment-anchored, floor/ceiling clamped). Inverted convention: Tier 1 = highest priority. Frozen by `hs_is_target_account = true`.
- **`signal_heat`** - current intent (decays automatically as the event date window slides). 4-bucket enum: `Hot` / `Warm` / `Cool` / `Cold` (Title Case, per HubSpot). **NOT frozen** by `hs_is_target_account` - tier is rep-locked; heat always reports the truth.

Every routine that writes `account_tier` (R1 Fresh Enrichment, R2 Stale Re-Enrichment, Weekly Signal Scan Stage 5b, R6 Territory & Hygiene, R-Tier-Audit, D7 Edge Case Resolution) MUST inline this logic. The routines that touch signal fields ALSO write `signal_heat` from the same inputs - never one without the other. Do not re-invent. **The 5 outreach skills** (cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline) also write signal fields + heat + tier as the absolute final step of their workflow when research surfaces a fresher event than what's in HubSpot — see CLAUDE.md "Signal Engine Unification" for the push-back pattern.

## 1. Inverted tier convention

Tier 1 = HIGHEST priority (white-glove rep weekly attention). Tier 5 = LOWEST (mass outreach / nurture). Lower number = more priority. A "+1 tier promotion" in human-readable copy means "tier number goes DOWN by 1." This spec uses arithmetic - `-1` means tier number decreases (more priority); `+1` means tier number increases (less priority).

## 2. Operating principles (Cooper feedback 2026-05-14)

1. **No-default-manual-review.** Classification routes to a sub-segment (best-fit + tiebreaker) OR `Flagged for deletion`. `manual_review_required` is the LAST resort, not the default. Target: manual_review population <5% of records.
2. **Multi-marker classification.** `infrastructure_profile` (multi-select bands for Facilities / Route Miles / POPs) is the PRIMARY structured signal. When `annualrevenue` conflicts with `infrastructure_profile`, `infrastructure_profile` wins. Revenue data is dirty more often than infrastructure.
3. **Read from 8 enriched fields, not HubSpot defaults.** `account_brief`, `geographic_focus`, `infrastructure_profile`, `hyperscaler_proximity`, `fabric_provisioning_approach`, `provisioning_landscape`, `recent_news_or_trigger_event`, `last_enriched_date`. HubSpot `description` and `industry` are last-resort only. (The signal persistence fields `last_signal_date` / `last_signal_score` / `signal_count_last_30d` + `signal_heat` are signal-engine fields, not enriched-fields — read by `compute_tier` + `compute_signal_heat` but not narrated.)
4. **Conciseness cap 2-4 sentences** on narrative enriched fields. At thousands-of-records scale, brevity beats completeness.
5. **`maiaedge_value_proposition` is NOT in enrichment scope.** Outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) populate this field on-demand at outreach time.
6. **Manual override `hs_is_target_account = true` freezes `account_tier` ONLY.** Segment, sub-segment, signal field, and enriched field writes ALL proceed normally.

## 3. Function signature

```
compute_tier(account) -> {new_tier: str, reason: str}
```

### Inputs (read from HubSpot company record + associated objects)

- `customer_segment` (string)
- `company_sub_segment` (string)
- `segmentation_confidence` (string, optional)
- `last_signal_score` (numeric, optional)
- `last_signal_date` (date, optional) — **primary freshness anchor** for hot/white-hot/stale/sustained-quiet modifiers. Semantics narrowed 2026-05-28 to event date (date the event happened), not the engine's run/detection date.
- `signal_count_last_30d` (numeric, optional) — counts events with `last_signal_date` (event date) in trailing 30d
- `network_op_track` (enum, optional - informational, does not affect tier)
- `hs_is_target_account` (boolean)
- `account_tier` (string, current value)
- Associated deals (via association lookup - count of deals past `appointmentscheduled`, not closed-lost)
- Engagement history (most recent engagement date)

### Outputs

- `new_tier` - one of `tier_1`, `tier_2`, `tier_3`, `tier_4`, `tier_5`
- `reason` - one-line audit string citing the file 06 / D5 rule that fired

## 4. Algorithm

### Step A0 - Pre-classification disqualifier guard

If `customer_segment` is NOT in the 6 active ICP segments (i.e., is `Other`, `Unknown`, `Flagged for deletion`, or `Partner Target`), return without modification - `compute_tier` only applies to active ICP segments. The full D1 global disqualifier evaluation (`context/account-tiering/sub-segment-qualification-full.md` §3 / `context/account-tiering/d1-global-disqualifiers.md`) runs INSIDE R1/R2/Signal Scan BEFORE the record is assigned to an ICP segment. If a record reaches `compute_tier` with a hyperscaler / equipment-vendor signature still on it, the calling routine missed D1 earlier - `compute_tier` does not re-litigate, it guards.

### Step A - Manual override

If `hs_is_target_account = true`:
- Return `{new_tier: <current account_tier>, reason: "Manual override locked via hs_is_target_account=true"}`.
- STOP tier compute.
- Calling routine still writes segment / sub-segment / signal / enriched fields normally.

### Step B - Defaults lookup

Look up `(customer_segment, company_sub_segment)` in the canonical defaults table (§5). Get `starting_tier`, `ceiling`, `floor`.

### Step C - Null + unknown-pair fallback

- If `company_sub_segment` is null or empty: use the segment's null fallback (§6).
- If `(customer_segment, company_sub_segment)` is not in the defaults table: use the segment's null fallback AND log warning `"Unknown (segment, sub-segment) pair: <X>, <Y>. Using null fallback for segment <X>."`. Do NOT throw.

### Step D - Signal modifiers (additive, applied in order)

Apply the modifiers in §7 in this order: hot signal -> white-hot signal (caps at ceiling) -> stacked signals -> open deal -> stale signal -> sustained quiet. Each modifier produces a `delta` that adjusts the running tier number.

### Step E - Clamp

Clamp the running tier to `[ceiling, floor]` inclusive. Ceiling = smallest allowed tier number (highest priority). Floor = largest allowed tier number (lowest priority).

### Step F - Build reason string

Concatenate the modifiers that applied with rule citations:
```
"Default <segment>/<sub-segment> = T<starting>, <modifier list> = T<final>. <file 06 §X.Y / D5 protocol ID>"
```

### Step G - Return

```
{new_tier: "tier_" + clamped_value, reason: reason_string}
```

## 5. Canonical defaults table

This is the authoritative truth. Encoded identically in `context/hubspot/property-schema.md` Section 3 and `context/hubspot/hubspot-values.md`. Internal values are CASE-SENSITIVE.

| Segment | Sub-segment (HubSpot internal value) | Default | Ceiling | Floor |
|---|---|---:|---:|---:|
| `Network Operator(Tier 1 / VNO)` | `Tier 1 Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Pure Wholesale Carrier - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Cable MSO Enterprise Division - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `International Backbone Specialist - Network Op` | 1 | 1 | 2 |
| `Network Operator(Tier 1 / VNO)` | `Subsea cable operator` | 2 | 1 | 3 |
| `Data Center Colo Provider` | `AI Signals - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Standard - colo` | 3 | 1 | 5 |
| `Data Center Colo Provider` | `Modular - colo` | 1 | 1 | 3 |
| `Data Center Colo Provider` | `Hyperscale Wholesale - colo` | 1 | 1 | 3 |
| `NeoCloud` | `Large Scale GPU - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Sovereign AI Clouds - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Tier 1 Inference - Neocloud` | 2 | 1 | 2 |
| `NeoCloud` | `AI Infrastructure providers - Neocloud` | 1 | 1 | 2 |
| `NeoCloud` | `Crypto to AI - Neoclouds` | 1 | 1 | 2 |
| `Fiber Operator` | `Tier 2 National Wholesale - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Long Haul / Backbone - Fiber operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Dark Fiber Specialist - Fiber Operator` | 2 | 1 | 3 |
| `Fiber Operator` | `Regional CLEC - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Regional Cable Operator - Fiber operator` | 3 | 1 | 4 |
| `Fiber Operator` | `Municipal / Cooperative - Fiber operator` | 4 | 2 | 5 |
| `MSP/Aggregator` | `Telecom Aggregator - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `Managed Network Services - MSP` | 2 | 1 | 4 |
| `MSP/Aggregator` | `TSD Technology Services Distributor - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Master Agent - MSP` | 3 | 1 | 5 |
| `MSP/Aggregator` | `Cloud + Telecom Hybrid MSP - MSP` | 2 | 1 | 4 |
| `Enterprise-CustomerSegment` | `Financial Services - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Healthcare Systems - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Retail and Distribution - Enterprise` | 3 | 2 | 4 |
| `Enterprise-CustomerSegment` | `Outsourcing Services - Enterprise` | 3 | 2 | 4 |
| `Data Center Colo Provider` OR `NeoCloud` | `Greenfield` | 2 | 1 | 3 |

### Case-sensitivity quirks (verified via HubSpot MCP 2026-05-14)

- `Dark Fiber Specialist - Fiber Operator` - capital "O" in `Operator` (every other Fiber sub-segment uses lowercase "o" in `operator`).
- `AI Infrastructure providers - Neocloud` - lowercase "p" in `providers`.
- `Crypto to AI - Neoclouds` - trailing "s" on `Neoclouds`.
- `Network Operator(Tier 1 / VNO)` - no space before the open paren.
- `Subsea cable operator` - lowercase `c` and `o`; NO `- Network Op` suffix despite sitting under Network Operator parent.
- `Managed Network Services - MSP` - `- MSP` suffix post-Phase 1.7c.1 (`- Network Operator` archived).
- `Greenfield` - pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` customer_segment parent.

## 6. Null sub-segment fallbacks

When `company_sub_segment` is null OR the `(segment, sub-segment)` pair is unknown:

| Segment | Null fallback (starting_tier, ceiling, floor) |
|---|---|
| `NeoCloud` | T2 (1, 2) |
| `Fiber Operator` | T3 (1, 4) |
| `Data Center Colo Provider` | T3 (1, 5) - Standard fallback |
| `Network Operator(Tier 1 / VNO)` | T1 (1, 2) |
| `MSP/Aggregator` | T2 (1, 4) |
| `Enterprise-CustomerSegment` | T3 (2, 4) |

For unknown `(segment, sub-segment)` pairs (5 known records as of Phase 2 audit - Mapletree, Montera, PTS, Lonestar, LS Power on MSP/Aggregator parent with colo sub-segment values), apply the segment's null fallback and log warning.

## 7. Signal modifiers (additive, applied in order)

Modifiers stack but cannot exceed ceiling or fall below floor.

| Modifier | Delta | Source field(s) | Evaluated by |
|---|---:|---|---|
| Hot signal score 27-44 with event in last 60d | -1 (toward Tier 1) | `last_signal_score` 27-44 AND `last_signal_date` <= 60d | Signal Scan + outreach push-back |
| White-hot signal score >=45 with event in last 60d | -2 (capped at ceiling) | `last_signal_score` >= 45 AND `last_signal_date` <= 60d | Signal Scan + outreach push-back |
| Stacked signals (2+ events scoring >=8 in trailing 30d) | -1 additional | `signal_count_last_30d` >= 2 | Signal Scan + outreach push-back |
| Open deal past `appointmentscheduled` | -1 | Association lookup: any deal not in {`closedwon`, `closedlost`} past `appointmentscheduled` | R6 Territory & Hygiene |
| Stale signal (event >90d ago) AND no rep activity <=30d | +1 (toward Tier 5) | `last_signal_date` > 90d AND no engagement <=30d | R-Tier-Audit, R6 |
| Sustained quiet (event >180d ago AND no activity <=180d) | +1 additional | `last_signal_date` > 180d AND no engagement <=180d | R-Tier-Audit |

Order: hot -> white-hot -> stacked -> open deal -> stale -> sustained quiet.

**Freshness anchor:** all date-bounded modifiers key off `last_signal_date`, which as of 2026-05-28 stores the **event date** — the date the news/funding/hire actually happened, not the engine's run/detection date. Semantically: a 6-month-old funding round caught by Signal Scan today is not hot — the event itself is stale. The semantic shift was on the same field; no new property was created.

## 8. Manual override (`hs_is_target_account = true`)

Freezes `account_tier` ONLY. Specifically:

- All routines READ tier for reports / briefings normally.
- `compute_tier` exits at Step A and returns the current `account_tier`.
- The calling routine STILL writes `customer_segment`, `company_sub_segment`, `segmentation_confidence`, all 8 enriched fields (account_brief / geographic_focus / infrastructure_profile / hyperscaler_proximity / fabric_provisioning_approach / provisioning_landscape / recent_news_or_trigger_event / last_enriched_date), and the 3 signal persistence fields (`last_signal_score`, `last_signal_date`, `signal_count_last_30d`). It also STILL writes `signal_heat` — heat is NOT frozen by the target-account flag.
- When the rep clears `hs_is_target_account = false`, the next routine touch resumes algorithmic tier control.

**Implementation rule:** every routine reads `hs_is_target_account` BEFORE the `account_tier` write step. If true, skip the tier write and log skip reason. All other field writes proceed.

## 9. Worked examples

### Example 1 - Tier 1 Carrier, no signals
- Account: AT&T. `customer_segment = "Network Operator(Tier 1 / VNO)"`, `company_sub_segment = "Tier 1 Carrier - Network Op"`. No `hs_is_target_account` flag. No signals in last 60d.
- Step B lookup: default 1, ceiling 1, floor 2.
- No modifiers fire.
- Clamp: 1 is within [1, 2].
- Output: `{new_tier: "tier_1", reason: "Default Network Operator(Tier 1 / VNO)/Tier 1 Carrier - Network Op = T1. file 06 §6.1"}`

### Example 2 - Sovereign AI Neocloud with white-hot signal
- Account: Nscale. Default `Sovereign AI Clouds - Neocloud` = T1. `last_signal_date` (event) = 10 days ago ($14.6B valuation funding round, score 50).
- Step B: default 1, ceiling 1, floor 2.
- Step D: white-hot signal -2 (score 50 ≥ 45 AND event 10d ago ≤ 60d), but cap at ceiling 1. Net delta = 0.
- Output: `{new_tier: "tier_1", reason: "Default NeoCloud/Sovereign AI Clouds - Neocloud = T1, white-hot signal -2 capped at ceiling = T1. file 06 §6.4"}`
- Heat: `Hot` (score ≥45 AND event ≤60d).

### Example 3 - Standard colo with stale signal + sustained quiet
- Account: mid-market Standard - colo. Default T3, ceiling 1, floor 5. `last_signal_date` (event) = 240 days ago. No engagement in 200 days.
- Step D: hot/white-hot/stacked/open-deal don't fire. Stale +1 fires (event 240d > 90d, no rep activity). Sustained quiet +1 fires (event >180d, no activity >180d). Running tier: 3 + 1 + 1 = 5.
- Clamp: 5 within [1, 5].
- Output: `{new_tier: "tier_5", reason: "Default Data Center Colo Provider/Standard - colo = T3, stale +1, sustained quiet +1 = T5. file 06 §6.3"}`
- Heat: `Cold` (event >180d).

### Example 4 - Master Agent with thin anchor evidence
- Account: a Master Agent independent. Default T3, ceiling 1, floor 5.
- No signal activity.
- Output: `{new_tier: "tier_3", reason: "Default MSP/Aggregator/Master Agent - MSP = T3. file 06 §6.5"}`

### Example 5 - Greenfield colo + hot signal
- Account: announced AI campus build, Series B funded. `customer_segment = "Data Center Colo Provider"`, `company_sub_segment = "Greenfield"`. Default T2, ceiling 1, floor 3. Funding announcement signal score 30, `last_signal_date` (event) = 20 days ago.
- Step D: hot signal -1 (score 27-44 AND event ≤60d). Running tier: 2 - 1 = 1.
- Clamp: 1 within [1, 3].
- Output: `{new_tier: "tier_1", reason: "Default Data Center Colo Provider/Greenfield = T2, hot signal -1 = T1. file 06 §6.7 / D5 protocol G"}`
- Heat: `Warm` (score 27-44 AND event ≤60d).

### Example 6 - `hs_is_target_account = true` freeze
- Account: international wholesale arm, `hs_is_target_account = true`, current `account_tier = tier_1`, segment shifted from null to `Tier 1 Carrier - Network Op` this run.
- Step A: `hs_is_target_account = true`, return current tier_1 with reason "Manual override locked".
- Output: `{new_tier: "tier_1", reason: "Manual override locked via hs_is_target_account=true"}`
- Calling routine STILL writes `customer_segment`, `company_sub_segment`, and all enriched fields.

### Example 7 - Enterprise Financial Services, no trigger
- Account: JPMorgan. Default `Financial Services - Enterprise` = T3, ceiling 2, floor 4. No signals in 90d. Open deal past `appointmentscheduled` exists.
- Step D: open deal -1. Running tier: 3 - 1 = 2.
- Clamp: 2 within [2, 4].
- Output: `{new_tier: "tier_2", reason: "Default Enterprise-CustomerSegment/Financial Services - Enterprise = T3, open deal -1 = T2. file 06 §6.6"}`

### Example 8 - Crypto to AI - Neoclouds (inclusive, operator OR landlord)
- Account: IREN. Default T1, ceiling 1, floor 2. Microsoft $9.7B landlord deal (white-hot, `last_signal_date` (event) = 45 days ago).
- Step D: white-hot -2 (score ≥45 AND event ≤60d) capped at ceiling 1.
- Output: `{new_tier: "tier_1", reason: "Default NeoCloud/Crypto to AI - Neoclouds = T1, white-hot signal -2 capped at ceiling = T1. file 06 §6.4 (Cooper 2026-05-14: Crypto to AI is inclusive of operator AND landlord)"}`
- Heat: `Hot` (score ≥45 AND event ≤60d).

### Example 9 - Unknown pair fallback
- Account: Mapletree. `customer_segment = "MSP/Aggregator"`, `company_sub_segment = "Standard - colo"` (data quality issue from prior schema). Not in defaults table.
- Step C: use MSP/Aggregator null fallback (T2, ceiling 1, floor 4). Log warning.
- No modifiers fire.
- Output: `{new_tier: "tier_2", reason: "Unknown (segment, sub-segment) pair: MSP/Aggregator, Standard - colo. Using MSP/Aggregator null fallback = T2. file 06 §10.1"}`

### Example 10 - Subsea cable operator
- Account: Seaborn Networks. Default `Subsea cable operator` = T2, ceiling 1, floor 3. No signals.
- Output: `{new_tier: "tier_2", reason: "Default Network Operator(Tier 1 / VNO)/Subsea cable operator = T2. file 06 §6.1 (new sub-segment 2026-05-14)"}`

## 10. Audit log format

Every tier change produces a HubSpot company note in this format:

```
Tier <old> -> <new> on <ISO date> by <routine_name>: <reason citing file 06 §X.Y or D5 protocol ID>
```

Examples:
- `"Tier 3 -> 2 on 2026-05-14 by Weekly Signal Scan: Default Standard - colo = T3, hot signal -1 = T2. file 06 §6.3"`
- `"Tier 1 -> 1 (no change) on 2026-05-14 by R1 Fresh Enrichment: Manual override locked via hs_is_target_account=true"`

If `new_tier == current account_tier`, no HubSpot write happens (idempotent no-op). Audit notes are only written when the tier actually changes.

## 11. Routine + skill routing table

Every routine and skill that writes tier reads from this spec and inlines the algorithm:

| Surface | When `compute_tier` runs |
|---|---|
| R1 Fresh Enrichment (Cowork) | Stage 4 - after Stage 3 sub-segment classification |
| R2 Stale Re-Enrichment (Cowork) | Stage 4 - on every FULL pass; on every LIGHT pass if segment / sub-segment changes |
| Weekly Signal Scan (Cowork) | Stage 5b - after writing the 3 signal persistence fields (`last_signal_date` event date + `last_signal_score` + `signal_count_last_30d`) |
| R6 Territory & Hygiene (Claude Code) | Tier maintenance step - after territory + hygiene writes, only for accounts touched in this run |
| R-Tier-Audit (Cowork) | Daily M-F drift correction sweep at 3pm CT over all active ICP records - 10% circuit breaker. Cadence widened from monthly → weekly → daily 2026-05-14 → 2026-05-21 per Cooper. |
| D7 Edge Case Resolution (Cowork) | On PASS resolution after sub-segment upgrade |
| **5 outreach skill push-backs** (cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline) | **Absolute final step** of the skill, AFTER primary output delivered, only when research surfaces an event with `last_signal_date` (event date) strictly newer than the HubSpot value. Push-back failures never block primary output. `call-prep` excluded per Cooper 2026-05-28. |

`compute_tier` is idempotent - if R6 just wrote tier_2 and Signal Scan computes the same tier_2, no second write happens. Outreach push-backs share the same idempotency: if the rep's research finds the same event already in HubSpot, no write.

## 11.5 Signal Heat Computation (`compute_signal_heat`)

**Status:** Canonical. Added 2026-05-20 alongside the HubSpot `signal_heat` property creation. **2026-05-28 update:** `last_signal_date` semantics narrowed to event date (was detection date); enum case corrected to Title Case to match HubSpot. Field set finalized at 5 signal-engine properties (see §11.6 below).

`signal_heat` is the 4-bucket rep-facing rollup of signal score + event recency + deal context that reps sort by daily. It is **orthogonal to `account_tier`**: tier is segment-anchored strategic value (clamped by floor/ceiling); heat is current intent (decays automatically as the event date window slides). Same inputs, different outputs, both written at the same time.

### Compute logic (top-down, first match wins)

```
signal_heat is computed top-down, first match wins:

Hot   IF (last_signal_score >= 45 AND last_signal_date <= 60 days ago)
       OR signal_count_last_30d >= 2
       OR account has any associated open deal past `appointmentscheduled`

Warm  IF last_signal_score 27-44 AND last_signal_date <= 60 days ago

Cool  IF last_signal_date <= 180 days ago AND not already Hot/Warm
       (catches: low-score signals with events in last 60d; any event 60-180d old
        that's no longer fresh enough for Hot/Warm)

Cold  IF last_signal_date > 180 days ago OR last_signal_date IS NULL

Override behavior:
- hs_is_target_account = true does NOT freeze signal_heat.
  Tier is rep-locked; heat always reports the truth.

Inputs read from HubSpot:
- last_signal_score (number)
- last_signal_date (date) -- EVENT DATE (semantics narrowed 2026-05-28)
- signal_count_last_30d (number)
- deal pipeline state (any associated deal past `appointmentscheduled` = TRUE)

Computed alongside account_tier - both share the same input fields.
Output: enum `Hot` | `Warm` | `Cool` | `Cold` (Title Case per HubSpot).
```

### Inputs (identical to `compute_tier` modifier inputs)

- `last_signal_score` (number)
- `last_signal_date` (date) — **primary freshness anchor**; semantics narrowed to event date 2026-05-28 (was detection date)
- `signal_count_last_30d` (number)
- Associated deals (any deal past `appointmentscheduled` not in {`closedwon`, `closedlost`} = open-deal TRUE)

### Output

- `signal_heat` (enum: `Hot` | `Warm` | `Cool` | `Cold` — Title Case per HubSpot)

### Override behavior

`hs_is_target_account = true` does NOT freeze `signal_heat`. Tier is rep-locked (per Step A above); heat always reports the truth. Reps may pin an account at Tier 1 strategically, but if the signal date is 200 days old that account is still `cold` - the rep needs to see that.

### Heat is recomputed by the same routines that update signal fields

The source-of-truth for current heat is the most recent routine pass. Routines + skills that write `signal_heat`:

| Surface | When | Default for new accounts |
|---|---|---|
| Weekly Signal Scan Stage 5b | After writing `last_signal_date` (event date) + the 2 other persistence fields + the narrative | `Cold` initialized to `Cold` then recomputed if events fired |
| R-Tier-Audit (daily M-F) | Same drift sweep as tier (no-op if `computed_heat == current_heat`) | n/a |
| R1 Fresh Enrichment Path α | Stage 5 write block, new accounts | `signal_heat = Cold` (no signal history yet) |
| R2 Stale Re-Enrichment RE_ENRICH_FULL | Stage 4/5 alongside tier recompute | n/a |
| R0 Import Validator | MATCH path if record is new to active pool | `signal_heat = Cold` |
| R6 Territory & Hygiene | Step 5.5 alongside tier maintenance | n/a |
| **5 outreach skill push-backs** (cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline) | **Absolute final step** of the skill, AFTER primary output delivered, only when research surfaces an event with a `last_signal_date` strictly newer than the HubSpot value. `call-prep` excluded. | n/a (push-back runs against existing accounts) |

### Rationale: tier vs heat

Tier = segment-anchored strategic value, clamped by floor/ceiling. A Tier 1 Carrier is Tier 1 whether the signals are hot or quiet - the strategic value of the account doesn't change.

Heat = current intent, decays automatically as the signal date window slides. Same Tier 1 Carrier may be `hot` this week and `cool` in 90 days without any rep action - that's the design. Reps sort their daily pipeline by heat to find the accounts with workable intent right now; they review their strategic accounts (high tier) on a slower cadence.

Same inputs, different outputs, both written same time. Routines that already read `last_signal_score`, `last_signal_date`, `signal_count_last_30d`, and open-deal state for tier modifiers compute heat with the same fields - it's one extra write per account, not a separate research pass.

### Heat-only recomputes do NOT bump `last_enriched_date`

Same rule as tier-only writes from R-Tier-Audit (per CLAUDE.md Unified Stamping Policy). `last_enriched_date` reflects full-pipeline passes only. Heat is a partial-write extension that runs alongside tier in every routine that writes tier; neither bumps the enrichment date.

### The 5-field signal engine (canonical inventory, locked 2026-05-28)

This is the **complete** set of HubSpot company fields that constitute the signal engine. No other signal-related fields exist; do not add new ones without an explicit redesign turn.

| # | Field | Type | Role | Who writes |
|---|---|---|---|---|
| 1 | `recent_news_or_trigger_event` | Text (≤250 char) | Narrative — what happened | Signal Scan Stage 5, R1/R2/D7, 5 outreach push-backs |
| 2 | `last_signal_date` | Date (YYYY-MM-DD) | **Event date** (when the news/funding/hire actually happened) — primary freshness anchor for tier + heat compute | Signal Scan Stage 5b, R0 (default null), R1 Path α, R2 RE_ENRICH_FULL, 5 outreach push-backs |
| 3 | `last_signal_score` | Number (0-60) | Rubric score (Tier × Freshness × Confidence) — drives Hot vs Warm heat bucket + hot/white-hot tier modifiers | Same as #2 |
| 4 | `signal_count_last_30d` | Number (0-5 typical) | Count of events with event-date in trailing 30d — drives stacked-signal modifier + Hot bucket trigger | Same as #2 |
| 5 | `signal_heat` | Enum (`Hot`/`Warm`/`Cool`/`Cold`) | Rep-facing rollup — what reps sort their pipeline by daily | Same as #2 + R-Tier-Audit + R6 Step 5.5 |

**Rep-facing surface (3):** narrative + date + heat. Score and count are engine plumbing — reps don't filter by them directly; they live behind heat. Open-deal state is read from associated deal records, not stored on the company.

**Archived (intentionally not in the engine):**
- `account_tier_legacy` (created Phase 1.3 2026-05-13, archived same day)
- The transient `recent_news__trigger_event_date` Cooper briefly created 2026-05-28 then deleted on review — `last_signal_date` was unified to hold event-date semantics rather than maintaining a duplicate field.

### Audit log format (heat changes)

When `signal_heat` changes, write a HubSpot company note alongside the field write:

```
Heat <old> -> <new> on <ISO date> by <routine_name>: <reason citing modifier fired>
```

Examples:
- `"Heat Cold -> Hot on 2026-05-28 by Signal Scan: last_signal_score 32, last_signal_date (event) today, open deal past appointmentscheduled"`
- `"Heat Warm -> Cool on 2026-05-28 by R-Tier-Audit: last_signal_date (event) 75d old (out of 60d Warm window), no stack, no open deal"`
- `"Heat Cool -> Hot on 2026-05-28 by cold-email push-back: discovered $50M Series B event 2026-05-25, score 32, supersedes prior last_signal_date 2026-04-12"`

If `new_heat == current signal_heat`, no HubSpot write happens (idempotent no-op). Audit notes only on actual heat changes.

## 12. See-also

- File 06 §3 (D1 global disqualifiers) - runs BEFORE compute_tier inside R1/R2/Signal Scan
- File 06 §4 (D2 wholesale-arm policy) - informs which record gets which sub-segment
- File 06 §5 (D3 disambiguation flowcharts per ICP) - produces the `company_sub_segment` value `compute_tier` reads
- File 06 §6 (per-sub-segment classification rules with anchors + confidence)
- `context/account-tiering/sub-segment-qualification.md` - short pointer file to file 06
- `context/account-tiering/enrichment-protocols.md` - D5 v2 operational protocols for the 5-stage research-first workflow
- `tiering-framework-signoff.md` - historical framework signoff. Cooper overrode some defaults in 2026-05-14 feedback; defaults in §5 of THIS file are canonical.

---

**File 06 path:** `context/account-tiering/sub-segment-qualification-full.md`
