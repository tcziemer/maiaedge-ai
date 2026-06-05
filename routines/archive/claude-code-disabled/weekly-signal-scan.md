# MaiaEdge Weekly Signal Scan Routine (HISTORICAL Claude Code copy - Phase 3 Tier Recompute + Signal Field Persistence)

> **Status: HISTORICAL / NOT SCHEDULED.** The Signal Scan routine moved to Cowork during the 2026-04-30 platform split because Claude Code's egress proxy blocks the segment-news scraping that drives Stage 1. The live operational version is at [`cowork-scheduled-tasks/weekly-signal-scan/prompt.md`](../../../cowork-scheduled-tasks/weekly-signal-scan/prompt.md). This Claude Code copy is kept as historical reference; do NOT re-enable on Claude Code without first resolving the egress proxy block.

## Phase 3 update (2026-05-14)

Phase 3 layers on top of Phase 2 without restructuring the 7-stage workflow. The pre-existing per-segment scrape, sub-agent QA, cascade-by-score Slack delivery, Carryover News pool, and Phase 0 routing all stay as documented below. Phase 3 adds:

1. **New Stage 5b** runs after Stage 5 partial writes. For every account where a signal scored >=8 this week, write the three signal persistence fields (`last_signal_score`, `last_signal_date`, `signal_count_last_30d`) AND recompute `account_tier` per `context/account-tiering/tier-compute-spec.md`. Stage 5b honors `hs_is_target_account = true` (signal field writes proceed; tier write skipped). Stage 5b is a Stage 5 partial-write extension and does NOT bump `last_enriched_date` per the CLAUDE.md Unified Stamping Policy.
2. **Stage 3 NEW-account creation runs the full R1 5-stage pipeline** (D1 disqualifier check + research-first 5-stage workflow) per `context/account-tiering/enrichment-protocols.md`. Stage 3 NEW-account creates DO bump `last_enriched_date`. No-default-manual-review: best-fit classification with calibrated confidence, target manual_review_required population under 5%.
3. **Excel "Account Tier" column reads the freshly-computed tier** from Stage 5b (not the pre-run value).
4. **Sub-segment vocabulary aligned to the 30 active values** in `context/account-tiering/sub-segment-qualification.md`. Notable updates: `Tier 1 Carrier - Network Op` (not "Tier 1 Global Incumbent"), `Subsea cable operator` (new 30th sub-segment, 2026-05-14), `Crypto to AI - Neoclouds` is inclusive of operator AND landlord variants (Cooper 2026-05-14), `Greenfield` is a real sub-segment (not deprecated), `Managed Network Services - MSP` (not the legacy `- Network Operator` suffix).
5. **Field rename:** `target_account` is now `hs_is_target_account` throughout. Updated below.

# MaiaEdge Weekly Signal Scan Routine (Phase 2 - Relevance Expanded, retained context)

You are executing the MaiaEdge weekly-signal-scan routine on behalf of Cooper Kennedy (RevOps, Slack `U0A24D9RJLS`, workspace `maia-edge.slack.com`). This is a production CRM data pipeline - correctness matters more than speed. No skipping steps.

**Model:** Run on **Claude Opus 4.7** (or Opus 4.6 fallback). The relevance judgment that drives this routine - "is this signal genuinely a buying-trigger for THIS prospect at THIS moment?" - is exactly the kind of multi-source synthesis Opus is needed for. Sonnet/Haiku produce mechanically-correct but flat output (right signals, wrong relevance ranking, missed cross-segment patterns).

**Phase 2 mode (current - 2026-04-27 redesign, Enterprise added 2026-05-11):**
- **Tier A + Tier B signals both active.** Tier C paired-only (fires only when stacked with another signal on the same account in the same 30-day window).
- **Score floor 12** (was 18). The previous 18-floor produced 5 accounts/week aggregate across all reps - Phase 2 broadens to relevance-graded coverage.
- **40-account cap per rep** (was 25). With Tier B activated and the lower floor, more genuinely-relevant accounts surface.
- **Per-segment Stage 1 sub-stages** (new). Stage 1 splits into **6 parallel passes** (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / **Enterprise** as 6th, added 2026-05-11), each with dedicated source coverage and signal inventory. This is what gives reps the depth Cooper asked for: relevance-graded coverage of the right accounts at the right time, by segment.
- **Expanded target list:** Stage 0 builds the cross-reference list from Tier 1+2+3 ICP accounts (was Tier 1+2 only) - Tier 3 ICP accounts have legitimate exec hires and hiring spikes too. **Includes `Enterprise-CustomerSegment` as of 2026-05-11.**
- **Watch-list tier (score 8-11):** writes `recent_news_or_trigger_event` to HubSpot but does NOT surface in rep DM. Reps see the signal when they open the account in HubSpot, without the DM getting cluttered.
- **Cascade-by-score Slack delivery** with subtle color tiers (red / orange / yellow / blue) by score band.
- **Phase 0 delivery override:** Tim Ziemer's international territory still routes to Cooper for signal-quality validation. Tim Lieto and Ken still get DMs directly.

**Relevance is the goal.** The point of Phase 2 isn't volume - it's coverage of every account where MaiaEdge's message will resonate THIS week because of what's happening at the account. A rep with 22 high-relevance accounts beats a rep with 5 ultra-rare ones because deal-rate × volume is what closes the quarter.

## Read These Files First - Every Run, In Order

The runtime MUST load all files in this section before Stage 1. Partial reads = misclassification risk. Skipping ICP files means Suggested Angles get written from default templates instead of segment-aware language. Read all of them on every run - caching is free, re-reading is cheap, wrong output is expensive.

### 1. Repo conventions
- **`CLAUDE.md`** - repo conventions, key rules, team structure, territory model. Critical: account tiers are INVERTED (Tier 1 = highest priority). MSP / Aggregator HubSpot internal value is `MSP/Aggregator` (matches the rep-facing label; renamed from the deleted `Enterprise` on 2026-05-07). **Enterprise (`Enterprise-CustomerSegment`) is now an ICP segment as of 2026-05-11** with four sub-segments: `Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`. Anchor: Meijer. AI Colo segment uses `customer_segment="Data Center Colo Provider"` + `company_sub_segment="AI Signals - colo"`.

### 2. Master skill
- **`skills/weekly-signal-scan/SKILL.md`** - 7-stage workflow, Phase 1 inventory table (with NC-/NO- disambiguated codes), Phase 1 suppression list (MaiaEdge self, Flagged for deletion), run-time invariants, Stage 5 overwrite-authority table, edge cases, MCP requirements, scope guardrails.

### 3. Signal catalogs (all seven - fire across all segments every run)
- **`context/signals/signal-framework.md`** - scoring model, universal signals (U1-U6), I-series international (I1, I2), full source stack, Exec Hire Detection Without Sales Navigator, conference agenda list, stacking rule (≥8 floor), greenfield/transition bonus math. Honor the Phase 1 override banner at the top.
- **`context/signals/universal-platform-signals.md`** - Apollo AP-1 through AP-7 + FR-1/2/3. Canonical scoring + noise demotions (AP-5 alone, AP-6 alone, FR-2 alone, Apollo keyword drift, generic headcount growth, status pages, Uptime Tier certs, generic PR).
- **`context/signals/colocation-signals.md`** - C-A* tier A codes (greenfield S1-S5, 1→2 transition, GPU tenant anchor, liquid cooling, interconnection exec hire, net-eng hiring spike, anchor tenant signing, M&A/PE recap). Sub-segments: Standard / AI Signals / Modular / Greenfield.
- **`context/signals/fiber-signals.md`** - F-A* tier A codes (BEAD award, PE roll-up, AI-DC fiber win, NaaS/portal launch, VP network automation hire, IRU, broader M&A, ABS/refinancing, consortium/federation).
- **`context/signals/network-operator-signals.md`** - **NO-A\*** (runtime prefix) / N-A* (catalog prefix) tier A codes (PCF copycat, earnings transcript, CTO/CNO transition, divestiture/spin-off, GitHub CAMARA/Nephio commits, TMF AN self-assessment, SRv6 production, multi-domain RFP, PCEP/SR-TE job reqs, CTrO/CDO appointment).
- **`context/signals/neocloud-signals.md`** - **NC-A\*** (runtime prefix) / N-A* (catalog prefix) tier A codes (greenfield S2/S3, 1→2 transition, new facility, NVIDIA Lepton/NCP/Exemplar, enterprise customer win, GPU-backed debt, net/SRE hiring spike, anchor tenant signing, colo lease 8-K, PeeringDB changes, IX port addition, MLPerf submission).
- **`context/signals/msp-aggregator-signals.md`** - M-A* tier A codes (PE acquisition/roll-up, carrier dropped from line card, new carrier added, AI Practice launch, CRO/VP SE hire, TSD platform replatforming, ScanSource earnings disclosure). Display label to reps: "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).
- **`context/signals/enterprise-signals.md`** - E-A* tier A codes (added 2026-05-11): E-A1 New DC Build / Expansion, E-A2 M&A (announcement OR close, two-event firing), E-A3 AI/GPU workload announcement requiring Enterprise GPU connectivity, E-A4 Network exec hire (VP/Director/Principal Network Infrastructure), E-A5 Regulatory enforcement event (NY DFS, HHS OCR breach, PCI v4.0, DORA CTPP), E-A6 Equinix Fabric / Megaport / PacketFabric customer-win naming a Tier 1 enterprise, E-A7 SOX 10-K disclosure of network modernization. Tier B: senior network role job-posting surge, peer-incident segment-wide review, multi-cloud migration kickoff. Tier C paired-only: industry conference speaking slot, earnings transcript mention, colo customer-logo appearance. Sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services. Anchor account: Meijer.

### 4. HubSpot schemas (field specs + enum values)
- **`context/hubspot/property-schema.md`** - especially `recent_news_or_trigger_event` (250 char HARD cap), `account_brief` (400 char), `infrastructure_profile` (500 char), `last_enriched_date`, `account_tier` (inverted), `hubspot_owner_id`, `customer_segment`, `company_sub_segment`, `linkedin_company_page` (Apollo-overwrite-authoritative), `state`, `country`.
- **`context/hubspot/hubspot-values.md`** - segment + sub-segment enum values, tier enum values, confidence enum values (HIGH=`high_90`, MEDIUM=`medium_7089`, LOW=`low_5069`, MANUAL=`manual_review_required`).
- **`context/hubspot/territory-model.md`** - state → owner mapping (East Tim L 30 states + West Ken 20+DC + International Tim Z).
- **`context/hubspot/contact-schema.md`** - contact property specs for new-account contact creation (lifecyclestage enum: `subscriber, lead, MQL, SQL, opportunity, customer, other` - no `evangelist`).
- **`context/hubspot/deals-schema.md`** - `hs_is_closed_won` + `hs_is_closed_lost` booleans for deal-protection checks (never filter dealstage strings; pipeline uses custom numeric IDs).
- **`context/hubspot/poc-schema.md`** - POC ticket pipeline for deal-protection check.

### 5. ICP cheatsheets - READ ALL SIX every run (Suggested Angle depth depends on this)
- **`context/segments/colocation.md`** - ICP definition, 4 sub-segments (`Standard - colo` / `AI Signals - colo` / `Modular - colo` / `Hyperscale Wholesale - colo`) + cross-segment `Greenfield` (pairs with colo OR NeoCloud parent), buyer personas by sub-segment, 2025-2026 industry landscape (power constraint, AI reshaping facility, market bifurcation, M&A dynamics, community opposition, sovereign tenant requirements, inference-profile shift, metro-edge diffusion, modular DC variant, colo/neocloud disambiguation, vertical-integration competitive sharpening), Relevance Bridges, Insider Language Bank.
- **`context/segments/fiber-operator.md`** - ICP definition, 6 sub-segments (`Regional CLEC - Fiber operator` / `Long Haul / Backbone - Fiber operator` / `Dark Fiber Specialist - Fiber Operator` / `Tier 2 National Wholesale - Fiber operator` / `Regional Cable Operator - Fiber operator` / `Municipal / Cooperative - Fiber operator`), buyer personas, BEAD timeline, AI-DC fiber demand, consolidation dynamics, ABS/refinancing context, consortium/federation thesis.
- **`context/segments/network-operator.md`** - ICP definition, 5 sub-segments (`Tier 1 Carrier - Network Op` / `Pure Wholesale Carrier - Network Op` / `Cable MSO Enterprise Division - Network Op` / `International Backbone Specialist - Network Op` / `Subsea cable operator` - NEW 2026-05-14). Track A vs Track B is now a dedicated `network_op_track` field (`external_extension` / `internal_external_unification`), NOT a sub-segment value (legacy sub-segments archived 2026-05-13). CAMARA/Nephio/ONAP/OpenConfig/Sylva standards context, TM Forum Autonomous Networks maturity ladder, SRv6 production context, Track A / Track B messaging split.
- **`context/segments/neocloud.md`** - ICP definition, 5 sub-segments (`Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds`), Persona Prioritization by stage (pre-revenue / early / mid-growth / scale / public), Neocloud Angle by Maturity (watch list / in-pain-now / scaling-wall), GPU debt wall context, agentic latency compounding, enterprise long-tail scaling wall, Datum channel intelligence, neocloud/colo disambiguation.
- **`context/segments/msp-aggregator.md`** - ICP definition (telecom/network aggregators NOT IT MSPs), 5 sub-segments (`Telecom Aggregator - MSP` / `Managed Network Services - MSP` / `TSD Technology Services Distributor - MSP` / `Master Agent - MSP` / `Cloud + Telecom Hybrid MSP - MSP`), two operational subtypes (US TSD channel + NaaS platform operators), ICP Exclusion List (IT MSPs, voice termination, SMS/A2P/CPaaS, cellular IoT MVNOs, roaming hubs, eSIM platforms).
- **`context/segments/enterprise.md`** - ICP definition (added 2026-05-11), 4 sub-segments only (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services), hard scale gate ($1B+ + 3+ DCs OR Equinix Fabric/Megaport port OR in-house net eng), buyer personas (VP Network Infrastructure → CIO → CSO/CISO with sub-segment-specific priority), Insider Language Bank with sub-segment-specific vocabulary (FFIEC physical-path verification, Epic downtime procedure, peak readiness / freeze, seat ramp / paired site / client carve-out), Anonymized Proof-Point Bank, Vocabulary Lock, Watch List verticals (Manufacturing, Energy/Utilities, Logistics - NOT ICP), Government/Defense FedRAMP-gated. Anchor: Meijer.
- **`context/segments/enterprise-use-cases.md`** - 8 priority Enterprise use cases × sub-segment fit matrix × persona fit × insider phrases × cold-email lead-angle templates × proof-point patterns × use-case-specific objections. Required reading for Suggested Angle depth on Enterprise accounts.

### 6. Core ICP context
- **`context/core/icp-playbook.md`** - ICP boundaries, segment sizing, top accounts per segment, exclusion rules.
- **`context/core/segment-qualification.md`** - proof-based qualification tests per segment, Common False Positive Patterns table.
- **`context/account-tiering/sub-segment-qualification.md`** - canonical 30 active sub-segment values (file 06 in the core context set). Used in Stage 3 NEW-account classification AND Stage 5b for the (segment, sub-segment) default-tier lookup. Includes `Tier 1 Carrier - Network Op` (renamed from "Tier 1 Global Incumbent"), `Subsea cable operator` (new 30th, 2026-05-14), `Crypto to AI - Neoclouds` (inclusive of operator AND landlord per Cooper 2026-05-14), `Greenfield` (real sub-segment, not deprecated), `Managed Network Services - MSP` (suffix correction from the legacy `- Network Operator`).
- **`context/account-tiering/tier-compute-spec.md`** - canonical compute_tier algorithm (default tier per segment+sub-segment, hot/white-hot/stacked-signal modifiers, open-deal modifier, stale/sustained-quiet modifiers, ceiling/floor clamps). Stage 5b reads from this. The spec is the single source of truth - do NOT reimplement tier math inline.
- **`context/account-tiering/enrichment-protocols.md`** - D5 v2 protocols. The Stage 3 NEW-account creation pipeline references this for the full R1 5-stage research-first workflow (D1 disqualifier check first, then 5-stage enrichment, then segment-classification, then no-default-manual-review best-fit). Do NOT skip stages or fall back to legacy 3-phase enrichment for NEW-account creates.
- **`context/core/maiaedge-101.md`** - product identity (PBC / Port Extender / PCE), IaaS subscription model, Acme Packet / 128 Technology founder provenance.

### 7. Copy strategy (for Suggested Angle column depth)
- **`context/copy-strategy/segment-messaging.md`** (if present) - canonical segment messaging frames.
- **`context/copy-strategy/scoring-rubric.md`** (if present) - copy-quality bar for the Suggested Angle / Signal Body cells.

### 8. Sub-skill SKILL.md files - invoke per spec; do NOT redefine their methodology
- **`skills/company-enrichment/SKILL.md`** - Stages 1-3 for new-account enrichment AND Step 0C re-enrichment mode. **Step 0C is the canonical overwrite-authority spec** for state / country / linkedin / domain / segment cascade. This skill references it; do not duplicate logic.
- **`skills/segment-classification/SKILL.md`** - qualification gates, EXCLUDE verdict routing, cascade rules for segment changes. Invoked at Stage 3 for new-account classification.
- **`skills/import-processor/SKILL.md`** - HubSpot enum value mapping (segment → HubSpot internal value, sub-segment, tier `tier_1`/`tier_5`, confidence `high_90`/`medium_7089`/etc.). Invoked before any field write in Stage 5.
- **`skills/edge-case-researcher/SKILL.md`** - second-pass investigation for LOW / MANUAL_REVIEW classifications. Invoked at Stage 3 when initial confidence is insufficient.
- **`skills/crm-guardian/SKILL.md`** - safety tiers T1/T2/T3, deal protection rules, cascade logic, Job 8 integration. Every field write in Stage 5 passes through these tiers.
- **`skills/territory-manager/SKILL.md`** - state → owner mapping, Apollo state verification, Contact Owner Cascade. Invoked at Stage 3 and any time `state` is overwritten in Stage 5.
- **`skills/account-brief/SKILL.md`** - stale brief regeneration logic (>30d trigger + research-divergence trigger). Invoked at Stage 5/6 when briefs need regeneration.
- **`skills/account-sourcing/SKILL.md`** - fallback for unknown-segment signals that don't cleanly classify. Invoked at Stage 3 when domain resolution fails.
- **`skills/cold-email/SKILL.md`** - rep-specific voice (Tim Lieto vs. Ken Cunningham). Referenced for the Suggested Angle column in the Excel output.

## What You Are Doing (high-level)

Every Monday at 10:00 UTC (= 5-6 AM ET), execute the 7-stage pipeline defined in `skills/weekly-signal-scan/SKILL.md`:

- **Stage 0** - Preflight checks (MCP availability, target-company list build)
- **Stage 1** - Scrape signals across the full source stack (last 7 days)
- **Stage 2** - Match detected companies → HubSpot by domain
- **Stage 3** - Enrich net-new companies via company-enrichment + crm-guardian safety tiers + territory-manager owner assignment
- **Stage 4** - Score every account-signal pair (Tier × Freshness × Confidence + stacking + greenfield/transition bonuses)
- **Stage 5** - Update HubSpot fields (`recent_news_or_trigger_event`, `infrastructure_profile` if transition detected, `account_brief` if stale or research-divergent, `last_enriched_date`)
- **Stage 6** - Generate 3 rep-specific outputs (email body + Excel attachment)
- **Stage 7** - Commit outputs to the repo (see "Output Delivery" below)

## Preflight Checks (do these BEFORE Stage 1)

**A.** Verify HubSpot MCP is connected. If not, STOP - write a run report to `weekly-reports/YYYY-MM-DD/cooper-run-report.md` explaining the blocker, commit with message `"weekly signal scan YYYY-MM-DD - BLOCKED (no HubSpot MCP)"`, and exit cleanly. Do NOT continue and produce a partial/incorrect run.

**B.** Verify Apollo MCP is connected. Same behavior as (A) if missing.

**C.** Verify today is Monday in America/New_York timezone. If not, STOP with a report "not a Monday run - aborting." The cron can trigger on the wrong day during DST transitions.

**D.** Build the **expanded target-company list** by querying HubSpot for all companies where `account_tier IN ('tier_1', 'tier_2', 'tier_3')` AND `customer_segment` is in the **6 ICP buckets** (`Data Center Colo Provider`, `Fiber Operator`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, `Enterprise-CustomerSegment`) AND `customer_segment != "Flagged for deletion"`. This is the ~700-1,000-account list (was ~400) used for exec-hire and hiring-spike cross-referencing throughout Stage 1. Cache in memory for the run, indexed by domain for O(1) lookup. Per-segment slicing happens in Stage 1.

**E.** Slice the cached target-company list into **6 segment buckets** (Colo, Fiber, NeoCloud, Network Op, MSP-Aggregator, Enterprise) so each Stage 1 sub-stage operates on its segment-specific list. International accounts stay in their segment buckets - territory routing is applied at Stage 6, not Stage 1.

## Critical Invariants

These cannot be violated.

### Timezone
All date math uses America/New_York. "This week" = Sunday 00:00 ET through Sunday 23:59 ET. "7 days ago" = 7 calendar days back from run start in ET.

### Apollo Monthly Budget Sub-Cap

**HARD cap 250 Apollo credits per run** (raised from 200 with Phase 2 broader signal scope; sub-cap from the 6,000-credit/month global Apollo budget - see `skills/crm-guardian/SKILL.md` "Apollo monthly budget" section). 250 cr/week × 4.3 weeks = 1,075/month max. Apollo is consumed in Stage 3 (new-account org enrichment) and on any Stage 1 fallback `apollo_organizations_enrich` calls when domain resolution from a signal can't be done via web alone.

**Pre-flight monthly budget check:** at run start, call `apollo_users_api_profile` to confirm `(monthly_consumed + 250) <= 6000`. If `remaining < 250`, scale down: process Stage 2 matched accounts (already in HubSpot) using whatever Apollo budget exists, defer Stage 3 new-account creation entirely to next Monday, and surface clearly in Cooper's run report: "Apollo monthly budget at X% - N net-new companies deferred to next run." Matched accounts (already in HubSpot) still get enriched since they're priority spend. No runaway-week risk.

### Field Write Rules
- `recent_news_or_trigger_event`: 250 char HARD cap. Format: `"[YYYY-MM-DD] [Signal Type] - [one-line summary]"`. Never exceed.
- `account_brief`: 400 char cap. "Also this week:" line appended only if 2+ signals hit same account.
- `infrastructure_profile`: 500 char cap. Rewrite with updated facility count + context when a site-transition signal is confirmed.
- `last_enriched_date`: set to run date (YYYY-MM-DD) on any touched account.
- `linkedin_company_page`: write from Apollo `linkedin_url` on new-account creation only. Don't overwrite existing HubSpot values.

### Content Rules (for all field writes and email/Excel outputs)
- NO em dashes anywhere. Use hyphens or restructure sentences.
- Category descriptor: "Carrier infrastructure" ONLY. Never "IaaS," "NaaS," "platform," or equivalents in MaiaEdge-facing descriptions.
- Competitor naming (nuanced): factual names OK (tenants like Lambda, Crusoe, Nebius, Nscale; former-employer mentions like "ex-Equinix" in an exec-hire context; deal-partner names). Competitor PRODUCTS get genericized - "Megaport Fabric" → "third-party interconnection fabric"; "Equinix Fabric" → "third-party interconnection fabric"; "Zayo DynamicLink" → "competing on-demand network product."

### Skip Rules (never touch these accounts)
- `customer_segment = "Flagged for deletion"` → drop from all processing (per CRM Guardian invariant).
- Non-ICP signal hits → do not create HubSpot records. Drop silently.

### HubSpot Writes Go Through MCP - HARD RULE

Every CRM mutation in this routine is an MCP call. The Excel attachment is a rep-facing read-only deliverable, NEVER a HubSpot import file.

- **New accounts (Stage 3 auto-create):** `mcp__claude_ai_HubSpot__manage_crm_objects` with `createRequest.objects[]`, `objectType: "companies"`, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`.
- **Field updates (Stage 5):** same tool with `updateRequest.objects[]`. **Batch cap: 10 companies per call** (HubSpot MCP enforces this; the prompt previously cited 100 in error). Loop 10/batch with ≥250ms between batches. Exponential backoff (1s → 2s → 4s) on HTTP 429; halve to 5/batch on 3+ consecutive 429s.
- **Owner cascades to contacts:** same tool, `updateRequest` on contact records.
- **Reads:** `search_crm_objects` (filtered by domain / segment / tier), `get_crm_objects` (for full property pulls), `get_properties` (enum discovery), `search_owners`.

**Do NOT** write a CSV or XLSX file "for Cooper to import" as a substitute for a failed or deferred MCP write. If a write fails, log the failure in the run report's Errors section with record ID + operation + error - Cooper fixes it manually in HubSpot UI, not via file upload.

The Stage 7 Excel attachment exists solely because Slack's `slack_send_message` tool cannot deliver binary attachments directly. The Excel is posted as a downloadable link; reps open it for the full 14-column detail. It never feeds back into HubSpot.

**`import-processor` sub-skill** is referenced in this routine ONLY as an enum-mapping helper (translate internal tier labels → HubSpot enum values like `tier_1`, `high_90`). Its legacy XLSX-to-HubSpot transform is explicitly out of scope for weekly-signal-scan.

### Deal Protection
Any account with at least one open deal (`dealstage NOT IN [closedwon, closedlost]`) still receives field writes, but those writes are flagged as Tier 2 in the run report. Report the account name, the open deal stage, and the signal applied.

## Phase 2 Signal Scope - Tier A + Tier B (scrape both); Tier C paired-only

Phase 2 runs scrape and score Tier A AND Tier B signals across all 6 segments (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / **Enterprise** - Enterprise added 2026-05-11). Tier C signals are scraped but score only when paired with another signal on the same account in the same 30-day window - they don't fire standalone. AP-5 (technographic change alone), AP-6 (Apollo Intent alone), and the Noise List remain disabled.

**Why Tier B is back:** Tier B signals are "strong, 30-90d window" - things like a new partnership announcement, a press release detailing a network upgrade, a planning-stage greenfield filing, a CTO podcast appearance, an OpenStack/Kubernetes commit, a TM Forum membership, etc. They're not as fresh or high-confidence as Tier A, but at the right account they're genuinely buy-trigger-relevant. Phase 1's "Tier A only" constraint was over-restrictive - it produced 5-account weeks even when 20+ relevant signals were detectable.

**Why Tier C is paired-only, not full-active:** Tier C alone is too noisy (job posts, conference appearances, generic blog posts). But Tier C stacked with Tier A or Tier B on the same account in the same window IS signal - it confirms the trigger event has multiple downstream observables.

**Tier A signal codes to scrape (pull each signal's full spec from its segment catalog before starting):**

- **Universal:** U1 exec hire, U2 M&A close, U3 new facility, AP-1 job change, AP-2 lateral, AP-7 funding/M&A, FR-1 SEC 8-K, I1 international state-aid, I2 sovereign AI grant
- **Colocation (7):** C-A0 greenfield S2/S3, C-A1 site 1→2, C-A2 GPU tenant anchor, C-A3 liquid cooling, C-A4 interconnection/network exec hire, C-A5 network eng hiring spike, C-A6 anchor tenant signing (hyperscaler/enterprise/neocloud), C-A7 M&A / PE recap
- **Fiber (9):** F-A1 BEAD award, F-A2 PE roll-up close, F-A3 AI-DC lit/dark fiber, F-A4 NaaS/portal launch, F-A5 VP network automation hire, F-A6 dark fiber IRU, F-A7 M&A broader, F-A8 ABS/refinancing, F-A9 consortium/federation
- **NeoCloud (11, runtime prefix `NC-`):** NC-A0 greenfield S2/S3, NC-A1 site 1→2, NC-A2 new facility N→N+1, NC-A3 NVIDIA Lepton/NCP/Exemplar, NC-A4 enterprise customer win, NC-A5 GPU-backed debt, NC-A6 network/SRE hiring spike, NC-A7 anchor tenant signing, NC-A8 colo lease filing 8-K, NC-A9 PeeringDB changes, NC-A10 IX 100G/400G port, NC-A11 MLPerf submission
- **Network Operator (10, runtime prefix `NO-`):** NO-A1 PCF copycat, NO-A2 earnings transcript, NO-A3 CTO/CNO transition, NO-A4 divestiture/spin-off, NO-A5 GitHub CAMARA/Nephio commits, NO-A6 TMF AN self-assessment, NO-A7 SRv6 production, NO-A8 multi-domain RFP, NO-A9 PCEP/SR-TE job reqs, NO-A10 CTrO/CDO appointment
- **MSP/Aggregator (7):** M-A1 PE acquisition/roll-up, M-A2 carrier dropped, M-A3 new carrier added, M-A4 AI practice launch, M-A5 CRO/VP SE hire, M-A6 TSD platform job-post signal, M-A7 ScanSource earnings disclosure
- **Enterprise (7, added 2026-05-11):** E-A1 New DC build / DC expansion / major capacity add, E-A2 M&A close (announcement OR close - two-event firing, +6 stacking on both within 12mo), E-A3 AI/GPU workload announcement requiring Enterprise GPU connectivity, E-A4 Network exec hire (VP/Director/Principal Network Infrastructure at the four ICP sub-segments), E-A5 Regulatory enforcement event / new framework effective date (NY DFS, HHS OCR breach, PCI v4.0, DORA CTPP, HIPAA NPRM, California AB 749), E-A6 Equinix Fabric / Megaport / PacketFabric / Console Connect customer-win naming a Tier 1 enterprise, E-A7 SOX 10-K disclosure of network / IT modernization initiative

Read each segment catalog (`context/signals/*-signals.md`) for the full thesis, source list, and pattern per code.

**Cooper priority callouts (must not miss, runtime-disambiguated codes):**
- **Greenfield:** C-A0, C-A1, NC-A0, NC-A1, NC-A2, F-A1, I1, **E-A1 (Enterprise new DC build / expansion)**
- **Big colo signings:** C-A2, C-A6, NC-A7, NC-A8 (NC-A8 dual-fires with C-A6 via SEC lease filings)
- **Big acquisitions:** C-A7, F-A2, F-A7, M-A1, NO-A4 (Network Op divestiture), U2, AP-7, **E-A2 (Enterprise M&A - Capital One/Discover, Concentrix/Webhelp, TP/Majorel, Cognizant/Astreya class)**
- **Enterprise regulatory triggers:** **E-A5 (NY DFS Part 500 cert deadline April 15 2026; DORA CTPP designations; HIPAA NPRM; PCI DSS v4.0; California AB 749)**

**⚠️ Code collision:** NeoCloud and Network Operator catalog files BOTH use `N-A*` prefix. In all rep-facing output and internal scoring, qualify codes with segment: `NC-A*` for NeoCloud, `NO-A*` for Network Operator. Never use bare `N-A*` - it's ambiguous.

**Active exclusions (never surface to reps, even when signals fire):**
- **MaiaEdge's own record** (HubSpot ID `124293230301`) - standard self-exclusion.
- **Any account where `customer_segment = "Flagged for deletion"`** - per CRM Guardian invariant.

## Scoring Formula (strict)

**Meeting Probability Score = Tier × Freshness × Confidence**

- **Tier:** A=3, B=2, C=1
- **Freshness (Phase 2 - Tier A flat-within-60-days):**
  - **Tier A signals:** ≤60 days = 3 (full); 60-90 days = 2 (decayed); >90 days = drop entirely
  - **Tier B signals:** 1wk = 3, 30d = 2, 90d = 1 (steeper decay - Tier B is by-definition older/more directional)
  - **Tier C:** paired-only, freshness inherits from the Tier A or Tier B it's paired with
- **Confidence:** High=3, Med=2, Low=1

**Why Tier A freshness is flat within 60 days (Cooper 2026-04-27 directive):** the previous 1wk=3 / 30d=2 / 90d=1 decay produced 5-account weeks because it floored out actionable signals. Catalog descriptions explicitly call out 60-90+ day action windows: exec hires have 90-day mandate windows; M&A has 60-120d post-close integration; BEAD awards have 18-24 month provisioning ramps; CTrO appointments have 12-18 month platformization mandates. A 50-day-old M&A close on a HIGH-confidence Tier A signal is still a hot trigger - score 27 under the new model (was 9 under the old, floored out). The 60-day flat window aligns the math with the action windows the catalogs already document.

### Stacking Rule (2+ signals same account same 30-day window)
Auto-elevate to score 18+ ONLY IF at least one individual stacked signal scores ≥ 8. Two weak signals (each score <8) do NOT stack to top-list. Tier C signals only score in stacks (one Tier C alone = score 0; Tier C + Tier B on same account in same window = base Tier B score + 2 stacking bonus).

### Bonuses
- **+3** for greenfield signals at stage S2 (permit filed) or S3 (utility interconnection / PPA) - Colo + NeoCloud. No bonus at S1, S4, or S5.
- **+6** for facility count 1 → 2 transition - Colo + NeoCloud. Parse current count from the account's `infrastructure_profile` free-text field using LLM read. If parse is low-confidence, skip the bonus (fall back to base greenfield score). When transition confirmed, REWRITE `infrastructure_profile` with updated count + context so next run has fresh state.
- **+3** for I-series signals (I1 international state-aid, I2 sovereign AI grant) - applies to Colo, Fiber, Network Op, NeoCloud in international territory.
- **+2 stacking bonus** for any account with 3+ signals in a 30-day window (on top of the base auto-elevate to 18+).

### Score Floor: 12 (Phase 2)
Drop any account-signal pair scoring below 12 from the rep DM. **Score 8-11 → "Watch List" path:** still write `recent_news_or_trigger_event` to HubSpot at Stage 5 (the rep sees it in the account record), but do NOT include in the rep DM. Reps work the DM as their priority list; the watch list is passive coverage that updates the CRM without DM clutter.

Below 8 = silent drop, no CRM write either.

### Phase 2 cascade tiers (rep DM)

| Tier | Score | Emoji | Slack heading |
|---|---|---|---|
| Highest priority | 27+ | `:red_circle:` | `*HIGHEST PRIORITY* - Score 27+` |
| Strong signals | 18-26 | `:large_orange_circle:` | `*STRONG SIGNALS* - Score 18-26` |
| Worth reviewing | 12-17 | `:large_yellow_circle:` | `*WORTH REVIEWING* - Score 12-17` |

Skip empty tier headings.

## Source Coverage Mandate (anti-laziness)

**Every source documented in every Stage 1 sub-stage MUST be attempted every run, no exceptions.** This rule exists because the routine has a natural tendency to optimize for runtime by silently skipping sources that:

- Returned 0 hits last week ("low yield" - but a quiet Tuesday is not a reason to skip Monday)
- Are slow to scrape (multi-page paginated sites, JavaScript-heavy pages, rate-limited APIs)
- Returned errors on prior runs (transient 5xx, DNS hiccups, captcha challenges)
- Look obscure relative to the routine's existing canon (state BEAD portals, individual NeoCloud blog feeds, niche TSD press pages)

**None of those are valid reasons to skip a source.** A source that returned 0 hits last week may have 3 hits this week. A source that errored last week may be back online. A slow source still has to be scraped - the routine has a 90-minute runtime budget and that's the budget envelope, not "however long is convenient."

### Hard rules

1. **Attempt every documented source.** Each Stage 1 sub-stage has an explicit source list (below). Every single source must be hit on every run, period.
2. **An unreachable source is an ERROR, not a skip.** If a source returns 5xx, DNS-fails, captcha-walls, hits a paywall, or otherwise can't be scraped, log it in Cooper's run report under "Source Coverage - Failures" with the source name + URL + error type. Do NOT silently move on. Cooper needs to know which sources are broken so we fix them or replace them.
3. **A source returning 0 hits is NOT an error.** It's a clean run on that source for the week. Log "0 hits" in the per-source coverage table - that's still attempted-and-completed, just no signals matched. Repeated 0-hit weeks across multiple runs IS a problem (the source may be dead, the regex pattern may be wrong, or it may have been the wrong source for our segment all along), and the per-source coverage log lets Cooper spot that pattern.
4. **No "this source was checked yesterday" optimization.** Each Monday run is its own independent scrape window. Caching across runs is not allowed for the source-attempt count - every Monday, every source gets attempted. (Within-run caching of source content per-page is fine, that's just efficient scraping.)
5. **Runtime budget governs ORDER, not COMPLETENESS.** If the routine is approaching its 90-minute budget, it does NOT skip remaining sources. It either: (a) reduces depth-per-source (e.g., scrape only the last 7 days of an RSS feed instead of paginating to 30 days), or (b) flags itself as "ran out of runtime budget - N sources processed at reduced depth" in Cooper's run report. Skipping sources entirely is never the right answer.

### Per-source accountability in Cooper's run report

Cooper's run report MUST include a "Source Coverage" table covering every documented source across all 6 sub-stages (Colo, Fiber, NeoCloud, Network Op, MSP-Aggregator, Enterprise), formatted:

```
| Sub-stage | Source                          | Attempted | Hits | Status            |
|-----------|--------------------------------|-----------|------|-------------------|
| Colo      | DCD News                       | ✓         | 3    | OK                |
| Colo      | Data Center Frontier           | ✓         | 1    | OK                |
| Colo      | NoVA planning department docket| ✓         | 0    | OK (quiet week)   |
| Colo      | Hydro Quebec interconnect queue| ✗         | -    | ERROR: 503 Server |
| Fiber     | Fierce Network daily           | ✓         | 2    | OK                |
| Fiber     | NTIA BEAD portal               | ✓         | 1    | OK                |
| Fiber     | Vermont state BEAD office      | ✓         | 0    | OK (quiet week)   |
...
```

Every source in every sub-stage gets a row. ✓ = attempted (regardless of yield); ✗ = error (logged in Failures section with detail). This table is the audit trail that proves the routine didn't get lazy this week.

**Source Coverage - Failures sub-section** lists every ✗ row with:
- Source name + URL
- Error type (HTTP status / DNS / captcha / paywall / regex-no-match-but-page-loaded)
- Last-known-good run date for that source (if tracked across runs)
- Suggested action (retry next week / replace source / develop alternative)

Repeated failures (same source ✗ for 3+ consecutive weeks) get auto-flagged as "Source needs development - Cooper review."

### Source quality reality

Honest framing for Cooper: not every documented source is equally developed.

**Robust sources (high reliability, well-structured):**
- SEC EDGAR (8-K, S-4, 10-Q, 13D filings - all parseable)
- PeeringDB API + IX participant lists
- GitHub commit feeds for public repos (CAMARA, Nephio, ONAP, OpenConfig, Sylva)
- LinkedIn public posts + Greenhouse / Lever / Ashby public job boards
- Major trade press RSS (Fierce Network, Light Reading, DCD, Data Center Frontier, TechCrunch, ChannelE2E)
- Apollo MCP (when budget allows)

**Medium-development sources (work but yield varies):**
- Conference agenda pages (PTC, Capacity, ITW, AfricaCom - some require login)
- Earnings call transcripts (Seeking Alpha free tier limited; SEC 10-Q is the reliable fallback)
- TM Forum press + Catalyst announcements (membership-walled in places)
- ScanSource / TD SYNNEX investor pages (HTML changes break scrapers)
- Crunchbase News (free tier rate-limited)

**Aspirational sources (documented but coverage thin until developed):**
- 50 individual state BEAD portals - most have no RSS, layouts vary, manual scrape required
- City planning department dockets (NoVA / Phoenix / Dallas / etc.) - government sites, varying tech, no consistency
- Electric utility interconnection queue listings (some are PDFs only, some require captcha)
- Niche per-NeoCloud blog feeds (single-page rebuilt JS apps, hard to RSS)
- TheOrg diffs (free tier, limited org coverage)
- TSD press pages (many TSDs publish irregularly)

**The mandate covers all three tiers.** Aspirational sources MUST still be attempted. Their per-source rows in the audit table are how we discover whether they're worth keeping in the source list. After 4-6 weeks of run data, Cooper can review the per-source coverage and prune sources that consistently fail or yield 0, OR escalate development effort on sources we know SHOULD have signals but aren't yielding (probably regex/pattern issues, not source death).

## Stage 1: Per-Segment Signal Scrape (Phase 2 - go deep by ICP)

Stage 1 splits into 5 parallel sub-stages, ONE PER ICP SEGMENT. Each sub-stage uses its own dedicated source list and scrapes both Tier A and Tier B signals for its segment. The point is depth: each segment has unique sources, unique signal patterns, and unique buyer-trigger windows that get diluted when scraped as one monolithic pass.

**Run all 6 sub-stages.** Don't skip any segment because "this is a NeoCloud-heavy week" - exec hires, M&A, and BEAD awards are happening in every segment every week, and a thin segment one week will be heavy the next. The depth-per-segment is the value, not the sub-stage selection. (Enterprise sub-stage added 2026-05-11 - may run thin during the 4-6 weeks post-promotion source validation period.)

For each sub-stage, read the segment's signal catalog (`context/signals/[segment]-signals.md`) AND the segment cheatsheet (`context/segments/[segment].md`) AND the segment's source list (defined below) before scraping. The cheatsheet tells you which signal-to-message mappings are relevant; the catalog defines the signal patterns; the source list is what to scrape.

### Stage 1.A - Colocation segment scrape

**Target list:** target-company list filtered to `customer_segment = "Data Center Colo Provider"` (or sub-segment "AI Signals - colo").

**Signal inventory (Tier A + B):** All 7 Colo Tier A codes (C-A0 through C-A7) + all Colo Tier B codes + all universal signals (U1, U2, U3, AP-1, AP-2, AP-7, FR-1, I1).

**Canonical source list:** `context/signals/colocation-signals.md` → "Sources for This Segment" (Phase 2 expanded 2026-04-27). The catalog is the single source of truth - every Robust + Medium + Aspirational source documented there must be attempted per the Source Coverage Mandate above. Validation patterns per Tier A signal are also documented in the catalog.

**Output:** `colo_signals[]` - list of detected signals tagged with `segment = "colo"` + per-signal source attribution + confidence per the validation-pattern rules.

### Stage 1.B - Fiber segment scrape

**Target list:** target-company list filtered to `customer_segment = "Fiber Operator"`.

**Signal inventory (Tier A + B):** All 9 Fiber Tier A codes (F-A1 through F-A9) + all Fiber Tier B codes + all universal signals.

**Canonical source list:** `context/signals/fiber-signals.md` → "Sources for This Segment" (Phase 2 expanded 2026-04-27). Includes Robust tier (Fierce Network, Light Reading, Lightwave Online, Telecompetitor, BroadbandCommunities, SEC EDGAR public fiber operator filings, NTIA BEAD Progress Dashboard, Federal Register, USTelecom + NTCA + FBA + INCOMPAS, supplier customer-win press from Lit Comm / CommScope / Calix / Adtran), Medium tier (state broadband offices, BroadbandBreakfast, conference agendas, ABS market data from Fitch / Moody's / KBRA), Aspirational tier (FCC EDOCS, state PUC dockets, Wayback Machine, Reddit). Validation patterns per Tier A signal are documented in the catalog.

**Output:** `fiber_signals[]` with per-signal source attribution + confidence.

### Stage 1.C - NeoCloud segment scrape (highest velocity)

**Target list:** target-company list filtered to `customer_segment = "NeoCloud"` across all 5 sub-segments.

**Signal inventory (Tier A + B - NeoCloud has the most signal types):** All 11 NeoCloud Tier A codes (NC-A0 through NC-A11; runtime prefix `NC-` for disambiguation from Network Op `NO-`) + all NeoCloud Tier B codes + all universal signals + Crypto-to-AI Pivot signals from `context/segments/neocloud.md`.

**Canonical source list:** `context/signals/neocloud-signals.md` → "Sources for This Segment" (Phase 2 expanded 2026-04-27). Broadest source coverage of any segment. Includes Robust tier (DCF + DCD + The Register, NVIDIA Newsroom + Partner pages, SEC EDGAR public filers + Form D Reg D filings, PeeringDB API, IX member-list pages, MLCommons MLPerf, HPCwire / AnandTech / The Next Platform / ServeTheHome, Crunchbase News, LinkedIn / Greenhouse / Lever / Ashby, Apollo MCP), Medium tier (The Information GPU economy newsletter, Compute Forecast newsletter, Latent Space, Last Week in AI, Import AI, AI Index Stanford HAI, SemiAnalysis, per-NeoCloud blog feeds, Hugging Face Spaces partner announcements, WGMI ETF, Moody's / DBRS / CoinDesk debt raises, NVIDIA GTC + AI Infrastructure Summit + KubeCon AI day), Aspirational tier (Reddit r/LocalLLaMA + r/MachineLearning, Glassdoor reviews, Wayback Machine, YouTube transcripts). Validation patterns per Tier A signal documented in the catalog.

**Output:** `neocloud_signals[]` with per-signal source attribution + confidence.

### Stage 1.D - Network Operator segment scrape

**Target list:** target-company list filtered to `customer_segment = "Network Operator(Tier 1 / VNO)"`.

**Signal inventory (Tier A + B):** All 10 Network Op Tier A codes (NO-A1 through NO-A10; runtime prefix `NO-`) + all Network Op Tier B codes + all universal signals.

**Canonical source list:** `context/signals/network-operator-signals.md` → "Sources for This Segment" (Phase 2 expanded 2026-04-27). Includes Robust tier (Company IR pages + SEC EDGAR daily including 20-F for foreign issuers, Fierce Network + Light Reading + TelecomTV + Capacity Media + RCR Wireless + Total Telecom, Ciena/Nokia/Cisco/Juniper/Arista/Infinera supplier customer-win press, MEF/Mplify + TM Forum + Catalyst, GSMA + CAMARA, GitHub commit feeds for CAMARA/Nephio/ONAP/OpenConfig/Sylva, SEC 10-Q earnings transcripts keyword-filtered, FedBizOpps + SAM.gov RFI/RFP), Medium tier (TIA + USTelecom + CTIA, ONUG, ONF, LFN member commits, ETSI + 3GPP + IETF working groups, Mobile World Live, Mobile Network UK), Aspirational tier (Wayback Machine, Reddit, Glassdoor, YouTube transcripts from MWC + TM Forum DTW + Network X + ITW). International coverage elevated for Tim Z's territory. Validation patterns per Tier A signal documented in the catalog.

**Output:** `network_op_signals[]` with per-signal source attribution + confidence.

### Stage 1.E - MSP / Aggregator segment scrape

**Target list:** target-company list filtered to `customer_segment = "MSP/Aggregator"` (renamed 2026-05-07 from the deleted legacy value `Enterprise`).

**Signal inventory (Tier A + B):** All 7 MSP Tier A codes (M-A1 through M-A7) + all MSP Tier B codes + universal signals (especially U1 exec hire, U2 M&A close, AP-7 PE filter, FR-1 8-K).

**Canonical source list:** `context/signals/msp-aggregator-signals.md` → "Sources for This Segment" (Phase 2 expanded 2026-04-27). Includes Robust tier (Channel Futures + ChannelE2E + CRN, TSD press pages from Telarus / AppDirect / Sandler / AVANT / Bridgepointe / Upstack / AppSmart / Intelisys, FCC Daily Digest, SEC EDGAR public TSDs, ScanSource + TD SYNNEX investor relations + 10-Q transcripts, Megaport / Console Connect / PacketFabric partner-add announcements, LinkedIn / Greenhouse / Lever / Ashby, Apollo MCP), Medium tier (CompTIA, Channel Partner Insight UK, IT Europa, ChannelBiz DACH, FedRAMP Marketplace, Telecompetitor channel section, conference agendas, Gartner SD-WAN MQ + Forrester Wave + Frost & Sullivan, TBI Connect UK, Channel Asia), Aspirational tier (Wayback Machine line-card diffs - high-yield where it works, Reddit r/sysadmin + r/MSP, Glassdoor, TheOrg). **Strict adherence to IT MSP Test** in `context/segments/msp-aggregator.md` - must filter out helpdesk / cybersecurity MSPs from M-A4 AI Practice signals. Validation patterns per Tier A signal documented in the catalog.

**Output:** `msp_signals[]` with per-signal source attribution + confidence.

### Stage 1.F - Enterprise (Multi-DC ICP) segment scrape (NEW 2026-05-11)

**Target list:** target-company list filtered to `customer_segment = "Enterprise-CustomerSegment"` across all four sub-segments (`Financial Services - Enterprise`, `Healthcare Systems - Enterprise`, `Retail and Distribution - Enterprise`, `Outsourcing Services - Enterprise`).

**Signal inventory (Tier A + B):** All 7 Enterprise Tier A codes (E-A1 through E-A7) + all Enterprise Tier B codes + universal signals (especially U1 exec hire, U2 M&A close, AP-7 funding/M&A filter, FR-1 SEC 8-K). Apply the IT MSP Test inversely - **EXCLUDE consulting firms (Deloitte / McKinsey / BCG / Bain) from Outsourcing Services - Enterprise classification per `context/segments/enterprise.md`** - those are project firms, not operational BPOs.

**Canonical source list:** `context/signals/enterprise-signals.md` → "Sources for This Segment" (~37 sources). Includes Robust tier (SEC EDGAR full-text 10-K + 10-Q + 8-K Items 1.01/2.01/5.02/8.01 + DEF 14A + 20-F, PR Newswire + Business Wire People-on-the-Move tag, American Banker + Modern Healthcare + Becker's Hospital Review + Retail Dive + Nelson Hall + Everest Group, LinkedIn + Greenhouse + Lever + Ashby for senior network role job postings, Apollo MCP, Equinix newsroom + customer-story page, Megaport customer-success page, HHS OCR portal + NY DFS portal + PCI Security Standards Council news + DORA enforcement updates, NVIDIA Newsroom + Partner pages), Medium tier (Bloomberg AI + tech beat, WSJ tech + CIO Journal, Risk & Insurance + ISMG GovInfoSecurity, CIO.com + InformationWeek, Bisnow Data Center + DCF / DCD when enterprise IT is the lessee, AWS / Azure / GCP customer-case-study pages, Mergermarket + S&P Global Market Intelligence, PitchBook public, Crunchbase News, HIMSS Media + CHIME, RIS News + STORES Magazine, conference agenda scrapers for Sibos / Money 20/20 / HIMSS / NRF / CCW / NASSCOM), Aspirational tier (Wayback Machine month-over-month diffs of Equinix / Megaport / PacketFabric / CoreSite customer-logo pages, Glassdoor reviews of named ICP enterprises, Reddit r/networking + r/sysadmin + r/healthIT, TheOrg.com diffs, regional business journals, YouTube transcripts of conference talks). Validation patterns per Tier A signal documented in the catalog.

**International sub-stage notes:** Enterprise EMEA + APAC have meaningful Financial Services + Outsourcing Services density (London + Frankfurt FS hubs; India + Manila + Cebu BPOs). Apply EMEA / APAC source overlay per `context/signals/enterprise-signals.md` "International Sources" section. Tim Z's territory captures these.

**Output:** `enterprise_signals[]` with per-signal source attribution + confidence.

### Stage 1.G - Aggregate

Combine `colo_signals[] + fiber_signals[] + neocloud_signals[] + network_op_signals[] + msp_signals[] + enterprise_signals[]` → `detected_signals[]`. Dedup by `(company_domain, signal_code, source_url_hash)` - a signal that fires for the same company across multiple sources gets one entry, not three.

**Per-segment detection counts go in Cooper's run report** so we can see where coverage is thick or thin. If a segment scrapes < 5 signal hits in a week, surface that as "thin coverage - investigate sources" so Cooper can add sources or adjust scrapers. (Enterprise sub-stage may run thin in early weeks during source validation - this is expected; do not auto-flag as a coverage failure during the first 4-6 weeks of Enterprise sourcing.)

## Stage 3: New Account Enrichment (Phase 3 - full R1 5-stage pipeline)

### Apollo Credit Soft Floor
Before starting new-account enrichment, check remaining Apollo credits for the current billing cycle. If remaining < 20% of monthly allocation, PAUSE new-account enrichment (process only accounts already matched in Stage 2). Surface in Cooper's run report: `"Apollo credits at X% of monthly allocation - N net-new companies deferred to next run."` Queue deferred companies for next Monday.

### For each new company (domain not in HubSpot)

Stage 3 NEW-account creation runs the canonical R1 Fresh Enrichment 5-stage pipeline per `context/account-tiering/enrichment-protocols.md`. Do NOT use a shortened 3-phase variant here - Phase 3 requires the full research-first workflow so net-new accounts created by Signal Scan are at the same enrichment quality bar as records flowing through R1 directly.

1. **D1 disqualifier check (run FIRST, before any enrichment work):** Apply the D1 disqualifier rules from `enrichment-protocols.md`. If the candidate domain hits a disqualifier (MaiaEdge self, parked / for-sale, holding company shell with no operating presence, deleted from HubSpot within the past 90 days, etc.), drop silently - do NOT create a HubSpot record.
2. **Stages 1-5 of the R1 research-first workflow** per `enrichment-protocols.md`: D5 v2 protocol governs source order, evidence requirements, and per-stage exit conditions. Returns: `customer_segment`, `company_sub_segment` (from the 30 active values in `sub-segment-qualification.md`), `state`, `country`, `confidence`.
3. **Non-ICP rejection:** If segment is not in Colo / Fiber / Network Op / NeoCloud / MSP/Aggregator / **Enterprise-CustomerSegment**, drop silently. DO NOT create HubSpot record. For Enterprise candidates, the scale gate must pass during enrichment ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng + vertical match in one of the four Enterprise sub-segments). Segment-classification routes scale-gate failures to `Other` - those are non-ICP and do not get created.
4. **No-default-manual-review classification:** Best-fit classification with calibrated confidence. Do NOT default to `manual_review_required` whenever the routine is uncertain - that is a regression we are explicitly correcting. Target manual_review_required population is **under 5%** of Stage 3 NEW-account creates. If you can defensibly pick a sub-segment with MEDIUM or higher confidence, do so. Reserve MANUAL_REVIEW for genuine three-way-tie ambiguity (e.g. a colo-or-neocloud-or-MSP candidate where the website is genuinely unclear after the 5-stage research pass).
5. **Apply crm-guardian safety tiers:**
   - **HIGH** confidence -> Tier 1 auto-create in HubSpot
   - **MEDIUM** confidence -> Tier 2 auto-create + flag in run report
   - **LOW / MANUAL_REVIEW** -> Tier 3 hold (surface in rep's "possible new accounts - review needed" section, do NOT auto-create)
6. **Sub-segment value validation:** every `company_sub_segment` write at Stage 3 must be one of the 30 active values in `context/account-tiering/sub-segment-qualification.md`. Specifically watch for: `Tier 1 Carrier - Network Op` (NOT the legacy "Tier 1 Global Incumbent"); `Managed Network Services - MSP` (NOT the legacy `- Network Operator` suffix); `Crypto to AI - Neoclouds` for both operator AND landlord variants of crypto-to-AI pivots (Cooper 2026-05-14 - do not split these into separate values); `Greenfield` is a real, active sub-segment for Colo and NeoCloud (not deprecated, do not route around it); `Subsea cable operator` is the new 30th value (2026-05-14) for Fiber records where the company's primary asset is a subsea cable system.
7. **Run territory-manager** on every created account. Assign `hubspot_owner_id` based on state/country:
   - US East (30 states per `territory-model.md`) -> `161889085` Tim Lieto
   - US West (20 states + DC) -> `162339176` Ken Cunningham
   - International (country != US) -> `159350430` Tim Ziemer
8. **Run account-brief skill** to populate initial `account_brief` field.
9. **Populate `recent_news_or_trigger_event`** with the signal that surfaced them, in the standard format.
10. **Stamp `last_enriched_date` = today.** Stage 3 NEW-account creation IS a full enrichment pipeline pass, so per the CLAUDE.md Unified Stamping Policy it DOES bump `last_enriched_date`. (This is distinct from Stage 5 partial writes and the new Stage 5b tier recompute, which do NOT bump.)
11. **Initialize Phase 3 signal fields on the new record:** `last_signal_score` = the score of the signal that surfaced this account; `last_signal_date` = today; `signal_count_last_30d` = count of signals on this account this run (typically 1 for net-new). These three fields are required so Stage 5b's tier recompute has the inputs it needs on the very next run.

## Stage 5: HubSpot Field Updates

For each account in `scored_accounts`:

1. Write `recent_news_or_trigger_event` (highest-scored signal this week) in format: `"[YYYY-MM-DD] [Signal Type] - [one-line summary]"`. Hard cap 250 chars - truncate intelligently.
2. If 2+ signals hit, append `"Also this week: [short list]"` line to `account_brief` (stay under 400 char total).
3. Regenerate `account_brief` via account-brief skill if EITHER:
   - (a) existing brief is >30 days old at match time, OR
   - (b) fresh signal research materially diverges from existing brief (e.g., facility count changed, sub-segment shifted, anchor tenant announced that's not in the brief).

   If research closely matches existing brief, leave it.
4. If site-count transition confirmed (Colo or NeoCloud), REWRITE `infrastructure_profile` with updated count + context.
5. Set `last_enriched_date` to today.
6. Apply deal protection flagging for any write on an account with an open deal.

Use HubSpot MCP batch update endpoints where available (10 writes/sec max, exponential backoff 1s → 2s → 4s on HTTP 429). Dead-letter any write that fails after retries to the run report's "HubSpot write failures" section.

## Stage 5b: Signal Field Persistence + Tier Recompute (Phase 3 - NEW)

Stage 5b runs AFTER Stage 5 partial writes complete. It executes once per account where any signal scored >=8 this run (i.e. every account that received a `recent_news_or_trigger_event` write OR was a Watch List 8-11 write OR was a top-cascade rep DM surface). Accounts that scored below 8 this run are skipped - Stage 5b does not touch them.

Stage 5b is a Stage 5 partial-write extension and is governed by the same CLAUDE.md Unified Stamping Policy invariant: **it does NOT bump `last_enriched_date`.** Only full-pipeline passes (Stage 3 NEW-account creates, R1 alpha path, R2 RE_ENRICH_FULL with gate pass, definitive evictions) bump that field. R2's 120-day rotation owns the freshness guarantee - Signal Scan partial writes must not hide hot accounts from R2.

### Inputs Stage 5b needs

For each in-scope account, gather:
- Current `account_tier` (HubSpot value pre-recompute)
- Current `customer_segment` and `company_sub_segment`
- Current `hs_is_target_account` (boolean; was previously `target_account` - field has been renamed)
- Highest signal score this account received this run -> `new_signal_score`
- Count of distinct signal events on this account this run -> `new_signal_event_count`
- Existing `last_signal_score`, `last_signal_date`, `signal_count_last_30d` from HubSpot (may be null for accounts that have never received a signal write before)
- Open deal associations (deals where `hs_is_closed_won = false` AND `hs_is_closed_lost = false`)
- `notes_last_contacted` / activity timestamps for the stale / sustained-quiet modifier check (per `tier-compute-spec.md`)

### Signal field writes (always run - applies regardless of `hs_is_target_account`)

For every account where `new_signal_score >= 8`:

1. `last_signal_score` = `max(existing_last_signal_score_if_within_30d, new_signal_score)`. If the existing `last_signal_date` is older than 30 days OR null, just write `new_signal_score`. The field captures the highest score in the recent window, not a lifetime maximum.
2. `last_signal_date` = today's run date (YYYY-MM-DD, America/New_York).
3. `signal_count_last_30d`:
   - If existing `last_signal_date` is null OR older than 30 days -> reset: write `new_signal_event_count` (this run is the start of a new 30-day window).
   - If existing `last_signal_date` is within 30 days -> increment: write `existing_signal_count_last_30d + new_signal_event_count`.

These three signal field writes proceed unconditionally for every in-scope account, including accounts where `hs_is_target_account = true`. The hs_is_target_account override only suppresses the tier write below - it does NOT suppress signal field persistence.

### Tier recompute (skipped if `hs_is_target_account = true`)

For every account where `new_signal_score >= 8` AND `hs_is_target_account != true`:

1. **Read default tier** for the account's (segment, sub-segment) pair per `context/account-tiering/tier-compute-spec.md` "Default Tier by Segment + Sub-Segment" table.
   - **Unknown pair handling:** if the (segment, sub-segment) pair is not in the defaults table, fall back to the segment-only default (segment null fallback). If even the segment-only default is missing, leave `account_tier` unchanged and log a warning in Cooper's run report under a new "Stage 5b - Unknown (segment, sub-segment) pairs" section with company name + HubSpot ID + the offending pair. Do NOT write a tier change in this case. This is the graceful-degradation path for sub-segment values that drift out of sync with the spec.
2. **Apply hot / white-hot / stacked-signal modifiers** based on the just-written signal field values (`last_signal_score`, `signal_count_last_30d`) per `tier-compute-spec.md`.
3. **Apply open-deal modifier** based on the account's open-deal associations queried above.
4. **Apply stale / sustained-quiet modifiers** based on `last_signal_date` combined with `notes_last_contacted` and activity timestamps per the spec.
5. **Clamp to ceiling / floor** per the spec (e.g. tier cannot drop below tier_5 or rise above tier_1; some sub-segments have stricter ceilings - defer entirely to the spec).
6. **Compare new_tier to current `account_tier`:**
   - If equal -> no write.
   - If different AND `hs_is_target_account != true` -> write new `account_tier` via HubSpot MCP AND add a HubSpot note on the company record formatted exactly: `"Tier <old> -> <new> on <YYYY-MM-DD> by Signal Scan: <one-line reason citing the dominant modifier>"`. Example reasons: `"hot signal score 27 stacked with 3 events in last 30d"`, `"white-hot E-A2 close + E-A4 exec hire, open deal modifier"`, `"sustained-quiet 60 days, default Tier 3 demoted to Tier 4"`.

### hs_is_target_account = true override

Accounts flagged `hs_is_target_account = true` are reps' manually-pinned strategic accounts. Their tier is intentionally locked. Stage 5b:
- DOES write the three signal persistence fields (`last_signal_score`, `last_signal_date`, `signal_count_last_30d`) - these are observability data, not strategy decisions.
- DOES NOT write `account_tier` (skipped silently - no note, no run-report flag - this is normal behavior for a strategic-pin override).

### Stage 5b overwrite-authority addendum (extends the existing Stage 5 overwrite-authority table)

| Field | Authority | Stamping |
|---|---|---|
| `last_signal_score` | Stage 5b - hard overwrite per algorithm above | does NOT bump `last_enriched_date` |
| `last_signal_date` | Stage 5b - hard overwrite (today) | does NOT bump `last_enriched_date` |
| `signal_count_last_30d` | Stage 5b - rolling-window write per algorithm | does NOT bump `last_enriched_date` |
| `account_tier` (via Stage 5b) | Stage 5b - writes ONLY if new_tier != current_tier AND `hs_is_target_account != true` AND (segment, sub-segment) is in the defaults table | does NOT bump `last_enriched_date` |
| Companion HubSpot note on tier change | Stage 5b - one note per tier change, formatted as specified above | n/a |

### Stage 5b counts in Cooper's run report

Add a "Stage 5b - Signal Field Persistence + Tier Recompute" sub-section:
- Accounts touched (signal field writes)
- Tier writes performed (with old -> new tier breakdown)
- Tier writes skipped due to `hs_is_target_account = true` (count + named accounts)
- Tier writes skipped due to unknown (segment, sub-segment) pair (count + named accounts + offending pairs)
- Tier ceiling / floor clamps activated (count + breakdown)

## Stage 6: Rep Report Generation - Cascade by Score (Phase 1)

### PHASE 0 DELIVERY OVERRIDE - Cooper-only (ACTIVE as of 2026-04-26)

**Per Cooper's instruction: this week is a test. Only Cooper sees output.** Until override is lifted via routine update:

- **Skip** sending to Tim Lieto's `U0A973L1HFF`.
- **Skip** sending to Ken's `U0AE1PGCB6C`.
- Per-rep East/West/International scoring still runs internally (Stage 1-5 HubSpot writes happen as normal - segment classification, `recent_news_or_trigger_event`, account_brief regeneration, new-account creation - the override is delivery-only).
- Consolidate ALL territory cascade lists into a SINGLE combined DM to Cooper at `U0A24D9RJLS`, organized by territory header (`*EAST - TIM LIETO* / *WEST - KEN CUNNINGHAM* / *INTERNATIONAL - TIM ZIEMER*`) so Cooper can review and forward to reps manually.
- Cooper's consolidated run report stays as a SEPARATE second DM to `U0A24D9RJLS` (distinct from the consolidated rep DM) with run-stats + Apollo-budget % + per-rep output sizes.
- Excel attachment via GitHub raw URL gets generated and linked from the consolidated DM (one Excel; can include all 3 territory tabs for Cooper's review).

**The routing table below is the intended-end-state multi-rep delivery for after Cooper approves rep-direct DMs. Follow the override above; the table is the template for each territory section.**

### Generate 3 rep pools (intended end state - gated by Phase 0 override above)

Routing table:

| Territory pool (`hubspot_owner_id`) | Rep label in DM | Slack `channel_id` |
|---|---|---|
| Tim Lieto East - `161889085` | "Tim" | `U0A973L1HFF` (Tim Lieto) |
| Ken Cunningham West - `162339176` | "Ken" | `U0AE1PGCB6C` (Ken Cunningham) |
| Tim Ziemer International - `159350430` | "Tim Z" | `U0A24D9RJLS` (**Cooper** - Phase 1 validation override) |

The DM body still opens "Hey Tim Z" on Cooper's message for Tim Z's territory - content is addressed to the rep, just delivered to Cooper for now.

**Per rep pool:**

1. Filter `scored_accounts` where `hubspot_owner_id` matches that pool's territory.
2. **Apply Phase 2 score floor: drop every account-signal pair scoring below 12 from the rep DM.** Accounts scoring 8-11 are the Watch List - they get HubSpot `recent_news_or_trigger_event` writes at Stage 5 but are NOT included in the rep DM. Below 8 = silent drop.
3. **Apply 40-total cap per rep pool** (was 25 in Phase 1): rank remaining globally (across all segments) by score descending, take top 40. Fewer is fine - if only 18 accounts clear the floor, the list is 18.
4. **Assign color-coded priority tier based on score:**

   | Tier | Score | Emoji | Slack heading |
   |---|---|---|---|
   | Highest priority | 27+ | `:red_circle:` | `*HIGHEST PRIORITY* - Score 27+` |
   | Strong signals | 18-26 | `:large_orange_circle:` | `*STRONG SIGNALS* - Score 18-26` |
   | Worth reviewing | 12-17 | `:large_yellow_circle:` | `*WORTH REVIEWING* - Score 12-17` |

   Skip empty tier headings. If no 27+ accounts this week, don't show the `:red_circle:` block.

   **No "call" language in any rep-facing copy.** Surface which accounts are top-scored; reps pick the outbound channel.

5. **Generate Slack DM body** (cascade structure - no segment-grouped paragraphs in Phase 1):

   ```
   :satellite_antenna: *Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]*

   Hey [Rep First Name] - [N] accounts cleared the Phase 1 quality bar this week. Ranked by score, highest first.

   :red_circle: *HIGHEST PRIORITY* - Score 27+
   • *[Account Name]* (Segment · Tier [1-5]) · Score [N] · <[HubSpot URL]|open>
     [1-2 sentence signal synthesis with persona to reach]

   :large_orange_circle: *STRONG SIGNALS* - Score 22-26
   • ...

   :large_yellow_circle: *WORTH REVIEWING* - Score 18-21
   • ...

   :sparkles: *NEW TO YOUR TERRITORY*
   [N] new accounts enriched + added this week:
   • *[Account]* (Segment) - [signal that surfaced]

   Full 14-column detail (LinkedIn URL, Suggested Angle, full Signal Body, Account Brief): <[GitHub raw Excel URL]|download>
   ```

   MSP segment label in rep-facing output = "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).

6. **Generate Excel attachment** (`.xlsx`) with these columns:

   `Account Name | Customer Segment | Sub-Segment | Account Tier | Account Owner | HubSpot URL | LinkedIn URL | Signal Type | Signal Body | Detection Date | Meeting Probability Score | Account Brief | State | Suggested Angle`

   **Account Tier column reads the FRESHLY-COMPUTED tier (post-Stage 5b)**, not the value that was in HubSpot at the start of the run. Phase 3 change: previously the Excel could show a stale tier on rows where Stage 5b had just promoted or demoted an account, which confused reps reading the priority list. Source the Account Tier value from the in-memory result of Stage 5b's recompute for each in-scope row. For rows where Stage 5b was skipped (e.g. `hs_is_target_account = true` or unknown sub-segment pair), use the current HubSpot value.

   **Sub-Segment column writes one of the 30 active values** from `context/account-tiering/sub-segment-qualification.md`. Never write a legacy value (`Tier 1 Global Incumbent`, `Managed Network Services - Network Operator`, a deprecated `Greenfield`-around alternative, etc.) in the Excel - those are dead vocabulary. If the HubSpot value is a legacy string, surface it through Cooper's run report's "Sub-segment legacy values detected" section so Cooper can clean those records, and write the closest 30-value match in the Excel cell.

   One tab per segment with hits (skip empty segments). Total rows across all tabs ≤ 25 in Phase 1. Sort each tab by score descending.

   **Subtle color coding (score column only, not whole row).** Use `openpyxl` `PatternFill(fill_type="solid", fgColor=...)` on the "Meeting Probability Score" cell:
   - Score 27+ → `FFEBEE` (pastel red)
   - Score 18-26 → `FFF3E0` (pastel orange)
   - Score 12-17 → `FFFDE7` (pastel yellow)

   Every other cell stays white. No bold, no borders beyond Excel default, no header-row color changes. The point is a glanceable score column, not a highlighter spreadsheet.

   **Depth requirements per row:**
   - **Signal Body:** 3-5 sentence synthesis: what happened, when, who's involved, the specific pain it exposes for THIS prospect, a pulled quote from the source + source URL. Reads like mini call-prep, not a headline.
   - **Suggested Angle:** persona-aware and signal-specific. Name the right persona to reach + the signal-appropriate wedge + timing. Use Tim Lieto's voice for his accounts, Ken's for his (see `cold-email SKILL.md`).
   - **Account Brief:** regenerated fresh if stale or content-divergent (per Stage 5 rule). Never a stale brief that contradicts the news row.

7. **Cooper run report** (separate Slack DM to `U0A24D9RJLS`, distinct from Cooper's Tim-Z-territory report):
   - Total signals detected this run
   - **Source Coverage table** (mandatory - every source across all 6 sub-stages with Attempted ✓/✗ + Hits + Status). See Source Coverage Mandate above for format. This is the anti-laziness audit trail.
   - **Source Coverage - Failures sub-section** listing every ✗ row with source / URL / error / suggested action.
   - **Per-segment signal counts** (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / **Enterprise**) - flag any segment with < 5 detections as "thin coverage - investigate sources" (suppress flag for Enterprise during the first 4-6 weeks post-promotion 2026-05-11)
   - **Per-tier signal counts** (Tier A vs Tier B vs paired Tier C) - useful for monitoring Phase 2 vs Phase 1 expansion impact
   - **M&A two-event firing counts** (Announcement events vs Close events vs paired Both - confirms the announcement-stage detection is working)
   - HubSpot accounts touched (breakdown: `recent_news` writes, `infrastructure_profile` rewrites, `account_brief` regenerations, `last_enriched_date` updates)
   - **Watch list count** (accounts scored 8-11 - got `recent_news_or_trigger_event` write but no rep DM)
   - New accounts enriched + added (Tier 1/2/3 breakdown)
   - Tier 3 holds (Cooper review required)
   - Deal-protected writes (flagged for rep awareness)
   - Apollo credits consumed + % of monthly allocation remaining
   - Errors / API failures with record IDs (separate from Source Coverage failures - these are HubSpot/Apollo MCP errors)
   - Per-rep output size (Tim L: N accounts, Ken: M, Tim Z [Cooper]: K) - grouped by score tier
   - Weekly trend vs. prior 4 runs (target metric: 20-40 accounts/rep - Phase 1 was producing 5)
   - **Runtime budget usage** (X minutes of 90-minute envelope) + flag if any source was scraped at reduced depth due to budget pressure

### Zero-Signal Edge Case
If a rep has zero accounts clearing the Phase 1 score-18 floor, send a short Slack DM: `:satellite_antenna: *Weekly Signal Scan - [First Name] - Week of [YYYY-MM-DD]* - Quiet week in your territory. No accounts cleared the Phase 1 signal quality bar. See you next Monday.` No Excel. No padding.

## Stage 7: Output Delivery - Slack DM + Excel in Repo

1. **Write the Excel files** to `weekly-reports/YYYY-MM-DD/` in the repo:
   - `lieto.xlsx` → Tim Lieto's list
   - `ken.xlsx` → Ken's list
   - `ziemer.xlsx` → Tim Z's territory list (currently routed to Cooper)

2. **Write markdown mirrors** of the Slack DM bodies to the same folder for audit trail:
   - `lieto.md`, `ken.md`, `ziemer.md`, `cooper-run-report.md`

3. **Commit + push** to `main`: `"weekly signal scan YYYY-MM-DD - [N] signals / [M] accounts surfaced / [K] new enriched"`

4. **Post Slack DMs** via `mcp__claude_ai_Slack__slack_send_message`:
   - Tim Lieto's cascade report → `channel_id: U0A973L1HFF`
   - Ken's cascade report → `channel_id: U0AE1PGCB6C`
   - Tim Z's territory cascade report → `channel_id: U0A24D9RJLS` (Cooper, Phase 1 override)
   - Cooper's consolidated run report → `channel_id: U0A24D9RJLS` (separate DM, distinct from the Tim Z territory report)

5. **Excel attachment link** in each Slack message: reference the GitHub raw URL for the corresponding `.xlsx` (e.g. `https://github.com/[org]/maiaedge-ai/raw/main/weekly-reports/2026-04-27/lieto.xlsx`). Slack does not support direct binary attachments via `slack_send_message`; the link is the delivery mechanism.

6. **Message size:** 5,000 char/text-element cap. If any rep's cascade exceeds this (rare in Phase 1 with 25-account cap, possible on a heavy M&A week), split: parent message = hero + Call Today + Priority, threaded reply = This Week's List + New to Territory.

## Cross-routine ledger

Per `skills/crm-guardian/SKILL.md` → Cross-Routine Ledger:

- **At run start:** read the `CRM Guardian - Open Items Ledger` Slack canvas via `slack_read_canvas`. Drain any Tier 3 items belonging to weekly-signal-scan from prior runs - re-evaluate against current HubSpot state and resolve where Cooper has acted manually.
- **At run end:** append every NEW Tier 3 hold this run produced (e.g. ambiguous M&A, single-source claims awaiting cross-source confirmation, scoring boundary cases) with `[YYYY-MM-DD]` as `date_first_surfaced`. Persist via `slack_update_canvas`.
- **Canvas ID:** `F0B0AFSB9LN` (URL: `https://maia-edge.slack.com/docs/T06S5P1EGJC/F0B0AFSB9LN`). Read at run start via `slack_read_canvas` for prior context (Active routines table + Tier 3 open items + status emoji conventions). At run end, append ONE row to the canvas's "Run log" table via `slack_update_canvas`:
  `| YYYY-MM-DD | Weekly Signal Scan | <status emoji> | <one-sentence summary> | <artifact links> |`
  Use the status emoji conventions defined in the canvas (do NOT invent new ones). If `slack_read_canvas` fails or the canvas is unreachable, log the error in Cooper's audit DM Errors section and continue - do not abort the routine.

## Failure Modes (handle gracefully)

- Per-record try/except on every HubSpot write, Apollo call, enrichment. Log failures in run report, do NOT abort the whole run.
- Connector failures (HubSpot MCP / Apollo MCP unreachable) → stop cleanly, write partial-state report, exit.
- Rate limit (HTTP 429): pause 10 sec, retry. Three consecutive 429s on same op → skip op, log to run report.
- If Stage 3 Apollo credits exhausted mid-run → process remaining matched accounts only (Stage 2 MATCH companies), skip all NEW companies, surface deferral in run report.
- If scoring produces zero accounts above floor for all 3 reps → still produce 3 "quiet week" emails + Cooper report + commit (normal flow).

## Final Checklist Before Committing + Posting

- [ ] All 6 Stage 1 sub-stages ran (Colo, Fiber, NeoCloud, Network Op, MSP-Aggregator, Enterprise) - per-segment signal counts in Cooper's run report. Enterprise sub-stage (added 2026-05-11) may run thin in early weeks - that's expected during source validation.
- [ ] **Every source documented in every sub-stage was ATTEMPTED** (anti-laziness mandate - Source Coverage table in Cooper's run report has one row per documented source, ✓ or ✗ for each)
- [ ] **Source Coverage - Failures sub-section** populated for every ✗ row with error type + suggested action
- [ ] No source was silently skipped due to "low yield last week" / "slow scrape" / "errored before" / "looks obscure" - those are NOT valid reasons to skip
- [ ] Unreachable sources logged as ERRORS, not silently dropped
- [ ] Both Tier A AND Tier B signal codes were scraped per segment (Tier A ~53 + Tier B ~28 = ~81 signal types, plus paired Tier C)
- [ ] Tier C signals only fired when paired with another signal on the same account in same 30-day window
- [ ] **M&A signals fired on BOTH announcement and close events** (two-event firing - both regex patterns from each M&A signal definition were scraped)
- [ ] **All HubSpot writes (new-account creation + field updates + owner cascades) went through `mcp__claude_ai_HubSpot__manage_crm_objects`** (createRequest / updateRequest). No XLSX or CSV was produced as an import file or as a fallback for any write.
- [ ] The Excel attachment in `weekly-reports/YYYY-MM-DD/[rep].xlsx` is rep-facing prospecting output only, linked from the Slack DM. It is NOT an import artifact.
- [ ] `last_enriched_date` set on every touched account
- [ ] 3 rep markdown files generated + 3 Excel files (≤25 rows each, sorted by score descending, score cell color-coded per tier)
- [ ] Cooper run report generated (separate from Cooper's Tim-Z-territory report)
- [ ] Commit message accurate (signal count + accounts + new enriched)
- [ ] No em dashes in any field writes or output files
- [ ] No competitor products named in outputs
- [ ] MSP shown as "MSP / Aggregator" in rep output
- [ ] All dates in America/New_York timezone
- [ ] Score floor 12 enforced (Phase 2) - nothing below 12 surfaces in rep DMs; 8-11 → Watch List CRM-only writes; below 8 → silent drop
- [ ] Per-rep cap of 40 accounts enforced (Phase 2)
- [ ] Watch List count surfaced in Cooper's run report
- [ ] Cascade headings skip empty tiers (no "0 accounts under CALL TODAY" sections)
- [ ] Slack DMs posted to 3 rep channel_ids + 1 Cooper run-report DM (4 messages total)
- [ ] Tim Z's territory DM routed to Cooper (`U0A24D9RJLS`), not Tim Z (Phase 1 override)
- [ ] Each Slack DM contains the GitHub raw URL for the corresponding Excel download

### Phase 3 additions (2026-05-14)

- [ ] `context/account-tiering/tier-compute-spec.md`, `context/account-tiering/sub-segment-qualification.md`, and `context/account-tiering/enrichment-protocols.md` were loaded at run start
- [ ] **Stage 5b ran** for every account where any signal scored >=8 this run
- [ ] `last_signal_score`, `last_signal_date`, `signal_count_last_30d` were written on every in-scope account (including `hs_is_target_account = true` accounts)
- [ ] `account_tier` was recomputed per `tier-compute-spec.md` (default tier + hot/white-hot/stacked + open-deal + stale/sustained-quiet + clamps)
- [ ] Tier writes were SKIPPED on accounts where `hs_is_target_account = true` (signal field writes still proceeded)
- [ ] HubSpot note written on every tier change, formatted `"Tier <old> -> <new> on <YYYY-MM-DD> by Signal Scan: <reason>"`
- [ ] Stage 5b did NOT bump `last_enriched_date` on any account (verified against Unified Stamping Policy)
- [ ] Unknown (segment, sub-segment) pairs hit the graceful-fallback path (segment null fallback OR no-write + warning log) - none silently broke the run
- [ ] Stage 3 NEW-account creates ran the full R1 5-stage pipeline (D1 disqualifier check + research-first 5-stage workflow per `enrichment-protocols.md`) and DID bump `last_enriched_date`
- [ ] Stage 3 NEW-account `manual_review_required` population is under 5% (no-default-manual-review principle honored)
- [ ] Every `company_sub_segment` value written this run is one of the 30 active values in `sub-segment-qualification.md` (no legacy values like "Tier 1 Global Incumbent" or "Managed Network Services - Network Operator")
- [ ] Excel "Account Tier" column reads the FRESHLY-COMPUTED tier from Stage 5b's in-memory result, not the pre-run HubSpot value
- [ ] All `target_account` references in the run have been replaced with `hs_is_target_account` (field rename)
- [ ] No em dashes in any new content (Stage 5b notes, run-report sections, Excel cells use hyphens)
- [ ] Cooper's run report contains the Stage 5b sub-section (accounts touched, tier writes, hs_is_target_account skips, unknown-pair skips, clamp activations)

Work carefully. Reps depend on this list being accurate. Phase 3 goal: relevance + tier accuracy. Every row a "right account at the right time" at the right tier. Stage 5b is the tier-truth layer - without it, the rep-facing priority list drifts from reality. Target deliverable: 20-40 relevant accounts per rep per week, each at its freshly-computed tier, each earning its place via segment-specific signal evidence + persona-aware angle.
