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
- **Contact properties and persona framework:** See `contact-schema.md`
- **Owner IDs and territory mapping:** See `territory-model.md`
- **Segment HubSpot values:** See `hubspot-values.md`
- **Use case taxonomy:** Classify calls against the canonical use cases in `use-case-taxonomy.md` (21 operator-segment use cases + Enterprise-specific use cases added 2026-05-11). A single call typically maps to 2-5 use cases. Use the trigger keywords as a guide but consider context -- a passing mention is not a substantive discussion. **Enterprise calls** (where the associated company has `customer_segment = "Enterprise-CustomerSegment"`) classify primarily against the Enterprise-specific use cases section in `use-case-taxonomy.md`, with secondary mapping to operator-shared use cases (Cloud On-Ramp, Data Center Interconnection, E2E Visibility, Security/Encryption) where relevant.
- **Enterprise segment context (added 2026-05-11):** Read `context/segments/enterprise.md` and `context/segments/enterprise-use-cases.md` for Enterprise calls. Sub-segment-specific Insider Language Banks (FFIEC physical-path verification, Epic downtime procedure, peak readiness, seat ramp / paired site / client carve-out) drive accurate use-case extraction and PMF signal classification on Enterprise call transcripts.
- **Messaging baseline (for Modes 5 & 6):** `messaging-framework.md`, `segment-language.md`, `segment-messaging.md`, `competitive-positioning.md` -- these define our CURRENT messaging. Call analysis compares what prospects actually say against these files to find alignment gaps and PMF signals.

---

## Task Routing

### MODE 1: CALL EXTRACTION
**Trigger:** "Analyze this call" or "Process recent calls" or "What did we discuss with [company]?" or "Pull calls from [date range]"

**Steps:**
1. Query HubSpot calls via `search_crm_objects` (objectType: `CALL`) with appropriate filters (date range, owner, or company association). Include `associations: ["COMPANY", "DEAL", "TICKET"]` to get linked objects inline (avoids N+1 lookups). Paginate if results exceed 100 (see `call-schema.md` pagination rules).
2. Use the **content analysis** property set: `hs_call_title, hs_call_summary, hs_call_body, hs_timestamp, hubspot_owner_id, hs_call_duration, hs_call_has_transcript`
3. From inline associations, get company `customer_segment` and company name
4. From inline associations, get deal stage and/or POC ticket status for pipeline context
5. Parse ALL content fields for maximum intelligence:
   - `hs_call_summary` (strip HTML) -- primary source, structured by HubSpot AI
   - `hs_call_body` -- rep-entered notes, often contains context the AI summary missed
   - `hs_call_transcript_tracked_terms` -- keywords detected in the transcript, useful as supplemental evidence
   Extract:
   - Use cases discussed (match against use-case-taxonomy.md)
   - Pain points expressed by prospect
   - Objections raised
   - Competitive mentions
   - Ah-ha moments / resonance signals
   - Next steps / action items
6. Check MEDDPICC currency (see MEDDPICC Rule below)

**Output:**
```
CALL ANALYSIS  -  [Company Name]
================================
Date: [date] | Rep: [name] | Duration: [X min]
Segment: [segment] | Deal Stage: [stage or "No deal"]
Has Transcript: [yes/no]

USE CASES DISCUSSED
- [Use Case 1]  -  [brief evidence from summary]
- [Use Case 2]  -  [brief evidence from summary]

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

### MODE 1B: CONTACT-LEVEL CALL HISTORY
**Trigger:** "What has [person] discussed?" or "Pull calls for [contact]" or "Call history for [name]" or "What's [name] been saying on calls?"

This mode focuses on a specific CONTACT record -- all calls associated with that person across time.

**Steps:**
1. Search HubSpot contacts by name or email to get the contact ID. Pull `firstname, lastname, jobtitle, email, customer_segment, company` from the contact record.
2. Query calls associated with the contact: use `search_crm_objects` (objectType: `CALL`) with `associations: ["CONTACT", "COMPANY", "DEAL", "TICKET"]`. Filter by contact association. If the HubSpot MCP doesn't support association-based filtering, pull calls associated with the contact's COMPANY and match by contact association.
3. For each call, pull the **full content set**: `hs_call_title, hs_call_summary, hs_call_body, hs_call_has_transcript, hs_call_transcript_tracked_terms, hs_timestamp, hubspot_owner_id, hs_call_duration, hs_call_direction`
4. Parse ALL content fields:
   - `hs_call_summary` (HTML) -- primary intelligence source. Strip HTML and extract topics, key notes, action items.
   - `hs_call_body` -- rep-entered notes. Often contains context the AI summary missed.
   - `hs_call_transcript_tracked_terms` -- keywords HubSpot detected in the transcript. Use as supplemental evidence.
5. Build a chronological narrative: what has this person discussed across all calls? How have their concerns evolved? What commitments were made?
6. Extract MEDDPICC from the most recent call (not stale deal-level properties).

**Output:**
```
CONTACT CALL HISTORY  -  [Full Name], [Title] at [Company]
==========================================================
Segment: [segment] | Total Calls: [N] | Date Range: [first] to [latest]
Associated Deal: [deal name + stage] or "No deal"
Associated POC: [ticket + status] or "No POC"

CALL TIMELINE (most recent first)
---
[Date] | [Duration] min | Rep: [name] | Transcript: [yes/no]
Topics: [extracted from summary]
Key Points: [pain points, decisions, action items]
Rep Notes: [from hs_call_body if present]
Tracked Terms: [from hs_call_transcript_tracked_terms if present]

[Date] | [Duration] min | Rep: [name] | Transcript: [yes/no]
...

EVOLUTION OF CONCERNS
- [How this person's pain points, priorities, or objections have shifted across calls]

COMMITMENTS & ACTION ITEMS
- [All action items across calls, with status: completed/open/stale]

USE CASES DISCUSSED (across all calls)
- [Use Case 1]  -  [N] calls, most recent: [date]
- [Use Case 2]  -  [N] calls

COMPETITIVE MENTIONS
- [Competitor/alternative]  -  [context from which call]

MEDDPICC (from most recent call)
- Identified Pain: [current]
- Key Stakeholders: [mentioned across calls]
- Competition: [current landscape]
- Buying Process: [latest signals]

RELATIONSHIP HEALTH
- Engagement pattern: [frequency trend  -  increasing/stable/declining]
- Last inbound signal: [date] | Last outbound: [date]
- Risk: [HEALTHY / COOLING / GOING DARK]
```

---

### MODE 2: USE CASE FREQUENCY ANALYSIS
**Trigger:** "What use cases are we discussing?" or "Use case breakdown" or "What topics come up most?" or "Use case frequency"

**Steps:**
1. Pull all calls in requested date range (default: last 90 days). Include `associations: ["COMPANY"]` for segment classification. Paginate through all pages (see `call-schema.md`).
2. Parse each call summary and classify against the canonical use cases in `use-case-taxonomy.md` (21 operator-segment use cases #1-21 + 8 Enterprise-specific use cases #22-29 added 2026-05-11 with Multi-DC ICP promotion)
3. Count frequency of each use case across all calls
4. Calculate % of calls mentioning each use case
5. Break down by segment (from associated company `customer_segment`) and by rep (`hubspot_owner_id`)
6. Compare to prior period if requested

**Output:**
```
USE CASE FREQUENCY  -  [Date Range]
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
SEGMENT CALL INTELLIGENCE  -  [Segment Name]
=============================================
[N] calls analyzed | [Date Range]
Companies: [list of companies discussed]

COMMON PAIN POINTS
1. [pain point]  -  mentioned in [N] calls ([X]%)
2. [pain point]  -  mentioned in [N] calls ([X]%)

TOP USE CASES
1. [use case]  -  [N] calls
2. [use case]  -  [N] calls

RECURRING OBJECTIONS
- [objection]  -  typical response: [how handled]

COMPETITIVE LANDSCAPE
- [competitor] mentioned in [N] calls  -  context: [brief]

STRONGEST RESONANCE SIGNALS
- [what lit up]  -  [company/context]

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
REP ACTIVITY  -  [Rep Name]
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

### MODE 5: MESSAGING ALIGNMENT ANALYSIS
**Trigger:** "How does our messaging match what prospects say?" or "Messaging alignment" or "Are our value props landing?" or "What's resonating vs. not?" or "Compare calls to our messaging"

This mode compares what prospects ACTUALLY say on calls against our CURRENT messaging framework. It turns call data into a feedback loop for messaging refinement.

**Steps:**
1. Pull all calls for the requested segment (or all segments) in the date range. Default: last 90 days. Include `associations: ["COMPANY", "DEAL", "CONTACT"]`. Paginate through all pages.
2. Read the messaging baseline files. These are the "current state" you're comparing against:
   - `messaging-framework.md` -- segment value props, pillar frameworks, persona pain mapping
   - `segment-language.md` -- insider vocabulary per segment, insider vs. outsider examples
   - `segment-messaging.md` -- detailed messaging per segment with value props and fallbacks
   - `competitive-positioning.md` -- how we position against competitors
3. For each call, parse the summary and extract:
   - **Pain points the prospect named** (in their words, not ours)
   - **Language the prospect used** (exact phrasing, not our framework terms)
   - **What resonated** (ah-ha moments, "that's exactly what we need", agreement signals)
   - **What fell flat** (objections, skepticism, topic changes, "interesting but...")
   - **Competitive mentions** (who they're comparing us to, how they frame alternatives)
   - **Unaddressed needs** (things the prospect asked about that we didn't have an answer for)
4. Compare against the messaging baseline:
   - **Pain alignment:** Do the pain points prospects name match what our framework says they care about? Flag divergences.
   - **Language alignment:** Are prospects using the same vocabulary we use? Flag differences (e.g., prospects say "fabric lock-in" but we say "third-party fabric risk").
   - **Value prop traction:** Which of our value props get resonance signals vs. objections? Rank by traction.
   - **Proof point effectiveness:** Which anonymized proof points land vs. get skepticism?
   - **Pillar relevance:** Do our 3-pillar frameworks (e.g., EXTEND REACH | MONETIZE | AUTOMATE for fiber) match the actual conversation distribution?
   - **Missing angles:** What are prospects discussing that our messaging framework doesn't address?
5. Produce a segment-by-segment alignment report.

**Output:**
```
MESSAGING ALIGNMENT  -  [Segment] (or "All Segments")
======================================================
Based on [N] calls | [Date Range]
Companies: [list]

PAIN POINT ALIGNMENT
| Our Framework Says | What Prospects Actually Say | Alignment |
|--------------------|----------------------------|-----------|
| [framework pain] | [actual pain from calls] | MATCH / PARTIAL / DIVERGENT |
| [framework pain] | [not mentioned in any call] | UNVALIDATED |
| [not in framework] | [pain mentioned in N calls] | MISSING FROM FRAMEWORK |

LANGUAGE GAPS
| We Say | They Say | Frequency | Recommendation |
|--------|----------|-----------|----------------|
| "third-party fabric risk" | "fabric lock-in" | [N] calls | Consider adopting their phrasing |
| "provisioning in minutes" | "speed to revenue" | [N] calls | Our framing is feature; theirs is outcome |
| [our term] | [their term] | [N] calls | [adjustment note] |

VALUE PROP TRACTION (ranked by signal strength)
| Value Prop | Resonance Signals | Objections/Flat | Net Traction | Notes |
|------------|-------------------|-----------------|--------------|-------|
| [value prop 1] | [N] calls | [N] calls | STRONG | [what specifically resonated] |
| [value prop 2] | [N] calls | [N] calls | WEAK | [what objection or silence] |
| [value prop 3] | [N] calls | [N] calls | UNTESTED | [never came up in calls] |

PROOF POINT EFFECTIVENESS
| Proof Point | Times Used | Resonance | Skepticism | Verdict |
|-------------|-----------|-----------|------------|---------|
| "60-90 days to minutes" | [N] | [N] | [N] | STRONG / MIXED / WEAK |

PILLAR DISTRIBUTION (actual conversation time vs. framework weight)
| Pillar | Framework Weight | Call Discussion % | Delta |
|--------|-----------------|-------------------|-------|
| [Pillar 1] | Primary | [X]% of call time | [over/under-indexed] |
| [Pillar 2] | Secondary | [X]% | [over/under-indexed] |
| [Pillar 3] | Tertiary | [X]% | [over/under-indexed] |

COMPETITIVE POSITIONING CHECK
| Competitor | Framework Positioning | How Prospects Frame Them | Gap |
|------------|---------------------|--------------------------|-----|
| NaaS (Megaport etc.) | "You lose the customer" | [how prospects actually describe the threat] | [aligned / misaligned] |
| Status quo | "Cost of inaction" | [how prospects describe doing nothing] | [aligned / misaligned] |

MESSAGING ADJUSTMENT RECOMMENDATIONS
1. [Specific recommendation based on divergence data]
   Evidence: [N] calls showed [pattern]. Current framework says [X]. Calls suggest [Y].
2. [Specific recommendation]
   Evidence: ...
3. [Specific recommendation]
   Evidence: ...

UNADDRESSED NEEDS (prospects asked, we had no answer)
- [Need 1]  -  raised in [N] calls by [companies]. Not in current messaging framework.
- [Need 2]  -  raised in [N] calls. Consider adding to [segment] value props.
```

---

### MODE 6: PRODUCT-MARKET FIT SIGNALS
**Trigger:** "Product-market fit" or "PMF analysis" or "Where's our strongest fit?" or "Which segments are landing?" or "Where are we struggling?" or "PMF scorecard"

This mode aggregates call signals to assess product-market fit by segment. It answers: where is MaiaEdge resonating most, where is the messaging falling flat, and what do prospects want that we don't address?

**Steps:**
1. Pull ALL calls in the date range (default: last 90 days, or all available calls for a longer view). Include `associations: ["COMPANY", "DEAL", "CONTACT", "TICKET"]`. Paginate through all pages.
2. Read the messaging baseline: `messaging-framework.md`, `segment-language.md`, `segment-messaging.md`, `competitive-positioning.md`
3. For each call, classify:
   - **Resonance signals** -- prospect expressed strong alignment, excitement, "that's what we need", asked about next steps, pricing, timeline, POC
   - **Neutral signals** -- informational conversation, prospect was engaged but non-committal
   - **Resistance signals** -- objections, "not a priority", "we're already doing this", "too early", skepticism about the approach
   - **Unaddressed signals** -- prospect raised a need or question we didn't have a clear answer for
4. Aggregate by segment:
   - Resonance-to-resistance ratio per segment (higher = stronger PMF)
   - Top resonance drivers per segment (which value props, use cases, proof points)
   - Top resistance drivers per segment (which objections, concerns, competitors)
   - Conversion signals: calls that led to deal creation, POC, or next meeting vs. dead ends
5. Cross-segment comparison: where is MaiaEdge winning conversations vs. losing them?
6. Identify the "messaging delta" -- the gap between what our framework says and what calls reveal.

**Output:**
```
PRODUCT-MARKET FIT SCORECARD
==============================
Based on [N] calls across [N] companies | [Date Range]

PMF BY SEGMENT (ranked by fit strength)
| Segment | Calls | Resonance | Neutral | Resistance | Ratio | PMF Grade |
|---------|-------|-----------|---------|------------|-------|-----------|
| [segment] | [N] | [N] ([%]) | [N] | [N] ([%]) | [X:1] | A/B/C/D |
| [segment] | [N] | [N] ([%]) | [N] | [N] ([%]) | [X:1] | A/B/C/D |

Grading: A = 3:1+ resonance:resistance | B = 2:1 | C = 1:1 | D = more resistance than resonance

STRONGEST FIT SIGNALS (what's working)
1. [Signal]  -  [N] calls, [segments]. Evidence: "[paraphrased from call summaries]"
2. [Signal]  -  [N] calls. Evidence: "..."
3. [Signal]  -  [N] calls. Evidence: "..."

WEAKEST FIT SIGNALS (where we're struggling)
1. [Objection/resistance pattern]  -  [N] calls, [segments]. Common response: [how reps handle it]
   Recommendation: [specific messaging or positioning adjustment]
2. [Pattern]  -  [N] calls. Recommendation: ...

UNMET NEEDS (prospects want, we don't address)
| Need | Calls | Segments | Companies | In Our Framework? |
|------|-------|----------|-----------|-------------------|
| [need] | [N] | [segments] | [companies] | NO  -  consider adding |
| [need] | [N] | [segments] | [companies] | PARTIAL  -  framework mentions but doesn't emphasize |

USE CASE PMF (which use cases have the strongest traction)
| Use Case | Resonance Calls | Resistance Calls | Net | Strongest In |
|----------|----------------|-----------------|-----|--------------|
| [use case] | [N] | [N] | +[N] | [segment] |

MESSAGING DELTA  -  Framework vs. Reality
| Dimension | Current Framework | What Calls Reveal | Suggested Adjustment |
|-----------|-------------------|-------------------|---------------------|
| Primary pain ([segment]) | [framework says X] | [calls show Y] | [specific change] |
| Language ([segment]) | [we say X] | [they say Y] | [adopt their phrasing] |
| Value prop weight ([segment]) | [pillar order] | [actual interest order] | [re-prioritize] |
| Competitive framing | [framework positioning] | [how prospects see it] | [adjust angle] |

QUARTER-OVER-QUARTER TREND (if sufficient data)
| Metric | Prior Period | Current Period | Trend |
|--------|-------------|----------------|-------|
| Overall resonance rate | [X]% | [X]% | [up/down] |
| Top segment by PMF | [segment] | [segment] | [changed?] |
| Most common objection | [objection] | [objection] | [shifted?] |
| Unaddressed needs count | [N] | [N] | [growing/stable] |
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
- "What has [person] discussed?" or "Call history for [contact]" or "Pull calls for [name]"
- "How does our messaging match what prospects say?" or "Messaging alignment" or "What's resonating?"
- "Product-market fit" or "PMF analysis" or "Where's our strongest fit?" or "Which segments are landing?"
- Any mention of: call summary, transcript, call intelligence, conversation analysis, call data, contact call history, messaging alignment, PMF, product-market fit
