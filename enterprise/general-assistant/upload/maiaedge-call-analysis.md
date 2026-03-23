---
name: call-analysis
description: "MaiaEdge call intelligence engine. Extracts use cases, segments, pain points, competitive intel, and MEDDPICC insights from HubSpot call summaries. Use when asked about what's being discussed in calls, use case frequency, segment-level call patterns, rep activity, or call-level detail. Parses AI-generated call summaries (hs_call_summary), classifies against the standardized use-case taxonomy, cross-references associated companies/deals/POCs, and produces structured call intelligence. Source of truth: HubSpot Call engagements with AI-generated summaries."
---

# MaiaEdge Call Analysis

## Purpose

Extract structured intelligence from HubSpot call summaries. This skill turns raw call data into actionable insights: what use cases are being discussed, which segments are most active, what pain points and objections come up, and what competitive intelligence surfaces in conversations.

The primary data source is `hs_call_summary` -- HubSpot's AI-generated call summaries in HTML format. These are detailed, structured summaries covering key topics, notes, and discussion points.

---

## Reference

### Reference Files

- **Call properties, query patterns, pagination, property sets:** See `call-schema.md`
- **Owner IDs and territory mapping:** See `territory-model.md`
- **Segment HubSpot values:** See `hubspot-values.md` (note: MSP/Aggregator = `Enterprise` in HubSpot)
- **Use case taxonomy:** Classify calls against the 21 canonical use cases in `use-case-taxonomy.md`. A single call typically maps to 2-5 use cases. Use the trigger keywords as a guide but consider context -- a passing mention is not a substantive discussion.

---

## Task Routing

### MODE 1: CALL EXTRACTION
**Trigger:** "Analyze this call" or "Process recent calls" or "What did we discuss with [company]?" or "Pull calls from [date range]"

**Steps:**
1. Query HubSpot calls via `search_crm_objects` (objectType: `CALL`) with appropriate filters (date range, owner, or company association). Include `associations: ["COMPANY", "DEAL", "TICKET"]` to get linked objects inline (avoids N+1 lookups). Paginate if results exceed 100 (see `call-schema.md` pagination rules).
2. Use the **content analysis** property set: `hs_call_title, hs_call_summary, hs_call_body, hs_timestamp, hubspot_owner_id, hs_call_duration, hs_call_has_transcript`
3. From inline associations, get company `customer_segment` and company name
4. From inline associations, get deal stage and/or POC ticket status for pipeline context
5. Parse `hs_call_summary` (strip HTML tags) and extract:
   - Use cases discussed (match against use-case-taxonomy.md)
   - Pain points expressed by prospect
   - Objections raised
   - Competitive mentions
   - Ah-ha moments / resonance signals
   - Next steps / action items
6. Check MEDDPICC currency (see MEDDPICC Rule below)

**Output:**
```
CALL ANALYSIS — [Company Name]
================================
Date: [date] | Rep: [name] | Duration: [X min]
Segment: [segment] | Deal Stage: [stage or "No deal"]
Has Transcript: [yes/no]

USE CASES DISCUSSED
- [Use Case 1] — [brief evidence from summary]
- [Use Case 2] — [brief evidence from summary]

KEY SIGNALS
- Pain: [what they said hurts]
- Objection: [what they pushed back on]
- Competitive: [who/what was mentioned]
- Resonance: [what lit up / ah-ha moment]

NEXT STEPS
- [action item 1]
- [action item 2]

MEDDPICC UPDATE
- Identified Pain: [current from this call]
- Key Stakeholders: [who was on call, who was mentioned]
- Competition: [current competitive landscape]
- Buying Process: [any timeline/process mentioned]
```

---

### MODE 2: USE CASE FREQUENCY ANALYSIS
**Trigger:** "What use cases are we discussing?" or "Use case breakdown" or "What topics come up most?" or "Use case frequency"

**Steps:**
1. Pull all calls in requested date range (default: last 90 days). Include `associations: ["COMPANY"]` for segment classification. Paginate through all pages (see `call-schema.md`).
2. Parse each call summary and classify against the 21 canonical use cases
3. Count frequency of each use case across all calls
4. Calculate % of calls mentioning each use case
5. Break down by segment (from associated company `customer_segment`) and by rep (`hubspot_owner_id`)
6. Compare to prior period if requested

**Output:**
```
USE CASE FREQUENCY — [Date Range]
=====================================
Based on [N] calls

| Rank | Use Case | Count | % of Calls | Top Segments | Trend |
|------|----------|-------|------------|--------------|-------|
| 1 | [use case] | [N] | [X]% | [segments] | [up/down/stable] |
| 2 | [use case] | [N] | [X]% | [segments] | [up/down/stable] |
...

BY SEGMENT
| Segment | Calls | Top Use Cases |
|---------|-------|---------------|
| Colocation | [N] | [top 3 use cases] |
...

BY REP
| Rep | Calls | Top Use Cases |
|-----|-------|---------------|
| Tim Lieto | [N] | [top 3 use cases] |
...
```

---

### MODE 3: SEGMENT CALL ANALYSIS
**Trigger:** "How are calls with [segment] going?" or "Colo call analysis" or "Neocloud conversations" or "What are fiber operators saying?"

**Steps:**
1. First, search companies where `customer_segment` = target value to get company IDs. Then query calls associated with those companies (avoids pulling all calls and filtering client-side). Include `associations: ["COMPANY", "DEAL"]`. Paginate if needed.
2. Parse each call summary for use cases, pain points, objections, and competitive mentions
3. Aggregate patterns: most common pain points, recurring objections, strongest resonance signals
4. Identify emerging themes vs. established patterns
5. Cross-reference with segment cheatsheet (e.g., `colocation.md`, `fiber-operator.md`) for context

**Output:**
```
SEGMENT CALL INTELLIGENCE — [Segment Name]
=============================================
[N] calls analyzed | [Date Range]
Companies: [list of companies discussed]

COMMON PAIN POINTS
1. [pain point] — mentioned in [N] calls ([X]%)
2. [pain point] — mentioned in [N] calls ([X]%)

TOP USE CASES
1. [use case] — [N] calls
2. [use case] — [N] calls

RECURRING OBJECTIONS
- [objection] — typical response: [how handled]

COMPETITIVE LANDSCAPE
- [competitor] mentioned in [N] calls — context: [brief]

STRONGEST RESONANCE SIGNALS
- [what lit up] — [company/context]

SEGMENT-SPECIFIC INSIGHTS
[Observations unique to this segment's calls vs. the segment cheatsheet expectations]
```

---

### MODE 4: REP ACTIVITY ANALYSIS
**Trigger:** "What's [rep] been working on?" or "Call activity by rep" or "Tim's calls this month" or "Rep scorecard"

**Steps:**
1. Pull calls filtered by `hubspot_owner_id` for the requested rep
2. Default to last 30 days if no date range specified
3. Summarize: call count, unique companies engaged, segments covered, use cases discussed
4. Identify focus patterns: which accounts get repeated calls, which segments dominate
5. Flag engagement gaps: accounts with deals but no recent outbound activity, AND accounts where we're active but the prospect has gone quiet (no inbound response in 14+ days despite outbound attempts). Query emails (objectType: EMAIL, filter `hs_email_direction` = `INCOMING_EMAIL`) and inbound calls to check prospect responsiveness.

**Output:**
```
REP ACTIVITY — [Rep Name]
============================
Period: [date range] | Total Calls: [N]

ENGAGEMENT SUMMARY
| Metric | Value |
|--------|-------|
| Unique Companies | [N] |
| Segments Covered | [list] |
| Calls with Transcripts | [N] / [total] |
| Avg Call Duration | [X] min |

TOP ACCOUNTS (by call frequency)
| Company | Calls | Segment | Deal Stage | Last Call |
|---------|-------|---------|-----------|-----------|

USE CASE FOCUS
| Use Case | Calls | % of Rep's Calls |
|----------|-------|-----------------|

ENGAGEMENT GAPS (Outbound)
[Accounts with open deals but no outbound call/email in 14+ days]

MOMENTUM RISK (Inbound Silent)
[Accounts where we're actively reaching out but prospect hasn't responded in 14+ days]
| Company | Last Outbound | Last Inbound | Outbound Count (30d) | Risk |
|---------|---------------|--------------|---------------------|------|
```

---

## MEDDPICC Rule -- Critical

See `call-schema.md` "MEDDPICC and Call Transcripts" section for the full rule. Key point: HubSpot only auto-fills MEDDPICC from the **first** call transcript. If a contact has multiple transcripts, **always extract MEDDPICC from the most recent call summary** rather than relying on stale deal-level properties.

---

## When to Use This Skill

Trigger on any of these patterns:
- "Analyze calls" or "Call analysis" or "What's in our calls?"
- "What use cases are being discussed?" or "Use case frequency" or "Topic breakdown"
- "How are [segment] calls going?" or "What are colos saying?" or "Neocloud call patterns"
- "What's [rep] working on?" or "Rep activity" or "Call scorecard"
- "What did we discuss with [company]?" or "Pull call notes for [company]"
- Any mention of: call summary, transcript, call intelligence, conversation analysis, call data
