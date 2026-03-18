---
name: pipeline-analytics
description: "MaiaEdge pipeline analytics engine. Analyzes MaiaEdge deal pipeline in HubSpot to provide actionable sales intelligence. Use when asked about pipeline health, deal velocity, stage analysis, what's likely to close, what's stuck, forecast accuracy, deal progression speed, stage conversion rates, or where reps should focus. Calculates weighted pipeline (amount × probability), stage velocity, deal age by stage, bottleneck identification, owner performance, segment trends, and stalled deal detection. Produces pipeline snapshots, velocity reports, forecast trends, and deal-specific recommendations. Source of truth: HubSpot Deals pipeline with native time-in-stage tracking."
---

# MaiaEdge Pipeline Analytics

## Purpose

Analyze the MaiaEdge deal pipeline in HubSpot to provide actionable sales intelligence. This skill turns raw deal data into insights: what's the pipeline worth, what's likely to close, what's stuck, and where should reps focus their time.

The MaiaEdge Deals pipeline is the source of truth. All analysis uses HubSpot's native time-in-stage tracking for accurate velocity calculations.

---

## Pipeline Reference

### MaiaEdge Deals Pipeline Stages (in order)

| Stage | HubSpot Internal Name | Purpose |
|-------|----------------------|---------|
| Appointment Scheduled | `appointmentscheduled` | First meeting booked |
| Discovery & Scoping | `qualifiedtobuy` | Understanding needs, qualifying opportunity |
| POC & Technical Validation | `presentationscheduled` | Proof of concept in progress |
| Quote Provided | `1996673735` | Formal pricing delivered |
| Price Agreement & Final Configuration | `decisionmakerboughtin` | Negotiation, final terms |
| Contract Review | `contractsent` | Legal review, signatures pending |
| Closed Won | `closedwon` | Deal signed |
| Closed Lost | `closedlost` | Deal lost |

### Key Deal Properties

```
dealname, dealstage, amount, hubspot_owner_id, customer_segment,
closedate, createdate, pipeline, hs_is_closed, hs_is_closed_won,
hs_is_closed_lost, hs_is_stalled, days_to_close, hs_deal_stage_probability,
hs_forecast_amount, hs_manual_forecast_category, hs_acv, hs_tcv, hs_mrr, hs_arr,
notes_last_contacted, notes_last_updated, num_associated_contacts,
contract_term, expected_pbc_count, bandwidth_tier
```

### Time-in-Stage Properties

HubSpot tracks cumulative and latest time in each stage automatically. Use these for velocity calculations:
- `hs_v2_cumulative_time_in_[stage]` — Total seconds in stage (all visits)
- `hs_v2_latest_time_in_[stage]` — Seconds since last entering stage
- `hs_v2_date_entered_[stage]` / `hs_v2_date_exited_[stage]` — Timestamps
- `hs_v2_time_in_current_stage` — Time in current stage

---

## Task Routing

### MODE 1: PIPELINE SNAPSHOT
**Trigger:** "How's our pipeline?" or "Pipeline overview" or "What do we have in the funnel?"

**Steps:**
1. Pull all open deals (not closed won or lost) from the MaiaEdge Deals pipeline
2. Group by stage, calculate total value per stage
3. Show weighted pipeline (amount × stage probability)
4. Break down by owner and segment

**Output:**
```
PIPELINE SNAPSHOT — [Date]
============================

OPEN PIPELINE: $[total] ([N] deals)
WEIGHTED PIPELINE: $[weighted total]

BY STAGE
| Stage | Deals | Total Value | Weighted Value | Avg Age |
|-------|-------|-------------|----------------|---------|
| Appointment Scheduled | [N] | $[X] | $[X] | [N] days |
| Discovery & Scoping | [N] | $[X] | $[X] | [N] days |
| POC & Technical Validation | [N] | $[X] | $[X] | [N] days |
| Quote Provided | [N] | $[X] | $[X] | [N] days |
| Price Agreement | [N] | $[X] | $[X] | [N] days |
| Contract Review | [N] | $[X] | $[X] | [N] days |

BY OWNER
| Owner | Deals | Pipeline Value | Weighted | Avg Deal Size |
|-------|-------|---------------|----------|---------------|

BY SEGMENT
| Segment | Deals | Pipeline Value | Avg Deal Size |
|---------|-------|---------------|---------------|
```

---

### MODE 2: DEAL VELOCITY ANALYSIS
**Trigger:** "How fast are deals moving?" or "Deal velocity" or "Stage conversion times" or "How long do deals take to close?"

**Steps:**
1. Pull closed won deals with time-in-stage data
2. Calculate average time in each stage (convert seconds to days)
3. Calculate overall average time to close
4. Break down by segment and deal size
5. Identify bottleneck stages (longest average time)

**Output:**
```
DEAL VELOCITY REPORT — [Date]
================================
```

---

## When to Use This Skill

Trigger on any of these patterns:
- "How's our pipeline?" or "Pipeline health" or "Pipeline overview"
- "Deal velocity" or "How fast do deals close?" or "Stage timing"
- "What's likely to close this quarter?" or "Forecast accuracy"
- "What's stuck?" or "Which deals are stalled?" or "Bottleneck analysis"
- "Deal by deal review" or "Which deals need attention?"
- "Owner performance" or "Who's moving deals?"
- "Segment trends" or "Pipeline by segment"
- Any mention of: pipeline, forecast, close rate, stage, velocity, bottleneck, stuck deals

