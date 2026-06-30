# Network Operator - Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` and `segments/network-operator.md`.

HubSpot `customer_segment` internal value: `Network Operator(Tier 1 / VNO)` (NO space before paren; display label is "Network Operator").
Sub-segments (5 active, post-Phase 1.6 2026-05-13 + Phase 3 2026-05-14): **Tier 1 Carrier - Network Op**, **Pure Wholesale Carrier - Network Op**, **Cable MSO Enterprise Division - Network Op**, **International Backbone Specialist - Network Op**, **Subsea cable operator** (NEW 2026-05-14, 30th sub-segment; lowercase, no `- Network Op` suffix). The legacy sub-segment values `External Extension - Network operator` and `Internal + external unification - Network Operator` were archived 2026-05-13 (Phase 1.6) and migrated to the dedicated `network_op_track` field (values: `external_extension` for Track A, `internal_external_unification` for Track B). See `context/account-tiering/sub-segment-qualification.md` for the full 30-value reference.

---

## Tier A - Board-Level Urgency Triggers (weekly)

### N-A1. Private-Connectivity-Fabric Copycat / Multi-Billion AI Deal Announcement

**Why:** After Lumen's ~$13B PCF deals, every Tier 1/2 board is asking "what's our PCF answer?" A rival signing a $Bn AI networking deal forces immediate strategic response. Asset-light partnership angle is the answer.

**Source:** Fierce Network, Light Reading, TelecomTV, press releases from Zayo, Console Connect, Arelion, Colt, GTT, BT, Orange, NTT, Tata, PCCW. SEC 8-Ks for US-listed carriers.

**Pattern:** `("private connectivity fabric"|"AI networking deal"|"AI fabric"|"multi-year connectivity agreement") AND ("$1 billion"|"$2 billion"|"multi-billion"|"hyperscaler")`

**Freshness:** 1wk. **Confidence:** HIGH.

### N-A2. Earnings Transcript Mentions - NaaS / Network APIs / Private Fabric / Programmable

**Why:** If a CEO/CFO mentions these terms on a call, strategy teams are ALREADY being asked to show progress. Outreach within 2 weeks of a call gets read.

**Source:** Seeking Alpha, Motley Fool, company IR, AlphaSense, SEC 10-Q/10-K, investor-day decks.

**Pattern:** Transcript search `"NaaS"`, `"network API"`, `"private fabric"`, `"programmable network"`, `"wholesale automation"`, `"AI connectivity"`, `"cross-carrier"`, `"beyond connectivity"` - rank by frequency AND speaker role (CEO/CTO > CFO).

**Freshness:** 30d (earnings windows). **Confidence:** HIGH.

### N-A3. Executive Transition - CTO / CNO / VP Automation / Chief Network Strategy

**Why:** New network leaders have a 90-day window to propose something new. Actively taking meetings.

**Source:** SEC 8-K Item 5.02 (US-listed carriers), PR Newswire / Business Wire Appointments RSS, Fierce Network People, TelecomTV exec moves, Capacity Media, Light Reading People, carrier IR newsroom RSS, TheOrg diffs. See `signal-framework.md` for full Sales-Nav-free stack.

**Pattern:** Cross-reference each detected exec move against Tier 1/2 carrier target list + title match `(CTO|CNO|"Chief Network"|"VP Automation"|"VP Programmable"|"VP Network Strategy"|"SVP Transport")`.

**Freshness:** 30d post-hire (first week is too early). **Confidence:** HIGH.

### N-A4. Wholesale / Consumer Divestiture or Spin-off - Announcement OR Close (two-event firing added 2026-04-27)

**Why:** Following Lumen playbook - divest consumer, pivot to enterprise/AI. Forces strategic shift AND frees capex. Two distinct windows:
- **At announcement** (intent to divest, not yet closed): 6-18 month pre-close runway. Carrier's strategic shift is now public; the post-divest network architecture is being scoped. This is when MaiaEdge can shape the platform conversation.
- **At close**: Post-divestiture is peak window - strategic shift complete, capex freed, enterprise/AI pivot underway.

If both events fire on same carrier within 18 months → +6 stacking auto-elevation.

**Source:** **SEC 8-K Item 1.01 + S-4 (announcement), SEC 8-K Item 2.01 (close)**, Reuters, Bloomberg, PR Newswire, Fierce M&A tracker, PwC/EY deal trackers.

**Pattern (announcement):** `(carrier|telecom) AND ("announces"|"to divest"|"plans to spin off"|"announces separation"|"intends to sell"|"agreement to carve out") AND ("consumer"|"wholesale"|"wireline"|"ILEC")`

**Pattern (close):** `(carrier|telecom) AND ("completes divestiture"|"closes spin-off"|"divestiture completes"|"separation completes"|"sale closes") AND ("consumer"|"wholesale"|"wireline"|"ILEC")`

**Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH.

### N-A5. GitHub Commits from @carrier.com to CAMARA / Nephio / ONAP / OpenConfig / Sylva

**Why:** Code-level commitment to open standards beats logo participation. When a @carrier.com email address shows up on commits to CAMARA, Nephio, ONAP, OpenConfig, or Sylva, the operator has engineering investment (not just marketing) in programmable / federated infrastructure. High signal that the operator is actively building on standards we align with.

**Source:** GitHub commit search (public), GitHub organization membership for carrier employees, foundation commit leaderboards (LFN, TM Forum Catalyst repos).

**Pattern:** `author-email:*@carrier.com` filtered to target operators + repo path in `(CAMARA|Nephio|ONAP|OpenConfig|Sylva|ODA)`. Weekly diff on committer list.

**Freshness:** 30d. **Confidence:** HIGH.

### N-A6. TM Forum Autonomous Networks Self-Assessment Publication

**Why:** Distinct from the certification signal `N-B3`. The self-assessment is an operator's own public declaration of where they are on the TM Forum AN maturity ladder  -  a leading indicator of where they want to go, not a lagging indicator of what they've already built. Self-assessments signal intent to buy or partner.

**Source:** TM Forum AN registry, TM Forum Inform, DTW Ignite presentations, operator press.

**Pattern:** `("Autonomous Networks self-assessment"|"AN maturity"|"TMF AN framework") + carrier`

**Freshness:** 90d. **Confidence:** HIGH.

### N-A7. SRv6 / Segment-Routing Production Rollout Announcement

**Why:** SRv6 in production = dataplane readiness for programmable path control. The gap between the dataplane (SRv6) and a federation-capable control plane is exactly where MaiaEdge fits. Operators presenting SRv6 in production at NANOG / RIPE / APRICOT or publishing engineering blog posts about SRv6 rollouts are primed for a cross-operator orchestration conversation.

**Source:** NANOG / RIPE / APRICOT conference archives, operator engineering blogs, LinkedIn engineering posts, IETF BGP-LS / SPRING working group participant lists.

**Pattern:** `("SRv6"|"SR-MPLS"|"segment routing"|"flex-algo"|"micro-SID") AND ("production"|"rolled out"|"deployed") + carrier`

**Freshness:** 90d. **Confidence:** HIGH.

### N-A8. Public RFI / RFP - Multi-Domain Orchestrator / TE Controller / Inter-Carrier Automation

**Why:** Most direct buying signal  -  the operator is actively procuring. Public procurement portals (TED in EU, SAM.gov in US, carrier own RFP portals) publish RFIs and RFPs for infrastructure orchestration platforms.

**Source:** TED (EU procurement), SAM.gov (US federal), carrier procurement portals, RFPDB, GovSpend.

**Pattern:** `(RFI|RFP|tender) AND ("multi-domain orchestrator"|"TE controller"|"path computation"|"inter-carrier automation"|"programmable underlay"|"cross-carrier NaaS") + carrier`

**Freshness:** 30d (respond windows are typically 60-90 days). **Confidence:** HIGH.

### N-A9. PCEP / SR-TE / BGP-LS / YANG-NETCONF Job Requisitions

**Why:** Hiring for controller-specific skills = standing up a TE team. 1-2 quarter lead over procurement. Sub-10-employee teams that start hiring for these skills are about to scope a platform.

**Source:** Carrier careers pages, LinkedIn Jobs (target carrier filter), Indeed, Greenhouse / Workday / SmartRecruiters aggregators.

**Pattern:** Job titles / descriptions matching `(PCEP|SR-TE|BGP-LS|YANG|NETCONF|OpenConfig|segment routing engineer|traffic engineering engineer)` at target carrier.

**Freshness:** 30d. **Confidence:** HIGH.

### N-A10. CTrO / CDO Appointment (distinct from CTO/CNO)

**Why:** Chief Transformation Officer or Chief Digital Officer appointments (distinct from CTO / CNO) signal a platformization mandate + consolidated budget authority that the CTO/CNO does not have. 12-18 month charter. Outreach in the first 90 days lands particularly well because the new CTrO / CDO is building the case for their transformation strategy.

**Source:** SEC 8-K Item 5.02 (US-listed), PR Newswire / Business Wire Appointments RSS, LinkedIn.

**Pattern:** `"named"|"appointed"|"joins as" + ("Chief Transformation Officer"|"Chief Digital Officer"|"CTrO"|"CDO"|"Chief Platform Officer") + carrier`

**Freshness:** 90d. **Confidence:** MED-HIGH.

---

## Tier B - Strategic-Posture Signals (weekly)

### N-B1. Tier 1 Supplier Customer Win (Ciena / Nokia / Cisco / Juniper)

Optical/routing wins reveal who's modernizing. Carrier buying WaveLogic 6 / 800G / coherent pluggables is rebuilding east-west capacity - needs a control plane on top.

Source: Ciena newsroom, Nokia press, Cisco Provider news, Juniper press, Light Reading optical, Fierce Network optical, OFC/ECOC coverage.

Pattern: `(Ciena|Nokia|Infinera|Cisco|Juniper) AND (target carrier) AND ("deployed"|"selected"|"1.6T"|"800G"|"coherent")`. Confidence: HIGH.

### N-B2. GSMA Open Gateway / Network API Commercial Launch in New Market

Programmable pivot at mobile layer. Transport/wholesale side needs to catch up - and they know it.

Source: GSMA newsroom, CAMARA project, MWC coverage, Open Gateway blog, operator press.

Pattern: `"Open Gateway" AND ("launch"|"live"|"commercially available") AND ("Number Verification"|"SIM Swap"|"Quality on Demand"|"Device Status")`. Confidence: MED-HIGH.

### N-B3. TM Forum Autonomous Network Level 3 / Level 4 Certification

Public commitment to autonomous networking. Needs cross-domain coverage - the gap MaiaEdge fills.

Source: TM Forum Inform, tmforum.org/news, DTW Ignite announcements, Fierce Network, Ericsson/Huawei/Nokia partner press.

Pattern: `("Autonomous Network Level 4"|"AN Level 4"|"AN L4"|"Level 3 autonomy") AND carrier`. Confidence: HIGH.

### N-B4. Submarine Cable Landing / Consortium Joining + Atlantic Retirement Crunch

New cable = new capacity to monetize = need for programmable activation. The inverse fires too: transatlantic capacity is tightening as ~a third of the Atlantic cables age out by ~2027 (internal trigger: ~7 of 21), which hands transatlantic-anchored operators scarcity-driven pricing power - but ONLY if they can sell that capacity as instantly activatable product. A cable-retirement or Atlantic-crunch story on a transatlantic-anchored target is a monetize trigger, not a threat signal: the angle is "turn scarce capacity into instantly activatable private paths and capture the premium."

Source: SubTel Forum, Submarine Networks, Telegeography, Capacity Media, Fierce Network subsea.

Pattern: `("cable landing"|"RFS"|"ready for service"|"joined consortium"|"subsea cable"|"cable retirement"|"end of life"|"Atlantic capacity"|"capacity crunch") AND carrier`. Confidence: MED.

### N-B5. MEF LSO Sonata / Open API Certification + Mplify AI-Federation Direction

Public commitment to inter-carrier automation standards. LSO Sonata alone doesn't solve same-day provisioning - we're complementary. The standards body itself is now naming the AI-federation endgame: Mplify (ex-MEF) openly describes an "AI federation / AI exchange" future, shipped a Carrier-Ethernet-for-AI certification (Q2 2026), and extended LSO APIs to internet exchanges (June 4, 2026). A carrier certifying against these = primed for the federation conversation. NOTE: the AI-federation framing is RFP / objection-handling proof ("aligned with where the certification bodies are heading"), NOT a cold-outreach claim - in cold, relevance comes from the operator's own problem.

Source: Mplify (formerly MEF) press, MEF registry, GlobeNewswire, Fierce Network.

Pattern: `("MEF 3.0"|"LSO Sonata"|"LSO Cantata"|"Carrier Ethernet for AI"|"AI federation"|"AI exchange"|"LSO"+"internet exchange") AND ("certification"|"certified"|"conformance"|"launch")`. Confidence: MED.

### N-B6. AI-Backbone Dataplane Disaggregation Deployment (DriveNets-class)

A carrier rebuilding its AI backbone on a disaggregated dataplane (DriveNets-class; KDDI / AT&T / Comcast deployments) has the dataplane ready but still lacks a federation-capable control plane across operators it does not own - that cross-carrier layer is exactly where MaiaEdge sits. A disaggregation deployment is a strong "dataplane ready, control plane gap open" trigger, parallel to N-A7 (SRv6 production rollout).

Source: DriveNets press + customer-win releases, carrier engineering blogs, Light Reading / Fierce Network optical + routing, NANOG / OCP coverage, supplier customer-win press.

Pattern: `("DriveNets"|"disaggregated"|"DDC"|"distributed disaggregated chassis"|"network cloud"|"white box backbone") AND ("AI backbone"|"deployed"|"production"|"rolled out") + carrier`. Confidence: MED-HIGH.

---

## Tier C - Context / Timing Signals (bi-weekly)

### N-C1. Private 5G + Network Slicing Enterprise Win

Wireless side demonstrating programmable infrastructure. Transport/wholesale persona under internal pressure to match.

Source: RCR Wireless, Light Reading 5G, Fierce Network wireless, operator press.

Pattern: `("network slicing"|"private 5G") AND ("enterprise"|"customer") AND ("commercial"|"live"|"deployed")`. Confidence: MED.

### N-C2. Sovereign Cloud / Edge Federation Partnership

EU AI Act Aug 2026 + DPDP + US state privacy = regulated customers demanding path sovereignty. Carriers joining federations (Euro Edge Continuum, EURO-3C) need deterministic cross-carrier paths.

Source: Deutsche Telekom / Orange / Telefónica / TIM / Vodafone press, EU Commission press, TelcoTitans, TelecomTV.

Pattern: `("sovereign cloud"|"digital sovereignty"|"Edge Continuum"|"EURO-3C"|"federated edge") AND carrier`. Confidence: MED-HIGH for EU carriers.

### N-C3. Activist Investor / PE Position Disclosure

Forces strategic review. Post-disclosure = 60-90 days of "what's our new story?" panic.

Source: SEC 13D/13G filings (>5% stakes), WSJ Heard on the Street, FT, Reuters activist coverage.

Pattern: 13D on target carrier + news mentions `"strategic review"|"review alternatives"|"activist"|"shareholder letter"`. Confidence: HIGH when hits.

### N-C4. Hyperscaler Carrier Deal (bypass signal)

Hyperscaler picking ONE carrier for a region pressures every other carrier to show AI networking story - or watch traffic bypass them.

Source: Microsoft/Google/AWS/Meta/Oracle press, DCD, Network World, Light Reading, carrier earnings.

Pattern: `(Microsoft|Azure|AWS|Google Cloud|Meta|Oracle) AND (carrier) AND ("fiber"|"capacity"|"connectivity"|"dedicated"|"private"|"multi-year")`. Confidence: HIGH (losers call fastest).

### N-C5. Carrier Layoff / Restructuring (nuanced - classify reason)

MIXED signal. Good: "automation-driven headcount reduction" (Verizon-style tied to automation) = they want MORE programmable infrastructure. Bad: cost-cutting from declining 5G capex (Ericsson-style) without AI pivot = window closed, defer 60d.

Source: Fierce Network layoff tracker, 8-K filings, WARN Act notices (state DoL), Reuters.

Pattern: Layoff mention + cross-reference latest earnings for automation/NaaS mention. Confidence: MED (reason-dependent).

---

## Sources for This Segment (scrape weekly - pruned 2026-05-11)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework.

**Search-anchor pattern is the canonical access method** - direct `web_fetch` is gated by URL-provenance on Cowork's runtime. Anchor each source via `web_search "{domain} {topic} {year}"` and read snippets from search results. Article URLs returned in search can then be fetched directly. Do NOT skip a documented source because direct fetch fails - use search anchoring.

### Robust tier

1. Company IR pages - direct newsroom diffs at target Tier 1/2 carriers (Lumen, AT&T, Verizon, T-Mobile, Charter, Cox, Comcast Business, BT, Vodafone, DT, Orange, Telefónica, NTT, Tata Comms, Singtel, Telstra) - highest single-source yield [Robust]
2. **StockTitan** (SEC 8-K mirror with parsed summaries - `stocktitan.net/sec-filings/{ticker}/`) - primary surrogate for SEC EDGAR direct queries; covers 8-K Items 1.01 / 2.01 / 5.02, 13D/G activist, 10-Q earnings; for international: 20-F annual filings [Robust]
3. SEC EDGAR full-text via search-anchor - backup to StockTitan [Robust]
4. **Earnings transcripts** - Seeking Alpha (free-tier headlines) + Motley Fool + MarketBeat + SEC 10-Q transcripts via StockTitan; keyword-filter for "NaaS" / "API" / "private fabric" / "programmable network" / "SRv6" / "autonomous network" / "MEF" / "TM Forum" (covers NO-A2) [Robust]
5. Fierce Network + Light Reading + TelecomTV + RCR Wireless + Total Telecom - primary US trade press [Robust]
6. Ciena / Nokia / Cisco / Juniper / Arista / Infinera newsrooms - supplier customer-win press often surfaces big carrier deals first [Robust]
7. **MEF / Mplify** (MEF rebranded to Mplify 2025; both names in use) + **TM Forum** newsroom + Catalyst announcements [Robust]
8. **GSMA newsroom** + **CAMARA project** GitHub + GSMA Open Gateway press [Robust]
9. GlobeNewswire + PR Newswire + Business Wire filtered to carrier list + Appointments tag [Robust]
10. Apollo MCP - `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events (covers AP-1 / AP-2 / AP-7) - enrichment tool [Robust]
11. **GitHub commit feeds** for CAMARA / Nephio / ONAP / OpenConfig / Sylva - corporate-domain authors only (covers NO-A5) [Robust - accessed via search anchor since direct GitHub fetches are URL-gated]
12. **FedBizOpps + SAM.gov + state procurement portals** - federal RFI / RFP for multi-domain orchestration / TE controllers / inter-carrier automation (covers NO-A8) [Robust at federal, Tier C reference at state portals]
13. Greenhouse + Lever + Ashby public job boards at target carriers (covers NO-A9 PCEP/SR-TE/BGP-LS/YANG job reqs) [Robust]

### Medium tier (Tier B fallback)

14. Capacity Media - content depth weaker than peer trade press, mostly event marketing; use as international fallback only [Tier B]
15. Mobile World Live + Mobile Network UK - strong on carrier-economic news, weak on infra-buying signals; for Fiber/NetOp segments only [Tier B]
16. **TIA (Telecommunications Industry Association)** + **USTelecom** + **CTIA** press [Medium]
17. **ONUG (Open Networking User Group)** announcements [Medium]
18. **ONF (Open Networking Foundation)** press [Medium]
19. **LFN (Linux Foundation Networking)** member commits + leadership announcements [Medium]
20. **ETSI standards activity** - NFV / MEC / MANO / Open RAN working group output [Medium - leading indicator]
21. **3GPP work item tracker** - release content reveals carrier roadmap commitments [Medium]
22. **IETF working groups** - carrier-participation WGs (PCE, IDR, BESS, SR, OPSAWG) [Medium]

### Excluded (do NOT scrape - cut 2026-05-11)

- Wayback Machine month-over-month diffs - theoretical, never run.
- Reddit r/networking + r/telecom + r/networkengineering - low signal density.
- Glassdoor reviews - login-gated.
- YouTube transcripts from MWC / TM Forum DTW / Network X / ITW - compute-expensive, redundant with trade-press coverage.
- TheOrg.com diffs - Aspirational, never produced a signal.
- Reuters telco feed - UA-blocked + JS rendering breaks search anchor. Use Bloomberg headlines (paywalled but search-snippet-reachable) instead.

LinkedIn public posts retained for **named-account research only** (specific company pages), not market-wide discovery - moved to `signal-framework.md`.

### International (Tim Z's territory - elevated priority here)

Tim Z's territory leans heaviest on this segment (global Tier 1/2 carriers). Elevate Capacity Media + TelecomTV to **primary** trade press (vs. US stack where Fierce / Light Reading lead). See `signal-framework.md` "International Source Stack" for full detail.

- **Global/EMEA:** Capacity Media (PRIMARY) [Robust], TelecomTV (PRIMARY) [Robust], Light Reading Europe [Robust], Total Telecom [Robust], ETNO press (EU-wide positioning) [Medium]. Target operators: Orange Business, BT Global, Colt, Deutsche Telekom International, KPN International, TIM Sparkle, Telia Carrier, Arelion, Liberty Global, Telefónica Tech.
- **APAC:** Capacity Asia [Robust], TelecomAsia.net [Medium]. Target operators: NTT, Tata Communications, PCCW Global, Telstra, Singtel, Axiata, Epsilon, Console Connect.
- **LATAM:** BNamericas [Medium], Capacity LATAM [Medium]. Target operators: Cirion, Telxius (wholesale arms of Telefónica LATAM).
- **MENA:** Capacity MENA [Medium], Commsmea [Medium]. Target operators: e& Carrier Wholesale, Etisalat International.
- **Subsea (global):** TeleGeography Submarine Cable Map RFS feed (PRIMARY) [Robust], SubmarineNetworks.com [Medium].
- **I-series signals (see `signal-framework.md`):** I2 Sovereign AI Compute Grants hit Network Op targets frequently (carriers winning government sovereign-network contracts).

**Quarterly batch:** Earnings transcript sweep across full Tier 1/2 target list - highest-yield recurring task.

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **NO-A1 PCF copycat / multi-billion AI deal** | SEC 8-K Item 1.01 [Robust] + ≥1 trade press [Robust] for the multi-billion deal claim. Copycat patterns require board-level public commitment (earnings transcript or formal announcement), not analyst speculation |
| **NO-A2 earnings transcript NaaS/API mention** | SEC 10-Q transcript [Robust] alone scores HIGH; Seeking Alpha alone → MEDIUM. Quote must include carrier-strategic language (not "we monitor NaaS competitors") |
| **NO-A3 CTO/CNO/VP Automation transition** | LinkedIn profile change [Robust] + (PR Newswire Appointments [Robust] OR SEC 8-K Item 5.02 [Robust] OR carrier IR press) |
| **NO-A4 wholesale/consumer divestiture (announcement OR close)** | SEC 8-K [Robust] (Item 1.01 announcement, Item 2.01 close) + ≥1 trade press OR 2 independent trade press |
| **NO-A5 GitHub commits to programmable-infra repos** | Author email matches `*@<carrier-domain>` [Robust] AND repo path in CAMARA / Nephio / ONAP / OpenConfig / Sylva. Personal-email author → DOWNGRADE to MEDIUM |
| **NO-A6 TM Forum AN self-assessment** | TM Forum press [Medium] confirmed by carrier's own announcement [Robust] |
| **NO-A7 SRv6 production rollout** | Carrier announcement [Robust] + supplier press confirming the deployment (Cisco / Juniper / Nokia customer-win) [Robust] |
| **NO-A8 multi-domain RFP** | FedBizOpps / SAM.gov listing [Robust] OR state procurement portal [Aspirational] + ≥1 trade press [Robust] |
| **NO-A9 PCEP/SR-TE/BGP-LS/YANG job reqs** | Greenhouse/Lever/Ashby [Robust] showing 2+ concurrent reqs at the carrier. LinkedIn-public-only → MEDIUM |
| **NO-A10 CTrO/CDO appointment** | LinkedIn profile change [Robust] + PR Newswire OR SEC 8-K Item 5.02 |

### International Sources (Tim Z's territory - elevated priority here)

Tim Z's territory leans heaviest on this segment (global Tier 1/2 carriers). Elevate Capacity Media + TelecomTV to **primary** trade press (vs. US stack where Fierce / Light Reading lead). See `signal-framework.md` "International Source Stack" for full detail.

- **Global/EMEA:** Capacity Media (PRIMARY), TelecomTV (PRIMARY), Light Reading Europe, Total Telecom, ETNO press (EU-wide positioning). Target operators: Orange Business, BT Global, Colt, Deutsche Telekom International, KPN International, TIM Sparkle, Telia Carrier, Arelion, Liberty Global, Telefónica Tech.
- **APAC:** Capacity Asia, TelecomAsia.net. Target operators: NTT, Tata Communications, PCCW Global, Telstra, Singtel, Axiata, Epsilon, Console Connect.
- **LATAM:** BNamericas, Capacity LATAM. Target operators: Cirion, Telxius (wholesale arms of Telefónica LATAM).
- **MENA:** Capacity MENA, Commsmea. Target operators: e& Carrier Wholesale, Etisalat International.
- **Subsea (global):** TeleGeography Submarine Cable Map RFS feed (PRIMARY), SubmarineNetworks.com.
- **I-series signals (see `signal-framework.md`):** I2 Sovereign AI Compute Grants hit Network Op targets frequently (carriers winning government sovereign-network contracts).

**Quarterly batch:** Earnings transcript sweep across full Tier 1/2 target list - highest-yield recurring task.

---

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A, website visitor tracking) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and are not duplicated in this file.
