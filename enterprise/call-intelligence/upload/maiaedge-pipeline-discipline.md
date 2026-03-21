---
name: pipeline-discipline
description: "MaiaEdge pipeline discipline engine. The CRO's primary tool for tracking account conversion through three pipeline columns: (1) accounts converting to POC, (2) POCs converting to purchase orders, (3) initial orders expanding. Combines deal pipeline data, POC ticket status, and call intelligence to produce actionable conversion boards. Use when asked about pipeline discipline, conversion pipeline, what's converting, 3-column view, weekly pipeline briefing, or conversion velocity."
---

# MaiaEdge Pipeline Discipline

## Purpose

Track account conversion through the three critical pipeline stages that matter for revenue. This is the CRO's primary operating view -- not a pipeline snapshot (see pipeline-analytics for that), but a **conversion discipline tool** that answers: what accounts are we actively converting, and what's the next action on each?

This skill combines deal pipeline data, POC ticket status, call intelligence, and engagement recency to produce the three-column view.

---

## The Three Columns

```
COLUMN 1                    COLUMN 2                    COLUMN 3
Accounts -> POC             POCs -> Purchase Order      Orders -> Expansion
───────────────────         ───────────────────         ───────────────────
Pre-POC deals +             Open POC tickets            Any company with
momentum accounts           converting to PO            closed-won history
(no deal required)
```

---

## Reference

### Deal Stages -> Column Mapping

See `deals-schema.md` for full stage reference. Column assignment for pipeline discipline:

| Stage | Internal Name | Column | Notes |
|-------|---------------|--------|-------|
| Appointment Scheduled | `appointmentscheduled` | 1 | |
| Discovery & Scoping | `qualifiedtobuy` | 1 | |
| POC & Technical Validation | `presentationscheduled` | 2 (deal side) | |
| Quote Provided | `1996673735` | 1 or 2 | Pre-POC if no POC ticket exists; Column 2 if POC is active |
| Price Agreement | `decisionmakerboughtin` | transition 2->3 | |
| Contract Review | `contractsent` | transition 2->3 | |
| Closed Won | `closedwon` | 3 | |

### POC Ticket Stages (Column 2)

See `poc-schema.md` for full stage mapping. Key stages:
- Requested, Scoping, Criteria Approved, Configuration Locked = early POC
- Building & Preparing, Shipped, Customer Testing = active POC
- Successful = ready for PO conversion

### POC Owners

POC tickets are owned by the SE/support team, not sales reps:
- **Kyle Blackwell** (Sales Engineering, owner ID `159701452`) -- primary POC owner
- **Woody Acosta** (Sales Support, owner ID `162281129`) -- secondary POC owner

When surfacing Column 2 data, always show the POC owner alongside the sales rep who owns the associated deal. Both need visibility into slippage.

### POC Health Scoring (Column 2)

Every POC in Column 2 gets a health assessment based on multiple signals from `poc-schema.md` properties:

**Timeline Signals:**
| Signal | Property | Condition | Severity |
|--------|----------|-----------|----------|
| Overdue | `poc_end_date` | End date is in the past, ticket still open | RED |
| Approaching deadline | `poc_end_date` | Within 7 days of end date | YELLOW |
| No end date set | `poc_end_date` | Null/empty | YELLOW -- no accountability |
| Long-running | `poc_start_date` | Started 60+ days ago, not in terminal stage | ORANGE |

**Trend Signals (from `poc_trend` dropdown):**
| poc_trend Value | Health | Action |
|----------------|--------|--------|
| On Track | GREEN | No action needed |
| Needs Attention | YELLOW | Flag for review |
| At Risk | ORANGE | Escalation recommended |
| Blocked | RED | Immediate action required -- surface blocker reason |
| On Hold | GRAY | Investigate why paused, check for staleness |

**Site Readiness Signals:**
For each site (up to `poc_number_of_sites`), check the 4 readiness checkboxes:
- `site_N_mgmt_connectivity` -- management connectivity confirmed
- `site_N_egress_allowlists` -- egress allow-lists approved
- `site_N_dia_confirmed` -- DIA confirmed
- `site_N_site_ready` -- overall site ready

| Readiness | Condition | Severity |
|-----------|-----------|----------|
| Site not ready | POC in "Customer Testing" but any `site_N_site_ready` = false | RED -- testing on unready site |
| Partial readiness | POC in "Shipped" or later but <50% readiness checkboxes complete | ORANGE |
| Pre-ship ready | POC in "Building & Preparing" and all checkboxes complete | GREEN -- ready for next stage |

**Exit Criteria Signals:**
| Signal | Condition | Severity |
|--------|-----------|----------|
| No success criteria | `poc_success_criteria` is empty | RED -- POC has no definition of success |
| Approval blocked | `poc_approval_status` = Denied | RED -- POC should not proceed |
| Conditional approval | `poc_approval_status` = Conditional Approval | YELLOW -- check conditions |
| Pending approval | POC past "Criteria Approved" stage but `poc_approval_status` still Pending | ORANGE |

**Issue Accumulation:**
| Signal | Condition | Severity |
|--------|-----------|----------|
| Bug pile-up | `poc_bugs` contains 3+ distinct issues | ORANGE |
| Feature creep | `poc_feature_requests` contains 3+ requests | YELLOW -- scope expanding |
| Both accumulating | 3+ bugs AND 3+ feature requests | RED -- POC is struggling |

**Combined POC Health (worst signal wins):**
| Health | Visual | Meaning |
|--------|--------|---------|
| GREEN | On Track | Timeline, trend, readiness all healthy |
| YELLOW | Watch | Minor concerns -- approaching deadline, needs attention, partial readiness |
| ORANGE | Slipping | Multiple warnings -- long-running, at risk trend, readiness gaps, pending approval |
| RED | Critical | Overdue, blocked, no success criteria, site not ready during testing, approval denied, bug pile-up |
| GRAY | Paused | On Hold -- check if it's been paused 30+ days (may be dead) |

### Handling Blank Fields

**Principle: report what we know, flag what we don't. Never guess.**

When a POC property is null/empty, do NOT infer a value. Instead, use these rules:

**Fields with reliable HubSpot auto-data (always available):**
- `createdate` -- HubSpot auto-populates. Use as "Days since created" when `poc_start_date` is blank.
- `hs_pipeline_stage_timestamp_*` -- HubSpot records stage entry timestamps. Always use these for "Days in stage" calculations. This is hard data, not inference.
- `hubspot_owner_id` -- if blank, show "Unassigned" (do not default to Kyle).

**Fields that are blank -- show clean labels, not guesses:**
| Field | When Blank, Show |
|-------|-----------------|
| `poc_trend` | "--" (do not infer a trend) |
| `poc_end_date` | "Not set" |
| `poc_start_date` | Use `createdate` with label "Created [date]" |
| `poc_success_criteria` | "Not defined" |
| `poc_number_of_sites` | "--" |
| `poc_bugs` | "--" |
| `poc_feature_requests` | "--" |
| Site readiness checkboxes | "Not started" if post-build stage; omit if pre-build stage |
| Exit criteria checkboxes | "Not started" |

**Health scoring with missing data:**
- Only score categories where data exists. Do not penalize or elevate health based on missing fields.
- If `poc_trend` is blank, exclude trend from health calculation -- health is determined only by timeline (from stage timestamps), readiness, exit criteria, and issue signals that ARE filled.
- If too few signals exist to score health (only stage timestamps available), show health as "--" rather than forcing a color.
- Timeline signals from `createdate` and stage timestamps are always valid (HubSpot auto-populates these) and can always contribute to health.

**Data completeness drives follow-up, not health color:**
- Low data completeness is surfaced in reporting as its own column, not folded into the health score.
- The weekly briefing calls out POCs with low completeness as an action item: "[Company] POC data incomplete -- [list missing fields]"
- This keeps health scores trustworthy (based only on real data) while still creating pressure to fill fields.

### POC Data Completeness Score

For each POC, calculate a fill rate across the key fields and show it in reporting. This creates visibility into data hygiene without blocking the health assessment.

| Field | Weight | Why |
|-------|--------|-----|
| `poc_trend` | 15% | Core health signal |
| `poc_success_criteria` | 15% | Definition of done |
| `poc_start_date` | 10% | Timeline tracking |
| `poc_end_date` | 10% | Accountability |
| `poc_next_step` | 10% | Operational clarity |
| `poc_approval_status` | 10% | Governance |
| `poc_number_of_sites` | 5% | Scope |
| Site readiness (any) | 10% | Deployment tracking |
| `poc_bugs` or `poc_feature_requests` | 5% | Issue tracking |
| Exit criteria (any checkbox) | 10% | Closeout readiness |

Show as: `Data: 65%` in the POC row. Color code: 80%+ = good, 50-79% = partial, <50% = poor.

In weekly briefings, add a one-line summary: "POC data completeness: [N]% average across [N] open POCs. Lowest: [company] at [N]%."

### Activity Gate (Two-Way Engagement)

See `call-schema.md` "Activity Gate (Engagement Health)" for full rules, thresholds, and query instructions.

**Quick reference -- Combined Assessment:**

| Outbound | Inbound | Status |
|----------|---------|--------|
| Active (14d) | Active (14d) | HEALTHY |
| Active (14d) | Stale (30+d) | AT RISK |
| Stale (30+d) | Active (14d) | INBOUND OPP |
| Stale (30+d) | Stale (30+d) | DEAD |

---

## Task Routing

### MODE 1: THREE-COLUMN PIPELINE BOARD
**Trigger:** "Pipeline discipline" or "3-column view" or "Conversion pipeline" or "What's converting?" or "Pipeline board"

**Steps:**

**Column 1 -- Accounts Converting to POC:**
1. Query open deals in pre-POC stages (`appointmentscheduled`, `qualifiedtobuy`, `1996673735`) via `search_crm_objects` with `associations: ["COMPANY", "CONTACT"]`. See `deals-schema.md` for stage reference.
2. For each deal's associated company, query recent calls with `associations: ["COMPANY"]` to get latest call context
3. ALSO query companies with multiple recent calls (2+ in last 30 days) but NO deal yet -- these are momentum accounts gaining traction from conversations
4. For each account, extract from most recent call: use cases discussed, next step, engagement signal
5. Rank by: (a) deal value if available, (b) call recency, (c) call frequency
6. Show top 10

**Column 2 -- POCs Converting to Purchase Order:**
1. Query open POC tickets (pipeline: POC pipeline, not in terminal stages) with `associations: ["COMPANY", "DEAL", "CONTACT"]`. Request properties: `poc_trend, poc_next_step, poc_start_date, poc_end_date, poc_number_of_sites, poc_success_criteria, poc_approval_status, poc_bugs, poc_feature_requests, poc_proof_points_validated, poc_hardware_validated, poc_customer_signoff, poc_go_nogo_documented, hubspot_owner_id`
2. For each POC, also fetch site readiness properties for all sites up to `poc_number_of_sites`: `site_N_site_ready, site_N_mgmt_connectivity, site_N_egress_allowlists, site_N_dia_confirmed`
3. From associations, get: company (name, segment), deal (amount, stage, owner -- this is the sales rep)
4. Note the POC ticket owner (Kyle Blackwell or Woody Acosta) separately from the deal owner (sales rep)
5. Run POC Health Scoring (see reference section) using only categories where data exists. Use stage timestamps (auto-populated) for timeline. If too few signals to score health, show "--" instead of forcing a color.
6. Query recent calls associated with the company for POC status updates -- extract: use cases being validated, blockers mentioned, technical progress
7. Apply two-way engagement assessment (see Activity Gate) using both the sales rep's and the POC owner's activity
8. Rank by: (a) POC health severity (RED first, then ORANGE, YELLOW, GREEN), (b) days overdue or approaching deadline, (c) deal value
9. Show top 10

**Column 3 -- Initial Orders Expanding:**
1. Query deals where `dealstage = closedwon` with `associations: ["COMPANY"]`. De-duplicate associated company IDs to get the customer list.
2. For each customer company, check for: additional open deals, new POC tickets, recent calls
3. Pull recent calls and scan for expansion signals: new use cases, additional sites, new contacts engaging, mentions of scaling/expanding/adding
4. Flag companies with expansion potential but no active deal or POC
5. Rank by: (a) initial deal value, (b) expansion signal strength, (c) call recency
6. Show top 10

**Output:**
```
PIPELINE DISCIPLINE BOARD — [Date]
======================================
Rep: [All / specific rep] | Period: [date range for call data]

COLUMN 1: ACCOUNTS -> POC ([N] accounts)
──────────────────────────────────────────
| # | Company | Segment | Deal Stage | Value | Last Outbound | Last Inbound | Use Cases | Next Step | Engagement |
|---|---------|---------|-----------|-------|---------------|--------------|-----------|-----------|-----------|
| 1 | [name] | [seg] | [stage] | $[X] | [date] | [date] | [use cases] | [from call] | [HEALTHY] |
| 2 | [name] | [seg] | No Deal | — | [date] | [date] | [use cases] | [from call] | [AT RISK] |
...

COLUMN 2: POCs -> PURCHASE ORDER ([N] POCs)
──────────────────────────────────────────────
| # | Company | Segment | POC Stage | Health | Trend | Days in Stage | End Date | Sites Ready | Data | POC Owner | Sales Rep | Validating | Engagement |
|---|---------|---------|----------|--------|-------|---------------|----------|-------------|------|-----------|-----------|-----------|-----------|
| 1 | [name] | [seg] | [stage] | [RED] | [trend] | [N] | [date/OVERDUE] | [2/3] | [65%] | [name] | [name] | [use cases] | [HEALTHY] |

When fields are blank, show clean labels per the "Handling Blank Fields" rules. Never show raw nulls or placeholder asterisks in output.
...

COLUMN 3: ORDERS -> EXPANSION ([N] customers)
────────────────────────────────────────────────
| # | Company | Segment | Initial Deal | Won Date | Expansion Signals | Open Deals/POCs | Last Outbound | Last Inbound | Engagement |
|---|---------|---------|-------------|----------|-------------------|-----------------|---------------|--------------|-----------|
| 1 | [name] | [seg] | $[X] | [date] | [signals from calls] | [N] deals, [N] POCs | [date] | [date] | [HEALTHY] |
...

MOMENTUM RISK ALERTS
- [Company] AT RISK: We've sent 3 emails in 14 days, no response (Column 1)
- [Company] GOING DARK: Last inbound response 35 days ago despite active outreach (Column 2)
- [Company] ONE-SIDED: 5 outbound touches, 1 inbound response in 30 days (Column 1)
- [Company] INBOUND OPP: They emailed us 3 days ago but we haven't responded (Column 3)

POC ALERTS (only when backed by HubSpot data)
- [Company] POC OVERDUE: End date was [date], still in [stage] ([N] days overdue)
- [Company] POC BLOCKED: poc_trend = Blocked, [N] days in current stage
- [Company] SITE NOT READY: In Customer Testing but [N] of [N] sites missing readiness checks
- [Company] APPROVAL DENIED: poc_approval_status = Denied
- [Company] APPROVAL STALLED: Past Criteria Approved stage but poc_approval_status still Pending
- [Company] POC ON HOLD [N] DAYS: Entered On Hold on [date]
- [Company] POC READY FOR PO: POC Successful -- no active deal in next stage
- [Company] STAGE STALLED: [N] days in [stage] (avg for this stage: [N] days)
- [Company] POC DATA INCOMPLETE: [list specific missing fields]

Rules for alerts:
- Every alert must cite the specific HubSpot property and value that triggered it
- Stage dwell alerts use hs_pipeline_stage_timestamp (auto-populated) compared to closed-POC benchmarks -- this is measured, not guessed
- Do NOT generate alerts from blank fields. A blank poc_trend does not mean "At Risk" -- it means trend is unknown. Surface it under data completeness, not health alerts.

ACTION ITEMS
- [Company] needs follow-up call (Column 1, 18 days since last contact)
- [Company] POC is At Risk (Column 2, blocked on [issue])
- [Company] showing expansion signals but no active deal (Column 3)
- [Company] prospect going dark -- consider executive escalation or new angle (Column 1)
```

---

### MODE 2: CONVERSION VELOCITY
**Trigger:** "How fast are accounts converting?" or "POC conversion rate" or "Pipeline velocity by stage" or "Conversion speed"

**Steps:**
1. Calculate average time from deal creation to POC ticket creation (Col 1 -> Col 2 transition)
2. Calculate average POC duration from start to successful completion (Col 2 throughput)
3. Calculate average time from first closed-won deal to expansion deal creation (Col 3 cycle)
4. Break down each metric by segment
5. Identify fastest and slowest conversions for pattern analysis

**Output:**
```
CONVERSION VELOCITY — [Date Range]
=====================================

| Transition | Avg Days | Fastest | Slowest | By Segment |
|-----------|---------|---------|---------|-----------|
| Account -> POC | [N] | [company, N days] | [company, N days] | Colo: [N], Fiber: [N], ... |
| POC -> PO | [N] | [company, N days] | [company, N days] | Colo: [N], Fiber: [N], ... |
| First Order -> Expansion | [N] | [company, N days] | [company, N days] | Colo: [N], Fiber: [N], ... |

BOTTLENECK ANALYSIS
[Which transition is slowest? Why? What do the call summaries reveal?]
```

---

### MODE 3: WEEKLY PIPELINE BRIEFING
**Trigger:** "Weekly pipeline briefing" or "Pipeline update for Tim Z" or "CRO briefing" or "Weekly discipline report"

**Steps:**
1. Run all three columns (Mode 1)
2. Compare to prior week: new accounts entering Column 1, accounts that moved between columns, accounts that fell out
3. Highlight stalled accounts: in Column 1 or 2 with no call activity in 14+ days
4. Identify accounts at risk: POCs with `poc_trend` = "At Risk" or "Blocked"
5. Generate recommended actions for the week

**Output:**
```
WEEKLY PIPELINE DISCIPLINE BRIEFING
======================================
Week of [date] | Prepared for: [CRO / name]

MOVEMENT THIS WEEK
- NEW in Column 1: [N] accounts ([company names])
- PROMOTED Col 1 -> Col 2: [N] ([company names])
- PROMOTED Col 2 -> Col 3: [N] ([company names])
- DROPPED OUT: [N] ([company names + reason])

[Full 3-column board from Mode 1]

STALLED ACCOUNTS (no call in 14+ days)
| Company | Column | Days Since Last Call | Deal/POC Stage | Recommended Action |
|---------|--------|---------------------|----------------|-------------------|

POC HEALTH REPORT
| Company | POC Stage | Health | Trend | Days in Stage | End Date | Issues | Sites Ready | POC Owner | Sales Rep | Last Call |
|---------|----------|--------|-------|---------------|----------|--------|-------------|-----------|-----------|----------|
[All non-GREEN POCs listed here with their health signals]

POC ALERTS
[All alerts from Mode 1 -- each backed by specific HubSpot property values]

POC DATA GAPS
[POCs below 50% completeness with specific missing fields -- action item, not health penalty]

THIS WEEK'S PRIORITIES
1. [Action] — [Company] — [Why]
2. [Action] — [Company] — [Why]
3. [Action] — [Company] — [Why]
```

---

### MODE 4: POC OPERATIONS REPORT
**Trigger:** "POC report" or "POC status" or "How are our POCs doing?" or "SE workload" or "Kyle's POCs" or "Woody's POCs" or "POC analytics"

**Steps:**

**POC Summary Dashboard:**
1. Query all open POC tickets with full property set (same as Column 2 Mode 1)
2. Query all closed POC tickets (Successful + Unsuccessful) from last 6 months for benchmarks
3. For each open POC, run health scoring using only filled fields. Show "--" for health when insufficient data.

**SE Workload:**
1. Group open POCs by ticket owner (Kyle vs Woody)
2. For each: count of POCs, health distribution, total sites across all POCs
3. Flag overload: 5+ active POCs per SE = capacity concern

**POC Conversion Funnel:**
1. From closed POCs: calculate success rate (Successful / total closed)
2. Break down by segment, by POC objective (`poc_type`), by number of sites
3. Calculate average POC duration (createdate to close date) by segment
4. Identify patterns: which segments/objectives convert best?

**Stage Dwell Analysis:**
1. For each open POC, calculate days in current stage using `hs_pipeline_stage_timestamp_*`
2. Compare to average dwell time per stage (from closed POCs)
3. Flag POCs dwelling 2x longer than average for their current stage

**Call Coverage During POC:**
1. For each open POC's associated company, count calls during the POC period
2. Flag POCs with zero calls in last 14 days
3. Flag POCs with no call from the SE owner (Kyle/Woody) -- only sales rep calling

**Output:**
```
POC OPERATIONS REPORT — [Date]
================================

OPEN POCs: [N] | Data Completeness: [N]% avg

SE WORKLOAD
| Owner | Open POCs | RED | ORANGE | YELLOW | GREEN | Total Sites | Capacity |
|-------|----------|-----|--------|--------|-------|-------------|----------|
| Kyle Blackwell | [N] | [N] | [N] | [N] | [N] | [N] | [OK/AT CAPACITY/OVERLOADED] |
| Woody Acosta | [N] | [N] | [N] | [N] | [N] | [N] | [OK/AT CAPACITY/OVERLOADED] |

ALL OPEN POCs (sorted by health severity)
| Company | Segment | Stage | Health | Trend | Days in Stage | Avg for Stage | End Date | Sites | Data% | POC Owner | Sales Rep |
|---------|---------|-------|--------|-------|---------------|---------------|----------|-------|-------|-----------|-----------|
[All open POCs listed]

STAGE DWELL ANALYSIS
| POC Stage | Avg Days (benchmark) | Open POCs in Stage | Over Benchmark |
|-----------|---------------------|-------------------|----------------|
| Requested | [N] | [N] | [list companies 2x+ over avg] |
| Scoping | [N] | [N] | [list] |
| Criteria Approved | [N] | [N] | [list] |
...

POC CONVERSION BENCHMARKS (last 6 months, N=[total closed POCs])
| Metric | Overall | Colo | Fiber | Neocloud | Network Op | MSP |
|--------|---------|------|-------|----------|-----------|-----|
| Success Rate | [N]% | [N]% | [N]% | [N]% | [N]% | [N]% |
| Avg Duration (days) | [N] | [N] | [N] | [N] | [N] | [N] |
| Avg Sites | [N] | [N] | [N] | [N] | [N] | [N] |
Note: Show "--" for any segment with fewer than 3 closed POCs. Sample too small to benchmark.

BY POC OBJECTIVE
| Objective | Count | Success Rate | Avg Duration |
|-----------|-------|-------------|-------------|
| Fiber Monetization | [N] | [N]% | [N] days |
| Speed to Revenue | [N] | [N]% | [N] days |
| Network Extension | [N] | [N]% | [N] days |
| Private Connectivity | [N] | [N]% | [N] days |
| Competitive Displacement | [N] | [N]% | [N] days |

CALL COVERAGE DURING POC
| Company | POC Stage | Days Since Last Call | Calls During POC | SE Calls | Sales Calls | Gap |
|---------|----------|---------------------|-----------------|----------|------------|-----|
[Only POCs with coverage concerns -- no recent calls, no SE calls, or lopsided coverage]

DATA COMPLETENESS
| Company | Score | Missing Fields |
|---------|-------|---------------|
[POCs below 50% completeness with specific missing fields listed]

RECOMMENDATIONS
1. [Action] — [Company] — [Why]
2. [Action] — [Company] — [Why]
3. [Action] — [Company] — [Why]
```

---

## When to Use This Skill

Trigger on any of these patterns:
- "Pipeline discipline" or "3-column" or "Conversion pipeline" or "What's converting?"
- "Accounts to POC" or "POCs to PO" or "Expansion opportunities"
- "Weekly pipeline briefing" or "CRO briefing" or "Tim Z update"
- "Conversion velocity" or "How fast are we converting?" or "Pipeline speed"
- "POC report" or "POC status" or "How are our POCs?" or "SE workload" or "Kyle's POCs" or "Woody's POCs"
- Any mention of: conversion board, pipeline columns, discipline board, account progression, POC health, POC analytics, POC operations
