# NeoCloud — Weekly Signal Catalog

For use by the `weekly-signal-scan` skill. Read alongside `signal-framework.md` and `segments/neocloud.md`.

HubSpot `customer_segment`: **NeoCloud**
Sub-segments: **Large Scale GPU**, **Tier 1 Inference**, **AI Infrastructure Providers**, **Sovereign AI Clouds**, **Crypto-to-AI**

**NeoCloud-specific note:** This segment decays fastest — most signals have 2-4 week windows before the connectivity project is scoped internally or defaulted to a vendor. Weekly cadence is mandatory.

---

## Tier A — Meeting-Ready Signals (1wk-30d window)

### N-A0. Greenfield Build — Stage S2/S3 (permit + utility + debt)

**Why:** Each new region = 6-week connectivity project. Detecting at permit stage buys 6-12 months of influence. Critical for NeoClouds because they lease colo space rather than own — debt + permit data gives earliest signal of site N+1.

**Stages:** Same S1-S5 framework as Colo — see `colocation-signals.md` for the full stage table.

**NeoCloud-specific add-ons:**
- GPU-backed debt raise naming "new region" or "site N" in 8-K or press → site build confirmed at financing
- NVIDIA Cloud Partner "regional expansion" press — NVIDIA announces before the neocloud does
- Crypto-to-AI site conversion filings (10-Q: former miner repositioning Texas/Wyoming/Iceland sites)

**Priority:** S2-S3 = +3 score bonus.

### N-A1. Site Count Transition — 1 → 2 Regions

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

**Watch list:** Series A/seed-stage neoclouds adding second region — Fluidstack, TensorWave, Sustainable Metal Cloud, PaleBlueDot, smaller Crusoe-tier entrants. Regional GPU providers going cross-region (US East → US West, or US → EU). Sovereign AI clouds adding second in-country site (HUMAIN, G42, Shakti, Nscale second DC).

**Freshness:** 90d. **Confidence:** HIGH.

### N-A2. New Facility / Region Launch (N→N+1)

**Why:** Every new facility = 6-week connectivity project starting that day. Week 1 is when they're still choosing carriers. Week 4 they're locked in.

**Source:** Data Center Frontier, DCD, The Register, company press RSS, IREN/Applied Digital/Hut 8 8-K filings.

**Pattern:** `("new facility"|"new site"|"go-live"|"expansion"|"phase 2"|"megawatts online") + company`

**Freshness:** 1wk (hottest first 14 days). **Confidence:** HIGH.

### N-A3. NVIDIA DGX Cloud Lepton / NCP / Exemplar Cloud Partner Announcement

**Why:** Lepton partners inherit NVIDIA's "real-time GPU health diagnostics + root-cause analysis" mandate — which requires cross-facility path visibility they don't have. Exemplar Clouds program explicitly requires resiliency/observability uplift.

**Source:** NVIDIA Newsroom, GTC keynote press, NVIDIA investor page.

**Pattern:** `"NVIDIA Cloud Partner"|"DGX Cloud Lepton"|"Exemplar Cloud"|"Blackwell allocation"|"GB200 partner"`

**Freshness:** 1wk. **Confidence:** HIGH — NVIDIA's own marketplace asks for what we sell.

### N-A4. Enterprise Customer Win (non-hyperscaler)

**Why:** The scaling-wall moment. First enterprise logo = onboarding pain hits in weeks. Hyperscaler customers didn't need network teams; enterprise customers do.

**Source:** Press releases, LinkedIn CRO/CEO posts, The Information, SemiAnalysis.

**Pattern:** `"selected by"|"partners with [Fortune 500]"|"chose [neocloud]"|"enterprise customer"` — exclude hyperscaler mentions (Microsoft, Meta, OpenAI, Anthropic).

**Freshness:** 1wk. **Confidence:** HIGH.

### N-A5. GPU-Backed Debt Raise / Credit Facility

**Why:** Debt = aggressive scaling with thin margins. Network downtime = checkpoint rollback = missed debt service. Recent A3-rated GPU-backed credit facilities set the template — every follow-on borrower carries the same existential network-quality pressure.

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

---

## Tier B — Strong Signals (30-90d window)

### N-B1. SEC Filing CapEx / Capacity Disclosure (public NeoClouds)

Quarterly 10-Qs/8-Ks reveal new-site spend, customer concentration, and risk-factor language exposing where network is a business-continuity worry.

Source: SEC EDGAR — CRWV, NBIS, APLD, IREN, HUT, CORZ, WULF.

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

Assembling a multi-fabric story — about to hit "single pane of glass" problem.

Source: DCD, Lightwave, Capacity Media, Equinix / Digital Realty / Aligned / QTS / EdgeConneX press.

Pattern: `"[neocloud] + partners with [colo/fiber]"` OR `"expands to [city]" + "[carrier]"` — flag any neocloud announcing 2+ colo partners in 90d. Confidence: MED-HIGH.

### N-B5. Blackwell / GB200 / GB300 Allocation Win

Allocation = new deployment = new deterministic path requirement. They fought for the allocation; network is giving it back.

Source: NVIDIA press, SemiAnalysis, The Information, company investor calls.

Pattern: `"Blackwell allocation"|"GB200"|"GB300"|"first to deploy" + company`. Confidence: HIGH.

---

## Tier C — Directional Signals (30-90d window)

### N-C1. Crypto-to-AI Pivot Filing

Bitcoin miners pivoting bring zero network reliability DNA. Tier 1 GPU tenants demand 99.99% uptime; crypto facilities rarely have it. CoinShares tracked $65B in AI/HPC contracts from miners by Oct 2025.

Source: WGMI ETF holdings monthly update, SEC 10-K pivot language, Hashrate Index, CoinShares reports.

Pattern: 10-K/10-Q `"HPC hosting"|"AI infrastructure"|"GPU tenant"` from Bitcoin miner filer. Watch list: Applied Digital, Galaxy Digital, Stronghold, Argo Blockchain, Mawson, Northern Data, Cathedra, Soluna. Confidence: MED-HIGH.

### N-C2. (Deprecated — see N-A11)

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

## Compound Signals — Triple-Firing Conditions

When stacked, meeting probability approaches certainty. Auto-elevate to score 18+:

- **Funding + network hiring spike + new facility** = enterprise-scaling wall hitting in real time
- **Debt raise + enterprise customer win** = existential margin pressure + first non-hyperscaler SLA
- **NVIDIA Lepton/Exemplar announcement + multi-colo partnership** = NVIDIA is forcing observability the customer hasn't yet scoped
- **Funding + greenfield S2-S3 permit + facility count = 1** = capital + site #2 + first-ever multi-site design (score 24+)

---

## Tier 1 Qualifier Filter

Per `segments/neocloud.md`: 5+ facilities, 100MW+ announced GPU capacity, enterprise growth plan referenced, active observability gap.

---

## Sources for This Segment (scrape weekly — Phase 2 expanded 2026-04-27)

**Reliability tier in [brackets]** per `signal-framework.md` → Source Reliability + Validation Framework. NeoCloud is the highest-velocity segment — broadest source coverage of any segment.

### Robust tier

1. Data Center Frontier + DCD + The Register RSS [Robust]
2. NVIDIA Newsroom + GTC press + **NVIDIA partner page (DGX Cloud Lepton, NCP, Exemplar Cloud)** [Robust — NVIDIA announces NeoCloud partner deals before the NeoCloud does]
3. SEC EDGAR daily — public NeoCloud filers (Crusoe public filings, Applied Digital, Hut 8, Core Scientific, IREN, Bitfarms); 8-K Items 1.01 (anchor tenant + colo lease) / 2.03 (debt) / 5.02 (officer change); **S-1 / 424 (IPO and follow-on filings)**; **Form D (Reg D private placements — common for NeoCloud Series B+)** [Robust]
4. **PeeringDB API** — weekly diff on target ASN list (N-A9) [Robust]
5. **IX member-list pages** — DE-CIX, AMS-IX, LINX, Equinix IX, SIX, Any2, plus **AMS-IX Asia, NetIX, AfricaIX** for international (N-A10) [Robust]
6. **MLCommons MLPerf** Inference + Training submission feeds (N-A11) [Robust]
7. LinkedIn public posts + Greenhouse + Lever + Ashby — public job posts and exec posts at target NeoClouds (N-A6 hiring spike) [Robust]
8. Apollo MCP — `apollo_organizations_enrich`, Job Postings, Job Changes, Funding events (covers AP-1, AP-2, AP-7) [Robust]
9. **HPCwire** + **AnandTech AI/HPC** + **The Next Platform** + **ServeTheHome** — technical confirmations of new GPU regions, deployment scale [Robust]
10. Crunchbase News — TechCrunch + SiliconANGLE; AI Infrastructure tag, Cloud Computing tag [Robust]
11. PR Newswire / Business Wire — AI / Cloud Computing feed + Appointments tag [Robust]

### Medium tier

12. **The Information** — paywalled but headlines available; GPU economy newsletter coverage [Medium]
13. **Compute Forecast newsletter** — independent GPU economy tracker [Medium]
14. **Latent Space newsletter / podcast** (Swyx) — frequent NeoCloud deep-dives [Medium]
15. **Last Week in AI newsletter** (Andrey Kurenkov, Sharon Zhou) — weekly AI infra digest [Medium]
16. **Import AI newsletter** (Jack Clark) [Medium]
17. **AI Index (Stanford HAI)** — annual + interim deal trackers [Medium]
18. SemiAnalysis (Dylan Patel) — insider deployment news + datacenter coverage; mostly paywalled but headlines accessible [Medium]
19. Per-NeoCloud blog feeds — Crusoe, Lambda, CoreWeave, Together, Anyscale, Modal, RunPod, Vultr, Fluidstack, Nebius, Nscale, Voltage Park, Applied Digital, Hut 8, Core Scientific [Medium where RSS available; Aspirational where JS-rendered]
20. **Hugging Face Spaces** partner announcements — model providers naming their NeoCloud infra partners [Medium]
21. WGMI ETF holdings + Hashrate Index — crypto-to-AI sub-segment [Medium]
22. Moody's / DBRS / CoinDesk — debt raises; NeoCloud GPU-backed lending coverage [Medium]
23. AI Infrastructure Summit + NVIDIA GTC + **GTC AI Conference + Open Compute Summit** — conference agenda scrapers (context only — conference talks alone are not a buying signal) [Medium]

### Aspirational tier (never standalone for major signals)

24. Reddit r/LocalLLaMA + r/MachineLearning + r/datasets — ground-truth on NeoCloud reliability and outages [Aspirational]
25. **Glassdoor reviews** — engineer reviews mentioning current GPU stack / network architecture / scale challenges at target NeoClouds [Aspirational]
26. Wayback Machine month-over-month diffs of NeoCloud websites — new GPUs listed (H100 → H200 → B200), new regions, new sub-segment positioning (sovereign, inference, training) [Aspirational]
27. YouTube transcripts from NVIDIA GTC + AI Infrastructure Summit + KubeCon AI day [Aspirational]
28. Provider status pages + HackerNews — outages (context only, per N-C3 demotion note — outages alone are not a buy signal at NeoClouds; the network-quality buying conversation is too compressed and we don't want "you had an outage, here's our pitch") [Aspirational]
29. Cross-segment exec hire stack (see `signal-framework.md`): Apollo + Crunchbase Exec Moves + PR Newswire Appointments + TheOrg + SemiAnalysis + The Information — covers N-C5 [tier per source within stack]

### International (Tim Z's territory — sovereign AI is the hot zone)

See `signal-framework.md` "International Source Stack" for full detail. NeoCloud internationally is dominated by sovereign AI programs.

- **EMEA:** EuroHPC JU AI Factory awards (13 awarded to date — each is a neocloud-adjacent buildout) [Robust], Gaia-X Federation releases [Medium], EURO-3C project updates (Telefónica-led, 70+ orgs) [Medium], IPCEI on Next-Gen Cloud press [Medium], UK AI Research Resource (AIRR) + Isambard-AI announcements [Robust], Bpifrance France 2030 AI compute grants [Robust]. Key neoclouds: Nebius, Nscale, Scaleway, Northern Data, Gcore, Ori, Nexgen Cloud, Atlas Cloud.
- **APAC:** IndiaAI program releases (~62k GPUs deployed as of Mar 2026) [Robust], Japan IOWN Global Forum (NTT) [Medium], METI Japan AI cloud grants [Robust], MeitY India [Robust], Singapore AI Strategy 2.0 [Robust], KISA Korea [Medium], NSTDA Thailand [Medium]. Key neoclouds: Shakti, Yotta (IN), Sustainable Metal Cloud (SG).
- **MENA:** HUMAIN press (KSA) [Medium], G42 press (UAE) [Medium], MGX fund announcements [Medium], SDAIA releases [Robust], Zawya + AGBI wires [Medium].
- **I-series signals:** I2 Sovereign AI Compute Grants = core NeoCloud international signal. +3 score bonus applies.

**EuroHPC AI Factory award = greenfield-equivalent event for EU neoclouds.** Detection at award stage gives 6-18 months before GPU cluster comes online — same outreach timing as BEAD for fiber.

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

### International Sources (Tim Z's territory — sovereign AI is the hot zone)

See `signal-framework.md` "International Source Stack" for full detail. NeoCloud internationally is dominated by sovereign AI programs.

- **EMEA:** EuroHPC JU AI Factory awards (13 awarded to date — each is a neocloud-adjacent buildout), Gaia-X Federation releases, EURO-3C project updates (Telefónica-led, 70+ orgs), IPCEI on Next-Gen Cloud press, UK AI Research Resource (AIRR) + Isambard-AI announcements, Bpifrance France 2030 AI compute grants. Key neoclouds: Nebius, Nscale, Scaleway, Northern Data, Gcore, Ori, Nexgen Cloud, Atlas Cloud.
- **APAC:** IndiaAI program releases (~62k GPUs deployed as of Mar 2026), Japan IOWN Global Forum (NTT), METI Japan AI cloud grants, MeitY India, Singapore AI Strategy 2.0, KISA Korea, NSTDA Thailand. Key neoclouds: Shakti, Yotta (IN), Sustainable Metal Cloud (SG).
- **MENA:** HUMAIN press (KSA), G42 press (UAE), MGX fund announcements, SDAIA releases, Zawya + AGBI wires.
- **I-series signals:** I2 Sovereign AI Compute Grants = core NeoCloud international signal. +3 score bonus applies.

**EuroHPC AI Factory award = greenfield-equivalent event for EU neoclouds.** Detection at award stage gives 6-18 months before GPU cluster comes online — same outreach timing as BEAD for fiber.
