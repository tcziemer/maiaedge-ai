# CRM Guardian — Routine 6: Territory & Hygiene Sweep

Daily, 1:00 AM ET — runs FIRST each day so the other routines operate on clean state. You validate territory ownership, auto-migrate deprecated enum values, fill gap fields, cascade contact owners, and flag clear-cut junk contacts. Apollo is used only for state verification when a company is missing state or the enrichment is 120+ days stale.

**CRM scale (as of 2026-04-24):** 3,489 companies, 13,309 contacts. Cooper-owned placeholder accounts: **0** (already clean). Deprecated `AI - Colocation Operator` enum values: **0** (already migrated). This routine is a safety-net sweep — steady-state output should be mostly "All clean" with minor daily drift.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/crm-hygiene/SKILL.md` (Modes 2-11 — this routine runs the audit-and-fix modes; duplicate merges are deferred to Routines 3+5)
- `skills/territory-manager/SKILL.md` (Mode 1 Full Territory Audit, contact owner cascade, Apollo state verification, strategic exception detection)

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/hubspot/territory-model.md`
- `context/hubspot/contact-schema.md`
- `context/hubspot/deals-schema.md`

**Connected tools:** HubSpot MCP, Apollo MCP (state verification only), Slack MCP (report delivery via `slack_send_message`).

## Run-Time Invariants

### A. Timezone
America/New_York.

### B. Skip Already-Flagged
Exclude `customer_segment = "Flagged for deletion"` companies from territory / hygiene operations (Routine 4 owns them).

### C. Customer Protection
Closed-won companies are protected from segment/tier changes — but territory/owner corrections remain Tier 1 (reps still need correct routing).

### D. Error Containment
Per-record try/except.

**Distinguish web_fetch failure modes when running the Field Resolution Ladder (state/country resolution, ladder step 2 is `web_fetch` on the company website footer):**

- **Proxy block (HTTP 403 with `x-deny-reason: host_not_allowed`)** → infrastructure failure, NOT a domain signal. Skip ladder step 2 (website fetch) and proceed directly to step 3 (LinkedIn About) and step 4 (WHOIS). Do NOT treat this as "state unresolvable" — the ladder still has remaining steps. If steps 3-4 also fail, Tier 3 hold (state genuinely unknown).
- **DNS NXDOMAIN / parked-page / persistent destination 4xx-5xx** → real dead website. Note this in the audit but continue ladder steps 3-4 (LinkedIn / WHOIS may still resolve state).
- **Timeout** → retry once with 5-sec backoff; if still times out → skip step 2, proceed to step 3.
- **Captcha / Cloudflare** → skip step 2, proceed to step 3.

### E. Default to Tier 3 When Uncertain
State still blank after Apollo verification → Tier 3 hold. Strategic / leadership-assigned owner overrides → skip (territory-manager detects these).

### F. Idempotency
All writes idempotent. A second same-day run finds clean state and returns "All clean" (minor).

### G. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest).
- `customer_segment = "Enterprise"` is MSP/Aggregator (legacy). Do not "fix" it.
- AI Colo: `Data Center Colo Provider` + `AI Signals - colo`. Auto-migrate deprecated `AI - Colocation Operator` (crm-hygiene Mode 7).
- No em dashes in customer-facing field values.

### H. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:**
- Company: `hubspot_owner_id` per territory-model, `state`, `country`, `customer_segment` (deprecated enum migration ONLY — e.g., `AI - Colocation Operator` → `Data Center Colo Provider`), `company_sub_segment` (cascade from segment migration), `account_tier` (cascade).
- Contact: `hubspot_owner_id` (cascade from corrected company owner), `customer_segment` (sync from company), `flagged_for_deletion = true` on Mode 11 junk.

**Hard stops:** MaiaEdge's own record (ID 124293230301). Never set `customer_segment = "Flagged for deletion"` (Routine 3 owns that specific transition).

## Workflow

Order matters — territory runs first so downstream hygiene operates on correct owners.

### Step 1: Territory Audit (territory-manager Mode 1)

1. Pull all active companies (`customer_segment != "Flagged for deletion"`).
2. For each company:
   - If `state` is populated and owner mismatches state-to-owner mapping → correct owner (Tier 1). Cascade contact owners.
   - If `state` is blank OR `last_enriched_date` is 120+ days stale: call **Apollo `apollo_organizations_enrich`** for state/country. Apollo is authoritative. Write the refreshed state + country (Tier 1 if write succeeds, Tier 2 if the account has an open deal and the state overwrite shifts territory).
   - **If state is still blank after Apollo → run the Field Resolution Ladder defined in `skills/company-enrichment/SKILL.md` (steps 2-4: website → LinkedIn About → WHOIS).** Write at the confidence level the ladder yields (Tier 1 from website, Tier 2 from LinkedIn, Tier 3 from WHOIS). Only if all four ladder steps return null → Tier 3 hold. The previous "Apollo blank → manual research" pattern lost 100% of the 3 records on 2026-04-24 (Shaun Telecom, Surf USA Mobile, kiocompany.com); the ladder recovers most of them.
   - Strategic exceptions (per territory-manager detection) → skip.
   - Cooper-owned accounts with known state → re-route per territory-model (Tier 1).
3. For every corrected owner: execute territory-manager Contact Owner Cascade. Contact writes are Tier 1.

### Step 2: Deprecated Enum Migration (crm-hygiene Mode 7)

1. Find companies where `customer_segment = "AI - Colocation Operator"`.
2. Migrate to `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"` (Tier 1).
3. Execute segment-classification Segment Change Cascade Rules (re-derive tier, confidence).

### Step 3: Gap Filling (crm-hygiene Modes 3, 8) — auto-drain mode

This routine no longer surfaces gap fields as Tier 3 holds when the cascade rules can fill them deterministically. The 2026-04-24 hygiene run found 1,451 records missing `account_tier` and 748 missing `company_sub_segment` and acted on zero. The new behavior auto-fills via cascade — both fields are deterministic from `customer_segment` per segment-classification's cascade rules.

1. **Mode 3 — Missing critical fields:**
   - Missing `customer_segment` with a usable domain → surface as Tier 3 ("belongs in Routine 1 or 2 — deferred"). Do NOT enrich here; enrichment is owned by Routines 1 + 2.
   - Missing `state` → already covered by Step 1 Apollo verification + Field Resolution Ladder.
   - Missing `hubspot_owner_id` with known `state` → apply territory mapping (Tier 1). Drain cap: 200/run.
   - **Missing `account_tier` where `customer_segment` is populated** → run segment-classification cascade to derive tier, write at Tier 1. Drain cap: **400/run** (drains 1,451 backlog in ~4 days).
   - **Missing `company_sub_segment` where `customer_segment` is populated** → run segment-classification cascade to derive sub-segment, write at Tier 1. Drain cap: **250/run** (drains 748 backlog in ~3 days).

2. **Mode 8 — Contact-level hygiene:**
   - Auto-sync contact `hubspot_owner_id` and `customer_segment` when they mismatch the parent company (Tier 1). No drain cap (cascade write).
   - **Orphaned contacts (995 in 2026-04-24 run)**: for each orphan, extract email domain. If the domain matches an existing HubSpot company by exact domain, auto-associate the contact to that company at Tier 2 (applied + flagged so Cooper can spot-check). If no domain match → leave orphaned, surface count in report. Drain cap: **300/run** (drains 995 backlog in ~4 days).
   - Missing-email contacts → report only (no auto-fix path that doesn't burn Apollo credits — out of scope here).

### Step 4: Stale-record drain (crm-hygiene Modes 4, 5, 6, 9)

- **Mode 4 — Stale records (no activity 90+ days):** Report only — no auto-action. Stale doesn't mean junk; the contact may be valuable but cold. Surface counts.
- **Mode 5 — Incomplete enrichment tracking:** Surface stale-enrichment candidates that Routine 2 will pick up. Counts only.
- **Mode 9 — Stale NEW leads (the 9,811 backlog from 2026-04-24):** Auto-advance `hs_lead_status` from `NEW` to `OPEN` for every contact where ALL of: `createdate > 14 days ago`, `hs_lead_status = NEW`, no logged sales activity (`notes_last_contacted IS EMPTY` and `hs_email_last_send_date IS EMPTY`), no open deal association, `hs_email_optout != true`. Tier 1 auto-write. Drain cap: **1000/run** (drains 9,811 backlog in ~10 days). Reasoning: NEW means "imported but never touched"; after 14 days the import is stale and OPEN better reflects reality. Reps can still re-stage to NEW if they choose to actively work the lead.
- **Mode 6 — Completeness health score:** Include in report hero.

### Step 5: Contact Deletion Flagging (crm-hygiene Mode 11)

Auto-flag clear-cut junk contacts. Full criteria per Mode 11; protection filters apply (`hs_email_optout`, customer lifecyclestage, open deals, open POC).

**Tier 1 auto-flags:**
- Hard-bounced emails (`hs_email_hard_bounce_reason_enum` populated).
- Generic spam patterns (`noreply@`, `no-reply@`, `donotreply@`, `mailer-daemon@`).
- Test / placeholder addresses (`test@test`, `@example.com`, `@yourdomain`, `firstname` and `lastname` both "test").
- Contacts associated ONLY to `Flagged for deletion` companies with zero open deals.

**Tier 2 auto-flags (applied + surfaced):**
- No email / phone / mobilephone / company AND `createdate > 180 days` AND `lifecyclestage` in {blank, subscriber, lead} AND zero deals AND no sales-activity timestamp.

**Never-flag:**
- Contacts < 30 days old with no contact info → route to Routine 5 or persona fill, not here.

### Step 6: Health Score

Calculate overall CRM health score per crm-hygiene Mode 6 and include in report hero.

## Caps & Budgets

- **Record cap:** full-table sweep (3,489 companies) for read; no per-record write cap (this is a low-write routine in steady state). Full read = ~35 pages × 1s = ~35s.
- **Apollo credits:** **HARD cap 25 Apollo `apollo_organizations_enrich` calls per run** (state-verification only — most accounts have populated state and won't need Apollo). Sub-cap from the 6,000-credit/month global Apollo budget; 25/day × 30 days = 750/month max, fits the global allocation. **Pre-flight monthly budget check: at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 25) <= 6000`. If not, skip Apollo state verification entirely for this run and surface the deferred state-blank/state-stale companies as Tier 3 holds.** Prioritize Apollo state-verification on (a) accounts with open deals, then (b) Tier 1 accounts, then (c) Tier 2 — within the 25-call budget. Hard stop on explicit Apollo rate-limit error.
- **HubSpot writes:** use `manage_crm_objects.updateRequest` in batch mode. **Batch cap: 10 `objects` per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. Owner cascades to contacts should still batch all contacts per company affected, but split across multiple 10-object calls if a single company has more than 10 contacts. **Soft cap 2,200 writes/run** (Step 1 territory: ~50; Step 3 tier-fill: 400; Step 3 sub-segment-fill: 250; Step 3 orphan-associate: 300; Step 4 stale-NEW advance: 1000; Mode 11 contact flags: ~200) → expect ~220 batched calls per run at cap. Well under HubSpot's 250K/day rate limit. Exponential backoff (1s → 2s → 4s) on 429; halve to 5/batch on 3+ consecutive 429s.
- **Deal-status checks:** when checking deal protection, use boolean `hs_is_closed_won` + `hs_is_closed_lost` flags. Do NOT rely on `dealstage` string matching — HubSpot pipelines use custom numeric IDs (e.g. `3401264867` = Closed Won in MaiaEdge's custom pipeline) that would be missed by string comparison.
- **Duplicate detection:** explicitly deferred — Routine 3 owns company dedup, Routine 5 owns contact dedup. This routine does not run crm-hygiene Mode 2.

## Output

- **Subject:** `CRM Guardian — Territory & Hygiene — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Hero:** health score, owner corrections applied, deprecated enums migrated, contact flags applied, Apollo credits consumed.
- **Territory corrections (Tier 1/2):** company ID, old owner → new owner, reason (state mapping / Apollo-refreshed state / Cooper-owned re-route).
- **Enum migrations (Tier 1):** companies migrated from deprecated values.
- **Contact hygiene:** owner cascades, segment syncs, Mode 11 flags (Tier 1 + Tier 2 counts).
- **Stale / completeness reports:** counts from Modes 4, 5, 6, 9 — informational, no action taken.
- **Tier 3 held:**
  - State still blank after Apollo.
  - Missing segment on accounts with domains (deferred to Routine 1/2).
  - Strategic-exception owner overrides (surfaced for visibility, not action).
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 6: Territory & Hygiene | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper. This routine's report typically arrives first each day (~1:30 AM ET).

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:broom: *CRM Guardian — Territory & Hygiene* — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Body format:** Slack mrkdwn. Health score prominent in hero. Correction tables in triple-backtick code blocks. Prefix every run `CRM Guardian — Territory & Hygiene —` for Slack search grouping.
- **Character limit:** 5,000 per text element. Steady-state output should fit well under the cap (most days will be "All clean" or minor drift).
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback.
