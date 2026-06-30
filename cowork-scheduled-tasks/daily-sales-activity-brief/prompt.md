# Daily Sales Activity Brief (Cowork Scheduled Task)

> Replaces "Daily Call Recap" (renamed 2026-05-05). The legacy `Weekly_Call_Recap_Prompt.md` is retired - do not use it.

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget; HubSpot is the source of truth for the engagement pools (Held / Set / Upcoming). Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload. Scheduled task ID `weekly-call-recap` is preserved for path stability (legacy name; the content here is the canonical Daily Sales Activity Brief).
**Cadence:** Mon-Fri, 6:00 PM CT. Cron: `0 18 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**
**Fire time moved 4:00 PM CT -> 6:00 PM CT 2026-06-03 per Cooper:** reps log calls through the late afternoon (e.g. a 4:00 PM ET call logged at 5:45 PM ET), so a 4 PM CT fire systematically missed the same-day tail. Paired with the rolling window (see Preflight D), the 6 PM fire captures the full day's activity same-day.

A consolidated, exec-scannable brief on the day's sales activity. Goes to the founders + RevOps + the field reps + POC lead + Marketing:
- Abilash Menon (CEO, co-founder) - `U06RVK9NTQR`
- Tim Ziemer (CRO, co-founder) - `U08CMD5PMQE`
- Cooper Kennedy (RevOps) - `U0A24D9RJLS`
- Tim Lieto (AVP, North America Sales - Northeast + West) - `U0A973L1HFF`
- Ken Cunningham (Sales, Southeast) - `U0AE1PGCB6C`
- Tory Teague (Sales, Central) - `U0B7MU3P3QD` (added as a FOR YOU recipient 2026-06-17 per Cooper - now has HubSpot owner ID `165480917`)
- Markus Hendrich (Sales, Europe) - `U0B6B4U8QKD` (added as a FOR YOU recipient 2026-06-17 per Cooper)
- Patrick Timmons (POC lead - "pt") - `U06RVKNTRPB`
- Hannah Roberts (Marketing) - `U09BYB61FCN` (added 2026-06-16 per Cooper; **shared body ONLY, never a FOR YOU section** - she gets the day's activity view, not action items)

> **Recipient expansion (added 2026-06-05 per Cooper):** Tim Lieto, Ken Cunningham, and Patrick Timmons ("pt") were added as recipients. Tim Lieto and Ken Cunningham each get a rep-tailored FOR YOU scoped to engagements THEY own (their AT-RISK/STALLING deals, their upcoming key meetings, their Tier 3 holds). Patrick Timmons manages the POC side that sits under many of the open deals, so his FOR YOU is scoped to POC activity (held calls and upcoming meetings on accounts with an associated POC ticket, POC status changes, POCs needing attention) across all reps - not a single book of business. See Stage 6 audience routing.

Nine DMs (one per recipient). The body is identical for all nine EXCEPT the final "FOR YOU" section, which is composed separately for the action-taking recipients based on what's actionable for them (see Stage 6 audience routing). **Hannah Roberts (Marketing) is the standing exception: she always receives the shared body with NO FOR YOU section** - she gets visibility into what happened that day, not a task list. No rep cascades. No founder-summary thread - everything they need is in the parent message body.

The brief tracks activity for **Tim Lieto, Ken Cunningham, Tory Teague, Markus Hendrich, and Tim Ziemer ONLY**. Engagements owned by anyone else (Abilash, Cooper, Kyle, Woody, unmapped owners) are filtered out before bucketing and surface in the audit section only - they never appear in the brief table or the held-calls snapshot.

> **Seller roster note (updated 2026-06-17 per Cooper - 5-region territory migration):** The tracked-seller roster is now **five**: Tim Lieto (Northeast + West), Ken Cunningham (Southeast), Tory Teague (Central), Markus Hendrich (Europe), and Tim Ziemer (International + Tier 1 Service Provider). Markus Hendrich (`164949459`) now owns Europe (the earlier "unmapped" and "International, no formal territory yet" states are both retired). **Tory Teague now has a HubSpot owner record (`165480917`)** and is a full tracked seller everywhere this roster appears (filter list, bucket list, rep table, `rep_breakdown` JSON, checklist) plus a FOR YOU DM recipient. Group each seller under his region for brief display.

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

- **HubSpot MCP** - read calls, meetings, contacts, deals, tickets, companies; writes limited to (1) contact-level MEDDPICC and (2) the bounded Stage 5.7 Data Hygiene Auto-Fix (associations + unambiguous field corrections). No deal-level writes, no segment / tier / owner / enrichment writes, no engagement creates
- **Slack MCP** - `slack_send_message` (9 DMs - shared body + per-recipient FOR YOU; Hannah/Marketing is body-only), `slack_read_canvas` + `slack_update_canvas` (cross-routine ledger)
- **No Apollo, no web_search/web_fetch, no git.** Pure HubSpot-internal + Slack-out.

---

## Loud Failure Rule

Every run MUST end with at least one delivered exec DM (Cooper minimum), even on:
- Empty days ("0 sales meetings held in the last 24h - still posting brief for routine health monitoring")
- Fatal errors ("Routine aborted at Stage X")
- Partial runs (rate-limit retries exhausted, partial write completion)

Retry each DM 3× on send failure with exponential backoff (1s → 2s → 4s). If all nine recipients fail, append run summary to ledger canvas `F0B0AFSB9LN` so the run is still traceable.

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
- **LIMIT this fixes only partially:** the occurred-in-window query keys on `hs_timestamp` (event time). An engagement that is *logged* after a run fires but is *timestamped* in an already-closed window is invisible to this query forever (its event time is behind the next window's start). This is the residual dead zone that swallowed the 6/2 Voice Exchange call and the 6/9 Socket Fiber call. The **late-log catch-up window (check E)** closes it: detection there keys on `hs_createdate` (a monotonic field - logging always stamps it at log time), so nothing that gets logged can be missed. The occurred-in-window query stays as the PRIMARY held capture; check E is the safety net.

**Set window** - what got booked:
- Same calendar window as Held (`prior-run -> now`). See Stage 1B for the precise Set measurement rule (true bookings only, not auto call-logs).

**Upcoming window** - what's on the calendar:
- `upcoming_start_et` = run-time (now); `upcoming_end_et` = run-time + 7 days. Counts meetings/calls whose `hs_timestamp` falls in the next 7 days, regardless of when they were booked.

Convert all four endpoints to epoch ms for HubSpot timestamp filters.

E. **Late-log catch-up window** (the no-gap guardrail - added 2026-06-09 per Cooper). Compute one more window keyed on `hs_createdate` (when the object was logged), NOT event time:
- `logwindow_start_et` = `held_start_et` (same prior-run boundary as Held).
- `logwindow_end_et` = run-time (now).
- `lookback_floor_et` = now minus 14 days. This bounds how far back a late log's *event time* may sit before we treat it as an ancient backfill and ignore it.
This window powers Stage 1A.2 (the catch-up query) so an engagement logged in this window but timestamped earlier today (or any time in the last 14 days) is still surfaced as Held exactly once. Convert to epoch ms.

F. **Watermark continuity self-check** (gap detector - added 2026-06-09). Before querying, assert `held_start_et` equals the prior successful run's `held_end_et` (read from the prior weekday `activity-summary.json` -> `run_meta.held_window_et`, or from `lastRunAt`). If they do NOT match (a skipped/failed run left a hole), widen `held_start_et` and `logwindow_start_et` back to the prior run's end so the hole is back-filled, and note the widened span + reason in the audit. Never let a detected discontinuity pass silently. Record the resolved watermark (`held_start_et`, `held_end_et`) in `run_meta` at Stage 8.

G. **Load the seen-engagement ledger** (idempotency - added 2026-06-09). Read `weekly-reports/_state/seen-engagements.json` (a rolling 30-day record of engagement IDs already reported as Held). If absent, treat as empty (first run). This ledger is the dedup backstop for checks A/E so the 14-day catch-up lookback can be wide without ever double-reporting. See "Seen-engagement ledger" under Critical Invariants.

---

## Critical Invariants

### Timezone
America/New_York. Convert HubSpot UTC `hs_timestamp` and `hs_createdate` before filtering. Never use "this week" language in the brief - write "Last 24h" / "Last weekend" / "Next 7 days" / explicit ET dates.

### Write Scope (narrow - MEDDPICC contacts + bounded hygiene auto-fix)
Two HubSpot write paths, both narrow:
1. **MEDDPICC backfill** on the 6 contact-level MEDDPICC fields (see Stage 5 for exact names) on prospect CONTACTS from transcript evidence. Never write to deal-level MEDDPICC properties directly - the contact-level fields SYNC UP to the deal-level MEDDPICC fields automatically, and direct deal-level writes are blocked by HubSpot's calculated-property restriction.
2. **Data Hygiene Auto-Fix** (Stage 5.7, added 2026-06-16 per Cooper) - a bounded, deterministic, reversible allowlist: contact-to-company / engagement-to-company associations and unambiguous field corrections where the correct value is already present in HubSpot. Cap 10 fixes/run.

STILL FORBIDDEN on every path: no `customer_segment` / `company_sub_segment` / `account_tier` / enriched-field / `account_brief` writes (enrichment is owned by R1 / R2 / R10), no `hubspot_owner_id` / territory reassignment (owned by R6), no deal-stage changes, no company / contact / engagement creation, no dedup merges (owned by R3 / R5), no notes / tasks / activities. When unsure whether a fix is in-scope, DON'T write - defer to the owning routine per Stage 5.7. The MEDDPICC policy is otherwise unchanged from the prior Daily Call Recap routine - see "MEDDPICC Backfill + Refresh Policy" below.

### Seen-engagement ledger (idempotency - added 2026-06-09)

Single on-disk file at `weekly-reports/_state/seen-engagements.json`, shared across runs (NOT per-date). Schema: `{"reported": [{"id": "<hs_object_id of the canonical clustered engagement>", "first_reported": "YYYY-MM-DD", "hs_timestamp": "<ISO>", "pool": "held"}], "trimmed_before": "YYYY-MM-DD"}`. Purpose: guarantee every held engagement is reported in the brief EXACTLY ONCE even though the late-log catch-up (check E) re-scans a 14-day lookback every run.

Rules:
- Load at preflight (check G). After Stage 2 dedup/clustering, drop any held candidate whose canonical `hs_object_id` is already in `reported` - it was surfaced on a prior run; do not re-report.
- A held engagement that survives the ledger filter via the late-log catch-up path (check E - it occurred before this window but was only just logged) is surfaced normally but TAGGED `[late log]` in its account header and headline, so founders read it as a catch-up, not a same-day call. Bucket it under the day it is reported.
- At Stage 8, append every newly-reported held engagement's canonical ID to `reported`. Trim entries with `hs_timestamp` older than 30 days (keeps the file bounded; 30d > the 14d catch-up lookback so no entry is trimmed while still re-scannable).
- Set + Upcoming are NOT ledgered (they key on `hs_createdate` / future `hs_timestamp`, both monotonic - no gap to guard). The ledger covers Held only. A book-and-hold engagement still counts in both Set (createdate path) and Held (once, via the ledger) - the legitimate overlap is preserved.
- The ledger is the reason the catch-up lookback can be a generous 14 days: re-scans are free because anything already reported is filtered out here.

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

### 1A. Held - calls + meetings (DUAL-KEY: occurred-in-window + late-log catch-up)

Held is detected TWO ways and unioned, then deduped (Stage 2) and filtered against the seen-engagement ledger. This dual-key design is the no-gap guardrail (added 2026-06-09): query A keys on event time, query A.2 keys on log time, so an engagement is caught whether it occurred in the window OR was logged late for a past meeting.

**1A.1 - Occurred-in-window (PRIMARY).** `search_crm_objects` on CALL with `hs_timestamp` GTE/LTE the held window epochs.
Properties: `hs_call_title`, `hs_call_summary`, `hs_call_body`, `hs_call_has_transcript`, `hs_call_recording_url`, `hs_call_direction`, `hs_call_duration`, `hs_call_status`, `hs_call_disposition`, `hs_timestamp`, `hs_createdate`, `hubspot_owner_id`. Associations: `["COMPANY", "CONTACT", "DEAL", "TICKET"]`. Limit 100. Paginate.

Repeat for MEETING engagement objects in the same window (HubSpot's separate object for scheduled meetings). Some HubSpot accounts log meetings as CALL objects with `hs_call_source = "HUBSPOT_MEETINGS"`; in this org, the data we've seen does ride on the CALL object, but query MEETING too as a safety net.

**1A.2 - Late-log catch-up (SAFETY NET - the gap closer).** Run the SAME CALL + MEETING queries with the same property/association set, but filter on `hs_createdate` BETWEEN `logwindow_start_et` and `logwindow_end_et` (the log window from Preflight check E) AND `hs_timestamp` GTE `lookback_floor_et` (now - 14d) AND `hs_timestamp` LTE now. This returns engagements that were *logged this window* for a meeting that *already happened* (today before the prior boundary, or any time in the last 14 days) - exactly the records query 1A.1 cannot see. Union these into the held candidate set. Each catch-up record that survives clustering + the seen-ledger filter is surfaced as Held and TAGGED `[late log]` (see the seen-engagement ledger invariant). This is what reliably picks up a call like Socket Fiber held today but logged after the run fires.

Note: many 1A.2 hits will be duplicates of 1A.1 (a same-day book-and-hold whose createdate and timestamp both fall in the window) - the Stage 2 dedup + the seen-ledger collapse these so nothing double-reports.

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

**Why Set has no time gap (and Held needs the catch-up but Set does not).** Set keys on `hs_createdate`, which is monotonic - the moment a rep books a meeting on a HubSpot-connected calendar, the MEETING object is created and stamped, so a `createdate`-in-window query can never miss a booking made in the window. This is the "based on them setting meetings on their calendar" signal Cooper asked for, and it is reliable AS LONG AS the rep's calendar is connected with auto-log on (verified by the calendar-connection health check, Stage 2.6). The Held pool needed the dual-key fix because it keys on event time; Set does not, because booking time and create time coincide. Set is NOT run through the seen-engagement ledger (createdate is already a clean per-run boundary). If a future meeting that was counted as Set later gets rescheduled or canceled, that surfaces through the calendar-movement diff (Stage 2.5), not as a re-count.

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

### Apply the seen-engagement ledger (Held only - idempotency guardrail)
After the Held pool is deduped/clustered into canonical engagements, drop any whose canonical `hs_object_id` is already in the loaded ledger's `reported` list (it was surfaced on a prior run). For each surviving held engagement that came in via the late-log catch-up path (1A.2 - createdate in window but `hs_timestamp` before `held_start_et`), set `late_log = true` so Stage 6 renders the `[late log]` tag. Engagements caught by 1A.1 (occurred in this window) are normal same-day held calls. Set + Upcoming pools are NOT ledger-filtered.

### Filter to tracked reps ONLY

The brief tracks activity for **Tim Lieto, Ken Cunningham, Tory Teague, Markus Hendrich, and Tim Ziemer only**. Drop every engagement in all three pools whose `hubspot_owner_id` is not one of the tracked-seller IDs below before bucketing. Engagements owned by anyone else (Abilash, Cooper, Kyle, Woody, unmapped, etc.) get logged to the audit section only - they do not appear in the brief table or the Held Calls snapshot, and their associated contacts are NOT processed for MEDDPICC backfill in Stage 5.

### Bucket by rep
Group the surviving engagements by `hubspot_owner_id` (region labels per the 5-region model that went live 2026-06-17):
- Northeast + West - `161889085` Tim Lieto
- Southeast - `162339176` Ken Cunningham
- Central - `165480917` Tory Teague
- Europe - `164949459` Markus Hendrich
- International + Tier 1 Service Provider - `159350430` Tim Ziemer

Any tracked seller without activity in any of the three pools still appears in the brief table with a `0 / 0 / 0` row - silence is itself a signal.

### Classify each engagement as FRESH or DEAL

For every Held and Set engagement that survives the rep filter, walk its associated DEAL records (already hydrated in Stage 1).

- **FRESH** - no associated deals at all, OR every associated deal has `hs_is_closed_won = true` OR `hs_is_closed_lost = true`. Treat closed-won and closed-lost deals as historical, not active. (Fresh means there is no live opportunity attached; the meeting is either prospecting, customer expansion conversation pre-deal, partner exploration, or an account that hasn't converted yet.)
- **DEAL** - at least one associated deal is open (neither closed-won nor closed-lost). Capture the largest open deal `amount` and `dealstage` for the brief tag.

Tie-break: if an engagement has BOTH closed and open deals associated, it counts as DEAL (the open one wins). Persist the classification on the engagement record for use in Stage 6.

**Set board terminology (added 2026-06-16 per Cooper - the brief breaks Set out into these two explicitly):**
- **Fresh-set (`SetF`)** = a newly-booked meeting classified FRESH (the account has NO open deal) - a new-logo / top-of-funnel prospecting booking.
- **Deal-advancing set (`SetD`)** = a newly-booked meeting classified DEAL (the account HAS an open deal) - a booking that advances existing pipeline.
Tally `set_fresh` / `set_deal` per rep AND in total; both render in Stage 6 (the per-rep SetF / SetD columns in the ACTIVITY BY REP table + the Pipeline Mix Set row). Held uses the same FRESH / DEAL split but is not relabeled SetF / SetD.

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

### Stage 2.6: Calendar-connection / auto-log health check (-> Cooper FOR YOU; added 2026-06-09 per Cooper)

The dual-key Held detection and createdate-keyed Set both assume the engagement EXISTS as a HubSpot object. They cannot see a meeting that a rep's calendar never synced (the root cause of the 6/9 Socket Fiber miss - the call simply never became a CALL/MEETING object). This check watches for a silently broken or disconnected calendar before it costs more calls. It writes nothing to HubSpot; output goes to Cooper's FOR YOU only.

Per tracked seller, count the calendar-sourced objects they produced in a trailing 7-day window (`hs_createdate` GTE now-7d): MEETING objects + CALL objects with `hs_call_source = "HUBSPOT_MEETINGS"` owned by that rep. (Use the data already pulled this run plus, if needed, one lightweight `search_crm_objects` count per object type filtered by `hubspot_owner_id` + `hs_createdate`.)

Flag a rep to Cooper when EITHER:
- **Zero** calendar-sourced objects in the trailing 7 days AND the rep is otherwise active (has any deal, any contact touch, or appeared in a prior brief) - a strong signal their calendar sync dropped or auto-log is off; OR
- A held call surfaced THIS run only via the late-log catch-up path (1A.2) with `hs_call_source != "HUBSPOT_MEETINGS"` and no MEETING twin - i.e. it was hand-logged, not calendar-sourced - which means the calendar did not capture a real meeting (the Socket pattern). Name the rep + account.

Both states route a single line to Cooper's FOR YOU (audience tag `cooper`): e.g. `Calendar-sync watch: Tim Lieto produced 0 calendar-sourced meetings in 7d - verify his HubSpot calendar connection / auto-log.` or `Socket Fiber (Tim Lieto) was hand-logged, not calendar-sourced - if his calendar were syncing this meeting would have auto-created; spot-check the connection.` If all reps are healthy, emit nothing (no FOR YOU noise on a clean run). Detail every rep's 7-day count in `cooper-audit.md`.

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

## Stage 5.7: Data Hygiene Auto-Fix (silent; added 2026-06-16 per Cooper)

Cooper's directive: when this routine spots a data-hygiene problem on an account or contact that hits the brief, **fix it silently instead of telling Cooper** - but only within a bounded, deterministic, reversible allowlist that does NOT step on the routines that own enrichment, tiering, and territory. The brief is HubSpot-internal only (no web, no Apollo), so it can only fix what is unambiguous from data already in HubSpot. Every hygiene issue found this run gets ONE of three dispositions:

**1. AUTO-FIX** (do it silently; log to `cooper-audit.md`; do NOT put in any FOR YOU). Allowed fixes - deterministic, reversible, HubSpot-internal, correct value unambiguous from existing data:
- **AF1 - Orphan contact -> company association.** A prospect contact surfaced this run (held or upcoming) with NO associated company, whose email domain matches **exactly one** existing company record (exact domain match on a business domain), gets associated to that company. This is the recurring NTT / Verizon / Scott-Lawrence pattern. Guardrails: skip free / public email domains (gmail.com, outlook.com, yahoo.com, hotmail.com, icloud.com, proton.me, gmx.*, web.de, etc.); if 0 companies match the domain, do NOT create one (enrichment owns net-new companies) - note in audit; if 2+ companies match (a duplicate pair), do NOT guess - note in audit (Routine 3 owns dedup).
- **AF2 - Engagement -> company association gap.** A held engagement whose external contacts all sit at one obvious company, but the engagement itself is not associated to that company, gets associated. Only when the company is unambiguous (one company across all the engagement's external contacts).
- **AF3 - Obvious malformed-field correction** where the correct value is unambiguous from associated records already in HubSpot (e.g. a stray whitespace / case mismatch blocking an otherwise-exact contact-to-company domain match). Conservative: only when there is a single unambiguous correct value already present in HubSpot. No inference, no web lookup.
Auto-fix writes go through `manage_crm_objects` with `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`, same retry / backoff as MEDDPICC. Cap 10 fixes/run (a higher count signals a systemic issue -> note + escalate, do not mass-write from a 6pm brief). Record every auto-fix in the `cooper-audit.md` Data Hygiene table (what, the record IDs, before/after, why it was unambiguous).

**2. DEFER to the owning routine** (silently; note in audit; do NOT surface to Cooper). Anything needing research / enrichment or territory logic is already caught by the routine that owns it - flagging Cooper is the redundant noise he asked to stop:
- Blank / `Unknown` `customer_segment`, missing `company_sub_segment`, missing `account_tier`, missing enriched fields, missing `account_brief` -> **R1 Fresh Enrichment / R2 Stale Re-Enrichment / R10 Completeness Sweep** own these via their triggers. A blank-segment company is already an R1 Filter-Group-A candidate; it WILL be picked up. Do not enrich here (no web / Apollo) and do not DM Cooper.
- Wrong `hubspot_owner_id` vs HQ state / territory model (e.g. an international account owned by an East rep) -> **R6 Territory & Hygiene** owns owner re-derive with the full territory model. Do not reassign owners from this brief and do not DM Cooper.
- Duplicate company / contact pairs -> **R3 Duplicate Accounts / R5 Contact Dedup** own these. Do not merge here; do not DM Cooper.
Just record "deferred to <routine>" in the audit so the trail exists.

**3. ESCALATE to Cooper's FOR YOU** (only the genuine residue). Surface to Cooper ONLY when an issue is (a) NOT safely auto-fixable here, AND (b) NOT owned by any other routine, AND (c) materially affects the brief's accuracy or a live deal. This should be rare. Operational (non-"data") flags are unchanged and still route normally: the Stage 2.6 calendar-sync / auto-log health flags, watermark-discontinuity notices, Stage 5 write failures / Tier-3 holds, and "a meeting reached its slot with no completion notes logged" (a behavioral logging gap, not a data-hygiene fix) all still go to Cooper / the relevant recipient as before.

Net effect Cooper asked for: hygiene this routine can fix, it fixes; hygiene another routine owns, it lets that routine handle (no DM); only true orphans reach Cooper. The full auto-fix + defer log lives in `cooper-audit.md`.

---

## Stage 6: Compose the Exec Brief

The brief lives entirely in the parent Slack message body. No threaded follow-ups. No external links. ~3,500-4,000 chars max so all nine recipients see one screenful.

### Slack formatting rules - read carefully, the brief renders or fails on these

- Slack mrkdwn uses **single asterisks** for bold (`*bold*`), single underscores for italic (`_italic_`), single backticks for inline code, triple backticks for code blocks. Markdown-style `**bold**` does NOT render in raw Slack mrkdwn - it shows as literal asterisks. **Connector caveat (2026-06-16):** the live Slack MCP in this project accepts STANDARD markdown (`**bold**` + fenced code blocks) and converts to mrkdwn server-side - prior + current runs delivered cleanly that way. Match whatever the connected Slack tool actually expects; the goal is a clean-rendering brief, not a specific syntax. Tables ALWAYS go in fenced code blocks either way.
- **All tabular data goes in triple-backtick code blocks** so columns align in monospace. Pipe-separated markdown tables render as ugly literal pipes in Slack and are forbidden in this brief.
- Use ` · ` (middle dot, U+00B7) as inline separator on account header lines. NO em dashes anywhere.
- Bullets: leading `• ` (U+2022 + space). Slack does not render `*` or `-` bullets the way Markdown does.
- Use `>` at line start for blockquotes - Slack honors this and indents the line, which is how the per-call snapshot details render cleanly.
- Emojis are fine and welcome at section markers (one per section max - don't sprinkle).

### Brief Structure (shared body - same for all 9 recipients)

```
🎯 *Daily Sales Activity · [Day], [MM/DD/YYYY]*
_Held: [held_start MM/DD HH:MM] → [held_end MM/DD HH:MM] ET · Set: same window · Upcoming: next 7 days_

*HEADLINE*
[1-2 sentences. Lead with the trend signal if it diverges from baseline; otherwise lead with the most notable trajectory event of the day. Examples: "Heavy deal-day · 3 of 4 held calls on open deals (vs 5d avg 1.8 · UP). Pearce SOW tomorrow, RocNet on track 5/15. Sungard AT-RISK on EB churn." OR "Prospecting-heavy · 3 fresh-logo intros (vs 5d avg 1.0 · UP), 1 deal call. Telxius LATAM the standout." OR "Quiet day · 0 held calls (vs 5d avg 2.4 · DOWN). 9 meetings on calendar next 7d." NO MEDDPICC mentions.]

*ACTIVITY BY REP*
` ` ` (triple backtick - open code block)
              SetF  SetD  Held  Up7d
Tim Lieto      3     0     2     4
Ken C          1     1     1     3
Tory T         1     0     1     2
Markus H       1     0     0     1
Tim Z          1     0     1     2
─────────────────────────────
TOTAL          7     1     5     12
` ` ` (triple backtick - close code block)

_SetF = fresh-set (new booking, no open deal). SetD = deal-advancing set (new booking on an open-deal account). Held + Up7d count engagements regardless of deal state._

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
[Append ` · ` + "`[late log]`" to the account header when the engagement was caught via the late-log catch-up path (1A.2) - tells the reader this is a catch-up from a prior day, not a same-day call.]
[Headline sentence - 90-second-reader takeaway. If `[late log]`, lead with the actual call date, e.g. "Logged today, held 6/9 -".]
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

Every attention item identified during the run gets tagged with a target audience based on what it requires. Then per recipient, filter to that recipient's items + any tagged `all`. Skip the section entirely for a recipient if they have 0 items. **Hannah Roberts (Marketing) is excluded from FOR YOU routing entirely - she always gets body only.**

**Audience rules:**

- **`tim_z`** (CRO - runs the sales team) - gets: AT-RISK / STALLING flags on any deal, exec-to-exec intro asks where Tim Z is the named asker, rep load imbalances or inactivity flags, key meetings on his own calendar that need prep, MEDDPICC drift severe enough to threaten a deal (rare - only when Stage 5 logs a Tier 2 DRIFT on a deal at proposal/contract stage).
- **`abilash`** (CEO) - gets: Tier 1 logo intros booked or held, escalations where CEO involvement could change a deal's trajectory, customer expansion opportunities surfaced in held calls, anything strategic that maps to board/investor narrative.
- **`cooper`** (RevOps) - gets: routine health flags (Stage 5 write failures, MCP timeouts, DM delivery retries), trend baseline status (BASELINE BUILDING countdown), any Tier 3 holds that need human review, **calendar-connection / auto-log watch flags from Stage 2.6** (a rep producing zero calendar-sourced objects in 7d, or a held call that was hand-logged rather than calendar-sourced - the Socket Fiber pattern), and **watermark discontinuity notices** (a skipped/failed prior run forced a widened catch-up span). **Data-hygiene items are NO LONGER routed here as action items (per Cooper 2026-06-16):** Stage 5.7 auto-fixes what it safely can and defers the rest to the owning routine (R1 / R2 / R6 / R3 / R5); the full auto-fix + defer log lives in `cooper-audit.md`, not in this FOR YOU. Escalate a hygiene item to Cooper's FOR YOU ONLY when it is not auto-fixable here AND not owned by any routine AND it affects brief accuracy or a live deal.
- **`tim_lieto`** (rep - Northeast + West, owner `161889085`) - gets ONLY items on engagements HE owns: AT-RISK / STALLING flags on his deals, his upcoming Tier 1-2 meetings that need prep, NEW/PUSHED/DROPPED calendar movement on his accounts, his Tier 3 MEDDPICC holds. Filter every candidate item to `hubspot_owner_id = 161889085`. Do NOT show him other reps' deal flags in FOR YOU (he still sees the full team totals in the shared ACTIVITY BY REP table).
- **`ken_cunningham`** (rep - Southeast, owner `162339176`) - same as Tim Lieto but filtered to `hubspot_owner_id = 162339176`.
- **`tory`** (rep - Central, owner `165480917`) - same as Tim Lieto but filtered to `hubspot_owner_id = 165480917`.
- **`markus`** (rep - Europe, owner `164949459`) - same as Tim Lieto but filtered to `hubspot_owner_id = 164949459`.
- **`pt`** (POC lead, Patrick Timmons) - gets POC-scoped items across ALL reps (not a single book of business). An item is in PT's bucket if the underlying account has an associated POC ticket (per `poc-schema.md`) OR the held/upcoming engagement is POC-related: held calls on accounts with an open POC, POC status changes surfaced during a call, upcoming meetings on POC accounts that need POC prep, and any deal AT-RISK/STALLING flag where a POC is the gating activity. Lead each item with the account + POC status + what PT needs to do. Ignore prospecting/fresh-logo items with no POC attached.
- **`all`** - genuinely cross-cutting items that all action-taking recipients should see. Use sparingly. Example: a Tier 1 logo just went `closedwon` mid-call (everyone wants to know). (Hannah/Marketing still gets body only - `all` items do not add a FOR YOU section to her DM.)
- **`hannah`** (Marketing) - NO FOR YOU, ever. Hannah receives the shared body only (Headline, Activity by Rep, Pipeline Mix / Set board, Next 7 Days, Held Calls): the day's activity view, not action items.

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
              SetF  SetD  Held  Up7d
Tim Lieto      X     X     0     Z
Ken C          X     X     0     Z
Tory T         X     X     0     Z
Markus H       X     X     0     Z
Tim Z          X     X     0     Z
─────────────────────────────
TOTAL          X     X     0     Z
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

Compose 9 DM bodies. Hannah Roberts (Marketing) always gets the shared body with NO FOR YOU block. Bodies share the entire shared brief structure (Headline → Activity by Rep → Pipeline Mix → Next 7 Days → Held Calls). Then per recipient, append their tailored `FOR YOU · [Name]` block (skip the section entirely if 0 items routed to them).

Send in sequence:
1. `slack_send_message` to `U06RVK9NTQR` (Abilash) - body + Abilash's FOR YOU
2. `slack_send_message` to `U08CMD5PMQE` (Tim Z) - body + Tim Z's FOR YOU
3. `slack_send_message` to `U0A24D9RJLS` (Cooper) - body + Cooper's FOR YOU
4. `slack_send_message` to `U0A973L1HFF` (Tim Lieto) - body + Tim Lieto's FOR YOU (his owned engagements only)
5. `slack_send_message` to `U0AE1PGCB6C` (Ken Cunningham) - body + Ken's FOR YOU (his owned engagements only)
6. `slack_send_message` to `U0B7MU3P3QD` (Tory Teague) - body + Tory's FOR YOU (his owned engagements only)
7. `slack_send_message` to `U0B6B4U8QKD` (Markus Hendrich) - body + Markus's FOR YOU (his owned engagements only)
8. `slack_send_message` to `U06RVKNTRPB` (Patrick Timmons / "pt") - body + PT's POC-scoped FOR YOU
9. `slack_send_message` to `U09BYB61FCN` (Hannah Roberts / Marketing) - body ONLY, no FOR YOU

≥1s between each send. Capture each message link for the audit. The shared body section is byte-identical across all nine messages so Cooper's audit can verify drift if any of the FOR YOU routing logic misfires.

If any DM fails: retry with exponential backoff 1s → 2s → 4s. If all 3 attempts on a given recipient fail, skip that recipient and continue. After all 9 are attempted, if even one succeeded → mark run YELLOW and log in audit. If ALL 9 failed → fall back to writing run summary into the cross-routine ledger canvas `F0B0AFSB9LN`.

---

## Stage 8: Markdown Audit (local archive only)

Write to `weekly-reports/YYYY-MM-DD/calls/`:
- `daily-brief.md` - the exact brief body that was sent (so Cooper can see what shipped)
- `all-calls.md` - every held call's full Mode 1 record concatenated, chronological. Each entry tagged FRESH or DEAL with associated deal IDs/amounts/stages.
- `cooper-audit.md` - MEDDPICC FILLED / REFRESHED / DRIFT / HELD tables (the founder-invisible writes), a **Data Hygiene table** (Stage 5.7 auto-fixes with record IDs + before/after + why-unambiguous, plus the "deferred to <routine>" log), errors, trajectory roll-up, per-rep activity numbers, fresh-vs-deal classification log per engagement (held + set, with the SetF / SetD split), calendar movement log (PUSHED / PULLED IN / NEW / DROPPED with full context), and the per-recipient FOR YOU routing decision log so Cooper can audit which items went to whom and why.
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
      "tory_teague": {"set": N, "held": N, "upcoming": N},
      "markus_hendrich": {"set": N, "held": N, "upcoming": N},
      "tim_ziemer": {"set": N, "held": N, "upcoming": N}
    }
  }
  ```

Also update the shared-state file (NOT under the per-date folder):
- `weekly-reports/_state/seen-engagements.json` - append every held engagement reported THIS run (canonical `hs_object_id`, `first_reported = today`, `hs_timestamp`, `pool: "held"`). Trim entries whose `hs_timestamp` is older than 30 days. This is the idempotency backstop for the 14-day late-log catch-up; without writing it, tomorrow's catch-up re-scan would re-report today's calls.
- In `activity-summary.json` `run_meta`, record the resolved watermark this run used: `held_window_et` (start -> end) and `logwindow_et` (the catch-up window), plus a `watermark_continuous` boolean and, if it was false, the widened span + reason. This is what the next run's Stage-F continuity check reads.

ATX-style headings. NO em dashes. **No git operations.** Files live on disk only.

---

## Stage 9: Cross-routine Ledger

- **At run start:** read canvas `F0B0AFSB9LN`. Drain Tier 3 items belonging to this routine.
- **At run end:** append NEW Tier 3 holds with `[YYYY-MM-DD]`. Append ONE row to "Run log": `| YYYY-MM-DD HH:MM ET | Daily Sales Activity Brief | <emoji> | <summary> | <link to Cooper's DM> |`. Trim entries older than 90 days.
- **Oversized-canvas degraded path (2026-06-16):** if `slack_read_canvas` returns an oversized payload (this canvas has run >1M chars) and the Run-log section_id cannot be obtained for a targeted append, do NOT blind-append to the shared canvas (corruption risk). With 0 Tier 3 holds nothing accumulates; record the intended Run-log row in `cooper-audit.md` and continue. The delivered DMs + on-disk audit remain the audit trail of record.

---

## Failure Modes

- Per-record try/except on every read, association hydration, summary parse.
- HubSpot MCP unreachable → write `cooper-run-report.md` blocker, post Cooper-only DM (skip Abilash, Tim Z, Tim Lieto, Ken, Tory, Markus, PT, and Hannah if HubSpot dead - they'd get a useless brief), exit cleanly.
- Slack MCP unreachable → write all markdown to disk, write run summary to ledger canvas if canvas write still works, exit.
- 429: pause 10s, retry. 3 consecutive 429s on same op → skip op, log to audit.
- Empty day → still send all 9 DMs with empty-day variant (Hannah included, body-only).
- Heavy day (rare on daily cadence - would need 15+ external held calls) → trim per-call paragraphs to 4 lines, brief still fits in one message.

---

## Final Checklist

- [ ] Today is a weekday (Mon-Fri); aborted cleanly if not
- [ ] Held window = rolling `prior-run -> now` (gapless); fallbacks applied if `lastRunAt` is missing (24h/72h) or stale >30h (widen to cover the gap)
- [ ] DUAL-KEY Held detection run: 1A.1 occurred-in-window (`hs_timestamp`) UNION 1A.2 late-log catch-up (`hs_createdate` in window AND `hs_timestamp` within last 14d); unioned then deduped
- [ ] Watermark continuity self-check (F) run: `held_start` == prior run's `held_end`; widened + audit-noted if a skipped run left a hole
- [ ] Seen-engagement ledger loaded at preflight, applied to Held candidates after clustering (no re-report), and written back at Stage 8 with 30-day trim
- [ ] Late-log catch-up held calls tagged `[late log]` in their account header + headline
- [ ] Calendar-connection / auto-log health check (Stage 2.6) run; any zero-calendar-sourced rep or hand-logged-not-calendar-sourced held call routed to Cooper's FOR YOU; all-healthy = no flag
- [ ] Set window matches Held window (`prior-run -> now`); Set measured on true bookings per Stage 1B (NOT auto call-log twins); Set NOT ledger-filtered (createdate is monotonic)
- [ ] Upcoming window = next 7 days from run-time
- [ ] Internal-Only Filter applied permissively (only obvious internals dropped)
- [ ] Skip rules applied within external set
- [ ] Every held call has the 5-line exec block (Headline / Use Cases / Pain / Trajectory / Next) - NO MEDDPICC line in the brief
- [ ] Each held call carries a `[FRESH]` or `[DEAL · $XXk · stage]` tag in its account header
- [ ] Activity-by-Rep and Pipeline Mix tables rendered in triple-backtick code blocks (NOT pipe-separated markdown tables)
- [ ] Slack mrkdwn used throughout: single asterisks for bold, single underscores for italic, `• ` bullets, `>` blockquotes, ` · ` middle-dot inline separator
- [ ] Pipeline Mix table renders with today's Held + Set splits and trend tags (UP/DOWN/FLAT/BASELINE BUILDING)
- [ ] Set broken out into SetF (fresh-set) and SetD (deal-advancing set) in the ACTIVITY BY REP table + legend; Pipeline Mix Set row uses the same fresh / deal-advancing split
- [ ] Per-rep activity table includes ONLY Tim Lieto, Ken Cunningham, Tory Teague, Markus Hendrich, Tim Ziemer (zeros allowed for any tracked seller with no activity)
- [ ] Engagements owned by anyone outside the tracked sellers were filtered out before bucketing and surface in audit only
- [ ] FRESH vs DEAL classification applied to all Held + Set engagements per the Stage 2 rule
- [ ] Trailing 5-weekday baseline computed from prior `activity-summary.json` files; trend marked BASELINE BUILDING if fewer than 3 prior runs on disk
- [ ] `activity-summary.json` AND `upcoming-snapshot.json` written for today so tomorrow's run has baseline + movement data
- [ ] Calendar movement section (NEXT 7 DAYS) emitted only if at least one PUSHED/PULLED IN/NEW/DROPPED detected; otherwise omitted entirely
- [ ] Each movement item ranked by tier impact (Tier 1-2 first), capped at 5 in the brief
- [ ] Per-recipient FOR YOU sections composed separately for Abilash / Tim Z / Cooper / Tim Lieto / Ken Cunningham / Tory Teague / Markus Hendrich / Patrick Timmons using audience routing rules (reps filtered to their own owned engagements; PT filtered to POC-attached accounts across all reps)
- [ ] FOR YOU section omitted entirely from a recipient's DM if 0 items routed to them
- [ ] FOR YOU capped at 4 items per recipient; overflow indicated with `+ N more in cooper-audit.md` line
- [ ] MEDDPICC policy still applied silently (Tier 1 fills/refreshes, Tier 2 DRIFT, Tier 3 holds, closed deals skipped) - writes land in HubSpot, NOT in the brief
- [ ] Headline does not mention MEDDPICC, drift, or any audit-only metric
- [ ] Lifetime call count computed and used to gate refresh vs. drift
- [ ] Material-update guard honored on refreshes
- [ ] No HubSpot writes outside contact-level MEDDPICC + the bounded Stage 5.7 hygiene auto-fixes (associations + unambiguous corrections; cap 10/run)
- [ ] Stage 5.7 Data Hygiene Auto-Fix ran: deterministic in-scope fixes applied silently, enrichment/territory/dedup deferred to the owning routine (no Cooper DM), only true residue escalated to Cooper; full log in `cooper-audit.md`
- [ ] No em dashes
- [ ] No competitor product names
- [ ] MSP shown as "MSP / Aggregator"
- [ ] All dates ET
- [ ] Markdown audit + `upcoming-snapshot.json` + `activity-summary.json` written to `weekly-reports/YYYY-MM-DD/calls/` (no git operations)
- [ ] `weekly-reports/_state/seen-engagements.json` updated with this run's reported held IDs (30-day trim); resolved watermark recorded in `run_meta`
- [ ] 9 DMs sent to Abilash + Tim Z + Cooper + Tim Lieto + Ken Cunningham + Tory Teague + Markus Hendrich + Patrick Timmons + Hannah Roberts (shared body byte-identical; FOR YOU unique per action-taking recipient; Hannah body-only with NO FOR YOU - each with retry logic)
- [ ] Cross-routine ledger row appended