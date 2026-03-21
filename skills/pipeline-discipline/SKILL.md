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
1. Query open POC tickets (pipeline: POC pipeline, not in terminal stages) with `associations: ["COMPANY", "DEAL", "CONTACT"]`
2. From associations, get: company (name, segment), POC stage, `poc_trend`, days in current stage, number of sites
3. From deal association, get commercial context (amount, stage)
4. Query recent calls associated with the company for POC status updates
5. Extract from call: use cases being validated, any blockers, technical progress
6. Rank by: (a) POC stage advancement, (b) poc_trend (On Track > Needs Attention > At Risk), (c) deal value
7. Show top 10

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
| # | Company | Segment | POC Stage | Trend | Days | Sites | Last Outbound | Last Inbound | Validating | Engagement |
|---|---------|---------|----------|-------|------|-------|---------------|--------------|-----------|-----------|
| 1 | [name] | [seg] | [stage] | [trend] | [N] | [N] | [date] | [date] | [use cases] | [HEALTHY] |
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

AT-RISK POCs
| Company | POC Trend | Issue | Last Call Summary |
|---------|----------|-------|------------------|

THIS WEEK'S PRIORITIES
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
- Any mention of: conversion board, pipeline columns, discipline board, account progression
