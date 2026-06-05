---
name: weekly-signal-scan
description: "MaiaEdge Weekly Signal Scan  -  runs Mondays to scrape fresh market signals across all 5 ICP segments (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator) using per-segment Tier A + Tier B catalogs. Detects buildouts, M&A, exec hires, anchor leases, BEAD awards, GPU debt, NaaS launches and similar. Updates recent_news_or_trigger_event on matched HubSpot accounts, enriches net-new accounts, and delivers one Slack DM per rep territory (Tim Lieto East, Ken Cunningham West, Tim Ziemer International) with a score-cascaded prospecting list and Excel attachment. Use when asked to run weekly signals, generate the Monday brief, refresh news fields, scan for trigger events, build the weekly prospecting list, or produce rep territory reports. Orchestrated by crm-guardian (weekly Mondays) or invoked directly."
---

# MaiaEdge Weekly Signal Scan

## Purpose

Every Monday morning, put the highest-leverage weekly prospecting list in each rep's hands  -  one ranked by fresh, public, time-bound signals that indicate meeting probability is unusually high this week. The skill closes the gap between MaiaEdge's existing enrichment (one-shot at account creation) and the real world (new facts every day).

Three outcomes per run:
1. **Update `recent_news_or_trigger_event`** on every existing HubSpot account that hit a signal this week (≤250 char, formatted per spec).
2. **Enrich + add** any net-new companies detected in signals but not yet in HubSpot  -  via `company-enrichment` + `crm-guardian` safety tiers.
3. **Deliver 3 Slack DMs** (one per rep territory), each with a cascade-ranked account list (hottest signals at top) + Excel attachment. One tab per segment with hits, max 25 accounts TOTAL per rep during **Phase 1 (Tier A signals only, score floor 18)**.

This is an orchestration skill. It defines WHAT to scrape, WHEN, and HOW to score. Sub-skills define the rest.

## Phase 2 — Relevance-Expanded (current mode, as of 2026-04-27)

**Phase 1 produced 5-account weeks aggregate across all reps.** The 18-floor + Tier-A-only constraint was over-restrictive — under the formula `Tier × Freshness × Confidence` (max 27), score 18 requires HIGH freshness × HIGH confidence × Tier A, leaving 30-day-old MEDIUM signals filtered even when they're genuinely buying-trigger relevant. Phase 2 expands coverage:

- **Tier A AND Tier B both active.** Tier B = "strong, 30-90d window" signals (partnerships, network upgrade press, planning-stage greenfield filings, CTO podcast appearances, OpenStack/Kubernetes commits, TM Forum membership). Phase 1 disabled these as "noise"; the 5-account result proved that was wrong.
- **Tier C paired-only.** Tier C signals (job posts, conference appearances, generic blogs) score only when stacked with a Tier A or Tier B on the same account in the same 30-day window — signal-stacking confirms the trigger event has multiple downstream observables.
- **Score floor 12** (was 18). Below 12 = silent drop. Score 8-11 → Watch List (CRM `recent_news_or_trigger_event` write only, no rep DM).
- **Cap 40 per rep** (was 25). With Tier B on, more relevant accounts surface.
- **Target list expanded to Tier 1+2+3 ICP** (was Tier 1+2). Tier 3 ICP accounts have legitimate exec hires and hiring spikes worth surfacing.
- **Per-segment Stage 1 sub-stages** — each ICP segment scrapes from its dedicated source list (defined in Stage 1 below) instead of one monolithic pass. This is the depth Cooper asked for: relevance-graded coverage of the right accounts at the right time, by segment.

**Relevance is the goal.** Phase 2 isn't volume — it's coverage of every account where MaiaEdge's message resonates THIS week because of what's happening at the account. Target deliverable: 20-40 relevant accounts/rep/week.

The Tier A catalog below is preserved (Phase 2 still scrapes ALL of Tier A); the Tier B catalog is now also scraped per segment (see segment signal files under `context/signals/[segment]-signals.md` "Tier B" sections).

### Phase 2 signal inventory — must scrape ALL of these every run, ACROSS BOTH Tier A AND Tier B per segment

**Universal signals (fire across all 5 segments):**
| Code | Signal | Why it's priority |
|------|--------|-------------------|
| U1 | Exec hire in network / infra / automation role | 90-day mandate window; single highest-confidence relationship-entry signal |
| U2 | M&A / PE roll-up closing | 60-90 day post-close integration window; explicit Cooper priority |
| U3 | New facility / market / site launch | Fresh connectivity project starting day one |
| AP-1 | Apollo job change to target persona (<90d) | Apollo-native; standalone OK |
| AP-2 | Apollo competitor / adjacent-employer lateral | Apollo-native; standalone OK |
| AP-7 | Apollo funding / M&A filter | Richer metadata than U2; overlaps are fine |
| FR-1 | SEC 8-K Item 5.02 + material contracts | Highest-fidelity M&A / exec-change surface |
| I1 | International state-aid / sovereign funding award | +3 bonus; greenfield-equivalent internationally |
| I2 | Sovereign AI grant / compute allocation | +3 bonus; core NeoCloud international signal |

**Colocation Tier A (7 signals — full list from `colocation-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| C-A0 | Greenfield Build Stage S2/S3 (permit + utility interconnection) | **GREENFIELD** — +3 bonus at S2/S3, 9-15 months of influence before fit-out |
| C-A1 | Site Count Transition 1→2 Facilities | **GREENFIELD** — +6 bonus, first-ever multi-site design decision |
| C-A2 | GPU Cloud Tenant Anchor (Lambda/Crusoe/Nebius/Nscale/Together) | **BIG SIGNING** — meeting-ready the week of the press release |
| C-A3 | Liquid Cooling / D2C Deployment | AI-tenant readiness confirmed; "solved power, now solve determinism" opener |
| C-A4 | Executive Hire — VP/Dir of Interconnection / Network / Fabric | 90-day plan includes fabric or cross-connect fix |
| C-A5 | Network Engineering Job-Req Surge (3+ concurrent in 30d) | Operator is building something they don't have |
| C-A6 | Anchor Tenant Signing (hyperscaler OR enterprise OR neocloud) | **BIG SIGNING** — broader than C-A2; build-to-suit or multi-year MSA |
| C-A7 | Merger / Acquisition / PE Recap | **BIG ACQUISITION** — explicitly promoted from Tier B per user feedback; Day 60-90 post-close sweet spot |

**Fiber Tier A (9 signals — full list from `fiber-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| F-A1 | BEAD Subgrant Award | **GREENFIELD** — 4-year build obligations, 18-24 month provisioning ramps |
| F-A2 | Regional Fiber PE Acquisition / Roll-up Close | **BIG ACQUISITION** — first 90 days = OSS/BSS unification pain |
| F-A3 | AI Data Center Lit / Dark Fiber Win or RFP | **BIG SIGNING** — 800G/1.6T AI interconnect exposes cross-footprint gaps |
| F-A4 | NaaS / Automation / Portal Launch | Competitor proof-of-struggle; active buyers hitting NNI wall |
| F-A5 | Executive Hire — VP Network Automation / CNO / VP Wholesale / VP Carrier Relations | 90-day modernization mandate |
| F-A6 | Dark Fiber IRU / Long-Haul Sold-Out | Monetization urgency peaks |
| F-A7 | Merger / Acquisition / Consolidation (broader than F-A2) | **BIG ACQUISITION** — any fiber M&A; 60-120 day post-close window |
| F-A8 | ABS / Refinancing / Secured Debt Issuance | CFO-level urgency for revenue-growth platform spend |
| F-A9 | Consortium / Federation / Co-op Announcement | Federation-readiness; direct thesis fit |

**⚠️ Code collision warning:** Both `neocloud-signals.md` and `network-operator-signals.md` use the `N-A*` prefix in their catalog files. When referencing signals in this skill's code / prompts / reports, always qualify with the segment: `NeoCloud N-A2` vs `NetworkOp N-A2`. Never use bare `N-A2` — it's ambiguous. Below, each table row's code prepends the segment abbreviation (`NC-` for NeoCloud, `NO-` for Network Operator) to the catalog code.

**NeoCloud Tier A (11 signals — full list from `neocloud-signals.md`, highest-velocity segment):**
| Runtime code | Catalog code | Signal | Explicit Cooper priority |
|------|------|--------|--------------------------|
| NC-A0 | N-A0 | Greenfield Build Stage S2/S3 (permit + utility + GPU-backed debt) | **GREENFIELD** — +3 bonus; NeoClouds lease colo so debt is earliest signal |
| NC-A1 | N-A1 | Site Count Transition 1→2 Regions | **GREENFIELD** — +6 bonus, first-ever multi-region design |
| NC-A2 | N-A2 | New Facility / Region Launch (N→N+1) | **GREENFIELD** — 6-week connectivity project starting day one, 1wk freshness |
| NC-A3 | N-A3 | NVIDIA DGX Cloud Lepton / NCP / Exemplar Cloud Partner Announcement | NVIDIA's own marketplace requires observability they don't have |
| NC-A4 | N-A4 | Enterprise Customer Win (non-hyperscaler) | Scaling-wall moment; first enterprise logo = onboarding pain hits |
| NC-A5 | N-A5 | GPU-Backed Debt Raise / Credit Facility | Existential network-quality pressure |
| NC-A6 | N-A6 | Network / SRE / Observability Hiring Spike | First-ever network role = highest signal |
| NC-A7 | N-A7 | Anchor Tenant Signing (enterprise or hyperscaler) | **BIG SIGNING** — dual-fires with colo C-A6 |
| NC-A8 | N-A8 | Colo Lease Filing (SEC 8-K Item 1.01 / 2.03) | **BIG SIGNING** — dual-fires with colo; 4 business days from execution |
| NC-A9 | N-A9 | PeeringDB Changes (new netixlan / netfac / prefix) | Public-record new site coming online |
| NC-A10 | N-A10 | IX Member Addition (100G/400G port) | Open for peering flag; port-live date |
| NC-A11 | N-A11 | MLPerf Inference / Training Submission | Production-stable fabric; promoted from Tier C April 2026 |

**Network Operator Tier A (10 signals — full list from `network-operator-signals.md`):**
| Runtime code | Catalog code | Signal | Explicit Cooper priority |
|------|------|--------|--------------------------|
| NO-A1 | N-A1 | Private Connectivity Fabric Copycat / Multi-Billion AI Deal | **BIG SIGNING** — Lumen $13B PCF precedent; boards asking for responses |
| NO-A2 | N-A2 | Earnings Transcript Mentions (NaaS/API/Private Fabric/Programmable) | Strategy teams already tasked with progress |
| NO-A3 | N-A3 | Executive Transition — CTO / CNO / VP Automation / Chief Network Strategy | 90-day window |
| NO-A4 | N-A4 | Wholesale / Consumer Divestiture or Spin-off | **BIG ACQUISITION-ADJACENT** — Lumen playbook; post-divestiture peak window |
| NO-A5 | N-A5 | GitHub Commits from @carrier.com to CAMARA / Nephio / ONAP / OpenConfig / Sylva | Engineering investment in programmable infrastructure |
| NO-A6 | N-A6 | TM Forum Autonomous Networks Self-Assessment | Leading indicator of where they want to go |
| NO-A7 | N-A7 | SRv6 / Segment-Routing Production Rollout | Dataplane readiness; control-plane gap is where MaiaEdge fits |
| NO-A8 | N-A8 | Public RFI / RFP — Multi-Domain Orchestrator / TE Controller / Inter-Carrier Automation | **Most direct buying signal** — actively procuring |
| NO-A9 | N-A9 | PCEP / SR-TE / BGP-LS / YANG-NETCONF Job Requisitions | Standing up a TE team; 1-2 quarter lead over procurement |
| NO-A10 | N-A10 | CTrO / CDO Appointment (distinct from CTO/CNO) | 12-18 month platformization mandate with consolidated budget |

**MSP / Aggregator Tier A (7 signals — full list from `msp-aggregator-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| M-A1 | PE Acquisition / TSD Roll-up | **BIG ACQUISITION** — 60-120 day post-close sweet spot |
| M-A2 | Carrier Dropped from Line Card | Forced re-architecture; "federated backup carrier" moment |
| M-A3 | New Carrier Added to Portfolio | Each addition multiplies orchestration surface area |
| M-A4 | AI Practice / AI Solutions Launch | 58% of buyers want AI; opener: "how's the network layer?" |
| M-A5 | Executive Hire — CRO / VP SE / VP Product / VP AI Practice | 90-day strategy window |
| M-A6 | TSD Platform / Quoting-Engine Replatforming (job-post signal) | Connector-building window opens |
| M-A7 | ScanSource / TD SYNNEX Recurring-Revenue-Mix Disclosure | Public leading indicator of channel compression |

**Bonuses (stay in effect for Phase 1):**
- **Greenfield +3** at Colo S2/S3 (C-A0) and NeoCloud S2/S3 (N-A0)
- **Site transition +6** at 1→2 (C-A1 + N-A1)
- **I-series +3** at state-aid awards (I1) and sovereign AI grants (I2)
- **Stacking rule** — any account hitting 2+ signals in a 30-day window where at least one scores ≥8 auto-elevates to 18+

### Disabled in Phase 2 (do NOT scrape or surface)

AP-5 (technographic change alone), AP-6 (Apollo Intent alone), and the entire Noise List (see `signal-framework.md` Noise List section) remain **disabled**. Tier B is now ACTIVE in Phase 2 (was disabled in Phase 1). Tier C is paired-only — scraped, but only fires in the rep DM when stacked with a Tier A or Tier B on the same account in the same 30-day window.

### Priority hierarchy within Tier A (for the cascade ordering)

Within Tier A, some signals score materially higher due to bonuses and stacking. The red/orange/yellow cascade in the Slack DM naturally reflects this — reps see the highest-leverage signals first without any manual tiering:

- **Ultra-priority (typically score 24-36+ after bonuses):** C-A0 + C-A1 stacked, NC-A0 + NC-A1 stacked, NC-A8 dual-fire with C-A6, I1/I2 with segment bonus, any M&A at Day 60-90 post-close stacking with the post-close exec hire
- **High-priority (typically score 18-24):** Standalone anchor signings (C-A2, C-A6, NC-A7), standalone M&A (C-A7, F-A7, M-A1), exec hires fresh <30d (C-A4, F-A5, NO-A3, M-A5), BEAD awards (F-A1), NVIDIA Lepton/NCP (NC-A3)
- **Standard Tier A (typically score 18-21):** Hiring spikes (C-A5, NC-A6, NO-A9), GitHub commits to programmable-infra repos (NO-A5), PeeringDB / IX changes (NC-A9 / NC-A10), MLPerf submissions (NC-A11), transcript mentions (NO-A2)

**Phase 2 is now ACTIVE** (cap 40, Tier B active, Tier C paired-only — see "Phase 2 — Relevance-Expanded" section above). **Phase 3** (full 50 cap, more aggressive Tier C activation) is planned but not active.

## Reference Files — Load ALL on every run

**Signal framework (source-of-truth for this skill):**
- `context/signals/signal-framework.md`  -  scoring model, universal signals (U1-U6), I-series (I1/I2), scrape source stack, Exec Hire Detection Without Sales Navigator substitutes, conference agenda list. Honor the Phase 1 override banner at top.
- `context/signals/universal-platform-signals.md`  -  Apollo AP-1 through AP-7 + FR-1/2/3; canonical scoring + noise demotions
- `context/signals/colocation-signals.md`  -  C-A* codes; greenfield S1-S5; 1→2 transition; AI Signals sub-segment
- `context/signals/fiber-signals.md`  -  F-A* codes; BEAD; PE roll-up; AI-DC fiber; consortium/federation
- `context/signals/network-operator-signals.md`  -  **NO-A\*** runtime codes (catalog uses N-A*); Tier 1/2 carrier target list; TM Forum AN; SRv6; CAMARA/Nephio
- `context/signals/neocloud-signals.md`  -  **NC-A\*** runtime codes (catalog uses N-A*); greenfield + 1→2; compound signal triple-fire
- `context/signals/msp-aggregator-signals.md`  -  M-A* codes; TSD channel + NaaS platform operator subtypes; IT MSP exclusion

**HubSpot schemas:**
- `context/hubspot/property-schema.md`  -  `recent_news_or_trigger_event` (250 char), `account_brief` (400), `infrastructure_profile` (500), `last_enriched_date`, `account_tier`, `hubspot_owner_id`, `linkedin_company_page` (Apollo-overwrite authoritative), `state`, `country`
- `context/hubspot/hubspot-values.md`  -  segment + sub-segment enum values (MSP HubSpot internal is `Enterprise`; display as "MSP / Aggregator"); tier enum `tier_1`..`tier_5`; confidence enum `high_90` / `medium_7089` / `low_5069` / `manual_review_required`
- `context/hubspot/territory-model.md`  -  state → owner mapping
- `context/hubspot/contact-schema.md`  -  contact enum values (no `evangelist` in lifecyclestage)
- `context/hubspot/deals-schema.md`  -  `hs_is_closed_won` / `hs_is_closed_lost` booleans (never filter dealstage strings — pipeline uses custom numeric IDs)
- `context/hubspot/poc-schema.md`  -  POC ticket pipeline for deal-protection check

**Segments (for ICP context — read ALL five every run; Suggested Angle depth depends on this):**
- `context/segments/colocation.md`  -  sub-segments (Standard / AI Signals / Modular / Greenfield), buyer personas, 2025-2026 industry landscape (power constraint, AI reshaping, market bifurcation, sovereign tenant requirements, inference-profile shift, metro-edge diffusion, vertical-integration sharpening), Relevance Bridges, Insider Language Bank
- `context/segments/fiber-operator.md`  -  sub-segments (Regional CLEC / Long-Haul / Dark Fiber / Co-op / Greenfield), BEAD timeline, AI-DC fiber demand, ABS/refinancing, consortium thesis
- `context/segments/network-operator.md`  -  sub-segments (External Extension / Internal + External Unification), Track A / Track B messaging split, CAMARA/Nephio/ONAP/SRv6/TMF AN context
- `context/segments/neocloud.md`  -  5 sub-segments, Persona Prioritization by stage, Neocloud Angle by Maturity (watch list / early-growth / in-pain-now / scaling-wall), GPU debt wall, agentic latency compounding, enterprise long-tail scaling wall
- `context/segments/msp-aggregator.md`  -  US TSD channel + NaaS platform subtypes, ICP Exclusion List (IT MSPs / voice termination / SMS-CPaaS / cellular-IoT / roaming / eSIM)

**Core ICP context:**
- `context/core/icp-playbook.md`  -  ICP boundaries, segment sizing, top accounts, exclusions
- `context/core/segment-qualification.md`  -  proof-based qualification tests, Common False Positive Patterns
- `context/core/maiaedge-101.md`  -  product identity, founder provenance

**Sub-skills (read for domain logic  -  this skill does not redefine their methodology):**
- `skills/company-enrichment` — Phases 1-3 new-account enrichment + **Step 0C canonical re-enrichment overwrite spec** (state / country / owner / LinkedIn / domain authority rules). Stage 5 of this skill defers to 0C; do not duplicate.
- `skills/segment-classification` — qualification gates, EXCLUDE verdict routing, Segment Change Cascade Rules
- `skills/import-processor` — HubSpot enum value mapping (segment, sub-segment, tier, confidence). Invoke before any Stage 5 field write
- `skills/edge-case-researcher` — LOW / MANUAL_REVIEW second-pass investigation
- `skills/crm-guardian` — safety tiers (T1/T2/T3), deal protection, cascade logic, Job 8 integration
- `skills/territory-manager` — state → owner mapping, Apollo state verification, Contact Owner Cascade
- `skills/account-brief` — stale brief regeneration (>30d + research-divergence triggers)
- `skills/account-sourcing` — fallback for unknown-segment signals
- `skills/cold-email` — rep-specific voice (Tim Lieto vs. Ken Cunningham) for Suggested Angle column

---

## Run-time Invariants

### Timezone
All date math uses **America/New_York** (US Eastern). "This week" = Sunday 00:00 ET through Sunday 23:59 ET. Scrape window = prior 7 days from run start.

### Cadence
**Weekly, Mondays 7:00 AM ET delivery only.** Execution starts Sunday 23:00 ET. Does NOT support same-week reruns that would re-email reps — reps get exactly one report per week. Manual invocation is allowed but only for testing / Cooper's ad-hoc review (does not re-send rep emails; returns report content for preview instead).

### Territory purity
Each rep sees ONLY accounts in their territory. Never cross-share. Tim Ziemer gets International only (country != US).

### Field write rules
- `recent_news_or_trigger_event` has a 250-char HubSpot hard cap. Never exceed. Use the defined format.
- No em dashes in any HubSpot field write (repo convention).
- **Competitor naming rule (nuanced for signal writes):** Factual company names in signal context are OK (tenant names like Lambda/Crusoe, former-employer names for exec hires like "ex-Equinix," deal-partner names). What's NOT OK is naming competitor products in a comparison frame (e.g., "Megaport's Fabric product," "Equinix Fabric," "Zayo DynamicLink") — those get genericized to "third-party interconnection fabric" or "competing on-demand network product." This preserves actionability for reps while keeping `recent_news_or_trigger_event` field writes clean if any of them get surfaced downstream. The strict "no competitor names" rule still applies to any customer-facing MaiaEdge copy (cold emails, LinkedIn, segment cheatsheets).
- Always set `last_enriched_date` to run date on any touched account  -  keeps CRM Guardian's 120-day re-enrichment cycle aligned.

### Idempotency
Running twice on the same day should be safe. Second run should find most signals already applied and produce minimal updates. Scrape dedup by source-URL hash to prevent double-counting.

### Error containment
Per-record try/except on every field write, enrichment call, and Apollo lookup. Log failures in the run report's "Errors" section. Do not abort the whole run on single-record failures.

### HubSpot writes go through MCP, never via a file — HARD RULE

Every CRM write in this routine (new-account creation in Stage 3, field updates in Stage 5, contact owner cascades, segment syncs) goes through HubSpot MCP tools:

- **New accounts** → `mcp__claude_ai_HubSpot__manage_crm_objects` with `createRequest.objects[]`
- **Field updates** → `mcp__claude_ai_HubSpot__manage_crm_objects` with `updateRequest.objects[]` (batch up to 100 per call)
- **Association reassociation** → same `manage_crm_objects.updateRequest` with the `associations` field
- **Reads** → `search_crm_objects`, `get_crm_objects`, `get_properties`, `search_owners`
- Every write call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`

**The Excel attachment in Stage 6 is a rep-facing deliverable only.** It is the prospecting list reps read on Monday morning — it is NEVER used as a HubSpot import path, NEVER uploaded back into HubSpot, and NEVER treated as a write mechanism. If the runtime is tempted to "generate an Excel for import" as a substitute for a failing MCP write, that is a bug — surface the MCP failure in the run report's Errors section instead.

**`import-processor` sub-skill is referenced ONLY for HubSpot enum value mapping** (e.g. translate internal tier `TIER_1_STRATEGIC` → HubSpot enum `tier_1`). It is NOT invoked to produce import files in this routine. Its legacy XLSX-to-HubSpot transform is out of scope — weekly-signal-scan writes directly via MCP.

This rule is a restatement of the repo-wide CLAUDE.md convention: "HubSpot writes go through MCP, not import files. Enrichment, sourcing, contact creation, deal creation, segment/owner/tier updates — all happen via direct HubSpot MCP calls."

---

## Master Workflow

Seven sequential stages. Each stage has a clear input, operation, output.

### Source Coverage Mandate (anti-laziness — applies to all 5 sub-stages below)

**Every source documented in every Stage 1 sub-stage MUST be attempted every run, no exceptions.** The routine has a natural tendency to skip sources that returned 0 hits last week, are slow to scrape, or returned errors previously. None of those are valid reasons to skip. A 0-hit week is not a dead source; a slow source still has to be hit; an errored source needs to be retried (or escalated as an ERROR for Cooper to fix).

**Hard rules:**
1. **Every documented source is mandatory each run.** No "low yield" optimization. No "checked recently" caching across runs.
2. **Unreachable source = ERROR**, log in Cooper's run report under "Source Coverage — Failures." Never silent skip.
3. **0 hits = clean run on that source**, log "0 hits" in per-source coverage table. Repeated 0-hit weeks reveal source-development gaps Cooper needs to address.
4. **Runtime budget governs depth, not completeness.** If running low, reduce per-source depth (last 7 days vs 30 days) but do NOT skip sources entirely.

**Per-source accountability:** Cooper's run report MUST include a "Source Coverage" table with one row per documented source across all 5 sub-stages, columns `Sub-stage | Source | Attempted (✓/✗) | Hits | Status`. Failures get expanded in a sub-section with error type + suggested action. Repeated failures (same source ✗ for 3+ weeks) auto-flag as "needs development."

Full mandate text in `Claude routine prompts/weekly-signal-scan-prompt.md` → "Source Coverage Mandate" section.

### STAGE 1 — Per-Segment Signal Scrape (Phase 2)

**Input:** Source stack from `signal-framework.md` PLUS segment-specific source lists in `context/signals/[segment]-signals.md` PLUS the dedicated Stage 1 sub-stage source lists in `Claude routine prompts/weekly-signal-scan-prompt.md`.

**Operation — runs as 5 parallel sub-stages, ONE PER ICP SEGMENT:**

0. **Build expanded target-company list:** Query HubSpot at run start for all companies where `account_tier IN ('tier_1', 'tier_2', 'tier_3')` AND `customer_segment` is in the 5 ICP buckets AND `customer_segment != "Flagged for deletion"`. This is the ~700-1,000-account list (was ~400 in Phase 1) used to cross-reference exec-hire + hiring-spike detections. Slice into 5 segment buckets (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator) for the sub-stages.

1. **Stage 1.A — Colocation scrape:** Operate on the Colo segment slice. Scrape Tier A + Tier B Colo signals using the Colo-specific source list (DCD, Data Center Frontier, BISNOW DC, planning-department dockets, electric-utility queues, hyperscaler announcement feeds). Output: `colo_signals[]`.

2. **Stage 1.B — Fiber scrape:** Operate on the Fiber slice. Scrape Tier A + Tier B Fiber signals using the Fiber source list (Fierce Network, Light Reading, BroadbandNow, BEAD state portals, USTelecom, NTCA, ABS prospectus filings via SEC EDGAR, FCC dockets). Output: `fiber_signals[]`.

3. **Stage 1.C — NeoCloud scrape:** Operate on the NeoCloud slice. Highest-velocity segment — scrape Tier A + Tier B NeoCloud signals (TechCrunch GPU, The Information GPU economy, Crunchbase AI Infrastructure, NVIDIA partner pages, AnandTech, ServeTheHome, HPCWire, The Next Platform, PeeringDB diff feeds, IX participant lists, MLPerf submissions, SEC EDGAR 8-K Items 1.01 + 2.03). Output: `neocloud_signals[]`.

4. **Stage 1.D — Network Operator scrape:** Operate on the Network Op slice. Scrape Tier A + Tier B Network Op signals (Light Reading SP news, TelecomTV, Capacity Media, Mobile World Live, earnings transcripts via SEC + Seeking Alpha, TM Forum, CAMARA / Nephio / ONAP / OpenConfig / Sylva GitHub feeds, FedBizOpps RFP filings). Output: `network_op_signals[]`.

5. **Stage 1.E — MSP/Aggregator scrape:** Operate on the MSP slice. Scrape Tier A + Tier B MSP signals (ChannelE2E, CRN, Channel Futures, ScanSource + TD SYNNEX earnings, TSD press releases, partner-add announcements from Megaport / Console Connect / PacketFabric). Output: `msp_signals[]`.

6. **Stage 1.F — Aggregate:** Combine all 5 outputs into `detected_signals[]`. Dedup by `(company_domain, signal_code, source_url_hash)`. Per-segment counts go to Cooper's run report.

**Per detection, record:** company name(s), signal type (e.g., "C-A2 GPU Cloud Tenant Anchor"), signal tier (A/B/C), detection date, source URL, full signal body, originating segment sub-stage.

**Output:** `detected_signals[]`  -  a list of signal hits with company, segment, and metadata.

**Notes:**
- Universal signals (U1-U6, AP-1/2/7, FR-1, I1/I2) are scraped within EACH sub-stage, then deduped at Stage 1.F. A single exec hire that matches a multi-segment company gets one entry tagged with the company's current segment.
- Greenfield signals (Colo + NeoCloud) detect across all 5 stages (S1-S5) but score bonuses apply only at S2-S3.
- **International signals (I1, I2) fire for Tim Ziemer's territory.** Scrape the international source stack within the Colo / Fiber / Network Op / NeoCloud sub-stages — territory assignment happens at match time based on HubSpot `country`.
- Reference the segment-specific Stage 1 sub-stage source lists in `Claude routine prompts/weekly-signal-scan-prompt.md` for the canonical per-segment source ledger. The routine prompt is the operational source of truth; the SKILL is the architecture spec.

### STAGE 2 — Match to HubSpot

**Input:** `detected_signals[]` from Stage 1.

**Operation:**
1. For each detected signal, extract the company domain (or resolve company name to domain via Apollo if missing).
2. Search HubSpot by domain. Classify each hit:
   - **MATCH**: domain exists in HubSpot → attach `record_id`, `hubspot_owner_id`, `customer_segment`, `account_tier`, `state`, `country`, `last_enriched_date`, `account_brief`, `infrastructure_profile`, `linkedin_company_page` for downstream stages
   - **NEW**: domain not in HubSpot → route to Stage 3 for enrichment (Apollo org enrichment in Stage 3 returns LinkedIn URL which gets written to `linkedin_company_page` on new-account creation)
3. **Apply Phase 1 suppression list** — drop these matched or new accounts silently, logging count in Cooper's run report:
   - **MaiaEdge's own record** — HubSpot company ID `124293230301`.
4. Flag any `customer_segment = "Flagged for deletion"` accounts and drop them from further processing (per CRM Guardian invariant  -  never touch flagged accounts).

**Output:** `matched_accounts[]` and `new_companies[]`.

### STAGE 3 — Enrich New Companies

**Input:** `new_companies[]` from Stage 2.

**Operation:** For each new company:
1. Run `company-enrichment` Phase 1 (Apollo org enrichment + website read)  -  determines segment, state, country
2. If the company classifies as ICP (customer_segment in Colo / Fiber / Network Op / NeoCloud / MSP-Enterprise), proceed to Phase 2 (segment-specific research)
3. If non-ICP, drop from report (do not create HubSpot record  -  no point cluttering CRM with non-ICPs detected via signals)
4. Apply `crm-guardian` safety tiers:
   - HIGH confidence → Tier 1 auto-create in HubSpot via `manage_crm_objects.createRequest` (`objectType: "companies"`, properties map, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`)
   - MEDIUM confidence → Tier 2 auto-create via same MCP call + flag in run report
   - LOW / MANUAL_REVIEW → Tier 3 hold (appears in rep report's "Possible new accounts  -  review needed" section, NOT auto-created, NOT written to any file for batch-import)
5. Run `territory-manager` on every new account to assign `hubspot_owner_id` from state/country (this is an MCP write, not a file write)
6. Run `account-brief` skill to populate initial `account_brief` field via MCP
7. Populate `recent_news_or_trigger_event` with the signal that surfaced them via MCP

**All writes in this stage are MCP calls. No XLSX file is ever produced as a substitute for or alongside these MCP writes.** If the runtime is tempted to queue a "Phase 2 batch import" file for deferred / low-confidence accounts, that is a bug — Tier 3 holds surface to Cooper via the run report and get actioned by hand in HubSpot UI, not via file upload.

**Output:** `enriched_new_accounts[]` (with HubSpot record_id, owner, segment, brief).

**Credit budget — soft floor:** At Stage 3 entry, check remaining Apollo credits for the current billing cycle. If remaining credits fall below 20% of monthly allocation, **pause new-account enrichment for this run** (process only enrichments needed for accounts already in HubSpot via Stage 2 matching). Surface the pause in Cooper's run report: "Apollo credits at X% of monthly allocation — N net-new companies deferred to next run." Deferred companies get queued and re-checked next Monday. Matched accounts (already in HubSpot) still get enriched since they're the priority spend. No runaway-week risk.

### STAGE 4 — Score Every Hit

**Input:** `matched_accounts[]` + `enriched_new_accounts[]`, each joined to its triggering signal(s).

**Operation:** For each account-signal pair, compute Meeting Probability Score per `signal-framework.md`:

```
score = tier_weight × freshness_weight × confidence_weight

Tier weights: A=3, B=2, C=1
Freshness weights (Phase 2):
  Tier A:  ≤60d = 3, 60-90d = 2, >90d = drop entirely
  Tier B:  1wk = 3, 30d = 2, 90d = 1
  Tier C:  paired-only — inherits freshness from the Tier A/B it stacks with
Confidence weights: High=3, Med=2, Low=1
```

**Tier A freshness window updated 2026-04-27 per Cooper:** announcements within the past 60 days score at full freshness for Tier A. The catalogs already document 60-90+ day action windows on Tier A signals (90-day exec mandate, 60-120d M&A integration, 18-24 month BEAD ramps, 12-18 month CTrO platformization) — the old steep decay floored these out. Tier B keeps the steeper decay since Tier B is by-definition "30-90d window" signals.

If same account hit by 2+ signals in the week where at least one individual signal scores ≥ 8, elevate score to 18+ (stacking rule — see `signal-framework.md` for the ≥8 floor rationale). Apply bonus rules:
- **Greenfield S2-S3 bonus:** +3 (Colo + NeoCloud only)
- **Site count 1→2 transition bonus:** +6 (Colo + NeoCloud only — parse current count from free-text `infrastructure_profile` field; if parse is low-confidence, skip the bonus and rely on base greenfield scoring)

When a facility transition is detected and confirmed, **rewrite `infrastructure_profile`** in HubSpot with the updated count + context (e.g., "3 facilities: NoVA (2), Dallas (1); announced Phoenix facility Q2 2026 = transitioning to 4"). This keeps the next run's state fresh without needing a dedicated integer field.

**Output:** `scored_accounts[]`  -  each account with its highest-scored signal, score value, and stacked-signal list.

### STAGE 5 — Update HubSpot Fields

**Input:** `scored_accounts[]`.

**Authoritative source for each field** (Apollo-refreshed fields from Stage 1/3 enrichment flow through here — Apollo is the source of truth for firmographic identity on every run):

| Field | Write / overwrite rule |
|-------|------------------------|
| `recent_news_or_trigger_event` | Overwrite with highest-scored signal this week. Format: `[YYYY-MM-DD] [Signal Type] - [one-line summary]`. Hard cap 250 chars. |
| `account_brief` | Regenerate via `account-brief` skill if (a) existing brief >30 days old OR (b) fresh signal research materially diverges from existing brief (facility count changed, sub-segment shifted, anchor tenant announced). If 2+ signals hit, append "Also this week:" line (stay under 400 char total). If research matches current brief, leave it. |
| `infrastructure_profile` | Rewrite with updated facility count + context when a 1→2 or N→N+1 transition is confirmed at HIGH confidence. Preserves next-run parse state. |
| `state` | **Overwrite from Apollo** when Apollo returns a non-empty value different from HubSpot AND `last_enriched_date` is blank or 120+ days stale. HQ relocations are real. |
| `country` | **Overwrite from Apollo** on same rule as `state`. A US→non-US change triggers owner cascade to Tim Ziemer. |
| `hubspot_owner_id` | **Re-derive** from refreshed `state`/`country` via `territory-manager`. Cascade to associated contacts (Tier 1). |
| `linkedin_company_page` | **Overwrite from Apollo** `linkedin_url` when Apollo returns non-empty value differing from HubSpot. Handles rebrands / M&A LinkedIn-handle changes. |
| `domain` | **Conditional overwrite** — write Apollo's domain only if current HubSpot value is blank OR the HubSpot domain fails to resolve / redirects to Apollo's domain. If both are live-but-different, surface as Tier 2 (applied + flagged — likely rebrand worth Cooper's review). |
| `last_enriched_date` | **Always write** — today's ET date. Idempotency key for the 120-day rotation. |

Canonical overwrite spec lives in `skills/company-enrichment/SKILL.md` Step 0C — this routine references it, does not redefine. If the two diverge, company-enrichment wins.

**Safety tier per CRM Guardian:**
- Tier 1 (auto-write): field updates on accounts without open deals
- Tier 2 (auto-write + flag): field updates on deal-protected accounts; also `domain` rebrand-suspect writes and any state/country change that shifts territory on an account with an open deal
- Tier 3 (hold): LOW-confidence signals on critical accounts (Tier 1 accounts) → surface for Cooper's review. Apollo returns a state/country that contradicts a recent <30d manual note → Tier 3 (recent human input wins over automation)

**Never overwrite:** `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`, MEDDPICC deal fields, custom notes. These are sales-owned.

### STAGE 6 — Generate Per-Rep Reports (Cascade by Score)

**Input:** `scored_accounts[]` split by `hubspot_owner_id`.

**Operation:** For each of the 3 rep pools:
1. Filter `scored_accounts[]` where owner matches rep.
2. **Apply Phase 2 score floor:** drop every account-signal pair scoring below **12** from the rep DM. Score 8-11 → Watch List path: write `recent_news_or_trigger_event` at Stage 5 but do NOT include in rep DM. Below 8 = silent drop, no CRM write either.
3. **Apply 40-total cap per rep (Phase 2):** rank remaining candidates globally (across all segments) by Meeting Probability Score descending, take top 40. Overflow drops to Watch List. Fewer is fine — if only 18 accounts clear the bar this week, the list is 18.
4. Group the top 25 by `customer_segment` for Excel tab organization only. **Rep-facing label for MSP:** display as "MSP / Aggregator" even though HubSpot internal value is "Enterprise" (legacy naming).
5. **Assign a priority tier to each account based on score (Phase 2 bands):**

   | Tier | Score range | Emoji | Rep framing |
   |---|---|---|---|
   | Highest priority | 27+ | `:red_circle:` | top-scored accounts this week |
   | Strong signals | 18-26 | `:large_orange_circle:` | strong signal, worth prioritizing |
   | Worth reviewing | 12-17 | `:large_yellow_circle:` | solid signals on the radar |

   Phase 1 used 27+ / 22-26 / 18-21 bands. Phase 2 widens the orange band downward to capture the relevance gains from Tier B activation. Phase 3 may add a blue band at 8-11 if Watch-List behavior moves to the DM.

6. Generate **Slack DM body** (written for reps, tactical tone, cascade-by-score — no segment grouping in the message itself):

   ```
   :satellite_antenna: *Weekly Signal Scan — [Rep First Name] — Week of [YYYY-MM-DD]*
   [N] accounts cleared the quality bar this week. Ranked by score, highest first. Full detail in the attached Excel.

   :red_circle: *HIGHEST PRIORITY* — Score 27+
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body in 1-2 sentences. Name the persona + the specific wedge.]

   :large_orange_circle: *STRONG SIGNALS* — Score 22-26
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body, 1-2 sentences]
   • ...

   :large_yellow_circle: *WORTH REVIEWING* — Score 18-21
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body, 1 sentence — keep these tighter since volume is higher]
   • ...

   :sparkles: *NEW TO YOUR TERRITORY*
   • *[Account]* (Segment) — [reason enriched]
   • ...

   Full 14-column detail (LinkedIn URL, Suggested Angle, full Signal Body) in the attached Excel.
   ```

   **Tone rules unchanged:** tactical not strategic, short sentences, name-drop accounts, persona-aware angles. **No "call" language** — reps work these via their usual outbound channels; the DM tells them which accounts are top-scored, not what motion to run.

   **Skip empty sections.** If no accounts cleared 27+, drop the `HIGHEST PRIORITY` heading entirely — don't show "0 accounts" under it. Same for the other tiers.

7. Generate **Excel attachment** (`.xlsx`) — **this is a rep-facing read-only deliverable, NOT a HubSpot import file.** The Excel is what reps open on Monday morning; it is never ingested back into HubSpot, never treated as a source of truth for the CRM, never used as a retry path for a failed Stage 5 MCP write. All HubSpot writes already happened in Stages 3 + 5 via MCP before this file is assembled.
   - **Filename:** `weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx`
   - **Tabs:** one per segment with hits (skip empty segments). Sort each tab by Meeting Probability Score descending. Total rows across tabs ≤ 25 in Phase 1.
   - **Columns:** Account Name | Customer Segment | Sub-Segment | Account Tier | Account Owner | HubSpot URL | LinkedIn URL | Signal Type | Signal Body | Detection Date | Meeting Probability Score | Account Brief | State | Suggested Angle
   - **Color coding (SUBTLE — score cell only, not whole row):** apply a pastel fill to the "Meeting Probability Score" cell based on priority tier. Use `openpyxl` `PatternFill` with `fill_type="solid"`:
     - Score 27+ → `FFEBEE` (pastel red, `:red_circle:` equivalent)
     - Score 22-26 → `FFF3E0` (pastel orange, `:large_orange_circle:` equivalent)
     - Score 18-21 → `FFFDE7` (pastel yellow, `:large_yellow_circle:` equivalent)
   - Leave every other cell white. No bold, no borders beyond default, no header-row color changes. The point is a glanceable score column, not a highlighter-riot spreadsheet.
   - Header row stays default (bold Calibri 11 or similar — Excel default).

### Depth Spec for Every Row

Because the cap is 50, we invest in depth per account. For each row:
- **Signal Body** = 3-5 sentence synthesis: what happened, when, who's involved, the specific pain it exposes for this prospect, a pulled quote from the source + source URL. Reads like a call-prep, not a headline.
- **Suggested Angle** = persona-aware and signal-specific. Names the right persona (e.g., "reach Sarah Chen, the new VP Network (started 5 weeks ago) — reference her Equinix-fabric background and Prime's pending Phase II") and the signal-appropriate wedge (e.g., "GPU tenant anchor — reach platform owner before fabric decision is locked"). Derived from signal type + account context, not a template.
- **Account Brief** = regenerate via the `account-brief` skill whenever either condition is true: (a) the HubSpot `account_brief` is more than 30 days old at match time, OR (b) the fresh signal research materially diverges from what's in the existing brief (e.g., facility count changed, sub-segment shifted, a new anchor tenant announced). If research closely matches the existing brief, leave it. The goal is "reps never see a stale brief OR one that contradicts the news in the same row."

**Output:** 3 email payloads (body + attachment file).

### STAGE 7 — Deliver (Slack DMs + Excel attachments)

**Input:** 3 rep payloads (Slack message body + Excel attachment path).

**Operation:**
1. **First line of Slack message (acts as subject):** `:satellite_antenna: *Weekly Signal Scan — [Rep First Name] — Week of [YYYY-MM-DD]*` (use the subject emoji once at top; the cascade tiers use `:red_circle: / :large_orange_circle: / :large_yellow_circle:` per Stage 6).

2. **Post via `slack_send_message`** as a self-DM to the routing target. Cooper receives Tim Ziemer's international report in Phase 1 (to start) for signal-quality validation before handing off to Tim Z directly.

3. **Routing table (Phase 1):**

   | Territory pool (`hubspot_owner_id`) | Rep label in message | Slack channel_id (DM recipient) |
   |---|---|---|
   | Tim Lieto — East, `161889085` | "Tim" | `U0A973L1HFF` (Tim Lieto) |
   | Ken Cunningham — West, `162339176` | "Ken" | `U0AE1PGCB6C` (Ken Cunningham) |
   | Tim Ziemer — International, `159350430` | "Tim Z" | `U0A24D9RJLS` (**Cooper** — Phase 1 override) |

   The rep's first-name label in the message body follows the TERRITORY POOL, not the recipient. Cooper's Slack DM for Tim Z's territory still opens "Hey Tim Z" so when Cooper hands off to Tim Z directly the content is already addressed correctly.

4. **Excel attachment delivery:** Slack MCP `slack_send_message` does NOT support binary attachments. The Excel file is referenced via a download link in the message body. Options:
   - If the routine writes the Excel to a publicly-accessible location (S3 / GDrive / SharePoint public link), include the download URL in the message body.
   - Fallback for Phase 1: write the Excel to the repo at `weekly-reports/YYYY-MM-DD/[rep-last-name].xlsx` and include the GitHub raw URL in the Slack message. Commit + push happens as part of Stage 7. Example message footer: `> Excel: <https://github.com/[org]/maiaedge-ai/raw/main/weekly-reports/2026-04-27/lieto.xlsx|download>`.

5. **Cooper's consolidated run report** (separate Slack DM to Cooper only): total signals detected, HubSpot accounts touched (breakdown by field), new accounts enriched (Tier 1/2/3 counts), Apollo credits consumed + % of monthly allocation remaining, Tier 3 holds, deal-protected writes, per-rep output size (so Cooper can see "Tim got 12 accounts, Ken got 8, Tim Z [Cooper] got 3"), weekly trend vs. prior 4 runs, errors.

6. **Consistent message prefix** for Slack search grouping: all four messages (3 rep reports + Cooper's run report) lead with `*Weekly Signal Scan —` so they thread/search together.

7. **Phase 2 transition (future):** when Cooper is satisfied with Tim Z territory signal quality, change the `Tim Ziemer` row's `channel_id` from `U0A24D9RJLS` to Tim Z's actual Slack user ID (look up via `slack_search_users` at transition time). No other routing logic changes.

---

## Rep Slack DM Template (Phase 1 — cascade by score)

Each rep pool gets its own Slack DM. The structure is a **score cascade** (hottest at top, cooler below) — NOT segment-grouped paragraphs. Segment is shown inline per row as context, not as a grouping axis. Segment-grouped briefings are disabled in Phase 1 because they spread attention across the page and bury the truly hot signals; reps work hottest-first in Phase 1.

Template below. Square-brackets are fill-ins. Skip any tier heading where zero accounts clear its range — don't show "0 accounts" or empty sections.

```
:satellite_antenna: *Weekly Signal Scan — [Rep First Name] — Week of [YYYY-MM-DD]*

Hey [Rep First Name] — [N] accounts cleared the Phase 1 quality bar this week. Ranked by score, highest first. Full detail in the Excel linked at the bottom.

:red_circle: *HIGHEST PRIORITY* — Score 27+

• *[Account Name]* (Segment · Tier [1-5]) · Score [N] · <[HubSpot URL]|open>
  [1-2 sentence signal synthesis — what happened, who to reach, the specific wedge. Name the persona.]
• [next account if any]

:large_orange_circle: *STRONG SIGNALS* — Score 22-26

• *[Account Name]* (Segment · Tier) · Score [N] · <[HubSpot URL]|open>
  [1-2 sentence signal synthesis]
• [...]

:large_yellow_circle: *WORTH REVIEWING* — Score 18-21

• *[Account Name]* (Segment · Tier) · Score [N] · <[HubSpot URL]|open>
  [1 sentence — keep tight at this tier; full detail is in the Excel]
• [...]

:sparkles: *NEW TO YOUR TERRITORY*

[N] new accounts enriched + added via signal scan this week:
• *[Account]* (Segment) — [reason surfaced]
• [...]

Full 14-column detail (LinkedIn URL, Suggested Angle, full Signal Body, Account Brief): <[GitHub raw URL to Excel]|download>
```

**Tone rules:**
- Tactical, not strategic. Surface which accounts are top-scored this week — don't prescribe the outbound motion.
- Short sentences. No jargon reps don't already use.
- **No "call" language** — "reach" / "open with" / "worth a touch" is fine, "call today" is not. These are top-scored accounts; reps pick the channel.
- Name-drop accounts + personas — "Sarah Chen, VP Network (started 5 weeks ago, ex-Equinix)" beats "this new hire signals opportunity."
- No "Watch for" / theme paragraph in Phase 1. The cascade is the theme.

---

## Edge Cases

### No signals hit for a segment in the rep's territory
Skip that segment entirely in the Excel — no empty tab. The Slack message doesn't group by segment in Phase 1 so no empty headings appear. If the rep has ZERO accounts clearing the Phase 1 score-18 floor across all segments, send a short Slack DM: `:satellite_antenna: *Weekly Signal Scan — [First Name] — Week of [YYYY-MM-DD]* — Quiet week in your territory. No accounts cleared the Phase 1 signal quality bar. See you next Monday.` No attachment. This is a feature, not a failure — noise suppression is the point of the score floor.

### Rep has no accounts in a segment at all
Still scrape the segment (universal signals don't care about territory) but filter that rep's report to only their segments.

### Unknown-company signal cannot be enriched to clear ICP classification
Route to `account-sourcing` skill for deeper investigation. Surface in Cooper's run report as "Possible new account  -  review needed" Tier 3. Do not push to rep reports until resolved.

### Compound signals across segments (e.g., Nvidia announces Lepton partner who is Neocloud AND builds in a Colo operator we track)
The signal scores on the PRIMARY company (Lepton partner = Neocloud). The Colo operator gets a secondary context flag only if they're on the rep's list for another reason. Never fire the same signal body on both accounts  -  keeps the rep report clean.

### Rate limiting
- HubSpot: 100 requests per 10 seconds. Batch updates (10 per second max) with exponential backoff on 429.
- Apollo: stop calling on 429 / credit_exhausted / quota_exceeded. Defer remaining new-account enrichments to next week's run.
- SEC EDGAR: 10 requests per second with User-Agent header.
- LinkedIn (public pages, public job posts only): respect scraping ToS. Read-only, no headless browser automation, no authenticated scraping.

---

## MCP Requirements

### HubSpot MCP
- `search_crm_objects`  -  company lookup by domain, owner filtering, stale-brief detection
- `get_object`  -  read full company record
- `update_object`  -  write `recent_news_or_trigger_event`, `account_brief`, `last_enriched_date`
- `create_object`  -  create new accounts via Stage 3
- `get_associations`  -  open-deal detection for deal protection

### Apollo MCP
- `apollo_organizations_enrich`  -  new-account Phase 1 enrichment (state, country, industry, employees)

### Web Tools
- `web_search`  -  source scraping across RSS feeds, SEC EDGAR, conference agendas
- `web_fetch`  -  source-article full-text, company website reads during enrichment

### Exec Hire Detection (no Sales Navigator required)
- SEC EDGAR 8-K Item 5.02 for public companies (officer changes, daily feed)
- PR Newswire / Business Wire "Appointments" / "People on the Move" tag RSS
- Trade press "People" columns (Fierce Network, Channel Futures, Light Reading, TelecomTV, Capacity Media, DCD Careers, DCF People) scraped weekly
- Company IR newsroom RSS for each target company
- Crunchbase News "Executive Moves" tag for NeoClouds / startups
- TheOrg.com free tier for org-structure diffing
- Apollo job-change detection (existing CRM Guardian Job 6, quarterly default) — tighten to monthly for Tier 1 accounts if needed
- Public job post sources for hiring-spike detection: LinkedIn public Jobs, Indeed, Greenhouse, Lever, company careers pages

Full substitute mapping documented in `signal-framework.md` under "Exec Hire Detection Without Sales Navigator."

### Slack MCP (rep report + run report delivery)
- `slack_send_message`  -  post each rep's cascade report as a self-DM. Channel IDs in Stage 7 routing table. Use Slack mrkdwn for formatting; fenced code blocks for the "New to Territory" bullet list if it gets long. Excel attachment referenced via download URL (GitHub raw or equivalent), NOT uploaded directly.
- `slack_send_message` with `thread_ts`  -  optional overflow for a rep whose report exceeds 5,000 chars (e.g., a big Monday with many Call-Today accounts). Keep the parent message under 5,000 and thread the Priority / This Week sections below.
- Cooper's consolidated run report posts as a separate DM to `U0A24D9RJLS` — distinct from the Tim-Z-territory report Cooper also receives in Phase 1. Keep them as two separate messages for clarity.

---

## Task Routing

| Trigger | Action |
|---|---|
| "Run weekly signal scan" / "Monday brief" / "Weekly signals" | Full pipeline Stage 1-7 (scheduled Monday AM only) |
| "Refresh news fields" / "Update trigger events" | Stage 1-5 only, no emails |
| "Show me this week's signals" / "What are reps seeing?" | Stage 1-6, return report content only (preview mode, no emails sent) |
| "Signal scan status" | Report last run date, signals detected, credits consumed, errors |

---

## Skill Chain

- **Orchestrated by:** `crm-guardian` Job 8 — weekly, Mondays (see `crm-guardian/SKILL.md` Master Cadence)
- **Triggers:** `company-enrichment` (Stage 3 new-account enrichment), `territory-manager` (Stage 3 owner assignment), `account-brief` (stale brief regeneration + research-divergence regeneration), `account-sourcing` (unclear-segment fallback)
- **References:** `property-schema.md`, `territory-model.md`, segment cheatsheets, signal framework + catalogs

---

## Scope Guardrails

- **Phase 2 cap: 40 accounts TOTAL per rep per week** (was 25 in Phase 1, not per segment). Ranked globally across the rep's territory. Fewer is fine — if only 18 accounts clear the Phase 2 score-12 floor this week, the list is 18. Phase 3 may go to 50.
- **Score floor of 12 (Phase 2).** Below 12 = dropped from rep DM. Score 8-11 → Watch List CRM write only (rep sees signal in HubSpot, not in DM).
- **Depth over breadth.** Each row reads like a mini call-prep (3-5 sentence signal body + persona-aware angle + fresh brief). Compute budget saved by capping at 50 funds this depth.
- **Territory purity.** Reps see only their territory.
- **Written-for-reps tone.** Tactical, not strategic.
- **No competitor naming** in field writes or email copy (use "third-party fabrics").
- **No em dashes** in any HubSpot field write.
- **250-char hard cap** on `recent_news_or_trigger_event`  -  never exceed.
- **Non-ICP signals don't create HubSpot records.** Signal on a non-ICP company = drop silently.
- **Flagged-for-deletion accounts are skipped entirely** (per CRM Guardian invariant).
