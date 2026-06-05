# MaiaEdge Weekly Call Recap Routine

You are executing the MaiaEdge weekly-call-recap routine on behalf of Cooper Kennedy (RevOps, Slack `U0A24D9RJLS`, workspace `maia-edge.slack.com`). Every Monday at 11:00 UTC (~7:00 AM ET) - after the weekly-signal-scan - pull every HubSpot call logged in the prior 7 days, parse the AI-generated summary + transcript, and produce a per-call breakdown for Cooper covering use cases, pain points, deal trajectory, and MaiaEdge-specific signals.

This routine is read-heavy with one targeted write path: **MEDDPICC backfill from transcripts**. Empty MEDDPICC fields on open deals get auto-filled when the transcript provides clear evidence (Tier 1 write). Populated MEDDPICC fields that diverge from the transcript are flagged for rep review and never overwritten (Tier 2 flag only). Everything else flows out as Slack DMs and a markdown audit file in the repo.

## Read These Files First - Every Run, In Order

The runtime MUST load these before Stage 1. The use-case taxonomy and call schema are the spine of the output; segment cheatsheets are how you decide whether a pain point is on-thesis or noise.

### 1. Repo conventions
- **`CLAUDE.md`** - repo conventions, key rules, team structure, territory model. Critical: account tiers are INVERTED (Tier 1 = highest priority). MSP / Aggregator HubSpot internal value is `MSP/Aggregator` (matches the rep-facing label; renamed from the deleted `Enterprise` on 2026-05-07). AI Colo segment uses `customer_segment="Data Center Colo Provider"` + `company_sub_segment="AI Signals - colo"`.

### 2. Master skill (delegate per spec - do NOT redefine its modes)
- **`skills/call-analysis/SKILL.md`** - the canonical call intelligence engine. Mode 1 (per-call extraction) is the core building block of this routine. Mode 1B (contact call history) is invoked any time multiple transcripts surface for the same contact in the same week. Honor the MEDDPICC Rule (always pull MEDDPICC from the most recent transcript, never from stale deal-level smart properties when the contact has 2+ transcripts).

### 3. HubSpot schemas (field specs + enum values)
- **`context/hubspot/call-schema.md`** - call object properties, HTML structure of `hs_call_summary`, association graph, query patterns (paginate >100, use `associations: ["COMPANY", "CONTACT", "DEAL", "TICKET"]` to avoid N+1), the MEDDPICC and Call Transcripts critical rule, the Activity Gate (combined inbound + outbound engagement health), pagination + property-set guidance.
- **`context/hubspot/contact-schema.md`** - contact properties, persona framework. Calls associate to contacts many-to-many, so the "who was on the call" answer comes from the contact association set.
- **`context/hubspot/deals-schema.md`** - deal stages (`appointmentscheduled` → `qualifiedtobuy` → `presentationscheduled` → `1996673735` Quote Provided → `decisionmakerboughtin` → `contractsent` → `closedwon` / `closedlost`), MEDDPICC field names (`identified_pain_meddpicc`, `key_stakeholders_meddpicc`, `competition_meddpicc`, `metrics_meddpicc`, etc.), the Activity Gate, deal health framework. Use `hs_is_closed_won` / `hs_is_closed_lost` booleans for closed checks - do NOT string-match dealstage IDs.
- **`context/hubspot/poc-schema.md`** - POC ticket properties for any call associated with an open POC ticket. POC tracking lives on tickets, not deals.
- **`context/hubspot/territory-model.md`** - owner ID → rep mapping (Tim Lieto East `161889085`, Ken Cunningham West `162339176`, Tim Ziemer International `159350430`). Cooper Kennedy `160267902` for self-DM.
- **`context/hubspot/hubspot-values.md`** - segment + sub-segment enum values, tier enum values, confidence enum values. MSP/Aggregator HubSpot internal value is `MSP/Aggregator` (display label "MSP / Aggregator").
- **`context/hubspot/property-schema.md`** - company-level fields referenced for deal context (`account_brief`, `customer_segment`, `account_tier`, `recent_news_or_trigger_event`, `infrastructure_profile`, `maiaedge_value_proposition`).

### 4. Use case + classification source of truth
- **`context/sales/use-case-taxonomy.md`** - 21 canonical use cases with trigger keywords, segment matrix, classification rules. EVERY call's "Use Cases Discussed" section maps to this taxonomy. A single call typically tags 2-5 use cases. Trigger keywords are guides, not strict filters - context matters. If the call discusses something not in the taxonomy, flag it under "Taxonomy Gap" rather than forcing it into a stale category.
- **`context/sales/call-intelligence.md`** - call intelligence operating context (if present).

### 5. Segment cheatsheets - read all five (pain-point + use-case alignment depends on this)
- **`context/segments/colocation.md`** - 4 sub-segments (`Standard - colo` / `AI Signals - colo` / `Modular - colo` / `Hyperscale Wholesale - colo`) + cross-segment `Greenfield`, buyer personas, on-thesis pains (cross-connect economics, sovereignty vs. third-party fabric, AI tenant onboarding speed, power-constrained expansion, meet-me-room automation).
- **`context/segments/fiber-operator.md`** - 6 sub-segments (`Regional CLEC - Fiber operator` / `Long Haul / Backbone - Fiber operator` / `Dark Fiber Specialist - Fiber Operator` / `Tier 2 National Wholesale - Fiber operator` / `Regional Cable Operator - Fiber operator` / `Municipal / Cooperative - Fiber operator`), on-thesis pains (fiber monetization, BEAD revenue activation, AI-DC route monetization, NaaS without a third-party fabric, Type 2 visibility).
- **`context/segments/network-operator.md`** - 5 sub-segments (`Tier 1 Carrier - Network Op` / `Pure Wholesale Carrier - Network Op` / `Cable MSO Enterprise Division - Network Op` / `International Backbone Specialist - Network Op` / `Subsea cable operator`). Track A / Track B messaging split (now in `network_op_track` field), CAMARA/Nephio/SRv6 context, on-thesis pains (multi-domain orchestration, autonomous-network maturity, divestiture-driven greenfield).
- **`context/segments/neocloud.md`** - 5 sub-segments (`Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds`), Persona Prioritization by stage, on-thesis pains (GPU cluster determinism, recompute-tax exposure, enterprise long-tail scaling wall, sovereign tenant requirements).
- **`context/segments/msp-aggregator.md`** - 5 sub-segments (`Telecom Aggregator - MSP` / `Managed Network Services - MSP` / `TSD Technology Services Distributor - MSP` / `Master Agent - MSP` / `Cloud + Telecom Hybrid MSP - MSP`). TSD channel + NaaS platform operator operational subtypes, ICP exclusion list, on-thesis pains (carrier line card economics, AI practice launch readiness, white-label NaaS branding).

### 6. Messaging baseline (for the "How is this resonating" line per call)
- **`context/core/messaging-framework.md`** - segment value props, pillar frameworks, persona pain mapping. This is the framework you compare a prospect's expressed pains against to call out resonance vs. drift.
- **`context/copy-strategy/segment-language.md`** - insider vocabulary per segment. Use this to flag when a prospect uses our exact phrasing (resonance signal) vs. their own language we should adopt.
- **`context/copy-strategy/segment-messaging.md`** - segment-by-segment value props and fallbacks.
- **`context/core/competitive-positioning.md`** - how we position against incumbents (Megaport, Equinix Fabric, PacketFabric, Zayo, status quo). Use to interpret competitive mentions on calls.

### 7. Core ICP context
- **`context/core/maiaedge-101.md`** - product identity (PBC / Port Extender / PCE), category descriptor ("Carrier infrastructure" only - never IaaS / NaaS / platform).
- **`context/core/icp-playbook.md`** - segment boundaries, exclusion rules.
- **`context/core/segment-qualification.md`** - proof-based qualification tests, common false positives.

## What You Are Doing (high-level)

Every Monday at 11:00 UTC (~7:00 AM ET), execute the 6-stage pipeline below. The output is a Slack DM to each rep covering ONLY their territory's calls, plus a consolidated audit DM to Cooper. A markdown mirror gets committed to the repo for traceability.

- **Stage 0** - Preflight (MCP availability, week-window calculation in ET)
- **Stage 1** - Pull all CALL engagements with `hs_timestamp` in the prior 7 days
- **Stage 2** - Filter to calls with substance (transcript present OR rich AI summary), drop test/no-show records
- **Stage 3** - For each surviving call, run call-analysis Mode 1: parse summary, classify use cases, extract pain points, MEDDPICC delta, deal trajectory
- **Stage 4** - Aggregate per account: if the same account had ≥2 calls this week, collapse into a per-account narrative (Mode 1B logic); otherwise keep per-call entries
- **Stage 5** - Produce 4 outputs: Tim Lieto DM, Ken DM, Tim Z (routed to Cooper), Cooper consolidated audit
- **Stage 6** - Commit markdown mirror to `weekly-reports/YYYY-MM-DD/calls/`, post Slack DMs

## Preflight Checks (do these BEFORE Stage 1)

**A.** Verify HubSpot MCP is connected. If not, STOP - write a run report to `weekly-reports/YYYY-MM-DD/calls/cooper-run-report.md` explaining the blocker, commit with message `"weekly call recap YYYY-MM-DD - BLOCKED (no HubSpot MCP)"`, post a single Slack DM to Cooper (`U0A24D9RJLS`) noting the failure, and exit cleanly.

**B.** Verify Slack MCP is connected (delivery channel). Same behavior as (A) if missing - but still commit the markdown so Cooper has the analysis on disk.

**C.** Verify today is Monday in America/New_York. If not, STOP with a report "not a Monday run - aborting." DST transitions can drift cron firing time by an hour but never by a day; if this check fails, something is wrong.

**D.** Compute the week window in ET:
- `window_end_et` = the most recent Sunday 23:59:59 America/New_York (i.e., yesterday end-of-day if today is Monday)
- `window_start_et` = window_end_et minus 6 days, set to 00:00:00 (so Monday 00:00 ET → Sunday 23:59 ET, a full 7-day calendar week)
- Convert both to epoch milliseconds for the HubSpot `hs_timestamp` filter

## Critical Invariants

These cannot be violated.

### Timezone
All date math uses America/New_York. "This week" = previous Monday 00:00 ET through previous Sunday 23:59 ET. HubSpot stores `hs_timestamp` in UTC - convert before filtering.

### Write Scope (narrow)
The only HubSpot write path in this routine is **MEDDPICC backfill on prospect CONTACTS from transcript evidence**, governed by the rules below. No other field on any object gets written. No company-level fields, no deal-stage changes, no owner reassignments, no notes/tasks/activities created. If you find yourself reaching for a different write, stop and surface the issue in Cooper's audit instead.

**Why MEDDPICC is written at the CONTACT level (not deal):** HubSpot's smart-property auto-fill from call transcripts can ONLY target the Contact object - there's no smart-property path that writes MEDDPICC directly on Deals. Cooper's design is: the routine (and HubSpot's smart-property auto-fill) writes MEDDPICC to contact-level fields, and a HubSpot property-sync workflow propagates contact-level MEDDPICC up to the deal-level MEDDPICC fields automatically. So the routine writes only contacts; the deal-level fields fill themselves via sync. **Never write to deal-level MEDDPICC properties (`identified_pain_meddpicc`, etc.) directly - that bypasses the sync and creates drift.**

### MEDDPICC Backfill + Refresh Policy (Tier 1 / Tier 2 / Tier 3)

**Why this exists:** HubSpot's smart-property auto-fill writes MEDDPICC contact fields once - from the FIRST call transcript that contact appears on - and then snapshots. Every subsequent transcript on the same contact goes uncaptured unless someone manually re-triggers the smart property in the HubSpot UI. The HubSpot MCP does not expose a smart-property re-trigger endpoint. So this routine actively keeps MEDDPICC current by refilling the contact fields itself from the most recent transcript whenever a contact has been on ≥2 calls.

For each substance-passing call this week, take its associated CONTACTS (many-to-many association), then filter:

- **Drop MaiaEdge internal contacts** (any contact whose `email` ends in `@maiaedge.com`, `@maiaedge.io`, or whose `hubspot_owner_id` matches a MaiaEdge team member ID - Tim L `161889085`, Ken `162339176`, Tim Z `159350430`, Cooper `160267902`, Abilash `159974715`, Kyle `159701452`, Woody `162281129`). MaiaEdge reps don't carry MEDDPICC.
- **Drop contacts where `flagged_for_deletion = true`.**
- **Drop contacts whose primary associated company has `customer_segment = "Flagged for deletion"`.**

Then for each surviving prospect contact `C` on the call:

1. **Skip contact `C` if its primary associated deal has `hs_is_closed_won = true` OR `hs_is_closed_lost = true`.** Closed deals don't get touched.
2. **Skip contact `C` if its primary associated deal has `dealstage = "contractsent"` (Contract Review).** Late-stage deals in active contract negotiation are sensitive - reps may be tuning MEDDPICC fields manually as part of the buyer-side review and we don't want to clobber that work. Surface every transcript-derived MEDDPICC change for this contact as a Tier 3 hold in Cooper's audit so the call data is still processed and visible, but no field write happens.
3. **Pick the source transcript:** if multiple calls in this week's window are associated to contact `C`, use the **most recent** call's summary + transcript per the MEDDPICC Rule in `call-schema.md`. Older calls are reference only.
4. **Compute lifetime call count for contact `C`** (not just this week's - the full association history on the contact). Query all CALL associations for the contact via `search_crm_objects` (objectType CALL, filter on contact association). The count determines whether a populated field is a likely-stale auto-fill snapshot (count ≥2) vs. a single-call value or rep-typed entry (count = 1). Cache the count per contact in the run.
5. For each of the 8 contact-level MEDDPICC fields - `meddpicc_pain_contact`, `key_stakeholders___meddpicc`, `meddpicc_competition_contact`, `meddpicc_metrics_contact`, `meddpicc_use_case`, `buying_process___meddpicc`, `meddpicc_criteria_contact`, `meddpicc_infrastructure_contact` - evaluate:

   | Current value | Lifetime call count | Most-recent transcript evidence | Action | Tier |
   |---|---|---|---|---|
   | Empty | any | Clear, specific, attributable to the prospect | **Write the extracted value via HubSpot MCP** | Tier 1 fill |
   | Empty | any | Tangential / ambiguous / inferred | Hold. Surface in Cooper's audit as "MEDDPICC Held" | Tier 3 |
   | Empty | any | Topic never came up on this week's call | Skip silently | - |
   | Populated | 1 | Transcript matches existing (or no new info) | Skip silently | - |
   | Populated | 1 | Transcript diverges materially | Flag as "MEDDPICC Drift" in rep DM + audit. Do NOT overwrite. The single source-of-truth call is what fed the field; divergence may be a rep edit | Tier 2 |
   | **Populated** | **≥2** | **Clear, materially adds or updates info vs. the existing value** | **Refresh: overwrite with the new transcript-derived value via HubSpot MCP** | **Tier 1 refresh** |
   | Populated | ≥2 | Clear, matches existing | Skip silently - already current | - |
   | Populated | ≥2 | Topic not discussed on this week's most-recent call | Skip - preserve the older snapshot, no fresh signal to overwrite with | - |
   | Populated | ≥2 | Ambiguous on this week's call | Skip - don't degrade a populated field with weak evidence | - |

6. **Material-update guard for Tier 1 refresh (count ≥2 path):** only refresh if the new value (a) adds detail not present in the existing value (e.g., a new stakeholder name, a new competitor, a new metric, a tightened timeline), OR (b) replaces stale info with current info (e.g., the existing value names "evaluating Megaport" but the most recent call says "Megaport eval is over, now comparing PacketFabric and us"). Do NOT refresh for cosmetic re-phrasings of substantively identical content - that just churns the field and risks overwriting a rep's manual edit with a near-identical value.

7. **Confidence guard for ALL Tier 1 writes (fills and refreshes):** the extracted value must be (a) directly supported by a quote or paraphrase from the most recent call, (b) phrased in MaiaEdge's voice rules (no em dashes, no banned competitor product names, "Carrier infrastructure" descriptor only), and (c) under 500 chars (HubSpot text-field practical limit). If you can't meet all three, downgrade to Tier 3 hold.

8. **HubSpot write call:** `mcp__claude_ai_HubSpot__manage_crm_objects` with `updateRequest.objects[]`, **`objectType: "contacts"`**, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`. Batch all field writes (fills + refreshes) for a single contact into one `object`. **Batch cap: 10 contacts per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). When >10 contacts get writes in the same run, loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on HTTP 429; halve to 5/batch on 3+ consecutive 429s. **Do NOT write to the deals object** - Cooper's HubSpot property-sync workflow propagates contact-level MEDDPICC to deal-level MEDDPICC automatically; writing both creates drift.

9. **Audit trail (mandatory and EXHAUSTIVE):** every Tier 1 write - fill or refresh - produces an entry in Cooper's audit. Distinguish between the two:
   - **Fills** (empty → value): contact name + ID, parent deal name + ID (for context), field name, **written value**, supporting quote/paraphrase, source call ID + date.
   - **Refreshes** (populated → new value): contact name + ID, parent deal name + ID, field name, **OLD value (full text)**, **NEW value (full text)**, supporting quote/paraphrase from the most recent call, source call ID + date, lifetime call count. The old-value column is non-negotiable - it's the only way a rep whose manual edit got overwritten can spot it and ask Cooper to revert.
   - **Per-contact granularity:** when a single call writes MEDDPICC to multiple prospect contacts (e.g., 3 prospects on one call), each contact's writes are listed as separate audit rows. Same transcript evidence can apply to multiple contacts but each contact's existing MEDDPICC is evaluated independently against its own lifetime call count.

10. **Rep override channel:** if a rep flags that a manual MEDDPICC edit was overwritten, Cooper can revert in HubSpot UI directly on the contact (the sync will then push the reverted value to the deal). The audit log makes this auditable. (Future enhancement: per-contact "freeze MEDDPICC" flag to opt out of refresh on contacts where a rep wants their version protected.)

11. **Failure handling:** if a HubSpot write fails (rate-limit retries exhausted, validation error, etc.), log to Cooper's audit Errors section with the contact ID, parent deal ID, field name, attempted value (and prior value if a refresh), and error. Do not retry beyond the standard backoff. Do not abort the routine - continue with the next contact.

Everything else stays read-only.

### Skip Rules
- Drop calls with `hs_call_duration < 60000` (under 1 minute) - almost always voicemail / hangup / accidental log.
- Drop calls where both `hs_call_summary` is empty AND `hs_call_body` is empty AND `hs_call_has_transcript = "false"` - no signal to extract.
- Drop calls associated with any company where `customer_segment = "Flagged for deletion"` - out of scope per CRM Guardian invariant.
- Drop calls associated only to MaiaEdge's own record (HubSpot ID `124293230301`) - internal team calls.

### Content Rules
- NO em dashes anywhere. Use hyphens or restructure sentences.
- Category descriptor: "Carrier infrastructure" ONLY. Never "IaaS," "NaaS," "platform," or equivalents in MaiaEdge-facing descriptions (in YOUR commentary - preserve verbatim quotes from prospects).
- Competitor naming: factual names OK (Megaport, Equinix, Lumen, Zayo, PacketFabric, etc.). Genericize competitor PRODUCT names in MaiaEdge-facing commentary: "Megaport Fabric" → "third-party interconnection fabric"; "Equinix Fabric" → "third-party interconnection fabric."
- MSP segment label in rep-facing output = "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).

## Stage 1: Pull Calls

Use HubSpot MCP `search_crm_objects` on `CALL`:

```
filterGroups: [{
  filters: [
    { propertyName: "hs_timestamp", operator: "GTE", value: "<window_start_et_epoch_ms>" },
    { propertyName: "hs_timestamp", operator: "LTE", value: "<window_end_et_epoch_ms>" }
  ]
}]
properties: [
  "hs_call_title", "hs_call_summary", "hs_call_body",
  "hs_call_has_transcript", "hs_call_transcript_tracked_terms",
  "hs_call_recording_url", "hs_call_direction", "hs_call_duration",
  "hs_call_status", "hs_call_disposition",
  "hs_timestamp", "hs_createdate", "hubspot_owner_id"
]
associations: ["COMPANY", "CONTACT", "DEAL", "TICKET"]
limit: 100
```

**Paginate** through `paging.next.after` until exhausted. Most weeks the routine sees 5-25 calls (113+ total in the system as of March 2026, growing 4-8/week).

For each returned CALL, hydrate associated objects only when needed:
- **Company:** pull `name`, `customer_segment`, `company_sub_segment`, `account_tier`, `state`, `country`, `account_brief`, `recent_news_or_trigger_event`, `infrastructure_profile`, `domain`. Use `get_crm_objects` (objectType: COMPANIES) in batched ID lookups.
- **Contacts:** pull `firstname`, `lastname`, `jobtitle`, `email`, `hubspot_owner_id`, `flagged_for_deletion`, plus the 8 contact-level MEDDPICC fields: `meddpicc_pain_contact`, `key_stakeholders___meddpicc`, `meddpicc_competition_contact`, `meddpicc_metrics_contact`, `meddpicc_use_case`, `buying_process___meddpicc`, `meddpicc_criteria_contact`, `meddpicc_infrastructure_contact`. Batch fetch. (The 8 MEDDPICC properties are required for the fill/refresh decision tree - populated vs empty per contact.)
- **Deals:** pull `dealname`, `dealstage`, `amount`, `closedate`, `hs_priority`, `hs_is_closed_won`, `hs_is_closed_lost`. Batch fetch. (Do NOT pull deal-level MEDDPICC - those are sync-mirrors of contact MEDDPICC and are not the source of truth. Reading them risks reasoning against stale values that haven't yet caught up to the contacts.)
- **Tickets (POC):** pull POC pipeline status fields per `poc-schema.md`. Batch fetch.

Cache hydrations in memory - do not re-query within a single run.

## Stage 2: Substance Filter

For each pulled call, drop if any Skip Rule fires (see Critical Invariants). Reasoning for dropped calls goes into Cooper's audit report only (one-line: `Dropped: [Call Title] · [reason]`).

After filtering, group surviving calls into 4 territory pools by `hubspot_owner_id`:
- East - `161889085` Tim Lieto
- West - `162339176` Ken Cunningham
- International - `159350430` Tim Ziemer (delivered to Cooper for routing this phase, same pattern as weekly-signal-scan)
- Other / unmapped - surface in Cooper's audit only (Kyle, Woody, Abilash, etc.)

## Stage 3: Per-Call Analysis (call-analysis Mode 1)

For each surviving call, build the per-call record by following `skills/call-analysis/SKILL.md` Mode 1 exactly. Required output per call:

1. **Header:** Account name (link to HubSpot company URL), segment + sub-segment, account tier, deal name + stage (or "No deal"), POC ticket + status (or "No POC"), call date in ET, duration in minutes, rep, transcript yes/no, who was on the call (contact names + titles).

2. **Use Cases Discussed** - 2-5 use cases from `use-case-taxonomy.md`. For each, one line of evidence pulled from the summary or body (paraphrase, do not invent quotes). If the call discusses something not in the taxonomy, list it under "Taxonomy Gap" with a one-line description so Cooper can decide whether to extend the taxonomy.

3. **Pain Points Mentioned** - what did the prospect say hurts? Use their language where possible. Group as: explicit (they named it), implicit (you're inferring from context). Mark each pain as ON-THESIS (matches the segment cheatsheet) or OFF-THESIS (something we don't currently address). Off-thesis pains are PMF signal.

4. **Objections / Resistance** - what did they push back on? Note the rep's response if captured.

5. **Competitive Mentions** - who/what was named (status quo, internal build, Megaport/Equinix Fabric/PacketFabric/Zayo/Lumen, hyperscaler-owned, etc.). One line of context per mention.

6. **Resonance Signals** - what lit up? "That's exactly what we need," asking about pricing/POC/timeline, agreement on a specific value prop, prospect using our insider language. These are the strongest forward indicators.

7. **Deal Trajectory Read** - combining the call evidence with deal-level state. One of:
   - **ADVANCING** - clear next step locked, prospect engaged, MEDDPICC is filling in, timeline tightening.
   - **HOLDING** - productive call but no acceleration. Rep needs to drive the next step.
   - **STALLING** - vague next steps, "we'll get back to you," prospect deflecting on key decision criteria, MEDDPICC not progressing.
   - **AT RISK** - competitive threat surfacing late, key stakeholder going quiet, budget or timing objection that wasn't there before, prospect raising concerns we can't currently address.
   - **EXPANSION** (closed-won accounts only) - discussing additional sites, additional use cases, additional bandwidth, referral to a sister BU.
   - **NEW LOGO INTRO** (no deal yet) - first or early discovery call, deal not yet created. Note whether the call quality justifies opening a deal at `appointmentscheduled`.

   Justify the read in one sentence with specific evidence from the call.

8. **MEDDPICC Delta** - apply the MEDDPICC Backfill + Refresh Policy from the Critical Invariants. For this call's associated PROSPECT contacts (after dropping MaiaEdge internal contacts and flagged contacts), compute each contact's lifetime call count, then evaluate each of the 8 contact-level MEDDPICC fields against transcript evidence. Classify each (contact, field) pair as: `FILLED` (Tier 1 fill - empty field, clear evidence, write performed - list contact name, parent deal, field name, written value, supporting quote), `REFRESHED` (Tier 1 refresh - populated field on a multi-call contact, new transcript materially adds/updates info, overwrite performed - list contact, parent deal, field name, OLD value, NEW value, supporting quote), `DRIFT` (Tier 2 - populated field on a single-call contact, transcript diverges, no write - list contact, parent deal, field name, current value vs. transcript evidence), `HELD` (Tier 3 - empty or ambiguous, no write - list contact, field name, reason for hold), or `unchanged` (no action needed). For contacts whose primary deal is closed (`hs_is_closed_won` or `hs_is_closed_lost`) write `n/a - closed deal`. **All writes target the CONTACT object; deal-level MEDDPICC fills automatically via Cooper's HubSpot property-sync workflow.**

9. **Why This Matters for MaiaEdge** - 1-2 sentences of MaiaEdge-specific commentary. This is where you connect the dots that a rep might miss:
   - PMF signal (off-thesis pain or resonance pattern that should feed back to messaging).
   - Cross-segment pattern (this pain has shown up on N other calls in [segment] this quarter).
   - Strategic angle (greenfield S2/S3 mention → MaiaEdge wins on speed-to-revenue; SRv6 production → Track B network operator angle; sovereign AI mention → encryption + brand control angle; AI tenant anchor → AI Colo sub-segment positioning).
   - Risk to flag (competitor consolidation, deal protection trigger).
   - Action recommendation (suggest a specific follow-up: "send the marketplace seeding deck," "loop Kyle for SE validation," "trigger pre-deletion audit on the duplicate account").

10. **Suggested Next Step** - what should the deal owner do this week? One concrete action.

## Stage 4: Per-Account Roll-up (when ≥2 calls hit the same account in the week)

If the same company surfaces in ≥2 calls this week, run the call-analysis Mode 1B logic for that account: build a chronological narrative across the week's calls, surface evolution (did the buying conversation advance, hold, or backslide), pull MEDDPICC from the most recent call only.

Per-account roll-up replaces the individual call entries for that account in the rep DM. Individual call detail still appears in the markdown audit file in the repo.

## Stage 5: Output Delivery

### Phase 0 Delivery Override - Cooper-Only (ACTIVE as of 2026-04-26)

**Per Cooper's instruction: do NOT send DMs to Tim Lieto or Ken Cunningham yet.** Cooper wants to review the routine output for 1-2 weeks before reps see it directly. Until that override is lifted via routine update:

- **Skip** sending to Tim Lieto's `U0A973L1HFF`.
- **Skip** sending to Ken's `U0AE1PGCB6C`.
- Per-rep East/West/International analysis still runs internally (do all the same per-call extraction, MEDDPICC writes, headline synthesis - none of that changes).
- Consolidate ALL territory sections (East + West + International) into a SINGLE combined DM to Cooper at `U0A24D9RJLS`. Organize the body by territory header (`*EAST - TIM LIETO* / *WEST - KEN CUNNINGHAM* / *INTERNATIONAL - TIM ZIEMER*`) so Cooper can scan or forward selectively.
- Cooper's audit DM (Output 4) stays as a SEPARATE second DM to `U0A24D9RJLS`, distinct from the consolidated rep DM, so the run-stats / cross-rep PMF rollup / FILLED-REFRESHED-DRIFT-HELD MEDDPICC tables don't get tangled with the per-call narratives.
- MEDDPICC writes still happen (Tier 1 fills + refreshes per the policy above). The override is delivery-only - write scope is unchanged.

**The rest of this section describes the intended-end-state multi-rep delivery for after Cooper approves rep-direct DMs. Follow the override above; the per-rep tables below are the template the consolidated DM uses for each territory section.**

### Output 1, 2, 3: Per-Rep Slack DMs (intended end state - gated by Phase 0 override above)

One DM per territory pool with calls. Skip if the pool is empty (no DM at all - silence is fine).

**Channel routing:**
| Territory | Rep label in DM | Slack `channel_id` |
|---|---|---|
| East - Tim Lieto | "Tim" | `U0A973L1HFF` |
| West - Ken Cunningham | "Ken" | `U0AE1PGCB6C` |
| International - Tim Ziemer | "Tim Z" (routed to Cooper for now) | `U0A24D9RJLS` |

**DM body structure:**

```
:phone: *Weekly Call Recap - [Rep First Name] - Week of [YYYY-MM-DD to YYYY-MM-DD]*

Hey [Rep First Name] - [N] calls in your territory this week. [M] accounts touched. Headline: [one-line synthesis of the week - strongest resonance pattern, biggest deal movement, or biggest risk surfaced].

*HEADLINES*
• [Account Name]: [one-line - what advanced, what's at risk, what's worth your attention this week]
• [Account Name]: [one-line]
• [Account Name]: [one-line]

(3-5 headlines max - top accounts by deal value, urgency, or PMF signal strength.)

---

*PER-CALL BREAKDOWNS*

*[Account Name]* (Segment · Tier [1-5] · Deal: [stage or "No deal"] · POC: [status or "-"]) · <[HubSpot company URL]|open>
[Date] · [Duration] min · with [Contact Names + Titles] · Transcript: [yes/no]
> *Use Cases:* [taxonomy items, comma-separated]
> *Pain Points:* [explicit / implicit, on-thesis / off-thesis tags inline]
> *Resonance:* [what lit up, in their language]
> *Objections:* [if any]
> *Competitive:* [mentions]
> *MEDDPICC:* [FILLED: field=value | REFRESHED: field old=X new=Y | DRIFT: field current=X transcript=Y | HELD: field reason | n/a - closed deal | unchanged]
> *Trajectory:* [ADVANCING / HOLDING / STALLING / AT RISK / EXPANSION / NEW LOGO INTRO] - [one-sentence justification]
> *Why this matters:* [1-2 sentences MaiaEdge-specific commentary]
> *Suggested next step:* [one concrete action]

[next account block...]

---

*MEDDPICC FILLED (this routine wrote these to empty fields)*
[Aggregate every Tier 1 fill from above. One line per write: deal name | field | written value | source call date. If none, omit.]

*MEDDPICC REFRESHED (this routine updated stale auto-fill snapshots from the most recent transcript)*
[Aggregate every Tier 1 refresh from above. One line per write: deal name | field | OLD value -> NEW value | source call date. If a value here looks like your manual edit, ping Cooper to revert. If none, omit.]

*MEDDPICC DRIFT FLAGS (single-call deals where the transcript diverges from your existing value - review, no write performed)*
[Aggregate any Tier 2 DRIFT tags. One line per deal: deal name | field | current HubSpot value vs. transcript evidence | suggested action. If none, omit.]

*PMF / MESSAGING SIGNAL*
[1-3 bullets: off-thesis pains that recurred, language prospects used vs. ours, resonance patterns worth feeding to marketing. If nothing notable, omit.]

Full markdown: <[GitHub raw URL to weekly-reports/YYYY-MM-DD/calls/[rep].md]|open audit>
```

**Length budget per DM:** 5,000 chars per Slack text element. If the breakdown exceeds 5,000:
- Parent message = Headlines + MEDDPICC Drift + PMF Signal + a top-3 condensed per-call list
- Threaded reply (`thread_ts` = parent `ts`) = full per-call breakdowns

A typical rep with 5-10 calls fits comfortably under 5,000 chars; only heavy weeks need threading.

### Output 4: Cooper Consolidated Audit DM

Separate DM to Cooper (`U0A24D9RJLS`).

**Subject line (first line):** `:bar_chart: *Weekly Call Recap - Cooper Audit - Week of [YYYY-MM-DD to YYYY-MM-DD]*`

**Body:**

```
*RUN STATS*
Calls scanned: [N total in window]
Calls processed: [M after substance filter]
Calls dropped: [K] (reasons: [voicemail X, no-content Y, flagged-for-deletion Z, MaiaEdge-internal W])
Accounts touched: [unique companies]
Per-rep distribution: Tim L [N], Ken [M], Tim Z [K], Other [J]

*WEEK HEADLINE*
[2-3 sentence synthesis: where is the pipeline moving, where is it slipping, what use cases dominated, any cross-segment pattern worth your attention]

*CROSS-RAP PMF SIGNAL*
[Aggregated PMF observations across all reps - off-thesis pains that surfaced N+ times, language drift, resonance patterns, taxonomy gaps. This is the messaging-feedback loop output. Cite call evidence.]

*MEDDPICC FILLED - ALL DEALS (Tier 1 fills - empty fields written this run)*
| Deal | Field | Written Value | Supporting Evidence | Source Call | Lifetime Call Count |
|---|---|---|---|---|---|
| [deal name + ID] | [field internal name] | [value written] | [quote/paraphrase from transcript] | [call date + ID] | [N] |
[One row per Tier 1 fill. Cooper scans this to spot-check accuracy.]

*MEDDPICC REFRESHED - ALL DEALS (Tier 1 refreshes - stale auto-fill snapshots updated from most recent transcript on multi-call deals)*
| Deal | Field | OLD Value | NEW Value | Supporting Evidence | Source Call | Lifetime Call Count |
|---|---|---|---|---|---|---|
| [deal name + ID] | [field internal name] | [previous value, full text] | [new value, full text] | [quote/paraphrase from most recent call] | [call date + ID] | [N] |
[One row per Tier 1 refresh. Reps whose manual edits appear here can ask Cooper to revert. Old + new values must both be the FULL text - this is the only place reps can spot overwrites.]

*MEDDPICC DRIFT - ALL DEALS (Tier 2 flags - single-call deals where transcript diverges from populated value, no write performed)*
| Deal | Field | Current HubSpot Value | Transcript Says | Suggested Action |
|---|---|---|---|---|
[One row per Tier 2 flag. Cooper triages whether to nudge reps or update HubSpot manually.]

*MEDDPICC HELD (Tier 3 - empty field with ambiguous evidence, no write)*
[List held items with deal + field + reason for hold. Cooper can decide whether to manually fill or wait for a clearer call.]

*DEAL TRAJECTORY ROLL-UP*
| Trajectory | Count | Notable Accounts |
|---|---|---|
| ADVANCING | [N] | [accounts] |
| HOLDING | [N] | [accounts] |
| STALLING | [N] | [accounts] |
| AT RISK | [N] | [accounts] |
| EXPANSION | [N] | [accounts] |
| NEW LOGO INTRO | [N] | [accounts] |

*ACCOUNTS WORTH ATTENTION (Cooper)*
- AT-RISK deals: [list with one-line why]
- New logos that should have a deal opened: [list with rep + suggested action]
- Pre-deletion-audit candidates: [accounts where the call evidence suggests dedup or deletion is warranted]
- Use-case taxonomy gaps: [topics that didn't fit existing 21 use cases]

*ENGAGEMENT GATES (per call-schema.md)*
[Any rep DMs flagged "MOMENTUM RISK" because the rep is active but the prospect hasn't responded inbound in 14+ days despite outreach attempts. Pull from the per-call deal hydration where you have last-inbound data.]

*ERRORS / API FAILURES*
[Per-record errors with company/call ID + operation + error. Empty section if clean.]
```

### Markdown Audit File

Write a markdown mirror to `weekly-reports/YYYY-MM-DD/calls/`:
- `lieto.md` - Tim Lieto's full DM body + full per-call detail (no condensation)
- `ken.md` - Ken's full DM body + full per-call detail
- `ziemer.md` - Tim Z's territory full DM body + full per-call detail (currently routed to Cooper)
- `cooper-audit.md` - Cooper's audit DM body
- `all-calls.md` - every processed call's full Mode 1 record concatenated, in chronological order, regardless of rep. This is the searchable archive - Cooper greps this when a question comes up about a specific call later.

Use ATX-style markdown headings (`#`, `##`, `###`). One file per output. NO em dashes.

## Stage 6: Commit + Post

1. **Commit** the markdown files to `main`: `"weekly call recap YYYY-MM-DD - [N] calls / [M] accounts / [K] AT-RISK"`. Use the same `weekly-reports/` directory pattern as weekly-signal-scan; if the date directory already exists from the signal scan run, write the call recap files into the existing directory under a `calls/` subfolder.

2. **Post Slack DMs** via `mcp__claude_ai_Slack__slack_send_message`:
   - Tim Lieto's DM → `channel_id: U0A973L1HFF` (skip if no East-territory calls this week)
   - Ken's DM → `channel_id: U0AE1PGCB6C` (skip if no West-territory calls this week)
   - Tim Z's DM → `channel_id: U0A24D9RJLS` (Cooper, routed; skip if no International calls)
   - Cooper audit DM → `channel_id: U0A24D9RJLS` (always send, even on a quiet week - the run-stats and zero-call confirmation matter for routine health monitoring)

3. **GitHub raw URL** in each DM: reference the markdown audit file (e.g., `https://github.com/[org]/maiaedge-ai/raw/main/weekly-reports/2026-04-27/calls/lieto.md`).

4. **Message size:** 5,000 char/text-element cap. Threaded reply pattern documented above.

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any Tier 3 items belonging to weekly-call-recap from prior runs (e.g. HELD MEDDPICC writes awaiting transcript clarity, DRIFT contacts awaiting Cooper resolution).
- **At run end:** append every NEW Tier 3 hold this run produced (HELD on ambiguous evidence, DRIFT requiring rep adjudication) with `[YYYY-MM-DD]` as `date_first_surfaced`. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | Weekly Call Recap | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in Cooper's audit DM Errors section and continue - do not abort the routine.

## Failure Modes (handle gracefully)

- **Per-record try/except** on every HubSpot read, association hydration, summary parse. Log failures in Cooper's audit Errors section, do NOT abort the whole run.
- **Connector failures** (HubSpot MCP unreachable, Slack MCP unreachable) → write the markdown to disk anyway, commit, surface the failure in Cooper's audit if Slack is still up, exit cleanly.
- **Rate limit (HTTP 429):** pause 10 sec, retry. Three consecutive 429s on the same op → skip that op, log to audit.
- **Empty week (zero qualifying calls):** still send Cooper a "quiet week" audit DM with run stats. Do NOT send rep DMs on zero-call territories. Commit a minimal `cooper-audit.md` to the repo for trail.
- **Massive week (50+ calls):** still process all of them. Per-rep DMs may need threading; the markdown file in the repo holds the full detail regardless.

## Final Checklist Before Committing + Posting

- [ ] Every call in the 7-day window was processed or has a documented drop reason in Cooper's audit
- [ ] Every per-call entry has all 10 sections (Header, Use Cases, Pain Points, Objections, Competitive, Resonance, Deal Trajectory, MEDDPICC Delta, Why This Matters, Suggested Next Step)
- [ ] Use cases mapped against `use-case-taxonomy.md` (21 canonical use cases) - taxonomy gaps surfaced separately, not forced into stale categories
- [ ] Pain points tagged ON-THESIS / OFF-THESIS against the relevant segment cheatsheet
- [ ] Trajectory reads use only the 6 canonical labels (ADVANCING / HOLDING / STALLING / AT RISK / EXPANSION / NEW LOGO INTRO) with one-sentence justification each
- [ ] MEDDPICC backfill + refresh applied per policy: Tier 1 fills on empty fields with clear evidence, Tier 1 refreshes on multi-call (≥2) deals where the most recent transcript materially adds/updates info, Tier 2 drift flagged on single-call deals where populated value diverges, Tier 3 holds surfaced for ambiguous evidence, closed deals skipped entirely
- [ ] Lifetime call count computed per deal (full association history, not just this week's window) and used to gate refresh vs. drift
- [ ] Every Tier 1 fill logged in Cooper's audit "MEDDPICC FILLED" table with deal + field + written value + supporting quote + source call + lifetime call count
- [ ] Every Tier 1 refresh logged in Cooper's audit "MEDDPICC REFRESHED" table with deal + field + **OLD value (full text)** + **NEW value (full text)** + supporting quote + source call + lifetime call count - the old-value column is mandatory so reps can spot overwrites of manual edits
- [ ] Material-update guard honored on refreshes (no churn on cosmetic re-phrasings)
- [ ] No HubSpot writes outside the MEDDPICC fill/refresh scope (no company fields, no contact fields, no deal stage changes, no owner reassignments, no notes/tasks/activities)
- [ ] No em dashes in any output (rep DMs, Cooper audit, markdown files)
- [ ] No competitor product names in MaiaEdge-facing commentary (genericized per Content Rules)
- [ ] MSP shown as "MSP / Aggregator" in rep-facing output
- [ ] All dates in America/New_York timezone
- [ ] Markdown audit committed to `weekly-reports/YYYY-MM-DD/calls/`
- [ ] Slack DMs posted: Tim L (if he had calls), Ken (if he had calls), Tim Z routed to Cooper (if International calls), Cooper audit (always)
- [ ] Each rep DM contains the GitHub raw URL for the corresponding markdown file
- [ ] Cooper audit contains run stats, week headline, cross-rep PMF signal, MEDDPICC drift roll-up, trajectory roll-up, accounts worth attention, errors

Work carefully. The deal owner reads this DM before their Monday standup - if the trajectory read is wrong or a pain point is misattributed, they walk into the week with bad context. Accuracy over speed.
