# Signal Scan — Network Operator — Segment Run Report

## 1. Run header

- **Date (CT):** 2026-06-15 (Monday)
- **Segment:** Network Operator (`customer_segment = "Network Operator(Tier 1 / VNO)"`)
- **Detection window:** 180-day rolling (event date on/after 2025-12-17).
- **Apollo consumed:** 0 of 50 (weekly pool W25: 2/850 at run start — Signal Scan Fiber spent 2 earlier today; effective budget min(50, 848) = 50). 0 NEW-account creation -> 0 Apollo.
- **Runtime:** ~16 min
- **MCPs:** HubSpot ✓, Apollo ✓ (available, unused), Slack ✓ (canvas read), web_search ✓, web_fetch ✓
- **Result:** 3 matched-account signal writes (DISH Network NO-A4 27/Warm; Sparkle NO-A4 18/Cool; Orange Group NO-B4 12/Cool). 0 NEW accounts. 0 Apollo.

## 2. Source coverage

Detection fanned out through 3 research sub-agents (US/NA Tier 1 + cable; International Tier 1/2 EMEA/APAC/LATAM/MENA; Subsea + Standards/Open-source + federal-procurement) to keep raw source text out of main context per the 2026-06-04 context-budget safeguard.

| # | Source (registry tier) | Status | Note |
|---|---|---|---|
| 1 | Company IR / newsroom diffs (AT&T, Verizon, T-Mobile, Cogent, Zayo, Comcast, Charter, DISH, BT, Vodafone, DT, Orange, Telefónica, NTT, Tata, Singtel, Telstra, Telia) | ✓ | Highest single-source yield; surfaced DISH/EchoStar, Zayo, Bell, DT, Singtel, Liberty Global, Telxius |
| 2 | StockTitan (8-K / 13D-G mirror) | ✓ | EchoStar/DISH FCC spectrum-sale approval confirmed |
| 3 | SEC EDGAR full-text | ✓ (partial) | Cogent close NOT found (no 8-K confirming completion as of 6/15) |
| 4 | Earnings transcripts (Seeking Alpha / Motley Fool / MarketBeat) — NaaS/API/SRv6 keyword filter | ✓ | DT Q1-2026 "Minder" autonomous-network surfaced; no AT&T NaaS/SRv6 quotes |
| 5 | Fierce Network + Light Reading + TelecomTV + RCR + Total Telecom | ✓ | M&A + exec-move + sovereign-cloud coverage |
| 6 | Ciena/Nokia/Cisco/Juniper/Arista/Infinera newsrooms (supplier wins) | ✓ (partial) | Ciena/Nokia reached; no in-window NO-B1 named carrier win for a target |
| 7 | MEF/Mplify + TM Forum + Catalyst | ✓ | Rakuten L4 cert (non-ICP); no carrier-specific LSO Sonata NO-B5 in window |
| 8 | GSMA + CAMARA GitHub + Open Gateway | ✓ (partial) | GSMA Open Gateway Greece launch surfaced (NO-B2); CAMARA GitHub author-domain NOT verifiable (see streak) |
| 9 | GlobeNewswire / PR Newswire / Business Wire (Appointments) | ✓ | Zayo BusinessWire + EchoStar/AT&T PR confirmed |
| 10 | Apollo MCP (AP-1/2/7) | n/a | Not invoked — 0 NEW-account creation |
| 11 | GitHub commit feeds CAMARA/Nephio/ONAP/OpenConfig/Sylva (NO-A5) | ✗ | Repos confirmed ACTIVE but per-commit corporate-email-domain authorship NOT verifiable via web search — needs GitHub commits API/UI. **3rd consecutive ✗** |
| 12 | FedBizOpps / SAM.gov / state procurement (NO-A8) | ✗ | Searched sam.gov for multi-domain orchestrator / TE controller / inter-carrier — only tactical/military SATCOM RFIs (out of scope). **3rd consecutive ✗** |
| 13 | Greenhouse/Lever/Ashby job boards (NO-A9) | ✗ | No named-carrier PCEP/SR-TE/BGP-LS/YANG reqs with a datable in-window posting surfaced. **3rd consecutive ✗** |
| 14 | Capacity Media (international primary) | ✓ | Via search aggregation |
| 15 | Mobile World Live + Mobile Network UK | ✓ | — |
| 16-22 | TIA/USTelecom/CTIA, ONUG, ONF, LFN, ETSI, 3GPP, IETF | ✗ | Medium-tier; not individually reached this run |
| Intl | Capacity Asia/MENA, BNamericas (LATAM), DCD, ETNO | ✓ (BNamericas ✗) | stc/HUMAIN, Singtel, DT sovereign factory, Sparkle sale surfaced via DCD/TelecomTV; BNamericas not surfaced |
| Subsea | TeleGeography RFS feed (✗ JS-only) + SubmarineNetworks.com (✓) + SubTelForum (✓) | ✓ | ViaTunisia RFS (6/3) + Telxius Tikal-Mexico + Datawave/SING surfaced |
| I2 | Sovereign AI Compute Grants | ✓ | Several found (DT, stc, Edge Continuum) but mapped out-of-segment or dropped on Tier-C freshness (see §10) |

**🚩 COVERAGE ESCALATION (for Aggregator to surface to Cooper):** NO-A5 (GitHub corporate-domain commits), NO-A8 (federal procurement), and NO-A9 (carrier ATS reqs) are now at a **3rd consecutive Monday ✗** (6/1, 6/8, 6/15). Per the standing failure-mode rule this auto-flags to Cooper. Root cause is a tooling gap, not absence of signal: NO-A5 requires the GitHub commits API or browser (WebSearch cannot see commit-author email domains); NO-A8/A9 appear to be genuine no-in-window but the access path (sam.gov full-text, ATS boards) is not reliably web-search-indexable. **Recommended fix:** give the subsea/standards sub-agent a GitHub-API path (or Chrome browser tool) for NO-A5, and a direct sam.gov API/saved-search for NO-A8. (No Slack DM sent from this task per task spec; flag carried here for the aggregator + Cooper run report.)

## 3. Candidate funnel

- **Target list:** 428 active Network Op records (all tiers, non-Flagged, `type != Customer`, MaiaEdge own excluded). 403 tier_1 / 25 tier_2. Owners: Tim Z (Intl) 397, Tim Lieto (East) 21, Ken Cunningham (West) 10. 77 carry `hs_is_target_account = true` (tier frozen). Up from 423 (2026-06-08) due to net-new imports.
- **Records carrying a stored signal (anti-churn sensitive):** 5 — Cogent (27/5-26), Vocus (27/5-11), Comcast Business (27/4-16), Orange Business Services (18/3-17), Bell (6/5-11). None re-detected fresher this run; all left untouched.
- **Tier 3 signal-scan carryover pool:** 0 networkop items on canvas F0B0AFSB9LN (canvas holds only R0-R4 enrichment/dedup holds; grep for `NO-` signal codes returned none). No carryover to drain.
- **Detected raw candidates (3 sub-agents, in-window):** ~20 material events.
- **Matched to a Network Op target AND scoring >= floor (8):** 3
- **NEW account candidates pursued:** 0 (see §6 for the DT decision)
- **Total HubSpot writes:** 3
- **Drops:** ~17 (freshness-tier cap, no-clean-target, out-of-segment, below floor)
- **Budget-overflow backlog:** none (scored set well under the 60-candidate batch ceiling)

### Detected events and disposition

| Company | Event | Event date | Code | Target match | Disposition |
|---|---|---|---|---|---|
| EchoStar / DISH | FCC approved $40B spectrum sale to AT&T ($23B) + SpaceX ($17B); DISH pivots to Boost MVNO | 2026-05-12 | NO-A4 | 326722976489 (tier_1, Ken/West, tgt=false) | **WRITE** — score 27, heat Cold->Warm, anti-churn pass (no prior signal) |
| TIM / Sparkle | EU cleared EUR 700M sale of Sparkle intl + subsea unit to Italy's Treasury + Retelit; Q2 close | 2026-04-13 | NO-A4 | 193866158789 (tier_1, Tim Z/Intl, tgt=true) | **WRITE** — score 18, heat Cold->Cool, anti-churn pass. Sovereign-state acquisition (no I2 AI-grant bonus — not an AI compute grant) |
| Orange (Medusa/ViaTunisia) | Orange activated ViaTunisia subsea segment (Marseille-Bizerte), first operational Medusa link | 2026-06-03 | NO-B4 | 303410169565 (orange.com, tier_1, Tim Z/Intl, tgt=true) | **WRITE** — score 12, heat Cold->Cool. Freshest event in scan. Dup-flagged (see §6); written to group carrier record, not the orange-business.com dup |
| Zayo Group | AI anchor customer + 8,000 route miles (4/16); closed $4.25B Crown Castle Fiber buy (5/1) | 2026-04-16 / 05-01 | NO-A1 | None (Zayo not in Network Op pool) | **DROP — out of segment.** Zayo absent from Network Op pool (likely Fiber Operator scope or absent). Sourcing-gap note §6 |
| Deutsche Telekom | Industrial AI Cloud / NVIDIA Munich sovereign AI factory (4/30, NO-A1, I2) + Q1 "Minder" autonomous network (5/15, NO-A2) | 2026-04-30 / 05-15 | NO-A1/A2 | No DT-AG carrier record; DT exists only as NeoCloud record 303925580502 | **DROP from Network Op + cross-segment handoff.** Sovereign-AI-factory signal belongs to NeoCloud record 303925580502 ("Deutsche Telekom AI Cloud") — flag to NeoCloud task/aggregator (appears missed in today's NeoCloud run). DT-AG carrier parent gap §6 |
| stc / center3 | center3 + HUMAIN JV up to 1GW AI DC capacity, signed 12/18 (I2, multi-billion) | 2025-12-18 | NO-A1 | Only "Stc Kuwait Wholesale" (different entity) | **DROP — no clean match.** center3 is stc Group Saudi; Kuwait wholesale arm is not the news entity. More AI-DC/colo than Network Op. Sourcing note §6 |
| Telecom Italia (+Orange/Telefónica/Vodafone) | Pan-EU federated Edge Continuum at MWC 2026 (I2, IPCEI-funded) | 2026-02-23 | NO-C2 | multi-operator | **DROP — Tier C freshness cap.** 112d > 90d Tier C ceiling |
| Liberty Global | 5-yr strategic AI partnership with Google Cloud | 2026-02-03 | NO-C4 | 316298284739 | **DROP — Tier C freshness cap.** 132d > 90d (same as 2026-06-08 disposition) |
| Singtel (Digital InfraCo) | Centre of Excellence for Applied AI w/ NVIDIA, sovereign cloud | 2026-02-24 | NO-C2 | 251574587097 (Optus — imperfect) | **DROP — Tier C freshness cap (111d > 90d) + imperfect match (Optus AU ≠ Singtel SG InfraCo)** |
| Fastweb Vodafone (IT) | MoU with Italian Institute for AI (AI4I), sovereign AI | 2026-01-27 | NO-C2 | 324617980617 | **DROP — Tier C freshness cap.** 139d > 90d |
| Telxius | Tikal subsea extension to Cancún, Mexico; RFS targeted mid-2026 | ~2026-Q2 | NO-B4 | 251270645453 (clean) | **DROP — no firm in-window past event date** (RFS is future-targeted; supply-contract date imprecise). Re-evaluate when RFS fires |
| COSMOTE / Vodafone Greece | GSMA Open Gateway commercial launch in Greece | 2026-03-06 | NO-B2 | 319151161037 (Vodafone Greece Wholesale) | **DROP — Tier B freshness cap.** 101d > 90d |
| Bell Canada | "Bell AI Fabric" + Bell Cyber/Ateko launch | ~2026-02-26 | NO-A2 | 322837059318 | **DROP — below floor + anti-churn.** 109d -> Tier A ×1 × MED ×2 = 6 < 8; stored 5/11 signal is newer anyway |
| Charter / Spectrum | ex-Frontier CEO Nick Jeffery named COO (starts 9/1) | 2026-02-25 | NO-A3 (weak) | 175162002126 / 192879703758 | **DROP — below floor.** COO (not network-exec) ×110d ×MED = 6 < 8 |
| Rogers | ~100 IT layoffs + call-center contract cancellation (AI-shift) | 2026-02-20 | NO-C5 | 251587604216 | **DROP — Tier C freshness cap (115d > 90d) + nuanced layoff reason** |
| AT&T / Verizon / T-Mobile | D2D satellite JV still only "agreement in principle"; no definitive/close since 5/14 | 2026-05-14 | NO-A4/C4 | all tier_1 | **DROP — no second event; below floor.** Carryover watch continues |
| Cogent | I Squared $225M DC sale (announced 5/26) — checked for CLOSE | n/a | NO-A4 | 236028986044 | **NO-OP — close NOT confirmed as of 6/15.** Do not re-fire; 5/26 announcement already stored. Carryover watch continues |
| Telus | Selected Capgemini for autonomous-network platform | 2026-02-26 | NO-A2/A8 | None (Telus not in pool) | **DROP — out of pool.** Sourcing-gap note §6 |
| Rakuten Mobile/Symphony | TM Forum Autonomous Network Level 4 certification (world-first) | 2026-02 | NO-B3 | None (non-ICP) | **DROP — not an ICP target** (awareness only) |
| Verizon / Frontier | Closed $20B Frontier consumer-fiber acquisition | 2026-01-20 | NO-A4 | 192899501812 | **DROP — wrong semantics (inbound consumer M&A) + 146d** |

## 4. Score distribution

| Band | Count |
|---|---|
| 27+ (Highest) | 1 (DISH) |
| 18-26 (Strong) | 1 (Sparkle) |
| 12-17 (Worth Reviewing) | 1 (Orange Group) |
| 8-11 (LIGHT) | 0 |
| <8 / dropped pre-score | ~17 |

## 5. Writes summary

| ID | Name | Code | Score | last_signal_date | Heat delta | Tier | Owner |
|---|---|---|---|---|---|---|---|
| 326722976489 | DISH Network | NO-A4 | 27 | 2026-05-12 | Cold -> Warm | tier_1 (written; tgt=false) | Ken Cunningham (West) |
| 193866158789 | Sparkle | NO-A4 | 18 | 2026-04-13 | Cold -> Cool | tier_1 (frozen, tgt=true) | Tim Ziemer (Intl) |
| 303410169565 | Orange Business (orange.com, group carrier) | NO-B4 | 12 | 2026-06-03 | Cold -> Cool | tier_1 (frozen, tgt=true) | Tim Ziemer (Intl) |

- Fields written per record: `recent_news_or_trigger_event`, `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`. `account_tier` written only on DISH (not a target account); frozen on Sparkle + Orange (`hs_is_target_account = true`).
- `last_enriched_date` NOT bumped on any record (partial signal writes) — verified post-write (DISH 2026-06-09, Sparkle 2026-05-19, Orange 2026-05-18 unchanged).
- 3 heat promotions: 1 Cold->Warm (DISH), 2 Cold->Cool (Sparkle, Orange).
- **Aggregator note:** all 3 writes carry back-dated event-date `last_signal_date` (5/12, 4/13, 6/3), NOT today's date — consistent with the engine-unification event-date semantics. The aggregator's `last_signal_date = today` query will NOT surface these; it should key on `hs_lastmodifieddate = today` (or equivalent) to pick up today's Network Op writes for the rep cascade. (Same caveat flagged 2026-06-08.)

## 6. Tier 3 holds / data-quality flags

- **0 new Tier 3 holds.** No canvas append required for networkop signal-scan items.
- **Orange duplicate flag (persists, for R3):** records 303410169565 ("Orange Business", domain orange.com, Tier 1 Carrier — got the ViaTunisia write this run) and 318223391443 ("Orange Business Services", domain orange-business.com, International Backbone Specialist — carries the 3/17 Summit signal, 18/Cool) are likely the same Orange B2B entity. The two now hold different signals. Recommend R3 merge; survivor should carry the max-score signal. ViaTunisia was written to orange.com (the group carrier record, no prior signal) rather than clobbering the stronger 318223391443 18-point signal.
- **Deutsche Telekom AG carrier-parent gap (sourcing):** DT exists in CRM ONLY as "Deutsche Telekom AI Cloud" (303925580502, customer_segment = NeoCloud). The DT-AG Tier-1-carrier parent is absent from the Network Op pool. Two strong in-window DT carrier-side signals (Industrial AI Cloud sovereign factory 4/30; "Minder" autonomous network 5/15) had no clean Network Op home. Did NOT auto-create DT-AG (brand-collision/duplicate risk with the existing NeoCloud record). Recommend Cooper / R7 sourcing decide whether to add a DT-AG carrier record.
- **Cross-segment handoff (NeoCloud):** the DT Industrial AI Cloud / NVIDIA Munich sovereign-AI-factory event (4/30, would score ~27 + I2) maps to the existing NeoCloud record 303925580502 and appears to have been missed by today's NeoCloud signal scan (its 9 writes did not include DT AI Cloud). Flag for the NeoCloud task / aggregator to pick up.
- **Other sourcing gaps surfaced by signals (not in Network Op pool):** Zayo Group (major US wholesale/dark-fiber carrier — strong AI-anchor + Crown Castle fiber close), Telus (autonomous-network move), stc Group Saudi / center3 (1GW HUMAIN AI-DC JV — likely Colo/NeoCloud scope). Flag to account-sourcing.

## 7. QA gate (Stage 4.5)

All 3 scored hits passed the 10-rule gate: source URLs real/reachable (sdxcentral FCC approval; datacenterdynamics EU clearance; submarinenetworks ViaTunisia); freshness within 180d (34/63/12 days); segment = Network Operator on all; narratives 208/230/216 chars (<=250); owners map West/Intl/Intl; pure prose, no date prefix, no `[Routine]` tag, no em dashes, no MaiaEdge-competitor names (AT&T/SpaceX are factual counterparties, not MaiaEdge fabric competitors); score arithmetic verified (27/18/12); no double-counting (EchoStar event -> DISH only, not AT&T buyer-side); all 3 NEW this run. 0 gate drops at Stage 4.5 (the ~17 drops occurred earlier at Stage 1/2 on freshness window, floor, target-match, or segment scope).

## 8. Failed writes

None. HubSpot batch: 3 processed, 3 updated, 0 failed. Post-write read-back verified all 5 signal fields on all 3 records.

## 9. Apollo budget post-run

- Sub-cap: 50 / run. Consumed: 0 (no NEW-account creation; matched-account writes are Apollo-free).
- Weekly pool W25 unchanged: 2 / 850 (Signal Scan Fiber spent 2 earlier today), 848 remaining.
- No JSON update required (0 consumption); tracker left as-is to avoid concurrent-routine contention.

## 10. International signal flags

- **I2 Sovereign AI Compute Grants / sovereign infra:** an unusually heavy sovereign-AI week — DT Industrial AI Cloud (IPCEI-funded, 4/30), stc/center3 + HUMAIN 1GW (PIF-backed, 12/18), pan-EU Edge Continuum (IPCEI-CIS, 2/23), Singtel + NVIDIA sovereign cloud (2/24), Fastweb Vodafone + AI4I (1/27). NONE landed a Network Op write: DT/stc/Singtel map to NeoCloud/Colo scope or imperfect entities; the EU/Edge-Continuum and Singtel items dropped on the Tier-C 90-day freshness cap. Surfaced here for cross-segment awareness.
- **Tim Z (International) territory carried the run again:** 2 of 3 writes (Sparkle, Orange) plus the heaviest drop list (DT, stc, Edge Continuum, Singtel, Fastweb, Telxius) — consistent with the international Tier 1/2 book being Tim Z's heaviest.
- **Subsea watch:** ViaTunisia RFS (6/3) written this run to Orange group. Telxius Tikal-to-Mexico RFS targeted mid-2026 — monitor for the actual RFS event (clean Telxius target 251270645453 ready to receive it). Datawave/Cerberus SING financing (1/20) noted but RFS not until 2030.
- **Next-Monday carryover watch:** (1) Cogent / I Squared $225M DC sale — close still unconfirmed as of 6/15; a close event re-fires NO-A4 on 236028986044. (2) AT&T/Verizon/T-Mobile D2D satellite JV — monitor for a definitive agreement/close (second-event firing would lift score). (3) DT-AG carrier-parent sourcing decision pending Cooper.

---

**[Network Op] target=428 matched=3 new=0 writes=3 heat_promotions=3 apollo=0/50 runtime=16min audit=weekly-reports/2026-06-15/signal-scan/networkop/**

No Slack DM sent from this task (per task spec). The Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs, canvas Run log, and the Cooper run report. Two items for the aggregator to surface: (a) the NO-A5/A8/A9 3-week ✗ source-coverage escalation (§2); (b) the DT Industrial AI Cloud cross-segment handoff to NeoCloud record 303925580502 (§6). Note the back-dated `last_signal_date` caveat in §5 when assembling today's rep cascade.
