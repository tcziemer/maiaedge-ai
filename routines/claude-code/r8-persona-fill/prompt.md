# CRM Guardian - Routine 8: Weekly Persona Gap Fill

Weekly, Friday at 9:00 AM ET (after the 6 daily routines complete). You audit Tier 1 and Tier 2 accounts for missing buying-committee personas (Technical Champion / Business Sponsor / Economic Buyer / Procurement per `contact-schema.md`), then use Apollo + LinkedIn to find + verify replacement contacts. Verified Apollo-sourced contacts auto-create in HubSpot at Tier 2 with `hs_marketable_status = "false"` (sales-only, not marketing). Deal-protected late-stage accounts and unverified candidates surface as Tier 3 for rep approval.

**CRM scale (as of 2026-04-24):** ~600-1,000 active Tier 1/2 accounts (the priority audit pool). Persona coverage health varies - many accounts have a Technical Champion but lack an Economic Buyer or Procurement contact. Steady-state weekly fill is 20-40 contacts; first run could create 100-300 if historical persona gaps have accumulated.

## Repo

**Orchestrator reference (for invariants + safety tiers):**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/contact-discovery/SKILL.md` (Mode 1 HubSpot persona audit, Mode 3 Apollo + LinkedIn hybrid fill - full methodology, suppression checks, verified-email-only filter)
- `skills/territory-manager/SKILL.md` (contact owner cascade per company territory)

**Context:**
- `context/hubspot/contact-schema.md` (persona framework: buying-committee roles + per-segment priority personas + multi-thread targets)
- `context/hubspot/property-schema.md`
- `context/hubspot/territory-model.md`
- `context/hubspot/deals-schema.md` (deal-stage check for late-stage protection)
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/neocloud.md`
- `context/segments/network-operator.md`
- `context/segments/msp-aggregator.md`
- `context/segments/enterprise.md` (Multi-DC ICP - added 2026-05-11. Persona priority by sub-segment: Retail/Distribution → Network Architect/Principal Network Engineer → VP Network Infrastructure → CIO; Financial Services → Principal Network Architect → VP Network Infrastructure → CSO/CISO; Healthcare Systems → VP Network Infrastructure → CSO/CISO → CIO; Outsourcing Services → VP Network Infrastructure → CSO/CISO → CIO. Apollo title patterns added in Workflow Step 3 below.)

**Connected tools:** HubSpot MCP, Apollo MCP, Slack MCP, web_fetch (for LinkedIn public-profile validation).

## Run-Time Invariants

### A. Timezone
America/New_York. "Friday" = Eastern calendar day.

### B. Day-Gate
Run only on Fridays in ET. If not Friday, exit cleanly with NO DM - append a single ⏭️ (or the canvas-convention skip emoji) Run-log row to canvas `F0B0AFSB9LN` noting `not a Friday run, skipped` and stop. The CRM Ops Daily Digest surfaces the skip from the ledger; a self-DM is not needed.

### C. Skip Already-Flagged
Skip companies with `customer_segment = "Flagged for deletion"`. Skip contacts with `flagged_for_deletion = true`.

### D. Customer Protection
Customer-history accounts (any deal where `hs_is_closed_won = true` or `dealstage = closedwon`): allow new persona-fill contacts (sales still works the customer base for expansion), but never modify existing customer contacts. The new contact is additive, not a replacement.

### E. Suppression Check (mandatory before every contact create)
Before creating any Apollo-sourced contact, check the proposed email against HubSpot for ALL of:
- `hs_email_optout = true` (CAN-SPAM / GDPR - must NOT contact)
- `hs_email_hard_bounced = true`
- `flagged_for_deletion = true` on any contact with this email
- An existing contact at the same company with this email (case-insensitive)
- An existing contact globally with this email (HubSpot rejects duplicates anyway, but skip cleanly to avoid the API error and log)

If ANY suppression hits → skip the candidate, log it in the report's "Suppressed" subsection.

### F. Error Containment
Per-contact try/except. A failure on one persona-search does not block the rest.

### G. Default to Tier 3 When Uncertain
Apollo-only with no LinkedIn validation → Tier 3 hold. LinkedIn says departed but Apollo says current → Tier 3 hold (ambiguous; route to Routine 9 next quarter for explicit job-change handling).

### H. Idempotency
Re-running same-day finds the same persona gaps either already filled (existing contact at that role) or surfaced as Tier 3 from the prior run, and produces minimal new work. The suppression check on existing email is the idempotency key.

### I. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest priority).
- HubSpot's contact `lifecyclestage` enum does NOT include `evangelist` - valid values: `subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, other`. Default for new persona-fill contacts: `lead`.
- `hs_marketable_status = "false"` is REQUIRED on every auto-created contact - keeps MaiaEdge's paid-marketing tier from inflating silently. Reps flip to `"true"` manually when they decide to run marketing touch.
- `customer_segment = "Enterprise-CustomerSegment"` is now an **ICP segment as of 2026-05-11**. Tier 1+2 Enterprise accounts (Meijer-class) are in scope for persona fill alongside the operator ICP segments. Apollo title patterns for Enterprise personas listed in Step 3 below.

### J. Write Authorization
Every `mcp__claude_ai_HubSpot__manage_crm_objects` create call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized creates:** new Contact with these properties:
- `firstname`, `lastname`, `email`, `jobtitle`, `phone`, `linkedin_url` (from Apollo)
- `lifecyclestage = "lead"`
- `hs_marketable_status = "false"` (HARD requirement)
- `hubspot_owner_id` cascaded from associated company's owner (territory-manager)
- `customer_segment` synced from associated company's segment
- Association to the company (via `associations` field in createRequest)

**Hard stops:**
- MaiaEdge's own record (HubSpot company ID 124293230301).
- Open deals at `dealstage = contractsent` or later (i.e., `contractsent` - `closedwon` and `closedlost` are out by closed check) → escalate persona-fill recommendation to Tier 3. Reasoning: contracts mid-negotiation are sensitive; introducing a new contact at this stage can disrupt rep-led legal/procurement dynamics. Rep approves before the contact lands.

## Workflow

0. **Preflight:**
   - Confirm Apollo MCP is connected. Call `apollo_users_api_profile` once. Compute `monthly_headroom = 6000 - monthly_consumed`. Set `apollo_budget_run = min(175, monthly_headroom)` when `monthly_headroom >= 50`, else `apollo_skip = true`.
   - Confirm HubSpot MCP is connected. If not: send the one-line hard-failure ping per Delivery (`:red_circle: CRM Guardian - Persona Fill (Weekly) ABORTED - HubSpot MCP unreachable.`), write the matching ❌ Run-log row, and exit.
   - No early-checkpoint smoke-signal DM. That R8 fired is recoverable from the on-disk run report + the canvas Run-log row + the CRM Ops Daily Digest. Capture the Apollo monthly counter + `apollo_budget_run` + `apollo_skip` for the on-disk run report hero.
   - NO `git pull` / `git fetch` / `git status` / `git commit` / `git push` at any point in this routine. Cross-run Apollo state lives entirely in the on-disk run reports + Apollo's native `apollo_users_api_profile.monthly_consumed`. The Bash tool is still available for non-git uses, but git commands MUST NOT be invoked.

1. **Pull target accounts:** HubSpot `search_crm_objects` on COMPANY with:
   - `account_tier IN ('tier_1', 'tier_2')`
   - `customer_segment != 'Flagged for deletion'`
   - Company ID != `124293230301`
   - Pull `signal_heat` alongside `account_tier`.
   - **Sort primarily by `signal_heat`** (`Hot` -> `Warm` -> `Cool` -> `Cold` — Title Case per HubSpot enum), then by `account_tier ASC` (Tier 1 before Tier 2 within each heat bucket), then `last_enriched_date DESC` (most recently enriched first - fresh data). Apollo budget hits the highest-intent accounts first; `Cold` Tier 1 accounts still get filled, they just queue behind `Hot` accounts. Rationale: persona-fill at the moment of intent is more valuable than persona-fill on a quiet strategic account. See `context/account-tiering/tier-compute-spec.md` §11.5 for the heat compute spec.
   - Paginate fully - no cap on accounts scanned.

2. **Per account, run contact-discovery Mode 1 (persona audit):**
   - Pull associated contacts (existing).
   - Compare against the segment-specific persona priority list in `contact-schema.md` Section 4 (Persona Coverage by Segment). Identify which buying-committee roles are missing.
   - Output: list of persona gaps for this account.

3. **For each persona gap, run contact-discovery Mode 3 (Apollo + LinkedIn hybrid fill):**

   **Apollo title patterns for Enterprise sub-segments (added 2026-05-11):** When the company is `customer_segment = "Enterprise-CustomerSegment"`, search for these titles via `apollo_mixed_people_api_search`:
   - **Technical Champion** (highest priority): `VP Network Infrastructure`, `Director Network Engineering`, `Principal Network Engineer`, `Principal Network Architect`, `Senior Director Networking`, `Head of Network Architecture`. Add seniority filter: VP, Director, Principal, Head, Senior Director.
   - **Business Sponsor / Economic Buyer:** `CIO`, `Chief Information Officer`, `SVP IT`, `EVP Technology`, `Chief Technology Officer` (CIO is the more reliable fit for Enterprise buying - most enterprises have CIOs, fewer have CTOs).
   - **Security Stakeholder:** `CSO`, `CISO`, `Chief Information Security Officer`, `VP Information Security`, `VP Cybersecurity`. Especially load-bearing for Healthcare Systems and Financial Services Enterprise sub-segments.
   - **Compliance** (regulated verticals - Financial Services + Healthcare Systems): `Chief Compliance Officer`, `VP Risk Management`, `Director Regulatory Affairs`. Lower priority than the other three; surface only if Enterprise is FS or Healthcare AND no other persona slot is open.

   **Sub-segment specialization in Enterprise title patterns (use as title-match boost when present in Apollo):**
   - Financial Services: + "Markets Network", "Trading Infrastructure", "Connectivity Engineering" (NY4/NY5 / co-lo adjacency)
   - Healthcare Systems: + "Clinical Network Operations", "EHR Infrastructure", "Imaging Network"
   - Retail and Distribution: + "Store-and-DC Network", "Distribution Network Operations", "Retail Connectivity"
   - Outsourcing Services: + "Delivery Center Network", "Client Connectivity", "Site Operations Network"

   **Apollo's two-step shape:** `apollo_mixed_people_api_search` returns CANDIDATES with obfuscated last names and no LinkedIn URLs (this is FREE and EXPECTED - not a Tier 3 trigger). To create a contact you MUST then call `apollo_people_match` on the chosen candidate to REVEAL email + LinkedIn URL (1 credit each). Reveal is the credit cost the routine is supposed to pay - the previous behavior of presenting obfuscated candidates as "Tier 2 review-ready" and waiting for Cooper was a misread. Reveal is part of the auto-create path.

   **Sub-flow (per persona gap):**
   1. `apollo_mixed_people_api_search` - filter by company domain + title patterns matching the persona role + seniority + `email_status = verified` (HARD requirement - never source unverified). Take top 3 candidates.
   2. For each candidate in priority order: call `apollo_people_match` to reveal email + LinkedIn URL (1 credit). On HIGH confidence match (Apollo employer = target company AND title still matches the persona role), proceed to step 3. On candidate-level mismatch (employer drift, title drift), discard the candidate and try the next; do NOT spend reveal credits on candidates Apollo flagged with low employment-match score.
   3. `web_fetch` the revealed LinkedIn URL - confirm:
      (a) person's listed company on LinkedIn matches target,
      (b) role title matches Apollo (casing differences OK),
      (c) no "departed" / "ex-" / "former" / "previous" markers.
   4. Apply suppression check (invariant E).
   5. If all green: auto-create at Tier 2 (per step 4 below). If LinkedIn fails or suppression hits: discard, try the next candidate. If all 3 candidates exhausted: surface the persona slot in "Rep action - manual sourcing needed" and move on.

   **Cap on reveals per persona slot:** 3 reveals max (matches the 3-candidate shortlist). Total reveals per run ≤ 43 at full cap (43 contacts × ~1 reveal each in the steady-state happy path; up to 3× when first candidates fail). Reduced from prior 60 due to 2026-05-03 weekly budget tightening (175 cr/run vs. 250).

4. **Tier assignment per Mode 3 result:**

   | Apollo result | LinkedIn result | Deal status | Action | Tier |
   |---|---|---|---|---|
   | Verified email + current employment | Confirms current at target company | No open deal OR deal `appointmentscheduled`-`decisionmakerboughtin` | Auto-create | Tier 2 |
   | Verified email + current employment | Confirms current at target company | Open deal at `contractsent` | Hold for rep approval | Tier 3 |
   | Verified email + current employment | Profile not publicly accessible / 404 / private | Any | Hold ("verify before adding") | Tier 3 |
   | Verified email | LinkedIn shows departed | Any | Hold (route to Routine 9 next quarter) | Tier 3 |
   | Apollo email status NOT verified | (not checked) | Any | Skip silently - never source unverified | - |
   | Suppressed (invariant E) | - | - | Skip + log in "Suppressed" | - |
   | Customer-history account | Any | Any | Auto-create allowed (additive) - flag for rep visibility | Tier 2 |

5. **Owner + segment cascade:** New contact's `hubspot_owner_id` = associated company's `hubspot_owner_id` (territory-manager). New contact's `customer_segment` = associated company's `customer_segment`.

6. **Surface remaining gaps:** Persona slots where no candidate was found (Apollo returned 0 verified-email matches for the role at this company) → "Rep action: source manually" subsection of the report. Include the company name + persona role + segment so the rep can target manually.

## Safety Tiers

(Summarized - full table in step 4.)

| Outcome | Tier |
|---|---|
| Verified Apollo + LinkedIn-confirmed contact, deal pre-`contractsent` | Tier 2 (auto-create + flag) |
| Same, but at customer-history account | Tier 2 (additive, flag for rep) |
| Same, but deal at `contractsent` | Tier 3 (hold for rep) |
| Apollo email not verified | Skip - never auto-source unverified |
| LinkedIn shows departed | Tier 3 (route to Routine 9) |
| Persona gap with no candidates found | Surface as "rep action: source manually" |

## Caps & Budgets

- **Account scan:** all Tier 1+2 accounts (uncapped read, paginated).
- **Persona audit:** up to 4 persona slots checked per account (Technical Champion / Business Sponsor / Economic Buyer / Procurement).
- **Priority order for persona search (when Apollo cap is binding):** open-deal accounts within Tier 1+2 always processed first regardless of audit recency; then Tier 1 accounts (oldest-persona-audited first); then Tier 2 (oldest-persona-audited first).
- **Contact create cap:** ~43 contacts per run (HARD cap, derived from ~175 Apollo cr/run target at ~4 cr/contact). First-run drain may exceed; defer remainder to next Friday - the audit is idempotent so persona gaps reappear next run.
- **Apollo credits (revised 2026-05-07):** monthly-only cap, no git, no shared tracker file. Soft per-run target: **175 credits**. Hard per-run cap: **250 credits** (defensive ceiling).
  - **Preflight check** (Step 0 below): call `apollo_users_api_profile` once. Compute `monthly_headroom = 6000 - monthly_consumed`. Set `apollo_budget_run = min(175, monthly_headroom)` if `monthly_headroom >= 50`, else `apollo_skip = true` (skip Apollo entirely, surface ALL persona gaps as "manual sourcing needed" in the on-disk run report, and note in the report hero that the monthly cap was reached). A monthly-cap `apollo_skip` is NOT a hard failure - it's a clean run with zero creates; no failure ping.
  - Mode 3 is Apollo-heavy: ~3-5 credits per persona search (people search + match). 43 contacts × 4 credits avg = 172. Stop the contact-create loop the moment cumulative `apollo_consumed >= apollo_budget_run`.
  - Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded` from Apollo - flip `apollo_skip = true` mid-run, surface remaining gaps as manual sourcing needed.
  - **Cross-run accounting** lives in the on-disk run reports. Each run's on-disk report hero records `Apollo credits consumed: N (monthly: X / 6000 used after this run)`. NO git pull, NO tracker file read, NO commit/push. (The CRM Ops Daily Digest also rolls these up.)
- **HubSpot writes:** **Batch cap: 10 contacts per `manage_crm_objects.createRequest` call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. At ~43 contacts/run that's ~5 batched calls per run. Exponential backoff (1s → 2s → 4s) on HTTP 429; halve to 5/batch on 3+ consecutive 429s.
- **LinkedIn fetches:** ~1 web_fetch per Apollo hit (validation). Soft cap 500 fetches per run.

## Output (on-disk run report)

Write this structured report to the on-disk run report at `weekly-reports/YYYY-MM-DD/r8-persona-fill/run-report.md`. It is NOT a DM body (see Delivery).

- **Subject (use as the report's top heading):** `CRM Guardian - Persona Fill (Weekly) - [YYYY-MM-DD] - [N] contacts created, [M] Tier 3 held, [K] manual sourcing needed`
- **Hero:** Tier 1+2 accounts scanned, persona gaps detected, contacts created (Tier 2), Tier 3 holds, suppressions, Apollo credits consumed.
- **Created (Tier 2) - by rep territory:**
  - Tim Lieto (Northeast + West): account name | persona role | new contact (firstname, jobtitle, email)
  - Ken Cunningham (Southeast): same
  - Tory Teague (Central): same
  - Markus Hendrich (Europe): same
  - Tim Ziemer (International + Tier 1 SP): same
  - Unassigned (Cooper): same
  This per-rep grouping helps Cooper preview which contacts will appear on each rep's dashboard.
- **Tier 3 held:** unverified Apollo, LinkedIn-departed, deal-protected at `contractsent`, customer-history (informational).
- **Suppressed:** suppression-check failures (opt-out, hard-bounced, duplicate, flagged) - count + reasons.
- **Rep action - manual sourcing needed:** persona gaps with zero candidates - companies + missing personas, route to source manually via LinkedIn Sales Nav or referrals.
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch. (For Routine 8: prior-run "Apollo reveal pending" candidates from before the auto-create flow was wired up should be drained on the first run after that fix lands - they should now auto-create, not be re-surfaced.)
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian - Routine 8: Persona Fill | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the on-disk run report's Errors section and continue - do not abort the routine.

## Delivery - quiet on success, ping only on hard failure

Do NOT DM Cooper a per-run debrief, and do NOT send an early-checkpoint smoke-signal DM. On a clean or partial-but-recoverable run, the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r8-persona-fill/run-report.md` (the Output structure above is that report, not a DM body - hero with `Apollo credits consumed: N (monthly: X / 6000 used after this run)`, per-rep created tables, Tier 3 holds, suppressions, manual-sourcing list), and (2) the one Run-log row this routine already appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji from the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's creates + holds from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`, self-DM, workspace `maia-edge.slack.com`) ONLY on a hard failure - HubSpot, Slack, or Apollo MCP unreachable, an abort (e.g. the Step 0 HubSpot-unreachable abort), or zero accounts processed against a non-empty Tier 1+2 audit pool - as ONE line:
`:red_circle: CRM Guardian - Persona Fill (Weekly) [FAILED/ABORTED/PAUSED] - [one-clause reason].`
Still write the matching ❌/⚠️ Run-log row to the canvas. Retry the ping once (1s -> 2s); if it still fails, the disk report + Run-log row are the fallback. (A monthly-cap `apollo_skip` run with zero creates is NOT a hard failure - record it normally.)
