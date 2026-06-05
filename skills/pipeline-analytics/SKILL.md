---
name: pipeline-analytics
description: "MaiaEdge pipeline analytics and forecasting engine. Produces a single comprehensive HTML report covering pipeline health, revenue forecast with POC-adjusted probabilities, deal-by-deal narratives, and stale deal flags. Use when asked about pipeline, forecast, what's likely to close, deal review, what's stuck, or anything pipeline-related. Source of truth: HubSpot Deals pipeline with native time-in-stage tracking."
---

# MaiaEdge Pipeline Analytics & Forecasting

## Purpose

When anyone asks for a pipeline report, forecast, or deal review  -  produce one comprehensive report that covers everything leadership needs to see. No follow-up questions. No options to choose from. One report, every time.

The MaiaEdge Deals pipeline is the source of truth. All analysis uses HubSpot's native time-in-stage tracking for accurate velocity calculations.

---

## Design System

Uses the shared MaiaEdge design system. See `call-reporting/SKILL.md` Design System section for the full CSS stylesheet and visual rules.

Key points:
- All output is self-contained HTML (no CDN, no JS libraries)
- Slate neutral palette (`#F8FAFC` background, `#0F172A` hero text, `#1E293B` headings)
- Indigo accent (`#6366F1`) for bar fills and highlights
- Desaturated status badges: GREEN `#059669`, YELLOW `#D97706`, ORANGE `#EA580C`, RED `#DC2626`
- KPI cards for hero metrics (36px number, 12px uppercase label, change indicator)
- CSS horizontal bar charts for ranked/distributed data
- Tables for precision data; bar charts for visual ranking
- Section titles state the insight, not the chart type
- Data reliability rules: counts with percentages, suppress <3 samples, no narrative without evidence
- `font-variant-numeric: tabular-nums` on all numbers

---

## Reference

### Pipeline Stages

See `deals-schema.md` for full stage reference. Quick mapping:

| Stage | Internal Name | Base Probability | Forecast Category |
|-------|---------------|-----------------|-------------------|
| Appointment Scheduled | `appointmentscheduled` | 5% | Pipeline |
| Discovery & Scoping | `qualifiedtobuy` | 15% | Pipeline |
| Quote Provided | `1996673735` | 35% | Pipeline |
| POC & Technical Validation | `presentationscheduled` | 50% | Pipeline |
| Price Agreement & Final Config | `decisionmakerboughtin` | 75% | Best Case |
| Contract Review | `contractsent` | 90% | Commit |
| Closed Won | `closedwon` | 100% | Closed Won |
| Closed Lost | `closedlost` | 0% | Not Forecasted |

> **Note:** Quote Provided (35%) comes before POC (50%) in the pipeline because some deals receive a quote before entering a POC, while others go straight to POC. The probability reflects conviction level, not strict ordering.

### Key Deal Properties

**Pipeline & value:** `dealname, dealstage, amount, pipeline, closedate, createdate, hubspot_owner_id, customer_segment`

**Forecasting:** `hs_deal_stage_probability, hs_forecast_amount, hs_manual_forecast_category, hs_acv, hs_tcv`

**Velocity:** `hs_v2_cumulative_time_in_[stage], hs_v2_latest_time_in_[stage], hs_v2_date_entered_[stage], hs_v2_date_exited_[stage], hs_v2_time_in_current_stage`

**Health:** `hs_is_closed, hs_is_closed_won, hs_is_closed_lost, num_associated_contacts, notes_last_contacted, notes_last_updated`

**MEDDPICC (8 fields, ~45% fill rate):** `buying_process_meddpicc, identified_pain_meddpicc, decision_criteria___meddpicc, key_stakeholders_meddpicc, competition_meddpicc, infrastructure_meddpicc, metrics_meddpicc, use_case_meddpicc`

### Owner IDs

See `territory-model.md` for complete mapping.

### Deal Health Assessment

From `deals-schema.md`:

| Metric | Healthy | Warning |
|--------|---------|---------|
| MEDDPICC completion | 70%+ fields filled | <40% filled |
| Time in stage | 14-30 days avg | >60 days |
| Contact depth | 2+ contacts at different levels | 1 contact only |
| Activity frequency | Touch within 14 days | 0 touches in 30+ days |
| Deal amount | $2K-$400K (consistent with SKU) | Outside range |

### Forecast Categories

HubSpot groups deals into five forecast categories. Stage changes auto-assign the mapped category; reps can override manually (override sticks until next stage change).

| Category | HubSpot API Value | Auto-Assigned Stages | Notes |
|----------|-------------------|---------------------|-------|
| Not Forecasted | OMIT | Closed Lost + stale (30+ days no activity on deal or POC) | Excluded from all forecast math |
| Pipeline | PIPELINE | Appointment Scheduled, Discovery, Quote Provided, POC | Conviction still building |
| Best Case | BEST_CASE | Price Agreement & Final Config | Manual override available |
| Commit | COMMIT | Contract Review | Rep-confirmed close |
| Closed Won | CLOSED | Closed Won | Auto-set by HubSpot |

When `hs_manual_forecast_category` is set on a deal, use it. Otherwise derive from stage. Label stage-derived assignments clearly so they are distinguishable from manual overrides.

### POC Signal Matrix

For any deal with an associated POC ticket, apply a probability modifier on top of the base stage probability. Cross-reference `hs_pipeline_stage` (POC stage) with `poc_trend` to determine the modifier:

| POC Stage | On Track | Needs Attention | Blocked / At Risk |
|-----------|----------|-----------------|-------------------|
| POC Requested | 0% | 0% | -5% |
| Scoping | 0% | -5% | -10% |
| Criteria Approved | +5% | 0% | -5% |
| Configuration Locked | +5% | -5% | -10% |
| Building & Preparing | +10% | -5% | -10% |
| Shipped | +10% | 0% | -10% |
| Customer Testing | +10% | -10% | -15% |
| POC Successful | +20% | +20% | +20% |
| POC Unsuccessful | 5% cap | 5% cap | 5% cap |
| On Hold | -10% | -10% | -15% |

**Formula:** Adjusted Probability = Stage Base Probability + POC Modifier
- Cap: 95% maximum, 5% minimum
- **POC Successful:** Always adds +20% regardless of trend -- strongest buying signal
- **POC Unsuccessful:** Overrides everything -- deal probability capped at 5%
- **No POC ticket:** Use base stage probability unchanged (no adjustment, no label)
- **Blank `poc_trend`:** Treat as "On Track" for modifier lookup; flag in data quality output

Use the adjusted probability everywhere in forecast output (weighted values, scenario totals). Show both base and adjusted probabilities on deal cards so the delta is visible.

### Blank Field Handling

Same principle as pipeline-discipline: report what we know, never guess.

- `amount` blank: show "--" for value columns, exclude from weighted calculations and averages
- `hs_manual_forecast_category` blank: derive from stage per the Forecast Categories table above, label as "Stage-based"
- `closedate` blank: show "Not set" -- flag as action item
- `customer_segment` blank: show "Unclassified"
- MEDDPICC fields: calculate fill % from filled fields only, show "0%" if all blank
- Win rate: show "--" if fewer than 3 closed deals for that segment/rep
- Velocity: show "--" for stages with fewer than 3 data points
- `poc_trend` blank: treat as "On Track" for probability math, note "(trend not set)" in POC status display

---

## Task Routing

### DEFAULT: FULL PIPELINE & FORECAST REPORT
**Trigger:** Any pipeline or forecast request. This is the default output. Examples: "Give me a forecast", "How's the pipeline?", "Pipeline report", "Weekly forecast", "What's likely to close?", "Deal review", "What's happening on our deals?", "What's stuck?", "What do we have in the funnel?", "Run the pipeline", "Pipeline health", "What should we be focused on?"  -  and any similar phrasing. Do not ask which mode or format the user wants. Just run this report.

**Steps:**

**Step 1  -  Pull all open deals:**
Pull all open deals (not closed won or lost) from the MaiaEdge Deals pipeline via `search_crm_objects`. Request properties: `dealname, dealstage, amount, hubspot_owner_id, customer_segment, closedate, createdate, hs_deal_stage_probability, hs_manual_forecast_category, hs_v2_time_in_current_stage, num_associated_contacts, notes_last_contacted, notes_last_updated`. Include `associations: ["COMPANY", "TICKET"]`. Paginate if >100 deals.

For each deal, also pull the associated company's `account_tier` and `signal_heat` via the COMPANY association. These power the deal-by-deal context columns (Section 6) and the Signal Heat Distribution section (Section 6b).

**Step 2  -  Stale deal detection:**
For each deal, determine the most recent activity date by checking:
- `notes_last_contacted` (deal-level activity)
- `notes_last_updated` (deal-level notes)
- If the deal has an associated POC ticket: also check `hs_pipeline_stage_timestamp` (most recent stage change) and any POC-level notes or updates on the ticket record

Take the most recent date across ALL of these sources. If that date is 30+ days ago, mark the deal as **Stale**. Stale deals are auto-assigned Not Forecasted (OMIT) in this report regardless of their HubSpot category. List them in the Stale Deals section at the end.

**Step 3  -  Assign forecast categories (non-stale deals):**
- If `hs_manual_forecast_category` is set, use it
- If blank, derive from stage per the Forecast Categories table in Reference
- Label stage-derived assignments "(stage-based)"

**Step 4  -  Calculate adjusted probability per deal:**
- Start with base stage probability (from Pipeline Stages table)
- If the deal has an associated POC ticket, pull `hs_pipeline_stage` (POC stage) and `poc_trend`
- Apply the POC Signal Matrix modifier; cap 95%, floor 5%
- No POC ticket: adjusted probability = base probability

**Step 5  -  Compute weighted values:**
Weighted value per deal = `amount × adjusted probability`. Use this everywhere.

**Step 6  -  Pull deal narratives:**
For each non-OMIT deal, pull the most recent available data (in order of recency): POC ticket status/notes → deal notes → `hs_call_summary` from associated calls → email activity timestamps. Synthesize into a 2-3 sentence plain-English summary of current state, next step, and any blocker or momentum signal.

**Step 7  -  Pull velocity data:**
Pull closed-won deals from the last 12 months with time-in-stage properties: `hs_v2_cumulative_time_in_appointmentscheduled, hs_v2_cumulative_time_in_qualifiedtobuy, hs_v2_cumulative_time_in_presentationscheduled, hs_v2_cumulative_time_in_1996673735, hs_v2_cumulative_time_in_decisionmakerboughtin, hs_v2_cumulative_time_in_contractsent, createdate, closedate, amount, customer_segment, hubspot_owner_id`. Calculate avg days per stage (cumulative time / 86400), median, fastest, slowest. Show "--" for stages with <3 data points. Identify bottleneck stage (longest avg dwell).

**Step 8  -  Pull rep performance data:**
Pull all deals (open + closed in last 6 months) with `dealname, dealstage, amount, hubspot_owner_id, customer_segment, closedate, createdate, hs_is_closed_won, hs_is_closed_lost`. Group by owner: open deal count, pipeline value, weighted value, avg deal size, avg days in pipeline, win rate (show "--" if <3 closed), deals closed this quarter. Also compute segment coverage per rep.

**Step 9  -  Render as single HTML report.**

---

**Output:** Single self-contained HTML report titled "MaiaEdge Pipeline & Forecast" with today's date.

**Section 1  -  Pipeline at a Glance (KPI cards):**
Four hero cards: Total Open Pipeline ($ ACV, deal count) | Weighted Pipeline ($ using adjusted probabilities) | Commit ($ weighted, deals in Contract Review) | Deals Flagged (stale + at-risk count)

**Section 2  -  Pipeline by Stage:**
Horizontal bar chart (total ACV per stage) + table:

| Stage | Deals | Total ACV | Weighted (Adj.) | Avg Days in Stage |
|-------|-------|-----------|-----------------|-------------------|

**Section 3  -  Forecast by Category:**
| Category | Deals | Total ACV | Weighted (Adj.) | Source |
|----------|-------|-----------|-----------------|--------|
| Commit | | | | Manual / Stage-based |
| Best Case | | | | Manual / Stage-based |
| Pipeline | | | | Manual / Stage-based |
| Not Forecasted | | $[X] | -- | Manual / Stale |

**Section 4  -  Scenario Overlays:**
| Scenario | What's Included | Deals | Weighted Revenue |
|----------|----------------|-------|-----------------|
| Conservative | Commit only | | |
| Likely | Commit + Best Case | | |
| Optimistic | Commit + Best Case + Pipeline | | |

**Section 5  -  Close Date Timeline:**
| Month | Deals | Total ACV | Weighted (Adj.) | Overdue? |
|-------|-------|-----------|-----------------|----------|
| [This month] | | | | [N] deals past close date |
| [Next month] | | | | |
| [Month+2] | | | | |
| Beyond / Not set | | | | |

Alert card for any deals with `closedate` in the past and still open.

**Section 6  -  Deal-by-Deal Summary:**
One row per non-OMIT deal, sorted by adjusted probability descending. Every deal with its full context at a glance.

| Deal | Rep | ACV | Stage | Base % | Adj. % | POC Signal | Heat | Category | Latest Summary |
|------|-----|-----|-------|--------|--------|------------|------|----------|----------------|
| [dealname] | [rep] | $[X] | [stage] | [base]% | [adj]% | [POC stage + trend, or "--"] | [hot/warm/cool/cold] | [category] | [2-3 sentence narrative] |

- If POC modifier applied, show the delta clearly: "50% → 60% (Customer Testing / On Track)"
- Heat column reads `signal_heat` from the associated company. Apply subtle color band on the cell: hot=red, warm=orange, cool=yellow, cold=gray.
- If no recent data for narrative: "No activity in [N] days."

**Section 6b  -  Signal Heat Distribution (NEW 2026-05-20):**

Surfaces the intent shape of the open pipeline. Useful for spotting deals that are advancing without current intent signals (a `Cold` deal in `presentationscheduled` is a watch flag) and for prioritizing rep follow-through (`Hot` deals at lower stages are the ones to push this week). Heat values are Title Case per HubSpot enum.

Horizontal bar chart: count of open deals per heat bucket × per stage.

| Heat | Count | Total ACV | Weighted | Notes |
|------|------:|----------:|---------:|-------|
| Hot | | | | High intent. Push to next stage this week. |
| Warm | | | | Recent signal. Maintain momentum. |
| Cool | | | | Signal stale. Investigate recency. |
| Cold | | | | No signal in 180d. Discovery call to validate. |

Suppress the section entirely if all four heat buckets contain <3 deals (low signal, the section adds noise without insight).

**Section 7  -  Rep Performance:**
Horizontal bar chart (pipeline value per rep) + table:

| Rep | Open Deals | Total ACV | Weighted | Avg Deal Size | Avg Days in Pipeline | Win Rate | Closed This Quarter |
|-----|-----------|-----------|----------|---------------|---------------------|----------|-------------------|

Segment coverage below: Rep | Colo | Fiber | Neocloud | Network Op | MSP | Enterprise (deal counts per cell - Enterprise added 2026-05-11 as 6th ICP segment)

**Section 8  -  Deal Velocity (closed-won, last 12 months):**
How long deals actually take to close and where they get stuck.

KPI row: Avg Days to Close | Deals Analyzed | Bottleneck Stage (name + avg days)

Time-in-stage table:

| Stage | Avg Days | Median Days | Fastest Deal | Slowest Deal |
|-------|----------|-------------|--------------|--------------|

Velocity by segment (3+ deals only):

| Segment | Avg Days to Close | Deal Count |
|---------|-------------------|------------|
| Colo | | |
| Fiber | | |
| Neocloud | | |
| Network Op | | |
| MSP / Aggregator | | |
| Enterprise (Multi-DC ICP) | | |

Note: Enterprise segment added 2026-05-11 with ICP promotion. Show "--" for Enterprise rows where fewer than 3 closed Enterprise deals exist (sample too small to benchmark - Meijer is the early anchor).

Bottleneck alert card: calls out the single slowest stage with context.

**Section 9  -  Stale Deals (if any):**
Deals excluded from forecast totals due to 30+ days no activity on deal or associated POC record.

| Deal | Rep | Stage | Last Activity | Days Since Activity | Action |
|------|-----|-------|---------------|---------------------|--------|
| [dealname] | [rep] | [stage] | [date] | [N] days | Consider marking Closed Lost |

---

## When to Use This Skill

Trigger on any mention of: pipeline, forecast, deal review, what's likely to close, what's stuck, stalled deals, pipeline health, pipeline report, weekly/monthly/quarterly forecast, where should we focus, deal velocity, rep performance, how are reps doing, close rate, stage timing, bottleneck.

Always produce the Full Pipeline & Forecast Report. No modes, no follow-up questions.
