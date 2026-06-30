# NeoCloud - Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` and `segments/neocloud.md`.

HubSpot `customer_segment`: **NeoCloud**
Sub-segments (5 active + 1 cross-segment, case-sensitive, verified 2026-05-14): **Large Scale GPU - Neocloud**, **Tier 1 Inference - Neocloud**, **AI Infrastructure providers - Neocloud** (lowercase "p"), **Sovereign AI Clouds - Neocloud**, **Crypto to AI - Neoclouds** (trailing "s"; INCLUSIVE of operator AND landlord per Cooper 2026-05-14). Cross-segment: **Greenfield** (pre-operational; pairs with Data Center Colo Provider OR NeoCloud parent). See `context/account-tiering/sub-segment-qualification.md` for the full 30-value reference.

**NeoCloud-specific note:** This segment decays fastest - most signals have 2-4 week windows before the connectivity project is scoped internally or defaulted to a vendor. Weekly cadence is mandatory.

---

## Tier A - Meeting-Ready Signals (1wk-30d window)

### N-A0. Greenfield Build - Stage S2/S3 (permit + utility + debt)

**Why:** Each new region = 6-week connectivity project. Detecting at permit stage buys 6-12 months of influence. Critical for NeoClouds because they lease colo space rather than own - debt + permit data gives earliest signal of site N+1.

**Stages:** Same S1-S5 framework as Colo - see `colocation-signals.md` for the full stage table.

**NeoCloud-specific add-ons:**
- GPU-backed debt raise naming "new region" or "site N" in 8-K or press → site build confirmed at financing
- NVIDIA Cloud Partner "regional expansion" press - NVIDIA announces before the neocloud does
- Crypto-to-AI site conversion filings (10-Q: former miner repositioning Texas/Wyoming/Iceland sites)

**Priority:** S2-S3 = +3 score bonus.

### N-A1. Site Count Transition - 1 → 2 Regions

**Why:** First-ever multi-region design decision. Inference latency variance across regions is a brand-new problem they've never solved.

**Detection:**
```
IF scraped_signal = "new facility/region by [company]"
  AND parse_facility_count(HubSpot.account[company].infrastructure_profile) = 1
  THEN transition_type = "1→2" → +6 score bonus
  ELSE IF parse is low-confidence:
    skip bonus (fall back to base greenfield score)

Parse method: LLM reads the free-text infrastructure_profile field at match time.
After successful detection, rewrite infrastructure_profile with updated count + context.
```

**Watch list:** Series A/seed-stage neoclouds adding second region - Fluidstack, TensorWave, Sustainable Metal Cloud, PaleBlueDot, smaller Crusoe-tier entrants. Regional GPU providers going cross-region (US East → US West, or US → EU). Sovereign AI clouds adding second in-country site (HUMAIN, G42, Shakti, Nscale second DC).

**Freshness:** 90d. **Confidence:** HIGH.

### N-A2. New Facility / Region Launch (N→N+1)

**Why:** Every new facility = 6-week connectivity project starting that day. Week 1 is when they're still choosing carriers. Week 4 they're locked in.

**Source:** Data Center Frontier, DCD, The Register, company press RSS, IREN/Applied Digital/Hut 8 8-K filings.

**Pattern:** `("new facility"|"new site"|"go-live"|"expansion"|"phase 2"|"megawatts online") + company`

**Freshness:** 1wk (hottest first 14 days). **Confidence:** HIGH.

### N-A3. NVIDIA DGX Cloud Lepton / NCP / Exemplar Cloud Partner Announcement

**Why:** Lepton partners inherit NVIDIA's "real-time GPU health diagnostics + root-cause analysis" mandate - which requires cross-facility path visibility they don't have. Exemplar Clouds program explicitly requires resiliency/observability uplift.

**Source:** NVIDIA Newsroom, GTC keynote press, NVIDIA investor page.

**Pattern:** `"NVIDIA Cloud Partner"|"DGX Cloud Lepton"|"Exemplar Cloud"|"Blackwell allocation"|"GB200 partner"`

**Freshness:** 1wk. **Confidence:** HIGH - NVIDIA's own marketplace asks for what we sell.

### N-A4. Enterprise Customer Win (non-hyperscaler)

**Why:** The scaling-wall moment. First enterprise logo = onboarding pain hits in weeks. Hyperscaler customers didn't need network teams; enterprise customers do.

**Source:** Press releases, LinkedIn CRO/CEO posts, The Information, SemiAnalysis.

**Pattern:** `"selected by"|"partners with [Fortune 500]"|"chose [neocloud]"|"enterprise customer"` - exclude hyperscaler mentions (Microsoft, Meta, OpenAI, Anthropic).

**Freshness:** 1wk. **Confidence:** HIGH.

### N-A5. GPU-Backed Debt Raise / Credit Facility

**Why:** Debt = aggressive scaling with thin margins. Network downtime = checkpoint rollback = missed debt service. Recent A3-rated GPU-backed credit facilities set the template - every follow-on borrower carries the same existential network-quality pressure.

**Source:** Moody's / DBRS rating releases, SEC 8-K, CNBC, company IR, CoinDesk (for USD.AI-style on-chain facilities).

**Pattern:** `"GPU-backed"|"delayed draw term loan"|"asset-backed financing"|"SOFR +" AND "AI infrastructure"`

**Freshness:** 30d. **Confidence:** HIGH.

### N-A6. Network / SRE / Observability Hiring Spike

**Why:** They've realized they need this capability. Sell the platform before they hire a full team (6-9 months anyway).

**Source:** LinkedIn Jobs (target account filter), Greenhouse / Lever public boards.

**Pattern:** 3+ roles posted in 30d matching `"Network Engineer"|"Staff SRE"|"Network Reliability"|"WAN architect"|"NOC"|"network observability"` at a neocloud target. **First-ever network role = highest signal.**

**Freshness:** 30d. **Confidence:** HIGH.

### N-A7. Anchor Tenant Signing (enterprise or hyperscaler)

**Why:** Dual-sided with colo signal `C-A6`. When a neocloud announces a new anchor tenant (Microsoft, Meta, OpenAI, Anthropic, enterprise logo), both the neocloud and the colo hosting the workload enter buying windows simultaneously. Neocloud side: the anchor has hard SLA and multi-region path requirements the neocloud must deliver inside 30-90 days.

**Source:** SEC 8-K Item 1.01 / 7.01 on public neocloud filers (CRWV, NBIS, APLD, CORZ, IREN, HUT, WULF), press release wires, LinkedIn CEO/CRO posts, The Information, SemiAnalysis.

**Pattern:** `"signed"|"selected by"|"multi-year agreement with" + [Fortune 500 / hyperscaler] + neocloud`. Distinct from N-A4 in that anchor tenant implies a facility-anchoring commitment (10+ years, single-tenant-scale) rather than a generic enterprise customer win.

**Freshness:** 1wk. **Confidence:** HIGH.

### N-A8. Colo Lease Filing (SEC 8-K Item 1.01 / 2.03 material lease)

**Why:** Public neoclouds file material colocation leases within 4 business days of signing. Each filing names the colo counterparty + site + size → dual-sided meeting signal (neocloud procurement is live; colo is sourcing connectivity for the new tenant).

**Source:** SEC EDGAR daily feed filtered to neocloud CIKs.

**Pattern:** 8-K Item 1.01 or 2.03 containing `"lease"|"colocation"|"datacenter agreement"|"master services"` + counterparty identification.

**Freshness:** 1wk (filing is <4 business days from execution). **Confidence:** HIGH. Also surfaces corresponding colo account via `C-A6`.

### N-A9. PeeringDB Changes (new netixlan / netfac / prefix)

**Why:** PeeringDB is the public-record source of where a network announces itself and at which IXes / facilities. Changes = new site coming online, new region, new peering strategy. Cheap, unique signal  -  weekly API diff produces it.

**Source:** PeeringDB API (`/api/netixlan`, `/api/netfac`, `/api/ix` filtered by target ASN).

**Pattern:** Weekly diff on target-neocloud ASN list. New `netixlan` (new IX session) OR new `netfac` (new facility) OR new prefix announcement = trigger. Second/third ASN registration = regional segmentation or sovereign build.

**Freshness:** Real-time API; run diff weekly. **Confidence:** HIGH.

### N-A10. Internet Exchange Member Addition (100G/400G port)

**Why:** Appearing on a public IX member list (DE-CIX, AMS-IX, LINX, Equinix IX, SIX, Any2) with a 100G or 400G port is a public "open for peering" flag. Port-live date = they can take inbound paths today. Doesn't require PeeringDB to surface  -  IX member pages are directly scrapable.

**Source:** DE-CIX / AMS-IX / LINX / Equinix IX / SIX / Any2 member list pages.

**Pattern:** New target-neocloud ASN appearing on member list + port speed ≥ 100G. Pair with N-A9 for high confidence.

**Freshness:** Weekly. **Confidence:** HIGH.

### N-A11. MLPerf Inference / Training Submission

**Why:** Submitting to MLPerf means the neocloud has a production-stable fabric. Network division submissions explicitly benchmark end-to-end latency under load. First-time submission = they're ready to compete on token-latency SLAs, which is exactly the pain MaiaEdge addresses. Bi-annual cadence = immediate conversation opener the week of results.

**Source:** MLCommons results pages, HPCwire coverage, submitter blog posts.

**Pattern:** First-time submitter OR new category entry (inference vs. training) + target company.

**Freshness:** Bi-annual (Sept + March windows). **Confidence:** HIGH during results window, drops after 30d. **Promoted from Tier C to Tier A** in April 2026 signal refresh.

### N-A12. Private-AI / Model-Provider Partnership

**Why:** A deal to deliver a named foundation model (Gemini, Anthropic, Llama) as private or dedicated AI into regulated verticals (healthcare, financial services, government) means the neocloud just took on hard data-residency and interconnect requirements. The customer wants the model without putting data into the public cloud, which is exactly the data-sovereignty + path-control angle MaiaEdge sells. High intent: the partnership is announced because customers are already asking.

**Source:** Company press / blog, the model provider's partner page, regulated-vertical trade press, LinkedIn CEO/CRO posts.

**Pattern:** `("private AI"|"dedicated AI"|"sovereign inference") + ("Gemini"|"Anthropic"|"Claude"|"Llama"|named model) + neocloud` OR a named partnership to serve a regulated vertical.

**Freshness:** 30d. **Confidence:** HIGH. Pairs with the Sovereign-angle variant even for US neoclouds (lead DATA sovereignty, not jurisdiction).

---

## Tier B - Strong Signals (30-90d window)

### N-B1. SEC Filing CapEx / Capacity Disclosure (public NeoClouds)

Quarterly 10-Qs/8-Ks reveal new-site spend, customer concentration, and risk-factor language exposing where network is a business-continuity worry.

Source: SEC EDGAR - CRWV, NBIS, APLD, IREN, HUT, CORZ, WULF.

Pattern: 10-Q/8-K/S-1 containing `"customer concentration"|"network-dependent"|"service level agreement"|"data center interconnect"|"capex guidance"`. Confidence: HIGH.

### N-B2. Series B+ / Growth Equity Funding Round

Scaling to enterprise = network-team hole. Capital in hand + 18-month spend timeline = scoping infrastructure now.

Source: Crunchbase News, PitchBook public pages, TechCrunch, SiliconANGLE, Yahoo Finance.

Pattern: `"Series B"|"Series C"|"growth round"|"valued at" + "GPU cloud"|"AI infrastructure"|"inference platform"|"neocloud"`. Confidence: HIGH.

### N-B3. Sovereign AI / Government Contract Win

Hard SLAs, audit requirements, in-country data-transit rules. Sovereign AI spend projected $100B+ in 2026. Argonne, HUMAIN, IndiaAI, Nscale contracts all generate meeting-worthy scopes.

Source: NVIDIA Global Public Sector page, government procurement feeds (SAM.gov, OJEU, TED), McKinsey Sovereign AI tracker.

Pattern: `"sovereign AI"|"national AI compute"|"Department of [X]"|"Ministry of [X]" + "awarded"|"selected" + GPU cloud`. Confidence: HIGH.

### N-B4. Multi-Carrier / Multi-Colo Partnership Press

Assembling a multi-fabric story - about to hit "single pane of glass" problem.

Source: DCD, Lightwave, Capacity Media, Equinix / Digital Realty / Aligned / QTS / EdgeConneX press.

Pattern: `"[neocloud] + partners with [colo/fiber]"` OR `"expands to [city]" + "[carrier]"` - flag any neocloud announcing 2+ colo partners in 90d. Confidence: MED-HIGH.

**Reactive variant (stronger intent):** A neocloud that diversified carriers AFTER a single-vendor networking failure (and bolted on a failover line) is in more acute pain than one proactively assembling a multi-fabric story. Signs: an exec or status history mentioning a single-carrier outage, a "we had to add two more carriers" account, or a sudden second/third transit provider on PeeringDB (N-A9) right after an incident. Treat as MED-HIGH even at a single site. Use as the angle-selector (lead with multi-carrier orchestration + auto-failover), never cite the specific outage in customer-facing copy.

### N-B5. Blackwell / GB200 / GB300 Allocation Win

Allocation = new deployment = new deterministic path requirement. They fought for the allocation; network is giving it back.

Source: NVIDIA press, SemiAnalysis, The Information, company investor calls.

Pattern: `"Blackwell allocation"|"GB200"|"GB300"|"first to deploy" + company`. Confidence: HIGH.

### N-B6. Builder-for-PE + Third-Party Monetization Partner

**Why:** A GPU-cluster builder that builds on behalf of private-equity asset owners and hands monetization to a separate partner (Hydra Host class) carries the per-customer networking-primitive burden (an ASN and IP block per customer) that the own-the-WAN consolidation pitch resolves directly. The PE owners and the monetization partner are each adjacent reachable entities, so one builder relationship opens a multi-thread.

**Source:** Company site / "how we work" pages, monetization-partner customer lists (Hydra Host and similar), PE infrastructure-fund announcements, LinkedIn (Infrastructure Lead / Head of Infrastructure titles).

**Pattern:** `("GPU as an asset class"|"build and operate"|"monetization partner"|"private equity" + "GPU"|"AI cluster") + builder`. Flag the monetization partner and the PE owner as separate accounts to associate.

**Freshness:** 90d. **Confidence:** MED-HIGH. Weight multi-site expansion intent highly: these builders are pre-federation by choice, not incapacity.

---

## Tier C - Directional Signals (30-90d window)

### N-C1. Crypto-to-AI Pivot Filing

Bitcoin miners pivoting bring zero network reliability DNA. Tier 1 GPU tenants demand 99.99% uptime; crypto facilities rarely have it. CoinShares tracked $65B in AI/HPC contracts from miners by Oct 2025.

Source: WGMI ETF holdings monthly update, SEC 10-K pivot language, Hashrate Index, CoinShares reports.

Pattern: 10-K/10-Q `"HPC hosting"|"AI infrastructure"|"GPU tenant"` from Bitcoin miner filer. Watch list: Applied Digital, Galaxy Digital, Stronghold, Argo Blockchain, Mawson, Northern Data, Cathedra, Soluna. Confidence: MED-HIGH.

### N-C2. (Deprecated - see N-A11)

MLPerf Inference submissions were promoted to Tier A (see N-A11) in the April 2026 refresh. Tier C placement is no longer accurate  -  results window gives 7-14 day high-intent outreach opportunity that warrants Tier A priority.

### N-C3. Public Outage / Status Page Incident / RCA

⚠️ **WEAK signal. Context-only.** Status-page incidents reveal pain but **do not indicate intent to buy**. Reactive, not forward-looking. Do NOT use as a sole trigger for outreach. Use only to inform *which angle to lead with* when a target already qualifies on another Tier A / Tier B signal  -  and even then, never cite the specific incident in customer-facing copy (the customer won't respond well to "I saw your status page was red last Tuesday"). Internal angle-selection guide only.

Source: Provider status pages, Twitter/X provider handles, HackerNews, Downdetector.

Pattern: Status page entry 2+ hours, keyword `"network"|"connectivity"|"latency"|"inter-region"` in post-mortem; HN thread with provider name. Confidence: MED-HIGH when RCA blames carrier/network; LOW when pure compute.

### N-C4. Inference-Focused Product Launch / Pricing

Shift from training-only to inference = adopting token-latency SLAs. Inference = 55% of AI spend now.

Source: Company blogs/changelogs, Product Hunt, DCD, The Register.

Pattern: `"inference endpoint"|"tokens/sec SLA"|"<100ms"|"serverless inference"|"dedicated inference" + neocloud`. Confidence: MED.

### N-C5. Executive Departure / Key Network-Role Hire

Departures of VP Infrastructure / Head of Networking / Chief Network Architect = 60-90 day replacement gap where a platform removing headcount dependency is compelling. Arrivals = will rebuild stack, often buying in.

Source: LinkedIn (job change alerts on target persona list), TheOrg, team page diffs.

Pattern: Departure/arrival at VP+ level in Infrastructure / Networking / Platform / SRE. Cross-reference against HubSpot contact list. Confidence: MED-HIGH for arrivals, HIGH for departures at sole-network-person companies.

---

## Compound Signals - Triple-Firing Conditions

When stacked, meeting probability approaches certainty. Auto-elevate to score 18+:

- **Funding + network hiring spike + new facility** = enterprise-scaling wall hitting in real time
- **Debt raise + enterprise customer win** = existential margin pressure + first non-hyperscaler SLA
- **NVIDIA Lepton/Exemplar announcement + multi-colo partnership** = NVIDIA is forcing observability the customer hasn't yet scoped
- **Funding + greenfield S2-S3 permit + facility count = 1** = capital + site #2 + first-ever multi-site design (score 24+)

---

## Tier 1 Qualifier Filter

Per `segments/neocloud.md`: 5+ facilities, 100MW+ announced GPU capacity, enterprise growth plan referenced, active observability gap.

---

## Sources for This Segment (scrape weekly - pruned 2026-05-11)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework. NeoCloud is the highest-velocity segment - broadest source coverage of any segment.

**Search-anchor pattern is the canonical access method** - direct `web_fetch` is gated by URL-provenance on Cowork's runtime. Anchor each source via `web_search "{domain} {topic} {year}"` and read snippets from search results. Article URLs returned in search can then be fetched directly. Do NOT skip a documented source because direct fetch fails - use search anchoring.

### Robust tier

1. Data Center Frontier + Data Center Dynamics + Data Center Knowledge + The Register data centre [Robust]
2. NVIDIA Newsroom + GTC press + **NVIDIA partner page (DGX Cloud Lepton, NCP, Exemplar Cloud)** [Robust - NVIDIA announces NeoCloud partner deals before the NeoCloud does]
3. **StockTitan** (SEC 8-K mirror with parsed summaries - `stocktitan.net/sec-filings/{ticker}/`) - primary surrogate for SEC EDGAR direct queries on public NeoCloud filers (CRWV, APLD, HUT, CORZ, IREN, BITF, MARA, WULF, CLSK, GLXY); covers 8-K Items 1.01 (anchor tenant + colo lease) / 2.03 (debt) / 5.02 + S-1 / 424 (IPO + follow-on) + Form D (Reg D private placements) [Robust]
4. SEC EDGAR full-text via search-anchor - backup to StockTitan; preferred for Form D and unusual filing types [Robust]
5. **Crypto-to-AI outlets - CoinDesk + Bitcoin Magazine + Cryptopolitan + news.bitcoin.com** - surface miner-to-AI pivot signals (MARA, Bitfarms, Hut 8, TeraWulf, Galaxy Digital, IREN, Core Scientific) 24-48 hours before mainstream trade press [Robust - promoted from Medium tier 2026-05-11 after consistent high yield on crypto-pivot signals]
6. **IX member-list pages** - DE-CIX, AMS-IX, LINX, Equinix IX, SIX, Any2, plus **AMS-IX Asia, NetIX, AfricaIX** for international (N-A10) [Robust]
7. Greenhouse + Lever + Ashby public job boards at target NeoClouds (N-A6 hiring spike) [Robust]
8. Apollo MCP - `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events (covers AP-1, AP-2, AP-7) - enrichment tool [Robust]
9. **HPCwire** + **The Next Platform** + **ServeTheHome** - technical confirmations of new GPU regions, deployment scale [Robust]
10. Crunchbase News - TechCrunch + SiliconANGLE; AI Infrastructure tag, Cloud Computing tag [Robust]
11. PR Newswire + Business Wire + GlobeNewswire - AI / Cloud Computing feed + Appointments tag [Robust]
12. Per-NeoCloud IR / newsroom pages - CoreWeave, Nebius, Applied Digital, Hut 8, Iris Energy (IREN), Marathon Digital, TeraWulf, Bitfarms (Keel), Galaxy Digital, Fluidstack, Lambda, Cerebras [Robust - IR newsrooms are highest-yield single-company source]

### Medium tier

13. **The Information** - paywalled but headlines + lede paragraphs surface in search snippets [Medium]
14. **SemiAnalysis** (Dylan Patel) - insider deployment news + datacenter coverage; mostly paywalled but headlines accessible [Medium]
15. **Compute Forecast newsletter** - independent GPU economy tracker [Medium]
16. **Latent Space newsletter / podcast** (Swyx) - frequent NeoCloud deep-dives [Medium]
17. **Last Week in AI newsletter** (Andrey Kurenkov, Sharon Zhou) - weekly AI infra digest [Medium]
18. **Import AI newsletter** (Jack Clark) [Medium]
19. **AI Index (Stanford HAI)** - annual + interim deal trackers [Medium]
20. **Hugging Face Spaces** partner announcements - model providers naming their NeoCloud infra partners [Medium]
21. WGMI ETF holdings + Hashrate Index - crypto-to-AI sub-segment context [Medium]
22. Moody's / DBRS / Fitch debt-rating notes - GPU-backed lending coverage (paywalled but headlines surface) [Medium]
23. AI Infrastructure Summit + NVIDIA GTC + Open Compute Summit - conference agenda scrapers (context only - conference talks alone are not a buying signal) [Medium]
24. **Cross-segment exec hire stack** (see `signal-framework.md`): StockTitan 8-K 5.02, PR Newswire Appointments, IR newsroom diffs, Crunchbase Exec Moves, SemiAnalysis + The Information headline scan [Medium]

### Excluded (do NOT scrape - cut 2026-05-11)

- **PeeringDB as a news source** - it's a structured database, not a news feed. Moved to `signal-framework.md` as an enrichment lookup tool (N-A9 still relies on it, but accessed at enrichment time, not weekly news cadence).
- **MLCommons MLPerf submission feeds** - wrong frequency. MLPerf rounds happen 3-4x/year. Moved to a separate quarterly batch task; not part of weekly scan.
- **AnandTech AI/HPC** - main site shut down August 2024. Forums only, low signal density. Replaced by The Next Platform + ServeTheHome.
- **Reddit r/LocalLLaMA + r/MachineLearning + r/datasets** - low signal density, unstructured.
- **Glassdoor reviews** - login-gated.
- **Wayback Machine month-over-month diffs** - theoretical, never run.
- **YouTube transcripts from GTC / AI Infrastructure Summit / KubeCon** - compute-expensive, redundant with trade-press coverage.
- **Provider status pages + HackerNews outage tracking** - per N-C3 demotion, outages alone are not a buy signal at NeoClouds.

LinkedIn public posts retained for **named-account research only** (specific company pages), not market-wide discovery - moved to `signal-framework.md`.

### International (Tim Z's territory - sovereign AI is the hot zone)

See `signal-framework.md` "International Source Stack" for full detail. NeoCloud internationally is dominated by sovereign AI programs.

- **EMEA:** EuroHPC JU AI Factory awards (13 awarded to date - each is a neocloud-adjacent buildout) [Robust], Gaia-X Federation releases [Medium], EURO-3C project updates (Telefónica-led, 70+ orgs) [Medium], IPCEI on Next-Gen Cloud press [Medium], UK AI Research Resource (AIRR) + Isambard-AI announcements [Robust], Bpifrance France 2030 AI compute grants [Robust]. Key neoclouds: Nebius, Nscale, Scaleway, Northern Data, Gcore, Ori, Nexgen Cloud, Atlas Cloud.
- **APAC:** IndiaAI program releases (~62k GPUs deployed as of Mar 2026) [Robust], Japan IOWN Global Forum (NTT) [Medium], METI Japan AI cloud grants [Robust], MeitY India [Robust], Singapore AI Strategy 2.0 [Robust], KISA Korea [Medium], NSTDA Thailand [Medium]. Key neoclouds: Shakti, Yotta (IN), Sustainable Metal Cloud (SG).
- **MENA:** HUMAIN press (KSA) [Medium], G42 press (UAE) [Medium], MGX fund announcements [Medium], SDAIA releases [Robust], Zawya + AGBI wires [Medium].
- **I-series signals:** I2 Sovereign AI Compute Grants = core NeoCloud international signal. +3 score bonus applies.

**EuroHPC AI Factory award = greenfield-equivalent event for EU neoclouds.** Detection at award stage gives 6-18 months before GPU cluster comes online - same outreach timing as BEAD for fiber.

### Validation patterns per Tier A signal

| Signal | Validation rule for HIGH confidence |
|---|---|
| **NC-A0 / NC-A1 greenfield S2/S3 + transition** | NeoClouds typically lease colo (don't own DC). Greenfield indicators: GPU-backed debt filing [Robust] + colo lease 8-K [Robust] OR NeoCloud announcement + at least one external confirmation (cloud blog or trade press) [Robust] |
| **NC-A2 new region launch** | NeoCloud's own announcement [Robust] + (PeeringDB diff [Robust] OR IX port addition [Robust] OR colo lease 8-K [Robust]). Single source → MEDIUM |
| **NC-A3 NVIDIA Lepton/NCP/Exemplar partner** | NVIDIA partner page entry [Robust] alone scores HIGH (NVIDIA wouldn't list non-existent partners) |
| **NC-A4 enterprise customer win** | NeoCloud + customer joint press [Robust] with specific named workload OR SEC 8-K material contract [Robust] |
| **NC-A5 GPU-backed debt** | SEC 8-K Item 2.03 [Robust] + ≥1 trade press [Robust] OR Moody's / DBRS rating action [Medium] + trade press [Robust] |
| **NC-A6 hiring spike (3+ in 30d)** | Greenhouse/Lever/Ashby [Robust] for the target NeoCloud showing 3+ concurrent network/SRE roles. LinkedIn-public-only → MEDIUM |
| **NC-A7 anchor tenant signing** | NeoCloud announcement [Robust] + named counterparty (Microsoft, Meta, OpenAI, Anthropic, named enterprise). "Unnamed major tech company" → MEDIUM |
| **NC-A8 colo lease filing** | SEC 8-K Item 1.01 [Robust] + lease counterparty named OR colo operator's own filing in tandem |
| **NC-A9 PeeringDB changes** | PeeringDB API diff [Robust] alone scores HIGH (it's the public-record source) |
| **NC-A10 IX port addition** | IX member-list page [Robust] alone scores HIGH |
| **NC-A11 MLPerf submission** | MLCommons submission listing [Robust] alone scores HIGH for the production-stable signal |

**Cross-segment signal infrastructure:** Apollo-native and other cross-segment platform signals (job changes, headcount, intent, funding M&A, website visitor tracking) are documented centrally in [universal-platform-signals.md](universal-platform-signals.md). Those signals apply here too and should not be duplicated in this file.

### International Sources (Tim Z's territory - sovereign AI is the hot zone)

See `signal-framework.md` "International Source Stack" for full detail. NeoCloud internationally is dominated by sovereign AI programs.

- **EMEA:** EuroHPC JU AI Factory awards (13 awarded to date - each is a neocloud-adjacent buildout), Gaia-X Federation releases, EURO-3C project updates (Telefónica-led, 70+ orgs), IPCEI on Next-Gen Cloud press, UK AI Research Resource (AIRR) + Isambard-AI announcements, Bpifrance France 2030 AI compute grants. Key neoclouds: Nebius, Nscale, Scaleway, Northern Data, Gcore, Ori, Nexgen Cloud, Atlas Cloud.
- **APAC:** IndiaAI program releases (~62k GPUs deployed as of Mar 2026), Japan IOWN Global Forum (NTT), METI Japan AI cloud grants, MeitY India, Singapore AI Strategy 2.0, KISA Korea, NSTDA Thailand. Key neoclouds: Shakti, Yotta (IN), Sustainable Metal Cloud (SG).
- **MENA:** HUMAIN press (KSA), G42 press (UAE), MGX fund announcements, SDAIA releases, Zawya + AGBI wires.
- **I-series signals:** I2 Sovereign AI Compute Grants = core NeoCloud international signal. +3 score bonus applies.

**EuroHPC AI Factory award = greenfield-equivalent event for EU neoclouds.** Detection at award stage gives 6-18 months before GPU cluster comes online - same outreach timing as BEAD for fiber.
