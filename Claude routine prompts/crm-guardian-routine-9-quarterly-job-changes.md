# CRM Guardian — Routine 9: Quarterly Job Change Detection

Quarterly, on the 1st of January / April / July / October at 9:00 AM ET (after the 6 daily routines complete). You scan contacts at Tier 1+2 accounts and contacts at any account with an open deal, detect job departures via Apollo + LinkedIn cross-check, surface departures for rep visibility (no auto-write to the existing departed contact), and auto-create verified replacements at the new role per Routine 8's persona-fill methodology. Late-stage deal-protected accounts hold replacements for rep approval.

**CRM scale (as of 2026-04-24):** ~3,000-4,000 contacts at Tier 1+2 accounts + open-deal contacts. Quarterly job-change rate is 5-10% across the contact base, so each run typically detects ~150-400 job changes. First quarterly run will be largest because no prior run has cleared the historical drift.

## Repo

**Orchestrator reference (for invariants + safety tiers):**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/contact-discovery/SKILL.md` (Mode 4 job change detection — full methodology; Mode 3 persona fill for replacements)
- `skills/territory-manager/SKILL.md`

**Context:**
- `context/hubspot/contact-schema.md` (persona framework, marketable_status default)
- `context/hubspot/property-schema.md`
- `context/hubspot/territory-model.md`
- `context/hubspot/deals-schema.md` (deal-stage gate for late-stage protection)

**Connected tools:** HubSpot MCP, Apollo MCP, Slack MCP, web_fetch (LinkedIn validation).

## Run-Time Invariants

### A. Timezone
America/New_York. Quarter starts: Jan 1, Apr 1, Jul 1, Oct 1 (Eastern calendar dates).

### B. Day-Gate
Run only when today's ET date is one of: `01-01`, `04-01`, `07-01`, `10-01`. Otherwise exit cleanly with a one-line Slack DM `:arrows_clockwise: *CRM Guardian — Job Changes (Quarterly)* — [YYYY-MM-DD] — not a quarter-start run, skipping.`

### C. Skip Already-Flagged
Companies + contacts with deletion flags are out of scope.

### D. Customer Protection
Customer-history accounts (any closed-won deal): detect job changes (still useful — AMs need to know who's left), but escalate any auto-create of a replacement to Tier 3. Humans approve customer-side persona changes because relationship continuity matters more than throughput here.

### E. Suppression Check (mandatory before every replacement create)
Same as Routine 8 invariant E — opt-out, hard-bounced, flagged-for-deletion, duplicate-email-at-company, duplicate-email-globally. If suppressed → skip and log.

### F. Departure Handling — Read-Only
Detected departures do NOT auto-modify the existing departed contact. The contact stays where it is in HubSpot; the routine's Slack DM is the audit trail. The replacement (if auto-created) is what shows up as a new HubSpot record.

**Why read-only on the existing contact:** HubSpot's `lifecyclestage` is rep-controlled; the existing contact may have closed-deal history we want to preserve for AM reference; and the contact may still be reachable at their new email if they moved within the network. Marking "departed" on the existing contact is a manual rep call.

### G. Error Containment + Idempotency
Per-contact try/except. Re-running same-day finds replacements already created (suppression check on existing email = no-op) and produces minimal new work. The departure detections themselves are read-only and reproducible.

### H. Default to Tier 3 When Uncertain
Apollo says current employer is X but LinkedIn 404s or is private → Tier 3 hold ("verify before treating as departed"). Apollo email unverified → never source as replacement.

### I. MaiaEdge Gotchas
[Same as Routine 8: tier inverted, lifecyclestage no `evangelist`, hs_marketable_status = "false" required.]

### J. Write Authorization
Every `manage_crm_objects` create call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized creates:** new Contact with same properties as Routine 8 (firstname, lastname, email, jobtitle, phone, linkedin_url, lifecyclestage=`lead`, hs_marketable_status=`"false"`, hubspot_owner_id cascaded, customer_segment synced, associated to company).

**Hard stops:**
- MaiaEdge own record (124293230301).
- Open deals at `dealstage = contractsent` (replacement creation → Tier 3).
- Customer-history accounts (any closed-won deal) — replacement creation → Tier 3.

## Workflow

1. **Build target contact set:** HubSpot `search_crm_objects` on CONTACT with:
   - Associated company `account_tier IN ('tier_1', 'tier_2')` OR associated company has any open deal (any deal where `hs_is_closed_won = false` AND `hs_is_closed_lost = false`, regardless of company tier).
   - `flagged_for_deletion != true`.
   - Paginate fully.

2. **For each contact, run contact-discovery Mode 4 (job change detection):**
   - Apollo `apollo_people_match` by `email` — returns Apollo's view of the person's current employer + title.
   - LinkedIn cross-check via `web_fetch` on the contact's `linkedin_url` if populated. Look for current company line + recent role title.
   - Compare Apollo's current_employer to HubSpot's company association:
     - Match → contact is current. Skip.
     - Different → contact has departed. Mark `DEPARTED`, capture (a) old role at old company per HubSpot, (b) new role at new company per Apollo + LinkedIn.
     - Apollo says departed but LinkedIn doesn't load → Tier 3 hold ("verify").
     - Apollo says current but LinkedIn shows departed → Tier 3 hold ("conflicting sources").

3. **For each DEPARTED contact:**
   - Surface the departure in the Slack DM (no HubSpot write to the existing contact).
   - Run **contact-discovery Mode 3 (persona fill)** on the now-vacated persona slot at the original company to find a replacement (same methodology as Routine 8: Apollo verified-email + LinkedIn cross-check + suppression check).
   - Replacement → tier per the table below.

4. **Tier assignment for replacements:**

   | Replacement found? | Verified? | Account state | Action | Tier |
   |---|---|---|---|---|
   | Yes | Apollo verified + LinkedIn confirms | No open deal OR deal `appointmentscheduled`-`decisionmakerboughtin` | Auto-create | Tier 2 |
   | Yes | Same | Deal `contractsent` | Hold for rep | Tier 3 |
   | Yes | Same | Customer-history (any closed-won deal) | Hold for rep | Tier 3 |
   | Yes | Apollo only, LinkedIn not validated | Any | Hold ("verify") | Tier 3 |
   | No replacement found | — | — | Surface as "rep action: source manually" | — |

5. **Cross-link in report:** for each departure + replacement pair, show both contact IDs side-by-side so reps can manually mark the old contact as departed if they want (in the HubSpot UI).

6. **Special case — DEPARTED contact had open-deal association:** the departure is high-impact (the deal's primary contact just left). Surface this prominently in the rep section: "Open deal X has lost contact Y (departed to Z); replacement W has been created/held."

## Safety Tiers

(Summarized — full table in step 4.)

| Scenario | Tier |
|---|---|
| Departure detected, surfaced in report only | (informational, not a tier) |
| Replacement found, verified, non-deal-protected | Tier 2 auto-create |
| Replacement found, verified, deal pre-`contractsent` | Tier 2 |
| Replacement found, verified, deal at `contractsent` | Tier 3 |
| Replacement found, customer-history account | Tier 3 |
| Replacement Apollo-only (no LinkedIn validation) | Tier 3 |
| No replacement found | Rep action — manual sourcing |

## Caps & Budgets

- **Contact scan:** uncapped HubSpot read on Tier 1+2 + open-deal contacts (paginated, ~30-40 pages × 1s = ~40s). The Apollo cap below — not the read cap — is what limits work per run.
- **Priority order for Apollo `apollo_people_match` calls (Apollo cap binds the actual scan):**
  1. **Open-deal contacts** (any contact at any company with `hs_is_closed_won = false` AND `hs_is_closed_lost = false` deal) — always processed, never skipped. Estimated ~50 contacts at current scale.
  2. **Tier 1 account contacts** — processed in `notes_last_contacted DESC` order (most-engaged first), then by `lastmodifieddate DESC`.
  3. **Tier 2 account contacts** — round-robin by oldest-Apollo-checked first. Track this via a sliding window: contacts checked in the last 4 quarters skip until they age out.
- **Apollo credits:** **HARD cap 750 credits per run** (sub-cap from the 6,000-credit/month global Apollo budget — quarterly cadence means ~250/month effective). Mode 4 burns `apollo_people_match` per scanned contact (~1 credit) + Mode 3 persona-fill on each detected departure (~3-5 credits). At 750 budget: ~600 contacts scanned + ~30 departures × 5 cr each (= 150 cr for replacements) = 750 total. **Pre-flight monthly budget check: at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 750) <= 6000`. If not, scale down to `remaining` budget and surface deferred contacts (next priority tier after current cutoff) in the Slack DM.** Hard stop on explicit Apollo rate-limit error.
- **Coverage cycle:** at 750 contacts scanned/quarter on a ~3,500 Tier 1+2+open-deal contact base, full base cycles in ~5 quarters (~15 months). Open-deal contacts (priority 1) get covered every quarter — that's the high-value subset. Tier 2 contacts get covered ~once a year. Acceptable for a slow-moving signal (job changes typically discoverable within 90-180 days of the move).
- **Replacement-create cap:** 100 per run (HARD cap). Departures detected beyond this → "rep action: source replacement manually" in the Slack DM.
- **HubSpot writes:** **Batch cap: 10 `objects` per `createRequest` call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. At the 100-replacement run cap that's ~10 batched calls. Exponential backoff (1s → 2s → 4s) on HTTP 429; halve to 5/batch on 3+ consecutive 429s.
- **LinkedIn fetches:** ~1 per scanned contact + ~1 per replacement candidate. Soft cap 1,500 fetches per run (down from 5,000 to align with the lower contact-scan cap).

## Output

- **Subject:** `CRM Guardian — Job Changes (Quarterly) — [YYYY-MM-DD] — [N] departures, [M] replacements created, [K] Tier 3 held`
- **Hero:** contacts scanned, departures detected, replacements created (Tier 2), Tier 3 holds, manual-sourcing items, Apollo credits consumed (% of monthly budget).
- **Departures (high-priority — open-deal exposure):** company | departed contact | new employer per Apollo+LinkedIn | open deal name + stage | replacement status (created / Tier 3 / not found).
- **Departures (Tier 1+2 accounts, no open deal):** company | departed contact | new employer | replacement status.
- **Replacements created (Tier 2) — by rep territory:** per-rep grouping like Routine 8.
- **Tier 3 held:** customer-history, contract-stage, Apollo-only-no-LinkedIn, conflicting-sources.
- **Rep action — manual sourcing needed:** companies where the persona slot is now vacant and Mode 3 found no replacement.
- **Suppressed:** suppression-check failures + reasons.
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 9: Job Changes (Quarterly) | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:arrows_clockwise: *CRM Guardian — Job Changes (Quarterly)* — [YYYY-MM-DD] — [N] departures, [M] replacements`
- **Body format:** Slack mrkdwn. Per-rep tables in triple-backtick code blocks. Lead with the open-deal-exposure section — these are time-critical (a deal's primary contact just left).
- **Thread prefix:** `CRM Guardian — Job Changes (Quarterly) —` for Slack search grouping.
- **Character limit:** 5,000 per text element. First quarterly run will exceed — split into hero (open-deal exposures + Tier 1+2 departures count + replacement counts) as parent + threaded replies for full tables (one thread per: Departures Open-Deal / Departures Other / Replacements Created / Tier 3 Held / Manual Sourcing).
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback.
