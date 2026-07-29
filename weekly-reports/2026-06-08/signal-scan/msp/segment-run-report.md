# Signal Scan — MSP/Aggregator — Segment Run Report

## 1. Run header

| Field | Value |
|---|---|
| Date (CT) | 2026-06-08 (Monday) |
| Segment | MSP/Aggregator |
| Detection window | 2025-12-10 → 2026-06-08 (180-day rolling, event-date basis) |
| Scope | All tiers, non-Flagged (tier filter removed 2026-06-04) |
| Apollo consumed | 0 of 20 |
| MCPs | HubSpot ✓ · Apollo ✓ (unused) · Slack/canvas ✓ (read) · web_search ✓ · web_fetch n/a (search-anchor) |
| Outcome | **3 matched-account signal writes (AppDirect 27/Warm · TD SYNNEX 18/Cool · Expereo 12/Cool). First MSP run under the 180-day window — surfaced the Q1/Q2 TSD backlog the prior 14-day gate discarded.** |
| Prior Monday report | PRESENT (2026-06-01, QUIET week) → all accounts CARRIED baseline; 0 prior signals to re-confirm |
| Backlog carry-in | None (no 2026-06-01 backlog.md on disk) |

## 2. Source coverage table

Search-anchor pattern throughout (direct web_fetch gated on Cowork runtime). EMEA channel press promoted into the primary rotation this run per the 2026-06-01 EMEA fallback recommendation.

| # | Source | Tier | Attempted | Result |
|---|---|---|---|---|
| 1 | Channel Futures (+ Hiring Roundup) | Robust | ✓ | Surfaced Telarus/Intelisys/TSD market context, Front ecosystem partnership (3/18), DeLozier Intelisys departure. No new writable carrier/hire at a target beyond items below. |
| 2 | ChannelE2E (+ People column) | Robust | ✓ | No in-window target-anchor exec move at the M-A5 title bar (CRO/VP-SE/VP-Product/VP-AI). |
| 3 | TSD press (Telarus / AppDirect / Sandler / AVANT / Bridgepointe / Upstack / Intelisys / ScanSource) | Robust | ✓ | **AppDirect/PartnerStack acq 2026-04-14 (WRITE).** Sandler Director-level regional hires + SCOUT email (Feb-26, below bar). Telarus Gateway/Hub (OOW). Upstack V3 Tech acq Feb-26 (NEW-account candidate, see §3). |
| 4 | CRN | Robust (caveat) | ✓ | Award-press only. EXCLUDED per syndication rule. |
| 5 | StockTitan (SCSC / SNX / CMCSA 8-K) | Robust | ✓ | **SNX 8-K Q1 FY26 earnings 2026-03-31 (WRITE).** SCSC = 5/07 (already stored, anti-churn skip). CMCSA none in-window for targets. |
| 6 | SEC EDGAR full-text | Robust | ✓ | SNX 10-Q (period end 2026-02-28) + 8-K confirmed. No other in-window Item 1.01/2.01/5.02 for targets. |
| 7 | FCC Daily Digest | Robust | ✗ | Not anchored; no MSP-relevant items incidentally. (✗ streak: 2) |
| 8 | ScanSource + TD SYNNEX IR / earnings (M-A7, M-B4) | Robust | ✓ | SNX Q1 FY26 (M-A7, WRITE). SCSC Q3 5/07 already stored. |
| 9 | PR Newswire + Business Wire + GlobeNewswire | Robust | ✓ | **Expereo COO (3/10) + GM Americas (3/04) appointments (WRITE, M-A5 title-adjacent MED).** AppDirect/PartnerStack BW release confirmed. |
| 10 | Apollo MCP (enrich / job postings / job changes) | Robust | ✗ | Not consumed — 0 NEW accounts created (Upstack documented, not created; see §3). |
| 11 | Megaport / Console Connect / PacketFabric partner-adds (M-A3) | Robust | ✓ | No in-window carrier/partner additions at a target aggregator. |
| 12 | Greenhouse / Lever / Ashby TSD job boards (M-A6) | Robust | ✗ | Not anchored this run. (✗ streak: 2) |
| 13 | CompTIA / GTIA | Medium | ✗ | Not anchored. (✗ streak: 2) |
| 14 | Channel Partner Insight / IT Europa / ChannelBiz (EMEA) | Medium | ✓ | Promoted to primary rotation per 2026-06-01 fallback. Expereo Americas-leadership reset captured (also via BW). No other in-window DACH/UK move at a target. |
| 15 | FedRAMP Marketplace (M-C2) | Medium | ✗ | Not anchored. (✗ streak: 2) |
| 16 | Telecompetitor channel | Medium | ✓ | Broadband/BEAD coverage only; no aggregator move. |
| 17 | CP Expo / Channel Partners Conf agenda | Medium | ✓ | Partner gatherings noted — EXCLUDED per conference-noise rule. |
| 18 | Gartner SD-WAN MQ / Forrester Wave | Medium | ✗ | Not anchored. (✗ streak: 2) |
| 19 | Frost & Sullivan TSD | Medium | ✗ | Not anchored. (✗ streak: 2) |
| 20 | TBI Connect / Channel Asia | Medium | ✗ | Not anchored. (✗ streak: 2) |

Robust-tier: 8 of 12 attempted; **in-window writable yield = 3** (above the 25-floor concern under the new 180-day window — no EMEA-fallback escalation needed this run).

## 3. Candidate funnel

| Stage | Count |
|---|---|
| Target accounts (MSP/Aggregator, all tiers, type != Customer, ≠ MaiaEdge) | 482 (tier_1=11, tier_2≈453, tier_3=6, tier_4=18 across the full pool) |
| Canvas F0B0AFSB9LN MSP Tier 3 carryovers requiring action | 0 (prior MSP holds drained 2026-05-25; none re-added) |
| Raw in-window signal candidates detected | 6 (AppDirect, TD SYNNEX, Expereo, Front-ecosystem [4 accts], Sandler hires, Upstack) |
| Matched to target accounts (Stage 2) | 3 writable (AppDirect, TD SYNNEX, Expereo) + 3 dropped (see §7/§10) |
| NEW-account candidates (Stage 3) | 1 (Upstack — NOT created; see note) |
| Scored hits ≥8 (Stage 4) | 3 |
| HubSpot writes (Stage 5/5b) | 3 |

**Upstack NEW-account candidate (not created this run):** UpStack Inc (upstack.com), NY-based technology brokerage for cloud/colocation/connectivity, PE-backed roll-up platform (~30 acquisitions; latest V3 Technology Feb-2026, Availpartners Aug-2025, Performance Networks, Breakwater). Clean Master Agent - MSP fit with an in-window M-A1 acquisition signal. **Deferred to R1 / company-enrichment for proper Apollo-backed onboarding** rather than created here — autonomous scheduled run has no Apollo interactive-confirm guardrail and a hand-tiered TSD anchor is an expensive write to roll back. Recommend Cooper/R1 onboard.

## 4. Score distribution

| Band | Count | Accounts |
|---|---|---|
| Highest (27+) | 1 | AppDirect (27) |
| Strong (18-26) | 1 | TD SYNNEX (18) |
| Worth Reviewing (12-17) | 1 | Expereo (12) |
| LIGHT (8-11) | 0 | — |

## 5. Writes summary

| id | name | signal code | event date | score | heat delta | tier | priority |
|---|---|---|---|---|---|---|---|
| 324037036787 | AppDirect | M-A1 (PE/roll-up acq of PartnerStack) | 2026-04-14 | 27 | Cold → **Warm** | tier_1 (FROZEN, hs_is_target_account) | **48h** |
| 300408171229 | TD SYNNEX | M-A7 (record Q1 FY26 earnings + segment realign) | 2026-03-31 | 18 | Cold → **Cool** | tier_1 (FROZEN, hs_is_target_account) | **48h** |
| 326331061982 | Expereo | M-A5 (GM Americas + COO appointments, title-adjacent MED) | 2026-03-10 | 12 | Cold → **Cool** | tier_2 (unchanged) | normal (aged 90d; M-A5 nominally 48h) |

3 narrative writes · 3 signal-field sets · 0 tier writes (2 frozen, 1 unchanged) · 3 heat promotions · 0 NEW accounts · 2 priority-48h hits. No `last_enriched_date` bump (all partial signal writes).

## 6. Tier 3 holds

None added. Canvas MSP carryover queue remains empty/resolved.

## 7. QA gate drops with reasons

- **Front channel-ecosystem partnership (2026-03-18; Bridgepointe, Intelisys, Sandler, Telarus):** DROPPED. Front is a B2B customer-operations software vendor, not a network carrier — fails M-A3 (carrier add) and is not a network-orchestration buying signal. Logged, not written.
- **Sandler Partners Director-level regional channel hires (Dagg/Costello/Paine) + SCOUT Email (Feb-2026):** DROPPED. Director-of-channel-sales titles miss the M-A5 bar (CRO/VP-SE/VP-Product/VP-AI); SCOUT email is a minor portal feature below M-B3 threshold.
- **ScanSource Q3 FY26 (5/07) / AVANT (5/05) / Bridgepointe (4/09):** anti-churn SKIP — already stored at equal-or-higher score; no newer in-window event.

## 8. Failed writes

None. Batch 3/3 OK (single batch, under the 10-record batch limit).

## 9. Apollo budget post-run

Sub-cap 20, used 0 of 20. Weekly W24: 0/850 consumed, 850 remaining. No tracker write required (0 consumption).

## 10. IT MSP Test rejections (record-level)

- **NaaS Technology Inc (Nasdaq: NAAS):** EXCLUDED — EV-charging-as-a-service in China, wrong entity entirely (keyword collision on "NaaS").
- **ConvergeOne / John DeLozier hire:** EXCLUDED — ConvergeOne is a solutions integrator; the underlying event is a departure FROM Intelisys (inverse signal, not a target hire).
- No helpdesk/cybersecurity IT MSP reached classification this run.

## 11. EMEA fallback flag

**No escalation needed.** Robust-tier in-window writable yield = 3 (above the 25-floor concern) under the new 180-day window. EMEA press was already promoted into the primary rotation this run and contributed the Expereo signal. Recommend keeping EMEA channel press in the primary rotation while the 180-day window remains in effect, and anchoring the under-attempted Robust sources next run (FCC Daily Digest, Greenhouse/Lever/Ashby TSD job boards for M-A6).

---

### Footer

```
[MSP] target=482 matched=3 new=0 writes=3 heat_promotions=3 priority_48h=2 apollo=0/20 runtime=~9min audit=weekly-reports/2026-06-08/signal-scan/msp/
```

No Slack DM sent. Aggregator (signal-scan-aggregator, 2:30pm CT) owns rep DMs + canvas Run log + Cooper run report; it reads HubSpot for records this scan touched. Note: this segment's writes carry backdated event dates (3/10–4/14), NOT today's date — if the aggregator filters strictly on `last_signal_date = today` it will not see these three. Surfacing for aggregator awareness: 3 MSP records updated today with backdated event signals — AppDirect (324037036787), TD SYNNEX (300408171229), Expereo (326331061982).
