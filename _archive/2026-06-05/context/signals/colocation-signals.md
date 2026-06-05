# Colocation Operator — Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` (scoring, cadence, delivery format) and `segments/colocation.md` (ICP, buyer personas, qualification).

HubSpot `customer_segment`: **Data Center Colo Provider**
Sub-segments: **Standard - colo**, **AI Signals - colo**, **Modular - colo**, **Greenfield** (pre-operational, cross-segment)

---

## Tier A — Meeting-Ready Signals (1wk-30d window)

### C-A0. Greenfield Build — Stage S2/S3 (permit + utility interconnection)

**Why it predicts a meeting:** Fabric decision gets made between permit filing and powered shell. Catching it at S2-S3 = 9-15 months of influence before fit-out. Critical for first-time multi-site operators (pair with site-count transition — see below).

**Stages (detect each, earliest = highest priority):**

| Stage | Lead Time | Source | Pattern |
|---|---|---|---|
| S1 — Site selection / MOU | 18-24mo | Bisnow, local business journals, state econ dev press | `("data center campus"\|"AI factory") AND ("announces"\|"MOU"\|"letter of intent") AND (county\|parish\|township)` |
| S2 — Permit / zoning filing | 12-18mo | County permitting portals, CEQA/NEPA/SEQRA, planning commission agendas | Permit applications tagged `"data center"\|"computing facility"` + applicant name match |
| S3 — Utility interconnection / PPA | 9-15mo | PJM/ERCOT/MISO/CAISO queue reports, utility commission filings, DCF Energy tag | `("interconnection agreement"\|"PPA signed"\|"load study") AND (MW\|megawatt) AND (data center)` |
| S4 — Groundbreaking / EPC contract | 6-12mo | Operator press, Bisnow, Construction Dive, ENR | `("breaks ground"\|"awards EPC contract") AND (data center\|campus)` |
| S5 — Powered shell / commissioning | 1-6mo | DCF, DCD, operator press | `("powered shell delivered"\|"commissioning"\|"Phase I complete")` |

**Priority:** S2-S3 = +3 score bonus. S4-S5 = no bonus (already past fabric decision).

**Freshness:** 90d. **Confidence:** HIGH (at S2-S3).

---

### C-A1. Site Count Transition — 1 → 2 Facilities

**Why it predicts a meeting:** First-ever multi-site design decision. Before this, network-between-sites was not a concept they owned. One-shot choice. Single highest-leverage moment for regional Colo operators.

**Detection:**
```
IF scraped_signal = "new facility announced by [company]"
  AND parse_facility_count(HubSpot.account[company].infrastructure_profile) = 1
  THEN transition_type = "1→2" → +6 score bonus
  ELSE IF parse is low-confidence:
    skip bonus (fall back to base greenfield score)

Parse method: LLM reads the free-text infrastructure_profile field at match time.
After successful detection, rewrite infrastructure_profile with updated count + context so next run has fresh state.
```

**Watch list examples:** Regional single-site operators adding site #2 — Flexential subsidiaries, NorthC, Tonaquint, Xapitus, edge operators launching second metro, Colo startups post-funding launching second campus.

**Freshness:** 90d. **Confidence:** HIGH.

---

### C-A2. GPU Cloud Tenant Anchor Announcement

**Why it predicts a meeting:** Operator just landed Lambda/Crusoe/Nebius/Nscale/Together as tenant. They now own a tenant whose SLA depends on deterministic paths — and they have zero fabric. Meeting-ready the week of the press release.

**Source:** Data Center Frontier, DCD, Data Center Knowledge, operator newsroom RSS, PR Newswire, Business Wire.

**Pattern:** `("signs"|"announces"|"welcomes"|"expands with") AND (Lambda|Crusoe|Nebius|Nscale|Together AI|Fluidstack|Vultr|RunPod) AND (colocation|colo|data center)`

**Freshness:** 30d. **Confidence:** HIGH.

---

### C-A3. Liquid Cooling / D2C Deployment Announcement

**Why it predicts a meeting:** Confirms AI-tenant readiness — operator has power/cooling but almost never has network to match. "You solved power, now solve determinism" opener.

**Source:** DCD product news, DCF, operator press, Vertiv/Schneider/CoolIT customer-win releases, LinkedIn company posts.

**Pattern:** `("direct-to-chip"|"D2C"|"rear-door heat exchanger"|"liquid cooling deployment"|"CDU"|"immersion") AND (colo|colocation|data center) AND (deploy|announce|install|retrofit)`

**Freshness:** 60d. **Confidence:** HIGH.

---

### C-A4. Executive Hire — VP/Director of Interconnection, Network, Fabric

**Why it predicts a meeting:** New leader's 90-day plan always includes "build our own fabric" or "fix cross-connect provisioning." Budget-authorized and actively looking.

**Source:** SEC 8-K Item 5.02 (public Colo REITs), PR Newswire / Business Wire "Appointments" RSS, DCD Careers + DCF People columns, company IR newsroom RSS, TheOrg.com diffs. See `signal-framework.md` for full Sales-Nav-free substitute stack.

**Pattern:** Title contains `(VP|Director|Head) of (Interconnection|Network|Network Engineering|Fabric|Connectivity|Platform)` AND `start_date < 90d` AND company in Colo target list. Cross-ref with LinkedIn "excited to join" post.

**Freshness:** 90d. **Confidence:** HIGH.

---

### C-A5. Network Engineering Job-Req Surge

**Why it predicts a meeting:** 3+ concurrent reqs for Network Architect / SDN / Fabric Engineer at a sub-$500M Colo = they're building something they don't have today. Indicates budget + roadmap.

**Source:** LinkedIn Jobs, Indeed, company careers pages, Greenhouse / Lever boards.

**Pattern:** Same company, ≥3 active reqs in 30d matching `(network architect|fabric engineer|SDN|interconnection platform|NOC lead|cloud on-ramp|MEF)`.

**Freshness:** 30d. **Confidence:** HIGH.

---

### C-A6. Anchor Tenant Signing (hyperscaler OR enterprise OR neocloud)

**Why it predicts a meeting:** Broader than `C-A2` (which is neocloud/GPU-specific). Any anchor-tenant signing  -  hyperscaler build-to-suit, Fortune 500 enterprise single-tenant lease, neocloud anchor  -  commits the colo to delivering tenant-specified SLAs it may not yet have fabric for. Creates a 60-90 day procurement window for connectivity.

**Dual-sided:** Fires simultaneously with neocloud `N-A7` (anchor tenant signing, neocloud-side) when a public neocloud files the lease. Surface both accounts.

**Source:** SEC 8-K Item 1.01 (public colo REITs + public neocloud tenants), operator press releases, DCF / DCD / Bisnow.

**Pattern:** `("signs"|"announces"|"executes"|"multi-year"|"build-to-suit") AND (lease|MSA|agreement) AND (MW|megawatt|campus|facility) + tenant identification`. Exclude shell-company or vague "unnamed tenant" filings unless counterparty can be inferred from reporting context.

**Freshness:** 1wk (filings <4 business days, press same-day). **Confidence:** HIGH.

---

### C-A7. Merger / Acquisition / PE Recap — Announcement OR Close (promoted from Tier B; two-event firing added 2026-04-27)

**Why it predicts a meeting:** Two distinct windows of opportunity, BOTH worth surfacing.
- **At announcement** (deal signed, not yet closed): the strategic decision has been made. Interconnection-revenue expansion is the #1 item on almost every colo sponsor thesis deck — the pre-close 6-12 month window is when the new sponsor is finalizing the operating plan and choosing platform vendors. Engaging early means we're a known option BEFORE close.
- **At close** (deal complete): Day 60-120 post-close is the integration sweet spot — pain is acute, new leadership is authorized to spend, the 100-day value-creation plan is active.

If both events fire on the same colo within 12 months → +6 stacking auto-elevation per signal-framework.md.

**Source:** PitchBook public pages, Mergr, DCD M&A tag, DCF Transactions, Infrastructure Investor, **SEC 8-K Item 1.01 + S-4 (announcement filings), SEC 8-K Item 2.01 (close filings)**.

**Pattern (announcement):** `("announces"|"to acquire"|"agreement to acquire"|"definitive agreement"|"to take-private"|"to merge with"|"signs definitive") AND (colocation|data center) AND (KKR|Blackstone|Brookfield|DigitalBridge|Stonepeak|IPI|I Squared|Partners Group|EQT|Macquarie|GI Partners)`

**Pattern (close):** `("acquires"|"completes acquisition"|"closes acquisition"|"completes take-private"|"closes recapitalization"|"completes merger") AND (colocation|data center) AND (sponsor)`

**Freshness:** ≤60d from whichever event is more recent (announcement OR close) = full Tier A. 60-90d = decayed. >90d from both = drop. **Confidence:** HIGH (SEC filings + sponsor press both confirm).

---

## Tier B — Strong Signals (30-60d window)

### C-B1. Public Colo 8-K / Earnings Call — Interconnection Miss Language

CEO/CFO admitting interconnection revenue flat or cross-connect velocity problem = internal heat. Applies to DLR, EQIX, IRM, plus any public filer.

Source: SEC EDGAR full-text, Seeking Alpha transcripts.

Pattern: `(8-K|10-Q) AND ("interconnection revenue"|"cross-connect"|"provisioning"|"attach rate") AND (decline|flat|headwind|initiative)`

Freshness: 90d. Confidence: MED-HIGH.

### C-B2. (Deprecated — see C-A7)

M&A / PE recap signals were promoted to Tier A (see `C-A7`) in the April 2026 refresh.

### C-B3. Power Capacity Uprate / PPA Announcement

Operator just secured incremental MW — about to lease to AI tenants, will need fabric to differentiate. Combine with C-A2 for Tier 1 trigger.

Source: DCF Energy section, DCD, utility commission filings (PJM, ERCOT, MISO), local press.

Pattern: `("PPA"|"power purchase"|"interconnection agreement" AND utility) OR ("uprate"|"additional MW"|"expanded capacity to") AND company`

Freshness: 90d. Confidence: MED.

### C-B4. Conference Speaking Slot — Interconnection / AI Panel

Operator exec publicly speaking on "AI-ready colo" or "interconnection at scale" is narrative-building. Will take the meeting.

Source: PTC, DCD Connect, Datacloud, Metro Connect, ITW, Capacity, AI Infrastructure Summit agenda pages.

Pattern: Agenda scrape, filter speakers by company type = Colo, panel titles matching `(interconnection|fabric|AI infra|GPU|inference|deterministic|sovereign)`.

Freshness: 30d pre-event / 14d post-event. Confidence: HIGH.

### C-B5. Sovereignty / Data-Residency Announcement

Colo claiming "sovereign" or "jurisdiction-controlled" capability needs policy-driven paths — BGP can't prove jurisdiction. Direct product fit.

Source: Operator press, DCD Regulation tag, DCF.

Pattern: `("sovereign"|"data residency"|"jurisdictional"|"EU AI Act"|"CLOUD Act") AND (colocation|facility|tenant)`

Freshness: 90d. Confidence: MED-HIGH.

---

## Tier C — Context Signals (60-90d window)

### C-C1. Hyperscaler-Adjacent Announcement (<50 miles claim)

Operators selling "low-latency to cloud" need actual cloud on-ramps, not just geographic proximity. Wedge for cloud on-ramp-as-a-product.

Pattern: `("<50 miles from"|"adjacent to"|"directly connected to") AND (AWS|Azure|Google Cloud|Oracle|hyperscaler region)`. Confidence: MED.

### C-C2. Carrier-Neutral / Meet-Me-Room Expansion

Adding carriers = tenants demanding more network options. Patching with physical. Virtual MMR pitch lands.

Pattern: `("adds"|"welcomes") AND (carrier|network provider) AND (meet-me room|MMR|carrier-neutral)`. Confidence: MED.

### C-C3. Tenant Churn to Equinix or Megaport (loss signal)

Equinix/Megaport customer-win press releases read inversely: who LOST the customer. Operator is bleeding.

Pattern: `("migrated from"|"selected Equinix Fabric"|"moved to Megaport") AND previous_provider IN Colo_target_list`. Confidence: MED.

### C-C4. Tenant RFP Leak / Procurement Portal Post

RFPs mentioning "cross-connect SLA," "virtual cross-connect," or "self-service portal" = tenant forcing the conversation.

Source: SAM.gov (federal), state procurement portals, RFPDB, LinkedIn tenant posts.

Pattern: `(RFP|RFQ|tender) AND (colocation|colo) AND ("cross-connect SLA"|"virtual cross-connect"|"self-service"|"portal provisioning")`. Confidence: MED-HIGH when it hits.

### C-C5. Modular / Edge Pod Deployment at New Power Site

Nodiac-type operators adding pod #N+1 — fresh window between pod #1 and pod #2. Applies to `Modular - colo` sub-segment specifically.

Pattern: `(modular|containerized|edge pod|micro-data center) AND (deploys|commissions|online) AND (new site|partner power|renewable energy site)`. Confidence: HIGH for modular archetype accounts.

---

## Explicitly NOT Tracked (noise)

These are signals intentionally excluded from productionized scoring per the April 2026 refresh:

- **Uptime Tier Certification** (Tier III / Tier IV awards from Uptime Institute). Trailing indicator — certification lags design + build by 12-18 months, so the fabric decision has already been made. Useful for account qualification (confirms facility is mature enough to have MaiaEdge's target tenant profile), not as a buying trigger.
- **Conference speaking slots alone** (`C-B4`). Useful as context for a deal already open on another signal. On its own it's marketing, not intent. Never surface an account solely on conference-slot signal.
- **Generic press releases** (SOC 2, ISO 27001, regional expansion into already-owned markets). Too common, too lagging, too weak on intent.
- **LinkedIn posts about "AI-ready data centers"** without tenant or build specifics. Brand positioning, not procurement signal.

---

## Sources for This Segment (scrape weekly — Phase 2 expanded 2026-04-27)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework.

### Robust tier (single-source can score at HIGH for non-major signals)

1. Data Center Frontier RSS — Site Selection, Energy, Colocation, Edge tags + **DCF People column** [Robust]
2. Data Center Dynamics RSS — company tags + keyword feeds + **DCD Careers tag + DCD People column** [Robust]
3. SEC EDGAR full-text — public Colo REITs (DLR, EQIX, IRM, DBRG); 8-K Items 1.01 / 2.01 / 5.02; S-4 (M&A) [Robust]
4. PR Newswire + Business Wire — Data Center feed + Appointments tag [Robust]
5. LinkedIn public posts + Greenhouse + Lever + Ashby — public job posts and exec posts at target accounts (C-A4 + C-A5) [Robust]
6. Apollo MCP — `apollo_organizations_enrich`, Job Postings filter, Job Changes filter (covers AP-1, AP-2, AP-7) [Robust]
7. Bisnow Data Center daily news — both national + Bisnow Local DC for project announcements [Robust]
8. Data Center Knowledge — coverage overlap with DCD/DCF; weekly diff [Robust]

### Medium tier (cross-source confirm preferred for major M&A / anchor-tenant claims)

9. PTC + Capacity Latin America + ITW + AfricaCom + Datacloud + AI Infrastructure Summit — agenda scrapers (exec speaker lists) [Medium]
10. AFCOM (Association For Computer Operations Management) news + 7x24 Exchange chapter announcements [Medium]
11. State economic development press: TX Comptroller / NC Dept of Commerce / VA EDC (Economic Development) / IA Economic Development Authority / AZ Commerce Authority / OH Department of Development — DC project announcements often appear here BEFORE trade press [Medium]
12. Local business journals — Atlanta Business Chronicle / Phoenix Business Journal / Dallas Morning News business / Richmond Times-Dispatch / Columbus Dispatch / Quad-City Times — for permit + construction announcements [Medium]
13. ISO interconnection queue reports beyond PJM/ERCOT/MISO/CAISO: SPP (Southwest Power Pool), NYISO, ISO-NE [Medium]
14. Crunchbase News — Data Center tag (free tier; Pro adds Funding events) [Medium]
15. Mighty Penguin DC newsletter [Medium]
16. Hyperscaler announcement feeds — AWS What's New / Azure announcements / Google Cloud blog — for "new region" / "expansion" / "new availability zone" → maps to anchor tenant signals [Medium]

### Aspirational tier (never standalone for major signals — require Robust or Medium cross-source confirmation)

17. **County permitting portals** — S2 greenfield (priority metros: NoVA, Dallas, Phoenix, Atlanta, Hillsboro/OR, Columbus/OH, Richmond/VA, Reno/NV, Quincy/WA, Council Bluffs/IA). Many are PDF-only or require captcha — log ✗ if unreachable [Aspirational]
18. **Electric utility interconnection queues** — Dominion, ERCOT, AEP, NV Energy, SCE, PG&E, Hydro Quebec, EirGrid (Ireland) — varying tech, some PDF-only [Aspirational]
19. **Reddit r/datacenter** — ground-truth project discussion; useful for confirming an announcement vs hype [Aspirational]
20. **Wayback Machine month-over-month diffs** of target colo websites — new tenant logos, new capacity numbers, new sub-segment positioning (AI / liquid cooling / sovereign) [Aspirational]
21. **Glassdoor reviews** — engineer reviews mentioning current tech stack / cooling / network upgrades at target accounts [Aspirational]
22. **Cross-segment exec hire stack** (see `signal-framework.md`): SEC 8-K 5.02, PR Newswire Appointments, company IR RSS, Crunchbase Exec Moves, TheOrg diffs — covers C-A4 [tier per source within stack]
23. **Public job-post scrape** (Indeed + Glassdoor) at target colo employers — covers C-A5 hiring spike [Aspirational unless via Greenhouse/Lever]

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **C-A0 / C-A1 greenfield S2/S3 (permit + utility)** | Planning docket filing [Aspirational] confirmed by ≥1 trade press [Robust] OR utility queue filing [Aspirational] confirmed by ≥1 trade press [Robust]. Single Aspirational alone → MEDIUM |
| **C-A2 GPU tenant anchor** | Counterparty named in press (Lambda / Crusoe / Nebius / Nscale / Together AI / Fluidstack / Vultr / RunPod). "Unnamed tenant" → MEDIUM unless inferable from context |
| **C-A3 liquid cooling deployment** | Tied to a specific named facility. Marketing blog without facility name → EXCLUDE (per signal-framework False Positive Patterns) |
| **C-A4 interconnection exec hire** | LinkedIn profile change [Robust] + (PR Newswire Appointments [Robust] OR SEC 8-K Item 5.02 [Robust] OR company IR press). Single source → MEDIUM |
| **C-A5 net-eng hiring spike (3+ in 30d)** | Confirmed via Greenhouse/Lever/Ashby [Robust] for the target operator. LinkedIn-public-only → MEDIUM |
| **C-A6 anchor tenant signing** | SEC 8-K Item 1.01 [Robust] + tenant's own announcement OR 2 trade press [Robust] with named counterparty. SEC alone with named tenant → HIGH |
| **C-A7 M&A / PE recap (announcement)** | SEC 8-K Item 1.01 OR S-4 [Robust] + ≥1 trade press OR 2 independent trade press [Robust]. Single trade press → MEDIUM |
| **C-A7 M&A / PE recap (close)** | SEC 8-K Item 2.01 [Robust] + ≥1 trade press OR 2 independent trade press [Robust] |

### International Sources (Tim Z's territory)

See `signal-framework.md` "International Source Stack" for the full regional stack. Colo-specific international priorities:

- **EMEA:** DCD EMEA tag, Data Centre Review, EUDCA releases, CBRE + Cushman EMEA DC reports, UK Planning Inspectorate + Dutch RVO + Irish An Bord Pleanála (S2 greenfield), ENTSO-E + TenneT / National Grid ESO / RTE / Red Eléctrica / Terna (S3 greenfield). Key operators: Atos, Data4, NorthC, Nikhef, Telehouse, Maincubes, Global Switch, Digital Realty EMEA, Equinix EMEA.
- **APAC:** DataCenterNews Asia Pacific, W.Media, DCD APAC tag, Capacity Asia, Structure Research APAC. Grid: AEMO Scorecard (AU), OCCTO (JP), EMA (SG). Key operators: AirTrunk, NEXTDC, STT GDC, ST Telemedia, Bridge Data Centres, GDS.
- **LATAM:** BNamericas LatAm Datacenters Watch (headlines), DCD LATAM, Teletime (BR), TeleSemana. Grid: ONS Brazil, CFE Mexico, CEN Chile.
- **MENA:** Capacity MENA, Commsmea, Zawya, AGBI, Intelligent CIO ME. Sovereign operators: HUMAIN, Center3, Tonomus (Saudi), G42 (UAE).

---

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A, website visitor tracking) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and are not duplicated in this file.
