# CRM Guardian - Routine 0: Import Validator (HISTORICAL Claude Code copy)

> **Status: DISABLED / NOT SCHEDULED.** R0 moved to Cowork during the 2026-04-30 platform split because the MISDOMAIN domain-rewrite path depends on `web_fetch` against arbitrary domains, which Claude Code's egress proxy blocks. The live operational version is at [`cowork-scheduled-tasks/r0-import-validator/prompt.md`](../../../cowork-scheduled-tasks/r0-import-validator/prompt.md). This Claude Code copy carries the same Phase 3 operating principles for reference; if the egress block is lifted and Cooper wants R0 re-enabled on Claude Code, sync this prompt to the Cowork version's content first.
>
> **Phase 3 deltas (synced to Cowork canonical 2026-05-14):**
> - Canonical sub-segment vocabulary: 30 active values in `context/account-tiering/sub-segment-qualification.md`. Includes `Subsea cable operator` (new 30th, 2026-05-14), `Crypto to AI - Neoclouds` (inclusive of operator AND landlord per Cooper 2026-05-14), `Greenfield` (REAL sub-segment, not deprecated).
> - D5 v2 protocols inlined at `context/account-tiering/enrichment-protocols.md` §6 (30 protocols), §6a (NC1/NC3/NC2 threshold matrix), §7 (Greenfield 4-tier migration catalog). Do NOT reference `working/D5-enrichment-protocols-no-silent-failures.md` - it is historical source only.
> - `hs_is_target_account` (renamed from `target_account` 2026-05-13) freezes `account_tier` writes ONLY. R0 HARD_FLAG / DEAD_DOMAIN eviction proceeds regardless of this field.
> - `account_tier_legacy` is ARCHIVED (Cooper archived 2026-05-13). NEVER write to this field. NEVER reference it.
> - `maiaedge_value_proposition` is OUT OF ENRICHMENT SCOPE - outreach skills own that field. R0 does not write it.
> - `last_enriched_date` policy (CLAUDE.md unified table): R0 HARD_FLAG / DEAD_DOMAIN eviction = YES bump; MISDOMAIN / RENAMABLE / MATCH / AMBIGUOUS = NO (R1 picks up).
> - Tier 3 hold cross-routine canvas `F0B0AFSB9LN` is the shared ledger across R0/R1/R2/R4 - read at run start.

Daily, 12:30 AM ET - runs FIRST in the daily cycle, before Routine 6 (1 AM territory) and before any Apollo-consuming routine. You scan companies created in the last 24 hours that haven't been enriched yet and validate that the HubSpot company NAME plausibly matches the entity ACTUALLY at the domain. Mismatches get auto-renamed; non-business or completely-unrelated domains get auto-flagged for deletion. This kills bad imports BEFORE Routine 1 wastes Apollo credits enriching them.

**Why this routine exists:** the 2026-04-27 manual run found records like "BCN" at `bcnhouston.com` (Houston restaurant), "EXA" at `exabeauty.com` (Madagascar insect farm), "Deutsche Telekom NA" at `dtna.com` (Daimler Trucks), "Neural Edge Solutions" at NASI (space workforce cert), "Uptown Hair" at an ISP domain, and 9 other clear-junk records. Enrichment was renaming them downstream rather than blocking upstream. Routine 0 closes that leak.

**CRM scale (as of 2026-04-24):** Typical daily import volume is 0-30 records; spike days (manual Apollo/ZoomInfo bulk imports) can push 100+. The 100-record/run cap absorbs spikes; the 24-hour `createdate` window means everything new gets validated before Routine 1 sees it.

## Repo

**Orchestrator reference:**
- `skills/crm-guardian/SKILL.md`

**Sub-skills (light touch only - Routine 0 is website-first and fast):**
- `skills/company-enrichment/SKILL.md` (Stage 1 website read - name/domain semantic check)
- `skills/segment-classification/SKILL.md` (used only to bucket a confirmed business into the right exclusion category for the rename path; Routine 0 does NOT classify into ICP segments)

**Context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/core/segment-qualification.md` (the exclusion list - apparel, restaurants, churches, etc.)

**Connected tools:** HubSpot MCP, Slack MCP, `web_fetch` (primary), `web_search` (fallback only). **No Apollo.** Default path is pure `web_fetch` on domain root + `/about` + `/contact`. `web_search` is reserved for two cases ONLY: (1) proxy-blocked `web_fetch` (HTTP 403 with `x-deny-reason: host_not_allowed`) - search to identify the entity at the domain so the routine can still bucket the record; (2) MISDOMAIN auto-correct path - search for the canonical domain of the company named on the HubSpot record. Never use `web_search` to enrich beyond what's needed to bucket the record.

## Run-Time Invariants

### A. Timezone
America/New_York.

### B. Skip Already-Flagged
Records with `customer_segment = "Flagged for deletion"` are out of scope (Routine 4 owns them).

### C. Customer Protection
HARD STOP: Any company with ANY closed-won deal (`hs_is_closed_won = true`) is NEVER touched by Routine 0, regardless of name/domain mismatch. Customer companies sometimes have legacy domain mismatches (M&A, rebrand) and are protected. Surface as Tier 3.

### D. Error Containment
Per-record try/except. **Distinguish infrastructure failures from domain signals - these route differently:**

- **Proxy block (HTTP 403 with `x-deny-reason: host_not_allowed` header, or any 4xx/5xx whose response body identifies the egress proxy rather than the destination)** → **infrastructure failure, NOT a domain signal**. Fall back to `web_search` for `"<domain> what is this site"` and `"<HubSpot name> official website"` to identify the entity. If `web_search` produces a clear identification → continue with normal Step 2 bucketing (MATCH / RENAMABLE / MISDOMAIN / HARD_FLAG / DEAD_DOMAIN). If `web_search` is also inconclusive → Tier 3 hold ("infrastructure: web_fetch blocked, web_search inconclusive"). NEVER auto-flag DEAD_DOMAIN on a proxy 403 - the proxy is the problem, not the domain.
- **DNS NXDOMAIN / `ECONNREFUSED` / `ENOTFOUND` from the actual destination** → real dead domain → DEAD_DOMAIN auto-flag (subject to Step 3 confirmation).
- **HTTP 404 / 410 from the actual destination after retry** → real dead domain → DEAD_DOMAIN auto-flag.
- **HTTP 5xx from the actual destination** → retry once with 2-sec backoff. If still 5xx → AMBIGUOUS / Tier 3 (could be a temporarily down site).
- **Parked-page detection** (registrar landing page, "this domain may be for sale", GoDaddy/Sedo parking signatures) → DEAD_DOMAIN auto-flag.
- **Captcha / Cloudflare / bot challenge** → AMBIGUOUS / Tier 3.
- **Timeout** → retry once with 5-sec backoff. If still times out → fall back to `web_search` (treat like a proxy block).

### E. Default to Tier 3 When Uncertain
MEDIUM or LOW confidence on the name-vs-domain check → Tier 3 hold. Do NOT auto-flag for deletion on ambiguous cases. The bar for auto-deletion is HIGH confidence the entity at the domain is from one of the hard-flag categories listed below.

### F. Idempotency
**`last_enriched_date` stamping policy** (aligns with CLAUDE.md unified table):
- **HARD_FLAG / DEAD_DOMAIN eviction → YES, stamp `last_enriched_date = today (ET)`.** Eviction is a definitive resolution; R2's 120-day rotation does not need to revisit.
- **MISDOMAIN / RENAMABLE / MATCH / AMBIGUOUS → NO stamp.** R0 is not a full enrichment - it's an upstream guard. The record stays at blank `last_enriched_date` so R1 picks it up at 6 AM via its blank-segment filter regardless. (Body sections E.4/E.5/E.6 below codify this.)

Same-day idempotency is owned by R0's trigger query (`createdate <= 24h ago` AND `last_enriched_date IS EMPTY`) - the 24-hour createdate window prevents R0 from reprocessing the same record next day even when `last_enriched_date` stays blank.

### G. MaiaEdge Gotchas
- `account_tier` inverted (Tier 1 = highest).
- The schema-correct value for the MSP/Aggregator segment is `MSP/Aggregator` (renamed from the deleted `Enterprise` on 2026-05-07). `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is now an **ICP segment as of 2026-05-11** - Multi-DC enterprises in the 4 sub-segments per `context/segments/enterprise.md`. Do not confuse the HubSpot enum values with the literal English word "enterprise."
- No em dashes in customer-facing fields.

### H. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:**
- Company `name` (rename to the actual entity at the domain - Tier 1 on HIGH confidence RENAMABLE path)
- Company `domain` (correct to the canonical domain of the named company - Tier 1 on HIGH confidence MISDOMAIN path; Tier 2 on MEDIUM)
- Company `customer_segment = "Flagged for deletion"` (HIGH-confidence hard-flag categories - Tier 2 auto-flag + surface)
- Company `account_brief` (write the validation reason: "Routine 0 [date]: HubSpot name was X, domain serves Y, entity flagged because [category]")

**Hard stops:** MaiaEdge's own record (ID 124293230301). Any company with a closed-won deal.

## Trigger Query

HubSpot `search_crm_objects` on COMPANY:

- `createdate` operator `GTE` value = `now - 24h` (ET, formatted as ISO timestamp)
- `last_enriched_date` operator `NOT_HAS_PROPERTY` (haven't been touched by any routine yet)
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- `customer_segment` operator `NOT_HAS_PROPERTY` OR populated (we want the freshly imported records regardless of whether segment was set on import - name/domain mismatch is independent of segment)
- Company ID != `124293230301`

**Sort:** `createdate ASCENDING` (oldest first within the 24-hour window so spikes drain in import order).

**Cap:** 100 records per run.

## Workflow

For each candidate (up to 100):

### Step 1 - Fetch domain content (1-3 web_fetch calls per record + web_search fallback)

1. `web_fetch` `https://[domain]` (root). Extract: `<title>` tag, `<meta name="description">`, H1, first paragraph, nav menu items, footer.
   - **If proxy-blocked (HTTP 403 with `x-deny-reason: host_not_allowed`)** → trigger Step 1b (web_search fallback). Do NOT treat this as a dead-domain signal.
   - **If DNS NXDOMAIN / `ENOTFOUND` / parked-page signature** → record as "domain dead," go to Step 2 with the DEAD_DOMAIN signal.
   - **If HTTP 5xx** → retry once with 2-sec backoff; on second 5xx, trigger Step 1b (treat as transient infrastructure failure).
   - **If HTTP 404 from the actual destination** → record as "domain content gone," go to Step 2 with the DEAD_DOMAIN signal.
2. If root page is thin or generic, `web_fetch` `https://[domain]/about` (skip if first fetch already gave clear entity description).
3. If still ambiguous, `web_fetch` `https://[domain]/contact` (last fetch).

Soft cap: 3 fetches per record. If after 3 fetches the entity is unclear → Tier 3 hold ("ambiguous after 3 fetches").

### Step 1b - `web_search` fallback (only when web_fetch is blocked or times out)

Triggered exclusively by infrastructure failures from Step 1 (proxy 403, repeated 5xx, repeated timeout). Goal: identify the entity at the domain WITHOUT loading the page directly. **NEVER use `web_search` as the primary path** - `web_fetch` is faster, cheaper, and more reliable when reachable.

1. `web_search` `"<domain>" site identification` - look for: business directory listings (BBB, Crunchbase, LinkedIn company page, Glassdoor), Wikipedia pages, news mentions, SEC filings.
2. If the domain itself doesn't surface useful results, `web_search` `"<HubSpot name>" "<domain>"` - see if the name+domain combination has any public association.
3. Synthesize: if 2+ independent results agree on the entity at the domain → treat as a HIGH-confidence Step 2 signal (continue with normal bucketing). If only 1 result or sources disagree → MEDIUM-confidence signal (bucket but tier-down: HIGH→MEDIUM, MEDIUM→Tier 3). If `web_search` returns nothing usable → Tier 3 hold ("infrastructure: web_fetch blocked, web_search inconclusive").

Soft cap: 2 web_search calls per record on the fallback path. Add ≥1 sec between searches per host.

### Step 1c - Domain-correction discovery (only triggers from MISDOMAIN bucket in Step 2)

Triggered ONLY when Step 2 buckets a record as MISDOMAIN (HubSpot name is correct, domain serves a different real company). Goal: find the canonical domain for the HubSpot-named company.

1. `web_search` `"<HubSpot name>" official website` (or `"<HubSpot name>" homepage`).
2. From the top 3-5 results, identify the URL most likely to be the company's canonical domain (look for: the company name in the page title; matching About-page corporate identity; SEC filings or LinkedIn company-page that links to the same domain).
3. **Validate via `web_fetch` on the candidate URL.** Confirm: page title / About / footer all identify the same entity as the HubSpot name. The validation fetch is what makes this Tier 1 vs. Tier 2 - without it, MEDIUM at best.
4. If validation fetch ALSO returns a proxy 403, validate the candidate via `web_search` (look for the candidate domain on the company's LinkedIn, Crunchbase, or SEC filing) → MEDIUM confidence at best.

Soft cap: 1 web_search + 1 validation web_fetch per MISDOMAIN candidate.

### Step 2 - Semantic name-vs-domain check

LLM compares the HubSpot `name` against the entity at the domain. Decide which bucket. **The PARTNER_KEEP carveout from the Non-ICP Eviction Rule (`skills/crm-guardian/SKILL.md`) applies here too - never HARD_FLAG a domain whose entity is on the keep-list (hyperscalers, major IT OEMs, major SIs, major analysts, named channel partners), even if the HubSpot name is wrong. Rename to the partner entity and let Routine 1 classify it as `Other` PARTNER_KEEP.**

**MISDOMAIN vs RENAMABLE - which is wrong, name or domain?**
When HubSpot `name` and domain entity disagree, the routine has historically auto-renamed the company to match the domain. That's correct when the HubSpot name was the import error (an internal codename / a broken row from a list import). It's **wrong** when the HubSpot name is correct and the domain itself was the import error - the customer wants the *domain* corrected, not the company renamed away from its real identity. Use this disambiguation:

| If... | Then bucket as... |
|---|---|
| HubSpot name searches cleanly to a single real, identifiable business with its own canonical domain `<X>` AND domain at hand `<Y>` is clearly a different real business | **MISDOMAIN** (correct the domain to `<X>`) |
| HubSpot name is generic/codename-like / unfindable / matches multiple businesses, AND domain at hand resolves to a single real, identifiable business | **RENAMABLE** (rename company to match domain) |
| Both name and domain identify equally-valid distinct businesses with no clear signal which the import was meant to be | **AMBIGUOUS** / Tier 3 (let Cooper decide) |
| HubSpot name and domain identify the same business (case/abbreviation differences OK) | **MATCH** |

| Bucket | Condition | Confidence |
|---|---|---|
| **MATCH** | HubSpot name and domain entity refer to the same organization (case differences, subsidiary/parent relationships, abbreviations all OK) | HIGH |
| **MISDOMAIN** | HubSpot `name` identifies a real findable business with a different canonical domain than the one in HubSpot. Run Step 1c discovery → validate candidate domain via web_fetch → write the corrected `domain`. Do NOT rename the company. | HIGH if Step 1c web_search returns a single canonical match validated by web_fetch; MEDIUM if Step 1c is ambiguous or validation fetch was proxy-blocked; LOW → Tier 3 |
| **RENAMABLE** | Domain serves a real, legitimate business that doesn't match the HubSpot name AND the HubSpot name doesn't search cleanly to its own canonical domain. e.g., `dtna.com` is Daimler Trucks NA, HubSpot name is "Deutsche Telekom NA" - both are real companies, but if the HubSpot name "Deutsche Telekom NA" search returns telekom.com / t-mobile.com, that's MISDOMAIN, not RENAMABLE. Includes domains that resolve to PARTNER_KEEP entities (Cisco, AWS, Accenture, etc.) when the HubSpot name doesn't have its own clean canonical domain. | HIGH if domain entity is unambiguously identifiable AND HubSpot name has no clean canonical match; MEDIUM if parent/subsidiary ambiguity remains |
| **HARD_FLAG** | Domain serves a non-business or a business in one of the hard-flag categories below (apparel, restaurants, churches, schools, agriculture, healthcare clinics, etc.) AND is NOT a PARTNER_KEEP entity. **NOTE:** if the HubSpot name itself searches to a real ICP-adjacent business, do NOT HARD_FLAG - bucket as MISDOMAIN and correct the domain instead. HARD_FLAG is for cases where BOTH name and domain point to non-ICP / junk. | HIGH if the category is unambiguous AND HubSpot name doesn't redeem the record via MISDOMAIN; MEDIUM if borderline |
| **DEAD_DOMAIN** | Domain returns DNS NXDOMAIN, parked-page signatures, or persistent 4xx/5xx from the actual destination (NOT proxy 403). **If HubSpot name is a real findable business, treat as MISDOMAIN instead** - the domain is dead but the company is real, so correct the domain. DEAD_DOMAIN is the bucket when both the domain is dead AND the HubSpot name doesn't redeem the record. | HIGH (the domain is not a usable business identifier AND the name doesn't search to a clean alternative) |
| **AMBIGUOUS** | Cannot determine after 3 fetches + web_search fallback, OR web_fetch returned proxy 403 AND web_search was inconclusive | LOW - Tier 3 hold |

### Step 3 - Take action per bucket

**MATCH:**
- No write. Set `last_enriched_date` blank so Routine 1 enriches normally at 6 AM.

**MISDOMAIN (HIGH confidence)** - *auto-correct the domain, do NOT rename the company:*
- Tier 1 auto-correct: write `domain = [discovered canonical domain]`.
- Write `account_brief` with: `Routine 0 [YYYY-MM-DD]: corrected domain from "[old domain]" to "[new domain]" because old domain serves [other entity description] while HubSpot name "[name]" matches [new domain] (validated via web_fetch on the new domain).`
- Leave `last_enriched_date` blank so Routine 1 enriches the corrected record at 6 AM.

**MISDOMAIN (MEDIUM confidence):** Tier 2 - apply the domain correction + surface for Cooper review. Same writes as HIGH but flag in the Slack DM "Tier 2 Domain Corrections" subsection.

**RENAMABLE (HIGH confidence):**
- Tier 1 auto-rename: write `name = [actual entity at domain]`.
- Write `account_brief` with: `Routine 0 [YYYY-MM-DD]: renamed from "[old name]" to "[new name]" because domain [domain] serves [entity description], and HubSpot name did not search to its own canonical domain.`
- Leave `last_enriched_date` blank so Routine 1 still does proper segment classification on the renamed record.

**RENAMABLE (MEDIUM confidence):** Tier 2 - apply the rename + flag for Cooper review.

**HARD_FLAG (HIGH confidence):**
- Tier 2 auto-flag: write `customer_segment = "Flagged for deletion"`.
- Write `account_brief` with: `Routine 0 [YYYY-MM-DD]: flagged for deletion because domain [domain] serves [entity description] (category: [hard-flag-category]). Imported HubSpot name was "[old name]" - name did not redeem record via MISDOMAIN check.`
- Set `last_enriched_date = today (ET)` so the record is fully off the active routes.

**HARD_FLAG (MEDIUM confidence):** Tier 3 hold. Do NOT auto-flag. Surface in the Slack DM with the discovered entity description so Cooper decides.

**DEAD_DOMAIN:**
- Tier 2 auto-flag: write `customer_segment = "Flagged for deletion"`.
- Write `account_brief` with: `Routine 0 [YYYY-MM-DD]: flagged for deletion because domain [domain] is dead/parked/NXDOMAIN/persistently-4xx (NOT a proxy block). Imported HubSpot name was "[old name]" - name did not search to a usable canonical alternative.`
- Reasoning: a record whose domain doesn't serve content AND whose name doesn't redeem via MISDOMAIN is almost never a real prospect.

**AMBIGUOUS / Tier 3 hold:**
- No write. Surface in the Slack DM with the 3 fetched page descriptions (or web_search summaries if web_fetch was proxy-blocked) so Cooper can adjudicate. **Distinguish "ambiguous because content unclear" from "ambiguous because infrastructure failed (proxy 403 + web_search inconclusive)" in the audit trail** - Cooper handles them differently (the latter is an infrastructure escalation, not a record-level decision).

### Hard-flag categories (auto-flag for deletion at HIGH confidence)

These categories are ALWAYS exclusions per `skills/crm-guardian/SKILL.md` → "Non-ICP Eviction Rule" and `context/core/segment-qualification.md`. They have NO legitimate path to ICP. When the LLM identifies the domain entity as one of these, auto-flag is the correct action - UNLESS the entity is on the PARTNER_KEEP keep-list, in which case rename instead:

- **Restaurants / food service / hospitality** (BCN Houston restaurant, hotels, caterers)
- **Apparel / fashion / retail** (t-shirt wholesalers, clothing brands)
- **Churches / religious organizations / faith-based AV** (vibrantchurchcommunications.com)
- **Schools / universities / educational institutions** (unless the domain is a legitimate research-university network operator, which is rare)
- **Government tribal organizations / cultural orgs** (Chumash tribe types - unless they explicitly operate carrier infrastructure)
- **Real estate / property management / brokerages**
- **Automotive manufacturers / trucking companies** (Daimler Trucks NA at dtna.com)
- **Consumer electronics distributors / retailers** (Toptel.pl Polish electronics distributor)
- **Blockchain / crypto / NFT projects** (ledgerofearth.com - unless explicitly a NeoCloud crypto-pivot classifying as `Crypto to AI - Neoclouds` per segments/neocloud.md)
- **Agriculture / farming / livestock** (Madagascar insect farms, etc.)
- **Healthcare clinics / dental / medical practices**
- **Law firms / legal services**
- **Staffing / recruiting / cert orgs** (NASI space workforce cert at neuraledgesolutions.com type imports)
- **AV / intercom / production-AV vendors** (Clear-Com intercoms - if the domain serves AV not telecom carriage)
- **Construction / infrastructure CONTRACTORS** (NOT operators - companies that BUILD fiber for carriers but don't operate networks. e.g., texasfiberdesigngroup.com is a fiber contractor, not a fiber operator)
- **Bathroom / plumbing fixtures** (axentbath.us types)
- **Personal services** (hair salons, beauty, fitness)
- **Spoofed brand domains** (`littlecrusoe.com`, `crusoesurvival.com` are spoofs of Crusoe; the domain registrants are not the real brand)

When in doubt about category fit → Tier 3, don't auto-flag.

## Caps & Budgets

- **Record cap:** 100 records/run. Typical import volume is 0-30/day; the cap absorbs spike-import days.
- **Apollo credits:** **0**. This routine is intentionally Apollo-free. The website is a HIGH-confidence source for entity identity and costs no credits.
- **Web fetches:** soft cap 3 per record × 100 records = 300/run on the primary path. Run with conservative pacing (≥0.5s between fetches per host) to avoid being rate-limited by target sites.
- **Web searches:** budget 2/record on the proxy-block fallback path + 1/record on the MISDOMAIN discovery path + 1/record validation fetch. At 100/run with ~20% proxy-block rate (today's proxy 403s) and ~10% MISDOMAIN rate, expected fallback usage is ~20×2 + 10×2 = ~60 web_search calls + ~10 validation web_fetch. ≥1s between web_search calls.
- **HubSpot writes:** at full cap with most records being HARD_FLAG / RENAMABLE / MISDOMAIN / DEAD_DOMAIN, ≤200 writes/run. **Batch cap: 10 objects per `manage_crm_objects.updateRequest` call** (HubSpot MCP enforces this cap; the routine prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on 429.
- **Session pacing:** 100 records/page on the trigger query (single page expected, given 24-hour window).

## Output

Structured report:

- **Subject:** `CRM Guardian - Import Validator - [YYYY-MM-DD] - [J] domain-corrected, [N] renamed, [M] flagged for deletion, [K] held for review`
- **Hero:** records scanned (24-hour window), bucket distribution (MATCH / MISDOMAIN / RENAMABLE / HARD_FLAG / DEAD_DOMAIN / AMBIGUOUS), web_fetches consumed (primary), web_searches consumed (fallback + MISDOMAIN discovery), proxy-block rate (% of records that hit `web_fetch` 403).
- **Domain corrections (Tier 1/2):** company ID, name (unchanged), old domain → new domain, validation evidence (web_fetch on new domain confirms entity matches name), confidence.
- **Renames (Tier 1/2):** company ID, old name → new name, domain (unchanged), discovered entity, confidence.
- **Hard-flagged (Tier 2):** company ID, name, domain, discovered entity, hard-flag category.
- **Dead domains (Tier 2):** company ID, name, domain, failure mode (NXDOMAIN / parked / 404 / persistent 5xx - NOT proxy 403).
- **Held for review (Tier 3):** ambiguous records with the 3 fetched page descriptions (or web_search summaries if web_fetch was proxy-blocked) so Cooper can adjudicate from the report. Distinguish content-ambiguity from infrastructure-ambiguity in this section.
- **Infrastructure incidents:** count of web_fetch 403s (proxy `host_not_allowed`), web_fetch timeouts, web_search rate-limit hits. If proxy-block rate exceeds 50% on a run, surface this as a top-level escalation in the hero (Cooper needs to know the platform allowlist is broken).
- **Errors / API failures.**

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper. This routine's report arrives FIRST each day (~12:45 AM ET), before Routine 6.

- **channel_id:** `U0A24D9RJLS` (self-DM, workspace `maia-edge.slack.com`)
- **First line (subject):** `:warning: *CRM Guardian - Import Validator* - [YYYY-MM-DD] - [J] domain-corrected, [N] renamed, [M] flagged, [K] held` (or `All clean - no fresh imports today`)
- **Body format:** Slack mrkdwn. Tables in triple-backtick code blocks. Prefix every run `CRM Guardian - Import Validator -` for Slack search grouping.
- **Character limit:** 5,000 per text element. On a typical day this routine has 0-30 records and fits in one message; on spike days, hero + per-bucket tables thread via `thread_ts`.
- On send failure: retry once with exponential backoff. If still failing, log in Errors and rely on routine-platform fallback. No email fallback.

## Cross-routine coordination

- **Runs BEFORE Routine 6 (1 AM territory & hygiene):** territory verifies a smaller, cleaner set of new records.
- **Runs BEFORE Routines 1 + 2 (6 AM / 8 AM enrichment):** enrichment doesn't waste Apollo credits on records this routine flagged.
- **Routine 1's `LIKELY_JUNK` bucket (pre-score triage)** routes records back to Routine 0 for re-investigation if they slipped through the first 24-hour window. Routine 0 picks them up next morning.
- **Ledger:** see `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger. At start, drain any items belonging to Routine 0 from the ledger; at end, append new Tier 3 holds with `[date_first_surfaced]`.

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian - Routine 0: Import Validator | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue - do not abort the routine.
