# CRM Guardian — Routine 8: Weekly Persona Gap Fill

Weekly, Friday at 9:00 AM ET (after the 6 daily routines complete). You audit Tier 1 and Tier 2 accounts for missing buying-committee personas (Technical Champion / Business Sponsor / Economic Buyer / Procurement per `contact-schema.md`), then use Apollo + LinkedIn to find + verify replacement contacts. Verified Apollo-sourced contacts auto-create in HubSpot at Tier 2 with `hs_marketable_status = "false"` (sales-only, not marketing). Deal-protected late-stage accounts and unverified candidates surface as Tier 3 for rep approval.

**CRM scale (as of 2026-04-24):** ~600-1,000 active Tier 1/2 accounts (the priority audit pool). Persona coverage health varies — many accounts have a Technical Champion but lack an Economic Buyer or Procurement contact. Steady-state weekly fill is 20-40 contacts; first run could create 100-300 if historical persona gaps have accumulated.

## Repo

**Orchestrator reference (for invariants + safety tiers):**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/contact-discovery/SKILL.md` (Mode 1 HubSpot persona audit, Mode 3 Apollo + LinkedIn hybrid fill — full methodology, suppression checks, verified-email-only filter)
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

**Connected tools:** HubSpot MCP, Apollo MCP, Slack MCP, web_fetch (for LinkedIn public-profile validation).

## Run-Time Invariants

### A. Timezone
America/New_York. "Friday" = Eastern calendar day.

### B. Day-Gate
Run only on Fridays in ET. If not Friday, exit cleanly with a one-line Slack DM `:bust_in_silhouette: *CRM Guardian — Persona Fill (Weekly)* — [YYYY-MM-DD] — not a Friday run, skipping.` so Cooper sees the cron fired.

### C. Skip Already-Flagged
Skip companies with `customer_segment = "Flagged for deletion"`. Skip contacts with `flagged_for_deletion = true`.

### D. Customer Protection
Customer-history accounts (any deal where `hs_is_closed_won = true` or `dealstage = closedwon`): allow new persona-fill contacts (sales still works the customer base for expansion), but never modify existing customer contacts. The new contact is additive, not a replacement.

### E. Suppression Check (mandatory before every contact create)
Before creating any Apollo-sourced contact, check the proposed email against HubSpot for ALL of:
- `hs_email_optout = true` (CAN-SPAM / GDPR — must NOT contact)
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
- HubSpot's contact `lifecyclestage` enum does NOT include `evangelist` — valid values: `subscriber, lead, marketingqualifiedlead, salesqualifiedlead, opportunity, customer, other`. Default for new persona-fill contacts: `lead`.
- `hs_marketable_status = "false"` is REQUIRED on every auto-created contact — keeps MaiaEdge's paid-marketing tier from inflating silently. Reps flip to `"true"` manually when they decide to run marketing touch.

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
- Open deals at `dealstage = contractsent` or later (i.e., `contractsent` — `closedwon` and `closedlost` are out by closed check) → escalate persona-fill recommendation to Tier 3. Reasoning: contracts mid-negotiation are sensitive; introducing a new contact at this stage can disrupt rep-led legal/procurement dynamics. Rep approves before the contact lands.

## Workflow

1. **Pull target accounts:** HubSpot `search_crm_objects` on COMPANY with:
   - `account_tier IN ('tier_1', 'tier_2')`
   - `customer_segment != 'Flagged for deletion'`
   - Company ID != `124293230301`
   - Sort by `account_tier ASC` (Tier 1 first), then `last_enriched_date DESC` (most recently enriched first — fresh data).
   - Paginate fully — no cap on accounts scanned.

2. **Per account, run contact-discovery Mode 1 (persona audit):**
   - Pull associated contacts (existing).
   - Compare against the segment-specific persona priority list in `contact-schema.md` Section 4 (Persona Coverage by Segment). Identify which buying-committee roles are missing.
   - Output: list of persona gaps for this account.

3. **For each persona gap, run contact-discovery Mode 3 (Apollo + LinkedIn hybrid fill):**

   **Apollo's two-step shape:** `apollo_mixed_people_api_search` returns CANDIDATES with obfuscated last names and no LinkedIn URLs (this is FREE and EXPECTED — not a Tier 3 trigger). To create a contact you MUST then call `apollo_people_match` on the chosen candidate to REVEAL email + LinkedIn URL (1 credit each). Reveal is the credit cost the routine is supposed to pay — the previous behavior of presenting obfuscated candidates as "Tier 2 review-ready" and waiting for Cooper was a misread. Reveal is part of the auto-create path.

   **Sub-flow (per persona gap):**
   1. `apollo_mixed_people_api_search` — filter by company domain + title patterns matching the persona role + seniority + `email_status = verified` (HARD requirement — never source unverified). Take top 3 candidates.
   2. For each candidate in priority order: call `apollo_people_match` to reveal email + LinkedIn URL (1 credit). On HIGH confidence match (Apollo employer = target company AND title still matches the persona role), proceed to step 3. On candidate-level mismatch (employer drift, title drift), discard the candidate and try the next; do NOT spend reveal credits on candidates Apollo flagged with low employment-match score.
   3. `web_fetch` the revealed LinkedIn URL — confirm:
      (a) person's listed company on LinkedIn matches target,
      (b) role title matches Apollo (casing differences OK),
      (c) no "departed" / "ex-" / "former" / "previous" markers.
   4. Apply suppression check (invariant E).
   5. If all green: auto-create at Tier 2 (per step 4 below). If LinkedIn fails or suppression hits: discard, try the next candidate. If all 3 candidates exhausted: surface the persona slot in "Rep action — manual sourcing needed" and move on.

   **Cap on reveals per persona slot:** 3 reveals max (matches the 3-candidate shortlist). Total reveals per run ≤ 60 at full cap (62 contacts × ~1 reveal each in the steady-state happy path; up to 3× when first candidates fail).

4. **Tier assignment per Mode 3 result:**

   | Apollo result | LinkedIn result | Deal status | Action | Tier |
   |---|---|---|---|---|
   | Verified email + current employment | Confirms current at target company | No open deal OR deal `appointmentscheduled`-`decisionmakerboughtin` | Auto-create | Tier 2 |
   | Verified email + current employment | Confirms current at target company | Open deal at `contractsent` | Hold for rep approval | Tier 3 |
   | Verified email + current employment | Profile not publicly accessible / 404 / private | Any | Hold ("verify before adding") | Tier 3 |
   | Verified email | LinkedIn shows departed | Any | Hold (route to Routine 9 next quarter) | Tier 3 |
   | Apollo email status NOT verified | (not checked) | Any | Skip silently — never source unverified | — |
   | Suppressed (invariant E) | — | — | Skip + log in "Suppressed" | — |
   | Customer-history account | Any | Any | Auto-create allowed (additive) — flag for rep visibility | Tier 2 |

5. **Owner + segment cascade:** New contact's `hubspot_owner_id` = associated company's `hubspot_owner_id` (territory-manager). New contact's `customer_segment` = associated company's `customer_segment`.

6. **Surface remaining gaps:** Persona slots where no candidate was found (Apollo returned 0 verified-email matches for the role at this company) → "Rep action: source manually" subsection of the report. Include the company name + persona role + segment so the rep can target manually.

## Safety Tiers

(Summarized — full table in step 4.)

| Outcome | Tier |
|---|---|
| Verified Apollo + LinkedIn-confirmed contact, deal pre-`contractsent` | Tier 2 (auto-create + flag) |
| Same, but at customer-history account | Tier 2 (additive, flag for rep) |
| Same, but deal at `contractsent` | Tier 3 (hold for rep) |
| Apollo email not verified | Skip — never auto-source unverified |
| LinkedIn shows departed | Tier 3 (route to Routine 9) |
| Persona gap with no candidates found | Surface as "rep action: source manually" |

## Caps & Budgets

- **Account scan:** all Tier 1+2 accounts (uncapped read, paginated).
- **Persona audit:** up to 4 persona slots checked per account (Technical Champion / Business Sponsor / Economic Buyer / Procurement).
- **Priority order for persona search (when Apollo cap is binding):** open-deal accounts within Tier 1+2 always processed first regardless of audit recency; then Tier 1 accounts (oldest-persona-audited first); then Tier 2 (oldest-persona-audited first).
- **Contact create cap:** ~62 contacts per run (HARD cap, derived from the 250 Apollo cr/run budget at ~4 cr/contact). First-run drain may exceed; defer remainder to next Friday — the audit is idempotent so persona gaps reappear next run.
- **Apollo credits:** **HARD cap 250 credits per run** (sub-cap from the 6,000-credit/month global Apollo budget; see `skills/crm-guardian/SKILL.md` "Apollo monthly budget" section). 250 cr/week × 4.3 weeks = 1,075/month max, fits the global allocation. Mode 3 is Apollo-heavy: ~3-5 credits per persona search (people search + match). 62 contacts × 4 credits avg = 248. **Pre-flight monthly budget check: at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 250) <= 6000`. If `remaining < 250`, scale down to `remaining`-credit budget (process priority order until budget exhausted) and surface deferred personas in the Slack DM.** Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded` from Apollo.
- **HubSpot writes:** **Batch cap: 10 contacts per `manage_crm_objects.createRequest` call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. At ~62 contacts/run that's ~7 batched calls per run. Exponential backoff (1s → 2s → 4s) on HTTP 429; halve to 5/batch on 3+ consecutive 429s.
- **LinkedIn fetches:** ~1 web_fetch per Apollo hit (validation). Soft cap 500 fetches per run.

## Output

- **Subject:** `CRM Guardian — Persona Fill (Weekly) — [YYYY-MM-DD] — [N] contacts created, [M] Tier 3 held, [K] manual sourcing needed`
- **Hero:** Tier 1+2 accounts scanned, persona gaps detected, contacts created (Tier 2), Tier 3 holds, suppressions, Apollo credits consumed.
- **Created (Tier 2) — by rep territory:**
  - Tim Lieto (East): account name | persona role | new contact (firstname, jobtitle, email)
  - Ken Cunningham (West): same
  - Tim Ziemer (International): same
  This per-rep grouping helps Cooper preview which contacts will appear on each rep's dashboard.
- **Tier 3 held:** unverified Apollo, LinkedIn-departed, deal-protected at `contractsent`, customer-history (informational).
- **Suppressed:** suppression-check failures (opt-out, hard-bounced, duplicate, flagged) — count + reasons.
- **Rep action — manual sourcing needed:** persona gaps with zero candidates — companies + missing personas, route to source manually via LinkedIn Sales Nav or referrals.
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch. (For Routine 8: prior-run "Apollo reveal pending" candidates from before the auto-create flow was wired up should be drained on the first run after that fix lands — they should now auto-create, not be re-surfaced.)
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 8: Persona Fill | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:bust_in_silhouette: *CRM Guardian — Persona Fill (Weekly)* — [YYYY-MM-DD] — [N] created, [M] Tier 3, [K] manual`
- **Body format:** Slack mrkdwn. Per-rep tables in triple-backtick code blocks (so Cooper can scan + forward selectively).
- **Thread prefix:** `CRM Guardian — Persona Fill (Weekly) —` for Slack search grouping.
- **Character limit:** 5,000 per text element. Hero + per-rep summaries as parent message; full Tier 2 + Tier 3 + Suppressed tables as threaded replies via `thread_ts` if cap exceeded (likely on first-run drain).
- On send failure: retry once with exponential backoff (1s → 2s). If still failing, log in Errors and rely on routine-platform fallback. No email fallback.
