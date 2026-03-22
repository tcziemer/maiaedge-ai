---
name: pipeline-analytics
description: "MaiaEdge pipeline analytics and forecasting engine. Produces HTML dashboards for pipeline health, deal velocity, revenue forecasting, deal-by-deal review with call intelligence, and rep performance. Use when asked about pipeline health, deal velocity, forecast, what's likely to close, what's stuck, deal review, rep performance, or where reps should focus. Source of truth: HubSpot Deals pipeline with native time-in-stage tracking."
---

# MaiaEdge Pipeline Analytics & Forecasting

## Purpose

Analyze the MaiaEdge deal pipeline in HubSpot and produce actionable, visually rich reports. Five modes: pipeline snapshot, deal velocity, revenue forecasting, deal-by-deal review (with call intelligence per deal), and rep performance.

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

| Stage | Internal Name | Probability |
|-------|---------------|-------------|
| Appointment Scheduled | `appointmentscheduled` | 20% |
| Discovery & Scoping | `qualifiedtobuy` | 40% |
| POC & Technical Validation | `presentationscheduled` | 60% |
| Quote Provided | `1996673735` | 80% |
| Price Agreement & Final Config | `decisionmakerboughtin` | 90% |
| Contract Review | `contractsent` | 90% |
| Closed Won | `closedwon` | 100% |
| Closed Lost | `closedlost` | 0% |

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

### Blank Field Handling

Same principle as pipeline-discipline: report what we know, never guess.

- `amount` blank: show "--" for value columns, exclude from weighted calculations and averages
- `hs_manual_forecast_category` blank: fall back to stage probability, label as "Stage-based" not "Commit"
- `closedate` blank: show "Not set" -- flag as action item
- `customer_segment` blank: show "Unclassified"
- MEDDPICC fields: calculate fill % from filled fields only, show "0%" if all blank
- Win rate: show "--" if fewer than 3 closed deals for that segment/rep
- Velocity: show "--" for stages with fewer than 3 data points

---

## Task Routing

### MODE 1: PIPELINE SNAPSHOT
**Trigger:** "How's our pipeline?" or "Pipeline overview" or "What do we have in the funnel?" or "Pipeline snapshot"

**Steps:**
1. Pull all open deals (not closed won or lost) from the MaiaEdge Deals pipeline via `search_crm_objects`. Request properties: `dealname, dealstage, amount, hubspot_owner_id, customer_segment, closedate, createdate, hs_deal_stage_probability, hs_v2_time_in_current_stage, num_associated_contacts, notes_last_contacted`. Include `associations: ["COMPANY"]`. Paginate if >100 deals.
2. Group by stage. For each stage: deal count, total value (sum of `amount` where not null), weighted value (sum of `amount x hs_deal_stage_probability`), avg days in stage (from `hs_v2_time_in_current_stage`, convert seconds to days).
3. Group by owner (`hubspot_owner_id`). For each: deal count, total pipeline value, weighted value, avg deal size.
4. Group by segment (`customer_segment`). For each: deal count, total value, avg deal size.
5. Calculate deal health distribution using the health assessment framework (see Reference section). Categorize each deal as GREEN/YELLOW/ORANGE/RED based on MEDDPICC %, time in stage, contact depth, and activity recency. Show health distribution as a stacked bar.
6. Render as HTML.

**Output:** HTML dashboard:
- **Header:** "Pipeline Snapshot" with date
- **KPI row (4 cards):** Total Pipeline ($, deal count), Weighted Pipeline ($), Avg Deal Size ($), Deals with Amount Set (N/total)
- **Section: "Pipeline by stage"** -- Horizontal bar chart (value per stage) + table: Stage, Deals, Total Value, Weighted Value, Avg Days in Stage
- **Section: "Pipeline by rep"** -- Horizontal bar chart (value per rep) + table: Owner, Deals, Pipeline Value, Weighted, Avg Deal Size
- **Section: "Pipeline by segment"** -- Stacked distribution bar (segment colors from design system) + table: Segment, Deals, Value, Avg Deal Size
- **Section: "Deal health distribution"** -- Stacked bar (GREEN/YELLOW/ORANGE/RED) + summary: "[N] healthy, [N] watch, [N] risk, [N] critical"
- **Footer**

---

### MODE 2: DEAL VELOCITY
**Trigger:** "How fast are deals moving?" or "Deal velocity" or "Stage conversion times" or "How long do deals take to close?"

**Steps:**
1. Pull closed-won deals from the last 12 months (or user-specified range) with time-in-stage properties: `hs_v2_cumulative_time_in_appointmentscheduled, hs_v2_cumulative_time_in_qualifiedtobuy, hs_v2_cumulative_time_in_presentationscheduled, hs_v2_cumulative_time_in_1996673735, hs_v2_cumulative_time_in_decisionmakerboughtin, hs_v2_cumulative_time_in_contractsent`. Also request: `dealname, amount, customer_segment, hubspot_owner_id, createdate, closedate`.
2. For each stage, calculate: avg days (mean of cumulative time / 86400), median days, fastest deal, slowest deal. Show "--" for stages with <3 data points.
3. Calculate total average days to close (createdate to closedate).
4. Break down by segment where sample size permits (3+ deals per segment).
5. Identify bottleneck stage (longest avg dwell time).
6. Render as HTML.

**Output:** HTML report:
- **Header:** "Deal Velocity Analysis" with date range
- **KPI row (3 cards):** Avg Days to Close, Deals Analyzed (N), Bottleneck Stage (name + avg days)
- **Section: "Time in each stage"** -- Horizontal bar chart (avg days per stage) + table: Stage, Avg Days, Median Days, Fastest (company, N days), Slowest (company, N days)
- **Section: "Velocity by segment"** -- Table: Segment, Avg Days to Close, Deal Count. Only segments with 3+ deals.
- **Section: "Bottleneck analysis"** -- Alert card highlighting the slowest stage with context
- **Footer**

---

### MODE 3: FORECAST
**Trigger:** "Forecast" or "What's likely to close?" or "Revenue projection" or "Quarterly forecast" or "What will we close this quarter?"

**Steps:**
1. Pull all open deals with: `dealname, dealstage, amount, hubspot_owner_id, customer_segment, closedate, hs_deal_stage_probability, hs_manual_forecast_category`. Include `associations: ["COMPANY"]`.
2. Build forecast categories:
   - If `hs_manual_forecast_category` is set, use it (Commit, Most Likely, Pipeline, Omit)
   - If blank, assign based on stage probability: >80% = "Most Likely (stage-based)", 40-80% = "Pipeline (stage-based)", <40% = "Pipeline (stage-based)"
   - Label stage-based assignments clearly so they are distinguishable from manual categorization
3. Compute weighted pipeline by category and by close date month.
4. If user provides a quarterly/monthly target, compute gap analysis.
5. Build scenario table.
6. Render as HTML.

**Output:** HTML report:
- **Header:** "Revenue Forecast" with date and target quarter/month if specified
- **KPI row (4 cards):** Commit Total ($), Best Case (Commit + Most Likely, $), Full Pipeline ($), Deals with Close Date Set (N/total)

- **Section: "Forecast by category"** -- Table:

| Category | Deals | Total Value | Weighted Value | Source |
|----------|-------|-------------|----------------|--------|
| Commit | [N] | $[X] | $[X] | Manual |
| Most Likely | [N] | $[X] | $[X] | Manual / Stage-based |
| Pipeline | [N] | $[X] | $[X] | Manual / Stage-based |
| Omit | [N] | $[X] | -- | Manual |

- **Section: "Close date forecast"** -- Table:

| Month | Deals | Total Value | Weighted Value | Overdue? |
|-------|-------|-------------|----------------|----------|
| [This month] | [N] | $[X] | $[X] | [N] deals past close date |
| [Next month] | [N] | $[X] | $[X] | -- |
| [Month+2] | [N] | $[X] | $[X] | -- |
| Beyond / Not set | [N] | $[X] | $[X] | -- |

Alert card below for deals with `closedate` in the past but still open.

- **Section: "Scenario table"**

| Scenario | Assumption | Deals | Revenue |
|----------|-----------|-------|---------|
| Conservative | Commit only | [N] | $[X] |
| Likely | Commit + 50% of Most Likely | [N] | $[X] |
| Best Case | Commit + Most Likely | [N] | $[X] |

- **Section: "Gap analysis"** (only if user provided a target)

| | Amount |
|---|--------|
| Target | $[X] |
| Commit | $[X] |
| Gap | $[X] |

Gap-filler table: deals from Most Likely and Pipeline ranked by weighted probability, close date proximity, and deal size. Show enough deals to cover the gap amount.

- **Footer**

---

### MODE 4: DEAL-BY-DEAL REVIEW
**Trigger:** "Deal review" or "Which deals need attention?" or "Deal-by-deal" or "Go through each deal" or "What's happening on our deals?"

**Steps:**

**Part 1 -- Summary Table:**
1. Pull all open deals with full property set (pipeline, value, velocity, MEDDPICC, contacts, activity). Include `associations: ["COMPANY", "CONTACT", "TICKET"]`.
2. For each deal, compute health using the health assessment framework.
3. Sort by health severity (RED first), then by value descending.
4. Render summary table.

**Part 2 -- Deal Intelligence Cards (one per deal):**

For each open deal:

5. **Activity Pulse:** Query calls and emails associated with the deal's contacts (HubSpot engagement objects). Get the last 3 outbound and last 3 inbound with dates. Determine engagement trend:
   - ACCELERATING: increasing touch frequency over last 30 days
   - STEADY: consistent cadence
   - COOLING: decreasing frequency, gaps widening
   - DARK: no inbound response in 30+ days
   All from HubSpot engagement associations -- not inference.

6. **Latest Conversation:**
   - Pull the most recent call associated with any contact on this deal
   - If the deal has an associated POC ticket (from step 1 associations), ALSO pull the most recent call associated with that ticket's company
   - Compare timestamps. Show the MORE RECENT one as the primary conversation:
     - If POC-level call is more recent: "Latest call (via POC ticket -- [POC stage])"
     - If deal-level call is more recent: "Latest call (on deal contacts)"
   - Show: date, title, call owner, 2-3 sentence summary excerpt from `hs_call_summary`
   - Extract from the summary: key topics discussed, any objections raised, stated next steps
   - If a second call exists from the other source (deal vs POC), show below as: "Previous: [date] -- [title] -- [1 sentence]"
   - If no calls exist on either deal contacts or POC ticket, show "No calls logged"

7. **POC Status (if applicable):**
   - From the deal's associated tickets, identify any in the POC pipeline
   - Show: POC stage, `poc_trend`, days in stage, `poc_end_date`, POC owner
   - POC call context is already surfaced in Latest Conversation if it was most recent
   - If no POC ticket, show "No POC"

8. **Deal Momentum Summary:**
   - 2-3 sentence paragraph synthesizing: where the deal is, what the last interaction revealed, what needs to happen next
   - Derived ONLY from call summary text and activity timestamps
   - If no calls or recent activity: "No calls or emails in [N] days. Deal may be stalled."

9. **Flags:** Only show flags that are true. Each backed by a specific HubSpot property value.
   - Stalled: >60 days no activity (`notes_last_contacted` or `notes_last_updated`)
   - Close date overdue: `closedate` is in the past
   - Close date approaching: `closedate` within 7 days
   - Single-threaded: `num_associated_contacts` = 1
   - No calls logged: zero calls on deal contacts and associated POC
   - POC at risk: associated POC ticket `poc_trend` = "At Risk" or "Blocked"
   - No amount set: `amount` is null
   - MEDDPICC low: <40% fields filled on deals past Discovery stage

**Output:** HTML report:

- **Header:** "Deal Review" with date
- **KPI row (4 cards):** Open Deals, Total Pipeline, Deals with Flags (count), Avg MEDDPICC Completion

- **Summary table:**

| Company | Segment | Stage | Value | Days in Stage | Close Date | MEDDPICC | Contacts | Last Activity | Health | Owner |
|---------|---------|-------|-------|---------------|-----------|----------|----------|---------------|--------|-------|

- **Deal intelligence cards** (one card per deal, inside a card element with card-title showing company name, segment, stage, value, owner):

```
[Company Name] | [Segment] | [Stage] | $[Value] | Owner: [Rep]
Health: [badge] | MEDDPICC: [N]% | Contacts: [N] | Days in Stage: [N]

ACTIVITY PULSE
  Outbound: [date] call, [date] email, [date] email
  Inbound:  [date] email reply, [date] call
  Trend: [COOLING] -- last inbound was [N] days ago

LATEST CONVERSATION ([date] -- [owner], via POC ticket -- Customer Testing)
  "[2-3 sentence excerpt from hs_call_summary]"
  Previous: [date] -- [title] -- [1 sentence]

POC STATUS
  Stage: [stage] | Trend: [trend] | Day [N] | End: [date]
  Owner: [Kyle/Woody]

MOMENTUM: [2-3 sentence synthesis from call content and activity data]

FLAGS: [only flags that are true, comma-separated]
```

- **Footer**

---

### MODE 5: OWNER PERFORMANCE
**Trigger:** "Rep performance" or "Owner comparison" or "How are reps doing?" or "Who's moving deals?"

**Steps:**
1. Pull all deals (open + closed in last 6 months) with: `dealname, dealstage, amount, hubspot_owner_id, customer_segment, closedate, createdate, hs_is_closed_won, hs_is_closed_lost`.
2. Group by owner. For each rep calculate:
   - Open deals: count and total pipeline value
   - Weighted pipeline value
   - Avg deal size (open deals with amount set)
   - Avg days in pipeline (open deals, from `createdate` to today)
   - Win rate: closed-won / (closed-won + closed-lost). Show "--" if <3 total closed.
   - Deals closed this quarter (count and value)
3. Segment coverage per rep: which segments they are working.
4. Render as HTML.

**Output:** HTML report:
- **Header:** "Rep Performance" with date range
- **KPI row (3 cards):** Total Open Pipeline ($), Deals Closed This Quarter (count, value), Team Win Rate (%, if 3+ total closed)

- **Section: "Pipeline by rep"** -- Horizontal bar chart (pipeline value per rep) + table:

| Rep | Open Deals | Pipeline Value | Weighted | Avg Deal Size | Avg Days in Pipeline | Win Rate | Closed This Quarter |
|-----|-----------|---------------|----------|---------------|---------------------|----------|-------------------|

- **Section: "Segment coverage"** -- Table: Rep | Colo | Fiber | Neocloud | Network Op | MSP (deal counts per cell)

- **Footer**

---

## When to Use This Skill

Trigger on any of these patterns:
- "How's our pipeline?" or "Pipeline health" or "Pipeline overview" or "Pipeline snapshot"
- "Deal velocity" or "How fast do deals close?" or "Stage timing" or "Bottleneck"
- "Forecast" or "What's likely to close?" or "Revenue projection" or "Quarterly forecast"
- "Deal review" or "Which deals need attention?" or "Go through each deal" or "What's happening on our deals?"
- "Rep performance" or "Owner comparison" or "Who's moving deals?" or "How are reps doing?"
- "What's stuck?" or "Stalled deals"
- "Pipeline by segment" or "Segment trends"
- Any mention of: pipeline, forecast, close rate, stage, velocity, bottleneck, stuck deals, deal review, rep performance
