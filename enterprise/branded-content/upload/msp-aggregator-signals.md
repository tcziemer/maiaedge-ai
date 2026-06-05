# MSP / Aggregator - Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` and `segments/msp-aggregator.md`.

HubSpot `customer_segment`: **MSP/Aggregator** (telecom/network aggregators, NOT IT MSPs).
Sub-segments (5 active, post-Phase 1.6 2026-05-13): **Telecom Aggregator - MSP**, **Managed Network Services - MSP** (`- MSP` suffix; legacy `- Network Operator` suffix archived), **TSD Technology Services Distributor - MSP**, **Master Agent - MSP**, **Cloud + Telecom Hybrid MSP - MSP**. See `context/account-tiering/sub-segment-qualification.md` for full reference.

**Two subtypes in scope per [msp-aggregator.md](../segments/msp-aggregator.md):**
1. US TSD / TA channel (Telarus / AppDirect / Upstack / AVANT / Bridgepointe / Sandler / ScanSource Intelisys, plus TA agencies).
2. NaaS platform operators (CBC Tech, Epsilon, PCCW Console Connect, Arelion, Sparkle Sparkhub).

**Do NOT target:** IT MSPs (helpdesk, cybersecurity), voice termination wholesalers, SMS/A2P/CPaaS aggregators, cellular IoT MVNOs, roaming hubs/IPX providers, eSIM/SIM platform vendors. See the segment file's ICP Exclusion List for detail and self-filtering copy rule.

---

## Tier A - Meeting-Ready Signals (1wk-30d window)

### M-A1. PE Acquisition / TSD Roll-up - Announcement OR Close (two-event firing added 2026-04-27)

**Why:** Two distinct windows of opportunity:
- **At announcement** (deal signed, not yet closed): 6-12 month pre-close runway. Acquirer's integration team is scoping multi-carrier reconciliation requirements; orchestration platform decisions are being made.
- **At close**: Post-close integration forces multi-carrier data reconciliation; acquirer inherits orchestration pain across disparate carrier portals. 60-120 days post-close is prime.

If both events fire on same TSD within 12 months → +6 stacking auto-elevation.

**Source:** Channel Futures M&A tag, ChannelE2E, Channel Playbook, PitchBook/Tracxn alerts on Upstack / Telarus / AppDirect / Bridgepointe / Sandler, **SEC 8-K Item 1.01 (announcement) + 2.01 (close)** for public-company TSDs.

**Pattern (announcement):** `("announces" + "to acquire" | "agreement to acquire" | "definitive agreement" | "announces roll-up")` on channelfutures.com / channele2e.com filtered to TSD/brokerage/agency.

**Pattern (close):** `"acquires"|"completes acquisition"|"roll-up completes"|"closes acquisition"` filtered to TSD/brokerage/agency; Tracxn acquirer pages (Upstack has 30+).

**Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH.

### M-A2. Carrier Dropped from Line Card

**Why:** Forced re-architecture; customers on dropped carrier need replacement path in weeks. "Federated backup carrier" moment.

**Source:** TSD news pages (telarus.com/news, sandlerpartners.com/partners, appdirect press), Channel Futures "line card"+"supplier" filters, agent LinkedIn.

**Pattern:** `"removed from line card"|"no longer offers"|"supplier change"|"contract ended" + TSD`

**Freshness:** 1wk. **Confidence:** HIGH.

### M-A3. New Carrier Added to Portfolio

**Why:** Each added carrier multiplies orchestration surface area; aggregator quote desks scale linearly with carriers. MaiaEdge collapses to one API.

**Source:** TSD press pages, Channel Futures "supplier agreements" roundup, iAgentNetwork.

**Pattern:** `"adds"|"signs"|"expands line card"|"new supplier"` + TSD name. Also diff Sandler/Telarus/AVANT/AppDirect supplier pages week-over-week.

**Freshness:** 1wk. **Confidence:** HIGH.

### M-A4. "AI Practice" / "AI Solutions" Launch

**Why:** 58% of buyers want AI help; only 13% of Technology Advisors feel ready. AI-practice press releases almost always lack the network story (AI workloads need deterministic paths). Opener: "You launched an AI practice - how's the network layer?"

**Source:** Channel Futures, ChannelE2E, Dialpad/UJET partner award releases, TSIA "State of Channel Partnerships 2026," Mindmatrix PartnerTechX.

**Pattern:** `"AI practice"|"AI solutions"|"AI advisory"|"AI readiness"` + (TSD|aggregator|agent).

**Freshness:** 30d. **Confidence:** HIGH.

### M-A5. Executive Hires - CRO / VP Solutions Engineering / VP Product / VP AI Practice

**Why:** 90-day "new strategy" window. SEs and Product VPs feel orchestration pain first.

**Source:** Channel Futures weekly hiring roundup ("Ribbon Layoffs, Telarus Hirings" format), ChannelE2E People column, PR Newswire / Business Wire Appointments RSS, TSD IR pages, TheOrg diffs on ~40 TSD/aggregator company list, Dialpad/UJET partner award press. See `signal-framework.md` for full Sales-Nav-free stack.

**Pattern:** Cross-reference each detected exec move against TSD/aggregator target list + title match `(CRO|VP Solutions Engineering|VP Product|VP AI Practice)`.

**Freshness:** 30d (LinkedIn) / 1wk (press). **Confidence:** HIGH.

### M-A6. TSD Platform / Quoting-Engine Replatforming (job-post signal)

**Why:** TSDs hiring for supplier strategy, platform engineering, developer experience, partner platform, or head of automation roles indicates the TSD is actively rebuilding its platform layer. Connector-building window opens at this stage  -  MaiaEdge slots in as an OpEx platform the TSD can white-label during the rebuild rather than bolt on post-launch.

**Source:** TSD careers pages, LinkedIn Jobs filtered to Telarus / AppDirect / Upstack / AVANT / Bridgepointe / ScanSource Intelisys / Sandler / TD SYNNEX, Greenhouse / Ashby public job boards.

**Pattern:** Job titles / descriptions matching `(supplier strategy|platform engineering|developer experience|partner platform|head of automation|quoting platform|VP Platform|VP Developer Experience)` at a target TSD.

**Freshness:** 30d. **Confidence:** MED-HIGH.

### M-A7. ScanSource / TDSYN Earnings Recurring-Revenue-Mix Disclosure

**Why:** ScanSource Intelisys disclosed recurring-revenue mix 29.3% → 36.0% Q3 FY25 (publicly verifiable). When ScanSource or TD SYNNEX call out a step-change in recurring-revenue mix (or specifically call out Intelisys / agent-business growth rate), it's a public leading indicator that the channel's bandwidth-reselling model is compressing and platforms are where growth lives. Use this to time outreach to TSD Platform / CRO personas.

**Source:** ScanSource (SCSC) + TD SYNNEX (SNX) investor pages, Motley Fool transcripts, SEC EDGAR 10-Q, Seeking Alpha.

**Pattern:** Transcript grep `"recurring"|"recurring revenue"|"agent business"|"Intelisys"|"recurring mix"` in quarterly transcripts, filter for step-change language.

**Freshness:** Quarterly (90d window). **Confidence:** HIGH for the narrative; timing of individual outreach is a 60-day window post-earnings.

---

## Tier B - Strong Signals (30-90d window)

### M-B1. Layoffs / Restructuring at Major Aggregators

Disruption loosens incumbency; survivors need wins fast and will audition new stories.

Source: Channel Futures "channel business" feed ("Ribbon Layoffs, Telarus Hirings" format), layoffs.fyi, TheLayoff.com forums, LinkedIn #OpenToWork spikes.

Pattern: `"layoffs"|"restructuring"|"reduction in force" + TSD`. Confidence: MED-HIGH.

### M-B2. NaaS / SASE / SD-WAN Platform Launch by TSD or Agent Group

Programmable story = selling outcome but don't own underlay. "We are the underlay" conversation.

Source: Channel Futures, ChannelPro, BusinessWire, Mplify LSO announcements.

Pattern: `"launches"|"unveils" + "NaaS"|"SASE"|"SD-WAN"|"programmable" + agent/TSD`. Confidence: MED-HIGH.

### M-B3. New Marketplace / Portal / Quote-Engine Launch

Every TSD building a portal hits the same wall: carrier APIs don't exist or are inconsistent. One demo from "build vs. MaiaEdge."

Source: ScanSource / Intelisys investor pages, AppDirect press, Telarus news, Channel Futures portal coverage.

Pattern: `"new portal"|"marketplace"|"quote engine"|"partner platform"|"self-serve" + TSD`. Confidence: MED-HIGH.

### M-B4. Public-Company Earnings - Agent Business / Automation / Convergence Mentions

CFO language previews 6-month priorities. ScanSource Q2 FY26 flagged "converged communication sales team" unifying Intelisys with hardware - orchestration pain signaled from top.

Source: Motley Fool transcripts, investor pages for ScanSource (SCSC), TD SYNNEX (TDSYN), Comcast Business (CMCSA).

Pattern: Transcript grep `"agent"|"Intelisys"|"automation"|"convergence"|"provisioning"` in latest quarter. Confidence: HIGH.

### M-B5. Enterprise Logo / Customer Win Announcements

Aggregator wins enterprise = inherited SLA pressure day one. Multi-site enterprise = multi-carrier = MaiaEdge story.

Source: TSD press pages, Channel Futures "customer wins," LinkedIn VP Sales posts, case-study pages diffed.

Pattern: `"selected by"|"chosen by"|"wins"|"new customer" + SLA/multi-site/enterprise`. Confidence: MED.

---

## Tier C - Context Signals (30-90d window)

### M-C1. Channel Conference Speaking Slots

Speaking slot = leader in "showcase a new story" mode for 60d before event. CP Expo 2026 added CEO track + AI Symposium.

Source: agenda.channelpartnersconference.com, MSP Summit agenda, NexGen agenda, Cloud Communications Alliance events. Vendelux attendee lists.

Pattern: Scrape agenda monthly, diff speaker list vs. ICP target list; flag anyone on AI / NaaS / SASE / CEO-track panels. Confidence: MED-HIGH.

### M-C2. FedRAMP / CMMC / StateRAMP Push Announcements

CMMC contractually enforceable in 2026; MSPs with federal/defense customers must modernize underlay. Federated/sovereign network = fit.

Source: FedRAMP.gov marketplace RSS, GovRAMP.org, Channel Futures government coverage, Continuum GRC blog, Security Boulevard.

Pattern: `"FedRAMP authorized"|"CMMC"|"StateRAMP"|"TX-RAMP" + MSP/aggregator`. Confidence: MED-HIGH.

### M-C3. Copper Retirement / TDM Sunset / STIR-SHAKEN Mandates

FCC March 2026 Network Modernization Order eliminated rules delaying copper removal. Modernization budget live now.

Source: FCC Daily Digest, Telecom Ramblings, CFCA, vendor POTS-replacement news.

Pattern: `"copper retirement"|"TDM sunset"|"grandfathering"|"STIR/SHAKEN deadline" + carrier/aggregator`. Confidence: MED.

### M-C4. New Enterprise Vertical Announcement (Healthcare, Finance, Manufacturing)

Vertical push = SLA-sensitive customers. HIPAA/PCI/OT-security language in press = tell.

Source: Aggregator press, Channel Futures vertical coverage, BusinessWire filtered to channel.

Pattern: `"healthcare practice"|"financial services practice"|"manufacturing vertical" + TSD`. Confidence: MED.

### M-C5. Multi-Carrier Outage / SLA Finger-Pointing Public Incident

Perfect timing - aggregator in crisis-comms with enterprise customer; reminded they can't prove performance across carriers. Reach out 7-14 days post.

Source: Downdetector spikes, Reddit r/networking + r/sysadmin, ThousandEyes Internet Report, Telecom Ramblings outage coverage.

Pattern: Carrier + `"outage"|"degraded"` with aggregator customer reports. Confidence: MED (timing-sensitive).

---

## Sources for This Segment (scrape weekly - pruned 2026-05-11)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework.

**Search-anchor pattern is the canonical access method** - direct `web_fetch` is gated by URL-provenance on Cowork's runtime. Anchor each source via `web_search "{domain} {topic} {year}"` and read snippets from search results. Article URLs returned in search can then be fetched directly. Do NOT skip a documented source because direct fetch fails - use search anchoring.

**Segment-thinness caveat:** MSP/Aggregator is the lowest-velocity segment and the thinnest source-list of the five. CRN's content has been drifting toward award-press syndication (Channel Chiefs / Women of the Channel) rather than M&A/buildout news, so weight Channel Futures + ChannelE2E + TSD direct IR over CRN. If MSP yield consistently falls below the 25-floor, promote the Tier B EMEA channel press (Channel Partner Insight UK + IT Europa + ChannelBiz DACH) into the weekly scrape rotation.

### Robust tier

1. Channel Futures - M&A, hirings, carrier agreements, layoffs, vertical tags + **Channel Futures Hiring Roundup column** [Robust]
2. ChannelE2E + **ChannelE2E People column** [Robust]
3. TSD press pages - Telarus, AppDirect, Sandler Partners, AVANT, Bridgepointe, Upstack, **AppSmart, Intelisys (ScanSource subsidiary), ScanSource agent business** (weekly diff) [Robust]
4. **CRN** - channel + agent + TSD news; weight lower than Channel Futures + ChannelE2E given award-press drift [Robust with caveat]
5. **StockTitan** (SEC 8-K mirror with parsed summaries - `stocktitan.net/sec-filings/{ticker}/`) - primary surrogate for SEC EDGAR on public TSDs and parents (SCSC ScanSource, SNX TD SYNNEX, CMCSA Comcast Business); covers 8-K Items 1.01 / 2.01 / 5.02 [Robust]
6. SEC EDGAR full-text via search-anchor - backup to StockTitan [Robust]
7. FCC Daily Digest [Robust]
8. **ScanSource + TD SYNNEX investor relations + earnings calls** - quarterly deeper read; SCSC/SNX 10-Q transcripts via StockTitan or search-anchor [Robust]
9. PR Newswire + Business Wire + GlobeNewswire - Channel + Telecom feed + Appointments tag [Robust]
10. Apollo MCP - `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events - enrichment tool [Robust]
11. **Megaport + Console Connect + PacketFabric partner-add announcements** - when an aggregator partners with a NaaS platform, that's M-A3 (new carrier added) [Robust]
12. Greenhouse + Lever + Ashby public job boards at target TSDs (covers M-A6 platform replatforming signal) [Robust]

### Medium tier

13. **CompTIA / GTIA** (CompTIA community spun out as GTIA in 2025; both names in use depending on topic) - channel research org [Medium]
14. **Channel Partner Insight (UK)** + **IT Europa** + **ChannelBiz (DACH)** - promote into weekly rotation if domestic yield falls below 25-floor [Medium → Tier B fallback]
15. FedRAMP Marketplace new-authorization feed [Medium]
16. **Telecompetitor channel section** [Medium]
17. CP Expo / MSP Summit / NexGen + **Channel Partners Conference & Expo** agenda scrapers (context only) [Medium]
18. **Gartner SD-WAN Magic Quadrant** + **Forrester Wave** reports - paywalled, but headlines surface in search snippets [Medium]
19. **Frost & Sullivan TSD analysis** - paywalled, headlines only [Medium]
20. **TBI Connect (UK)** + **Channel Asia** [Medium]

### Excluded (do NOT scrape - cut 2026-05-11)

- Wayback Machine month-over-month diffs of TSD line-card / partner pages - high theoretical value but never actually run; replaced by direct TSD press page scrape (#3) which covers carrier-add events when TSDs publish them. For unpublished line-card changes, accept the visibility gap.
- Reddit r/sysadmin + r/MSP + r/networking - low signal density, IT-MSP-heavy bias confuses segment classification.
- Glassdoor reviews - login-gated.
- TheOrg.com free tier - Aspirational, never produced a signal.
- Public Slack channels (Cloud Native, NetDev) - not actually accessible.

LinkedIn public posts retained for **named-account research only** (specific company pages), not market-wide discovery - moved to `signal-framework.md`.

### International (Tim Z's territory - thinnest of the 5 segments internationally)

MSP / Aggregator ICP is predominantly a US channel concept. Europe has adjacent plays but coverage is sparse.

- **EMEA:** Channel Partner Insight (UK) [Medium], IT Europa [Medium], ChannelBiz (DACH) [Medium]. Low cadence - flag only significant moves. Target companies: Expereo, Masergy legacy assets, Wavenet, ITancia.
- **APAC / LATAM / MENA:** Minimal ICP fit. Deprioritize unless Tim Z flags specific regional aggregator activity.

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **M-A1 PE acquisition / TSD roll-up (announcement OR close)** | SEC 8-K [Robust] (Item 1.01 announcement / Item 2.01 close) + ≥1 trade press OR 2 independent trade press [Robust] |
| **M-A2 carrier dropped from line card** | TSD press release [Robust] OR Wayback Machine line-card diff [Aspirational] confirmed by ≥1 trade press [Robust]. Wayback alone → MEDIUM |
| **M-A3 new carrier added to portfolio** | TSD press release [Robust] OR partner platform's announcement (Megaport / Console Connect / PacketFabric) [Robust]. Either alone scores HIGH |
| **M-A4 AI Practice / AI Solutions launch** | TSD press release [Robust] + (TSD careers page hiring AI practice roles [Robust] OR partner award press [Medium]). **MUST pass IT MSP Test** - if the announcement is from a helpdesk/cybersecurity MSP not a telecom aggregator, EXCLUDE per signal-framework False Positive Patterns |
| **M-A5 CRO / VP SE / VP Product / VP AI Practice hire** | LinkedIn profile change [Robust] + (PR Newswire Appointments [Robust] OR Channel Futures hiring roundup [Robust] OR ChannelE2E People [Robust]) |
| **M-A6 TSD platform replatforming (job-post signal)** | Greenhouse/Lever/Ashby [Robust] showing 2+ concurrent platform/supplier-strategy/developer-experience roles at target TSD. LinkedIn-public-only → MEDIUM |
| **M-A7 ScanSource / TD SYNNEX recurring-revenue disclosure** | SEC 10-Q transcript [Robust] OR investor day press [Robust] alone scores HIGH; Seeking Alpha summary alone → MEDIUM |

---

### International Sources (Tim Z's territory - thinnest of the 5 segments internationally)

MSP / Aggregator ICP is predominantly a US channel concept. Europe has adjacent plays but coverage is sparse.

- **EMEA:** Channel Partner Insight (UK), IT Europa, ChannelBiz (DACH). Low cadence - flag only significant moves. Target companies: Expereo, Masergy legacy assets, Wavenet, ITancia.
- **APAC / LATAM / MENA:** Minimal ICP fit. Deprioritize unless Tim Z flags specific regional aggregator activity.

## Priority Routing

Signals M-A1, M-A2, M-A4, M-A5, M-A6, M-A7, M-B4 are highest-conversion - route to rep within 48 hours of detection. Channel moves fast; the 48-hour window matters more here than any other segment.

---

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A, website visitor tracking) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and are not duplicated in this file.
