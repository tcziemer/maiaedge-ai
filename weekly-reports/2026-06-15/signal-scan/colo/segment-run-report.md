# Signal Scan — Data Center Colo Provider — Segment Run Report

## 1. Run Header
- **Date (CT):** 2026-06-15 (Monday)
- **Segment:** Data Center Colo Provider
- **Detection window:** 2025-12-17 -> 2026-06-15 (180 days rolling, event-date basis)
- **Scope:** ALL tiers (no tier filter), non-Flagged, type != Customer, excl. MaiaEdge own (124293230301)
- **Apollo consumed:** 0 of 35 (interactive-confirm guardrail unavailable in scheduled run; 3 NEW accounts created from public web research per the 2026-06-08 NeoCloud precedent)
- **Runtime:** detection fanned out across 3 research sub-agents (context-budget safeguard); matched-account writes batched
- **MCPs used:** HubSpot (search + manage_crm_objects), Slack (canvas read), web_search/web_fetch; Apollo NOT invoked
- **Outcome:** 14 HubSpot writes (11 matched-account signal writes + 3 NEW-account creates); 0 failed. Active week — the 180-day window plus a busy early-June DC news cycle surfaced a wave of fresh buildouts, anchor leases, and M&A.

## 2. Source Coverage Table
Search-anchor attempts against the documented Colo Source Registry. ✓ = reachable / returned results (even if 0 actionable); ✗ = errored / unreachable / nothing returned.

| # | Source (tier) | Status | In-window actionable hits |
|---|---|---|---|
| 1 | Data Center Frontier (Robust) | ✓ | NTT DATA hyperscale-wins feature (115MW US leases); Aligned $40B (out of window). Lighter on pure colo news vs DCD |
| 2 | Data Center Dynamics (Robust) | ✓ | Highest yield: DartPoints Lexington, Ark/Nebius Longcross, Kao/Nebius Harlow, CyrusOne Freestone 380MW, STT GDC Jakarta, Digital Edge Seoul, Keppel Ansan, Lefdal Mine, DC North Croatia, DataVerge |
| 3 | Data Center Knowledge (Robust) | ✓ | June roundup: Prime SMF02 Sacramento, WhiteFiber/Nscale NC-1 (routed NeoCloud), Kasi Cloud Lagos |
| 4 | Bisnow Data Center (Robust) | ✓ | Centersquare $1B (out of window), DataBank securitization (capital-markets, excluded). No unique net-new |
| 5 | PR Newswire / Business Wire / GlobeNewswire (Robust) | ✓ | High yield: CyrusOne/Eolian, PowerHouse Arcola, DataBank x2, Flexential x2, DartPoints, atNorth x2; I Squared $1B platform via BW |
| 6 | StockTitan 8-K (DLR/EQIX/IRM/DBRG/COR) (Robust) | ✓ | IRM Q1 + DLR Q1 earnings language (both scored <8); EQIX/DLR in-window 8-Ks were capital-markets-only (excluded). COR (Switch) private — no public filings |
| 7 | SEC EDGAR full-text (Robust) | ✓ | Cogent 8-K Item 1.01 — sale of 10 DCs to I Squared affiliate (Cogent = Network Op; platform deferred, no named OpCo) |
| 8 | Greenhouse / Lever / Ashby job boards (Robust) | ✗ | Only a Cologix Director-of-Infrastructure (Lever, M-conf) surfaced — not a confirmed C-A4 Interconnection/Network/Fabric hire nor a 3+ C-A5 surge. ATS pages not web-indexed. **3-week ✗ streak -> Sources Needing Development** |
| 9 | Apollo MCP (Robust) | n/a | Not invoked (0 Apollo). Interactive-confirm guardrail unavailable in scheduled run; NEW accounts built from public research |
| 10 | Hyperscaler feeds AWS/Azure/GCP (Robust) | ✗ | AWS Chile region in-works but no named third-party colo anchor; no actionable colo-landlord angle. **3-week ✗ streak -> Sources Needing Development** |
| 11 | NVIDIA Newsroom / GTC (Robust) | ✗ | DGX-Ready Colo partner page = standing program (not a dated event); in-window NVIDIA names neoclouds (CoreWeave/Nscale/IREN), not colo landlords. Was ✓ last week |
| 12 | Crunchbase News (Medium) | ✗ | No disclosed colo equity rounds in window (DataBank $2B was construction debt, captured via wires). Was ✓ last week |
| 13 | Conference agendas PTC/Capacity/ITW/Datacloud/AI Infra (Medium) | ✓ | Context only (DCD Connect APAC Bali Jun 9-11; DCD Connect London). No standalone signal per noise list |
| 14 | AFCOM + 7x24 Exchange (Medium) | ✗ | Event calendars only (7x24 Fall San Antonio Oct; Data Center World Apr industry-level) |
| 15 | Mighty Penguin DC newsletter (Medium) | ✗ | Not retrievable / no indexed in-window issue |
| 16 | Cross-segment exec-hire stack (Medium) | ✓ | Reviewed StockTitan 5.02 + PRN Appointments — zero qualifying C-A4 Interconnection/Network/Fabric hires |
| Intl | DCD EMEA/APAC/LATAM, Capacity, Data Centre Review, BNamericas, Zawya, AGBI | ✓ | STT GDC (Jakarta), Digital Edge + Keppel (Seoul), Lefdal (Norway), Ark (UK), DC North (Croatia). BNamericas LatAm (KIO/IFX/Telsur) lacked dated-event granularity — deferred |

**3-week ✗ streak (actioned):** Sources #8 (Greenhouse/Lever/Ashby job boards) and #10 (hyperscaler region feeds) are now at **3 consecutive ✗** (✗ on 2026-06-01, 2026-06-08, 2026-06-15). Flagging both as **"Sources Needing Development"** for Cooper via the aggregator. #11 NVIDIA and #12 Crunchbase regressed to ✗ this week (1-week, were ✓ on 06-08) — watch, not yet a streak.

## 3. Candidate Funnel
| Stage | Count |
|---|---|
| Target list size (Colo, all tiers, type != Customer, excl. MaiaEdge own) | ~470 active (471 total minus 1 type=Customer) |
| Tier 3 canvas carryovers added | 0 (no live Colo signal-scan hold in F0B0AFSB9LN) |
| Detected raw candidates (3 sub-agents) | ~30 |
| In-scope Colo candidates after routing/exclusions | 16 |
| Matched to existing account + written | 11 |
| NEW accounts created | 3 (Apollo 0) |
| **Total HubSpot writes** | **14** |
| Skipped — anti-churn (stored newer/higher) | 2 (NTT DATA, QTS) + Equinix/DataBank/Digital Realty (no newer event detected) |
| Dropped — routed to NeoCloud (BTC-heritage, Op Principle 9) | WhiteFiber (+ IREN, Applied Digital, Hut 8, Bitzero, Cipher, Core Scientific noted by sub-agents) |
| Dropped — below score floor (<8) | 2 (DataVerge 6; Iron Mountain Q1 earnings 4) |
| Dropped — out of window (>180d) | 2 (Aligned $40B 2025-10-16; Centersquare $1B 2025-10-07) |
| Dropped — capital-markets-only | DataBank securitization, DLR ATM equity, EQIX senior notes, DBRG SoftBank buyout |
| Deferred — no named operating entity | 1 (I Squared $1B US AI-inference/edge colo platform; revisit when OpCo named) |
| Dropped — not Colo segment | Cogent (Network Operator) |

## 4. Score Distribution
| Bucket | Count |
|---|---|
| 27+ (Highest) | 11 (CyrusOne, atNorth, Kao Data, Digital Edge, Flexential, DartPoints, Prime, Keppel, STT GDC, Ark, Kasi Cloud) |
| 18-26 (Strong) | 1 (DC North 18) |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 2 (PowerHouse 9, Lefdal 9) |
| <8 (silent drop, log only) | 2 (DataVerge 6, Iron Mountain 4) |

## 5. Writes Summary
14/14 succeeded (manage_crm_objects: matched batch 10/10, PowerHouse 1/1, creates 3/3; 0 failed). `last_enriched_date` bumped ONLY on the 3 NEW creates (full pipeline ran); matched writes are partial signal writes (no bump). sc30 = 1 unless event >30d (Prime, PowerHouse, Lefdal = 0).

### Matched-account writes (11)
| id | Name | Code | Event date | Score | Heat prior -> new | Tier |
|---|---|---|---|---|---|---|
| 254558124749 | CyrusOne | U3 (Freestone 380MW groundbreak) | 2026-06-04 | 27 | Hot -> Hot (open deal DFW1 POC) | tier_1 (write SKIPPED: hs_is_target_account=true) |
| 267092339390 | atNorth | C-A1 (NOR01 Norway 120MW) | 2026-06-03 | 27 | Cool -> **Warm** | tier_1 (write SKIPPED: hs_is_target_account=true) |
| 302015231719 | Kao Data | C-A6 (Nebius 22MW Harlow) | 2026-06-08 | 27 | Cold -> **Warm** | tier_1 (unchanged; AI Signals - colo default T1) |
| 251533417160 | Digital Edge | U3 (Seoul SEL5 60MW) | 2026-06-08 | 27 | Cold -> **Warm** | tier_2 (write SKIPPED: hs_is_target_account=true) |
| 193906531042 | Flexential | C-A1 (Hillsboro 4+5 acq) | 2026-05-28 | 27 | Cold -> **Warm** | tier_1 (write SKIPPED: hs_is_target_account=true) |
| 193863998196 | DartPoints | C-A7 (Lexington acq) | 2026-05-27 | 27 | Cold -> **Warm** | tier_1 (unchanged; Modular - colo default T1) |
| 254541933251 | Prime Data Centers | U3 (SMF02 Sacramento) | 2026-05-07 | 27 | Cold -> **Warm** | tier_1 (unchanged; Hyperscale Wholesale default T1) |
| 302063896300 | Keppel Data Centres | U3 (Ansan Seoul 60MW) | 2026-06-09 | 27 | Cold -> **Warm** | tier_1 (unchanged; AI Signals - colo default T1) |
| 302188131053 | ST Telemedia GDC | U3 (Jakarta 2/3/5/6) | 2026-06-11 | 27 | Cold -> **Warm** | tier_1 (unchanged; AI Signals - colo default T1) |
| 103770391285 | Ark Data Centers | C-A6/U3 (Longcross 36MW + Nebius) | 2026-06-09 | 27 | Cold -> **Warm** | tier_3 -> **tier_2** (Standard - colo T3, hot signal -1) |
| 303312798423 | PowerHouse Data Centers | C-A6 (Arcola hyperscale lease) | 2026-01-15 | 9 | Cold -> **Cool** | tier_1 (write SKIPPED: hs_is_target_account=true) |

### NEW-account creates (3) — last_enriched_date stamped 2026-06-15
| id | Name | Segment / Sub-segment | Code | Event date | Score | Heat | Tier | Owner |
|---|---|---|---|---|---|---|---|---|
| 327581198017 | Kasi Cloud Datacenters | Data Center Colo Provider / Standard - colo | U3/C-B5 (LOS1 Lagos commissioned) | 2026-05-19 | 27 | Warm | tier_2 (T3, hot -1) | 159350430 (Tim Z, Nigeria=Intl) |
| 327599085257 | DC North | Data Center Colo Provider / Standard - colo | C-A7 (Gnomon PE acquisition) | 2026-05-27 | 18 | Cool | tier_3 (T3 default) | 159350430 (Tim Z, Croatia=Intl) |
| 327599216356 | Lefdal Mine Datacenter | Data Center Colo Provider / Standard - colo | C-A7 (3i majority stake) | 2026-03-11 | 9 | Cool | tier_4 (T3, stale +1) | 159350430 (Tim Z, Norway=Intl) |

**Narratives written (pure prose, no date prefix, no em dash, no MaiaEdge-competitor brand):**
- CyrusOne: "Broke ground on a 380MW data center campus in Freestone County, Texas, co-located with a Calpine natural gas plant, and signed a second 380MW agreement, marking a major Texas capacity expansion."
- atNorth: "Acquired land for its NOR01 mega-site in Haugaland, Norway, with 120MW initial capacity scaling to 350MW, completing its Nordic country footprint following a recent $4B take-private agreement."
- Kao Data: "Signed a 10-year, 22MW capacity agreement with AI cloud platform Nebius at its Harlow campus in the UK, anchoring continued high-density colocation demand."
- Digital Edge: "Acquired a fully powered 60MW site (SEL5) in Ansan, greater Seoul, with a 90MVA power agreement and dual 154kV feed, expanding to a fifth South Korea facility built for liquid-cooled AI workloads."
- Flexential: "Acquired two Hillsboro, Oregon data centers (Hillsboro 4 at 18MW and Hillsboro 5 at 36MW, 496k sq ft), its largest real estate transaction, shifting from leased to owned capacity."
- DartPoints: "Acquired a 343k sq ft, 29.5-acre data center campus in Lexington, Kentucky with an on-site substation, backed by over $250M in committed capital to serve AI, neocloud, and hyperscale demand."
- Prime Data Centers: "Broke ground on SMF02, the second building on its Sacramento campus, adding 150k sq ft and 18MW of critical IT capacity to meet regional wholesale demand."
- Keppel Data Centres: "Secured land in Ansan, greater Seoul for a 60MW Tier III facility, with construction permits and power approvals in hand, marking its entry into the South Korea market."
- ST Telemedia GDC: "Launched Jakarta 2 (24MW), topped out Jakarta 3, and broke ground on Jakarta 5 and 6 (40MW each), backed by $500M in green financing toward a 360MW Indonesia campus target."
- Ark Data Centers: "Committed 807M GBP to add a 36MW building at its Longcross campus near London after AI cloud platform Nebius expanded its lease to take the existing facility."
- PowerHouse Data Centers: "Executed a long-term hyperscale lease at its PowerHouse Arcola campus in Loudoun County, Virginia, advancing its Northern Virginia expansion."
- Kasi Cloud (new): "Commissioned its LOS1 campus in Lekki, Lagos, positioned as West Africa's first hyperscale-ready, carrier-neutral, AI-capable colocation facility targeting up to 100MW."
- DC North (new): "Acquired in full by private equity firm Gnomon Capital, which took 100 percent of Croatia's largest carrier-neutral data center in Varazdin, sited where three optical crossroads link Slovenia, Hungary, and Austria."
- Lefdal Mine (new): "3i Infrastructure agreed to acquire a majority stake valued near 300M EUR, backing 37MW of operational capacity plus 43MW under construction at the underground Norway facility, with the deal completing summer 2026."

## 6. Tier 3 Holds
- **Came in:** 0 (no live Colo signal-scan Tier 3 carryover in canvas F0B0AFSB9LN — confirmed by grep; the 06-08 Digi Power X hold was resolved/re-routed to NeoCloud).
- **New Tier 3 holds created this run:** 0 (every candidate was written, anti-churn-skipped, routed to NeoCloud, deferred, or dropped below floor — none parked as manual_review).
- **Net canvas action:** nothing re-appended to F0B0AFSB9LN.

## 7. QA Gate Drops / Skips
- **NTT DATA (208857135824)** — anti-churn SKIP. Detected 115MW hyperscaler leases event 2026-03-03; stored last_signal_date 2026-04-20 is NEWER. Do not overwrite a newer stored signal with an older detection.
- **QTS Realty (251536944853)** — SKIP. A Richmond VA expansion permit filing (2026-06-12) was flagged by a sub-agent but had no verified primary URL (QA rule 1 fail) and is lower materiality than the stored Van Wert $10B mega-campus (score 27, written 2026-05-29, still fresh/Warm). Keeping the stronger stored signal.
- **DataVerge** — DROP, score 6 (<8). Brooklyn carrier-neutral MMR + 3MW expansion + small Mathpix B300 tenant. Mathpix is not on the C-A2 GPU-cloud anchor list; best-firing code C-C2 Tier C scored below floor. On-thesis (carrier-neutral interconnection) but does not clear the floor; not created.
- **Iron Mountain** — DROP, Q1 earnings-language (C-B1) scored 4 (<8).
- **WhiteFiber (Nscale 40MW NC-1)** — routed to NeoCloud (Bit Digital crypto heritage; Bit Digital already classified NeoCloud Crypto-to-AI by R1 on 2026-06-09). Per Operating Principle 9, crypto-heritage AI-pivot routes to NeoCloud regardless of operator/landlord model. NOT scored as Colo.
- **Cogent / I Squared $1B platform** — deferred (no named operating entity yet); Cogent itself is Network Operator. Revisit when the platform OpCo is named.
- **Aligned ($40B), Centersquare ($1B)** — out of window (Oct 2025).

## 8. Failed Writes
None. 14/14 succeeded across 3 batches (matched 10/10, PowerHouse 1/1, creates 3/3).

## 9. Apollo Budget Post-Run
- Credits consumed this run: **0** (no apollo_organizations_enrich calls; the Apollo MANDATORY-CONFIRMATION guardrail cannot be satisfied in an unattended scheduled run, so the 3 NEW accounts were created from public web research per the 2026-06-08 NeoCloud precedent).
- Sub-cap: 35/run. Used 0 of 35.
- Weekly W24 (2026-W24, pre-rollover): 0/850 before -> 0/850 after. R1 (10am) owns the W24->W25 rollover; this 8:30am scan reads+appends under W24 per the documented pattern.

---

## Routed to NeoCloud (flagged for the NeoCloud segment scan — NOT scored as Colo)
BTC-mining-heritage AI-pivot operators (Operating Principle 9 -> NC5):
| Entity | Event | Date | Note |
|---|---|---|---|
| WhiteFiber (whitefiber.com) | Nscale 10-yr, 40MW, ~$865M colocation anchor at NC-1, Madison NC | 2025-12-18 | Bit Digital subsidiary; Bit Digital classified NeoCloud Crypto-to-AI by R1 2026-06-09. NeoCloud scan should detect independently. |
| IREN, Applied Digital, Hut 8, Bitzero, Cipher, Core Scientific | Various 2026 AI-infra leases / campus builds | Q2 2026 | All BTC heritage -> NeoCloud. Surfaced by sub-agents; excluded from Colo. |

## Notes for Cooper / aggregator
- **Active week, 11 accounts at score 27.** The 180-day window plus a heavy early-June DC news cycle (CyrusOne Freestone 6/4, atNorth Norway 6/3, Kao 6/8, Digital Edge 6/8, Keppel 6/9, Ark 6/9, STT GDC 6/11) produced an unusually full Highest-Priority tier. All are confirmed Tier-A high-confidence events at Tier-1 operators.
- **Sources Needing Development (3-week ✗):** Greenhouse/Lever/Ashby ATS job boards (#8) and hyperscaler region feeds (#10). The C-A4/C-A5 hiring-signal path is effectively dark via public ATS indexing; consider an Apollo Job-Changes/Job-Postings pass (AP-1) to recover the exec-hire signal class, or a named-operator ATS list.
- **Ark Data Centers tier_3 -> tier_2** is the only tier movement this run (driven by the hot Longcross signal; not a target account). All other matched tiers were frozen (target accounts) or already at ceiling tier_1.
- **3 NEW international colos added** (Kasi Cloud / Nigeria, DC North / Croatia, Lefdal Mine / Norway) — all owned by Tim Z. Created from public research; D7/R2 can deepen the structured enriched fields (infrastructure_profile etc. set to sentinels). Lefdal sub-segment (Standard vs Hyperscale Wholesale) is a best-fit estimate at medium_7089 confidence.
- **Data-quality note:** "Digital Edge DC - Hong Kong, Hong Kong" (251533417160) carries a messy per-location name on what is the canonical digitaledgedc.com record; the Seoul corporate signal was written there. Possible R3/R6 name cleanup. CyrusOne (Ken/West) and Ark/Flexential (Ken/East-HQ operators) have owner/territory mismatches left untouched (R6 scope).

---
*End of segment run report. No rep DMs, no canvas Run log row, no Cooper run report sent — those are owned by signal-scan-aggregator at 2:30pm CT, which reads HubSpot (source of truth) for last_signal_date = today records.*
