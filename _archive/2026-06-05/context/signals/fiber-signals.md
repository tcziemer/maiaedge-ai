# Fiber Operator — Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` and `segments/fiber-operator.md`.

HubSpot `customer_segment`: **Fiber Operator**
Sub-segments: **Regional CLEC**, **Long Haul / Backbone**, **Dark Fiber Specialist**, **Co-op/consortium**, **Greenfield** (pre-operational)

---

## Tier A — Meeting-Ready Signals (1wk-30d window)

### F-A1. BEAD Subgrant Award (by state broadband office)

**Why:** Winners have binding 4-year build obligations and 18-24 month provisioning ramps. Middle-mile monetization questions surface within 60-120 days of award. They need to answer "how do we sell into these new footprints once built?"

**Source:** State broadband office award pages (47+ active: Texas Comptroller, Michigan LEO, CA CPUC, PA Broadband Authority), NTIA BEAD Progress Dashboard, fiberbroadband.org news, Telecompetitor.

**Pattern:** `"BEAD subgrant awarded" + entity name + route miles` — filter fiber tech selections > $5M.

**Freshness:** 1wk (Q2-Q4 2026 = peak award velocity). **Confidence:** HIGH.

### F-A2. Regional Fiber PE Acquisition / Roll-up — Announcement OR Close (two-event firing added 2026-04-27)

**Why:** PE-backed operators integrate 2-5 networks in year one — classic "fiber islands" problem. Two distinct windows of opportunity:
- **At announcement** (deal signed, not yet closed): 6-12 month pre-close runway. Sponsor's value-creation plan is being finalized; OSS/BSS unification and provisioning standardization are top-of-deck items. Engaging during this window means we're known when the operating plan locks.
- **At close**: First 90-day priorities are OSS/BSS unification and provisioning standardization — Day 60-90 post-close is the integration sweet spot.

If both events fire on same fiber operator within 12 months → +6 stacking auto-elevation.

**Source:** Fierce Network M&A tracker, Light Reading M&A Watch, Stonepeak/Oak Hill/Brookfield/DigitalBridge/Grain/EQT/CVC DIF press, **SEC 8-K Item 1.01 + S-4 (announcement), SEC 8-K Item 2.01 (close)**.

**Pattern (announcement):** `("announces" + "to acquire" | "agreement to acquire" | "definitive agreement" | "to combine with" | "signs definitive") + "fiber" + ("route miles" OR "combined footprint" OR "platform")`

**Pattern (close):** `("acquires" | "completes acquisition" | "closes" | "completes platform acquisition") + "fiber" + ("route miles" OR "combined footprint")`

**Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH.

### F-A3. AI Data Center Lit / Dark Fiber Win or RFP

**Why:** Winning an AI-DC interconnect contract with 800G/1.6T and 36x fiber density exposes every NNI, partner-reach, and multi-region gap. They close the deal, realize they can't deliver cross-footprint.

**Source:** Lightwave Online, Telecom Ramblings, Data Center Knowledge, DCD, FierceNetwork, operator press (Uniti, FiberLight, Zayo, Lumen, Crown Castle Fiber, Lightpath).

**Pattern:** `("AI data center"|"hyperscaler"|"GPU cluster") AND ("dark fiber"|"IRU"|"wavelength"|"400G"|"800G") + operator name`

**Freshness:** 1wk. **Confidence:** HIGH.

### F-A4. NaaS / Automation / Portal Launch (competitor proof-of-struggle)

**Why:** An operator announcing a "real-time portal" is 12-18 months into automation and almost always hitting the NNI/Type 2 wall. ACTIVE buyers, not cold.

**Source:** Fierce Network Modernization, Light Reading, MEF.net news, Capacity Media, LinkedIn company pages.

**Pattern:** `("launches"|"unveils") + ("NaaS"|"on-demand portal"|"API-driven"|"self-service provisioning")`. Zayo DynamicLink is the benchmark — track copycat announcements explicitly.

**Freshness:** 30d. **Confidence:** HIGH.

### F-A5. Executive Hire — VP Network Automation / Chief Network Officer / VP Wholesale / VP Carrier Relations

**Why:** 90-day modernization plan mandate. Budget, pain, vendor-shopping mode, approachable.

**Source:** SEC 8-K Item 5.02 (public fiber ops), PR Newswire / Business Wire Appointments RSS, Light Reading People, Fierce Telecom leadership column, operator IR newsrooms, TheOrg diffs. See `signal-framework.md` for full Sales-Nav-free stack.

**Pattern:** `"named"|"appointed"|"joins as" + (VP|SVP|Chief) + (Network Automation|Network Operations|Wholesale|Carrier Relations|Service Delivery|Transport|Interconnection)`

**Freshness:** 30d post-hire (not day 1). **Confidence:** HIGH — single best relationship-entry signal.

### F-A6. Dark Fiber IRU / Long-Haul Sold-Out Announcement

**Why:** "IRU signed with hyperscaler" = operator committed 20-year capacity on a route. Optimizing remaining strands for sellable services. Monetization urgency peaks.

**Source:** Lightwave Online, Telecom Ramblings, operator 8-Ks, press releases.

**Pattern:** `"IRU"|"indefeasible right of use"|"dark fiber agreement" + hyperscaler/operator` OR `"sold out" + "long-haul capacity"`

**Freshness:** 30d. **Confidence:** HIGH.

### F-A7. Merger / Acquisition / Consolidation — Announcement OR Close (broader than F-A2; two-event firing added 2026-04-27)

**Why:** User-flagged as explicit priority signal. Broader than `F-A2` (PE-only) — includes any fiber-operator merger, acquisition, divestiture, carve-out, or consolidation regardless of sponsor type. Two distinct windows:
- **At announcement**: 6-12 month pre-close engagement runway. Buyer-side strategy team is scoping the post-close integration — being on their shortlist before close changes everything.
- **At close**: Island-unification pain is the operational reality on Day 1. Day 60-120 post-close is the sweet spot where new leadership can spend.

If both events fire on same fiber operator within 12 months → +6 stacking auto-elevation.

**Source:** Fierce Network M&A tracker, Light Reading M&A Watch, **SEC 8-K Item 1.01 + S-4 (announcement), SEC 8-K Item 2.01 (close)**, S&P / Infrastructure Investor, Telecompetitor, Telecom Ramblings.

**Pattern (announcement):** `("announces" + "to acquire" | "agreement to acquire" | "definitive agreement" | "to combine with" | "to divest" | "to spin off" | "to carve out") AND ("fiber"|"route miles"|"broadband"|"wholesale") + fiber-operator identification`

**Pattern (close):** `("acquires"|"completes acquisition"|"closes merger"|"closes divestiture"|"carve-out completes"|"merger completes") AND ("fiber"|"route miles"|"broadband"|"wholesale")`

**Freshness:** ≤60d from whichever event is more recent = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH.

### F-A8. ABS / Refinancing / CLO / Secured Debt Issuance

**Why:** Fiber operators issuing asset-backed securitizations (ABS), bond refinancings, or secured-debt facilities are signaling monetization-velocity urgency  -  they need the plant generating cash fast enough to service debt. Creates a CFO-level urgency window for revenue-growth platform spend. Pattern most common at regional CLECs + dark-fiber specialists.

**Source:** SEC EDGAR (S-1, S-3, 8-K Item 8.01 / 2.03), Moody's / KBRA / DBRS rating releases, Fitch, Reorg Research fiber tag, PitchBook public pages.

**Pattern:** `("ABS"|"asset-backed securitization"|"senior notes"|"revolving credit facility"|"term loan B"|"refinancing") AND (fiber|broadband|wholesale telecom) + operator`

**Freshness:** 90d (outreach within 90 days of issuance). **Confidence:** MED-HIGH.

### F-A9. Consortium / Federation / Co-op Announcement

**Why:** Multi-operator consortia, co-op federations, or cross-operator partnership announcements are direct federation-readiness signals. Applies especially to the new `Co-op/consortium` sub-segment. Pattern matches the federation thesis MaiaEdge is ahead of carrier messaging on  -  these operators are already organized around it.

**Source:** Fierce Network, Telecompetitor, state broadband office press, NRECA (co-op coverage), NTIA middle-mile grant announcements, BroadbandCommunities.

**Pattern:** `("consortium"|"federation"|"co-op alliance"|"multi-operator partnership"|"open-access agreement") AND (fiber|broadband|middle-mile) + participants`

**Freshness:** 90d. **Confidence:** MED-HIGH.

---

## Tier B — Strong Signals (30-90d window)

### F-B1. 400G/800G Optical Upgrade Press

Upgrade programs expose manual provisioning underlayer. "New 800G backbone + 90-day NNI" = exact wedge.

Source: Lightwave Online, Light Reading Cloud, Ciena/Nokia/Infinera/Ekinops/Ribbon/Adtran press.

Pattern: `"400G"|"800G coherent"|"Apollo"|"WaveLogic" + operator + ("deployed"|"expansion")`. Confidence: MED-HIGH.

### F-B2. Route Expansion / New-Market Entry

"Extending to Columbus" = multi-state footprint they've never provisioned across. Fiber-islands onset.

Source: Operator press, Fierce Network, Telecompetitor, BroadbandCommunities.

Pattern: `"fiber expansion"|"new market"|"enters" + state/metro`. Confidence: MED-HIGH.

### F-B3. Subsea Cable Landing / Backhaul Partnership

Subsea landings create cross-country backhaul pressure. Landing operator needs partner reach inland.

Source: SubmarineNetworks.com, TeleGeography, Telecom Ramblings, local business journals.

Pattern: `"landing station"|"cable landing"|"subsea backhaul" + operator/region`. Confidence: MED-HIGH.

### F-B4. Public-Company Earnings Call Keyword Hits

Uniti, Lumen, Frontier, Consolidated, Cogent, Crown Castle Fiber C-suite naming "provisioning speed," "automation capex," or "wholesale growth" = internal business case being built.

Source: Seeking Alpha transcripts, Motley Fool, SEC EDGAR 10-Q/8-K, company IR pages.

Pattern: Transcript search `"provisioning"|"time to activate"|"automation"|"NaaS"|"dark fiber monetization"|"wholesale growth"|"mean time to install"`. Confidence: HIGH (public) / MED (PE sponsor letters).

### F-B5. Fiber Connect / ISE EXPO / FTTH Speaker Slots on Automation / Monetization

Operator speakers on "automation," "cross-carrier," "dark fiber monetization," "AI interconnect" panels are self-identifying.

Source: fiberbroadband.org agenda, ISE Expo, FTTH Conference.

Pattern: Session titles matching automation/NaaS/provisioning/monetization; extract speaker + company. Confidence: HIGH.

---

## Tier C — Directional Signals (60-90d window)

### F-C1. FCC Pole-Attachment / Make-Ready Complaint Filings (RBAT docket)

Operators filing pole disputes are watching BEAD timelines slip — forcing them back to monetizing existing middle-mile fiber.

Source: FCC EDOCS/ECFS, docs.fcc.gov, FCC RBAT docket page, Davis Wright Tremaine Broadband Advisor.

Pattern: Docket search `"pole attachment"` + complaint filings past 90d; filter attacher = fiber operator. Confidence: MED.

### F-C2. State PSC / PUC Filings — Tariff Changes, CLEC Certifications

CLEC certification in new state = multi-state expansion. Tariff filings for new wholesale products = productizing.

Source: State PUC dockets (CA CPUC, TX PUC, NY PSC, FL PSC, VA SCC).

Pattern: `"CLEC certification"|"certificate of convenience and necessity"|"wholesale tariff" + operator`. Confidence: MED.

### F-C3. LinkedIn Company-Page Post Signals

Posts celebrating "first automated NNI turn-up," "new customer portal," partnerships reveal active transformation.

Source: LinkedIn company pages of top 120 target fiber operators.

Pattern: `"automated"|"portal"|"customer experience"|"cloud on-ramp"|"milestone"` + reactions from Director+ titles. Confidence: MED.

### F-C4. Government / Hyperscaler RFP Aggregators

Operators shopping an RFP for "middle-mile fabric" or "NNI automation" are in-market today.

Source: BidNet / SAM.gov, state e-procurement portals, FindRFP.

Pattern: `"middle-mile"|"carrier-grade NaaS"|"automated provisioning" + NAICS 517`. Confidence: MED.

### F-C5. Earnings-Disclosed Fiber-Count Step-Change

**Why:** Public fiber operators (Zayo, Windstream, Consolidated, Frontier, Lumen) occasionally disclose on earnings calls that fiber-order sizes have jumped materially (historical 8-12 fibers per route to 144-432+ on recent deals; 864-fiber hyperscaler orders). Indicates manual provisioning can no longer absorb customer demand. Internal angle-selection signal; use to time outreach to the VP Network / Chief Network Officer persona.

**Source:** Seeking Alpha transcripts, Motley Fool, SEC 10-Q / 8-K Exhibit 99, operator IR pages.

**Pattern:** Transcript search `"fiber count"|"fiber pairs"|"fiber density"|"order size"|"multi-ribbon"` AND (step-change language like "up from"|"previously"|"now seeing"). Confidence: MED.

---

## Sources for This Segment (scrape weekly — Phase 2 expanded 2026-04-27)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework.

### Robust tier

1. Fierce Network + Fierce Telecom RSS — M&A tracker, hiring roundups, carrier-agreements, layoff tracker, **People column** [Robust]
2. Light Reading RSS — optical, M&A Watch, People moves [Robust]
3. Lightwave Online — 400G/800G, IRU, AI-DC fiber [Robust]
4. Telecompetitor + BroadbandCommunities — regional operators, BEAD coverage [Robust]
5. SEC EDGAR full-text — public fiber operators (Uniti, Lumen, Frontier, Consolidated, Cogent, Crown Castle, Zayo if public, Altice USA); 8-K Items 1.01 / 2.01 / 5.02; S-1 / S-3 / 424 (ABS prospectuses for F-A8) [Robust]
6. NTIA BEAD Progress Dashboard — subgrant awards (broadbandusa.ntia.gov) [Robust]
7. **Federal Register** — daily filings; BEAD allocation announcements + FCC RDOF + Affordable Connectivity Program [Robust]
8. LinkedIn public posts + Greenhouse + Lever + Ashby — public job posts and exec posts at target operators (F-A5) [Robust]
9. Apollo MCP — `apollo_organizations_enrich`, Job Postings filter, Job Changes, Funding events (covers AP-1 / AP-2 / AP-7) [Robust]
10. **USTelecom** + **NTCA (Rural Broadband Association)** + **Fiber Broadband Association (FBA)** + **INCOMPAS** member press [Robust — trade groups publish reliable major-news releases]
11. **Lit Communications + CommScope + Calix + Adtran customer-win press** — supplier announcements often reveal big customer ramps before operator press [Robust]
12. PR Newswire / Business Wire — fiber + telecom feed + Appointments tag [Robust]

### Medium tier

13. State broadband office press — 47+ state offices (prioritize TX, CA, NY, PA, MI, VA, FL, OH, NC, GA, AZ, WA, OR, CO, MN, WI, IL, OH, IN, NJ) [Medium where state has reliable RSS; Aspirational for states publishing irregularly]
14. **BroadbandBreakfast** — DC-policy-focused fiber coverage [Medium]
15. **Fiber Connect + ISE Expo + FTTH Conference + USTelecom-NTCA Summit** — agenda scrapers [Medium]
16. Tele-Tech (telecom trade) [Medium]
17. **WTA (Wireless ISP Association)** + **NCTA (cable + fiber trade)** press [Medium]
18. Earnings transcripts — Seeking Alpha free tier; SEC 10-Q transcripts (more reliable) [Medium]
19. ABS market data — **Fitch ABS reports** + **Moody's ABS reports** + **KBRA** + **Bloomberg Terminal ABS** public summaries (covers F-A8) [Medium]
20. **USAC (Universal Service Administrative Co)** Connect America Fund news [Medium]

### Aspirational tier (never standalone for major signals)

21. FCC EDOCS — pole-attachment + RBAT docket [Aspirational — government data, scrape-able but layout-fragile]
22. State PUC dockets — TX PUC, FL PSC, NY PSC, CA CPUC, others by request [Aspirational]
23. SubmarineNetworks + TeleGeography — subsea + cross-border [Aspirational where free-tier; Medium for paid summaries]
24. Wayback Machine month-over-month diffs of target operator websites — new BEAD project mentions, new POPs, new wholesale-tier products [Aspirational]
25. Reddit r/networking + r/HomeNetworking — ground-truth on operator service quality [Aspirational]
26. Glassdoor reviews — engineer reviews mentioning current network architecture / NaaS efforts at target operators [Aspirational]

### International (Tim Z's territory)

See `signal-framework.md` "International Source Stack" for the full regional stack + I-series signal classes (I1 state-aid / sovereign funding awards, I2 sovereign AI compute grants).

- **EMEA:** Light Reading Europe, Telecompaper (NL/DACH regulator coverage) [Robust], Total Telecom [Robust], Fibre Provider (UK) [Medium], Capacity Media [Robust]. Regulators: Ofcom UK, BNetzA Germany, ARCEP France, AGCOM Italy, CNMC Spain, ACM Netherlands [Robust]. **UK Project Gigabit contract awards** (direct BEAD analogue) [Robust]. **EU CEF Digital awards + Digital Decade tracker** [Robust]. **EU state-aid register** (competition-cases.ec.europa.eu) [Robust]. Key operators: Colt, euNetworks, Eurofiber, EllaLink, Arelion, Telia Carrier.
- **APAC:** TelecomAsia.net, Capacity Asia, DealStreetAsia [Medium]. Regulators: IMDA Singapore, MIC Japan, TRAI India, ACMA Australia [Robust]. Key operators: Digital Realty AMS-IX partners, BBIX Japan, Superloop AU, Megaport AU.
- **LATAM:** BNamericas, TeleSemana, Teletime (BR) [Medium]. Regulators: Anatel BR, IFT Mexico, Subtel Chile, ENACOM Argentina [Robust]. Key operators: Cirion, Telxius.
- **MENA:** Capacity MENA, Commsmea, Zawya [Medium]. Regulators: TDRA UAE, CST Saudi [Robust]. Key operators: e& Carrier Wholesale, Etisalat, du.

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **F-A1 BEAD subgrant award** | NTIA portal entry [Robust] + state broadband office press [Medium]. NTIA alone for major awards → HIGH; trade press alone → MEDIUM (recipient may be sub-contractor not operator — apply contractor/operator filter) |
| **F-A2 PE acquisition / roll-up (announcement)** | SEC 8-K Item 1.01 [Robust] + ≥1 trade press OR 2 independent trade press [Robust] |
| **F-A2 PE acquisition / roll-up (close)** | SEC 8-K Item 2.01 [Robust] + ≥1 trade press OR 2 independent trade press [Robust] |
| **F-A3 AI-DC fiber win** | Operator press [Robust] + counterparty named (anchor cloud / DC operator named); supplier-press from Lit Comm / CommScope often surfaces this first [Robust] |
| **F-A4 NaaS / portal launch** | Operator's own announcement [Robust] + product page on operator's website. Marketing blog alone → MEDIUM |
| **F-A5 VP Network Automation hire** | LinkedIn profile change [Robust] + (PR Newswire Appointments [Robust] OR SEC 8-K Item 5.02 OR operator IR press) |
| **F-A6 dark fiber IRU** | Operator press [Robust] + (annual report / 10-K mention OR counterparty named in press) |
| **F-A7 broader M&A (announcement OR close)** | SEC filing [Robust] + ≥1 trade press OR 2 independent trade press [Robust] |
| **F-A8 ABS / refinancing** | SEC S-1 / S-3 / 424 [Robust] + rating agency note [Medium] (Moody's / KBRA / Fitch) OR ≥1 trade press [Robust] |
| **F-A9 consortium / federation** | Multi-operator joint press [Robust] OR state/federal middle-mile grant announcement [Robust] |

### International Sources (Tim Z's territory)

See `signal-framework.md` "International Source Stack" for the full regional stack + I-series signal classes (I1 state-aid / sovereign funding awards, I2 sovereign AI compute grants).

- **EMEA:** Light Reading Europe, Telecompaper (NL/DACH regulator coverage), Total Telecom, Fibre Provider (UK), Capacity Media. Regulators: Ofcom UK, BNetzA Germany, ARCEP France, AGCOM Italy, CNMC Spain, ACM Netherlands. **UK Project Gigabit contract awards** (direct BEAD analogue). **EU CEF Digital awards + Digital Decade tracker**. **EU state-aid register** (competition-cases.ec.europa.eu). Key operators: Colt, euNetworks, Eurofiber, EllaLink, Arelion, Telia Carrier.
- **APAC:** TelecomAsia.net, Capacity Asia, DealStreetAsia. Regulators: IMDA Singapore, MIC Japan, TRAI India, ACMA Australia. Key operators: Digital Realty AMS-IX partners, BBIX Japan, Superloop AU, Megaport AU.
- **LATAM:** BNamericas, TeleSemana, Teletime (BR). Regulators: Anatel BR, IFT Mexico, Subtel Chile, ENACOM Argentina. Key operators: Cirion, Telxius.
- **MENA:** Capacity MENA, Commsmea, Zawya. Regulators: TDRA UAE, CST Saudi. Key operators: e& Carrier Wholesale, Etisalat, du.

---

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A, website visitor tracking) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and are not duplicated in this file.
