---
name: call-reporting
description: "MaiaEdge call reporting and dashboard engine. Produces visually rich reports from HubSpot call data -- monthly dashboards, multi-month trend analysis, deals vs POCs call comparison, and audience-specific briefings for CEO, CRO, and reps. Outputs as HTML artifacts or downloadable files. Use when asked for call reports, dashboards, trends, monthly summaries, CEO/CRO briefings, rep scorecards, or any visual call analytics."
---

# MaiaEdge Call Reporting

## Purpose

Produce visually rich, audience-specific reports from HubSpot call data. This skill transforms raw call analysis into formatted dashboards and briefings that leadership, sales management, and individual reps can act on.

**Output formats:**
- **Default:** HTML artifact rendered inline in Claude.ai chat (self-contained HTML/CSS, no external dependencies)
- **Save to file:** When requested, write as `.html` file to disk for sharing via email or hosting

---

## Reference

### Reference Files

- **Owner IDs and territory mapping:** See `territory-model.md`
- **Segment HubSpot values:** See `hubspot-values.md` (note: MSP/Aggregator = `Enterprise` in HubSpot)
- **Call properties, query patterns, pagination, property sets:** See `call-schema.md`
- **Use case taxonomy:** See `use-case-taxonomy.md`

---

## HTML Output Specification

All HTML reports should use this styling baseline:

```html
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 20px; background: #f5f5f5; }
  .header { background: #1a365d; color: white; padding: 20px 30px; border-radius: 8px 8px 0 0; }
  .header h1 { margin: 0; font-size: 22px; }
  .header .subtitle { opacity: 0.8; font-size: 14px; margin-top: 4px; }
  .metrics-bar { display: flex; gap: 20px; padding: 15px 30px; background: #2d4a7c; color: white; }
  .metric { text-align: center; }
  .metric .value { font-size: 28px; font-weight: bold; }
  .metric .label { font-size: 12px; opacity: 0.8; text-transform: uppercase; }
  .card { background: white; border-radius: 8px; margin: 15px 0; box-shadow: 0 1px 3px rgba(0,0,0,0.1); overflow: hidden; }
  .card-title { padding: 12px 20px; background: #f8f9fa; border-bottom: 1px solid #e9ecef; font-weight: 600; font-size: 15px; }
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  th { background: #1a365d; color: white; padding: 10px 12px; text-align: left; font-weight: 500; }
  td { padding: 8px 12px; border-bottom: 1px solid #e9ecef; }
  tr:nth-child(even) { background: #f8f9fa; }
  tr:hover { background: #e3f2fd; }
  .trend-up { color: #2e7d32; } .trend-up::before { content: "\\25B2 "; }
  .trend-down { color: #c62828; } .trend-down::before { content: "\\25BC "; }
  .trend-stable { color: #757575; } .trend-stable::before { content: "\\25C6 "; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 500; }
  .badge-green { background: #e8f5e9; color: #2e7d32; }
  .badge-yellow { background: #fff8e1; color: #f57f17; }
  .badge-orange { background: #fff3e0; color: #e65100; }
  .badge-red { background: #ffebee; color: #c62828; }
  .footer { text-align: center; padding: 15px; color: #999; font-size: 12px; }
</style>
```

---

## Task Routing

### MODE 1: MONTHLY CALL DASHBOARD
**Trigger:** "Monthly call report" or "Call dashboard" or "How did [month] look?" or "March call report"

**Steps:**
1. Pull all calls for the target month via `search_crm_objects` (objectType: CALL, filter by `hs_timestamp`). Include `associations: ["COMPANY"]` for segment classification. Paginate through all pages (see `call-schema.md`).
2. **First pass (lightweight):** Use the counting property set (`hs_timestamp, hubspot_owner_id, hs_call_has_transcript, hs_call_duration`) to compute:
   - Total calls, vs. previous month (% change)
   - Calls by rep (group by `hubspot_owner_id`)
   - Calls by segment (via associated company `customer_segment`)
   - Calls with transcripts vs. without
   - Average call duration (ms -> minutes)
3. **Second pass (content):** Fetch `hs_call_summary` for calls that need use-case classification. Extract use cases (classify against use-case-taxonomy.md), rank by frequency.
4. Identify top companies by call volume
5. Render as HTML

**Output:** HTML dashboard with:
- **Header banner:** Month, total calls, vs. prior month
- **Metrics bar:** Total calls, unique companies, avg duration, transcript coverage %
- **Rep activity table:** Rep name, call count, unique companies, top segments, avg duration
- **Use case frequency table:** Rank, use case name, count, % of calls, vs. prior month trend
- **Segment breakdown table:** Segment, call count, % of total, top use cases in segment
- **Top companies table:** Company, segment, call count, most recent call date, use cases discussed
- **Footer:** Generated date, data source note

---

### MODE 2: TREND ANALYSIS (Multi-Month)
**Trigger:** "Call trends" or "How are use cases trending?" or "6-month call analysis" or "Call trends since October"

**Steps:**
1. Pull all calls across the requested time range (default: last 6 months or since Oct 2025). Include `associations: ["COMPANY"]`. Paginate through all pages (see `call-schema.md`). If data was already fetched in this conversation, reuse it.
2. Group by month, compute per month: total calls, calls by segment, use case frequency
3. Calculate month-over-month changes for each use case
4. Classify trends: RISING (3+ months of growth), FALLING (3+ months of decline), STABLE, NEW (appeared recently)
5. Show segment engagement trends over time
6. Render as HTML

**Output:** HTML report with:
- **Header:** Date range, total calls across period
- **Monthly overview table:** Month | Total Calls | vs. Prior Month
- **Use case trend table:** Use Case | [Month columns with count] | Trend Direction | % Change
- **Rising use cases callout:** Which topics are gaining momentum?
- **Falling use cases callout:** Which topics are declining?
- **Segment trend table:** Segment | [Month columns with call count] | Trend
- **Key observations:** Narrative summary of the most important trends

---

### MODE 3: DEALS vs. POCs CALL ANALYSIS
**Trigger:** "Call analysis for deals vs POCs" or "Separate deal and POC calls" or "How do conversations change through the pipeline?" or "Deal stage call analysis"

**Steps:**
1. Query deals in pre-POC stages (`appointmentscheduled`, `qualifiedtobuy`, `1996673735` -- see `deals-schema.md` for stage reference), then get their associated calls
2. Query open POC tickets, then get their associated calls
3. Query closed-won deals (`dealstage = closedwon`), then get their associated calls
4. For each group, extract use cases and compute frequency
5. Compare: which topics dominate in each pipeline phase? How does the conversation shift?
6. Render as HTML side-by-side comparison

**Output:** HTML report with:
- **Header:** "Conversation Evolution Through Pipeline"
- **Three-column comparison table:**

| Use Case | Pre-POC Calls (%) | POC Calls (%) | Post-Sale Calls (%) | Shift |
|----------|-------------------|--------------|--------------------|----|

- **Narrative insights:**
  - What topics appear in early calls but disappear during POC? (sales-stage topics)
  - What topics emerge during POC? (technical validation topics)
  - What topics surface post-sale? (expansion/deepening topics)
- **Implications for sales process:** What should reps focus on at each stage?

---

### MODE 4: AUDIENCE-SPECIFIC BRIEFING
**Trigger:** "Report for [person]" or "CEO briefing" or "Abilash update" or "Rep scorecard for Tim L" or "CRO report"

**Steps depend on audience:**

**CEO (Abilash Menon):**
1. Strategic overview: total call volume trend (3-month), segment momentum (which segments are getting more/fewer calls)
2. Competitive themes: which competitors are being mentioned in calls and how frequently
3. Use case demand signals: which capabilities are prospects asking about most
4. Pipeline health from call perspective: are we having enough conversations in each column?
5. Key wins and risks surfaced in recent calls

**CRO (Tim Ziemer):**
1. Build the 3-column pipeline board inline using the same logic as `pipeline-discipline/SKILL.md` Mode 1 (query pre-POC deals, open POC tickets, closed-won companies with expansion signals)
2. Add: call coverage analysis -- which accounts with open deals/POCs have gone quiet?
3. Add: rep comparison -- who's making more calls, who's covering more accounts
4. Add: stalled account alerts -- accounts with zero calls in 30+ days despite active pipeline

**Rep (Tim Lieto / Ken Cunningham):**
1. Their calls this period: count, companies, segments
2. Their top accounts by call frequency with deal/POC stage context
3. Use case coverage: which use cases are they discussing most?
4. Suggested follow-ups: accounts with open deals but no recent call
5. Segment distribution: are they covering their territory evenly?

**Output:** HTML briefing tailored to the audience. Use the header to indicate recipient:
- "STRATEGIC BRIEFING -- Prepared for Abilash Menon, CEO"
- "PIPELINE DISCIPLINE REPORT -- Prepared for Tim Ziemer, CRO"
- "REP SCORECARD -- Tim Lieto, East Region"

---

## Save to File Mode

When user says "save as file" or "download" or "export" or "write to file":
1. Generate the HTML report as normal
2. Write to disk at a sensible location (project root or user-specified path)
3. Filename convention: `maiaedge-call-report-[type]-[YYYY-MM-DD].html`
   - Examples: `maiaedge-call-report-monthly-2026-03-21.html`, `maiaedge-call-report-ceo-briefing-2026-03-21.html`

---

## When to Use This Skill

Trigger on any of these patterns:
- "Call report" or "Call dashboard" or "Monthly call summary"
- "Call trends" or "How are calls trending?" or "Use case trends"
- "CEO briefing" or "Abilash update" or "Strategic call report"
- "CRO report" or "Tim Z briefing" or "Pipeline discipline report"
- "Rep scorecard" or "Tim L activity" or "Ken's performance"
- "Deals vs POCs" or "How do conversations change?" or "Pipeline stage analysis"
- "Save call report" or "Export dashboard" or "Download call analysis"
- Any mention of: call dashboard, call report, trend report, briefing, scorecard
