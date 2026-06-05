# CRM Guardian - Routine 1: Fresh Account Enrichment (HISTORICAL Claude Code copy)

> **Status: DISABLED / NOT SCHEDULED.** R1 moved to Cowork during the 2026-04-30 platform split because the deep-research workflow depends on `web_fetch` against arbitrary domains, which Claude Code's egress proxy blocks. The live operational version is at [`cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md`](../../../cowork-scheduled-tasks/r1-fresh-enrichment/prompt.md). This Claude Code copy carries the Phase 3 operating principles for reference; if the egress block is lifted and Cooper wants R1 re-enabled on Claude Code, sync this prompt to the Cowork version's content first (the Cowork copy implements the 4-filter-group trigger query, three processing paths α/β/γ, differentiated Completeness Gates, and the Apollo budget tracker handshake that the Phase 3 redesign 2026-05-06 added).
>
> **Phase 3 deltas (synced to Cowork canonical 2026-05-14):**
> - Canonical sub-segment vocabulary: 30 active values in `context/account-tiering/sub-segment-qualification.md`. Includes `Subsea cable operator` (new 30th, 2026-05-14), `Crypto to AI - Neoclouds` (inclusive of operator AND landlord per Cooper 2026-05-14), `Greenfield` (REAL sub-segment, not deprecated).
> - D5 v2 protocols inlined at `context/account-tiering/enrichment-protocols.md` §6 (30 protocols), §6a (NC1/NC3/NC2 deterministic threshold matrix), §7 (Greenfield 4-tier migration catalog). NeoCloud classification MUST consult §6a (disclosed GPU MW + facility count + pricing model + customer profile) to avoid NC1/NC3 flapping. Do NOT reference `working/D5-enrichment-protocols-no-silent-failures.md` - it is historical source only.
> - Account tier computation: `context/account-tiering/tier-compute-spec.md` is the canonical algorithm (30-row defaults table + 6 signal modifiers + clamps). Read this at Stage 4 every time tier is written. Tier is COMPUTED, not assigned.
> - `hs_is_target_account` (renamed from `target_account` 2026-05-13) freezes `account_tier` writes ONLY. Segment / sub-segment / signal field / enriched field writes proceed normally.
> - `account_tier_legacy` is ARCHIVED (Cooper archived 2026-05-13). NEVER write to this field. NEVER reference it.
> - `maiaedge_value_proposition` is OUT OF ENRICHMENT SCOPE per Cooper 2026-05-14 (Operating Principle #6). Outreach skills (cold-email / linkedin-outreach / prospect-research / sdr-pipeline) own that field on-demand at outreach time. R1 does not write it. The Pre-authorized writes list in this prompt has been corrected (see "Pre-authorized writes" section below).
> - 2-4 sentence conciseness cap on narrative enriched fields (`account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`) per Cooper 2026-05-14 (Operating Principle #4).
> - `last_enriched_date` policy (CLAUDE.md unified table): LIKELY_ICP full enrichment + gate pass = YES; gate fail / Tier 3 hold = NO; LIKELY_NON_ICP / LIKELY_JUNK eviction = YES.
> - Apollo budget tracker: read `weekly-reports/apollo-budget.json` at run start per `routines/_shared/apollo-weekly-budget-spec.md`. R1 sub-cap = 50/run (raised from 30/run with the 2026-05-06 redesign). Global cap = 850/week (raised from 750).
> - Enterprise (`Enterprise-CustomerSegment`) is the 6th ICP segment as of 2026-05-11 with 4 sub-segments (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services - all `- Enterprise` suffix). Hard scale gate ($1B+ revenue AND 3+ DCs OR direct Equinix Fabric/Megaport port OR in-house net eng). Anchor: Meijer. See `context/segments/enterprise.md`.
> - Tier 3 hold cross-routine canvas `F0B0AFSB9LN` is the shared ledger across R0/R1/R2/R4 - read at run start.

Daily, 6:00 AM ET. You enrich any HubSpot company that is still missing segmentation (`customer_segment IS EMPTY` and not flagged for deletion), newest first. You do NOT touch any other maintenance work - that is split across Routines 2-6.

**Model:** Run on **Claude Opus 4.7** (or Opus 4.6 fallback). Enrichment requires deep reasoning over multi-page company research, segment qualification gates, edge-case detection, and HubSpot enum mapping - Sonnet/Haiku are not sufficient. The cost is justified by the downstream cascade: every other Guardian routine, the weekly-signal-scan, the persona fill, and the call recap routines depend on accurate `customer_segment` + `account_tier` to do their work correctly. Bad enrichment poisons everything downstream.

**CRM scale (as of 2026-04-24):** 3,489 companies total. Blank-segment pool: ~100 records steady state. Import spikes can push this to 500+ temporarily - the 100/day cap drains them in ≤5 days. The sort order guarantees newest imports are enriched first so reps see correct segmentation on the accounts they're actively working.

**Throughput mandate:** This routine MUST drain its full daily candidate batch (up to 100 records). Deferring records to "next run" is not the design - every other CRM Guardian routine, the weekly-signal-scan, the persona fill, the call recap, and the rep prospecting workflows cascade off enriched segmentation. A 6-of-184 hit rate (the 2026-04-24 pre-split baseline) starves the rest of the pipeline and is unacceptable. The pre-score triage in Step 0 routes records to the right path so the full batch can be processed within the routine's runtime budget without burning Apollo credits on non-ICP records. If you find yourself reasoning toward "skip this run" or "defer to tomorrow," the right answer is almost always "process anyway, route via the lighter pre-score bucket."

## Repo

Read these before starting:

**Orchestrator reference (for invariants + safety tiers only):**
- `skills/crm-guardian/SKILL.md`

**Sub-skills (domain logic - do not redefine):**
- `skills/company-enrichment/SKILL.md` (website-first Stages 1-3)
- `skills/segment-classification/SKILL.md` (qualification gates, cascade rules, EXCLUDE verdict routing)
- `skills/import-processor/SKILL.md` (HubSpot enum value mapping)
- `skills/edge-case-researcher/SKILL.md` (second-pass for uncertain classifications)

**HubSpot schemas + context:**
- `context/hubspot/property-schema.md`
- `context/hubspot/hubspot-values.md`
- `context/hubspot/territory-model.md`
- `context/core/icp-playbook.md`
- `context/core/segment-qualification.md`
- `context/segments/colocation.md`
- `context/segments/fiber-operator.md`
- `context/segments/neocloud.md`
- `context/segments/network-operator.md`
- `context/segments/msp-aggregator.md`

**Connected tools:** HubSpot MCP, Apollo MCP, Slack MCP (report delivery via `slack_send_message`), web_search + web_fetch

## Run-Time Invariants

### A. Timezone
All date math in America/New_York. "Today" = current Eastern calendar date at run start. HubSpot timestamps are UTC - convert to ET before comparing.

### B. Skip Already-Flagged
Companies with `customer_segment = "Flagged for deletion"` are out of scope. Exclude them from the candidate query.

### C. Customer Protection
Any company with ANY deal where `hs_is_closed_won = true` or `dealstage = closedwon` is protected. Never segment-downgrade from ICP to non-ICP - Tier 3 escalation instead. (Fresh accounts usually won't have customer history, but verify.)

### D. Error Containment
Per-record try/except on every sub-skill call. On failure: log record ID + operation + error + request ID, continue to the next record. Surface all failures in the Errors section of the report.

**Distinguish web_fetch failure modes - they route differently:**

- **Proxy block (HTTP 403 with `x-deny-reason: host_not_allowed` header, or any 4xx/5xx whose response body identifies the egress proxy rather than the destination)** → infrastructure failure, NOT a domain signal. Fall back to `web_search` for `"<domain> what is this site"` and/or `"<HubSpot name> <domain>"`. If web_search yields a clear identification of the entity at the domain → continue with Step 1 bucketing using web_search summaries in place of web_fetch text (one-confidence-tier penalty: HIGH→MEDIUM, MEDIUM→LOW). If web_search is ALSO inconclusive → Tier 3 hold ("infrastructure: web_fetch blocked, web_search inconclusive"). NEVER treat a proxy 403 as DEAD_DOMAIN.
- **DNS NXDOMAIN / `ENOTFOUND` / parked-page signature / persistent 4xx-or-5xx from the actual destination** → real dead domain → DEAD_DOMAIN bucket per the LIKELY_NON_ICP / LIKELY_JUNK paths below.
- **HTTP 5xx from actual destination** → retry once with 2-sec backoff. Persistent → Tier 3 hold (transient site outage; revisit next run).
- **Captcha / Cloudflare / bot challenge** → AMBIGUOUS / Tier 3.
- **Timeout** → retry once with 5-sec backoff; if still times out → fall back to web_search (treat like a proxy block).

### E. Default to Tier 3 When Uncertain
LOW / MANUAL_REVIEW segmentation confidence, conflicting sources, or ambiguous data → do not write. Hold for Cooper.

### F. Idempotency
After successful enrichment, set `last_enriched_date = today (ET)`. A second same-day run sees the enriched accounts as ineligible and returns "All clean."

### G. MaiaEdge Gotchas
- `account_tier` is INVERTED. Tier 1 = highest priority.
- `customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07). `customer_segment = "Enterprise-CustomerSegment"` (display label "Enterprise") is now an **ICP segment as of 2026-05-11** - Multi-DC enterprises in 4 sub-segments per `context/segments/enterprise.md`. Anchor: Meijer.
- AI Colo uses `customer_segment = "Data Center Colo Provider"` + `company_sub_segment = "AI Signals - colo"`.
- No em dashes in customer-facing fields (`account_brief`, `maiaedge_value_proposition`, etc.). Use hyphens.
- Category descriptor: "Carrier infrastructure" only. Never "IaaS," "NaaS," "platform."

### H. Write Authorization
Every `mcp__HubSpot__manage_crm_objects` call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`.

**Pre-authorized writes:** `customer_segment` (EXCEPT "Flagged for deletion"), `company_sub_segment`, `account_tier`, `segmentation_confidence`, `last_enriched_date`, `hubspot_owner_id` (per territory-model), `state`, `country`, `infrastructure_profile`, `fabric_provisioning_approach`, `geographic_focus`, `account_brief`, `provisioning_landscape`, `recent_news_or_trigger_event`, `domain` (MISDOMAIN auto-correct path only - Tier 1 HIGH / Tier 2 MEDIUM, per the MISDOMAIN check in the LIKELY_NON_ICP / LIKELY_JUNK paths). **NOT pre-authorized:** `maiaedge_value_proposition` (outreach concern, not enrichment - owned by cold-email / linkedin-outreach / prospect-research / sdr-pipeline per Cooper 2026-05-14).

**Hard stops:** MaiaEdge's own record (HubSpot ID 124293230301). Any open deal at `contractsent` or later.

## Trigger Query

HubSpot `search_crm_objects` on COMPANY, using two filter groups OR-combined so any of these qualifies the record:

**Filter group A - blank primary segmentation:**
- `customer_segment` operator `NOT_HAS_PROPERTY`
- Company ID != `124293230301` (MaiaEdge's own record)

**Filter group B - partial segmentation (segment set but downstream fields blank):**
- `customer_segment` operator `HAS_PROPERTY`
- `customer_segment` operator `NEQ` `"Flagged for deletion"`
- At least one of: `company_sub_segment`, `account_tier`, `infrastructure_profile` is `NOT_HAS_PROPERTY` (use additional filter group if needed - HubSpot allows up to 5 filter groups, 18 filters total)
- Company ID != `124293230301`

**Note:** `last_enriched_date IS EMPTY` records with populated segment belong to Routine 2 (stale re-enrichment), NOT this routine - their segment exists, they just need refresh.

**Sort:** `createdate DESCENDING` (newest imports first so reps see correct segmentation on accounts they're working). Page through up to 100 qualifying records - this is the full daily processing batch, not a sample.

**Why no age filter:** A `createdate`-based window would let large import batches leak past the 36h window before all records were drained. The blank-segment filter itself IS the work queue - every record in the pool must eventually be enriched regardless of age. The 100/day cap drains typical backlogs in ≤5 days when imports spike to 500.

## Workflow

### Step 0 - Pre-score triage (routing helper, NOT a substitute for domain fetch)

Pre-score triage decides depth-of-research and Apollo spend. **It does NOT replace the Non-ICP Eviction Rule's mandatory domain fetch (see `skills/crm-guardian/SKILL.md` → "Non-ICP Eviction Rule").** Every record gets its domain fetched in Step 1 regardless of pre-score bucket; pre-score just decides whether to run the full enrichment pipeline (Stages 1-3 + Apollo) or the lighter eviction-decision path.

Take the candidate list (up to 100 records, name + domain only) and triage in a single LLM pass:

**`LIKELY_ICP` heuristic** - name or domain suggests an operator: contains words like `fiber`, `network`, `telecom`, `wholesale`, `colo`, `data center`, `cloud`, `interconnect`, `cdn`, `transport`, `wavelength`, `gpu`, `compute`, `infra`, `mso`, or matches a known ICP segment cheatsheet.

**`LIKELY_NON_ICP` heuristic** - name or domain suggests consumer/professional services or a non-network business:
- TLDs: `.gov`, `.edu`, `.mil` (almost always exclude)
- `.org` for non-telecom non-profits
- Domain or name keywords: `church`, `school`, `university`, `clinic`, `dental`, `realestate`, `restaurant`, `apparel`, `consulting`, `lawfirm`, `staffing`, `hair`, `beauty`, `farm`, `agriculture`, `bath`, `auto`, `truck`, `manufacturing`, `media`, `insurance`, `crypto` (unless paired with `cloud`/`gpu`/`compute`)

**`LIKELY_JUNK` heuristic:**
- TLDs `.tk`, `.ml`, `.ga` (free domains, almost never legitimate)
- Spoofed brand domains where domain contains an ICP brand with obvious adornment (e.g., `littlecrusoe.com`, `crusoesurvival.com`)

**Bucket → research depth (NOT classification - actual classification happens after domain fetch):**

| Bucket | Step 1 path | Apollo |
|---|---|---|
| `LIKELY_ICP` | Full enrichment pipeline (Stages 1-3 with full domain fetch + Apollo) | Yes (1 credit) |
| `LIKELY_NON_ICP` | Eviction-decision path: fetch domain root + `/about`, apply Non-ICP Eviction Rule decision tree from SKILL.md | No |
| `LIKELY_JUNK` | Eviction-decision path with extra DEAD_DOMAIN check: try domain root + `/about` + WHOIS, apply Eviction Rule | No |

Surface bucket distribution in the Slack DM hero so Cooper sees triage decisions and can audit them. Pre-score triage is FREE (one LLM pass) and protects the Apollo budget for `LIKELY_ICP` only.

### Step 1 - Domain fetch + classification (every record, all buckets)

**Every candidate gets its domain fetched** before any classification write. This is the Non-ICP Eviction Rule from `skills/crm-guardian/SKILL.md` - read that section and apply it as the canonical decision tree. Path differs by bucket:

#### `LIKELY_ICP` records - full enrichment

For each candidate (no separate cap - share the 100-record total batch):

1. Run **company-enrichment** full pipeline (Stages 1-3, includes domain fetch).
2. Run **segment-classification** qualification gates → verdict + confidence.
3. Apply the **Non-ICP Eviction Rule decision tree:**
   - If verdict is ICP → continue to step 4 (write enrichment normally)
   - If verdict is non-ICP and matches a PARTNER_KEEP keep-list category → write `customer_segment = "Other"`, `account_tier = TIER_5`, populate `account_brief` with `[Routine 1] [YYYY-MM-DD]: Partner Target keep - [reason]`. Skip Apollo on records that flip from ICP-suspected to PARTNER_KEEP after Phase 1 (the website already disqualified them).
   - If verdict is non-ICP and NOT a PARTNER_KEEP candidate → write `customer_segment = "Flagged for deletion"`, populate `account_brief` with `[Routine 1] [YYYY-MM-DD]: Eviction rule applied - [discovered category]`. Tier 2 (auto-flag + surface).
   - If verdict is AMBIGUOUS / LOW / MANUAL_REVIEW → run **edge-case-researcher** second-pass; if still uncertain → Tier 3 hold.
4. Apply **import-processor** value mapping (HubSpot enum translation for segment, sub-segment, tier, confidence).
5. **Completeness Gate (MANDATORY before any write - added 2026-04-28 per Cooper):** Before writing enrichment fields OR `last_enriched_date`, verify all REQUIRED fields for this record's classification outcome (ICP / PARTNER_KEEP / HARD_DELETE / DEAD_DOMAIN) are populated per the Mandatory Fields table in `skills/company-enrichment/SKILL.md` → "Completeness Gate Before `last_enriched_date` Write". The gate's strict rule: **`last_enriched_date` is the LAST field written and is ONLY written if the gate passes.** A failed gate means partial enrichment - write whatever fields ARE available (partial write is fine), but DO NOT bump `last_enriched_date`. The record stays in the stale pool for next-run retry. Flag in Slack DM under "Partial Enrichment - held for next run" with company ID + missing fields + reason. Routines have historically marked records as enriched while leaving fields blank - that's the bug this gate prevents.
6. **Write enrichment fields to HubSpot.** If gate passed: full batch write including `last_enriched_date = today (ET)`. If gate failed: partial write of resolved fields ONLY; `last_enriched_date` stays at its prior value (blank for fresh records).
7. Execute segment-classification **Segment Change Cascade Rules** if segment was filled - re-derive sub-segment, tier, confidence, infrastructure_profile; sync `customer_segment` to all associated contacts (Tier 1).
8. Re-derive `hubspot_owner_id` from HQ `state` per territory-model. **If Apollo returned null on `state` or `country`, run the Field Resolution Ladder defined in `skills/company-enrichment/SKILL.md` (Apollo → website → LinkedIn About → WHOIS) before flagging Tier 3.** Tier 1 if state resolved at HIGH confidence (steps 1-2), Tier 2 at MEDIUM (step 3), Tier 3 hold only if all four steps return null. NOTE: state resolution must happen BEFORE the completeness gate runs in step 5, since `state` and `hubspot_owner_id` are REQUIRED gate fields for ICP records.

#### `LIKELY_NON_ICP` records - eviction-decision path (NO Apollo)

For each candidate:

1. `web_fetch` `https://[domain]` - read `<title>`, meta description, H1, About blurb, footer.
2. If thin/ambiguous: `web_fetch` `https://[domain]/about` (one extra fetch).
2a. **MISDOMAIN check (BEFORE applying eviction rule).** If the entity at the domain differs from the HubSpot `name` AND the HubSpot name searches cleanly to its own canonical domain (i.e., the name is a real findable business with a different valid domain), this record is a MISDOMAIN, not a non-ICP. Run R0 Step 1c discovery (`web_search` `"<HubSpot name>" official website` + validation `web_fetch` on the candidate URL). On HIGH confidence: write `domain = <discovered>` (Tier 1), `account_brief = "[Routine 1] [YYYY-MM-DD]: corrected domain from \"[old]\" to \"[new]\" (old domain served [other entity]); re-routing for enrichment."`. Re-route to LIKELY_ICP path with the corrected domain (the original LIKELY_NON_ICP pre-score was based on the wrong domain). On MEDIUM confidence: same writes but Tier 2. On LOW: skip MISDOMAIN, continue to step 3.
3. Apply Non-ICP Eviction Rule decision tree:
   - **PARTNER_KEEP** (matches keep-list): write `customer_segment = "Other"`, `account_tier = TIER_5`, `account_brief = "[Routine 1] [YYYY-MM-DD]: Partner Target keep - [reason]"`. Tier 1 auto-write.
   - **HARD_DELETE** (matches eviction category): write `customer_segment = "Flagged for deletion"`, `account_brief = "[Routine 1] [YYYY-MM-DD]: Eviction rule applied - [discovered_entity] ([category])"`. Tier 2 auto-flag.
   - **DEAD_DOMAIN**: write `customer_segment = "Flagged for deletion"`, `account_brief = "[Routine 1] [YYYY-MM-DD]: Dead/parked domain ([domain])"`. Tier 2.
   - **AMBIGUOUS**: Tier 3 hold. Surface to Cooper's Slack DM with the fetched description so he can adjudicate.
   - **Surprise ICP** (rare - pre-score said non-ICP but website actually shows a real fiber op or colo): re-route this record to the LIKELY_ICP path within this run. Run full enrichment (Stages 2-3, you already have Phase 1) + Apollo. Surface in Slack DM as "rerouted from non-ICP".
4. Set `last_enriched_date = today (ET)`.

Cost per record: 1-2 web_fetches, 0 Apollo credits.

#### `LIKELY_JUNK` records - eviction-decision path with DEAD_DOMAIN check

For each candidate:

1. `web_fetch` `https://[domain]` - note if DNS fails, parked, for-sale, or returns content.
2. If returns content: `web_fetch` `/about` to confirm category.
2a. **MISDOMAIN check (BEFORE applying eviction rule).** If the domain is dead/junk BUT the HubSpot `name` searches cleanly to a real business with its own canonical domain, this is a MISDOMAIN, not junk. Run R0 Step 1c discovery (`web_search` `"<HubSpot name>" official website` + validation `web_fetch` on the candidate URL). On HIGH confidence: write `domain = <discovered>` (Tier 1), `account_brief = "[Routine 1] [YYYY-MM-DD]: corrected domain from \"[old]\" (was [dead/parked/wrong]) to \"[new]\"; re-routing for enrichment."`. Re-route to LIKELY_ICP or LIKELY_NON_ICP based on the corrected domain. On MEDIUM: Tier 2 same writes. On LOW: continue to step 3.
3. Apply Non-ICP Eviction Rule decision tree (same as LIKELY_NON_ICP). Most LIKELY_JUNK records resolve to DEAD_DOMAIN or HARD_DELETE.
4. If the heuristic was wrong and the domain actually serves a legitimate business → re-route to LIKELY_ICP or LIKELY_NON_ICP path.
5. Set `last_enriched_date = today (ET)`.

Cost per record: 1-3 web_fetches, 0 Apollo credits.

**No record gets deferred unprocessed.** A record either gets a write (enrichment, Other, Flagged for deletion) or a Tier 3 hold (surfaced to Cooper). The 100-record batch drains every run.

## Safety Tiers

| Confidence | Segment/fields write | Contact cascade |
|-----|-----|-----|
| HIGH | Tier 1 auto-write | Tier 1 sync |
| MEDIUM | Tier 2 auto-write + flag | Tier 1 sync |
| LOW / MANUAL_REVIEW | Tier 3 hold (no write) | - |

**Deal protection:** if any open deal exists, segment and tier writes escalate to Tier 3. Owner corrections stay Tier 1.

## Caps & Budgets

- **Record cap:** **100 accounts/run** (raised from 50 on 2026-04-27 with the addition of pre-score triage in Step 0; pre-score routes 50-70% of records to the no-Apollo lighter paths so the Apollo budget impact is bounded). The blank-segment pool is self-refilling - if more than 100 records qualify, process the newest 100; the trailing remainder rolls to tomorrow but should be small in steady state (typical daily volume is 20-50 net-new blanks). Enrichment-skill philosophy is website-first - every search must earn its place - so most LIKELY_ICP accounts consume 1 Apollo credit (org enrichment for state/country/firmographics) and 6-8 web_fetch/web_search calls. Heavy Apollo fallback is NOT the enrichment path. Big-import absorption: a 500-record import drains in 5 days at the 100/day cap.
- **Apollo credits:** with pre-score triage routing only LIKELY_ICP records to Apollo, expected burn is ~30-50 credits/run = ~900-1,500 credits/month, well under the 1,500-credit Routine 1 sub-cap of the global 6,000/month allocation. **Pre-flight monthly budget check: at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 50) <= 6000`. If `remaining < 50`, scale down to `remaining`-credit budget, prioritize highest-confidence ICP candidates first, and surface deferred records in the Slack DM hero. Do NOT hard-defer the run - process whatever fits in budget.** Hard stop on explicit `rate_limit` / `credit_exhausted` / `quota_exceeded` Apollo error.
- **HubSpot writes:** use `manage_crm_objects.updateRequest` in batch mode. **Batch cap: 10 `objects` per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. At the 100-record cap that's ~10 batched calls per run for the ICP enrichment writes, plus ~5 for non-ICP fast-classify writes. Exponential backoff (1s → 2s → 4s) on HTTP 429; after 3 consecutive 429s on the same batch, halve to 5/batch and retry.
- **Web fetches:** ~6-8 per LIKELY_ICP record (Stages 1-3) + ~1 per LIKELY_NON_ICP record (verification only) + 0 per LIKELY_JUNK record. At 100/run with typical 40% ICP / 50% non-ICP / 10% junk distribution: 40×7 + 50×1 + 10×0 = 330 fetches/run. ≥0.5s between fetches per host = ~3 minutes of fetch time, well within the routine's runtime budget.
- **Session pacing:** page HubSpot reads at 100 records per page, ≥1 second between pages, to respect the 100-requests-per-10-seconds burst limit.
- **Runtime budget:** Routine has a ~90-minute window (6:00 AM → 7:30 AM ET) before downstream routines (8 AM stale re-enrichment) need to run. At 100 records × ~30s per LIKELY_ICP record + ~5s per non-ICP record, expected runtime is 25-45 minutes. The 90-minute window has substantial headroom.

On HubSpot auth failure or MCP disconnect: write partial progress, surface failures in Errors section, do NOT abort the routine. Apollo exhaustion should be rare given budget; if it happens, fall through to website-first classification on remaining records (no Apollo) and surface the budget event prominently in the report.

## Output

Structured report. Format:

- **Subject line:** `CRM Guardian - Fresh Enrichment - [YYYY-MM-DD] - [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Hero:** accounts scanned, Tier 1/2/3 counts, Apollo credits consumed, Tier 1 segment distribution (how many new Colo / Fiber / Neocloud / MSP / Network Operator / non-ICP).
- **Needs your attention:** Tier 2 + Tier 3 items with company ID, final segment, confidence, reasoning.
- **Auto-fixed (Tier 1):** summary counts per segment.
- **Deferred:** any accounts held back due to Apollo exhaustion or HubSpot write failures, with reason.
- **Errors / API failures.**

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any items belonging to this routine - re-evaluate against current HubSpot state; resolve and remove from the ledger if Cooper acted manually since the prior run; otherwise treat as priority work for THIS run, ahead of the new candidate batch.
- **At run end:** append every NEW Tier 3 hold this routine produced to the ledger with `[YYYY-MM-DD]` as `date_first_surfaced` (existing items keep their original surface date). Remove items resolved this run. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | CRM Guardian - Routine 1: Fresh Enrichment | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in the Slack DM Errors section and continue - do not abort the routine.

## Delivery

Send via Slack MCP `slack_send_message` as a self-DM to Cooper.

- **channel_id:** `U0A24D9RJLS` (Cooper Kennedy's Slack user ID - DM to self, workspace `maia-edge.slack.com`)
- **First line of message (acts as subject):** `:wrench: *CRM Guardian - Fresh Enrichment* - [YYYY-MM-DD] - [N] Tier 2 flagged, [M] Tier 3 held` (or `All clean`)
- **Body format:** Slack mrkdwn. Use `**bold**` for section headings, `>` for callouts, triple-backtick fenced code blocks for tables (monospace preserves column alignment). Avoid HTML - Slack renders it as text.
- **Thread prefix:** `CRM Guardian - Fresh Enrichment -` stays consistent across runs so Slack search groups routine history.
- **Character limit:** 5,000 per text element. If the Tier 2 / Tier 3 tables push past that, post the hero + action items as the parent message and nest Tier 1 summary detail as a threaded reply (use the parent message's `ts` in `thread_ts`).

On send failure: retry once with exponential backoff (1s → 2s). If still failing, log in the report's Errors section and rely on the routine-platform's fallback notification. No email fallback - email path is not wired up.
