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

## Design System

Inspired by Stripe/Linear aesthetics. Muted, professional, built for executive scanning. All reports are self-contained HTML -- no CDN, no JavaScript libraries, no external dependencies.

### Color Palette

**Neutrals (Slate scale -- foundation for all text, backgrounds, borders):**

| Token | Hex | Use |
|-------|-----|-----|
| Page background | `#F8FAFC` | Body background |
| Surface | `#F1F5F9` | Card backgrounds, table header bg, empty bar tracks |
| Border | `#E2E8F0` | Dividers, card borders, table row borders |
| Muted text | `#94A3B8` | Labels, secondary text, footer, table headers |
| Body text | `#475569` | Table cells, body copy |
| Heading text | `#1E293B` | Section titles, card titles |
| Hero text | `#0F172A` | KPI numbers, report title |

**Accent (single accent color -- used sparingly):**

| Token | Hex | Use |
|-------|-----|-----|
| Accent | `#6366F1` | Primary bar fills, active tab indicator, KPI highlights |
| Accent light | `#E0E7FF` | Accent backgrounds (KPI card bg when highlighted) |

**Status (desaturated, enterprise-grade -- never bright primary colors):**

| Status | Text | Background | Use |
|--------|------|------------|-----|
| Healthy | `#059669` | `#ECFDF5` | On track, active engagement |
| Watch | `#D97706` | `#FFFBEB` | Needs attention, approaching deadline |
| Risk | `#EA580C` | `#FFF7ED` | At risk, slipping |
| Critical | `#DC2626` | `#FEF2F2` | Blocked, overdue, dead |
| Unknown | `#94A3B8` | `#F1F5F9` | "--" values, insufficient data |

**Data series (for multi-category charts -- segments, reps):**

| Series | Hex | Assigned to |
|--------|-----|-------------|
| 1 | `#6366F1` | Colo (indigo) |
| 2 | `#0EA5E9` | Fiber (sky) |
| 3 | `#8B5CF6` | Neocloud (violet) |
| 4 | `#14B8A6` | Network Op (teal) |
| 5 | `#F59E0B` | MSP (amber) |

Segment-to-color mapping is fixed. Same segment = same color across every chart in every report.

### Typography

```
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
```

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Report title | 24px | 700 | `#0F172A` |
| Section heading | 18px | 600 | `#1E293B` |
| Card title | 14px | 600 | `#1E293B` |
| KPI number | 36px | 700 | `#0F172A` |
| KPI label | 12px | 500 | `#94A3B8` |
| KPI change indicator | 13px | 500 | status color |
| Table header | 11px | 600 | `#64748B` (uppercase, 0.4px letter-spacing) |
| Table cell | 13px | 400 | `#334155` |
| Bar label | 13px | 500 | `#475569` |
| Bar count | 13px | 600 | `#1E293B` |
| Badge text | 11px | 600 | status color |
| Alert text | 13px | 400 | `#475569` |
| Footer | 11px | 400 | `#94A3B8` |

All numeric values use `font-variant-numeric: tabular-nums` for column alignment.

### Spacing (8px grid)

| Element | Value |
|---------|-------|
| Page padding | 32px |
| Section gap | 32px |
| Card padding | 24px |
| Card margin (between cards) | 16px |
| KPI card gap | 16px |
| Table cell padding | 8px vertical, 16px horizontal |
| Bar row gap | 8px |
| Alert card gap | 8px |

### CSS Stylesheet

```html
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; background: #F8FAFC; color: #475569; line-height: 1.5; padding: 32px; }
  .container { max-width: 1100px; margin: 0 auto; }

  /* Header */
  .header { padding: 32px 0 24px 0; border-bottom: 1px solid #E2E8F0; margin-bottom: 32px; }
  .header h1 { font-size: 24px; font-weight: 700; color: #0F172A; letter-spacing: -0.3px; }
  .header .subtitle { font-size: 13px; color: #94A3B8; margin-top: 4px; }
  .header .prepared-for { font-size: 14px; color: #64748B; margin-top: 8px; }

  /* KPI cards row */
  .kpi-row { display: flex; gap: 16px; margin-bottom: 32px; }
  .kpi { flex: 1; background: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 20px 24px; }
  .kpi .value { font-size: 36px; font-weight: 700; color: #0F172A; font-variant-numeric: tabular-nums; line-height: 1.1; }
  .kpi .label { font-size: 12px; font-weight: 500; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.4px; margin-top: 4px; }
  .kpi .change { font-size: 13px; font-weight: 500; margin-top: 6px; }
  .kpi .change-up { color: #059669; }
  .kpi .change-down { color: #DC2626; }
  .kpi .change-flat { color: #94A3B8; }

  /* Section headings */
  .section { margin-bottom: 32px; }
  .section-title { font-size: 18px; font-weight: 600; color: #1E293B; margin-bottom: 16px; }

  /* Cards */
  .card { background: white; border: 1px solid #E2E8F0; border-radius: 8px; margin-bottom: 16px; overflow: hidden; }
  .card-title { padding: 16px 24px; font-size: 14px; font-weight: 600; color: #1E293B; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; }
  .card-title .note { font-weight: 400; font-size: 12px; color: #94A3B8; }
  .card-body { padding: 24px; }

  /* Tables */
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  th { padding: 8px 16px; text-align: left; font-weight: 600; font-size: 11px; color: #64748B; text-transform: uppercase; letter-spacing: 0.4px; border-bottom: 2px solid #E2E8F0; background: #F8FAFC; }
  td { padding: 8px 16px; border-bottom: 1px solid #F1F5F9; vertical-align: middle; color: #334155; }
  tr:hover { background: #F8FAFC; }
  td:first-child { font-weight: 500; color: #1E293B; }
  .num { text-align: right; font-variant-numeric: tabular-nums; }

  /* Badges */
  .badge { display: inline-block; padding: 2px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; }
  .badge-healthy { background: #ECFDF5; color: #059669; }
  .badge-watch { background: #FFFBEB; color: #D97706; }
  .badge-risk { background: #FFF7ED; color: #EA580C; }
  .badge-critical { background: #FEF2F2; color: #DC2626; }
  .badge-unknown { background: #F1F5F9; color: #94A3B8; }

  /* Trend indicators */
  .trend-up { color: #059669; font-weight: 500; }
  .trend-down { color: #DC2626; font-weight: 500; }
  .trend-flat { color: #94A3B8; }

  /* Horizontal bar chart */
  .bar-chart { padding: 8px 0; }
  .bar-row { display: flex; align-items: center; margin-bottom: 8px; }
  .bar-label { width: 180px; font-size: 13px; font-weight: 500; color: #475569; flex-shrink: 0; }
  .bar-track { flex: 1; height: 22px; background: #F1F5F9; border-radius: 4px; overflow: hidden; }
  .bar-fill { height: 100%; border-radius: 4px; background: #6366F1; }
  .bar-count { width: 50px; text-align: right; font-size: 13px; font-weight: 600; color: #1E293B; margin-left: 12px; font-variant-numeric: tabular-nums; flex-shrink: 0; }

  /* Stacked bar */
  .stacked-bar { display: flex; height: 24px; border-radius: 4px; overflow: hidden; }
  .stacked-segment { display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 600; color: white; min-width: 24px; }

  /* Health distribution bar (single horizontal stacked bar) */
  .health-bar { display: flex; height: 8px; border-radius: 4px; overflow: hidden; margin-top: 8px; }
  .health-bar div { height: 100%; }

  /* Data completeness bar (inline in table cells) */
  .data-bar { display: inline-flex; align-items: center; gap: 6px; }
  .data-track { width: 48px; height: 4px; background: #E2E8F0; border-radius: 2px; overflow: hidden; }
  .data-fill { height: 100%; border-radius: 2px; }
  .data-fill-good { background: #059669; }
  .data-fill-partial { background: #D97706; }
  .data-fill-poor { background: #DC2626; }
  .data-pct { font-size: 12px; color: #64748B; font-variant-numeric: tabular-nums; }

  /* Alerts */
  .alert { padding: 10px 16px; margin-bottom: 8px; border-radius: 6px; font-size: 13px; border-left: 3px solid; color: #475569; }
  .alert-critical { background: #FEF2F2; border-color: #DC2626; }
  .alert-risk { background: #FFF7ED; border-color: #EA580C; }
  .alert-watch { background: #FFFBEB; border-color: #D97706; }
  .alert-info { background: #EFF6FF; border-color: #6366F1; }
  .alert-neutral { background: #F8FAFC; border-color: #E2E8F0; }
  .alert strong { color: #1E293B; }

  /* Layout helpers */
  .row { display: flex; gap: 16px; }
  .col { flex: 1; }
  .col .card { height: 100%; margin-bottom: 0; }

  /* Tabs */
  .tabs { display: flex; gap: 0; border-bottom: 1px solid #E2E8F0; margin-bottom: 32px; }
  .tab { background: none; border: none; padding: 12px 20px; font-size: 14px; font-weight: 500; color: #94A3B8; cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -1px; }
  .tab:hover { color: #475569; }
  .tab.active { color: #6366F1; border-bottom-color: #6366F1; }
  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* Footer */
  .footer { text-align: center; padding: 32px 0 16px 0; font-size: 11px; color: #94A3B8; border-top: 1px solid #E2E8F0; margin-top: 32px; }

  /* Print */
  @media print {
    body { background: white; padding: 16px; }
    .card { border: 1px solid #E2E8F0; }
    .tabs { display: none; }
    .tab-content { display: block !important; page-break-inside: avoid; }
    .bar-fill, .stacked-segment, .health-bar div, .data-fill { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  }
</style>
```

### When to Use Each Format

| Data | Format | Why |
|------|--------|-----|
| 1 hero number (total calls, avg duration) | KPI card | Scannable in 1 second |
| 3-15 ranked items (use cases, reps, segments) | Horizontal bar chart + table below | Bar = visual ranking, table = exact values |
| Distribution (5 segments, health split) | Single horizontal stacked bar with legend | Compact, shows proportions without SVG complexity |
| Month-over-month trend | Arrow + % change in table cell | Simpler than sparklines, more reliable to render |
| Detailed per-account data (pipeline board) | Table only | Too many dimensions for a chart |
| Progress / completeness | Inline bar in table cell | Shows proportion at a glance within the row |
| Alerts / action items | Left-border cards | Distinct from data, reads as "do something about this" |

**Rule: charts summarize, tables provide precision.** Show both when a chart is used. Never show a chart without the exact numbers accessible.

**Rule: one insight per section.** Each card/section answers one question. Title the section with the insight, not the chart type. "Cloud On-Ramp leads use case mentions" not "Use Case Frequency Chart."

### Chart Examples

**Horizontal bar chart (CSS-only):**
```html
<div class="bar-chart">
  <div class="bar-row">
    <span class="bar-label">Cloud On-Ramp</span>
    <div class="bar-track"><div class="bar-fill" style="width:100%"></div></div>
    <span class="bar-count">34</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">Federation</span>
    <div class="bar-track"><div class="bar-fill" style="width:79%"></div></div>
    <span class="bar-count">27</span>
  </div>
  <div class="bar-row">
    <span class="bar-label">DC Interconnection</span>
    <div class="bar-track"><div class="bar-fill" style="width:65%"></div></div>
    <span class="bar-count">22</span>
  </div>
</div>
```
Width = (value / max value) * 100. Top bar is always 100%. Count always shown to the right. Use accent color `#6366F1` for all bars unless comparing segments (then use segment colors).

**Stacked distribution bar (for health, segments, phases):**
```html
<div style="display:flex; align-items:center; gap:12px;">
  <div class="health-bar" style="flex:1;">
    <div style="width:25%; background:#059669;"></div>
    <div style="width:25%; background:#D97706;"></div>
    <div style="width:25%; background:#EA580C;"></div>
    <div style="width:15%; background:#DC2626;"></div>
    <div style="width:10%; background:#E2E8F0;"></div>
  </div>
  <span style="font-size:12px; color:#94A3B8;">1 GREEN, 1 YELLOW, 1 ORANGE, 1 RED, 1 --</span>
</div>
```

**Data completeness (inline in table):**
```html
<td>
  <span class="data-bar">
    <span class="data-track"><span class="data-fill data-fill-partial" style="width:65%"></span></span>
    <span class="data-pct">65%</span>
  </span>
</td>
```

**Trend indicator (in table cell):**
```html
<td class="num"><span class="trend-up">+40% (8 -> 11)</span></td>
```

---

**Visual rules:**
- White background cards on `#F8FAFC` page -- no dark headers, no colored banners
- Health badges and trend arrows are the only color in table rows
- Numbers always include context: "75% (3/4)" not "75%"
- Section titles state the insight: "Arvig POC is 6 days overdue" not "POC Health Table"
- Alerts use left-border cards sorted by severity (critical first)
- Footer: "Generated [date] | Data: HubSpot CRM | Use cases classified from call summaries"
- No emojis, no icons, no decorative elements
- Maximum 6 KPI cards in a row
- Bar charts limited to top 10 items; full list in table below

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

**Output:** HTML dashboard:
- **Header:** Report title, month, prepared-for line (if audience-specific)
- **KPI row (4 cards):** Total Calls (with vs. prior month change), Unique Companies, Avg Duration (minutes), Transcript Coverage %
- **Section: "Use cases driving conversations"** -- Bar chart (top 10) + ranked table with count, % of calls, vs. prior month trend arrow
- **Section: "Activity by rep"** -- Bar chart (calls per rep) + detail table: rep, call count, unique companies, top segments
- **Section: "Segment breakdown"** -- Stacked distribution bar + table: segment, count, %, top use cases
- **Section: "Most active accounts"** -- Table: company, segment, call count, most recent date, use cases
- **Footer**

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

**Output:** HTML report:
- **Header:** Date range, total calls across period
- **KPI row (3 cards):** Total Calls (period), Avg Monthly Volume, Most Active Segment
- **Section: "Monthly call volume"** -- Bar chart (one bar per month, count to the right)
- **Section: "Use case momentum"** -- Table: Use Case | [Month columns with count] | Trend arrow + % change. Highlight rows where trend is RISING (3+ months growth) or FALLING (3+ months decline)
- **Section: "Segment engagement over time"** -- Table: Segment | [Month columns] | Trend arrow
- **Section: "Key observations"** -- 3-5 bullet points, every statement cites specific data ("Cloud On-Ramp increased 40%, from 8 calls in Jan to 11 in Mar")

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

### MODE 5: EXECUTIVE DASHBOARD (Tabbed)
**Trigger:** "Full dashboard" or "Executive dashboard" or "All reports" or "Weekly dashboard" or "Build me the dashboard"

This is the single-artifact output. One HTML file with tabs -- click through views without asking for separate reports.

**Steps:**
1. Fetch all call data for the period once (default: current month + 2 prior months for trend). Paginate fully. Reuse data across all tabs.
2. Fetch all open deals with associations, all open POC tickets with full property set, all closed-won deals
3. Build all tabs from the same data set -- no redundant queries

**Tabs:**

| Tab | Label | Layout |
|-----|-------|--------|
| 1 | Pipeline | KPI row (accounts in each column, total pipeline value). 3-column pipeline board tables. Engagement badges, alert cards below. |
| 2 | POC Status | KPI row (open POCs, avg data completeness). Health distribution stacked bar. SE workload bar chart. All open POCs table (sorted by health). Stage dwell table with benchmark comparison. Data gaps table. |
| 3 | Calls | KPI row (total calls, unique companies, avg duration, transcript %). Use case bar chart + table. Rep activity bar chart + table. Segment stacked bar + table. Top companies table. |
| 4 | Trends | KPI row (total calls this period, avg monthly, most active segment). Monthly volume bar chart. Use case trend table with arrows. Segment trend table with arrows. Key observations. |
| 5 | Pipeline Phases | Stacked comparison bars per phase. Side-by-side table. Narrative insights on conversation evolution. |

**Tab HTML pattern:**
```html
<div class="tabs">
  <button class="tab active" onclick="showTab('pipeline')">Pipeline</button>
  <button class="tab" onclick="showTab('poc')">POC Status</button>
  <button class="tab" onclick="showTab('calls')">Calls</button>
  <button class="tab" onclick="showTab('trends')">Trends</button>
  <button class="tab" onclick="showTab('phases')">Pipeline Phases</button>
</div>
<div id="pipeline" class="tab-content active">...</div>
<div id="poc" class="tab-content">...</div>
...
<script>
function showTab(id) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  event.target.classList.add('active');
}
</script>
```

Tab styles are included in the base CSS stylesheet above. Tabs use underline indicator with accent color `#6366F1` on a clean white/slate background -- no dark nav bar.

**Output:** Single self-contained HTML file. No external dependencies. All data embedded. Default header: "MaiaEdge Sales Intelligence" with date and optional recipient name below.

---

## Data Reliability Rules

These rules apply to ALL modes. Reports go to leadership -- accuracy is non-negotiable.

**Only show data you queried.** Never populate a table cell with assumed, estimated, or placeholder data. If a HubSpot query returned a value, show it. If it returned null or was not queried, show "--".

**Show counts and sample sizes.** Whenever displaying a percentage, rate, or average, show the underlying count. "Success Rate: 75% (3/4)" not just "75%." This lets the reader judge reliability.

**Suppress unreliable metrics.** If a breakdown has fewer than 3 data points, show "--" instead of a number. One closed POC does not make a "100% success rate."

**No narrative without evidence.** Every sentence in insights/observations must reference specific data from the report. "Cloud On-Ramp calls increased 40% (8 -> 11)" not "Cloud On-Ramp is trending upward."

**Label the data window.** Every table header or section title must include the date range it covers. "Calls: March 2026" not just "Calls."

**Distinguish hard data from soft data:**
- Hard: HubSpot property values, timestamps, counts, stage names, owner IDs
- Soft: Use case classification from call summaries (Claude interpreting text)
- Always label use case data as "classified from call summaries" in table footers

**No duplicate counting.** When a call has multiple associated objects (company + deal + POC), count it once. Attribute to the most specific: POC if POC exists, deal if deal exists, company otherwise.

**Blank field handling (inherited from pipeline-discipline):**
- Blank = "--" in tables, never inferred values
- Health scores only use filled fields
- Data completeness shown as separate column, not mixed into health

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
- "Full dashboard" or "Executive dashboard" or "All reports" or "Weekly dashboard" or "Build me the dashboard"
- "Save call report" or "Export dashboard" or "Download call analysis"
- Any mention of: call dashboard, call report, trend report, briefing, scorecard, executive dashboard
