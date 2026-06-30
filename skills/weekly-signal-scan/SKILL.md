---
name: weekly-signal-scan
description: "MaiaEdge Weekly Signal Scan  -  runs Mondays to scrape fresh market signals across all 6 ICP segments (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise) using per-segment Tier A + Tier B catalogs. Detects buildouts, M&A, exec hires, anchor leases, BEAD awards, GPU debt, NaaS launches, Enterprise DC builds + regulatory enforcement events + Enterprise GenAI/GPU partnerships. Updates recent_news_or_trigger_event on matched HubSpot accounts, enriches net-new accounts, and delivers Slack DMs per rep territory (see context/hubspot/territory-model.md for the 5-region owner map) with score-cascaded prospecting lists. Use when asked to run weekly signals, generate the Monday brief, refresh news fields, scan for trigger events, build the weekly prospecting list, or produce rep territory reports. Orchestrated by crm-guardian (weekly Mondays) or invoked directly."
---

# MaiaEdge Weekly Signal Scan

## 2026-05-28 split - monolithic prompt retired, replaced by 7 Cowork scheduled tasks

The single `cowork-scheduled-tasks/weekly-signal-scan/` prompt was hitting context-budget walls mid-run (the 2026-05-25 fire degraded to focused-WebSearch reduced-scope and produced a blank per-source ✓/✗ audit). The fix is structural: one Cowork scheduled task per ICP segment, plus an aggregator that builds the rep-facing output from HubSpot.

**The 7 live tasks (this skill describes the pattern they all instantiate):**

| Task | Schedule (CT) | Apollo sub-cap | What it does |
|---|---|---|---|
| `signal-scan-colo` | Mon 8:30am | 35 | Stages 0-5c for Colo segment only |
| `signal-scan-fiber` | Mon 9:30am | 35 | Same for Fiber |
| `signal-scan-neocloud` | Mon 10:30am | 55 | Same for NeoCloud |
| `signal-scan-networkop` | Mon 11:30am | 50 | Same for Network Op |
| `signal-scan-msp` | Mon 12:30pm | 20 | Same for MSP/Aggregator |
| `signal-scan-enterprise` | Mon 1:00pm | 55 | Same for Enterprise |
| `signal-scan-aggregator` | Mon 2:30pm | 0 | Reads HubSpot for `last_signal_date = today`; builds 3 rep DMs + canvas Run log + Cooper run report |

Each per-segment scan reads from `context/signals/[segment]-signals.md` for the source registry + signal codes, writes to HubSpot via Stage 5 (pure-prose narrative) + Stage 5b (structured signal fields + tier/heat). The aggregator reads from HubSpot (source of truth) so a single per-segment scan failure doesn't block rep delivery - only Cooper's cross-ICP run report shows the gap.

**This SKILL.md remains the conceptual reference** documenting what to scrape, how to score, and the heat/tier compute rules. The 7 per-segment + aggregator prompts inline the operational rules per the Cowork runtime requirement. Cooper edits prompts in `cowork-scheduled-tasks/signal-scan-*` and re-pastes into Cowork UI; updates to this SKILL.md describe the conceptual pattern.

Monolithic archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/`. Do NOT re-enable it.

---

## Purpose

Every Monday morning, put the highest-leverage weekly prospecting list in each rep's hands  -  one ranked by fresh, public, time-bound signals that indicate meeting probability is unusually high this week. The skill closes the gap between MaiaEdge's existing enrichment (one-shot at account creation) and the real world (new facts every day).

Three outcomes per run:
1. **Update `recent_news_or_trigger_event`** on every existing HubSpot account that hit a signal this week (≤250 char, formatted per spec).
2. **Enrich + add** any net-new companies detected in signals but not yet in HubSpot  -  via `company-enrichment` + `crm-guardian` safety tiers.
3. **Deliver 3 Slack DMs** (one per rep territory), each with a cascade-ranked account list (hottest signals at top) + Excel attachment. One tab per segment with hits, max 25 accounts TOTAL per rep during **Phase 1 (Tier A signals only, score floor 18)**.

This is an orchestration skill. It defines WHAT to scrape, WHEN, and HOW to score. Sub-skills define the rest.

## Phase 3 - Volume-Hardened, Git-Free (current mode, as of 2026-05-04)

**Phase 2 produced a 5-account week on 2026-05-04 (1 NEW, 4 carried) due to two compounding failures.** First, Stage 1 was implemented as 5 parallel sub-agents - those sub-agents on the Claude Code runtime hit the egress proxy block on news sites, returned empty, or hallucinated structured-but-fabricated signals (caught at QA-1 and dropped, but volume floor collapsed). Second, the 7-day strict detection window plus score floor 12 was filtering out genuinely relevant signals that a rep would happily work. Phase 3 fixes both:

- **Detection window 14 days rolling** (was 7-day strict). Tier A scoring brackets unchanged (≤60d full freshness), so widening detection ≠ lowering quality - only surfaces more candidates the strict cutoff was filtering artificially.
- **Stage 1 runs as 6 independent Cowork scheduled tasks** (one per segment - Colo, Fiber, NeoCloud, Network Op, MSP-Aggregator, Enterprise; each at `cowork-scheduled-tasks/signal-scan-{segment}/prompt.md`). The 2026-05-28 split replaced the parent-runtime / sub-agent template architecture with standalone per-segment Cowork tasks. Eliminates the inline-token problem on 100K-500K char news index pages.
- **Search-anchor pattern is the canonical access method** (updated 2026-05-11). Direct `web_fetch` is gated by URL-provenance on Cowork's runtime - every URL fails first-attempt fetch regardless of source. The 2026-05-11 reachability audit (68 URLs tested across all 5 catalogs) confirmed this is a runtime-wide constraint, not a per-source issue. The working pattern is: for each documented source in `context/signals/[segment]-signals.md` "Sources for This Segment", run `web_search "{domain} {topic} {year}"` and read snippets + article URLs from the search results. Article URLs returned in search results can then be fetched directly. Sub-agents MUST attempt every documented source via search anchor - skipping a source because it's "paywalled" or "URL-gated" without trying the search anchor first fails the source-coverage gate by definition. The per-source loop is still mandatory; the *method* changed from "web_fetch each URL" to "search-anchor each domain."
- **Source-coverage gate (inlined in each per-segment prompt post-2026-05-28 split).** Gate logic and retry behavior are now inlined directly in each `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise}/prompt.md`. The old `check_source_coverage_gate.py` helper is archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/helpers/`. Any segment below 80% coverage triggers a retry; persistent gaps surface in the Cooper run report.
- **Volume-per-rep gate (inlined in the aggregator task post-2026-05-28 split).** Gate logic is now inlined in `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md`. The old `check_volume_gate.py` helper is archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/helpers/`. Reps with pool < 25 AND non-exhausted carryover have their DMs HELD pending Cooper review (RED tag). Reps with pool < 25 AND exhausted carryover post with YELLOW tag (genuine signal scarcity, not detection failure).
- **Score floor 8** (was 12). 8+ surfaces in rep DM. Below 8 = silent drop. Score 8-11 renders as `LIGHT` cascade tier (green emoji), separate from Strong / Worth Reviewing / Highest Priority. Watch List concept retired.
- **Cap target 25-50 per rep, hard cap 50.** Three-tier fill-down: Primary (≥12) → LIGHT (8-11) → Carryover News. Carryover fires only when combined Primary + LIGHT < 25.
- **Carryover News pool (new):** accounts where last week's `recent_news_or_trigger_event` is still chronologically valid (within last 30 days) AND no rep activity recorded ≤14 days. Pulls in only as fill-down to keep light weeks from going too thin.
- **No git operations anywhere in the run.** Excel files written to local `weekly-reports/YYYY-MM-DD/` only. WoW baseline reads local folder, never GitHub. Apollo budget tracker writes are local-file-only. The local mounted folder IS the persistence layer.
- **Rep DMs carry data inline.** Top 15-20 accounts in DM body, full 50-row list in threaded markdown table. Excel becomes Cooper's oversight artifact (surfaced via Cowork's `present_files`), not a primary rep deliverable.
- Tier A AND Tier B both active. Tier C paired-only.
- Target list: Tier 1+2+3 ICP accounts.

**Relevance + volume.** Phase 3's combined fixes target 25-50 surfaced accounts per rep per week without sacrificing source-quality discipline. The QA gate (Stage 4.5) still drops fabricated or stale signals; Phase 3 just makes it harder for the upstream pipeline to produce so few real ones in the first place.

The Tier A catalog below is preserved (Phase 3 still scrapes ALL of Tier A); the Tier B catalog is now also scraped per segment (see segment signal files under `context/signals/[segment]-signals.md` "Tier B" sections).

### Phase 2 signal inventory - must scrape ALL of these every run, ACROSS BOTH Tier A AND Tier B per segment

**Universal signals (fire across all 6 segments - Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise):**
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

**Colocation Tier A (7 signals - full list from `context/signals/colocation-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| C-A0 | Greenfield Build Stage S2/S3 (permit + utility interconnection) | **GREENFIELD** - +3 bonus at S2/S3, 9-15 months of influence before fit-out |
| C-A1 | Site Count Transition 1→2 Facilities | **GREENFIELD** - +6 bonus, first-ever multi-site design decision |
| C-A2 | GPU Cloud Tenant Anchor (Lambda/Crusoe/Nebius/Nscale/Together) | **BIG SIGNING** - meeting-ready the week of the press release |
| C-A3 | Liquid Cooling / D2C Deployment | AI-tenant readiness confirmed; "solved power, now solve determinism" opener |
| C-A4 | Executive Hire - VP/Dir of Interconnection / Network / Fabric | 90-day plan includes fabric or cross-connect fix |
| C-A5 | Network Engineering Job-Req Surge (3+ concurrent in 30d) | Operator is building something they don't have |
| C-A6 | Anchor Tenant Signing (hyperscaler OR enterprise OR neocloud) | **BIG SIGNING** - broader than C-A2; build-to-suit or multi-year MSA |
| C-A7 | Merger / Acquisition / PE Recap | **BIG ACQUISITION** - explicitly promoted from Tier B per user feedback; Day 60-90 post-close sweet spot |

**Fiber Tier A (9 signals - full list from `context/signals/fiber-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| F-A1 | BEAD Subgrant Award | **GREENFIELD** - 4-year build obligations, 18-24 month provisioning ramps |
| F-A2 | Regional Fiber PE Acquisition / Roll-up Close | **BIG ACQUISITION** - first 90 days = OSS/BSS unification pain |
| F-A3 | AI Data Center Lit / Dark Fiber Win or RFP | **BIG SIGNING** - 800G/1.6T AI interconnect exposes cross-footprint gaps |
| F-A4 | NaaS / Automation / Portal Launch | Competitor proof-of-struggle; active buyers hitting NNI wall |
| F-A5 | Executive Hire - VP Network Automation / CNO / VP Wholesale / VP Carrier Relations | 90-day modernization mandate |
| F-A6 | Dark Fiber IRU / Long-Haul Sold-Out | Monetization urgency peaks |
| F-A7 | Merger / Acquisition / Consolidation (broader than F-A2) | **BIG ACQUISITION** - any fiber M&A; 60-120 day post-close window |
| F-A8 | ABS / Refinancing / Secured Debt Issuance | CFO-level urgency for revenue-growth platform spend |
| F-A9 | Consortium / Federation / Co-op Announcement | Federation-readiness; direct thesis fit |

**⚠️ Code collision warning:** Both `context/signals/neocloud-signals.md` and `context/signals/network-operator-signals.md` use the `N-A*` prefix in their catalog files. When referencing signals in this skill's code / prompts / reports, always qualify with the segment: `NeoCloud N-A2` vs `NetworkOp N-A2`. Never use bare `N-A2` - it's ambiguous. Below, each table row's code prepends the segment abbreviation (`NC-` for NeoCloud, `NO-` for Network Operator) to the catalog code.

**NeoCloud Tier A (11 signals - full list from `context/signals/neocloud-signals.md`, highest-velocity segment):**
| Runtime code | Catalog code | Signal | Explicit Cooper priority |
|------|------|--------|--------------------------|
| NC-A0 | N-A0 | Greenfield Build Stage S2/S3 (permit + utility + GPU-backed debt) | **GREENFIELD** - +3 bonus; NeoClouds lease colo so debt is earliest signal |
| NC-A1 | N-A1 | Site Count Transition 1→2 Regions | **GREENFIELD** - +6 bonus, first-ever multi-region design |
| NC-A2 | N-A2 | New Facility / Region Launch (N→N+1) | **GREENFIELD** - 6-week connectivity project starting day one, 1wk freshness |
| NC-A3 | N-A3 | NVIDIA DGX Cloud Lepton / NCP / Exemplar Cloud Partner Announcement | NVIDIA's own marketplace requires observability they don't have |
| NC-A4 | N-A4 | Enterprise Customer Win (non-hyperscaler) | Scaling-wall moment; first enterprise logo = onboarding pain hits |
| NC-A5 | N-A5 | GPU-Backed Debt Raise / Credit Facility | Existential network-quality pressure |
| NC-A6 | N-A6 | Network / SRE / Observability Hiring Spike | First-ever network role = highest signal |
| NC-A7 | N-A7 | Anchor Tenant Signing (enterprise or hyperscaler) | **BIG SIGNING** - dual-fires with colo C-A6 |
| NC-A8 | N-A8 | Colo Lease Filing (SEC 8-K Item 1.01 / 2.03) | **BIG SIGNING** - dual-fires with colo; 4 business days from execution |
| NC-A9 | N-A9 | PeeringDB Changes (new netixlan / netfac / prefix) | Public-record new site coming online |
| NC-A10 | N-A10 | IX Member Addition (100G/400G port) | Open for peering flag; port-live date |
| NC-A11 | N-A11 | MLPerf Inference / Training Submission | Production-stable fabric; promoted from Tier C April 2026 |

**Network Operator Tier A (10 signals - full list from `context/signals/network-operator-signals.md`):**
| Runtime code | Catalog code | Signal | Explicit Cooper priority |
|------|------|--------|--------------------------|
| NO-A1 | N-A1 | Private Connectivity Fabric Copycat / Multi-Billion AI Deal | **BIG SIGNING** - Lumen $13B PCF precedent; boards asking for responses |
| NO-A2 | N-A2 | Earnings Transcript Mentions (NaaS/API/Private Fabric/Programmable) | Strategy teams already tasked with progress |
| NO-A3 | N-A3 | Executive Transition - CTO / CNO / VP Automation / Chief Network Strategy | 90-day window |
| NO-A4 | N-A4 | Wholesale / Consumer Divestiture or Spin-off | **BIG ACQUISITION-ADJACENT** - Lumen playbook; post-divestiture peak window |
| NO-A5 | N-A5 | GitHub Commits from @carrier.com to CAMARA / Nephio / ONAP / OpenConfig / Sylva | Engineering investment in programmable infrastructure |
| NO-A6 | N-A6 | TM Forum Autonomous Networks Self-Assessment | Leading indicator of where they want to go |
| NO-A7 | N-A7 | SRv6 / Segment-Routing Production Rollout | Dataplane readiness; control-plane gap is where MaiaEdge fits |
| NO-A8 | N-A8 | Public RFI / RFP - Multi-Domain Orchestrator / TE Controller / Inter-Carrier Automation | **Most direct buying signal** - actively procuring |
| NO-A9 | N-A9 | PCEP / SR-TE / BGP-LS / YANG-NETCONF Job Requisitions | Standing up a TE team; 1-2 quarter lead over procurement |
| NO-A10 | N-A10 | CTrO / CDO Appointment (distinct from CTO/CNO) | 12-18 month platformization mandate with consolidated budget |

**MSP / Aggregator Tier A (7 signals - full list from `context/signals/msp-aggregator-signals.md`):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| M-A1 | PE Acquisition / TSD Roll-up | **BIG ACQUISITION** - 60-120 day post-close sweet spot |
| M-A2 | Carrier Dropped from Line Card | Forced re-architecture; "federated backup carrier" moment |
| M-A3 | New Carrier Added to Portfolio | Each addition multiplies orchestration surface area |
| M-A4 | AI Practice / AI Solutions Launch | 58% of buyers want AI; opener: "how's the network layer?" |
| M-A5 | Executive Hire - CRO / VP SE / VP Product / VP AI Practice | 90-day strategy window |
| M-A6 | TSD Platform / Quoting-Engine Replatforming (job-post signal) | Connector-building window opens |
| M-A7 | ScanSource / TD SYNNEX Recurring-Revenue-Mix Disclosure | Public leading indicator of channel compression |

**Enterprise Tier A (7 signals - full list from `context/signals/enterprise-signals.md`, added 2026-05-11 with ICP promotion):**
| Code | Signal | Explicit Cooper priority |
|------|--------|--------------------------|
| E-A1 | New DC Build / DC Expansion / Major Capacity Add | **GREENFIELD-equivalent** - every new corporate IT DC = fresh fabric decision; capacity uprate = inter-DC connectivity envelope being redesigned |
| E-A2 | Definitive M&A Agreement (Announcement OR Close - two-event firing) | **BIG ACQUISITION** - every Enterprise M&A = 18-36 month network integration project; Capital One/Discover, Concentrix/Webhelp, TP/Majorel, Cognizant/Astreya class deals; +6 stacking on both events within 12mo |
| E-A3 | AI / GPU Workload Announcement Requiring Enterprise GPU Connectivity | Enterprise GenAI deployments need east-west fabric to GPU clusters; JPMorgan IndexGPT, Walmart Sparky, Cognizant Neuro AI + NVIDIA, Teleperformance Azure OpenAI 170 markets |
| E-A4 | Network Exec Hire - VP/Director/Principal Network Infrastructure | 90-day inherited-architecture audit window; technical-champion persona signal |
| E-A5 | Regulatory Enforcement Event / New Framework Effective Date | DORA enforcement (Jan 2025) + CTPP designations (Nov 2025); NY DFS Part 500 cert (April 15 2026); HIPAA NPRM (Dec 2024); PCI v4.0 (March 2025); California AB 749; HHS OCR breach disclosures |
| E-A6 | Equinix Fabric / Megaport / PacketFabric / Console Connect Customer-Win Naming a Tier 1 Enterprise | Confirms active multi-cloud connectivity buying motion + currently committed to a third-party fabric incumbent (the on-ramp use case displacement target) |
| E-A7 | SOX 10-K / Annual Report Disclosure of Network / IT Modernization Initiative | Budget-authorized initiative already in flight; 10-K is Robust source - single hit scores HIGH |

**Bonuses (stay in effect for Phase 1):**
- **Greenfield +3** at Colo S2/S3 (C-A0) and NeoCloud S2/S3 (N-A0)
- **Site transition +6** at 1→2 (C-A1 + N-A1)
- **I-series +3** at state-aid awards (I1) and sovereign AI grants (I2)
- **Stacking rule** - any account hitting 2+ signals in a 30-day window where at least one scores ≥8 auto-elevates to 18+

### Disabled in Phase 2 (do NOT scrape or surface)

AP-5 (technographic change alone), AP-6 (Apollo Intent alone), and the entire Noise List (see `context/signals/signal-framework.md` Noise List section) remain **disabled**. Tier B is now ACTIVE in Phase 2 (was disabled in Phase 1). Tier C is paired-only - scraped, but only fires in the rep DM when stacked with a Tier A or Tier B on the same account in the same 30-day window.

### Priority hierarchy within Tier A (for the cascade ordering)

Within Tier A, some signals score materially higher due to bonuses and stacking. The red/orange/yellow cascade in the Slack DM naturally reflects this - reps see the highest-leverage signals first without any manual tiering:

- **Ultra-priority (typically score 24-36+ after bonuses):** C-A0 + C-A1 stacked, NC-A0 + NC-A1 stacked, NC-A8 dual-fire with C-A6, I1/I2 with segment bonus, any M&A at Day 60-90 post-close stacking with the post-close exec hire, **E-A2 Enterprise M&A two-event firing within 12mo (+6 stacking)**, **E-A4 Enterprise network exec hire stacked with E-A1 new DC build at the same enterprise**
- **High-priority (typically score 18-24):** Standalone anchor signings (C-A2, C-A6, NC-A7), standalone M&A (C-A7, F-A7, M-A1, **E-A2**), exec hires fresh <30d (C-A4, F-A5, NO-A3, M-A5, **E-A4**), BEAD awards (F-A1), NVIDIA Lepton/NCP (NC-A3), **Enterprise regulatory triggers at named accounts (E-A5)**, **Enterprise DC build / expansion (E-A1)**, **Enterprise GenAI / GPU partnership (E-A3 with named GPU partner)**
- **Standard Tier A (typically score 18-21):** Hiring spikes (C-A5, NC-A6, NO-A9), GitHub commits to programmable-infra repos (NO-A5), PeeringDB / IX changes (NC-A9 / NC-A10), MLPerf submissions (NC-A11), transcript mentions (NO-A2), **Enterprise fabric-vendor customer-win (E-A6)**, **Enterprise SOX 10-K modernization disclosure (E-A7)**

**Phase 2 is now ACTIVE** (cap 40, Tier B active, Tier C paired-only - see "Phase 2 - Relevance-Expanded" section above). **Phase 3** (full 50 cap, more aggressive Tier C activation) is planned but not active.

## Reference Files - Load ALL on every run

**Signal framework (source-of-truth for this skill):**
- `context/signals/signal-framework.md`  -  scoring model, universal signals (U1-U6), I-series (I1/I2), scrape source stack, Exec Hire Detection Without Sales Navigator substitutes, conference agenda list. Honor the Phase 1 override banner at top.
- `context/signals/universal-platform-signals.md`  -  Apollo AP-1 through AP-7 + FR-1/2/3; canonical scoring + noise demotions
- `context/signals/colocation-signals.md`  -  C-A* codes; greenfield S1-S5; 1→2 transition; AI Signals sub-segment
- `context/signals/fiber-signals.md`  -  F-A* codes; BEAD; PE roll-up; AI-DC fiber; consortium/federation
- `context/signals/network-operator-signals.md`  -  **NO-A\*** runtime codes (catalog uses N-A*); Tier 1/2 carrier target list; TM Forum AN; SRv6; CAMARA/Nephio
- `context/signals/neocloud-signals.md`  -  **NC-A\*** runtime codes (catalog uses N-A*); greenfield + 1→2; compound signal triple-fire
- `context/signals/msp-aggregator-signals.md`  -  M-A* codes; TSD channel + NaaS platform operator subtypes; IT MSP exclusion
- `context/signals/enterprise-signals.md`  -  E-A* codes (added 2026-05-11): E-A1 New DC build / expansion, E-A2 M&A two-event firing, E-A3 AI/GPU workload, E-A4 Network exec hire, E-A5 Regulatory enforcement, E-A6 Fabric-vendor customer win, E-A7 SOX 10-K disclosure. Sub-segments: Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services. Anchor: Meijer.

**HubSpot schemas:**
- `context/hubspot/property-schema.md`  -  `recent_news_or_trigger_event` (250 char), `account_brief` (400), `infrastructure_profile` (500), `last_enriched_date`, `account_tier`, `hubspot_owner_id`, `linkedin_company_page` (Apollo-overwrite authoritative), `state`, `country`
- `context/hubspot/hubspot-values.md`  -  segment + sub-segment enum values (MSP HubSpot internal value is `MSP/Aggregator`, also the rep-facing label "MSP / Aggregator"); tier enum `tier_1`..`tier_5`; confidence enum `high_90` / `medium_7089` / `low_5069` / `manual_review_required`
- `context/hubspot/territory-model.md`  -  state → owner mapping
- `context/hubspot/contact-schema.md`  -  contact enum values (no `evangelist` in lifecyclestage)
- `context/hubspot/deals-schema.md`  -  `hs_is_closed_won` / `hs_is_closed_lost` booleans (never filter dealstage strings - pipeline uses custom numeric IDs)
- `context/hubspot/poc-schema.md`  -  POC ticket pipeline for deal-protection check

**Segments (for ICP context - read ALL five every run; Suggested Angle depth depends on this):**
- `context/segments/colocation.md`  -  4 sub-segments (`Standard - colo` / `AI Signals - colo` / `Modular - colo` / `Hyperscale Wholesale - colo`) + cross-segment `Greenfield`, buyer personas, 2025-2026 industry landscape (power constraint, AI reshaping, market bifurcation, sovereign tenant requirements, inference-profile shift, metro-edge diffusion, vertical-integration sharpening), Relevance Bridges, Insider Language Bank
- `context/segments/fiber-operator.md`  -  6 sub-segments (`Regional CLEC - Fiber operator` / `Long Haul / Backbone - Fiber operator` / `Dark Fiber Specialist - Fiber Operator` / `Tier 2 National Wholesale - Fiber operator` / `Regional Cable Operator - Fiber operator` / `Municipal / Cooperative - Fiber operator` - renamed from retired `Co-op/consortium` 2026-05-13), BEAD timeline, AI-DC fiber demand, ABS/refinancing, consortium thesis
- `context/segments/network-operator.md`  -  5 sub-segments (`Tier 1 Carrier - Network Op` / `Pure Wholesale Carrier - Network Op` / `Cable MSO Enterprise Division - Network Op` / `International Backbone Specialist - Network Op` / `Subsea cable operator` - NEW 2026-05-14). Track A / Track B is now a dedicated `network_op_track` field (`external_extension` / `internal_external_unification`), NOT a sub-segment value (legacy sub-segments archived 2026-05-13). CAMARA/Nephio/ONAP/SRv6/TMF AN context.
- `context/segments/neocloud.md`  -  5 sub-segments (`Large Scale GPU - Neocloud` / `Tier 1 Inference - Neocloud` / `AI Infrastructure providers - Neocloud` / `Sovereign AI Clouds - Neocloud` / `Crypto to AI - Neoclouds`) + cross-segment `Greenfield`, Persona Prioritization by stage, Neocloud Angle by Maturity (watch list / early-growth / in-pain-now / scaling-wall), GPU debt wall, agentic latency compounding, enterprise long-tail scaling wall
- `context/segments/msp-aggregator.md`  -  US TSD channel + NaaS platform subtypes, ICP Exclusion List (IT MSPs / voice termination / SMS-CPaaS / cellular-IoT / roaming / eSIM)
- `context/segments/enterprise.md`  -  4 sub-segments only (Financial Services / Healthcare Systems / Retail and Distribution / Outsourcing Services), hard scale gate, sub-segment-specific Insider Language Banks (FFIEC physical-path verification, Epic downtime procedure, peak readiness / freeze, seat ramp / paired site / client carve-out), Anonymized Proof-Point Bank, Vocabulary Lock, Watch List verticals (Manufacturing / Energy-Utilities / Logistics - NOT ICP), Government/Defense FedRAMP-gated. Anchor: Meijer.
- `context/segments/enterprise-use-cases.md`  -  8 priority use cases × sub-segment fit × persona fit × insider phrases × cold-email lead-angle templates × proof-point patterns × use-case-specific objections.

**Core ICP context:**
- `context/core/icp-playbook.md`  -  ICP boundaries, segment sizing, top accounts, exclusions
- `context/core/segment-qualification.md`  -  proof-based qualification tests, Common False Positive Patterns
- `context/core/maiaedge-101.md`  -  product identity, founder provenance
- `context/account-tiering/sub-segment-qualification.md`  -  **canonical 30-value list of active `company_sub_segment` enums (case-sensitive)**. Read at every Stage 3 NEW-account create. Key entries: `Subsea cable operator` (30th, added 2026-05-14), `Greenfield` is a real sub-segment paired with Colo or NeoCloud parent, `Crypto to AI - Neoclouds` inclusive of operator AND landlord. Retired (never write): `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `Managed Network Services - Network Operator`.
- `context/account-tiering/enrichment-protocols.md`  -  Stage 3 calls this for the research-first workflow + D1 disqualifier check + D5 v2 per-sub-segment protocols. Every NEW-account creation in Stage 3 runs the full R1 five-stage pipeline per this spec.
- `context/account-tiering/tier-compute-spec.md`  -  **Stage 5b** calls `compute_tier()` per this spec for every account scoring ≥8. Inputs include `last_signal_score`, `last_signal_date`, `signal_count_last_30d`. Honors `hs_is_target_account = true` (compute logged, tier write skipped).

**Sub-skills (read for domain logic  -  this skill does not redefine their methodology):**
- `skills/company-enrichment` - Phases 1-3 new-account enrichment + **Step 0C canonical re-enrichment overwrite spec** (state / country / owner / LinkedIn / domain authority rules). Stage 5 of this skill defers to 0C; do not duplicate.
- `skills/segment-classification` - qualification gates, EXCLUDE verdict routing, Segment Change Cascade Rules
- `skills/import-processor` - HubSpot enum value mapping (segment, sub-segment, tier, confidence). Invoke before any Stage 5 field write
- `skills/edge-case-researcher` - LOW / MANUAL_REVIEW second-pass investigation
- `skills/crm-guardian` - safety tiers (T1/T2/T3), deal protection, cascade logic, Job 8 integration
- `skills/territory-manager` - state → owner mapping, Apollo state verification, Contact Owner Cascade
- `skills/account-brief` - stale brief regeneration (>30d + research-divergence triggers)
- `skills/account-sourcing` - fallback for unknown-segment signals
- `skills/cold-email` - rep-specific voice for Suggested Angle column; sender pool defined in `context/hubspot/territory-model.md`

**Additional context (HIGH - read alongside signal catalogs):**
- `context/signals/outreach-signal-pushback.md`  -  Stage 5b write semantics and increment rule for the 5 structured signal fields; canonical source for signal field write behavior
- `context/outreach/email-writing-rules.md`  -  Suggested Angle craft rules (Load-Bearing Assumption Gate, banned phrases, no em dashes, no competitor naming in copy)
- `context/europe/europe-signal-sources.md`  -  international source stack for Tim Ziemer / Markus Hendrich territory scraping; undefined without this file

**Additional context (MEDIUM - load when the corresponding path arises):**
- `context/account-tiering/d3-disambiguation-flowcharts.md`  -  segment-routing tiebreakers when a detected signal company spans multiple sub-segments
- `context/account-tiering/sub-segment-qualification-full.md`  -  full 30-sub-segment evidence tables for Stage 3 new-account classification
- `context/outreach/voice-gold-standard.md`  -  Suggested Angle tone calibration
- `context/outreach/sender-profiles.md`  -  per-sender craft register for Suggested Angle column; sender pool is the 5-region set from `context/hubspot/territory-model.md`
- `context/core/differentiation-naas-aggregator.md`  -  cold-safe competitive language for Suggested Angle bullets
- `context/europe/europe-market-map.md`  -  European account geography for Markus Hendrich territory signals
- `context/europe/sovereignty-positioning.md`  -  DORA/NIS2 framing for Enterprise + Network Op Suggested Angles in European territory
- `context/copy-strategy/segment-language.md`  -  approved segment vocabulary for narrative field writes
- `context/product/proof-points.md`  -  factual anchors for Suggested Angle and account-brief regeneration
- `context/outreach/fallback-messaging.md`  -  fallback angle language when no fresh signal anchor is available

---

## Run-time Invariants

### Timezone
All date math uses **America/New_York** (US Eastern). "This week" = Sunday 00:00 ET through Sunday 23:59 ET. Scrape window = prior 7 days from run start.

### Cadence
**Weekly, Mondays 7:00 AM ET delivery only.** Execution starts Sunday 23:00 ET. Does NOT support same-week reruns that would re-email reps - reps get exactly one report per week. Manual invocation is allowed but only for testing / Cooper's ad-hoc review (does not re-send rep emails; returns report content for preview instead).

### Territory purity
Each rep sees ONLY accounts in their territory. Never cross-share. Territory assignment follows `context/hubspot/territory-model.md` (5-region model: Northeast / Southeast / Central / Europe / International). Tim Ziemer gets International (country outside US and non-Europe); Markus Hendrich gets Europe; US accounts route by state per `context/hubspot/territory-model.md`.

### Field write rules
- `recent_news_or_trigger_event` has a 250-char HubSpot hard cap. Never exceed. Use the defined format.
- No em dashes in any HubSpot field write (repo convention).
- **Competitor naming rule (nuanced for signal writes):** Factual company names in signal context are OK (tenant names like Lambda/Crusoe, former-employer names for exec hires like "ex-Equinix," deal-partner names). What's NOT OK is naming competitor products in a comparison frame (e.g., "Megaport's Fabric product," "Equinix Fabric," "Zayo DynamicLink") - those get genericized to "third-party interconnection fabric" or "competing on-demand network product." This preserves actionability for reps while keeping `recent_news_or_trigger_event` field writes clean if any of them get surfaced downstream. The strict "no competitor names" rule still applies to any customer-facing MaiaEdge copy (cold emails, LinkedIn, segment cheatsheets).
- `last_enriched_date` is NOT bumped by Stage 5 partial writes (per CLAUDE.md Unified Stamping Policy). Only Stage 3 NEW-account creates bump it (the full enrichment pipeline ran).

### Idempotency
Running twice on the same day should be safe. Second run should find most signals already applied and produce minimal updates. Scrape dedup by source-URL hash to prevent double-counting.

### Error containment
Per-record try/except on every field write, enrichment call, and Apollo lookup. Log failures in the run report's "Errors" section. Do not abort the whole run on single-record failures.

### Anti-shortcut rule (updated 2026-05-11)
The runtime constraint that drives this rule is URL-provenance gating on Cowork's `web_fetch` - direct fetches fail across the board. The canonical access method is search-anchor: `web_search "{domain} {topic} {year}"` against each documented source, then read snippets + follow article URLs returned in search results. The 2026-05-11 reachability audit confirmed this is a runtime-wide constraint, not a per-source issue.

The anti-shortcut rule that remains in force: **every documented source in the segment catalog must be attempted via search anchor.** Skipping a source because the domain "feels paywalled" or "looked URL-gated" without running the search anchor first is the shortcut. A `web_search "{generic phrase} 2026"` query that doesn't anchor on documented source domains fails the source-coverage gate by definition - the gate counts attempted sources by `source_url` in `sources_attempted.json`, not raw search count.

When `web_fetch` does work on an article URL returned by search, use it (and on oversized HTML, save to disk and run `headline_extract.py` - archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/helpers/headline_extract.py`; gate logic is now inlined in each per-segment prompt). When it doesn't, the search snippet itself is the input - read date, company name, signal type from the snippet and follow the article URL only if the snippet is ambiguous.

Under-target output reaches reps ONLY when the volume-per-rep gate confirms the carryover pool is genuinely exhausted - the runtime cannot label thin output a "test run" and ship it.

### HubSpot writes go through MCP, never via a file - HARD RULE

Every CRM write in this routine (new-account creation in Stage 3, field updates in Stage 5, contact owner cascades, segment syncs) goes through HubSpot MCP tools:

- **New accounts** → `mcp__claude_ai_HubSpot__manage_crm_objects` with `createRequest.objects[]`
- **Field updates** → `mcp__claude_ai_HubSpot__manage_crm_objects` with `updateRequest.objects[]` (batch up to 100 per call)
- **Association reassociation** → same `manage_crm_objects.updateRequest` with the `associations` field
- **Reads** → `search_crm_objects`, `get_crm_objects`, `get_properties`, `search_owners`
- Every write call sets `confirmationStatus = "CONFIRMATION_WAIVED_FOR_SESSION"`

**The Excel attachment in Stage 6 is a rep-facing deliverable only.** It is the prospecting list reps read on Monday morning - it is NEVER used as a HubSpot import path, NEVER uploaded back into HubSpot, and NEVER treated as a write mechanism. If the runtime is tempted to "generate an Excel for import" as a substitute for a failing MCP write, that is a bug - surface the MCP failure in the run report's Errors section instead.

**`import-processor` sub-skill is referenced ONLY for HubSpot enum value mapping** (e.g. translate internal tier `TIER_1_STRATEGIC` → HubSpot enum `tier_1`). It is NOT invoked to produce import files in this routine. Its legacy XLSX-to-HubSpot transform is out of scope - weekly-signal-scan writes directly via MCP.

This rule is a restatement of the repo-wide CLAUDE.md convention: "HubSpot writes go through MCP, not import files. Enrichment, sourcing, contact creation, deal creation, segment/owner/tier updates - all happen via direct HubSpot MCP calls."

---

## Master Workflow

Seven sequential stages. Each stage has a clear input, operation, output.

### Source Coverage Mandate (anti-laziness - applies to all 6 sub-stages below - Enterprise sub-stage added 2026-05-11)

**Every source documented in every Stage 1 sub-stage MUST be attempted every run, no exceptions.** The routine has a natural tendency to skip sources that returned 0 hits last week, are slow to scrape, or returned errors previously. None of those are valid reasons to skip. A 0-hit week is not a dead source; a slow source still has to be hit; an errored source needs to be retried (or escalated as an ERROR for Cooper to fix).

**Hard rules:**
1. **Every documented source is mandatory each run.** No "low yield" optimization. No "checked recently" caching across runs.
2. **Unreachable source = ERROR**, log in Cooper's run report under "Source Coverage - Failures." Never silent skip.
3. **0 hits = clean run on that source**, log "0 hits" in per-source coverage table. Repeated 0-hit weeks reveal source-development gaps Cooper needs to address.
4. **Runtime budget governs depth, not completeness.** If running low, reduce per-source depth (last 7 days vs 30 days) but do NOT skip sources entirely.

**Per-source accountability:** Cooper's run report MUST include a "Source Coverage" table with one row per documented source across all 6 sub-stages (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise), columns `Sub-stage | Source | Attempted (✓/✗) | Hits | Status`. Failures get expanded in a sub-section with error type + suggested action. Repeated failures (same source ✗ for 3+ weeks) auto-flag as "needs development."

Full mandate text lives in each per-segment prompt at `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise}/prompt.md` → "Source Coverage Mandate" section.

### STAGE 1 - Per-Segment Signal Scrape (Phase 2)

**Input:** Source stack from `context/signals/signal-framework.md` PLUS segment-specific source lists in `context/signals/[segment]-signals.md`. Each per-segment prompt at `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise}/prompt.md` is the canonical per-segment source ledger and the operational source of truth for that segment's Stage 1 sub-stage.

**Operation - runs as 6 parallel sub-agents, ONE PER ICP SEGMENT (Cowork pattern, restored 2026-05-05; expanded from 5 to 6 with Enterprise sub-agent added 2026-05-11):**

Each per-segment task IS the sub-agent (the 2026-05-28 split eliminated the parent-runtime / sub-agent template architecture). The gate logic and source ledger are inlined directly in each `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise}/prompt.md`. The old `helpers/stage1-subagent-prompt-template.md` is archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/helpers/`. Each task receives segment name, full source URL list (from `context/signals/[segment]-signals.md` "Sources for This Segment" sub-section), 14-day window, signal codes, target ICP companies. The Enterprise sub-agent reads `context/signals/enterprise-signals.md` 33 documented sources (pruned 2026-05-11, audit-verified reachable via search-anchor) across StockTitan (SEC mirror) + SEC EDGAR + American Banker / Modern Healthcare / Becker's / Retail Dive / RIS News / NRF Blog / HIMSS / CHIME / CIO.com / InformationWeek / Risk & Insurance / GovInfoSecurity / WSJ CIO Journal + Nelson Hall / Everest Group (awareness-tier) + HHS OCR portal + HIPAA Journal mirror + NY DFS / PCI Council / EBA DORA portals + Equinix / Megaport / PacketFabric / Console Connect customer-win pages + NVIDIA partner press + earnings transcript outlets (Seeking Alpha / Motley Fool / MarketBeat). Per the search-anchor pattern (Phase 3 banner above + signal-framework.md), each sub-agent uses `web_search "{domain} {topic} {year}"` against documented sources, then follows article URLs from search results. Returns compact JSON of detected signals + per-source coverage log. Soft cap 25 sources per task; partial returns supported. Each per-segment task writes `weekly-reports/<run_date>/sources_attempted.json` and evaluates the source-coverage gate (inlined in the task prompt) before advancing. The aggregator task at `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` reads HubSpot for `last_signal_date = today` records and builds the rep DMs.

0. **Build expanded target-company list:** Query HubSpot at run start for all companies where `account_tier IN ('tier_1', 'tier_2', 'tier_3')` AND `customer_segment` is in the **6 ICP buckets** (`Data Center Colo Provider`, `Fiber Operator`, `NeoCloud`, `Network Operator(Tier 1 / VNO)`, `MSP/Aggregator`, **`Enterprise-CustomerSegment`** - added 2026-05-11) AND `customer_segment != "Flagged for deletion"`. This is the ~700-1,000-account list (was ~400 in Phase 1) used to cross-reference exec-hire + hiring-spike detections. Slice into **6 segment buckets** (Colo / Fiber / NeoCloud / Network Op / MSP-Aggregator / Enterprise) for the sub-agent fanout.

1. **Stage 1.A - Colocation scrape:** Operate on the Colo segment slice. Scrape Tier A + Tier B Colo signals using the Colo-specific source list (DCD, Data Center Frontier, BISNOW DC, planning-department dockets, electric-utility queues, hyperscaler announcement feeds). Output: `colo_signals[]`.

2. **Stage 1.B - Fiber scrape:** Operate on the Fiber slice. Scrape Tier A + Tier B Fiber signals using the Fiber source list (Fierce Network, Light Reading, BroadbandNow, BEAD state portals, USTelecom, NTCA, ABS prospectus filings via SEC EDGAR, FCC dockets). Output: `fiber_signals[]`.

3. **Stage 1.C - NeoCloud scrape:** Operate on the NeoCloud slice. Highest-velocity segment - scrape Tier A + Tier B NeoCloud signals (TechCrunch GPU, The Information GPU economy, Crunchbase AI Infrastructure, NVIDIA partner pages, AnandTech, ServeTheHome, HPCWire, The Next Platform, PeeringDB diff feeds, IX participant lists, MLPerf submissions, SEC EDGAR 8-K Items 1.01 + 2.03). Output: `neocloud_signals[]`.

4. **Stage 1.D - Network Operator scrape:** Operate on the Network Op slice. Scrape Tier A + Tier B Network Op signals (Light Reading SP news, TelecomTV, Capacity Media, Mobile World Live, earnings transcripts via SEC + Seeking Alpha, TM Forum, CAMARA / Nephio / ONAP / OpenConfig / Sylva GitHub feeds, FedBizOpps RFP filings). Output: `network_op_signals[]`.

5. **Stage 1.E - MSP/Aggregator scrape:** Operate on the MSP slice. Scrape Tier A + Tier B MSP signals (ChannelE2E, CRN, Channel Futures, ScanSource + TD SYNNEX earnings, TSD press releases, partner-add announcements from Megaport / Console Connect / PacketFabric). Output: `msp_signals[]`.

6. **Stage 1.F - Enterprise scrape (NEW 2026-05-11):** Operate on the Enterprise slice. Scrape Tier A + Tier B Enterprise signals using the Enterprise source list per `context/signals/enterprise-signals.md` (SEC EDGAR full-text 10-K + 10-Q + 8-K Items 1.01/2.01/5.02/8.01, American Banker / Modern Healthcare / Becker's / Retail Dive / Nelson Hall / Everest Group, HHS OCR + NY DFS + PCI Council + DORA enforcement portals, Equinix / Megaport / PacketFabric customer-win pages, NVIDIA partner press for Enterprise GenAI deployments). Apply IT MSP Test inversely - EXCLUDE consulting firms (Deloitte / McKinsey / BCG / Bain) from Outsourcing Services - Enterprise classification per `context/segments/enterprise.md`. Apply hard scale gate ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng + vertical match) when classifying net-new candidates - segment-classification owns the gate. Output: `enterprise_signals[]`.

7. **Stage 1.G - Aggregate:** Combine all 6 outputs into `detected_signals[]`. Dedup by `(company_domain, signal_code, source_url_hash)`. Per-segment counts go to Cooper's run report. (Enterprise sub-stage may run thin during the 4-6 weeks post-promotion source validation period - do not auto-flag thin Enterprise coverage during that window.)

**Per detection, record:** company name(s), signal type (e.g., "C-A2 GPU Cloud Tenant Anchor"), signal tier (A/B/C), detection date, source URL, full signal body, originating segment sub-stage.

**Output:** `detected_signals[]`  -  a list of signal hits with company, segment, and metadata.

**Notes:**
- Universal signals (U1-U6, AP-1/2/7, FR-1, I1/I2) are scraped within EACH sub-stage, then deduped at Stage 1.G. A single exec hire that matches a multi-segment company gets one entry tagged with the company's current segment.
- Greenfield signals (Colo + NeoCloud) detect across all 5 stages (S1-S5) but score bonuses apply only at S2-S3.
- **International signals (I1, I2) fire for Tim Ziemer's territory.** Scrape the international source stack within the Colo / Fiber / Network Op / NeoCloud sub-stages - territory assignment happens at match time based on HubSpot `country`.
- The canonical per-segment source ledger lives in each `cowork-scheduled-tasks/signal-scan-{colo,fiber,neocloud,networkop,msp,enterprise}/prompt.md`. Those prompts are the operational source of truth; this SKILL is the architecture spec.

### STAGE 2 - Match to HubSpot

**Input:** `detected_signals[]` from Stage 1.

**Operation:**
1. For each detected signal, extract the company domain (or resolve company name to domain via Apollo if missing).
2. Search HubSpot by domain. Classify each hit:
   - **MATCH**: domain exists in HubSpot → attach `record_id`, `hubspot_owner_id`, `customer_segment`, `account_tier`, `state`, `country`, `last_enriched_date`, `account_brief`, `infrastructure_profile`, `linkedin_company_page` for downstream stages
   - **NEW**: domain not in HubSpot → route to Stage 3 for enrichment (Apollo org enrichment in Stage 3 returns LinkedIn URL which gets written to `linkedin_company_page` on new-account creation)
3. **Apply Phase 1 suppression list** - drop these matched or new accounts silently, logging count in Cooper's run report:
   - **MaiaEdge's own record** - HubSpot company ID `124293230301`.
4. Flag any `customer_segment = "Flagged for deletion"` accounts and drop them from further processing (per CRM Guardian invariant  -  never touch flagged accounts).

**Output:** `matched_accounts[]` and `new_companies[]`.

### STAGE 3 - Enrich New Companies

**Input:** `new_companies[]` from Stage 2.

**Stage 3 runs the FULL R1 five-stage pipeline** per `context/account-tiering/enrichment-protocols.md` - research-first workflow including the D1 disqualifier check (drop confirmed non-ICP / junk pre-Apollo) and the D5 v2 per-sub-segment protocols (each of the 30 active sub-segments per `context/account-tiering/sub-segment-qualification.md` has its own qualifying-evidence checklist; the protocols document is the canonical source). Stage 3 is NOT a lightweight enrichment - it's the same pipeline R1 runs daily, just triggered by signal-scan detection instead of import or trigger-query candidate selection. Use the 30 active sub-segment values (case-sensitive) from `context/account-tiering/sub-segment-qualification.md`. Key new values: `Subsea cable operator` (added 2026-05-14, 30th active), `Greenfield` is a real sub-segment paired with Colo or NeoCloud parent, `Crypto to AI - Neoclouds` inclusive of operator AND landlord. Retired values (never write): `Co-op/consortium`, `External Extension - Network operator`, `Internal + external unification - Network Operator`, `Managed Network Services - Network Operator`.

**Operation:** For each new company:
1. Run `company-enrichment` Phase 1 (Apollo org enrichment + website read)  -  determines segment, state, country
2. **D1 disqualifier check** per `context/account-tiering/enrichment-protocols.md` - drop confirmed non-ICP / junk records before continuing (saves Apollo credits on Stage 3 candidates that signal scan happened to detect but are not actually viable).
3. If the company classifies as ICP (customer_segment in Colo / Fiber / Network Op / NeoCloud / MSP/Aggregator / **Enterprise-CustomerSegment**), proceed to Phase 2 (segment-specific research) + **D5 v2 per-sub-segment protocols** for the matching sub-segment. For Enterprise candidates, the scale gate must pass during enrichment ($1B+ rev + 3+ DCs OR Equinix Fabric/Megaport port OR confirmed in-house net eng + vertical match) - segment-classification routes scale-gate failures to `Other`.
4. If non-ICP, drop from report (do not create HubSpot record  -  no point cluttering CRM with non-ICPs detected via signals)
5. Apply `crm-guardian` safety tiers:
   - HIGH confidence → Tier 1 auto-create in HubSpot via `manage_crm_objects.createRequest` (`objectType: "companies"`, properties map, `confirmationStatus: "CONFIRMATION_WAIVED_FOR_SESSION"`)
   - MEDIUM confidence → Tier 2 auto-create via same MCP call + flag in run report
   - LOW / MANUAL_REVIEW → Tier 3 hold (appears in rep report's "Possible new accounts  -  review needed" section, NOT auto-created, NOT written to any file for batch-import)
6. Run `territory-manager` on every new account to assign `hubspot_owner_id` from state/country (this is an MCP write, not a file write)
7. Run `account-brief` skill to populate initial `account_brief` field via MCP
8. Populate `recent_news_or_trigger_event` with the signal that surfaced them via MCP
9. **Stage 3 NEW-account creates DO bump `last_enriched_date`** per CLAUDE.md Unified Stamping Policy - the full enrichment pipeline ran, so the 120-day rotation gate counter starts today. Contrast with Stage 5 partial writes (which do NOT bump).

**All writes in this stage are MCP calls. No XLSX file is ever produced as a substitute for or alongside these MCP writes.** If the runtime is tempted to queue a "Phase 2 batch import" file for deferred / low-confidence accounts, that is a bug - Tier 3 holds surface to Cooper via the run report and get actioned by hand in HubSpot UI, not via file upload.

**Output:** `enriched_new_accounts[]` (with HubSpot record_id, owner, segment, brief).

**Credit budget - soft floor:** At Stage 3 entry, check remaining Apollo credits for the current billing cycle. If remaining credits fall below 20% of monthly allocation, **pause new-account enrichment for this run** (process only enrichments needed for accounts already in HubSpot via Stage 2 matching). Surface the pause in Cooper's run report: "Apollo credits at X% of monthly allocation - N net-new companies deferred to next run." Deferred companies get queued and re-checked next Monday. Matched accounts (already in HubSpot) still get enriched since they're the priority spend. No runaway-week risk.

### STAGE 4 - Score Every Hit

**Input:** `matched_accounts[]` + `enriched_new_accounts[]`, each joined to its triggering signal(s).

**Operation:** For each account-signal pair, compute Meeting Probability Score per `context/signals/signal-framework.md`:

```
score = tier_weight × freshness_weight × confidence_weight

Tier weights: A=3, B=2, C=1
Freshness weights (Phase 2):
  Tier A:  ≤60d = 3, 60-90d = 2, >90d = drop entirely
  Tier B:  1wk = 3, 30d = 2, 90d = 1
  Tier C:  paired-only - inherits freshness from the Tier A/B it stacks with
Confidence weights: High=3, Med=2, Low=1
```

**Tier A freshness window updated 2026-04-27 per Cooper:** announcements within the past 60 days score at full freshness for Tier A. The catalogs already document 60-90+ day action windows on Tier A signals (90-day exec mandate, 60-120d M&A integration, 18-24 month BEAD ramps, 12-18 month CTrO platformization) - the old steep decay floored these out. Tier B keeps the steeper decay since Tier B is by-definition "30-90d window" signals.

If same account hit by 2+ signals in the week where at least one individual signal scores ≥ 8, elevate score to 18+ (stacking rule - see `context/signals/signal-framework.md` for the ≥8 floor rationale). Apply bonus rules:
- **Greenfield S2-S3 bonus:** +3 (Colo + NeoCloud only)
- **Site count 1→2 transition bonus:** +6 (Colo + NeoCloud only - parse current count from free-text `infrastructure_profile` field; if parse is low-confidence, skip the bonus and rely on base greenfield scoring)

When a facility transition is detected and confirmed, **rewrite `infrastructure_profile`** in HubSpot with the updated count + context (e.g., "3 facilities: NoVA (2), Dallas (1); announced Phoenix facility Q2 2026 = transitioning to 4"). This keeps the next run's state fresh without needing a dedicated integer field.

**Output:** `scored_accounts[]`  -  each account with its highest-scored signal, score value, and stacked-signal list.

### STAGE 5 - Update HubSpot Fields

**Input:** `scored_accounts[]`.

**Authoritative source for each field** (Apollo-refreshed fields from Stage 1/3 enrichment flow through here - Apollo is the source of truth for firmographic identity on every run):

| Field | Write / overwrite rule |
|-------|------------------------|
| `recent_news_or_trigger_event` | Overwrite with highest-scored signal this week. **Pure narrative, no date prefix** (post-2026-05-28; the legacy `[YYYY-MM-DD]` prefix convention was retired - date now lives structurally in `last_signal_date`). Format: `[Signal Type] - [one-line summary]`. Hard cap 250 chars. |
| `account_brief` | Regenerate via `account-brief` skill if (a) existing brief >30 days old OR (b) fresh signal research materially diverges from existing brief (facility count changed, sub-segment shifted, anchor tenant announced). If 2+ signals hit, append "Also this week:" line (stay under 400 char total). If research matches current brief, leave it. |
| `infrastructure_profile` | Rewrite with updated facility count + context when a 1→2 or N→N+1 transition is confirmed at HIGH confidence. Preserves next-run parse state. |
| `state` | **Overwrite from Apollo** when Apollo returns a non-empty value different from HubSpot AND `last_enriched_date` is blank or 120+ days stale. HQ relocations are real. |
| `country` | **Overwrite from Apollo** on same rule as `state`. A US→non-US change triggers owner cascade to Tim Ziemer. |
| `hubspot_owner_id` | **Re-derive** from refreshed `state`/`country` via `territory-manager`. Cascade to associated contacts (Tier 1). |
| `linkedin_company_page` | **Overwrite from Apollo** `linkedin_url` when Apollo returns non-empty value differing from HubSpot. Handles rebrands / M&A LinkedIn-handle changes. |
| `domain` | **Conditional overwrite** - write Apollo's domain only if current HubSpot value is blank OR the HubSpot domain fails to resolve / redirects to Apollo's domain. If both are live-but-different, surface as Tier 2 (applied + flagged - likely rebrand worth Cooper's review). |
| `last_enriched_date` | **Stage 5 partial writes do NOT bump** per CLAUDE.md Unified Stamping Policy - signal-scan partial field writes are intentionally excluded from the 120-day rotation gate. Only Stage 3 NEW-account creates DO bump (the full company-enrichment pipeline ran). |

Canonical overwrite spec lives in `skills/company-enrichment/SKILL.md` Step 0C - this routine references it, does not redefine. If the two diverge, company-enrichment wins.

### Stage 5b - Signal Field Writes + Tier Recomputation + Signal Heat Recomputation (NEW 2026-05-14 - Phase 3; signal_heat added 2026-05-20)

After the Stage 5 field writes complete, every account that scored ≥8 this run gets THREE additional signal-tracking field writes, followed by a tier recomputation AND a signal-heat recomputation:

| Field | Write rule |
|-------|------------|
| `last_signal_score` | Numeric. Write the highest Meeting Probability Score this account received this run. Used downstream by the tier-compute spec as a signal modifier input. |
| `last_signal_date` | Date. **Event date** of the highest-scored signal hit this run - when the news/funding/hire actually happened (extract from the source article; if the body doesn't explicitly state the event date, use article publication date as a ±few-day approximation). Semantics narrowed 2026-05-28 - was previously written as today's run date (detection); now stores event date. Pairs with `last_signal_score` so the tier function can apply freshness decay against the actual event. |
| `signal_count_last_30d` | Integer. Count of distinct events on this account whose event date falls within the trailing 30 days. Used as a stacking-density modifier in the tier function. Sub-8 matches also count (Cooper 2026-05-22). |

**Tier recomputation (mandatory after the three signal writes):**

Call `compute_tier()` per `context/account-tiering/tier-compute-spec.md` with inputs `(customer_segment, company_sub_segment, last_signal_score, last_signal_date, signal_count_last_30d, hs_is_target_account)`. The spec defines the canonical defaults table, signal modifier weights, and clamping rules. Write the returned `account_tier` value back to HubSpot.

**`hs_is_target_account = true` override (canonical behavior from the spec):** if the record has `hs_is_target_account = true`, the three signal field writes proceed normally (these are observability fields, not tier writes), but the tier write is **SKIPPED**. The spec's compute-then-skip-write semantics honor Cooper's manual tier override on target accounts. Log the computed tier in the run report's audit table but do not persist.

**Signal heat recomputation (mandatory, applies REGARDLESS of `hs_is_target_account`):**

Call `compute_signal_heat()` per `context/account-tiering/tier-compute-spec.md` §11.5 with inputs `(last_signal_score, last_signal_date (event date), signal_count_last_30d, open_deal_state)`. Returns one of `Hot` / `Warm` / `Cool` / `Cold` (Title Case per HubSpot enum). Write the returned `signal_heat` value back to HubSpot if it differs from the current value (idempotent no-op if equal). Heat writes are NOT frozen by `hs_is_target_account` - tier is rep-locked, heat always reports the truth. On heat change, write a HubSpot company note: `"Heat <old> -> <new> on YYYY-MM-DD by Signal Scan: <reason>"` (Title Case heat values in the note).

**Safety tier per CRM Guardian:** signal field writes + tier recompute follow the same deal-protection rules as Stage 5 - Tier 1 on accounts without open deals, Tier 2 on deal-protected (applied + flagged), Tier 3 hold for LOW-confidence signals on Tier 1 accounts.

**Safety tier per CRM Guardian:**
- Tier 1 (auto-write): field updates on accounts without open deals
- Tier 2 (auto-write + flag): field updates on deal-protected accounts; also `domain` rebrand-suspect writes and any state/country change that shifts territory on an account with an open deal
- Tier 3 (hold): LOW-confidence signals on critical accounts (Tier 1 accounts) → surface for Cooper's review. Apollo returns a state/country that contradicts a recent <30d manual note → Tier 3 (recent human input wins over automation)

**Never overwrite:** `lifecyclestage`, `hs_lead_status`, `type`, `hs_is_target_account`, MEDDPICC deal fields, custom notes. These are sales-owned.

### STAGE 6 - Generate Per-Rep Reports (Cascade by Score)

**Input:** `scored_accounts[]` split by `hubspot_owner_id`.

**Operation:** For each of the 3 rep pools:
1. Filter `scored_accounts[]` where owner matches rep.
2. **Apply Phase 2 score floor:** drop every account-signal pair scoring below **12** from the rep DM. Score 8-11 → Watch List path: write `recent_news_or_trigger_event` at Stage 5 but do NOT include in rep DM. Below 8 = silent drop, no CRM write either.
3. **Apply 40-total cap per rep (Phase 2):** rank remaining candidates globally (across all segments) by Meeting Probability Score descending, take top 40. Overflow drops to Watch List. Fewer is fine - if only 18 accounts clear the bar this week, the list is 18.
4. Group the top 25 by `customer_segment` for Excel tab organization only. **Rep-facing label for MSP:** display as "MSP / Aggregator" (matches the HubSpot internal value `MSP/Aggregator`).
5. **Assign a priority tier to each account based on score (Phase 2 bands):**

   | Tier | Score range | Emoji | Rep framing |
   |---|---|---|---|
   | Highest priority | 27+ | `:red_circle:` | top-scored accounts this week |
   | Strong signals | 18-26 | `:large_orange_circle:` | strong signal, worth prioritizing |
   | Worth reviewing | 12-17 | `:large_yellow_circle:` | solid signals on the radar |

   Phase 1 used 27+ / 22-26 / 18-21 bands. Phase 2 widens the orange band downward to capture the relevance gains from Tier B activation. Phase 3 may add a blue band at 8-11 if Watch-List behavior moves to the DM.

6. Generate **Slack DM body** (written for reps, tactical tone, cascade-by-score - no segment grouping in the message itself):

   ```
   :satellite_antenna: *Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]*
   [N] accounts cleared the quality bar this week. Ranked by score, highest first. Full detail in the attached Excel.

   :red_circle: *HIGHEST PRIORITY* - Score 27+
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body in 1-2 sentences. Name the persona + the specific wedge.]

   :large_orange_circle: *STRONG SIGNALS* - Score 22-26
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body, 1-2 sentences]
   • ...

   :large_yellow_circle: *WORTH REVIEWING* - Score 18-21
   • *[Account Name]* (Segment) · Score [N] · <[HubSpot URL]|open>
     [Signal body, 1 sentence - keep these tighter since volume is higher]
   • ...

   :sparkles: *NEW TO YOUR TERRITORY*
   • *[Account]* (Segment) - [reason enriched]
   • ...

   Full 14-column detail (LinkedIn URL, Suggested Angle, full Signal Body) in the attached Excel.
   ```

   **Tone rules unchanged:** tactical not strategic, short sentences, name-drop accounts, persona-aware angles. **No "call" language** - reps work these via their usual outbound channels; the DM tells them which accounts are top-scored, not what motion to run.

   **Skip empty sections.** If no accounts cleared 27+, drop the `HIGHEST PRIORITY` heading entirely - don't show "0 accounts" under it. Same for the other tiers.

7. Generate **Excel attachment** (`.xlsx`) - **this is a rep-facing read-only deliverable, NOT a HubSpot import file.** The Excel is what reps open on Monday morning; it is never ingested back into HubSpot, never treated as a source of truth for the CRM, never used as a retry path for a failed Stage 5 MCP write. All HubSpot writes already happened in Stages 3 + 5 via MCP before this file is assembled.
   - **Filename:** `weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx`
   - **Tabs:** one per segment with hits (skip empty segments). Sort each tab by Meeting Probability Score descending. Total rows across tabs ≤ 25 in Phase 1.
   - **Columns:** Account Name | Customer Segment | Sub-Segment | Account Tier | Signal Heat | Account Owner | HubSpot URL | LinkedIn URL | Signal Type | Signal Body | Detection Date | Meeting Probability Score | Account Brief | State | Suggested Angle
   - **Signal Heat column** reads the freshly-computed `signal_heat` from Stage 5b for every row (including `hs_is_target_account = true` rows - heat is not frozen). Values are Title Case (HubSpot enum): `Hot` / `Warm` / `Cool` / `Cold`.
   - **Color coding (SUBTLE - score cell only, not whole row):** apply a pastel fill to the "Meeting Probability Score" cell based on priority tier. Use `openpyxl` `PatternFill` with `fill_type="solid"`:
     - Score 27+ → `FFEBEE` (pastel red, `:red_circle:` equivalent)
     - Score 22-26 → `FFF3E0` (pastel orange, `:large_orange_circle:` equivalent)
     - Score 18-21 → `FFFDE7` (pastel yellow, `:large_yellow_circle:` equivalent)
   - Leave every other cell white. No bold, no borders beyond default, no header-row color changes. The point is a glanceable score column, not a highlighter-riot spreadsheet.
   - Header row stays default (bold Calibri 11 or similar - Excel default).

### Depth Spec for Every Row

Because the cap is 50, we invest in depth per account. For each row:
- **Signal Body** = 3-5 sentence synthesis: what happened, when, who's involved, the specific pain it exposes for this prospect, a pulled quote from the source + source URL. Reads like a call-prep, not a headline.
- **Suggested Angle** = persona-aware and signal-specific. Names the right persona (e.g., "reach Sarah Chen, the new VP Network (started 5 weeks ago) - reference her Equinix-fabric background and Prime's pending Phase II") and the signal-appropriate wedge (e.g., "GPU tenant anchor - reach platform owner before fabric decision is locked"). Derived from signal type + account context, not a template.
- **Account Brief** = regenerate via the `account-brief` skill whenever either condition is true: (a) the HubSpot `account_brief` is more than 30 days old at match time, OR (b) the fresh signal research materially diverges from what's in the existing brief (e.g., facility count changed, sub-segment shifted, a new anchor tenant announced). If research closely matches the existing brief, leave it. The goal is "reps never see a stale brief OR one that contradicts the news in the same row."

**Output:** 3 email payloads (body + attachment file).

### STAGE 7 - Deliver (Slack DMs + Excel attachments)

**Input:** 3 rep payloads (Slack message body + Excel attachment path).

**Operation:**
1. **First line of Slack message (acts as subject):** `:satellite_antenna: *Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]*` (use the subject emoji once at top; the cascade tiers use `:red_circle: / :large_orange_circle: / :large_yellow_circle:` per Stage 6).

2. **Post via `slack_send_message`** as a self-DM to the routing target. Cooper receives Tim Ziemer's international report in Phase 1 (to start) for signal-quality validation before handing off to Tim Z directly.

3. **Routing:** Territory-to-owner mapping is the 5-region model in `context/hubspot/territory-model.md`. The aggregator task at `cowork-scheduled-tasks/signal-scan-aggregator/prompt.md` owns the live routing table with current Slack channel IDs. Derive `hubspot_owner_id` from `state`/`country` using `context/hubspot/territory-model.md` at runtime; do not hardcode a 2-region map here.

   Current rep DM recipients (cross-check against `context/hubspot/territory-model.md` before any sender-routing change):
   - Tim Lieto (`161889085`) - Northeast + West interim: `U0A973L1HFF`
   - Ken Cunningham (`162339176`) - Southeast: `U0AE1PGCB6C`
   - Tory Teague (`165480917`) - Central: `U07C3MNBQK2` (confirm Slack ID in aggregator prompt)
   - Markus Hendrich (`164949459`) - Europe: (confirm Slack ID in aggregator prompt)
   - Tim Ziemer (`159350430`) - International + Tier 1 SP: `U0A24D9RJLS` (**Cooper** override during Phase 1 validation)

   The rep's first-name label in the message body follows the TERRITORY POOL, not the recipient.

4. **Excel attachment delivery:** Slack MCP `slack_send_message` does NOT support binary attachments. The Excel file is referenced via a download link in the message body. Options:
   - If the routine writes the Excel to a publicly-accessible location (S3 / GDrive / SharePoint public link), include the download URL in the message body.
   - Fallback for Phase 1: write the Excel to the repo at `weekly-reports/YYYY-MM-DD/[rep-last-name].xlsx` and include the GitHub raw URL in the Slack message. Commit + push happens as part of Stage 7. Example message footer: `> Excel: <https://github.com/[org]/maiaedge-ai/raw/main/weekly-reports/2026-04-27/lieto.xlsx|download>`.

5. **Cooper's consolidated run report** (separate Slack DM to Cooper only): total signals detected, HubSpot accounts touched (breakdown by field), new accounts enriched (Tier 1/2/3 counts), Apollo credits consumed + % of monthly allocation remaining, Tier 3 holds, deal-protected writes, per-rep output size (so Cooper can see "Tim got 12 accounts, Ken got 8, Tim Z [Cooper] got 3"), weekly trend vs. prior 4 runs, errors.

6. **Consistent message prefix** for Slack search grouping: all four messages (3 rep reports + Cooper's run report) lead with `*Weekly Signal Scan -` so they thread/search together.

7. **Phase 2 transition (future):** when Cooper is satisfied with Tim Z territory signal quality, change the `Tim Ziemer` row's `channel_id` from `U0A24D9RJLS` to Tim Z's actual Slack user ID (look up via `slack_search_users` at transition time). No other routing logic changes.

---

## Rep Slack DM Template (Phase 1 - cascade by score)

Each rep pool gets its own Slack DM. The structure is a **score cascade** (hottest at top, cooler below) - NOT segment-grouped paragraphs. Segment is shown inline per row as context, not as a grouping axis. Segment-grouped briefings are disabled in Phase 1 because they spread attention across the page and bury the truly hot signals; reps work hottest-first in Phase 1.

Template below. Square-brackets are fill-ins. Skip any tier heading where zero accounts clear its range - don't show "0 accounts" or empty sections.

```
:satellite_antenna: *Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]*

Hey [Rep First Name] - [N] accounts cleared the Phase 1 quality bar this week. Ranked by score, highest first. Full detail in the Excel linked at the bottom.

:red_circle: *HIGHEST PRIORITY* - Score 27+

• *[Account Name]* (Segment · Tier [1-5]) · Score [N] · <[HubSpot URL]|open>
  [1-2 sentence signal synthesis - what happened, who to reach, the specific wedge. Name the persona.]
• [next account if any]

:large_orange_circle: *STRONG SIGNALS* - Score 22-26

• *[Account Name]* (Segment · Tier) · Score [N] · <[HubSpot URL]|open>
  [1-2 sentence signal synthesis]
• [...]

:large_yellow_circle: *WORTH REVIEWING* - Score 18-21

• *[Account Name]* (Segment · Tier) · Score [N] · <[HubSpot URL]|open>
  [1 sentence - keep tight at this tier; full detail is in the Excel]
• [...]

:sparkles: *NEW TO YOUR TERRITORY*

[N] new accounts enriched + added via signal scan this week:
• *[Account]* (Segment) - [reason surfaced]
• [...]

Full 14-column detail (LinkedIn URL, Suggested Angle, full Signal Body, Account Brief): <[GitHub raw URL to Excel]|download>
```

**Tone rules:**
- Tactical, not strategic. Surface which accounts are top-scored this week - don't prescribe the outbound motion.
- Short sentences. No jargon reps don't already use.
- **No "call" language** - "reach" / "open with" / "worth a touch" is fine, "call today" is not. These are top-scored accounts; reps pick the channel.
- Name-drop accounts + personas - "Sarah Chen, VP Network (started 5 weeks ago, ex-Equinix)" beats "this new hire signals opportunity."
- No "Watch for" / theme paragraph in Phase 1. The cascade is the theme.

---

## Edge Cases

### No signals hit for a segment in the rep's territory
Skip that segment entirely in the Excel - no empty tab. The Slack message doesn't group by segment in Phase 1 so no empty headings appear. If the rep has ZERO accounts clearing the Phase 1 score-18 floor across all segments, send a short Slack DM: `:satellite_antenna: *Weekly Signal Scan - [First Name] - Week of [YYYY-MM-DD]* - Quiet week in your territory. No accounts cleared the Phase 1 signal quality bar. See you next Monday.` No attachment. This is a feature, not a failure - noise suppression is the point of the score floor.

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

### Web Tools (updated 2026-05-11 - runtime methodology change)
- `web_search`  -  **PRIMARY** signal-discovery tool on Cowork. Used in the search-anchor pattern: each documented source in `context/signals/[segment]-signals.md` is anchored via `web_search "{domain} {topic} {year}"`. Snippets returned by search are read directly for date / company / signal-type; article URLs returned can be passed to `web_fetch` for full text.
- `web_fetch`  -  **SECONDARY**, used after search-anchor returns article URLs. Direct fetches against catalog source domains fail URL-provenance gating on Cowork - only fetches against URLs returned by `web_search` reliably work. On oversized HTML, save to disk and use `headline_extract.py`.

This is a reversal of the 2026-05-05 guidance, which placed `web_fetch` primary. The 2026-05-11 reachability audit (68 URLs tested) confirmed direct fetch is universally blocked on this runtime, while search-anchor produces fresh dated content for ~95% of documented sources.

### Helper Scripts (archived post-2026-05-28 split)

These helpers supported the monolithic parent-runtime architecture. After the 2026-05-28 split into 7 per-segment + aggregator Cowork tasks, their gate logic was inlined directly in the per-segment prompts. The files are archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/helpers/` for reference only.

- `headline_extract.py`  -  Bash-callable Python parser. Reads a saved `web_fetch` HTML file, returns JSON of headlines matching segment keywords + 14-day date window.
- `check_source_coverage_gate.py`  -  Reads `sources_attempted.json` after Stage 1, returns pass/fail per segment (≥80% coverage required).
- `check_volume_gate.py`  -  Reads `scored.json` after Stage 6 fill-down, returns pass/fail per rep (≥25 floor OR carryover exhausted).

### Exec Hire Detection (no Sales Navigator required)
- SEC EDGAR 8-K Item 5.02 for public companies (officer changes, daily feed)
- PR Newswire / Business Wire "Appointments" / "People on the Move" tag RSS
- Trade press "People" columns (Fierce Network, Channel Futures, Light Reading, TelecomTV, Capacity Media, DCD Careers, DCF People) scraped weekly
- Company IR newsroom RSS for each target company
- Crunchbase News "Executive Moves" tag for NeoClouds / startups
- TheOrg.com free tier for org-structure diffing
- Apollo job-change detection (existing CRM Guardian Job 6, quarterly default) - tighten to monthly for Tier 1 accounts if needed
- Public job post sources for hiring-spike detection: LinkedIn public Jobs, Indeed, Greenhouse, Lever, company careers pages

Full substitute mapping documented in `context/signals/signal-framework.md` under "Exec Hire Detection Without Sales Navigator."

### Slack MCP (rep report + run report delivery)
- `slack_send_message`  -  post each rep's cascade report as a self-DM. Channel IDs in Stage 7 routing table. Use Slack mrkdwn for formatting; fenced code blocks for the "New to Territory" bullet list if it gets long. Excel attachment referenced via download URL (GitHub raw or equivalent), NOT uploaded directly.
- `slack_send_message` with `thread_ts`  -  optional overflow for a rep whose report exceeds 5,000 chars (e.g., a big Monday with many Call-Today accounts). Keep the parent message under 5,000 and thread the Priority / This Week sections below.
- Cooper's consolidated run report posts as a separate DM to `U0A24D9RJLS` - distinct from the Tim-Z-territory report Cooper also receives in Phase 1. Keep them as two separate messages for clarity.

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

- **Orchestrated by:** `crm-guardian` Job 8 - weekly, Mondays (see `crm-guardian/SKILL.md` Master Cadence)
- **Triggers:** `company-enrichment` (Stage 3 new-account enrichment), `territory-manager` (Stage 3 owner assignment), `account-brief` (stale brief regeneration + research-divergence regeneration), `account-sourcing` (unclear-segment fallback)
- **References:** `context/hubspot/property-schema.md`, `context/hubspot/territory-model.md`, segment cheatsheets, signal framework + catalogs

---

## Scope Guardrails

- **Phase 2 cap: 40 accounts TOTAL per rep per week** (was 25 in Phase 1, not per segment). Ranked globally across the rep's territory. Fewer is fine - if only 18 accounts clear the Phase 2 score-12 floor this week, the list is 18. Phase 3 may go to 50.
- **Score floor of 12 (Phase 2).** Below 12 = dropped from rep DM. Score 8-11 → Watch List CRM write only (rep sees signal in HubSpot, not in DM).
- **Depth over breadth.** Each row reads like a mini call-prep (3-5 sentence signal body + persona-aware angle + fresh brief). Compute budget saved by capping at 50 funds this depth.
- **Territory purity.** Reps see only their territory.
- **Written-for-reps tone.** Tactical, not strategic.
- **No competitor naming** in field writes or email copy (use "third-party fabrics").
- **No em dashes** in any HubSpot field write.
- **250-char hard cap** on `recent_news_or_trigger_event`  -  never exceed.
- **Non-ICP signals don't create HubSpot records.** Signal on a non-ICP company = drop silently.
- **Flagged-for-deletion accounts are skipped entirely** (per CRM Guardian invariant).
