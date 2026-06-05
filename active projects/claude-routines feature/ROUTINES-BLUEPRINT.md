# MaiaEdge Routines Blueprint

A complete implementation guide for setting up Claude Code Routines against the MaiaEdge AI repo. Hand this file to Claude Code and say: "Set up these routines using this blueprint."

---

## What Are Routines?

Routines are a Claude Code feature that lets you configure a prompt + a trigger (schedule, API endpoint, or GitHub webhook) and Claude Code runs it autonomously. No cron jobs, no infra management. Three trigger types:

- **Scheduled**: Runs on a cadence (hourly, nightly, weekly)
- **API**: Gets its own authenticated endpoint -- POST to trigger, returns a session URL
- **Webhook (GitHub)**: Fires on repo events (PR opened, push to branch, etc.)

Limits: Pro = 5/day, Max = 15/day, Team/Enterprise = 25/day.

---

## Summary: All Recommended Routines

### Scheduled Routines

**1. CRM Guardian -- Nightly at 2 AM ET**
A single daily master cycle that runs up to 7 maintenance jobs against HubSpot. Every day: hygiene, new-account enrichment + re-enrichment, territory validation, and pre-deletion audit with contact consolidation. Plus: persona gap fill (Fridays), prospect sourcing (1st of month), and contact job-change detection (quarterly). Before any account gets flagged `customer_segment = "Flagged for deletion"`, the pre-deletion audit checks for duplicates of ICP primaries (reassociates contacts), preserves any contact with activity in the last 90 days or an open deal, and writes `flagged_for_deletion = true` only on truly dormant contacts. Uses a 3-tier safety system -- low-risk fixes happen automatically, medium-risk fixes are applied but flagged for Cooper's review, and high-risk changes (open-deal accounts, MEDIUM-confidence dedup matches, any archive decision) are held for human approval. This is the single highest-impact routine because it prevents data rot from compounding day over day and makes the CRM self-managing.

**2. Pipeline Monday Brief -- Weekly, Monday at 7 AM ET**
Generates the 3-column conversion board that tracks every account through the full revenue lifecycle: accounts converting to POC, POCs converting to purchase orders, and initial orders expanding. Each account shows the rep owner, deal stage, days in stage, last activity date, POC health score (for Column 2), and a recommended next action. The brief lands before Monday standup so Tim Z, Tim L, and Ken walk in knowing exactly what needs attention -- no one has to pull it live.

**3. Stale Deal Watchdog -- Nightly at 6 AM ET**
Scans every open deal for staleness signals: time in current stage exceeding thresholds (14 days early-stage, 30 days mid-pipeline, 45 days late-stage), no activity in 14+ days, close dates that have already passed, and MEDDPICC qualification gaps on deals past discovery. Only alerts on deals that crossed a new threshold in the last 24 hours so reps don't get alert fatigue. The goal is to catch deals that are quietly dying before they go fully cold -- a deal with no activity for 3 weeks is salvageable, but 6 weeks is usually not.

**4. Weekly Call Digest -- Friday at 4 PM ET**
Pulls every call logged in HubSpot over the past 7 days, extracts the AI-generated summaries, and classifies each call against our 21-use-case taxonomy. The output is a formatted HTML report showing: which use cases came up most often (and with real quotes), recurring pain points by segment, every competitive mention (who was named, in what context), and rep activity stats. This turns raw call data into systematic market intelligence -- instead of insights living in individual reps' heads, the whole team sees what's resonating and what's blocking.

**5. Territory Drift Check -- Weekly, Sunday at 9 PM ET**
Audits all company records created or modified in the past week to verify territory assignments match the HQ state-to-owner mapping (Tim Lieto = East 30 states, Ken Cunningham = West 20 states + DC, Tim Ziemer = International). Also catches US companies with blank state fields and accounts still sitting under Cooper's placeholder ownership that need routing. This is an audit-only routine -- it produces a correction list for Cooper to review rather than auto-fixing, since territory exceptions sometimes exist for strategic reasons.

### Webhook Routines (GitHub)

**6. Repo Build Validator -- On PR to main**
When anyone opens a pull request against the main branch, this routine runs build.sh and verifies that all 9 plugins, 5 standalone skill zips, and 7 enterprise project uploads assemble cleanly. It checks that the skill counts inside each plugin zip match the plugin-manifest.json declarations and that no enterprise upload folder is empty. If anything breaks, it comments directly on the PR with the specific failure. This is an insurance policy -- as the knowledge base grows past 25 skills and 49 context files, a bad merge in one file can silently break downstream builds.

**7. Context Drift Detector -- On PR touching context/**
When a PR modifies files in the context/ directory (territory model, HubSpot schemas, segment cheatsheets, etc.), this routine cross-references every skill that references the changed file and checks whether any hardcoded values in those skills are now stale. For example, if someone updates territory-model.md to reassign a state, the territory-manager skill's hardcoded state list would need updating too. Most skills read context dynamically at runtime so drift is rare, but catching the exceptions automatically prevents subtle bugs.

### API Routines (On-Demand)

**8. Enrichment Chain -- POST to trigger**
After running a company-enrichment batch, today you manually kick off import-processor to transform the output into HubSpot format, then manually run edge-case-researcher on the flagged accounts. This routine chains those two steps automatically: POST the enrichment output file path, and it runs import processing (value transforms, qualified/excluded separation), then deep-dive research on edge cases, then merges recovered accounts back into the final qualified import file. Eliminates the manual handoff between three skills and produces a single HubSpot-ready file.

---

## Routine 1: CRM Guardian (Nightly)

**Why this is #1 priority:** The crm-guardian skill defines 7 maintenance jobs with a 3-tier safety system and a single daily master cycle. Today it only runs when manually invoked. Making it nightly means data rot gets caught within 24 hours instead of whenever someone remembers, and new accounts get enriched within a day of creation.

### What It Does Each Run

The master cycle evaluates each job's cadence and runs the ones due today. In order of execution:

1. **Territory & owner validation** (daily) -- Runs territory-manager state-to-owner mapping. Auto-corrects Tier 1 misassignments. Flags strategic exceptions. Runs first so later jobs see correct ownership.
2. **Data hygiene & gap filling** (daily) -- crm-hygiene Modes 2-10. Finds missing segments, blank states, deprecated enum values, stale records, orphaned contacts, Cooper-owned placeholders. Auto-fixes Tier 1, flags Tier 2, holds Tier 3.
3. **New account enrichment + re-enrichment** (daily) -- Detects companies added in the last 24h with no enrichment and runs website-first adaptive enrichment. Processes a batch of 25 re-enrichment candidates per day where `last_enriched_date` is 6+ months old.
4. **Pre-deletion audit & contact consolidation** (daily) -- Before any non-ICP account gets `customer_segment = "Flagged for deletion"`, this gate checks: (a) open-deal hard stop, (b) whether the flagged company is a duplicate of an ICP primary (if yes: reassociates contacts to primary and flags the duplicate), (c) per-contact activity — any contact with `notes_last_contacted` within 90 days, `notes_last_updated` within 90 days, or association to an open deal is preserved and never flagged. Writes `flagged_for_deletion = true` only on truly dormant contacts. Never archives records — humans finalize.
5. **Contact persona gap analysis** (Fridays only) -- For Tier 1/2 accounts and accounts with open deals, checks Technical Champion + Business Sponsor + Economic Buyer coverage. Fills gaps via Apollo + LinkedIn validation.
6. **New account sourcing** (1st of month only) -- CRM gap analysis + search query generation for priority segments (Data Center Colo AI Signals, NeoCloud). All candidates held as Tier 3 for Cooper's review.
7. **Contact job-change detection** (1st of Jan / Apr / Jul / Oct only) -- Apollo + LinkedIn cross-check on Tier 1/2 contacts + contacts on accounts with open deals. Finds replacements for departures.

### Prompt for This Routine

```
You are the MaiaEdge CRM Guardian. Run the full autonomous maintenance cycle.

REPO: This repo contains the complete MaiaEdge AI knowledge base. Read these files before starting, in this order:

Primary orchestrator:
- skills/crm-guardian/SKILL.md (your master instructions -- follow exactly)

Sub-skills (domain logic -- crm-guardian delegates to these, do not redefine):
- skills/pre-deletion-audit/SKILL.md (Job 7: duplicate consolidation + flag_for_deletion gating)
- skills/company-enrichment/SKILL.md (Job 2: website-first enrichment, Step 0C re-enrichment mode)
- skills/segment-classification/SKILL.md (Job 2: qualification gates, cascade rules, EXCLUDE verdict routing)
- skills/crm-hygiene/SKILL.md (Job 1: Modes 2-10)
- skills/territory-manager/SKILL.md (Job 3: state-to-owner mapping, Apollo state verification, contact owner cascade)
- skills/contact-discovery/SKILL.md (Job 5 Mode 3 persona fill, Job 6 Mode 4 job change detection, suppression checks)
- skills/account-sourcing/SKILL.md (Job 4: CRM gap analysis, search query generation  -- 1st of month only)
- skills/import-processor/SKILL.md (Job 2: HubSpot enum value mapping)
- skills/edge-case-researcher/SKILL.md (Job 2: second-pass investigation for uncertain classifications)

HubSpot schemas + context:
- context/hubspot/property-schema.md
- context/hubspot/hubspot-values.md
- context/hubspot/territory-model.md
- context/hubspot/contact-schema.md
- context/hubspot/poc-schema.md
- context/hubspot/deals-schema.md
- context/core/icp-playbook.md
- context/core/segment-qualification.md
- context/segments/colocation.md
- context/segments/fiber-operator.md
- context/segments/neocloud.md
- context/segments/network-operator.md
- context/segments/msp-aggregator.md

CONNECTED TOOLS: HubSpot MCP, Apollo MCP

RUN-TIME INVARIANTS (apply to every job, every run):

A. TIMEZONE: All date math uses America/New_York. "Today" = current Eastern calendar date at run start. "Within 90 days" = 90 ET-calendar days. "1st of month" / "Quarterly 1st" = Eastern date. HubSpot stores timestamps in UTC; convert to ET before comparing to thresholds.

B. SKIP ALREADY-FLAGGED: Any company with customer_segment = "Flagged for deletion" is NOT touched by Jobs 1, 2, 3, 4, 5, or 6. Only Job 7 handles them.

C. CUSTOMER PROTECTION (company-level): Any company with ANY deal where hs_is_closed_won = true or dealstage = closedwon is protected. Never flag for deletion. Never segment-downgrade from ICP to non-ICP (Tier 3 escalation instead). Never reassociate contacts away from a customer company in Job 7 Mode A.

D. ERROR CONTAINMENT: A failure on one record must not abort the job. Wrap each sub-skill operation in a per-record try/except. On failure: log record ID + operation + error + request ID, continue to the next record, surface all failures in the run report's Errors section. Only connector-level failures (Apollo exhaustion, HubSpot auth revoked, MCP disconnect) halt further calls to that specific connector.

E. DEFAULT TO TIER 3 WHEN UNCERTAIN: Ambiguous data (LOW/MANUAL_REVIEW confidence, fuzzy dedup below HIGH threshold, activity signal at the 90-day boundary, conflicting sources) → do not write. Tier 3 hold for human review.

F. IDEMPOTENCY: Safe to run multiple times per day. All writes are deterministic based on current state + input. A second run same-day should return mostly "All clean."

G. MAIAEDGE GOTCHAS (these do not match intuition):
- account_tier is INVERTED. Tier 1 = highest priority, Tier 5 = lowest.
- customer_segment value "Enterprise" is legacy naming for MSP/Aggregator, NOT enterprise consumer. Enterprise consumers use "Enterprise-CustomerSegment" (non-ICP).
- AI Colo accounts use customer_segment = "Data Center Colo Provider" + company_sub_segment = "AI Signals - colo". The old value "AI - Colocation Operator" is deprecated and auto-migrated by Job 1 Mode 7.
- No em dashes in customer-facing field values (account_brief, maiaedge_value_proposition, provisioning_landscape, recent_news_or_trigger_event). Use hyphens or restructure sentences.
- Category descriptor: "Carrier infrastructure" only. Never "IaaS," "NaaS," "platform."

EXECUTION:
1. Evaluate each of the 7 jobs' cadences (using Eastern calendar date per invariant A) and run the ones due today per the crm-guardian SKILL.md Master Cadence section. Daily: jobs 1, 2, 3, 7. Friday: + job 5. 1st of month: + job 4. Quarterly (1st of Jan/Apr/Jul/Oct): + job 6.
2. Respect the 3-tier safety system exactly:
   - Tier 1: Auto-fix (field value is the evidence; do NOT create per-record HubSpot notes)
   - Tier 2: Auto-fix AND flag in the daily email report for Cooper's review
   - Tier 3: DO NOT auto-fix; list in report as pending action
3. Respect Deal Protection: escalate segment/tier/contact changes to Tier 3 on accounts with open deals; Job 7 pre-deletion audit hard-stops entirely on open-deal accounts AND customer-history accounts (invariant C).
4. For Job 7 (pre-deletion audit): a contact is preserved from flagged_for_deletion = true if ANY is true -- notes_last_contacted within 90 days (ET), notes_last_updated within 90 days (ET), any non-closed deal association, any open POC ticket association, lifecyclestage in (customer, evangelist, subscriber), or createdate within 14 days (ET). Companies with createdate within 14 days are skipped entirely.
5. For Job 2 (enrichment): the re-enrichment trigger is the company-level property last_enriched_date. Query for companies where last_enriched_date < today(ET) - 120 days OR last_enriched_date IS EMPTY with segment populated. Do NOT use hs_lastmodifieddate or createdate as a proxy. Set last_enriched_date to today's ET date after every successful enrichment.
6. For Job 3 (territory): Apollo apollo_organizations_enrich is the authoritative source for HQ state and country. When HubSpot state is blank or last_enriched_date is 120+ days stale and HubSpot disagrees with Apollo, trust Apollo and overwrite HubSpot.
7. For any Apollo-sourced contact creation (Jobs 5, 6): set hs_marketable_status = "false" (non-marketing) as the default. Before creating, check the proposed email against HubSpot for hs_email_optout = true, hs_email_hard_bounced = true, flagged_for_deletion = true, or suppression notes. If suppressed, skip and log.
8. Never archive or delete records. The routine only writes field values. Humans finalize archival as Tier 3 review.
9. Never create per-record HubSpot notes. The daily email report is the only audit trail.
10. Apollo credit exhaustion (HTTP 429 or quota errors): stop Apollo calls for this run, write partial progress, defer remainder to next run, flag in report. HubSpot rate limit (100/10s): batch writes with exponential backoff (1s -> 2s -> 4s); after 3 consecutive 429s on the same operation, log to dead-letter and move on.

OUTPUT:
Return a structured daily run report as the final output so the routine platform emails it. Format:

- Subject-ready line: CRM Guardian — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held (or All clean if both zero). Use Eastern date.
- Hero section: jobs run today, total records scanned per job, Tier 1 auto-fix counts, Apollo credits consumed, health score
- Needs your attention: Tier 2 applied-but-flagged and Tier 3 held items grouped by job, with record IDs, old/new values, and the gate that fired
- Pre-deletion audit highlights: Mode A consolidations (duplicate + primary company IDs, contacts reassociated, contacts flagged), Mode B standalone flags, Tier 3 held edge cases (including customer-history skips, strategic-exception skips)
- Errors / API failures (if any): Apollo exhaustion, HubSpot write failures, MCP auth issues, per-record exceptions with record ID + operation + request ID

Lead with items needing Cooper's attention (Tier 2 + Tier 3). Tier 1 is summary counts only.
```

### Configuration

- **Trigger**: Scheduled
- **Cadence**: Nightly, 2:00 AM Eastern
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP, Apollo MCP
- **Notification**: Email to `cooperkennedy@maiaedge.io` (Microsoft 365 / Outlook). Configure the routine's built-in notification destination to this address. The skill returns its run report as the final structured output; the routine platform handles the SMTP send via its own transport. Works for any recipient email provider (Gmail, Outlook, custom domains).
  - **Note on sender identity:** The `From:` header will be the routine platform's sender address, not `cooperkennedy@maiaedge.io` itself. True self-send (From: = Cooper's own address) would require Microsoft Graph OAuth via n8n or a Python script, which is not wired up. Skip unless the inbox-threading/sender-identity concern becomes real.
  - **Not applicable:** Gmail MCP. Google-only; does not authenticate Microsoft 365 accounts.

### Email Report Format

Every run produces a single email with:

- **Subject:** `CRM Guardian — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held`
- **Top summary (hero section):** Jobs run today, total records touched, health score, Apollo credits consumed
- **Needs your attention:** All Tier 2 (applied + flagged) and Tier 3 (held) items, grouped by job. This should be scannable in under 60 seconds.
- **What was auto-fixed:** Tier 1 summary counts per job (collapsed detail — "47 state fills, 12 owner corrections, 3 segment fills"). Full detail in HubSpot notes on the records themselves.
- **Pre-deletion audit highlights:** Mode A consolidations (duplicate → primary with contact counts), Mode B standalone flags (company name + count flagged/preserved), any held-for-review edge cases.
- **Errors or API failures:** If any job failed or an MCP call errored, list at the bottom.

The subject line is the "at a glance" — you should be able to decide whether to open the email from the subject alone. If Tier 2 = 0 and Tier 3 = 0, it was a clean day and the email is informational only.

---

## Routine 2: Pipeline Monday Brief

**Why:** Tim Ziemer (CRO) and the reps should walk into Monday standup with a current conversion view. No one should have to pull this manually.

### What It Does

Generates the 3-column pipeline discipline board:

- **Column 1 (Accounts to POC):** Pre-POC deals + momentum accounts with recent engagement
- **Column 2 (POCs to Purchase Order):** Open POC tickets with health scoring (timeline signals, trend status, blocker flags)
- **Column 3 (Orders to Expansion):** Closed-won accounts with expansion signals

For each account in each column: company name, segment, rep owner, deal stage, days in stage, last activity date, next action, and health status (GREEN/YELLOW/ORANGE/RED).

### Prompt for This Routine

```
You are running the MaiaEdge weekly pipeline discipline briefing.

REPO: Read these files first:
- skills/pipeline-discipline/SKILL.md (primary instructions)
- context/hubspot/deals-schema.md
- context/hubspot/poc-schema.md
- context/hubspot/territory-model.md

CONNECTED TOOLS: HubSpot MCP

EXECUTION:
1. Pull all open deals from the MaiaEdge Deals pipeline
2. Pull all open POC tickets (pipeline: POC Pipeline)
3. Pull call engagement data from the last 14 days for activity recency
4. Build the 3-column board per the SKILL.md methodology
5. Score each POC in Column 2 using the POC Health Scoring framework (timeline signals + trend signals)
6. Flag any account appearing in Column 1 for 30+ days with no stage progression
7. Flag any POC in Column 2 that is overdue or has no end date set

OUTPUT:
Produce a clean, scannable briefing formatted for executive consumption:
- Lead with "Needs Attention" items (RED/ORANGE health) across all columns
- Then show the full 3-column board
- End with velocity stats: avg days in Column 1 before POC, avg POC duration, conversion rates if sample size allows
- Include rep-level breakdown (Tim Lieto accounts vs Ken Cunningham accounts)

Keep it actionable. Every account listed should have a clear "next action" recommendation.
```

### Configuration

- **Trigger**: Scheduled
- **Cadence**: Weekly, Monday 7:00 AM Eastern
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP
- **Notification**: Slack #pipeline channel or email to Tim Ziemer + Tim Lieto + Ken Cunningham

---

## Routine 3: Stale Deal Watchdog (Nightly)

**Why:** Deals quietly die when no one's watching time-in-stage. This catches them before they go cold.

### What It Does

Scans all open deals for staleness signals:

- **Time in current stage > threshold** (14 days for early stages, 30 days for mid-pipeline, 45 days for late-stage)
- **No activity in 14+ days** (no calls, emails, or notes)
- **Close date in the past** with deal still open
- **MEDDPICC completion < 40%** on deals past Discovery stage

Only alerts on NEW threshold crossings -- deals that crossed a staleness boundary since the last run. Doesn't re-alert on already-flagged deals.

### Prompt for This Routine

```
You are running the MaiaEdge stale deal watchdog.

REPO: Read these files first:
- skills/pipeline-analytics/SKILL.md (deal health assessment section)
- context/hubspot/deals-schema.md

CONNECTED TOOLS: HubSpot MCP

EXECUTION:
1. Pull all open deals (dealstage NOT closedwon, NOT closedlost)
2. For each deal, check:
   a. hs_v2_time_in_current_stage -- flag if exceeds stage threshold:
      - Appointment Scheduled / Discovery: 14 days
      - Quote Provided / POC: 30 days
      - Price Agreement / Contract Review: 45 days
   b. notes_last_contacted -- flag if > 14 days ago or null
   c. closedate -- flag if in the past and deal still open
   d. MEDDPICC fields -- count filled vs total 8 fields, flag if < 40% on deals past appointmentscheduled
3. Only report deals that are NEWLY stale (crossed threshold in last 24h) OR critically stale (any deal with 0 activity in 30+ days regardless of prior alerts)

OUTPUT:
- Section 1: URGENT (30+ days no activity, or close date past)
- Section 2: WARNING (crossed time-in-stage threshold in last 24h)
- Section 3: MEDDPICC gaps (deals advancing without qualification data)

For each deal: deal name, company, rep, stage, days in stage, last activity date, amount, and a one-line recommended action.
```

### Configuration

- **Trigger**: Scheduled
- **Cadence**: Nightly, 6:00 AM Eastern
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP
- **Notification**: Slack DM to deal owner (Tim Lieto or Ken Cunningham) for their deals; full report to Cooper

---

## Routine 4: Weekly Call Digest

**Why:** Call summaries contain the best signal in the CRM -- use cases that resonate, objections that block, competitive mentions, PMF signals. Today no one systematically reviews them.

### What It Does

1. Pulls all calls from the prior 7 days with AI summaries
2. Runs call-analysis Mode 1 (extraction) on each call
3. Aggregates into patterns: top use cases discussed, recurring pain points, competitive mentions, segment-level trends
4. Produces a formatted HTML report per call-reporting design system

### Prompt for This Routine

```
You are running the MaiaEdge weekly call intelligence digest.

REPO: Read these files first:
- skills/call-analysis/SKILL.md (Mode 1: Call Extraction, Mode 2: Trend Analysis)
- skills/call-reporting/SKILL.md (Design System section for HTML formatting)
- context/sales/use-case-taxonomy.md
- context/hubspot/call-schema.md
- context/hubspot/territory-model.md

CONNECTED TOOLS: HubSpot MCP

EXECUTION:
1. Query all CALL engagements from the last 7 days using search_crm_objects
   - Include associations: COMPANY, DEAL, TICKET
   - Use the content analysis property set from call-schema.md
   - Paginate if > 100 results
2. For each call with hs_call_summary content:
   - Strip HTML from summary
   - Classify use cases against use-case-taxonomy.md (21 canonical use cases)
   - Extract: pain points, objections, competitive mentions, resonance signals, next steps
   - Note the associated company segment and deal stage
3. Aggregate across all calls:
   - Use case frequency (ranked, with example quotes)
   - Pain points by segment
   - Competitive mentions (who, how often, in what context)
   - Deals where calls surfaced risk signals
   - Rep activity breakdown (calls per rep, avg duration)
4. Produce the report as self-contained HTML using the call-reporting design system:
   - Slate color palette, indigo accent
   - KPI cards for hero metrics (total calls, avg duration, unique accounts touched)
   - CSS bar charts for use case ranking
   - Segment color mapping (Colo=#6366F1, Fiber=#0EA5E9, Neocloud=#8B5CF6, NetOp=#14B8A6, MSP=#F59E0B)

OUTPUT:
Save the HTML report to a file. The report should be scannable in under 2 minutes by the CRO.
Lead with: "X calls this week across Y accounts. Top signal: [most frequent use case or most notable insight]."
```

### Configuration

- **Trigger**: Scheduled
- **Cadence**: Weekly, Friday 4:00 PM Eastern
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP
- **Notification**: Email to Tim Ziemer, Tim Lieto, Ken Cunningham with HTML report attached

---

## Routine 5: Territory Drift Check

**Why:** New accounts get created constantly. If someone enters a company without a state, or with a state that doesn't match the assigned owner, the rep might never see it. A weekly sweep prevents silent misroutes.

### Prompt for This Routine

```
You are running the MaiaEdge weekly territory drift check.

REPO: Read these files first:
- skills/territory-manager/SKILL.md
- context/hubspot/territory-model.md
- context/hubspot/property-schema.md

CONNECTED TOOLS: HubSpot MCP

EXECUTION:
1. Pull all company records created or modified in the last 7 days
2. For each, check:
   a. state is populated
   b. hubspot_owner_id matches the state-to-owner mapping in territory-model.md
   c. If state is blank but country = United States, flag as "needs state"
   d. If non-US country, verify owner = Tim Ziemer (159350430)
3. Also check: any companies currently owned by Cooper Kennedy (160267902) -- these are placeholder assignments that need routing
4. Produce a correction list:
   - Misassigned (has state, wrong owner): list with current vs correct owner
   - Missing state (US company, no state): list for manual research
   - Cooper-owned (placeholder): list for routing

Do NOT auto-correct. This is an audit routine -- produce the report for Cooper to review and approve corrections.
```

### Configuration

- **Trigger**: Scheduled
- **Cadence**: Weekly, Sunday 9:00 PM Eastern
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP
- **Notification**: Slack DM to Cooper

---

## Routine 6: Repo Build Validator (Webhook)

**Why:** The repo has 25 skills, 49 context files, 9 plugins, and 8 enterprise projects. A bad merge in any skill or context file can silently break plugin builds. Catch it before it hits main.

### Prompt for This Routine

```
You are validating the MaiaEdge AI repo build after a code change.

EXECUTION:
1. Run: bash build.sh
2. Check exit code. If non-zero, report the error and stop.
3. Verify all 9 plugin zips exist in builds/plugins-zipped/:
   - linkedin-network-builder.zip
   - maiaedge-call-intelligence.zip
   - maiaedge-enrichment-pipeline.zip
   - maiaedge-events.zip
   - maiaedge-outreach.zip
   - maiaedge-revops.zip
   - maiaedge-sales-docs.zip
   - maiaedge-sales-support.zip
   - maiaedge-sdr-pipeline.zip
4. Verify all 5 standalone skill zips exist in builds/skills-zipped/
5. Verify all 7 enterprise upload/ folders are populated (non-empty)
6. Spot-check: for each plugin, verify the skill count inside the zip matches the plugin-manifest.json declaration
7. If any check fails, comment on the PR with the specific failure

OUTPUT:
- If all checks pass: Comment "Build validated. 9 plugins, 5 standalone skills, 7 enterprise projects -- all clean."
- If any check fails: Comment with the specific failure(s) and which plugin/project is affected
```

### Configuration

- **Trigger**: GitHub Webhook
- **Event filter**: Pull requests targeting `main` branch
- **Repo**: maiaedge-ai
- **Connectors**: GitHub (for PR comments)

---

## Routine 7: Context Drift Detector (Webhook)

**Why:** When someone changes a context file (e.g., updates territory-model.md), skills that reference it might need updates too. This routine catches the gap.

### Prompt for This Routine

```
You are checking for context drift after a change to reference files.

EXECUTION:
1. Identify which files in context/ were changed in this PR
2. For each changed context file, search all skills/*/SKILL.md for references to that filename
3. Read the changed context file's diff to understand WHAT changed
4. For each referencing skill, assess:
   - Does the skill hardcode any values from the changed file? (e.g., owner IDs, state lists, enum values, stage names)
   - If yes, does the skill's hardcoded value still match the updated context file?
   - If no hardcoded values, the skill dynamically reads context at runtime -- no drift risk
5. Report findings

OUTPUT:
- List each changed context file
- For each, list skills that reference it
- Flag any skill where hardcoded values are now stale
- If no drift detected: "No skill updates needed -- all references are dynamic or still current."
```

### Configuration

- **Trigger**: GitHub Webhook
- **Event filter**: Pull requests that modify files in `context/`
- **Repo**: maiaedge-ai
- **Connectors**: GitHub

---

## Routine 8: Enrichment Chain (API)

**Why:** Today, after running company-enrichment on a batch, you manually kick off import-processor, then manually run edge-case-researcher. An API routine chains them automatically.

### Prompt for This Routine

```
You are running the MaiaEdge post-enrichment processing chain.

The request body will contain:
- enrichment_output_path: path to the enrichment output XLSX/CSV file

REPO: Read these files first:
- skills/import-processor/SKILL.md
- skills/edge-case-researcher/SKILL.md
- context/enrichment/output-schemas.md
- context/hubspot/hubspot-values.md

CONNECTED TOOLS: HubSpot MCP, Apollo MCP

EXECUTION:
1. Read the enrichment output file from the provided path
2. Run the import-processor workflow:
   - Transform all values to HubSpot property labels
   - Separate qualified accounts (ready for import) from edge cases and definitive excludes
   - Produce: qualified.xlsx, edge-cases.xlsx, excludes-log.xlsx
3. Run edge-case-researcher on the edge-cases.xlsx output:
   - Deep-dive each edge case with multi-source verification
   - Reclassify as qualified or confirm exclusion
   - Append any recovered accounts to qualified.xlsx
4. Produce final outputs:
   - final-qualified-import.xlsx (HubSpot-ready, zero manual adjustment needed)
   - final-excludes-log.xlsx (with detailed exclusion reasons)
   - processing-summary.txt (counts: input -> qualified -> edge cases -> recovered -> final excludes)

OUTPUT:
Report the processing summary and file locations. Flag any edge cases that were borderline and might warrant manual review despite the automated decision.
```

### Configuration

- **Trigger**: API endpoint
- **Repo**: maiaedge-ai
- **Connectors**: HubSpot MCP, Apollo MCP
- **Usage**: Call via POST after any enrichment batch completes. Can be wired into a webhook from enrichment tooling or called manually.

---

## Implementation Order

Ranked by effort-to-impact ratio. Start at the top and work down:

| Priority | Routine | Effort | Impact | Notes |
|----------|---------|--------|--------|-------|
| 1 | CRM Guardian (nightly) | Low -- skill fully built | Very High -- catches all data rot daily | Biggest single improvement to CRM quality |
| 2 | Stale Deal Watchdog | Low -- straightforward query logic | High -- prevents silent deal death | Quick win, immediate rep value |
| 3 | Pipeline Monday Brief | Low -- skill fully built | High -- weekly leadership visibility | Tim Z sees conversion health without asking |
| 4 | Territory Drift Check | Very Low -- simple audit | Medium -- prevents misrouting | Runs quietly, catches routing errors |
| 5 | Weekly Call Digest | Medium -- aggregation + HTML formatting | High -- systematic call intelligence | Best signal extraction from existing data |
| 6 | Repo Build Validator | Low -- shell script validation | Medium -- protects the knowledge base | Insurance policy as repo grows |
| 7 | Context Drift Detector | Medium -- cross-reference analysis | Medium -- prevents stale skills | Smart guard rail for content changes |
| 8 | Enrichment Chain | Medium -- multi-step orchestration | Medium -- saves manual handoffs | API trigger, use after batch enrichment |

---

## Setup Checklist

Before creating any routine, verify these prerequisites:

- [ ] Claude Code Pro, Max, Team, or Enterprise plan active
- [ ] HubSpot MCP connector configured and authenticated
- [ ] Apollo MCP connector configured and authenticated (needed for Routines 1, 8)
- [ ] GitHub repo `maiaedge-ai` connected to Claude Code
- [ ] Slack or email notification channel configured for routine outputs
- [ ] Confirm daily routine limit for your plan tier (Pro=5, Max=15, Team/Enterprise=25)

### Connector Requirements by Routine

| Routine | HubSpot | Apollo | GitHub | Slack/Email |
|---------|---------|--------|--------|-------------|
| 1. CRM Guardian | Required | Required | -- | Recommended |
| 2. Pipeline Monday | Required | -- | -- | Recommended |
| 3. Stale Deal Watchdog | Required | -- | -- | Recommended |
| 4. Call Digest | Required | -- | -- | Recommended |
| 5. Territory Drift | Required | -- | -- | Recommended |
| 6. Build Validator | -- | -- | Required | -- |
| 7. Context Drift | -- | -- | Required | -- |
| 8. Enrichment Chain | Required | Required | -- | Optional |

---

## How to Create Each Routine in Claude Code

For each routine above:

1. Open Claude Code in the maiaedge-ai repo
2. Run: `/routines create` (or use the Routines UI if available)
3. Set the trigger type (Scheduled / Webhook / API)
4. Paste the prompt from this document
5. Configure the cadence/event filter per the Configuration section
6. Connect the required integrations (HubSpot MCP, Apollo MCP, GitHub)
7. Test with a manual trigger first before enabling the schedule
8. Review the first 3 runs manually to verify output quality

---

## Daily Routine Budget

Assuming a Max plan (15 routines/day):

| Routine | Runs/Day | Day |
|---------|----------|-----|
| CRM Guardian | 1 | Every day |
| Stale Deal Watchdog | 1 | Every day |
| Territory Drift | -- | Sunday only (1 run) |
| Pipeline Monday Brief | -- | Monday only (1 run) |
| Call Digest | -- | Friday only (1 run) |
| Build Validator | Variable | On PR (estimate 0-2/day) |
| Context Drift | Variable | On PR touching context/ (estimate 0-1/day) |
| Enrichment Chain | Variable | On-demand (estimate 0-1/day) |
| **Typical weekday total** | **2-5** | Well within 15/day limit |

---

## Future Routine Ideas (Phase 2)

Once the core 8 are running smoothly:

- **Post-call MEDDPICC updater**: After any call is logged in HubSpot, auto-extract MEDDPICC fields and update the associated deal record
- **Weekly competitive intel digest**: Aggregate competitive mentions from calls + web signals into a weekly brief
- **Lead response time tracker**: Alert if a NEW lead sits untouched for > 4 hours during business hours
- **Monthly pipeline trend report**: Full pipeline-analytics HTML report comparing this month vs last month
- **Smartlead reply sync**: When a positive reply comes in via Smartlead webhook, update HubSpot contact status and create a follow-up task for the rep
- **Conference attendee auto-enrichment**: When a new attendee list file is committed to the repo, auto-run event-intelligence processing
