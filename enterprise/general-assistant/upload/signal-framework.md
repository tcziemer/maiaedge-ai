# Signal Framework - Cross-Segment Reference

Source-of-truth for the `weekly-signal-scan` skill. Defines the scoring model, universal signal types, scrape sources, and the rep-facing delivery spec.

> **⚠️ Phase 3 overrides (as of 2026-05-04):** The `weekly-signal-scan` skill currently runs in **Phase 3 mode**. Where this file and the skill's Phase 3 section disagree, **the skill wins**. Phase 3 active overrides:
> - **Score floor: 8** (was 12 in Phase 2). Score 8-11 surfaces in rep DM as `LIGHT` cascade tier (green emoji). Below 8 = silent drop. Watch List concept retired.
> - **Cap target: 25-50 per rep, hard cap 50.** Three-tier fill-down: Primary (≥12) → LIGHT (8-11) → Carryover News (open-lane). Carryover fires only when natural Primary + LIGHT pool <25.
> - **Carryover News pool (new):** accounts where prior-week `recent_news_or_trigger_event` is ≤30 days old AND no rep activity logged ≤14 days. Built at Preflight Check G; consumed only by Stage 6 fill-down.
> - **Detection window: 14 days rolling** (was 7-day strict). Tier A scoring brackets unchanged.
> - **Stage 1 runs as parallel sub-agents on Cowork** (5 sub-agents, one per segment). The 2026-05-04 retirement of parallel sub-agents was specific to Claude Code's egress proxy block; Cowork has no equivalent block. The 2026-05-11 reachability audit confirmed direct `web_fetch` is universally URL-provenance-gated on Cowork's runtime - so the access methodology changed (see next bullet) but the parallel-fanout pattern is correct.
> - **Search-anchor pattern is the canonical access method** (updated 2026-05-11): for each documented source in the segment's catalog "Sources for This Segment" sub-section, run `web_search "{domain} {topic} {year}"` and read snippets + follow article URLs returned in search results. `web_fetch` is used as a follow-up against article URLs returned by `web_search`, not against documented source domains directly. Sub-agents must attempt every documented source via search anchor - generic search queries that don't anchor on a documented domain do NOT count toward source coverage.
> - **Tier A + Tier B both active.** Tier C paired-only. AP-5, AP-6, FR-2, and Noise List signals remain disabled.
> - **Delivery: Slack DMs.** Phase 0 partial lift active - Tim Lieto cascade → `U0A973L1HFF` (LIVE direct), Ken cascade → `U0AE1PGCB6C` (LIVE direct), Tim Ziemer International → `U0A24D9RJLS` (still Cooper, validating), Cooper run report → `U0A24D9RJLS`. Each rep DM body carries top 15-20 inline + threaded full-list table.
> - **Git-free run.** Local `weekly-reports/YYYY-MM-DD/` is the WoW baseline + Apollo-budget tracker store. No GitHub fallback, no commit/push anywhere.
> - **Signal code disambiguation:** both NeoCloud and Network Operator catalogs use `N-A*` prefix - runtime uses `NC-A*` (NeoCloud) and `NO-A*` (Network Operator) to disambiguate.
> - **Suppression list:** MaiaEdge's own record (124293230301), any `customer_segment = "Flagged for deletion"` account.
>
> See `skills/weekly-signal-scan/SKILL.md` "2026-05-28 split" header for the live 7-task architecture (6 per-segment scans + aggregator under `cowork-scheduled-tasks/signal-scan-*`). The monolithic `cowork-scheduled-tasks/weekly-signal-scan/` is archived at `routines/archive/cowork-disabled/weekly-signal-scan-monolithic/` and MUST NOT be re-enabled. Phase 1 (floor 18 / cap 25 / Tier A only) and Phase 2 (floor 12 / cap 50 / Watch List 8-11 not surfaced) are historical and superseded.

---

## Purpose

The signal framework defines what to scrape, how to score, and how to deliver a weekly Monday-morning briefing that answers one question per rep: **"Which accounts in my territory have a fresh, time-bound reason to meet this week?"**

The framework pairs with 5 per-segment signal catalogs + 1 cross-segment file:
- [colocation-signals.md](colocation-signals.md)
- [fiber-signals.md](fiber-signals.md)
- [network-operator-signals.md](network-operator-signals.md)
- [neocloud-signals.md](neocloud-signals.md)
- [msp-aggregator-signals.md](msp-aggregator-signals.md)
- [universal-platform-signals.md](universal-platform-signals.md)  -  Apollo + free cross-segment signals (AP-1 through AP-7, FR-1 through FR-3)

**Production stack:** Apollo (licensed) + free sources + web search. Paid Phase 2 signals (PitchBook, Structure Research, Kentik, HG Insights, LinkedIn Sales Navigator, Leadfeeder, 6sense, BuiltWith, etc.) are out of scope and not wired into the scanner.

---

## Universal Signal Types

These 6 signal classes fire across every segment. Detection is the same; per-segment catalogs refine the patterns.

| # | Signal Class | Why It's Universal |
|---|---|---|
| U1 | Exec Hire in Network/Infra/Automation role | New-in-seat has 90-day mandate to propose something new. Highest-confidence relationship-entry signal. |
| U2 | M&A / PE Roll-up - Announcement OR Close | Fire on BOTH events, not just close. Announcement = strategic decision made; 6-18 months of pre-close runway to engage. Close = integration pain + new sponsor's value-creation plan = roadmap slot available (60-120 days post-close sweet spot). Stack auto-elevates if both events fire on same account within 12 months. |
| U3 | New Facility / Market / Site Launch | Every new location = fresh connectivity project. Hits Colo, Fiber, NeoCloud hardest. |
| U4 | Earnings / 10-Q / 8-K Language Shift | CEO/CFO mentioning "provisioning," "NaaS," "automation," "private fabric," "wholesale" = initiative already funded internally. |
| U5 | Conference Speaking Slot | Exec publicly framing a narrative will take pre-event meetings to pressure-test it. 3-5x response vs. cold. ⚠️ Context only when alone; see noise list. |
| U6 | Public Outage / RCA / Status-Page Incident | Pain just became visible. Reach in 7-14 days while memory is fresh. ⚠️ Neocloud-specific demotion: status page incidents are context-only (see `neocloud-signals.md` N-C3). |

## Apollo Signal Class (AP-series)

Apollo-native signals documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Scoring mapping:

| Apollo Signal | Default Tier | Standalone OK? |
|---|---|---|
| AP-1 Job Change to Target Persona (<90d) | A | ✅ Yes |
| AP-2 Competitor / Adjacent Employer Lateral | A | ✅ Yes |
| AP-3 Apollo Scoops / News Feed | B | ✅ Yes (but overlaps RSS) |
| AP-4 Department Headcount Growth (≥15%) | B | ⚠️ Pair required |
| AP-5 Technographic Change | C | ❌ Noise alone |
| AP-6 Apollo Intent (Bombora) | B paired / C alone | ❌ **Never standalone** (>50% false-positive) |
| AP-7 Funding / M&A Filter | A | ✅ Yes (overlaps U2 / U4 with richer metadata) |
| FR-1 SEC 8-K material filings | A | ✅ Yes |
| FR-2 Conference Speaking Slot | C | ❌ Weak alone |
| FR-3 Website Visitor Tracking | A (when live) | ✅ Yes (availability flag) |

## Noise List (explicitly demoted)

Signals that cannot surface an account on their own as of the April 2026 refresh. Each may add color to an existing qualified signal but never triggers alone:

- **AP-5 Apollo Technographic Change alone**
- **AP-6 Apollo Intent without pairing**
- **Apollo keyword drift / description changes** (quarterly; TAM context, not deal trigger)
- **Generic total-headcount growth** (function-specific is stronger)
- **FR-2 / U5 Conference Speaking Slot alone**
- **Status page incidents** (reactive; neocloud-specific demotion)
- **Uptime Tier Certification** (trailing 12-18 months behind design + build)
- **Generic press releases** without tenant / build / capital specifics

---

## Scoring Model

Every detected signal gets scored. The score drives rep-facing priority.

```
Meeting Probability Score = Tier × Freshness × Confidence

Tier:        A = 3, B = 2, C = 1
Freshness:   ≤60d = 3, 60-90d = 2, 90-180d = 1, >180d = drop  (Tier A signals)
             1wk = 3, 30d = 2, 90d = 1                          (Tier B signals)
Confidence:  High = 3, Med = 2, Low = 1

Score Ranges (Phase 3, 2026-05-04):
  27+   → HIGHEST PRIORITY cascade tier (red), same-day attention
  18-26 → STRONG SIGNALS cascade tier (orange)
  12-17 → WORTH REVIEWING cascade tier (yellow)
  8-11  → LIGHT SIGNALS cascade tier (green) - surfaced in rep DM, exploratory
  <8    → Dropped entirely (no CRM write either)
```

**Tier A freshness window updated 2026-04-27 per Cooper:** announcements within the past 60 days score at full freshness for Tier A signals. The previous steep decay (1wk=3 / 30d=2 / 90d=1) over-penalized signals that the catalogs themselves describe as actionable for 60-90+ days - exec hires have 90-day mandate windows, M&A has 60-120 day post-close integration, BEAD awards have 18-24 month provisioning ramps, CTrO appointments have 12-18 month platformization mandates. A 50-day-old M&A on a HIGH-confidence Tier A signal is still a hot trigger; the old model floored it out at score 9. **Extended 2026-06-04:** a 90-180d ×1 band was added (Tier A only) so a HIGH-confidence material event still clears the score-8 floor out to the 180-day `Cool` horizon (Tier A 3 × ×1 × HIGH 3 = 9); the signal-scan **detection window was widened from 14 to 180 days** to match heat relevance - anything that scores ≥8 and computes to Hot/Warm/Cool gets written, and only >180d (Cold-by-recency) is dropped for staleness. MEDIUM-confidence Tier A at 90-180d scores 6 and still drops, so the floor keeps stale noise out.

**M&A two-event firing (added 2026-04-27 per Cooper):** M&A signals fire on TWO distinct events - the announcement (deal signed, not yet closed) AND the close. Each event gets its own ≤60-day Tier A freshness window. The announcement window opens a 6-18 month pre-close engagement runway BEFORE the integration window even starts; we want both. If both events fire on the same account within a 12-month window, apply +6 stacking elevation (the deal proved real and we're tracking it through the lifecycle). SEC filing types tell you which event: 8-K Item 1.01 / S-4 = announcement; 8-K Item 2.01 = close.

**Tier B freshness keeps the steeper decay** because Tier B signals are by-definition "30-90d window" already - they're scraped exactly because they're slightly older / more directional. Decaying them further within that window keeps the relevance gradient.

**Minimum score floor: 8 (Phase 3, lowered 2026-05-04).** Score 12+ → Primary cascade tier (Highest / Strong / Worth Reviewing). Score 8-11 → LIGHT cascade tier (surfaced in rep DM with `:large_green_circle: LIGHT` heading and green Score-column color band). Below 8 = silent drop. CRM `recent_news_or_trigger_event` (narrative) + `last_signal_date` (event date) writes happen for every score ≥8.

## Signal Heat — Rep-Facing Rollup

`signal_heat` is the 4-bucket rollup of the scoring framework that reps sort by daily. Where the score (`last_signal_score`) is a continuous number used for cascade thresholds and analytical work, heat is the discrete bucket reps actually live in. **HubSpot enum values are Title Case** (verified via MCP 2026-05-28): `Hot` / `Warm` / `Cool` / `Cold`. **Freshness anchor:** `last_signal_date`, whose semantics were narrowed to **event date** (when the news/funding/hire happened) on 2026-05-28 — previously it stored detection date.

| Bucket | Definition (top-down, first match wins) |
|---|---|
| `Hot` | `last_signal_score >= 45` with `last_signal_date` (event) in last 60d, OR `signal_count_last_30d >= 2`, OR any open deal past `appointmentscheduled` |
| `Warm` | `last_signal_score` 27-44 with `last_signal_date` (event) in last 60d |
| `Cool` | Any `last_signal_date` (event) in last 180d, not already Hot/Warm (catches sub-27 scores and events 60-180d old) |
| `Cold` | `last_signal_date > 180d` OR null |

**Math + override behavior lives in `context/account-tiering/tier-compute-spec.md` §11.5.** Heat is computed alongside `account_tier` in every routine that touches signal fields (Stage 5b, R-Tier-Audit, R1 Path α, R2 RE_ENRICH_FULL, R6 Step 5.5, R0 MATCH) and in the 5 outreach skill push-backs (cold-email, linkedin-outreach, account-brief, prospect-research, sdr-pipeline — `call-prep` excluded).

**The raw score views still exist for analytical work** - "show me everything scoring 8+ in last 30d," "trend signal volume by segment quarter-over-quarter," cascade-tier banding in the rep Excel. Heat is for daily prioritization; it does not replace the score.

**`hs_is_target_account` does NOT freeze `signal_heat`.** Reps may pin a strategic account at Tier 1 indefinitely, but heat will still go Cold if the event date crosses the 180d boundary - that's the design. Heat tells the truth about intent regardless of strategic-pin status.

### Stacking Rule

Any account hitting **2+ signals in the same 30-day window, where at least one individual signal scores ≥ 8**, auto-elevates to a score of 18+. This catches the highest-intent compound events (e.g., VP Network hire + liquid cooling deploy = strong buy window) while preventing weak-signal stacking - two Tier-C low-confidence hits should NOT produce a top-list promotion. The ≥8 floor means at least one of the stacked signals must be at least (Tier B × 30d × Med) or stronger.

### Greenfield + Site Transition Bonus (Colo + NeoCloud only)

Accounts transitioning **1 → 2 sites** receive a +6 score bonus (captures first-ever multi-site design moment). Accounts with any greenfield signal in stages S2-S3 (permit / utility interconnection filed) receive a +3 score bonus. See per-segment catalogs for full greenfield stage definitions.

**Facility count source:** Parse from the existing free-text `infrastructure_profile` HubSpot field. The skill performs an LLM-based parse at match time to extract a best-effort integer count (e.g., "3 facilities in NoVA + 1 in Dallas" → 4). If the count cannot be parsed confidently (free text is vague or absent), no transition bonus is applied - the skill falls back to the base greenfield score. When the skill detects a facility transition and the parse is confident, it writes the updated count and context back into `infrastructure_profile` (same field, rewritten) so the next run has fresh state. No dedicated integer field is needed.

---

## Source Reliability + Validation Framework

**Purpose:** define how the routine knows a signal hit is real, what confidence level to assign, and which sources can stand alone vs which require cross-source confirmation. This addresses Cooper's 2026-04-27 directive: broaden source coverage AND make signals as accurate and reliable as possible.

### Source reliability tiers

Every source in every segment catalog is tagged with one of three reliability tiers. The tier governs (a) how the routine treats a single hit, (b) whether cross-source confirmation is required, and (c) what confidence to assign.

| Tier | Definition | Confidence on single hit | Cross-source required? |
|---|---|---|---|
| **Robust** | Authoritative, structured, widely-distributed, low false-positive rate. SEC EDGAR filings, PeeringDB, GitHub commits, major trade press (Fierce Network, Light Reading, DCD, TechCrunch), Apollo MCP, LinkedIn public posts, Greenhouse/Lever/Ashby job feeds. | HIGH | No - single source can score |
| **Medium** | Reliable but yields vary. Conference agendas, earnings transcripts (Seeking Alpha tier), TM Forum/Catalyst press, ScanSource/TD SYNNEX investor pages, Crunchbase News (free tier), niche trade press. | MEDIUM (single hit) → HIGH (with cross-source confirm) | Confirmation preferred for major M&A or anchor-tenant claims |
| **Aspirational** | Documented but coverage thin or unstable. State BEAD portals (50 different sites), city planning dockets, electric utility queues (PDF/captcha), per-NeoCloud blog feeds, TheOrg diffs, individual TSD press pages. | LOW (single hit) → MEDIUM (with cross-source confirm from Robust) | YES - never score Aspirational alone for major signals |

The reliability tier of each documented source is now noted in each segment catalog's "Sources for This Segment" section.

### Cross-source confirmation rules (anti-false-positive)

For HIGH-stakes signals, the routine MUST require at least 2 independent sources confirming the same event before scoring at HIGH confidence:

| Signal type | Minimum confirmation |
|---|---|
| **M&A / divestiture announcement** | SEC 8-K Item 1.01 (or S-4) + trade press OR 2 independent trade press from different publishers |
| **M&A / divestiture close** | SEC 8-K Item 2.01 + trade press OR 2 independent trade press |
| **Anchor tenant signing** | SEC 8-K Item 1.01 + tenant's own announcement OR 2 trade press with named counterparty (no "unnamed tenant" filings) |
| **Greenfield S2/S3 (permit + utility)** | Planning docket filing + utility queue filing OR planning + trade press |
| **BEAD subgrant award** | NTIA portal entry + state broadband office press (single trade press alone is MEDIUM not HIGH) |
| **Exec hire (Tier A persona)** | LinkedIn profile change + (PR Newswire / SEC 8-K Item 5.02 / company IR press) - Apollo or LinkedIn alone is MEDIUM not HIGH |
| **GPU-backed debt / colo lease** | SEC 8-K (Item 2.03 / 1.01) + trade press OR rating agency note (Moody's / KBRA / Fitch) + trade press |

When only one source fires, score at MEDIUM and surface as a Watch List candidate; the rep DM still gets the account if score clears 12, but the Slack DM line includes "single-source pending second confirmation." If a second confirmation lands within 2 weeks, upgrade to HIGH and re-score.

### Confidence assignment rules

The routine writes one of four confidence values per signal hit:

| Confidence | When to assign |
|---|---|
| **HIGH** | Cross-source confirmation rule satisfied (per table above) OR single Robust-tier source for non-major signals |
| **MEDIUM** | Single Robust source on a major signal type that requires cross-source confirmation, OR single Medium-tier source on any signal type, OR Aspirational-tier source confirmed by a Medium or Robust source |
| **LOW** | Single Aspirational-tier source on any signal type, OR conflicting details across sources (e.g., date discrepancy, party name discrepancy), OR signal applies to ambiguous company (multiple HubSpot records could match) |
| **MANUAL_REVIEW** | First-time source the routine hasn't validated yet (new source addition; surface to Cooper for first 4 weeks of yields), OR the company identification is uncertain even after Apollo enrichment |

### False-positive patterns (drop or downgrade)

Common false positives that should NOT score at face value - codified here so the routine knows to apply them every run:

| Pattern | Action |
|---|---|
| Press release announcing "AI Practice" / "AI Solutions" launch from an IT MSP (helpdesk + cybersecurity) | EXCLUDE - fails the IT MSP Test (`context/segments/msp-aggregator.md`) |
| Apollo job change with no LinkedIn profile confirming the move | DOWNGRADE to MEDIUM - Apollo lag-data has departure-date ambiguity |
| "Data center" appearing in a name where the entity is actually a real estate brokerage (e.g., "Data Center Realty") | EXCLUDE - apply Routine 0 import-validator entity check |
| GitHub commits from a `@gmail.com` / personal email even if the username matches a carrier employee | DOWNGRADE to MEDIUM - corporate-domain author is the only HIGH-confidence signal for company-attributable code |
| "Liquid cooling" mentioned in a marketing blog with no facility named | EXCLUDE - must be tied to a specific facility filing or trade press confirmation |
| "BEAD award" where the recipient is a sub-contractor (build crew / install firm), not the operator | EXCLUDE - apply contractor/operator filter from `context/core/segment-qualification.md` |
| "Anchor tenant" filing where the tenant is a shell company or unnamed | DOWNGRADE to MEDIUM unless the counterparty can be inferred from reporting context |
| "Funding round" announcement that's a Series Seed at a stealth NeoCloud (< 50 employees) | DOWNGRADE to MEDIUM and route to Watch List - too early for MaiaEdge engagement |
| Earnings transcript mention of "NaaS" / "API" / "private fabric" without operational confirmation | DOWNGRADE to MEDIUM - strategic narrative without a product is a watch signal, not a buying signal |
| Conference speaking slot alone (no other signal) | EXCLUDE per `signal-framework.md` Noise List - context only, never standalone |

### Validation patterns by signal type (in segment catalogs)

Each Tier A signal in each segment catalog now has an explicit "Validation pattern" line that says: "this signal scores at HIGH only when [validation rule]; otherwise score at MEDIUM with single-source flag."

The catalog updates land alongside expanded source lists per the 2026-04-27 broadening + reliability initiative.

### New-source onboarding workflow

When a new source is added to any segment catalog:

1. **First 4 weeks: MANUAL_REVIEW confidence on every hit.** Cooper validates each match against the underlying source manually.
2. **Weeks 5-8: LOW confidence** if false-positive rate < 20% in weeks 1-4; MEDIUM if < 10%.
3. **After 8 weeks: graduate to Medium-tier** if validation has been clean. Promote to Robust only after 12+ weeks AND demonstrating consistent yield + < 5% false-positive rate.

Track the validation pipeline per-source in Cooper's run report under "Source Coverage - New Sources In Validation."

### Repeated-failure auto-flag (link to Source Coverage Mandate)

If a source returns ✗ ERROR for 3+ consecutive runs, OR returns 0 hits for 8+ consecutive runs (when other sources in the same segment yielded), the routine auto-flags it in Cooper's run report under "Sources Needing Development":

- 3-week ERROR streak: source likely dead/changed/auth-walled. Cooper investigates whether to replace or repair.
- 8-week 0-hit streak: source likely doesn't actually publish the signal type we attached it to. Cooper investigates whether the source has the wrong segment tag, the wrong signal pattern, or genuinely doesn't carry the content type.

This is how the Source Coverage Mandate translates into source-development action over 4-12 weeks of run data.

---

## Scrape Source Stack

Organized by cost tier and cadence.

### Free + High-Signal (scrape weekly - priority build)

| Source | Covers | Detection Type |
|---|---|---|
| Data Center Frontier RSS | Colo, NeoCloud | Keyword feeds on Site Selection, Energy, Colocation, Edge tags |
| Data Center Dynamics RSS | Colo, NeoCloud, Network Op | Company-tag + keyword feeds |
| Fierce Network / Fierce Telecom | Fiber, Network Op, MSP | M&A tracker, hiring roundups, carrier-agreement tags |
| Light Reading | Fiber, Network Op | Optical upgrades, NaaS launches |
| Lightwave Online | Fiber | AI-DC dark fiber, 400G/800G |
| Telecompetitor | Fiber | Regional operator news |
| Channel Futures | MSP | M&A, hirings, line-card changes |
| ChannelE2E | MSP | TSD / aggregator news |
| SEC EDGAR full-text | All (public cos) | 8-Ks, 10-Qs, material contracts |
| PR Newswire / Business Wire | All | Filter to company tags + keywords |
| SubmarineNetworks / TeleGeography | Fiber, Network Op | Subsea landings |
| FCC EDOCS / ECFS | Fiber | Pole attachment, tariff filings |
| State PUC dockets | Fiber | CLEC certifications, multi-state expansion |
| NTIA BEAD Progress Dashboard | Fiber | Subgrant awards |
| MLCommons MLPerf Inference | NeoCloud | First-time or new-workload submissions |
| NVIDIA Newsroom | NeoCloud | NCP / DGX Cloud Lepton / Exemplar Cloud partner news |
| FedRAMP Marketplace | MSP | New authorizations |
| FCC Daily Digest | Fiber, MSP | Copper retirement, STIR/SHAKEN mandates |

### Paid (optional - flag before building)

| Source | Covers | Why Paid Matters |
|---|---|---|
| Seeking Alpha Premium | All - Universal Signal U4 | Full earnings transcripts. Free tier gives headlines only. |
| PitchBook / Tracxn | All - Universal Signal U2 | PE roll-up tracking. Fierce/Channel Futures M&A trackers cover most, but Tracxn gives acquirer-level view (e.g., Upstack 30+ acquisitions). |

### Exec Hire Detection Without Sales Navigator

LinkedIn Sales Navigator is intentionally NOT in the source stack. The following free substitutes cover exec-hire signals (Universal Signal U1 + per-segment equivalents) at ~85-90% of Sales Nav's coverage:

| Source | What It Catches | Cadence |
|---|---|---|
| **SEC 8-K Item 5.02** | Officer departures/appointments at ALL US public companies | Immediate (EDGAR daily) |
| **PR Newswire / Business Wire - "Appointments" / "People on the Move" tags** | Executive hires at mid/large public + private cos who pay for PR | Daily RSS |
| **Fierce Network / Fierce Telecom "People" column** | Fiber, Network Op, MSP exec moves | Weekly roundup |
| **Channel Futures weekly hiring/layoff roundup** | TSD / aggregator exec moves ("Ribbon Layoffs, Telarus Hirings" format) | Weekly |
| **Light Reading "People" column** | Network Op, Fiber, carrier moves | Weekly |
| **TelecomTV + Capacity Media "Executive moves"** | International Network Op moves | Weekly |
| **Data Center Dynamics "Careers" tag + DCF "People"** | Colo, NeoCloud exec moves | Weekly |
| **Company IR newsrooms (bulk RSS)** | Self-announced leadership changes (scraped from target company list) | Daily |
| **Crunchbase News - "Executive Moves" tag** | Startup / NeoCloud VP+ hires | Daily RSS |
| **TheOrg.com (free tier)** | Diff of target company org structures week-over-week | Weekly |
| **Apollo job-change detection** | Already wired via CRM Guardian Job 6 (quarterly) - can be tightened to monthly for Tier 1 accounts if needed | Quarterly default |
| **Company careers-page / LinkedIn public Jobs + Indeed + Greenhouse + Lever** | Hiring spikes (3+ concurrent network reqs = signal) - public job posts don't require Sales Nav | Weekly diff |

**Implementation note:** The weekly-signal-scan skill maintains a target-company list (~700-1,000 accounts across all 6 segments - sourced from HubSpot Tier 1+2+3 ICP accounts after the Phase 2 expansion 2026-04-27 + Enterprise added 2026-05-11). Each run cross-references every exec-hire detection against this list. Matches fire signals; misses are ignored. This is the Sales Nav "saved search" equivalent, executed via free sources.

### International Source Stack (Tim Ziemer's territory)

The US-heavy source stack above is supplemented with the following for international coverage parity. Tim Ziemer's territory (non-US) triggers these sources in addition to the global ones (SEC EDGAR is US-only; DCD / TelecomTV / Capacity Media / TeleGeography are global).

**Top 8 international sources (build priority - highest meeting-probability yield per hour of scrape):**

| # | Source | Covers | Why Priority |
|---|---|---|---|
| 1 | **DCD regional tags** (EMEA / Asia-Pacific / LATAM) | Colo, NeoCloud, Network Op all regions | Already in stack; regional filtering turns it global |
| 2 | **Capacity Media** (capacitymedia.com) | Network Op, Fiber, subsea global | Wholesale carrier paper of record globally. Elevate to primary. |
| 3 | **TelecomTV** (telecomtv.com) | Network Op, NaaS/DSP launches | Strong exec-move column + Tier-1 carrier strategy |
| 4 | **ENTSO-E Transparency Platform** + national TSO queues (TenneT NL/DE, National Grid ESO UK, RTE FR, Red Eléctrica ES, Terna IT, 50Hertz, Amprion) | EMEA Colo + NeoCloud greenfield | European PJM/ERCOT equivalent. Free, API-accessible. |
| 5 | **AEMO Connections Scorecard** (Australia) | AU Colo + NeoCloud greenfield | 100-600MW DC load enquiries surface here before trade press |
| 6 | **TeleGeography Submarine Cable Map - RFS feed** | Fiber, Network Op subsea | Definitive subsea RFS tracker |
| 7 | **BNamericas - LatAm Datacenters Watch** | LATAM Colo, Fiber, Network Op | Only non-paywalled LATAM-wide source. Headlines free, depth paid. |
| 8 | **CEF Digital awards + Digital Decade tracker** (digital-strategy.ec.europa.eu) | EMEA Fiber | EU's BEAD equivalent. Awarded projects = fresh fiber buildout. |

**Per-region secondary sources:**

**EMEA**
- Trade press: Data Centre Review, Computer Weekly data-centre tag, Broadband TV News, Total Telecom, Telecompaper, Fibre Provider (UK)
- Regulators: Ofcom UK, BNetzA Germany, ARCEP France, AGCOM Italy, CNMC Spain, ACM Netherlands
- Permits/planning: UK Planning Inspectorate portal, Dutch RVO permits, Irish An Bord Pleanála
- Funding signals: UK Project Gigabit contract awards, EuroHPC JU AI Factory awards (13 awarded to date), IPCEI Next-Gen Cloud, Gaia-X Federation releases, EURO-3C project updates
- Startup/funding: Sifted (EU AI), Crunchbase EMEA tag
- Analyst reports (free tier): EUDCA releases, CBRE EMEA DC Outlook (semi-annual), Cushman & Wakefield EMEA DC Update

**APAC**
- Trade press: DataCenterNews Asia Pacific, W.Media (strong Indonesia/Vietnam/India scoops), Capacity Asia, TelecomAsia.net, DealStreetAsia, Light Reading Asia, Data Center Magazine APAC, Structure Research APAC
- Regulators: IMDA Singapore, MIC Japan, MCMC Malaysia, TRAI India, ACMA Australia
- Grid: AEMO (AU), OCCTO Japan, KPX Korea, EMA Singapore, TEPCO regional feeders
- Sovereign AI: IndiaAI program releases, Japan IOWN Global Forum (NTT), METI Japan AI cloud grants, MeitY India press, Singapore AI Strategy 2.0, KISA Korea, NSTDA Thailand, NVIDIA APAC newsroom
- Broadband: Australian NBN quarterly updates, Japan MIC gigabit coverage, Indonesia Palapa Ring

**LATAM**
- Trade press: BNamericas (headlines free, depth paywalled - scrape headlines for detection), TeleSemana (Spanish, MX/Andean), DCD LATAM, Teletime (BR), Convergencia (AR), Data Center Magazine LATAM
- Regulators: Anatel Brazil, IFT Mexico, Subtel Chile, ENACOM Argentina
- Grid: ONS Brazil, CFE Mexico, CEN Chile, CAMMESA Argentina

**MENA**
- Trade press: Capacity MENA, Commsmea, Zawya (free wire - Saudi/UAE corporate announcements), AGBI (Gulf business intelligence), Intelligent CIO Middle East, Khaleej Times tech
- Regulators: TDRA UAE, CST Saudi, CRA Qatar, TRA Bahrain
- Sovereign AI: HUMAIN press (KSA), G42 press (UAE), MGX fund, SDAIA releases. Often surface on Zawya / AGBI within hours.
- Grid (utility IR only - limited free): DEWA Dubai, SEC Saudi, ADWEA Abu Dhabi, KAHRAMAA Qatar

---

### New Signal Classes - International (I-series)

These are distinct from the per-segment A/B/C tiering because they fire across multiple segments and have a direct US analogue (BEAD for fiber, FedRAMP for MSP, etc.).

**I1. International State-Aid / Sovereign Funding Award**
- *What:* Government subsidy or concession award for fiber buildout, data center, or network infrastructure. Awards publish beneficiary + scope months before actual buildout.
- *Why it predicts a meeting:* Same pattern as BEAD - winners have binding obligations. 6-18 month build window = same outreach timing.
- *Sources:* EU competition-cases state-aid register (competition-cases.ec.europa.eu), UK Project Gigabit awards, EU CEF Digital awards, Australia NBN tenders, Japan MIC fiber subsidies
- *Scoring:* Tier A base + **+3 bonus (greenfield-equivalent)**. Typical score: 3 × 3 (1wk) × 3 (High) + 3 = **30**
- *Freshness:* 1wk (announcement).

**I2. Sovereign AI Grant / Compute Allocation**
- *What:* Government-funded AI compute allocation or Sovereign AI program win (not hyperscaler-adjacent).
- *Why it predicts a meeting:* Recipient is about to scale GPU deployment with hard SLA + in-country transit rules - exactly the pain MaiaEdge solves.
- *Sources:* EuroHPC JU AI Factory awards, IndiaAI GPU allocation rounds (MeitY), Japan METI AI cloud subsidy awards, Singapore AI Strategy 2.0, HUMAIN/G42/MGX deal announcements, Bpifrance France 2030 AI compute grants
- *Scoring:* Tier A base + **+3 bonus**. Typical score: 30.
- *Freshness:* 30d (award to announcement window).

Both I-series signals apply across Colo, Fiber, Network Op, NeoCloud segments where relevant.

---

### Conference Agenda Scrapers (custom per event)

| Event | Cadence | Segments |
|---|---|---|
| PTC | January | Colo, Fiber, Network Op |
| DCD Connect (NY, Virginia, London, Singapore) | Year-round | Colo, NeoCloud |
| Datacloud USA / Global | Spring | Colo, NeoCloud |
| Fiber Connect | Summer | Fiber |
| ISE Expo | Fall | Fiber |
| ITW / Capacity | Spring | Network Op |
| Channel Partners Conference + MSP Summit | Spring | MSP |
| AI Infrastructure Summit | Fall | NeoCloud, Colo (AI Signals) |
| NVIDIA GTC | March | NeoCloud |
| DCD Connect Singapore / Sydney / Bangkok | Year-round | APAC Colo, NeoCloud |
| Asia Tech Singapore / CommunicAsia | Spring | APAC all |
| India Mobile Congress | Fall | APAC Network Op, NeoCloud |
| Datacloud Asia | Spring | APAC Colo |
| Capacity Asia / Capacity LATAM / Capacity Europe / Capacity Middle East | Year-round (regional) | Network Op, Fiber, MSP |
| Futurecom Brazil | Fall | LATAM Fiber, Network Op |
| LEAP (Riyadh) / GITEX Global (Dubai) | Spring / Fall | MENA all + sovereign AI |
| MWC Barcelona / MWC Shanghai | Winter / Summer | Global Network Op |
| Mobile World Congress Shanghai | Summer | APAC Network Op |

---

## Run Cadence

**Weekly, Mondays 7:00 AM Eastern.** Execution begins Sunday 11 PM ET to complete before delivery.

### Sequence

```
Sun 23:00 ET  → Scrape all sources (signals since previous Sunday)
Sun 23:45 ET  → Match detected companies to HubSpot by domain
Mon 00:30 ET  → Enrich unknown companies (company-enrichment skill)
Mon 01:30 ET  → Run matched/new accounts through crm-guardian (territory, owner, tier assignment)
Mon 02:30 ET  → Update recent_news_or_trigger_event narrative (pure prose, no date prefix) AND last_signal_date (event date) on all hit accounts
Mon 03:30 ET  → Generate 3 territory-split email reports (Tim L, Ken, Tim Z)
Mon 07:00 ET  → Deliver emails with Excel attachment
```

---

## HubSpot Field Update Spec

### `recent_news_or_trigger_event` (narrative, 250 char max) + `last_signal_date` (structured event date)

**Format (post-2026-05-28):** narrative + structured event date pair, no date prefix in the narrative string.

- `recent_news_or_trigger_event` (text, 250 char max): **pure narrative**, no date prefix. E.g. `"VP Network Hire - Lambda named Sarah Chen VP Network Eng (ex-AWS); build-vs-buy fabric decision window open"`.
- `last_signal_date` (Date, YYYY-MM-DD): the date the event actually happened. E.g. `2026-04-18`. Semantics narrowed 2026-05-28 from "detection date" → "event date." Enables HubSpot sort/filter by event recency without parsing strings, and drives the `compute_tier` + `compute_signal_heat` freshness modifiers.

**Rules:**
- If multiple signals hit the same account in one week, keep the **highest-scored** one in both fields.
- The narrative and the date are written **together** — never one without the other.
- Stack additional signals in `account_brief` (400 char) as a short "Also this week: ..." line.
- Never exceed 250 char on the narrative - the field is a HubSpot hard cap.
- No em dashes. Use hyphens or restructure.
- No competitor names (per repo feedback rules - use "third-party fabrics" instead).
- **Legacy `[YYYY-MM-DD] [Signal Type] - one-liner` prefix format is retired.** The one-time backfill task parses existing prefixes into `last_signal_date` for records pre-dating this change.

### `last_enriched_date`

Set to run date for any account touched (new enrichment OR field update). Keeps the CRM Guardian 120-day re-enrichment cadence in sync.

### New accounts (domain not in HubSpot at match time)

1. Run `company-enrichment` skill → segment, tier, state, account brief
2. Run `crm-guardian` safety tiers → territory assignment via territory-manager, owner ID, quality gates
3. Create account in HubSpot with `recent_news_or_trigger_event` populated
4. Flag in the new-accounts section of that week's rep report

---

## Territory Routing

| Owner ID | Rep | Territory |
|---|---|---|
| 161889085 | Tim Lieto | East (30 states) |
| 162339176 | Ken Cunningham | West (20 states + DC) |
| 159350430 | Tim Ziemer | International |

Filter the rep-facing prospecting list by `hubspot_owner_id`. New accounts added via enrichment get owner assigned before hitting the report.

Full state mapping lives in `context/hubspot/territory-model.md` - never hardcode state lists in the signal skill.

---

## Output Specification

### Email (one per rep per week)

**Subject:** `Weekly Signal Scan - [Rep First Name] - Week of [YYYY-MM-DD]`

**Body (written for reps, tactical tone):**

```
PART 1 - Segment Briefing

[One paragraph per segment IN REP'S TERRITORY]

Each paragraph covers:
- Headline theme of the week (1 sentence)
- Top 3 signal events in-segment (1 sentence each, named accounts)
- Emerging pattern or watchout (1 sentence)

Tone: strategic briefing, not data dump. Think field commander update.

PART 2 - Where to Prospect This Week

"If you only call 5 accounts this week, these are the 5:"
- Top 5 accounts overall by Meeting Probability Score, regardless of segment
- One line per account: name (segment) + signal summary + why now

PART 3 - New Accounts Added This Week

"N new accounts were found via signal scan, enriched, and added to your territory:
- [Account name] ([segment]) - [reason added]
- ..."
```

### Excel Attachment

**File naming:** `weekly-signal-scan-[rep-last-name]-[YYYY-MM-DD].xlsx`

**Tabs:** One tab per segment in the rep's territory (max 5 tabs: Colocation, Fiber, Network Operator, NeoCloud, MSP-Aggregator). Accounts in segments with zero hits that week get no tab.

**Cap:** 50 accounts TOTAL per rep (distributed across segment tabs by Meeting Probability Score). Ranking is global across segments - a rep could get 22 Colo + 15 NeoCloud + 8 Fiber + 5 Network Op in one week, and a different mix the next. Segment tabs are for organization, not quotas. Overflow (score 12+ but below the top 50) moves to silent nurture and does not appear in the report.

**Columns (every tab):**

| Column | Source |
|---|---|
| Account Name | HubSpot `name` |
| Customer Segment | HubSpot `customer_segment` |
| Sub-Segment | HubSpot `company_sub_segment` |
| Account Tier | HubSpot `account_tier` (inverted - Tier 1 = highest) |
| Account Owner | `hubspot_owner_id` resolved to name |
| HubSpot URL | `https://app.hubspot.com/contacts/[hub_id]/company/[record_id]` |
| LinkedIn URL | HubSpot `linkedin_company_page` field. If blank, fall back to Apollo `linkedin_url` from organization enrichment. If still missing, leave blank (don't guess or construct a URL). |
| Signal Type | Universal signal class or segment-specific signal name |
| Signal Body | 3-5 sentence synthesis: what happened, when, the specific pain it exposes for this prospect, quoted context from the source + source URL. Reads like a mini call-prep, not a headline. |
| Detection Date | YYYY-MM-DD |
| Meeting Probability Score | Tier × Freshness × Confidence (+ stacking / greenfield bonuses) |
| Account Brief | HubSpot `account_brief` (regenerated fresh if >30 days stale) |
| State | HubSpot `state` |
| Suggested Angle | Persona-aware and signal-specific. Names the right persona to reach (e.g., "reach the new VP Network in week 3-6 referencing her fabric mandate") and the specific angle from the signal (e.g., "GPU tenant anchor - reach platform owner before fabric decision is locked"). References `cold-email` skill for voice, but the angle is derived from the signal type + account context. |

---

## Integration with Existing Skills

| Skill | How It's Used |
|---|---|
| `company-enrichment` | New accounts (signal hit, not in HubSpot) → full enrichment pipeline |
| `crm-guardian` | Safety tiers for new-account writes; territory routing; owner assignment |
| `territory-manager` | State → owner mapping for new accounts |
| `account-sourcing` | Falls back to this for unknown-company signals that don't resolve to a clear segment |
| `account-brief` | Regenerates stale briefs (>30 days) before they hit the rep report |
| `cold-email` | Referenced in the "Suggested Angle" column  |

---

## Scope Guardrails

- **Target 25-50 accounts per rep per week, hard cap 50** (not per segment). Ranked globally across the rep's territory by Meeting Probability Score. Phase 3 fill-down keeps the list at 25+ even on quiet weeks: Primary (≥12) → LIGHT (8-11) → Carryover News (open-lane, prior-week news still valid + no rep activity ≤14d). Carryover never fires when Primary + LIGHT ≥25.
- **Score floor of 8.** Below 8 = dropped, not "nurture-listed" in the report. Keeps every row meaningful.
- **Depth-over-breadth.** Every row should read like a mini call-prep: 3-5 sentence signal synthesis, persona-aware angle, fresh account brief. The compute budget saved by capping at 50 funds this depth.
- **Territory purity.** Reps see only their territory. Never cross-share unless Tim Z explicitly wants global view.
- **Written-for-reps tone.** Tactical, not strategic. Reps are being told what to do, not what to think about.
- **No competitor naming in field writes** (per repo feedback rule).
- **No em dashes in any HubSpot field write** (per repo convention).
