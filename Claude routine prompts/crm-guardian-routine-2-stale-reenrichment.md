# CRM Guardian — Routine 2: Stale Account Re-Enrichment

Daily, 8:00 AM ET. You drain the stale-enrichment backlog — companies whose `last_enriched_date` is older than 120 days OR blank (with segment already populated) — so the full CRM rotates through re-enrichment on a 120-day cycle. You do NOT touch fresh accounts (blank segment → Routine 1) or any other maintenance work.

**Model:** Run on **Claude Opus 4.7** (or Opus 4.6 fallback). Re-enrichment requires deep reasoning over website diff detection (what changed since last enrichment), trigger-event detection (M&A, funding, leadership), segment cascade decisions (when a colo pivots to NeoCloud, when a fiber op gets acquired), and customer-protection logic on closed-won accounts. Sonnet/Haiku are not sufficient. Downstream cascade impact is the same as Routine 1: the weekly-signal-scan, persona fill, call recap, and rep prospecting all depend on accurate `customer_segment`, `account_tier`, and `recent_news_or_trigger_event` to do their work.

**CRM scale (as of 2026-04-24):** 3,489 companies total. After excluding ~379 flagged-for-deletion, ~3,110 are active. At 120-day rotation that is **26 accounts/day steady state**. The current stale pool is ~190 accounts; with the 100/day cap it drains in ~2 days, then the routine runs in steady state where most runs have < 30 candidates.

**Throughput mandate:** This routine MUST drain its full daily candidate batch (up to 100 records). Re-enrichment is the ONLY mechanism that catches accounts whose classification has shifted (colo → NeoCloud pivots, fiber op M&A, leadership changes, AI signal upgrades) — failing to process them means stale segment/tier/owner assignments propagate forward, breaking territory routing, persona fill targeting, and signal-scan account prioritization. Pre-score triage in Step 0 routes RE_ENRICH_LIGHT records (already-classified-as-Other / Partner Target / non-ICP at Tier 4-5) to a no-Apollo idempotency-bump path so the full 100-record batch can be processed within the runtime budget without burning the Apollo budget on records that won't change classification.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills:**
- `skills/company-enrichment/SKILL.md` (Step 0C re-enrichment mode + Stages 1-3)
- `skills/segment-classification/SKILL.md` (qualification gates, cascade rules)
- `skills/import-processor/SKILL.md` (enum mapping)
- `skills/territory-manager/SKILL.md` (state-to-owner re-derivation)
- `skills/edge-case-researcher/SKILL.md`

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/hubspot/territory-model.md`
- `context/core/icp-playbook.md`
- `context/core/segment-qualification.md`
- `context/segments/` (all segment cheatsheets)

**Connected tools:** HubSpot MCP, Apollo MCP, Slack MCP (report delivery via `slack_send_message`), web_search + web_fetch

## Run-Time Invariants

### A. Timezone
America/New_York for all date math. `last_enriched_date` comparisons use ET calendar dates.

### B. Skip Already-Flagged
Exclude `customer_segment = "Flagged for deletion"` from the candidate pool.

### C. Customer Protection
Companies with any closed-won deal (`hs_is_closed_won = true` or `dealstage = closedwon`) are protected. If re-enrichment proposes a segment downgrade from ICP to non-ICP, escalate to Tier 3 — do NOT auto-write the downgrade. A customer record briefly reclassifying as non-ICP is a classification re-evaluation signal, not a delete signal.

### D. Error Containment
Per-record try/except. Continue on failure; surface in report.

**Distinguish web_fetch failure modes — they route differently:**

- **Proxy block (HTTP 403 with `x-deny-reason: host_not_allowed` header, or any 4xx/5xx whose response body identifies the egress proxy rather than the destination)** → infrastructure failure, NOT a domain signal. Fall back to `web_search` for `"<domain> what is this site"` and/or `"<company name> <domain>"`. If web_search yields a clear identification → continue with Step 1 bucketing using web_search summaries in place of web_fetch text (one-confidence-tier penalty: HIGH→MEDIUM, MEDIUM→LOW). If web_search is ALSO inconclusive → AMBIGUOUS Tier 3 hold ("infrastructure: web_fetch blocked, web_search inconclusive") — **do NOT bump `last_enriched_date`** (we didn't actually verify anything; record stays in stale pool for next run).
- **DNS NXDOMAIN / `ENOTFOUND` / parked-page signature / persistent 4xx-or-5xx from the actual destination** → real dead domain → DEAD_DOMAIN bucket per the RE_ENRICH_LIGHT path. Bump `last_enriched_date` (the eviction is the resolution).
- **HTTP 5xx from actual destination** → retry once with 2-sec backoff. Persistent → Tier 3 hold (transient site outage; revisit next run, do NOT bump date).
- **Captcha / Cloudflare / bot challenge** → AMBIGUOUS / Tier 3 (do NOT bump date).
- **Timeout** → retry once with 5-sec backoff; if still times out → fall back to web_search (treat like a proxy block).
- **Critical for re-enrichment:** the LIGHT-path date-bump rule depends on this distinction. AMBIGUOUS-from-infrastructure = no date bump (record needs another shot). DEAD_DOMAIN-from-real-failure = date bump (eviction is resolution). The 120-day rotation only stays honest if these are kept separate.

### E. Default to Tier 3 When Uncertain
LOW / MANUAL_REVIEW confidence, conflicting Apollo vs. website data, boundary cases → no write, hold for Cooper.

### F. Idempotency
Set `last_enriched_date = today (ET)` on every successful enrichment — this is the authoritative rotation key. Never skip this write after a successful run; the next cycle depends on it. Safe to re-run same-day; idempotent output.

### G. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest).
- `customer_segment = "Enterprise"` = MSP/Aggregator (legacy).
- AI Colo: `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`. Auto-migrate deprecated `AI - Colocation Operator`.
- No em dashes in customer-facing fields.
- Category descriptor: "Carrier infrastructure" only.

### H. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"` on every manage_crm_objects call.

**Pre-authorized writes:** same as Routine 1 — `customer_segment` (EXCEPT "Flagged for deletion"), `company_sub_segment`, `account_tier`, `segmentation_confidence`, `last_enriched_date`, `hubspot_owner_id`, `state`, `country`, all enrichment narrative fields, plus `domain` (MISDOMAIN auto-correct path only — Tier 1 HIGH / Tier 2 MEDIUM, per the MISDOMAIN check in the RE_ENRICH_LIGHT path).

**Hard stops:** MaiaEdge's own record (ID 124293230301). Open deals at `contractsent` or later.

## Trigger Query

HubSpot `search_crm_objects` on COMPANY, using two filter groups OR-combined:

**Filter group A — stale enrichment (120+ days old):**
- `last_enriched_date` operator `LT` with value = today(ET) - 120 days, formatted as `YYYY-MM-DD`
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`

**Filter group B — never enriched but segment populated:**
- `last_enriched_date` operator `NOT_HAS_PROPERTY`
- `customer_segment` operator `HAS_PROPERTY`
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`

**Explicitly NOT in scope** (belongs to Routine 1): records where `customer_segment IS EMPTY`. Those are fresh-enrichment candidates, not re-enrichment.

**Sort:** `last_enriched_date ASCENDING` (oldest first; records with no value sort earliest on HubSpot's search). This drains the staleest backlog first. Page through up to 100 qualifying records — this is the full daily processing batch, not a sample.

## Workflow

### Step 0 — Pre-score triage (routing helper, NOT a substitute for domain fetch)

Re-enrichment is the highest-volume Apollo consumer in steady state. Pre-score routes records by depth-of-research, but **every record still gets its domain fetched and verified** before any classification write. Pre-score doesn't replace the Non-ICP Eviction Rule (see `skills/crm-guardian/SKILL.md` → "Non-ICP Eviction Rule") — it just decides whether to run the full enrichment pipeline + Apollo or the lighter eviction-decision path.

Take the candidate list (up to 100 records: `id`, `name`, `domain`, current `customer_segment`, current `account_tier`) and triage in one LLM pass:

| Bucket | Definition | Step 1 path |
|---|---|---|
| `RE_ENRICH_FULL` | Already classified as ICP (Colocation / Fiber / NeoCloud / Network Operator / MSP) AT ANY TIER, OR currently `customer_segment IS EMPTY` with a usable domain | Full re-enrichment pipeline (Stages 1-3 + Apollo). Apply Non-ICP Eviction Rule if classification flips to non-ICP. |
| `RE_ENRICH_LIGHT` | Already classified as `Other`, `Unknown`, `Dark Fiber - Commercial Enterprise`, or `Enterprise-CustomerSegment`, AND `account_tier` in {TIER_4, TIER_5, UNRANKED} | Eviction-decision path (no Apollo): fetch domain, apply Non-ICP Eviction Rule decision tree. **Most "Other" records will resolve to PARTNER_KEEP (bump date) or HARD_DELETE (flag for eviction).** This is where stale Tier 5 pollution gets cleaned up. |
| `MAYBE_RECLASSIFY` | Classified as non-ICP but Cooper or recent runs flagged the classification as questionable (e.g., MetroNet currently UNQUALIFIED but is a real Tier 2 fiber operator), OR domain looks ICP but record is stale | Full pipeline (treat like `RE_ENRICH_FULL`) |
| `RE_ENRICH_DEFER` | Already classified as `Flagged for deletion` (shouldn't be in the pool but defensive check) | Skip — record is already evicted. |

Surface bucket distribution in the Slack DM hero. The `RE_ENRICH_LIGHT` path is the throughput lever AND the eviction lever — it drains the rotation pool without consuming Apollo credits AND actively removes confirmed non-partner non-ICP records that have been polluting the CRM as Tier 5 noise.

### Step 1 — Path execution (every record, by bucket)

**Every candidate gets its domain fetched** before any classification write. The Non-ICP Eviction Rule (see `skills/crm-guardian/SKILL.md`) is the canonical decision tree for non-ICP records. Path differs by bucket.

#### `RE_ENRICH_FULL` + `MAYBE_RECLASSIFY` records — full re-enrichment

For each candidate (no separate cap — share the 100-record total batch):

1. Run **company-enrichment Step 0C** (re-enrichment prep: diff check against current HubSpot state, detect material changes).
2. Run company-enrichment **Stages 1-3** (website-first adaptive enrichment, includes mandatory domain fetch).
3. Run **Apollo `apollo_organizations_enrich`** — authoritative source for refreshed `state`, `country`, industry, employee count, revenue, funding. Apollo wins when it disagrees with stale HubSpot values.
4. Run **segment-classification** → verdict + confidence.
5. **Apply Non-ICP Eviction Rule decision tree** (per SKILL.md):
   - If verdict is ICP → continue to step 6.
   - If verdict is non-ICP and matches PARTNER_KEEP keep-list (Cisco, Dell, AWS, Accenture, Gartner, Megaport, Datum, etc.) → write `customer_segment = "Other"`, `account_tier = TIER_5`, populate `account_brief` with `[Routine 2] [YYYY-MM-DD]: Partner Target keep — [reason]`. Apply Completeness Gate per step 7 below. Skip steps 8-9 (no cascade needed).
   - If verdict is non-ICP and NOT a PARTNER_KEEP candidate → write `customer_segment = "Flagged for deletion"`, populate `account_brief` with `[Routine 2] [YYYY-MM-DD]: Eviction rule applied — [discovered category] (re-enrichment confirmed non-ICP, non-partner)`. Tier 2 (auto-flag + surface). Apply Completeness Gate per step 7. Skip steps 8-9.
   - If verdict is AMBIGUOUS / LOW / MANUAL_REVIEW → run **edge-case-researcher**; if still uncertain → Tier 3 hold (do NOT bump `last_enriched_date` — record stays unresolved until Cooper acts).
6. Apply **import-processor** enum mapping.
7. **Completeness Gate (MANDATORY — added 2026-04-28 per Cooper):** Before writing enrichment fields OR `last_enriched_date`, verify all REQUIRED fields for this record's classification outcome are populated per the Mandatory Fields table in `skills/company-enrichment/SKILL.md` → "Completeness Gate Before `last_enriched_date` Write". **`last_enriched_date` is the LAST field written and is ONLY written if the gate passes.** A failed gate means partial enrichment — write whatever fields ARE available, but DO NOT bump `last_enriched_date`. The record stays in the stale pool for next-run retry. Flag in Slack DM under "Partial Enrichment — held for next run" with company ID + missing fields + reason. **This is critical for re-enrichment specifically:** historical bug pattern was bumping `last_enriched_date = today` while leaving enrichment fields blank, which removed the record from the stale pool for 120 days while it was actually still unenriched. The 120-day rotation depends on `last_enriched_date` being honest.
8. **Write enrichment fields to HubSpot.** If gate passed: full batch write including `last_enriched_date = today (ET)`. If gate failed: partial write of resolved fields ONLY; `last_enriched_date` stays at its prior value (could be blank or 120+ days old — both indicate the record needs re-enrichment).
9. Re-derive `hubspot_owner_id` from refreshed `state` per **territory-manager**. **If Apollo returned null on `state` or `country`, run the Field Resolution Ladder defined in `skills/company-enrichment/SKILL.md` (Apollo → website → LinkedIn About → WHOIS) before flagging Tier 3.** Tier 1 if state resolved at HIGH confidence; Tier 2 if state changed on a deal-protected account; Tier 3 hold only if all four ladder steps return null. NOTE: state resolution must happen BEFORE the Completeness Gate runs in step 7, since `state` and `hubspot_owner_id` are REQUIRED gate fields for ICP records.
10. If `customer_segment` changed: execute **segment-classification Segment Change Cascade Rules** → re-derive sub-segment, tier, confidence, infrastructure_profile; sync segment to associated contacts (Tier 1).

#### `RE_ENRICH_LIGHT` records — eviction-decision path (NO Apollo)

These are records currently classified as `Other`, `Unknown`, or non-ICP enterprise at low tiers. The point of this path is to verify each is STILL a legitimate keeper (Partner Target) or finally flag-for-deletion the ones that aren't. Stop letting Tier 5 sludge sit in the CRM forever.

For each candidate:

1. `web_fetch` `https://[domain]` — read `<title>`, meta description, H1, About blurb, footer.
2. If thin/ambiguous: `web_fetch` `https://[domain]/about` (one extra fetch).
2a. **MISDOMAIN check (BEFORE applying eviction rule).** If the entity at the domain differs from the HubSpot `name` AND the HubSpot name searches cleanly to its own canonical domain, this record is a MISDOMAIN, not a stale non-ICP. Run R0 Step 1c discovery (`web_search` `"<HubSpot name>" official website` + validation `web_fetch` on the candidate URL). On HIGH confidence: write `domain = <discovered>` (Tier 1), `account_brief = "[Routine 2] [YYYY-MM-DD]: corrected domain from \"[old]\" to \"[new]\" (old domain served [other entity]); re-routing for full re-enrichment."`. Re-route to RE_ENRICH_FULL path with the corrected domain — the FULL-path Completeness Gate governs the `last_enriched_date` write (do NOT bump in the LIGHT path). On MEDIUM: same writes Tier 2. On LOW: skip MISDOMAIN, continue to step 3.
2b. **MISDOMAIN check on web_fetch failure.** If step 1's web_fetch returned DNS NXDOMAIN / parked-page / persistent destination 4xx-5xx (real dead domain) BUT the HubSpot name searches cleanly to a real business with its own canonical domain → MISDOMAIN. Same Step 1c discovery + re-route as 2a. This is the case where a previously valid domain has died and the company has moved.
3. Apply Non-ICP Eviction Rule decision tree:
   - **PARTNER_KEEP** (matches keep-list — hyperscaler, major IT OEM, major SI, major analyst, named channel partner): write `account_brief = "[Routine 2] [YYYY-MM-DD]: Re-verified Partner Target keep — [reason]"`, bump `last_enriched_date = today (ET)`. Tier 1. (Verification = web_fetch succeeded AND PARTNER_KEEP keep-list category confirmed.)
   - **HARD_DELETE** (confirmed non-ICP, NOT on keep-list): write `customer_segment = "Flagged for deletion"`, `account_brief = "[Routine 2] [YYYY-MM-DD]: Eviction rule applied — [discovered_entity] ([category]) — was previously classified as [old_segment]"`. Tier 2 auto-flag + surface. Bump `last_enriched_date = today (ET)` (the eviction itself is the resolution).
   - **DEAD_DOMAIN**: write `customer_segment = "Flagged for deletion"`, `account_brief = "[Routine 2] [YYYY-MM-DD]: Domain dead/parked ([domain]) — was previously classified as [old_segment]"`. Tier 2. Bump `last_enriched_date = today (ET)` (the eviction is the resolution).
   - **Surprise ICP** (the company has pivoted — e.g., a former IT consultancy now operates a NeoCloud): re-route to RE_ENRICH_FULL path within this run. Run full pipeline + Apollo. The LIGHT-path date-bump does NOT happen here — the FULL path's Completeness Gate governs the date write. Surface in Slack DM as "rerouted from LIGHT to FULL — classification changed".
   - **AMBIGUOUS**: Tier 3 hold. **Do NOT bump `last_enriched_date`** — record stays in the stale pool for Cooper to investigate or for next-run retry. Surface to Cooper's Slack DM with the fetched description.
   - **Web fetch failed** (DNS error, 5xx, captcha, or other unrecoverable error): **Do NOT bump `last_enriched_date`** — we didn't actually verify anything. Surface as Tier 3 ("re-verification failed — held for next run"). Don't silently mark as fresh.

4. **Date bump rule (NOT blanket):** `last_enriched_date = today (ET)` is set ONLY when the LIGHT path reaches a clear resolution — PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN. AMBIGUOUS and web-fetch-failed records keep their prior `last_enriched_date` so they'll be picked up again in the next stale-rotation window. **Cooper directive 2026-04-28: do NOT bump dates blindly — historical bug pattern was hiding unresolved records by marking them fresh.**

Cost per record: 1-2 web_fetches, 0 Apollo credits. **This path is where the CRM gets cleaner over time** — a 120-day rotation through ~3,000 active records means ~25/day get LIGHT-path eviction-checked, so any stale "Tier 5 Other" pollution drains within 4 months.

#### `RE_ENRICH_DEFER` records — skip

Already-flagged records stay flagged. Move on.

## Safety Tiers

| Scenario | Tier |
|-----|-----|
| HIGH-confidence refresh, no segment change | Tier 1 |
| HIGH-confidence segment change on account with no open deals | Tier 1 + cascade |
| MEDIUM-confidence refresh | Tier 2 |
| Segment change on deal-protected account | Tier 3 |
| Downgrade from ICP → non-ICP on customer (closed-won history) | Tier 3 hard stop |
| LOW / MANUAL_REVIEW after edge-case-researcher | Tier 3 |

**Pool-exhaustion signal:** if the query returns fewer than 50 candidates, the CRM is fully rotated within the 120-day window. Log "CRM freshness: green" in the report and process whatever's available (including zero). Don't fabricate work.

## Caps & Budgets

- **Record cap:** **100 accounts/run** (raised from 50 on 2026-04-27 with the addition of pre-score triage in Step 0; pre-score routes 50-70% of records to the RE_ENRICH_LIGHT no-Apollo path so the Apollo budget impact is bounded). Steady state is ~26/day once the initial backlog drains; runs with < 30 candidates are normal and healthy. First-run backlog of ~190 stale accounts drains in ~2 days at the 100/day cap.
- **Apollo credits:** with pre-score triage routing only RE_ENRICH_FULL and MAYBE_RECLASSIFY records to Apollo, expected burn is ~30-50 credits/run = ~900-1,500 credits/month, well under the 1,500-credit Routine 2 sub-cap of the global 6,000/month allocation. Re-enrichment does one Apollo org enrichment per account in the FULL/RECLASSIFY paths. **Pre-flight monthly budget check: at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 50) <= 6000`. If `remaining < 50`, scale down to `remaining`-credit budget, prioritize the oldest-stale records first (they're the most likely to have changed classification), and surface deferred records in the Slack DM hero. Do NOT hard-defer the run — process whatever fits in budget, and let the RE_ENRICH_LIGHT records (which use 0 credits) keep flowing through.** Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded` Apollo error.
- **HubSpot writes:** use `manage_crm_objects.updateRequest` in batch mode. **Batch cap: 10 `objects` per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. At the 100-record cap that's ~10 batched calls for FULL/RECLASSIFY enrichment writes, ~5 for LIGHT idempotency `last_enriched_date` bumps, ~5 for cascade contact-segment syncs. Exponential backoff (1s → 2s → 4s) on HTTP 429; after 3 consecutive 429s on the same batch, halve to 5/batch and retry.
- **Web fetches:** ~6-8 per RE_ENRICH_FULL record (Stages 1-3) + ~1 per RE_ENRICH_LIGHT record (verification only) + 0 per RE_ENRICH_DEFER record. At 100/run with typical 40% FULL+RECLASSIFY / 50% LIGHT / 10% DEFER distribution: 40×7 + 50×1 = 330 fetches/run.
- **Session pacing:** 100 records/page, ≥1 second between pages for HubSpot reads.
- **Contact-segment sync:** when a segment cascade fires, sync to associated contacts in a second batch update; do not issue one-contact-per-call writes.
- **Runtime budget:** Routine has a ~90-minute window (8:00 AM → 9:30 AM ET) before the next routines (Routine 7 monthly sourcing on the 1st, Routine 8 persona fill on Friday) need to run. At 100 records × ~30s per FULL record + ~5s per LIGHT record, expected runtime is 25-45 minutes — substantial headroom.

## Output

Structured report:

- **Subject:** `CRM Guardian — Stale Re-Enrichment — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Hero:** accounts processed, freshness signal (green if backlog < 50; yellow 50-500; red > 500), Apollo credits consumed.
- **Segment changes:** Tier 1 + Tier 2 segment transitions with old → new, reason.
- **Tier 3 held:** downgrade-on-customer, LOW-confidence, conflicting-source cases.
- **Territory shifts:** accounts whose owner changed because state was refreshed.
- **Auto-fixed (Tier 1):** summary counts.
- **Deferred / Errors.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian — Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine — re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian — Routine 2: Stale Re-Enrichment | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue — do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:arrows_counterclockwise: *CRM Guardian — Stale Re-Enrichment* — [YYYY-MM-DD] — [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean` / `CRM freshness: green` when backlog < 50)
- **Body format:** Slack mrkdwn. Tables in triple-backtick code blocks. Prefix every run `CRM Guardian — Stale Re-Enrichment —` for Slack search grouping.
- **Character limit:** 5,000 per text element; thread overflow via `thread_ts`.
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback. No email fallback.
