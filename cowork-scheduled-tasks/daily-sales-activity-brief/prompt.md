# Daily Sales Activity Brief (Cowork Scheduled Task)

> Replaces "Daily Call Recap" (renamed 2026-05-05). The legacy `Weekly_Call_Recap_Prompt.md` is retired - do not use it.

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget; HubSpot is the source of truth for the engagement pools (Held / Set / Upcoming). Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload. Scheduled task ID `weekly-call-recap` is preserved for path stability (legacy name; the content here is the canonical Daily Sales Activity Brief).
**Cadence:** Mon-Fri, 6:00 PM CT. Cron: `0 18 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**
**Fire time moved 4:00 PM CT -> 6:00 PM CT 2026-06-03 per Cooper:** reps log calls through the late afternoon (e.g. a 4:00 PM ET call logged at 5:45 PM ET), so a 4 PM CT fire systematically missed the same-day tail. Paired with the rolling window (see Preflight D), the 6 PM fire captures the full day's activity same-day.

A consolidated, exec-scannable brief on the day's sales activity. Goes to the founders + RevOps:
- Abilash Menon (CEO, co-founder) - `U06RVK9NTQR`
- Tim Ziemer (CRO, co-founder) - `U08CMD5PMQE`
- Cooper Kennedy (RevOps) - `U0A24D9RJLS`

Three DMs (one per recipient). The body is identical for all three EXCEPT the final "FOR YOU" section, which is composed separately for each recipient based on what's actionable for them specifically (see Stage 6 audience routing). No rep cascades. No founder-summary thread - everything they need is in the parent message body.

The brief tracks activity for **Tim Lieto, Ken Cunningham, Tim Ziemer, and Markus Hendrich ONLY**. Engagements owned by anyone else (Abilash, Cooper, Kyle, Woody, unmapped owners) are filtered out before bucketing and surface in the audit section only - they never appear in the brief table or the held-calls snapshot.

> **Seller roster note (added 2026-06-03 per Cooper):** Markus Hendrich (`164949459`) is now a tracked seller. He has not been assigned a formal territory yet but is actively working deals and holding meetings, so his activity is tracked; group him under International for brief display until a territory is assigned. (Heads-up: `164949459` was previously logged as an "unmapped" owner and his engagements were being dropped to audit - that stops now.) **Tory Teague is also being added but has no HubSpot owner record yet** - once he has an owner ID, add him as a 5th tracked seller everywhere this roster appears (filter list, bucket list, rep table, `rep_breakdown` JSON, checklist).

The brief answers five questions every weekday at 6pm CT:

1. **Who set what?** Per tracked rep: meetings newly booked in the last 24h (the prospecting signal) AND meetings on the calendar in the next 7 days (the load-ahead signal).
2. **What was held?** Per tracked rep: how many prospect/customer/partner meetings actually occurred in the last 24h.
3. **What's the mix - fresh logos vs existing deals?** Every held and set engagement is classified as `FRESH` (no associated open deal) or `DEAL` (at least one associated open deal). Today's split is compared to a rolling 5-weekday baseline so the founders see whether the team is leaning into prospecting, advancing existing pipeline, or trending in either direction.
4. **How did each call go?** A short, exec-flavored paragraph per held call: who, what they said, where the deal is, what's next. The fresh-or-deal tag rides on the account header.
5. **What needs attention?** Stalled deals, AT-RISK trajectory flags, big logos hitting the calendar - surfaced at the top.

**MEDDPICC is silent.** The routine still runs MEDDPICC backfill + refresh on prospect contacts as a side effect of held calls (same policy as the prior Daily Call Recap routine). Those writes land in HubSpot quietly. They do NOT appear in the exec brief - no per-call MEDDPICC tally, no MEDDPICC mention in the Headline or What Needs Your Attention. Cooper sees the full FILLED / REFRESHED / DRIFT / HELD audit in `cooper-audit.md` on disk; the founders never see it in Slack.

**No git, no GitHub raw URLs.** Markdown is written to `weekly-reports/YYYY-MM-DD/calls/` on disk for archival only. Nothing pushed anywhere.

---

## Connected Tools (Cowork)

- **HubSpot MCP** - read calls, meetings, contacts, deals, tickets, companies; write contact-level MEDDPICC ONLY (no deal-level writes, no company writes, no engagement creates)
- **Slack MCP** - `slack_send_message` (3 identical exec DMs), `slack_read_canvas` + `slack_update_canvas` (cross-routine ledger)
- **No Apollo, no web_search/web_fetch, no git.** Pure HubSpot-internal + Slack-out.

---

## Loud Failure Rule

Every run MUST end with at least one delivered exec DM (Cooper minimum), even on:
- Empty days ("0 sales meetings held in the last 24h - still posting brief for routine health monitoring")
- Fatal errors ("Routine aborted at Stage X")
- Partial runs (rate-limit retries exhausted, partial write completion)

Retry each DM 3× on send failure with exponential backoff (1s → 2s → 4s). If all three recipients fail, append run summary to ledger canvas `F0B0AFSB9LN` so the run is still traceable.

---

## Reference Files (read at run start)

### Repo conventions + master skill
- `CLAUDE.md`
- `skills/call-analysis/SKILL.md` (Mode 1 per-call extraction logic still drives the per-call paragraphs.)

### HubSpot schemas
- `context/hubspot/call-schema.md` (call object properties, `hs_call_summary` HTML structure, association graph, MEDDPICC + Call Transcripts critical rule, Activity Gate)
- `context/hubspot/contact-schema.md` (the 6 contact-level MEDDPICC fields - see Stage 5 for the exact verified internal names; these sync up to deal-level MEDDPICC)
- `context/hubspot/deals-schema.md` (deal stages, MEDDPICC field names, `hs_is_closed_won` / `hs_is_closed_lost` booleans)
- `context/hubspot/poc-schema.md`
- `context/hubspot/territory-model.md` (owner ID → rep mapping)
- `context/hubspot/hubspot-values.md`
- `context/hubspot/property-schema.md`

### Use case + classification
- `context/sales/use-case-taxonomy.md` (every "Use Cases Discussed" maps to one of these)

### Segment cheatsheets - all 6 every run (Enterprise added 2026-05-11 ICP promotion)
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/network-operator.md`
- `context/segments/neocloud.md`
- `context/segments/msp-aggregator.md`
- `context/segments/enterprise.md` (Multi-DC ICP - Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services. Anchor: Meijer)
- `context/segments/enterprise-use-cases.md` (8 priority Enterprise use cases × sub-segment fit - required for use-case taxonomy extraction on Enterprise calls)

### Messaging baseline (for resonance commentary)
- `context/core/messaging-framework.md`
- `context/core/competitive-positioning.md`

### Core ICP context
- `context/core/maiaedge-101.md` (PBC / Port Extender / PCE; "Carrier infrastructure" only)
- `context/core/icp-playbook.md`

---

## Preflight Checks (before Stage 1)

A. Verify HubSpot MCP connected. If not → write `weekly-reports/YYYY-MM-DD/calls/cooper-run-report.md` with blocker, post Cooper-only DM, exit.

B. Verify Slack MCP connected. Same as A.

C. Verify today is a weekday (Mon-Fri) in America/New_York. If not → STOP with abort report (no weekend runs).

D. Compute the two run windows (both in ET):

**Held window** - what occurred. ROLLING `prior-run -> now` window (changed 2026-06-03 - see rationale below):
- `held_end_et` = run-time (now). NOT a fixed 15:59 cutoff. This is the key fix: the window closes at run-time so calls held and logged in the late afternoon are captured same-day.
- `held_start_et` = the routine's prior `lastRunAt` (the moment the last successful run closed its window). This makes consecutive windows continuous and gapless - every engagement is seen exactly once, nothing falls into a dead zone between runs.
- Fallbacks when `lastRunAt` is unavailable or stale:
  - No `lastRunAt` on record (first run) -> default `held_start_et` = now minus 24h (Tue-Fri) or now minus ~72h (Mon weekend catch-up).
  - `lastRunAt` is older than ~30h (a missed/skipped run, e.g. a holiday or a Monday after a Friday no-fire) -> use `lastRunAt` directly so the gap is back-filled; do not truncate to 24h. The window simply widens to cover everything since the last successful close.
- WHY THIS CHANGED: the old fixed window ended at 15:59 ET while the task fires later in the day (now 6 PM CT), leaving a 60-120 min same-day blind spot. Calls held after the cutoff - or logged after run-time - were deferred a day or, when logged very late, slipped entirely (observed repeatedly: ONUG 2026-06-03 held 4:00 PM ET / logged 5:45 PM ET; the 6/2 Voice Exchange discovery call; the 5/28 Movi 4:30 PM call). Anchoring to `prior-run -> now` removes both the gap and the deferral.

**Set window** - what got booked:
- Same calendar window as Held (`prior-run -> now`). See Stage 1B for the precise Set measurement rule (true bookings only, not auto call-logs).

**Upcoming window** - what's on the calendar:
- `upcoming_start_et` = run-time (now); `upcoming_end_et` = run-time + 7 days. Counts meetings/calls whose `hs_timestamp` falls in the next 7 days, regardless of when they were booked.

Convert all four endpoints to epoch ms for HubSpot timestamp filters.

---

## Critical Invariants

### Timezone
America/New_York. Convert HubSpot UTC `hs_timestamp` and `hs_createdate` before filtering. Never use "this week" language in the brief - write "Last 24h" / "Last weekend" / "Next 7 days" / explicit ET dates.

### Write Scope (narrow - MEDDPICC contacts ONLY)
The ONLY HubSpot write path = MEDDPICC backfill on the 6 contact-level MEDDPICC fields (see Stage 5 for exact names) on prospect CONTACTS from transcript evidence. No company fields, no deal-stage changes, no owner reassignments, no notes/tasks/activities created. Never write to deal-level MEDDPICC properties directly - the contact-level fields SYNC UP to the deal-level MEDDPICC fields automatically, and direct deal-level writes are blocked by HubSpot's calculated-property restriction. The MEDDPICC policy is otherwise unchanged from the prior Daily Call Recap routine - see "MEDDPICC Backfill + Refresh Policy" below.

### Internal-Only Filter

A meeting/call is INTERNAL ONLY (drop from the brief) if BOTH:
- Every associated contact has an email ending in `@maiaedge.com`, `@maiaedge.io`, or `@maia-tech.com` (or has no associated contacts at all), AND
- The only associated company is MaiaEdge own (`124293230301`), or there are no associated companies.

If either condition fails (any external contact OR any external company), the meeting is EXTERNAL - include it. **Be permissive.** Cooper wants only obvious internal team syncs excluded; non-ICP customer calls, partner training, and exploratory chats with external companies all count.

This means a 4-minute "internal-flavored" sync that has even one external attendee (like a partner contact) still makes the brief. The bar is intentionally low.

### Skip Rules (still apply within the external set)
- Drop calls with `hs_call_duration < 60000` (under 1 min) AND no associated deal/POC. (A 30-second call associated to an open deal still surfaces - could be a ringback or quick coordination. A 30-second call to a Tier 5 with no deal does not.)
- Drop calls where `hs_call_summary`, `hs_call_body`, AND `hs_call_has_transcript = "false"` are all empty.
- Drop calls associated to a company with `customer_segment = "Flagged for deletion"`.

### Content Rules
- NO em dashes anywhere in MaiaEdge commentary (preserve verbatim quotes from prospects).
- Category descriptor: "Carrier infrastructure" only.
- Genericize competitor PRODUCT names: "Megaport Fabric" / "Equinix Fabric" → "third-party interconnection fabric".
- MSP segment label in the brief = "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).
- Enterprise segment label in the brief = "Enterprise" (matches the HubSpot internal value `Enterprise-CustomerSegment`, display "Enterprise"). When showing Enterprise sub-segment in the account header, use the sub-segment name (`Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`).
- Exec-friendly tone: assume the reader has 90 seconds. Lead with the headline. No jargon dumps.

---

## Stage 1: Pull Three Engagement Pools

### 1A. Held - calls + meetings that occurred in the held window

`search_crm_objects` on CALL with `hs_timestamp` GTE/LTE the held window epochs.
Properties: `hs_call_title`, `hs_call_summary`, `hs_call_body`, `hs_call_has_transcript`, `hs_call_recording_url`, `hs_call_direction`, `hs_call_duration`, `hs_call_status`, `hs_call_disposition`, `hs_timestamp`, `hs_createdate`, `hubspot_owner_id`. Associations: `["COMPANY", "CONTACT", "DEAL", "TICKET"]`. Limit 100. Paginate.

Repeat for MEETING engagement objects in the same window (HubSpot's separate object for scheduled meetings). Some HubSpot accounts log meetings as CALL objects with `hs_call_source = "HUBSPOT_MEETINGS"`; in this org, the data we've seen does ride on the CALL object, but query MEETING too as a safety net.

**Dedup rule (strengthened 2026-06-03 - do NOT rely on `hs_object_id` alone).** The same real-world conversation routinely logs as MULTIPLE objects with DIFFERENT `hs_object_id`s: a CALL (with transcript/summary) plus a MEETING twin, plus sometimes an owner-less duplicate CALL/MEETING (a recurring HubSpot logging artifact). On 2026-06-03 the Digital Realty call had 3 objects and LatWan had 3. To collapse these into ONE held engagement:
1. First drop owner-less duplicates (owner `None`) - they are not tracked-rep owned and fall to audit anyway.
2. Then cluster the remainder by fuzzy match on (normalized title + `hs_timestamp` within ±90 min + same `hubspot_owner_id`). Treat each cluster as ONE engagement.
3. Within a cluster, keep the richest record as canonical - prefer the one carrying `hs_call_summary`/`hs_call_body`/transcript (usually the CALL) over a bare MEETING shell. Count the engagement once; use the canonical record for the per-call snapshot and MEDDPICC.
Log the collapsed duplicates (IDs + why) to the audit section.

### 1B. Set - engagements newly created in the set window

Same query shape, but filter on `hs_createdate` GTE/LTE set window epochs.

**Set measurement rule (codified 2026-06-03 - this was previously re-derived every run, now it is law).** "Set" means a genuinely NEW booking made in the window - a real prospecting/load-ahead signal. Measure Set on:
- MEETING objects whose `hs_createdate` falls in the window, AND
- CALL objects that are forward-dated bookings (a future `hs_timestamp` set at create time).

EXCLUDE from Set the auto-generated / after-the-fact call logs - any CALL or MEETING object whose `hs_createdate` is approximately equal to its `hs_timestamp` (i.e. logged at-or-after the meeting happened, including `hs_call_source = "HUBSPOT_MEETINGS"` auto-logs and manually back-logged past calls). Counting those as "Set" double-counts the Held pool and falsely inflates the booking signal. A meeting whose time is in the past relative to its create time is a log, not a booking.
Net effect: Set counts true forward bookings only. It may still overlap Held when a meeting is booked and held the same day; that legitimate book-and-hold is fine. The point is to exclude retroactive logs. Final dedup against Held still happens in Stage 2.

### 1C. Upcoming - engagements on the calendar over the next 7 days

`search_crm_objects` on CALL and MEETING with `hs_timestamp` GTE now, LTE now+7d. Properties: `hs_object_id`, `hs_call_title` / `hs_meeting_title`, `hs_timestamp`, `hs_createdate`, `hs_call_status` / `hs_meeting_outcome`, `hubspot_owner_id`. Associations: `["COMPANY", "DEAL"]` (we need the company name + tier + segment for callouts and the deal tag for FRESH/DEAL classification). We don't need summaries/transcripts on upcoming (haven't happened yet).

### Hydrate associations on demand
- Company: `name`, `customer_segment`, `company_sub_segment`, `account_tier`, `state`, `country`, `account_brief`, `recent_news_or_trigger_event`, `infrastructure_profile`, `domain`.
- Contacts: `firstname`, `lastname`, `jobtitle`, `email`, `hubspot_owner_id`, `flagged_for_deletion`, plus the 6 contact-level MEDDPICC fields (exact names in Stage 5).
- Deals: `dealname`, `dealstage`, `amount`, `closedate`, `hs_priority`, `hs_is_closed_won`, `hs_is_closed_lost`. Do NOT pull deal-level MEDDPICC.
- Tickets (POC): per `poc-schema.md`.

---

## Stage 2: Filter + Bucket

### Apply Internal-Only Filter
Walk every engagement in all three pools. Drop any that match the Internal-Only Filter above. Log dropped engagements with reason for the audit section ("internal sync, no external contact/company").

### Apply Skip Rules
On the Held pool only: drop sub-1-minute calls without deal/POC, drop calls with no summary AND no transcript, drop calls on Flagged-for-deletion companies.

### Filter to tracked reps ONLY

The brief tracks activity for **Tim Lieto, Ken Cunningham, Tim Ziemer, and Markus Hendrich only**. Drop every engagement in all three pools whose `hubspot_owner_id` is not one of the tracked-seller IDs below before bucketing. Engagements owned by anyone else (Abilash, Cooper, Kyle, Woody, unmapped, etc.) get logged to the audit section only - they do not appear in the brief table or the Held Calls snapshot, and their associated contacts are NOT processed for MEDDPICC backfill in Stage 5.

### Bucket by rep
Group the surviving engagements by `hubspot_owner_id`:
- East - `161889085` Tim Lieto
- West - `162339176` Ken Cunningham
- International - `159350430` Tim Ziemer
- International (no formal territory yet) - `164949459` Markus Hendrich
- _(pending owner ID)_ Tory Teague - add as a tracked seller once his HubSpot owner record exists

Any tracked seller without activity in any of the three pools still appears in the brief table with a `0 / 0 / 0` row - silence is itself a signal.

### Classify each engagement as FRESH or DEAL

For every Held and Set engagement that survives the rep filter, walk its associated DEAL records (already hydrated in Stage 1).

- **FRESH** - no associated deals at all, OR every associated deal has `hs_is_closed_won = true` OR `hs_is_closed_lost = true`. Treat closed-won and closed-lost deals as historical, not active. (Fresh means there is no live opportunity attached; the meeting is either prospecting, customer expansion conversation pre-deal, partner exploration, or an account that hasn't converted yet.)
- **DEAL** - at least one associated deal is open (neither closed-won nor closed-lost). Capture the largest open deal `amount` and `dealstage` for the brief tag.

Tie-break: if an engagement has BOTH closed and open deals associated, it counts as DEAL (the open one wins). Persist the classification on the engagement record for use in Stage 6.

### Compute today's mix and the rolling 5-day trend

After classification, tally per pool:
- `held_fresh`, `held_deal`, `held_total`
- `set_fresh`, `set_deal`, `set_total`

Then compute the trend baseline by reading prior weekday summaries from disk:
- For the prior 5 weekday runs (skip weekends), read `weekly-reports/[YYYY-MM-DD]/calls/activity-summary.json` if present.
- Compute trailing 5-weekday averages: `avg_held_fresh_5d`, `avg_held_deal_5d`, `avg_set_fresh_5d`, `avg_set_deal_5d`. Use whatever subset of the 5 is available; if fewer than 3 prior runs are on disk, mark trend as `BASELINE BUILDING` and skip the up/down arrows for this run.
- For each metric, compare today vs trailing average. Tag direction:
  - **UP** if today >= ceil(avg * 1.20) AND today exceeds avg by at least 1 absolute count
  - **DOWN** if today <= floor(avg * 0.80) AND avg exceeds today by at least 1 absolute count
  - **FLAT** otherwise
- Held trend matters more than Set trend for the headline (held = real conversations); call out Set trend only if it diverges sharply from Held (e.g. Held DOWN but Set UP = pipeline is being built but not converting to conversations yet).

Persist today's tallies to `weekly-reports/YYYY-MM-DD/calls/activity-summary.json` in Stage 8 so future runs can read it.

### Detect calendar movement vs yesterday's Upcoming snapshot

Read yesterday's weekday `weekly-reports/[YYYY-MM-DD]/calls/upcoming-snapshot.json` (skip weekends - Monday compares to last Friday). The snapshot is a list of objects with `hs_object_id`, `hs_timestamp`, `hubspot_owner_id`, `company_name`, `account_tier`, `segment`, `fresh_or_deal`. If yesterday's file does not exist, mark calendar movement as `BASELINE BUILDING - first run, no comparison`.

For every engagement in today's Upcoming pool that is owned by one of the tracked sellers, classify against yesterday's snapshot:

- **PUSHED** - `hs_object_id` exists in both. Today's `hs_timestamp` is **later** than yesterday's by ≥ 1 hour. Capture old date and new date.
- **PULLED IN** - `hs_object_id` exists in both. Today's `hs_timestamp` is **earlier** than yesterday's by ≥ 1 hour.
- **NEW** - `hs_object_id` is in today's pool but NOT in yesterday's. (Someone booked it today or yesterday after the prior run.)
- **DROPPED** - `hs_object_id` is in yesterday's snapshot but NOT in today's pool, AND yesterday's `hs_timestamp` was still in the future at today's run-time. (Cancelled, or rescheduled outside the 7-day window.)

Movement under 1 hour is noise (calendar reschedule rounding) and is ignored. Movement that just rolls a meeting OUT of the 7-day window counts as PUSHED with new date noted; movement that pulls one IN counts as PULLED IN with old date noted. Persist today's snapshot to `weekly-reports/YYYY-MM-DD/calls/upcoming-snapshot.json` in Stage 8.

Cap the brief callout at 5 movement items, sorted by impact: DROPPED on Tier 1-2 first, then PUSHED on Tier 1-2, then NEW on Tier 1-2, then anything else. If 0 movement, omit the section entirely from the brief (don't render an empty header).

---

## Stage 3: Per-Held-Call Analysis (call-analysis Mode 1, exec-flavored)

For each Held engagement that survives filters, follow `skills/call-analysis/SKILL.md` Mode 1 - but ABBREVIATED for exec scanability. Each held call gets exactly:

- **Headline (1 sentence):** the 90-second-reader takeaway. What happened, what it means.
- **Use Cases (1 line):** taxonomy items, comma-separated.
- **Pain (1 line):** the strongest pain explicit/implicit; on-thesis or off-thesis tag.
- **Trajectory (1 word + 1 phrase):** one of ADVANCING / HOLDING / STALLING / AT RISK / EXPANSION / NEW LOGO INTRO + a 5-10 word justification.
- **Next step (1 line):** one concrete action.

That's 5 lines per call. NOT the full Mode 1 dump. **No MEDDPICC line in the brief** - the writes happen silently in Stage 5 and only show up in `cooper-audit.md` on disk. The full Mode 1 record (including the MEDDPICC tally) still gets written to the markdown audit.

---

## Stage 4: Per-Account Roll-up (only when needed)

If the same account surfaces in ≥2 held calls in the window → add a 2-line roll-up at the top of the per-account block: "2 calls today, narrative is X, MEDDPICC pulled from most recent." Daily cadence usually means this stage is empty.

---

## Stage 5: MEDDPICC Backfill + Refresh (silent side effect)

Same policy as the prior Daily Call Recap routine. Apply it to held calls only. The full policy table below is unchanged.

For each substance-passing held call, take its associated CONTACTS, then filter:
- Drop MaiaEdge internal contacts (`@maiaedge.com` / `@maiaedge.io` / `@maia-tech.com`).
- Drop contacts where `flagged_for_deletion = true`.
- Drop contacts whose primary associated company has `customer_segment = "Flagged for deletion"`.

For each surviving prospect contact `C`:
1. Skip if primary deal `hs_is_closed_won = true` OR `hs_is_closed_lost = true`.
2. Skip writes if primary deal `dealstage = "contractsent"`. Surface as Tier 3 hold.
3. Pick source transcript: most recent call in this run window per the MEDDPICC Rule.
4. Compute lifetime call count for contact `C`.
5. For each of the contact-level MEDDPICC fields below, apply this matrix.

**The tenant exposes exactly 6 contact-level MEDDPICC fields (verified via `search_properties` 2026-06-03). Use these exact internal names; do NOT guess others:**
- `meddpicc_pain_contact` (Identified Pain)
- `meddpicc_use_case` (Use Case)
- `meddpicc_criteria_contact` (Decision Criteria)
- `meddpicc_competition_contact` (Competition)
- `meddpicc_metrics_contact` (Metrics)
- `meddpicc_infrastructure_contact` (Infrastructure)

There is NO contact-level economic-buyer or champion field in this tenant - do not attempt to write `meddpicc_economic_buyer_contact` / `meddpicc_champion_contact` (they 400). Capture economic-buyer / champion observations in the audit only.

**Contact -> Deal sync (per Cooper 2026-06-03):** these contact-level fields SYNC UP to the deal-level MEDDPICC fields automatically. That is exactly why we write at the contact level and never write deal-level MEDDPICC directly (direct deal-level writes are blocked by HubSpot's calculated-property restriction). A clean contact write IS the deal-level update - so apply the confidence + material-update guards rigorously, because the value propagates to the deal record.

Matrix:

| Current value | Lifetime calls | Most-recent transcript evidence | Action | Tier |
|---|---|---|---|---|
| Empty | any | Clear, specific, attributable | Write extracted value | Tier 1 fill |
| Empty | any | Tangential / ambiguous / inferred | Hold, surface in audit | Tier 3 |
| Empty | any | Topic never came up | Skip silently | - |
| Populated | 1 | Transcript matches existing | Skip silently | - |
| Populated | 1 | Transcript diverges materially | Flag DRIFT in audit, no overwrite | Tier 2 |
| Populated | ≥2 | Clear, materially adds or updates info | Refresh: overwrite | Tier 1 refresh |
| Populated | ≥2 | Clear, matches existing | Skip silently | - |
| Populated | ≥2 | Topic not on this window's most-recent call | Skip - preserve older snapshot | - |
| Populated | ≥2 | Ambiguous on this window's call | Skip - don't degrade with weak evidence | - |

6. Material-update guard: only refresh if new value adds detail or replaces stale info.
7. Confidence guard: extracted value must be directly supported by quote/paraphrase, in MaiaEdge voice (no em dashes, no banned product names, "Carrier infrastructure" only), under 500 chars.
8. HubSpot write: `manage_crm_objects` updateRequest, `objectType: "contacts"`, `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`. Batch cap 10/call. ≥250ms between batches. Backoff 1s → 2s → 4s on 429.
9. Audit trail: every Tier 1 write into the `cooper-audit.md` MEDDPICC tables. Every Tier 2 DRIFT into a flag table. Every Tier 3 hold into the hold table.
10. Failure handling: per-record try/except. Log failures, do not abort.

---

## Stage 6: Compose the Exec Brief

The brief lives entirely in the parent Slack message body. No threaded follow-ups. No external links. ~3,500-4,000 chars max so all three execs see one screenful.

### Slack formatting rules - read carefully, the brief renders or fails on these

- Slack mrkdwn uses **single asterisks** for bold (`*bold*`), single underscores for italic (`_italic_`), single backticks for inline code, triple backticks for code blocks. Markdown-style `**bold**` does NOT render in Slack - it shows as literal asterisks.
- **All tabular data goes in triple-backtick code blocks** so columns align in monospace. Pipe-separated markdown tables render as ugly literal pipes in Slack and are forbidden in this brief.
- Use ` · ` (middle dot, U+00B7) as inline separator on account header lines. NO em dashes anywhere.
- Bullets: leading `• ` (U+2022 + space). Slack does not render `*` or `-` bullets the way Markdown does.
- Use `>` at line start for blockquotes - Slack honors this and indents the line, which is how the per-call snapshot details render cleanly.
- Emojis are fine and welcome at section markers (one per section max - don't sprinkle).

### Brief Structure (shared body - same for all 3 recipients)

```
🎯 *Daily Sales Activity · [Day], [MM/DD/YYYY]*
_Held: [held_start MM/DD HH:MM] → [held_end MM/DD HH:MM] ET · Set: same window · Upcoming: next 7 days_

*HEADLINE*
[1-2 sentences. Lead with the trend signal if it diverges from baseline; otherwise lead with the most notable trajectory event of the day. Examples: "Heavy deal-day · 3 of 4 held calls on open deals (vs 5d avg 1.8 · UP). Pearce SOW tomorrow, RocNet on track 5/15. Sungard AT-RISK on EB churn." OR "Prospecting-heavy · 3 fresh-logo intros (vs 5d avg 1.0 · UP), 1 deal call. Telxius LATAM the standout." OR "Quiet day · 0 held calls (vs 5d avg 2.4 · DOWN). 9 meetings on calendar next 7d." NO MEDDPICC mentions.]

*ACTIVITY BY REP*
` ` ` (triple backtick - open code block)
              Set   Held   Up7d
Tim Lieto      3     2      4
Ken C          2     1      3
Tim Z          1     1      2
Markus H       1     0      1
─────────────────────────────
TOTAL          7     4     10
` ` ` (triple backtick - close code block)

*PIPELINE MIX (vs 5d avg)*
` ` `
          Fresh   Deal   Total
Held        1      3       4     →  Fresh FLAT  · Deal UP
Set         2      4       6     →  Fresh FLAT  · Deal UP
` ` `
_[1 sentence interpretation. Examples: "Team leaning into existing pipeline; deal calls outpacing prospecting 3:1 today." OR "Prospecting motion doubled vs last week - 3 fresh intros today." OR "Baseline building · trend arrows go live once 3 prior weekday runs are on disk."]_

*NEXT 7 DAYS · calendar movement*
[Render this section ONLY if there is at least one PUSHED / PULLED IN / NEW / DROPPED item from Stage 2.5. Cap at 5 items, prioritized by tier and impact. Use these glyphs at line start so it scans fast:]
• ⏩ *Pushed:* [Account] · [old date] → [new date] · [Rep] · [tier/segment]
• ⏪ *Pulled in:* [Account] · [old date] → [new date] · [Rep]
• 🆕 *New on calendar:* [Account] · [date] · [Rep] · [tier/segment]
• ❌ *Dropped:* [Account] · was [date] · [Rep] · [reschedule status if known]

[If 0 movement → omit the entire section. If first run with no prior snapshot → render: "_Calendar movement tracking starts tomorrow - no prior snapshot on disk._"]

*HELD CALLS*

*[Account 1]* · `[FRESH]` or `[DEAL · $XXk · stage]` · [Segment] · Tier [N] · [Rep First Name]
[Headline sentence - 90-second-reader takeaway.]
> Use Cases: [comma list]
> Pain: [strongest pain · on-thesis/off-thesis tag]
> Trajectory: [LABEL] · [5-10 word justification]
> Next: [concrete action with date]

*[Account 2]* · ...

(Repeat per held call. 5 lines each. NO MEDDPICC line.)

[FOR YOU section is composed separately per recipient - see "Per-recipient FOR YOU routing" below. Insert it here in each DM.]

_Full call detail + MEDDPICC writes audit: `weekly-reports/[YYYY-MM-DD]/calls/cooper-audit.md`_
```

### Per-recipient FOR YOU routing

Every attention item identified during the run gets tagged with a target audience based on what it requires. Then per recipient, filter to that recipient's items + any tagged `all`. Skip the section entirely for a recipient if they have 0 items.

**Audience rules:**

- **`tim_z`** (CRO - runs the sales team) - gets: AT-RISK / STALLING flags on any deal, exec-to-exec intro asks where Tim Z is the named asker, rep load imbalances or inactivity flags, key meetings on his own calendar that need prep, MEDDPICC drift severe enough to threaten a deal (rare - only when Stage 5 logs a Tier 2 DRIFT on a deal at proposal/contract stage).
- **`abilash`** (CEO) - gets: Tier 1 logo intros booked or held, escalations where CEO involvement could change a deal's trajectory, customer expansion opportunities surfaced in held calls, anything strategic that maps to board/investor narrative.
- **`cooper`** (RevOps) - gets: routine health flags (Stage 5 write failures, MCP timeouts, DM delivery retries), data-quality observations (companies hitting the brief with bad segment / missing tier / wrong owner), trend baseline status (BASELINE BUILDING countdown), any Tier 3 holds that need human review.
- **`all`** - genuinely cross-cutting items that all three should see. Use sparingly. Example: a Tier 1 logo just went `closedwon` mid-call (everyone wants to know).

**Composition rule:** if a recipient has 0 items in their bucket, omit their FOR YOU section entirely from their DM. The shared body alone is the brief that day. Don't render an empty header.

**Per-recipient block format:**
```
*FOR YOU · [First Name]*
• [Item 1 · 1-2 lines · what + the ask + by-when]
• [Item 2]
• [Item 3]
```

Cap at 4 items per recipient. If more than 4 items are tagged for one person, keep the 4 highest-impact (Tier 1 > Tier 2 > Tier 3+; AT-RISK > STALLING > FYI) and append a one-liner: `_+ [N] more in cooper-audit.md_`.

If the brief overflows ~4,500 chars (rare - daily run is usually 1-5 held calls), trim per-call paragraphs to 3 lines (drop Use Cases line · keep Headline + Pain + Trajectory + Next).

### Empty-day variant

If the Held pool is empty after filters, the brief still sends with:

```
🎯 *Daily Sales Activity · [Day], [MM/DD]*
_Held: ... · Upcoming: next 7d_

*HEADLINE*
0 prospect/customer/partner calls held in this window (vs 5d avg of [N] · DOWN). [N] meetings on the calendar over the next 7 days · top accounts: [top 3 by tier/segment].

*ACTIVITY BY REP*
` ` `
              Set   Held   Up7d
Tim Lieto      X     0      Z
Ken C          X     0      Z
Tim Z          X     0      Z
Markus H       X     0      Z
─────────────────────────────
TOTAL          X     0      Z
` ` `

*PIPELINE MIX*
[Set row only if any meetings were booked today; skip if Set is also 0.]

*NEXT 7 DAYS · calendar movement*
[Same rendering rules as the regular brief - emit only if movement detected.]

[Per-recipient FOR YOU section - empty days often have no items, so this commonly omits.]

_Quiet day. Routine fired clean._
```

---

## Stage 7: Deliver

Compose 3 DM bodies. Bodies share the entire shared brief structure (Headline → Activity by Rep → Pipeline Mix → Next 7 Days → Held Calls). Then per recipient, append their tailored `FOR YOU · [Name]` block (skip the section entirely if 0 items routed to them).

Send in sequence:
1. `slack_send_message` to `U06RVK9NTQR` (Abilash) - body + Abilash's FOR YOU
2. `slack_send_message` to `U08CMD5PMQE` (Tim Z) - body + Tim Z's FOR YOU
3. `slack_send_message` to `U0A24D9RJLS` (Cooper) - body + Cooper's FOR YOU

≥1s between each send. Capture each message link for the audit. The shared body section is byte-identical across the three messages so Cooper's audit can verify drift if any of the FOR YOU routing logic misfires.

If any DM fails: retry with exponential backoff 1s → 2s → 4s. If all 3 attempts on a given recipient fail, skip that recipient and continue. After all 3 are attempted, if even one succeeded → mark run YELLOW and log in audit. If ALL 3 failed → fall back to writing run summary into the cross-routine ledger canvas `F0B0AFSB9LN`.

---

## Stage 8: Markdown Audit (local archive only)

Write to `weekly-reports/YYYY-MM-DD/calls/`:
- `daily-brief.md` - the exact brief body that was sent (so Cooper can see what shipped)
- `all-calls.md` - every held call's full Mode 1 record concatenated, chronological. Each entry tagged FRESH or DEAL with associated deal IDs/amounts/stages.
- `cooper-audit.md` - MEDDPICC FILLED / REFRESHED / DRIFT / HELD tables (the founder-invisible writes), errors, trajectory roll-up, per-rep activity numbers, fresh-vs-deal classification log per engagement, calendar movement log (PUSHED / PULLED IN / NEW / DROPPED with full context), and the per-recipient FOR YOU routing decision log so Cooper can audit which items went to whom and why.
- `upcoming-snapshot.json` - today's full Upcoming pool serialized for tomorrow's calendar-movement comparison. List of `{hs_object_id, hs_timestamp, hubspot_owner_id, company_name, account_tier, segment, fresh_or_deal}`. Without this file written, tomorrow's run cannot detect movement.
- `activity-summary.json` - machine-readable tallies for the next run's trend baseline. Schema:
  ```json
  {
    "date": "YYYY-MM-DD",
    "weekday": "Wed",
    "held": {"fresh": N, "deal": N, "total": N},
    "set":  {"fresh": N, "deal": N, "total": N},
    "upcoming_total": N,
    "rep_breakdown": {
      "tim_lieto": {"set": N, "held": N, "upcoming": N},
      "ken_cunningham": {"set": N, "held": N, "upcoming": N},
      "tim_ziemer": {"set": N, "held": N, "upcoming": N},
      "markus_hendrich": {"set": N, "held": N, "upcoming": N}
    }
  }
  ```

ATX-style headings. NO em dashes. **No git operations.** Files live on disk only.

---

## Stage 9: Cross-routine Ledger

- **At run start:** read canvas `F0B0AFSB9LN`. Drain Tier 3 items belonging to this routine.
- **At run end:** append NEW Tier 3 holds with `[YYYY-MM-DD]`. Append ONE row to "Run log": `| YYYY-MM-DD HH:MM ET | Daily Sales Activity Brief | <emoji> | <summary> | <link to Cooper's DM> |`. Trim entries older than 90 days.

---

## Failure Modes

- Per-record try/except on every read, association hydration, summary parse.
- HubSpot MCP unreachable → write `cooper-run-report.md` blocker, post Cooper-only DM (skip Abilash + Tim Z if HubSpot dead - they'd get a useless brief), exit cleanly.
- Slack MCP unreachable → write all markdown to disk, write run summary to ledger canvas if canvas write still works, exit.
- 429: pause 10s, retry. 3 consecutive 429s on same op → skip op, log to audit.
- Empty day → still send all 3 DMs with empty-day variant.
- Heavy day (rare on daily cadence - would need 15+ external held calls) → trim per-call paragraphs to 4 lines, brief still fits in one message.

---

## Final Checklist

- [ ] Today is a weekday (Mon-Fri); aborted cleanly if not
- [ ] Held window = rolling `prior-run -> now` (gapless); fallbacks applied if `lastRunAt` is missing (24h/72h) or stale >30h (widen to cover the gap)
- [ ] Set window matches Held window (`prior-run -> now`); Set measured on true bookings per Stage 1B (NOT auto call-log twins)
- [ ] Upcoming window = next 7 days from run-time
- [ ] Internal-Only Filter applied permissively (only obvious internals dropped)
- [ ] Skip rules applied within external set
- [ ] Every held call has the 5-line exec block (Headline / Use Cases / Pain / Trajectory / Next) - NO MEDDPICC line in the brief
- [ ] Each held call carries a `[FRESH]` or `[DEAL · $XXk · stage]` tag in its account header
- [ ] Activity-by-Rep and Pipeline Mix tables rendered in triple-backtick code blocks (NOT pipe-separated markdown tables)
- [ ] Slack mrkdwn used throughout: single asterisks for bold, single underscores for italic, `• ` bullets, `>` blockquotes, ` · ` middle-dot inline separator
- [ ] Pipeline Mix table renders with today's Held + Set splits and trend tags (UP/DOWN/FLAT/BASELINE BUILDING)
- [ ] Per-rep activity table includes ONLY Tim Lieto, Ken Cunningham, Tim Ziemer, Markus Hendrich (zeros allowed for any tracked seller with no activity; add Tory Teague once he has an owner ID)
- [ ] Engagements owned by anyone outside the tracked sellers were filtered out before bucketing and surface in audit only
- [ ] FRESH vs DEAL classification applied to all Held + Set engagements per the Stage 2 rule
- [ ] Trailing 5-weekday baseline computed from prior `activity-summary.json` files; trend marked BASELINE BUILDING if fewer than 3 prior runs on disk
- [ ] `activity-summary.json` AND `upcoming-snapshot.json` written for today so tomorrow's run has baseline + movement data
- [ ] Calendar movement section (NEXT 7 DAYS) emitted only if at least one PUSHED/PULLED IN/NEW/DROPPED detected; otherwise omitted entirely
- [ ] Each movement item ranked by tier impact (Tier 1-2 first), capped at 5 in the brief
- [ ] Per-recipient FOR YOU sections composed separately for Abilash / Tim Z / Cooper using audience routing rules
- [ ] FOR YOU section omitted entirely from a recipient's DM if 0 items routed to them
- [ ] FOR YOU capped at 4 items per recipient; overflow indicated with `+ N more in cooper-audit.md` line
- [ ] MEDDPICC policy still applied silently (Tier 1 fills/refreshes, Tier 2 DRIFT, Tier 3 holds, closed deals skipped) - writes land in HubSpot, NOT in the brief
- [ ] Headline does not mention MEDDPICC, drift, or any audit-only metric
- [ ] Lifetime call count computed and used to gate refresh vs. drift
- [ ] Material-update guard honored on refreshes
- [ ] No HubSpot writes outside contact-level MEDDPICC
- [ ] No em dashes
- [ ] No competitor product names
- [ ] MSP shown as "MSP / Aggregator"
- [ ] All dates ET
- [ ] Markdown audit + `upcoming-snapshot.json` + `activity-summary.json` written to `weekly-reports/YYYY-MM-DD/calls/` (no git operations)
- [ ] 3 DMs sent to Abilash + Tim Z + Cooper (shared body byte-identical, FOR YOU section unique per recipient - each with retry logic)
- [ ] Cross-routine ledger row appended
