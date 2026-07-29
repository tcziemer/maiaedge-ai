# Signal Scan — Network Operator — Segment Run Report

## 1. Run header

- **Date (CT):** 2026-06-08 (Monday)
- **Segment:** Network Operator (`customer_segment = "Network Operator(Tier 1 / VNO)"`)
- **Detection window:** 180-day rolling (event date on/after 2025-12-10) — first networkop run under the widened window + all-tier scope (2026-06-04 change).
- **Apollo consumed:** 0 of 50 (weekly pool W24: 0/850 at run start; effective budget min(50, 850) = 50). 0 NEW-account creation -> 0 Apollo.
- **Runtime:** ~10 min
- **MCPs:** HubSpot ✓, Apollo ✓ (available, unused), Slack ✓ (canvas read), web_search ✓, web_fetch ✓
- **Result:** 3 matched-account signal writes (Cogent NO-A4 27/Warm; Vocus NO-A3 27/Warm; Orange Business NO-A2 18/Cool). 0 NEW accounts. The widened window surfaced the in-window strategic backlog the old 14-day gate dropped on 2026-06-01.

## 2. Source coverage

Detection fanned out through 2 research sub-agents (US/NA Tier 1 + cable; International Tier 1/2 + subsea) to keep raw source text out of main context per the 2026-06-04 context-budget safeguard.

| # | Source (registry tier) | Status | Note |
|---|---|---|---|
| 1 | Company IR / newsroom diffs (Lumen, AT&T, Verizon, T-Mobile, Charter, Cox, Comcast, BT, Vodafone, DT, Orange, Telefónica, NTT, Tata, Singtel, Telstra) | ✓ | Highest single-source yield; surfaced Cogent/Vocus/Orange/Lumen moves |
| 2 | StockTitan (8-K / 13D-G mirror) | ✓ (partial) | Crown Castle 8-K restructuring surfaced (tower-side, out of segment scope) |
| 3 | SEC EDGAR full-text | ✓ (partial) | Crown Castle cci-20260204 8-K confirmed |
| 4 | Earnings transcripts (Seeking Alpha / Motley Fool / MarketBeat) — NaaS/API/SRv6 keyword filter | ✓ | Lumen PCF $13B Investor Day disclosure (NO-A2) surfaced but Lumen not in target segment |
| 5 | Fierce Network + Light Reading + TelecomTV + RCR + Total Telecom | ✓ | M&A + exec-move coverage |
| 6 | Ciena/Nokia/Cisco/Juniper/Arista/Infinera newsrooms (supplier wins) | ✗ | Not individually reached; no NO-B1 candidate surfaced incidentally |
| 7 | MEF/Mplify + TM Forum + Catalyst | ✗ | Not reached this run |
| 8 | GSMA + CAMARA GitHub + Open Gateway | ✗ | Not reached this run |
| 9 | GlobeNewswire / PR Newswire / Business Wire (Appointments) | ✓ | Cogent divestiture (PRNewswire) confirmed |
| 10 | Apollo MCP (AP-1/2/7) | n/a | Not invoked — 0 NEW-account creation |
| 11 | GitHub commit feeds CAMARA/Nephio/ONAP/OpenConfig/Sylva (NO-A5) | ✗ | Not reached — **2nd consecutive ✗ (streak watch: 2 of 3)** |
| 12 | FedBizOpps / SAM.gov / state procurement (NO-A8) | ✗ | Not reached — **2nd consecutive ✗ (streak watch: 2 of 3)** |
| 13 | Greenhouse/Lever/Ashby job boards (NO-A9) | ✗ | Not reached — **2nd consecutive ✗ (streak watch: 2 of 3)** |
| 14 | Capacity Media (international primary) | ✓ | Via search aggregation |
| 15 | Mobile World Live + Mobile Network UK | ✓ | D2D satellite JV surfaced |
| 16-22 | TIA/USTelecom/CTIA, ONUG, ONF, LFN, ETSI, 3GPP, IETF | ✗ | Medium-tier; not reached this run |
| Intl | Capacity Asia/LATAM/MENA, ETNO, BNamericas, itnews.com.au | ✓ | Vocus CTO + Orange Business Summit + Liberty Global/Google Cloud surfaced |
| Subsea | TeleGeography RFS feed + SubmarineNetworks.com + SubTelForum | ✓ | ViaTunisia RFS (6/4) + 2Africa Ghana/Nigeria landings surfaced (see §3 dispositions) |
| I2 | Sovereign AI Compute Grants | ✓ | None won by a target carrier in window |

**Coverage note:** NO-A5 / NO-A8 / NO-A9 now at a **2-week ✗ streak** (first ✗ logged 2026-06-01). If ✗ persists a 3rd consecutive Monday, auto-flag to Cooper — these source classes (GitHub corp-domain commits, federal procurement, ATS job reqs) are not web-search-indexable and may need a different access path.

## 3. Candidate funnel

- **Target list:** 423 active Network Op records (all tiers, non-Flagged, `type != Customer`, MaiaEdge own excluded). Up from 404 (2026-06-01) due to all-tier scope + net-new imports.
- **Tier 3 signal-scan carryover pool:** 0 networkop items on canvas F0B0AFSB9LN (canvas holds only R0-R3 enrichment dedup holds, no Network-Op signal-scan items). 2026-06-01 report logged Vocus (5/12) + D2D JV (5/14) as informal carryovers — both re-evaluated this run (see below).
- **Detected raw candidates (both sub-agents, in-window):** ~12 material events
- **Matched to a Network Op target AND scoring >= floor (8):** 3
- **NEW account candidates pursued:** 0
- **Total HubSpot writes:** 3
- **Drops:** 9
- **Budget-overflow backlog:** none (scored set well under the 60-candidate batch ceiling)

### Detected events and disposition

| Company | Event | Event date | Code | Target match | Disposition |
|---|---|---|---|---|---|
| Cogent Communications | Definitive agreement to sell 10 data centers (~53MW) to I Squared Capital for $225M | 2026-05-26 | NO-A4 | 236028986044 (tier_1, Ken/West) | **WRITE** — score 27, heat Cool->Warm, anti-churn pass (5/26 > stored 5/6) |
| Vocus | Revived CTO role; hired Nikos Katinakis (ex-Zayo, ex-Telstra) effective July | 2026-05-11 | NO-A3 | 251600877280 (tier_1, Tim Z/Intl) | **WRITE** — score 27, heat Cold->Warm, anti-churn pass (5/11 > stored 2025-08-01). Resolves the 2026-06-01 carryover. |
| Orange Business | Summit 2026 launch — trusted AI + sovereign cloud (Cloud Avenue SecNum) + secure programmable connectivity | 2026-03-17 | NO-A2 | 318223391443 (orange-business.com, tier_1, Tim Z/Intl) | **WRITE** — score 18, heat Cold->Cool, anti-churn pass (no prior signal). See dup flag §6. |
| Lumen Technologies | Alkira acquisition ($475M NaaS control plane); $13B PCF disclosure | 2026-05-05 / ~Mar | NO-A1/NO-A2 | None | **DROP — out of segment.** Lumen is a MaiaEdge competitor reference (Lumen PCF), not a Network Op target. Correctly absent. |
| AT&T / Verizon / T-Mobile | Direct-to-device satellite JV (agreement in principle) | 2026-05-14 | NO-C4 | all tier_1 | **DROP — below floor.** Tier C × ≤30d (×2) × HIGH (×3) = 6 < 8 for each. |
| AT&T | Closed $5.75B acquisition of Lumen consumer fiber | 2026-02-02 | (NO-A4?) | 300403571414 | **DROP — wrong signal semantics.** Inbound consumer/residential acquisition, not the wholesale/programmable-fabric divestiture NO-A4 targets. |
| Verizon | Frontier acquisition completed (already stored) | ~2026-01 | — | 192899501812 | **DROP — stale + inbound consumer M&A, already in stored brief.** |
| T-Mobile | (existing 4/28 fiber-JV signal retained) | 2026-04-28 | NO-A4 | 268250706641 | **NO-OP — keep stored 4/28 signal** (newer/stronger than the 5/14 D2D move which scored 6). |
| Crown Castle | ~20% headcount restructuring | 2026-02-04 | NO-C5 | None | **DROP — out of segment** (towerco; not in Network Op pool) + tower-side relevance only. |
| Liberty Global | Google Cloud 5-yr strategic AI partnership | 2026-02-03 | NO-C4 | 316298284739 | **DROP — Tier C freshness cap.** 125 days > 90d Tier C ceiling -> drop before scoring. |
| Deutsche Telekom | Industrial AI Cloud commercial GPU availability (NVIDIA, Munich) | 2026-04-30 | NO-A1/NO-C2 | None | **DROP — not in Network Op target pool** (no Deutsche Telekom record in segment; searched telekom/T-Systems). Event is a sovereign-AI-cloud signal, not programmable-fabric. |
| Orange Marine / Tunisie Telecom | ViaTunisia subsea cable reaches Ready-for-Service | 2026-06-04 | NO-B4 | None clean | **DROP — no clean operator record.** Cable operated by Orange Marine + Tunisie Telecom; neither is a clean target record (Orange Tunisia Wholesale is a different entity). |
| Bayobab (MTN GlobalConnect) | 2Africa landings Ghana/Nigeria | ~2026-02 | NO-B4 | 316212615892 | **DROP — Tier B freshness cap.** ~113 days > 90d Tier B ceiling -> drop. |

## 4. Score distribution

| Band | Count |
|---|---|
| 27+ (Highest) | 2 (Cogent, Vocus) |
| 18-26 (Strong) | 1 (Orange Business) |
| 12-17 (Worth Reviewing) | 0 |
| 8-11 (LIGHT) | 0 |
| <8 / dropped pre-score | 9 |

## 5. Writes summary

| ID | Name | Code | Score | last_signal_date | Heat delta | Tier | Owner |
|---|---|---|---|---|---|---|---|
| 236028986044 | Cogent Communications Holdings | NO-A4 | 27 | 2026-05-26 | Cool -> Warm | tier_1 (frozen, target=true) | Ken Cunningham (West) |
| 251600877280 | Vocus | NO-A3 | 27 | 2026-05-11 | Cold -> Warm | tier_1 (frozen, target=true) | Tim Ziemer (Intl) |
| 318223391443 | Orange Business Services | NO-A2 | 18 | 2026-03-17 | Cold -> Cool | tier_1 (frozen, target=true) | Tim Ziemer (Intl) |

- Fields written per record: `recent_news_or_trigger_event`, `last_signal_date`, `last_signal_score`, `signal_count_last_30d`, `signal_heat`. `account_tier` NOT written (all three carry `hs_is_target_account = true` -> tier frozen).
- `last_enriched_date` NOT bumped on any record (partial signal writes).
- 2 heat promotions (Cold/Cool -> Warm); 1 heat promotion Cold -> Cool.

## 6. Tier 3 holds / data-quality flags

- **0 new Tier 3 holds.** No canvas append required for networkop signal-scan items.
- **Orange Business duplicate flag (for R3):** records 303410169565 ("Orange Business", domain orange.com, Tier 1 Carrier) and 318223391443 ("Orange Business Services", domain orange-business.com, International Backbone Specialist) both represent Orange's B2B/ICT services arm and are likely duplicates. Signal written to the exact-domain match (318223391443). Recommend R3 merge; carry the signal forward to the surviving primary.
- **Cogent stored-news prefix artifact:** prior `recent_news_or_trigger_event` carried a legacy `[F-A7]` Fiber-signal-code prefix on a Network Op record. Overwritten this run with pure-prose narrative (no code prefix), consistent with the 2026-05-28 engine-unification format.

## 7. QA gate (Stage 4.5)

All 3 scored hits passed the 10-rule gate: source URLs real/reachable (PRNewswire, itnews.com.au, orange-business.com press); freshness within 180d; segment = Network Operator; narratives 219/191/220 chars (<=250); owners map to West/Intl/Intl; pure prose, no date prefix, no `[Routine]` tag, no em dashes, no MaiaEdge competitor names; score arithmetic verified; no double-counting; all NEW signals this run. 0 gate drops at Stage 4.5 (the 9 drops occurred earlier at Stage 1/2 on freshness window, floor, target-match, or segment scope).

## 8. Failed writes

None. HubSpot batch: 3 processed, 3 updated, 0 failed.

## 9. Apollo budget post-run

- Sub-cap: 50 / run. Consumed: 0 (no NEW-account creation; matched-account writes are Apollo-free).
- Weekly pool W24 unchanged: 0 / 850, 850 remaining.
- No JSON update required (0 consumption); tracker left as-is.

## 10. International signal flags

- **I2 Sovereign AI Compute Grants:** none won by a target carrier in window.
- **Tim Z (International) territory carried the run:** 2 of 3 writes (Vocus AU, Orange Business) plus the heaviest drop list (DT, Liberty Global, Bayobab, ViaTunisia) — consistent with the international Tier 1/2 book being Tim Z's heaviest.
- **Subsea watch:** ViaTunisia RFS (6/4) is genuinely fresh and high-relevance but has no clean single-operator target record — revisit if an operating entity (Orange Marine or Tunisie Telecom) is added to the CRM. 2Africa Pearls/PEACE Gulf extensions projected RFS H2-2026 — monitor for in-window landing events.
- **Next-Monday carryover watch:** D2D satellite JV (AT&T/Verizon/T-Mobile) — monitor for a definitive-agreement/close event (second-event firing would lift score); Cogent DC sale close (~mid-June) — a close event re-fires NO-A4.

---

**[Network Op] target=423 matched=3 new=0 writes=3 heat_promotions=3 apollo=0/50 runtime=10min audit=weekly-reports/2026-06-08/signal-scan/networkop/**

No Slack DM sent from this task (per task spec). The Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs, canvas Run log, and the Cooper run report — it will read HubSpot for `last_signal_date = today` records (note: this segment's writes carry event dates 2026-05-26 / 2026-05-11 / 2026-03-17, NOT today's date, per the engine-unification event-date semantics; the aggregator keys on `last_signal_date` and should account for back-dated event dates when assembling today's rep cascade).
