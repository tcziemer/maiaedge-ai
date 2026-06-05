# CRM Guardian - Import Validator (Cowork Scheduled Task)

**Execution model:** **Cowork scheduled task** (not a Cowork routine). Each run is fire-and-forget, stateless across runs (HubSpot is the source of truth for what was imported in the last 24h). Schedule via Cowork's scheduled-task feature with a cron expression; the prompt below is the full payload.
**Cadence:** Daily, 9:00 AM CT, Monday-Friday. Cron: `0 9 * * 1-5` (local CT — Cowork interprets cron in the user's local timezone, not UTC).
**Reframed as scheduled task (not routine) 2026-05-14 per Cooper.**

Runs FIRST in the daily Cowork cycle. Scans companies imported in the last 24 hours that have not yet been enriched, and validates that the HubSpot company NAME plausibly matches the entity ACTUALLY at the domain. Fixes mismatches BEFORE downstream Apollo-consuming scheduled tasks waste credits.

**Why this task exists:** without an upstream guard, junk imports (restaurants at carrier-sounding domains, parked domains, spoofed brand domains, contractor companies named like operators) reach R1 Fresh Enrichment and burn Apollo credits before being flagged.

**CRM scale baseline:** 0-30 records/day typical. Spike days (manual bulk imports) push 100+. The 100-record cap absorbs spikes; the 24-hour `createdate` window catches everything new before Routine 1 sees it.

---

## Connected Tools (Cowork)

- **HubSpot MCP** - read companies + deals; write `name`, `domain`, `customer_segment`, `flagged_for_deletion_reason`, `account_brief`
- **Slack MCP** - `slack_send_message` to Cooper's self-DM (hard-failure ping ONLY), `slack_read_canvas` + `slack_update_canvas` for the cross-routine ledger
- **`web_search`** - PRIMARY research path (use first, every time)
- **`web_fetch`** - opportunistic enhancement only (when the page is reachable, fetch it; if it returns 4xx/5xx/timeout, drop it and proceed on web_search alone - no penalty, no Tier-3 hold)
- **No Apollo.** This routine is intentionally Apollo-free.

---

## Delivery - quiet on success, ping only on hard failure (READ FIRST)

Do NOT DM Cooper a per-run debrief. On a clean or partial-but-recoverable run (including zero-record "all clean" runs and partial runs where some records deferred to the next run), the full record is: (1) the on-disk run report at `weekly-reports/YYYY-MM-DD/r0-import-validator/...` (the report body structured in the Output section below becomes the on-disk report, NOT a DM), and (2) the one Run-log row this task appends to the working-ledger canvas `F0B0AFSB9LN` (status emoji per the canvas conventions). The CRM Ops Daily Digest (M-F 4:45pm CT) surfaces this run's work from HubSpot + the ledger, so a self-DM is redundant.

Send a Slack DM to Cooper (`U0A24D9RJLS`) ONLY on a hard failure - HubSpot/Slack MCP unreachable, an abort, or zero records processed against a non-empty candidate queue - as ONE line:

`:red_circle: CRM Guardian - Import Validator [FAILED/ABORTED] - [one-clause reason].`

Still write the matching ❌/⚠️ Run-log row. Retry the ping once (1s → 2s); if it still fails, the disk report + Run-log row are the fallback.

---

## Run-Time Invariants

### A. Timezone
America/New_York for all date math. Convert HubSpot UTC timestamps to ET before comparing.

### B. Skip Already-Flagged
Records with `customer_segment = "Flagged for deletion"` are out of scope (Routine 4 owns them).

### C. Customer Protection - HARD STOP
Any company with ANY closed-won deal (`hs_is_closed_won = true`) is NEVER touched. Customer companies sometimes have legacy domain mismatches (M&A, rebrand) and are protected. Surface as Tier 3 "customer history present, do not auto-correct."

### D. MaiaEdge Own Record
HubSpot ID `124293230301` is hard-stopped. Never write to it.

### E. Idempotency
**`last_enriched_date` stamping policy** (aligns with CLAUDE.md unified table):
- **HARD_FLAG / DEAD_DOMAIN eviction → YES, stamp `last_enriched_date = today (ET)`.** Eviction is a definitive resolution; R2's 120-day rotation does not need to revisit.
- **MISDOMAIN / RENAMABLE / MATCH / AMBIGUOUS → NO stamp.** R0 is not a full enrichment - it's an upstream guard. The record stays at blank `last_enriched_date` so R1 (Fresh Enrichment) picks it up at 10:00 AM CT via its blank-segment filter regardless.

Same-day idempotency is owned by R0's trigger query (`createdate <= 24h ago` AND `last_enriched_date IS EMPTY`) - the 24-hour createdate window prevents R0 from reprocessing the same record next day even when `last_enriched_date` stays blank. Do NOT stamp `last_enriched_date` after a rename or domain correction; doing so would hide the record from R2's 120-day rotation and break the unified stamping invariant in CLAUDE.md ("Stamps only on a passing definitive gate or definitive eviction").

### F. Default to Tier 3 When Uncertain
MEDIUM or LOW confidence on the name-vs-domain check → Tier 3 hold. Do NOT auto-flag for deletion on ambiguous cases. The bar for auto-deletion is HIGH confidence the entity at the domain is from one of the hard-flag categories listed below.

### G. Write Authorization
`confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"` on every `manage_crm_objects` call.

**Pre-authorized writes:**
- `name` (rename to actual entity at domain - Tier 1 on HIGH RENAMABLE)
- `domain` (correct to canonical domain of named company - Tier 1 on HIGH MISDOMAIN, Tier 2 on MEDIUM)
- `customer_segment = "Flagged for deletion"` (HIGH-confidence hard-flag categories, Tier 2)
- `flagged_for_deletion_reason` (scannable reason code + one sentence of evidence; written in the SAME update as any `customer_segment = "Flagged for deletion"` write; lead with the canonical reason code per property-schema §2.1)
- `account_brief` (pure-prose narrative describing what the entity at the domain actually is, and — on flag/correction paths — why the record was renamed / re-domained / flagged. NO bracketed routine tag, NO leading date prefix; the routine identity is implied by `last_enriched_date` + on-disk run report, and the date lives structurally in `last_enriched_date`.)
- `signal_heat = Cold` (MATCH-path default for new records with no signal history - Tier 1; idempotent if already populated)

### H. MaiaEdge Gotchas
- `account_tier` is INVERTED (Tier 1 = highest priority).
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07).
- `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is now an **ICP segment as of 2026-05-11** - Multi-DC enterprises in financial services / healthcare systems / retail and distribution / outsourcing services that pass the scale gate. Never confuse the HubSpot enum value with the literal English word "enterprise" (still used as a generic descriptor in non-ICP contexts).
- AI Colo: `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`.
- No em dashes in customer-facing fields. Use hyphens.
- Category descriptor: "Carrier infrastructure" only.

### I. Enterprise ICP Defensive Notes (2026-05-11)

The Enterprise ICP promotion (2026-05-11) means records previously tagged `customer_segment = "Enterprise-CustomerSegment"` under the old non-ICP framing are now potentially in-ICP. R0 (this routine) should:

- Treat `Enterprise-CustomerSegment` as an ICP segment in all bucket evaluations (RENAMABLE / MISDOMAIN / MATCH paths). Do NOT auto-flag an Enterprise-CustomerSegment record as HARD_FLAG just because it doesn't match an obvious operator-segment naming convention.
- The hard-flag categories list below remains correct - restaurants, churches, schools, etc. at literal "enterprise"-named domains still HARD_FLAG when category is confirmed.
- Only Cooper-set `customer_segment = "Enterprise-CustomerSegment"` records reach R0 in practice (R0's trigger is `last_enriched_date IS EMPTY` - fresh imports). If Cooper set the segment intentionally during import, leave it alone (MATCH path) and let R1 handle scale-gate verification.

---

## Trigger Query

HubSpot `search_crm_objects` on COMPANY:

- `createdate` operator `GTE` value = `now - 24h` (ET, formatted as ISO timestamp)
- `last_enriched_date` operator `NOT_HAS_PROPERTY`
- `customer_segment` operator `NEQ` value `"Flagged for deletion"`
- Company ID != `124293230301`

**Sort:** `createdate ASCENDING` (oldest first within window, so spikes drain in import order).

**Cap:** 100 records per run.

---

## Workflow

### Step 1 - Identify the entity at the domain (web_search primary)

For each candidate, your goal is to identify what the domain actually serves and compare it to the HubSpot `name`.

1. **`web_search` `"<domain>"` site identification** - look for: business directory listings (BBB, Crunchbase, LinkedIn company page, Glassdoor), Wikipedia, news mentions, SEC filings.
2. If domain itself doesn't surface useful results: **`web_search` `"<HubSpot name>" "<domain>"`** - see if the name+domain combination has any public association.
3. **OPTIONAL `web_fetch` enhancement** - `https://[domain]` (root). If it returns 200 OK with content, extract `<title>`, meta description, H1, About blurb, footer to confirm the web_search picture. If it returns 4xx/5xx/timeout/proxy-block, **proceed on web_search alone** - do NOT downgrade confidence and do NOT Tier-3 hold solely because web_fetch failed.

Synthesis rule: 2+ independent sources agreeing on the entity at the domain = HIGH confidence. 1 source = MEDIUM. Conflicting / no useful results = AMBIGUOUS / Tier 3.

### Step 1b - Domain-correction discovery (only when Step 2 buckets as MISDOMAIN)

Triggered ONLY when the HubSpot name is clearly correct but the domain serves a different real business. Goal: find the canonical domain for the HubSpot-named company.

1. **`web_search` `"<HubSpot name>" official website`** (or `"<HubSpot name>" homepage`).
2. From top 3-5 results, identify the URL most likely to be the company's canonical domain (look for: company name in page title; matching About-page corporate identity; SEC filings or LinkedIn company page that links to the same domain).
3. **Optional validation `web_fetch` on the candidate URL.** If reachable and confirms the entity → HIGH confidence. If web_fetch fails, validate via web_search (look for the candidate domain on LinkedIn, Crunchbase, or SEC filings) → MEDIUM confidence at best.

### Step 2 - Bucket the record

Compare HubSpot `name` to the entity at the domain. Apply this disambiguation:

| If... | Then bucket as... |
|---|---|
| HubSpot name searches cleanly to a single real, identifiable business with its own canonical domain `<X>` AND domain at hand `<Y>` is clearly a different real business | **MISDOMAIN** (correct the domain to `<X>`, do not rename) |
| HubSpot name is generic/codename-like / unfindable / matches multiple businesses, AND domain at hand resolves to a single real, identifiable business | **RENAMABLE** (rename company to match domain) |
| Both name and domain identify equally-valid distinct businesses with no clear signal which the import was meant to be | **AMBIGUOUS** / Tier 3 (let Cooper decide) |
| HubSpot name and domain identify the same business (case/abbreviation differences OK, parent/subsidiary relationships OK) | **MATCH** |
| Domain serves a non-business or hard-flag category AND HubSpot name doesn't redeem via MISDOMAIN | **HARD_FLAG** |
| Domain returns DNS NXDOMAIN, parked-page signatures, or persistent destination 4xx/5xx (NOT proxy block) AND name doesn't redeem | **DEAD_DOMAIN** |

**PARTNER_KEEP carveout:** Never HARD_FLAG a domain whose entity is on the keep-list (hyperscalers, major IT/Network OEMs, major SIs, major analysts, named channel partners). Rename to match the partner entity and let Routine 1 classify it as `Other` Tier 5 PARTNER_KEEP.

### Step 3 - Take action per bucket

**MATCH:**
- No write to enriched fields. Leave `last_enriched_date` blank so Routine 1 enriches normally at 10:00 AM CT.
- **`signal_heat` default for new records:** if this record is new to the active pool (created in the last 24h, no `signal_heat` value yet), write `signal_heat = Cold` as the default. No signal history exists yet; heat will be recomputed by Weekly Signal Scan / R-Tier-Audit once signals start arriving. This is a default assignment, not a classification - R0 does not compute heat from research findings. Skip the write if `signal_heat` is already populated (idempotent).

**MISDOMAIN (HIGH):**
- Tier 1: write `domain = [discovered canonical domain]`.
- Write `account_brief = "Domain corrected from \"[old domain]\" to \"[new domain]\" because old domain serves [other entity] while HubSpot name \"[name]\" matches [new domain]. [One-to-two sentences describing what the entity at the new domain actually is, so the brief stands on its own when R1 picks the record up.]"` (pure prose; no leading routine tag, no leading date.)
- Leave `last_enriched_date` blank.

**MISDOMAIN (MEDIUM):**
- Tier 2: same writes as HIGH, but log in the run report's "Domain Corrections - review" table.

**RENAMABLE (HIGH):**
- Tier 1: write `name = [actual entity at domain]`.
- Write `account_brief = "Renamed from \"[old name]\" to \"[new name]\" because domain [domain] serves [entity description], and HubSpot name did not search to its own canonical domain. [One-to-two sentences describing what the new-named entity actually is.]"` (pure prose; no leading routine tag, no leading date.)
- Leave `last_enriched_date` blank.

**RENAMABLE (MEDIUM):**
- Tier 2: same writes, log in the run report's "Renames - review" table.

**HARD_FLAG (HIGH):**
- Tier 2: write `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Hard junk / non-business: <one concrete sentence of evidence>"` (e.g. `Hard junk / non-business: domain serves a restaurant in Austin TX, not a carrier or operator`) in the SAME HubSpot update. Lead with the canonical reason code `Hard junk / non-business`; see property-schema §2.1. No em dashes in the reason string.
- Write `account_brief = "[2-3 sentence description of the actual entity at the domain — what it does, scale if visible, why it falls in the hard-flag category]. Flagged for deletion as [hard-flag-category]; imported HubSpot name was \"[old name]\" and did not redeem the record via MISDOMAIN check."` (pure prose; no leading routine tag, no leading date.)
- Set `last_enriched_date = today (ET)`.

**HARD_FLAG (MEDIUM):**
- Tier 3 hold - surface, do NOT auto-flag.

**DEAD_DOMAIN:**
- Tier 2: write `customer_segment = "Flagged for deletion"` + `flagged_for_deletion_reason = "Dead domain: <one concrete sentence of evidence>"` (e.g. `Dead domain: [domain] returns DNS NXDOMAIN and HubSpot name has no usable canonical alternative`) in the SAME HubSpot update. Lead with the canonical reason code `Dead domain`; see property-schema §2.1. No em dashes in the reason string.
- Write `account_brief = "Domain [domain] is dead/parked/NXDOMAIN; HubSpot name did not search to a usable canonical alternative. Flagged for deletion."` (pure prose; no leading routine tag, no leading date.)
- Set `last_enriched_date = today (ET)`.

**AMBIGUOUS / Tier 3:**
- No write. Surface in the run report's Tier 3 table with the web_search summaries (and on the ledger canvas Tier 3 section) so Cooper can adjudicate via the digest.

### Hard-flag categories (auto-flag for deletion at HIGH confidence)

These categories have NO legitimate path to ICP. When the entity at the domain is identified as one of these, auto-flag is correct (UNLESS PARTNER_KEEP rescues it):

- **Restaurants / food service / hospitality**
- **Apparel / fashion / retail**
- **Churches / religious organizations / faith-based AV**
- **Schools / universities / educational institutions** (unless the domain is a legitimate research-university network operator - rare)
- **Tribal / cultural / government civic orgs** (unless they explicitly operate carrier infrastructure)
- **Real estate / property management / brokerages**
- **Automotive manufacturers / trucking companies** (e.g., Daimler Trucks NA at `dtna.com`)
- **Consumer electronics distributors / retailers**
- **Blockchain / crypto / NFT projects** (unless explicitly a NeoCloud crypto-pivot)
- **Agriculture / farming / livestock**
- **Healthcare clinics / dental / medical practices**
- **Law firms / legal services**
- **Staffing / recruiting / cert orgs**
- **AV / intercom / production-AV vendors** (where the domain serves AV not telecom carriage)
- **Construction / infrastructure CONTRACTORS** (companies that BUILD fiber but don't operate networks - e.g., texasfiberdesigngroup.com)
- **Bathroom / plumbing fixtures**
- **Personal services** (hair salons, beauty, fitness)
- **Spoofed brand domains** (e.g., `littlecrusoe.com`, `crusoesurvival.com` are spoofs of Crusoe - registrants are not the real brand)

When in doubt about category fit → Tier 3, don't auto-flag.

---

## Caps & Budgets

- **Record cap:** 100 records/run.
- **Apollo credits:** 0 (intentionally Apollo-free).
- **web_search:** budget ~2 per record on standard path + 2 per MISDOMAIN candidate. Pace ≥1s between searches.
- **web_fetch:** opportunistic only. ≥0.5s between fetches per host.
- **HubSpot writes:** **batch cap 10 `objects` per `manage_crm_objects` call.** Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on 429.
- **Trigger query pagination:** 100 records/page (single page expected on a 24-hour window).

---

## On-disk run report (structure)

Write this report to `weekly-reports/YYYY-MM-DD/r0-import-validator/run-report.md`. This is the durable record the CRM Ops Daily Digest reads from - it is NOT sent as a DM. Keep the structure; it documents what happened for the digest + Cooper's review.

**Header:**
```
CRM Guardian - Import Validator - [YYYY-MM-DD] - [J] domain-corrected, [N] renamed, [M] flagged, [K] held
```

**Body:**
```
Run summary: [X] records scanned, [J/N/M/K bucket counts], [Y] HubSpot writes, [Z] errors

What needs Cooper's attention:
- [If K > 0] [K] Tier 3 holds - see per-bucket tables below
- [If M > 0] [M] hard-flagged companies - Filter HubSpot Companies → customer_segment = "Flagged for deletion"
- [If MEDIUM-confidence MISDOMAIN/RENAMABLE writes] [count] medium-confidence corrections to verify - see tables below

Run health: [traffic-light: GREEN / YELLOW / RED]
- GREEN: 0 errors, 0 Tier 3, all writes succeeded
- YELLOW: writes succeeded but Tier 3 holds present, OR proxy-block rate >50%
- RED: ≥1 fatal error or aborted partway through

Errors: [None | error description]
```

**Per-bucket tables (append to the report):** Domain Corrections / Renames / Hard-flagged / Tier 3 held with web_search summaries.

**Zero-record run:** report header `All clean - 0 fresh imports in the last 24 hours. Nothing to validate. Run health: GREEN.` plus the ✅ Run-log row. No DM.

**Hard failure (abort / MCP unreachable / zero processed against a non-empty queue):** write the report with `Run health: RED` + the residual unresolved candidates, write the ❌ Run-log row, AND send the one-line failure ping per the Delivery rule at the top.

---

## Cross-routine ledger

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas (`F0B0AFSB9LN`) via `slack_read_canvas`. Drain any items belonging to Routine 0 - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced`. Remove items resolved this run. Persist via `slack_update_canvas`. Append ONE row to the canvas's "Run log" table:
  `| YYYY-MM-DD | CRM Guardian - Import Validator | <status emoji> | <one-sentence summary> | <artifact links> |`
  Status emojis: ✅ success · ⚠️ partial · ❌ failed · ⏭ skipped (do NOT invent new ones).
- If `slack_read_canvas` fails or the canvas is unreachable, log the error in the run report's Errors section and continue - do not abort the routine.

---

## Delivery

See the "Delivery - quiet on success, ping only on hard failure" rule at the top of this prompt. Summary:

- **Success / partial-recoverable runs:** NO DM. Write the on-disk run report (structure in the "On-disk run report" section) + append the Run-log row to canvas `F0B0AFSB9LN`.
- **Hard failure only** (HubSpot/Slack MCP unreachable, abort, or zero processed against a non-empty queue): one-line `:red_circle:` ping to `slack_send_message` channel_id `U0A24D9RJLS` (Cooper's self-DM, workspace `maia-edge.slack.com`). Retry the ping once (1s → 2s); if it still fails, the disk report + ❌ Run-log row are the fallback.
- **Body format:** Slack mrkdwn for the failure ping; the on-disk report uses plain markdown with tables in triple-backtick code blocks.

---

## Cross-routine coordination

- **Runs BEFORE Routine 1 (10:00 AM CT enrichment):** R1 doesn't waste Apollo credits on records this routine flagged.
- **Routine 1's `LIKELY_JUNK` bucket** routes records back to Routine 0 for re-investigation if they slipped past the first 24-hour window. Routine 0 picks them up next run.
