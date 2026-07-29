# Weekly Signal Scan — Cross-ICP Run Report (Aggregator)

**Date:** 2026-06-15 (Monday, CT) · **Run window:** 8:30am (Colo) → ~2:45pm (aggregator) · **Status:** :white_check_mark: complete

All 6 per-segment scans fired and wrote; aggregator built and dispatched all 3 rep DMs from the current Hot/Warm/Cool heat pool, appended the canvas Run log, and wrote this report. **You do not need to do anything for the run to be complete** — the items in §10 are optional improvements, not blockers.

---

## 1. Run header
- **Total HubSpot writes across 6 segments:** 48 (45 matched + 3 NEW accounts)
- **Per-segment audit files:** 6 of 6 present (Colo, Fiber, NeoCloud, NetworkOp, MSP, Enterprise)
- **Rep DMs dispatched:** 3 of 3 (Lieto direct, Cunningham direct, Ziemer cascade → Cooper for validation)
- **Rep-DM population:** 150 accounts surfaced (50/rep) from a **current heat pool of 229** Hot/Warm/Cool ICP records (2026-06-04 reframe — DMs are the heat pool, not just today's writes)
- **NEW accounts auto-enriched:** 3 (all Colo, all Tim Z, Apollo 0)
- **Apollo consumed this run:** 0 by aggregator; 2 total for the day (Fiber Stage 3). W25 2/850.
- **Heat promotions today:** ~31 across writes; 2 to Hot (SOLUNA, Crusoe), ~23 to Warm, ~6 Cold→Cool.

## 2. Per-segment summary
| Segment | Audit | Target pool | Matched | NEW | Writes | Score dist (8-11 / 12-17 / 18-26 / 27+) | Apollo | Source coverage |
|---|---|---|---|---|---|---|---|---|
| Colo | ✓ | ~470 | 11 | 3 | 14 | 2 / 0 / 1 / 11 | 0/35 | Robust hit; #8 job-boards + #10 hyperscaler-feeds 3-wk ✗ |
| Fiber | ✓ | 1,260 | 21 | 0 | 21 | 3 / 1 / 7 / 10 | 2/35 | Strong; BEAD/M&A/ABS all reached |
| NeoCloud | ✓ | 188 | 9 | 0 | 9 | 1 / 0 / 1 / 7 | 0/55 | **Streaks broken** (IX/job-boards/PeeringDB via bash curl) |
| Network Op | ✓ | 428 | 3 | 0 | 3 | 0 / 1 / 1 / 1 | 0/50 | NO-A5/A8/A9 **3rd-week ✗** (escalation) |
| MSP/Aggregator | ✓ | 480 | 0 | 0 | 0 | — | 0/20 | Quiet/anti-churn (TSD backlog already stored); #12/13/15/18-20 ✗ |
| Enterprise | ✓ | 16 | 1 | 0 | 1 | 1 / 0 / 0 / 0 | 0/55 | 7 sources **3rd-week ✗** (subscription/ATS) |
| **Total** | **6/6** | — | **45** | **3** | **48** | **7 / 2 / 10 / 29** | **2/250** | — |

Notable: Colo had an unusually full Highest-Priority tier (11 at score 27) off a busy early-June DC news cycle. Fiber's 21 came largely from finalized Texas BEAD subgrants (06-03). NeoCloud's stored public-name backlog was correctly anti-churn-suppressed; only week-over-week deltas wrote. MSP genuinely quiet (no new in-window telecom-aggregator buying signal). Enterprise thin pool (16) is FinSvc-heavy; HCL was the only write.

## 3. Cross-ICP heat rollup
- **Today's 48 writes by heat:** Hot 7 · Warm 23 · Cool 18 · Cold 0
- **Current full rep-owned heat pool (the DM population source):** 229 records — **Hot 44 · Warm 72 · Cool 113**. Pool has grown materially week-over-week (NeoCloud alone 163→188; net-new imports across Fiber/Colo). Every rep is now well over the 50 cap from Hot+Warm alone, so the 25-floor fill-down never fired and Carryover News (retired) was not needed.

## 4. Rep DM dispatch
| Rep | Owner ID | Slack | Surfaced | NEW | CARRIED | LIGHT | Hot-no-score (open-deal) | Top account |
|---|---|---|---|---|---|---|---|---|
| Tim Lieto (East) | 161889085 | U0A973L1HFF (direct) | 50 | 10 | 40 | 6 | 7 | Omni Fiber (33 🔥) |
| Ken Cunningham (West) | 162339176 | U0AE1PGCB6C (direct) | 50 | 13 | 37 | 3 | 0 | Applied Digital (33 🔥) |
| Tim Ziemer (Intl) | 159350430 | U0A24D9RJLS (→ Cooper) | 50 | 14 | 36 | 2 | 9 | Nscale (33 🔥) |

Tim Z's cascade + full table + xlsx are routed to you (`weekly-signal-scan-ziemer-2026-06-15.xlsx`). Validate and forward when ready. All three bodies + 9 threaded table chunks delivered (12 Slack messages, 0 failures).

## 5. Source-coverage delta vs prior Monday
**Improved this run:** NeoCloud reset its IX (#6), job-board (#7), and PeeringDB (NC-A9) **2-week ✗ streaks** by reaching the ATS/PeeringDB JSON via `bash curl` (web_fetch is provenance-locked against them) — and the job-board attempt yielded a real detection (Crusoe NC-A6 hiring spike). Enterprise broke WSJ/CIO (#22), Bisnow (#25), Mergermarket (#27), Crunchbase (#29). MSP reset FCC Daily Digest (#7).

**Sources needing development (3-consecutive-Monday ✗ — auto-flagged):**
- **ATS job boards (Greenhouse/Lever/Ashby):** Colo #8, MSP #12, Enterprise #10, Network Op NO-A9. Search indexing doesn't surface ATS boards.
- **Federal procurement (sam.gov / FedBizOpps):** Network Op NO-A8.
- **GitHub commit-author domains (CAMARA/Nephio/etc.):** Network Op NO-A5 — needs the GitHub commits API/UI, not web search.
- **Subscription-gated analyst (Nelson Hall, HIMSS/CHIME, Risk&Insurance/ISMG) + PacketFabric/Console Connect:** Enterprise #8/#14/#23/#30/#31/#32.

**Root cause is a tooling gap, not absence of signal.** NeoCloud proved the fix this run: `bash curl` reaches the ATS + PeeringDB machine-readable JSON that the provenance-locked web_fetch cannot. **Recommendation: wire curl-via-bash (or the Chrome MCP) into the A5/A6/A9-class source paths across all per-segment scans.** This is the single highest-leverage coverage improvement.

## 6. Anomalies
1. **type=Customer in the heat pool:** HDCO GROUP (265768509166) carried signal_heat=Hot inside an ICP segment but is `type = "Customer"` — **excluded from Lieto's rep DM** per the `type != Customer` rule (caught at the aggregator's correctness gate; the pool query did not pre-filter type). Worth checking why an existing customer sits in the prospect signal pool (mis-set `type`, or a real customer that needs a CS motion).
2. **Event-date semantics (working as designed):** all per-segment writes carry back-dated `last_signal_date` (event date), so a naive `last_signal_date = today` query returns ~0. Aggregator correctly built the population from the heat pool + the 6 audit files + `hs_lastmodifieddate` — the 2026-06-01 "0 today" bug did not recur.
3. **DT cross-segment gap (carried from Network Op §6):** Deutsche Telekom's fresh carrier-side sovereign-AI signals (Industrial AI Cloud sovereign factory 4/30; "Minder" autonomous network 5/15) map to the existing NeoCloud record 303925580502 ("Deutsche Telekom AI Cloud") but were **not refreshed in today's NeoCloud 9 writes**. The record still surfaces to Tim Z at its stored 4/30 score-27 Warm, so the rep sees it — but the newest milestones aren't reflected. Next NeoCloud scan should pick it up.
4. **Below-cap (silent nurture):** Lieto pool ~80 (30 below cap), Cunningham ~63 (13 below), Ziemer ~56 (6 below). Below-cap tails are score-0 Cool records; not surfaced. Lefdal Mine (3rd new Colo account) initially fell below Ziemer's cap on the first pass, then surfaced at #40 once HDCO was removed — both now correct.
5. **No score arithmetic mismatches** between the 6 audit "writes summary" counts and the HubSpot reads.

## 7. R3 / R6 data-quality flags (for the next 2am ET R3 run + R6)
- **Orange duplicate pair (R3):** `orange.com` (303410169565, got the ViaTunisia write, score 12) vs `orange-business.com` (318223391443, holds the 3/17 Summit NaaS signal, score 18) — same Orange B2B entity, now holding different signals. Both are in Tim Z's DM. Merge; survivor should carry the max-score signal.
- **Digital Edge messy name (R6/R3):** "Digital Edge DC - Hong Kong, Hong Kong" (251533417160) is the canonical digitaledgedc.com record carrying a per-location name; the Seoul SEL5 signal was written there. Surfaces to Tim Z with that messy label. Name cleanup.
- **JPMorgan dup (R3, not in pool):** JPMorgan Chase (324628785885) / J.P. Morgan & Co. (240446137023) — merge pending (flagged by Enterprise audit).
- **Owner/territory mismatches (R6):** CyrusOne (Ken/West on an East-HQ operator), Ark + Flexential (Ken on East-HQ operators) — left untouched by the scan, R6 scope.

## 8. Apollo budget post-run
- **W25 (week_start 2026-06-15):** 2 / 850 consumed (Fiber Stage 3 new-account enrich: usconnect.net 1cr + win-technology.com wrong-entity 1cr). **848 remaining.**
- Signal Scan weekly sub-cap is 250; used **2 of 250** this run (essentially free — matched writes and the 3 NEW Colo accounts were built from public web research, no Apollo).
- Projection for rest of W25: R1 M-F (~0-30/day historically near 0), R2 M-F (~0), R8 Fri (175), R6 (~5). Comfortable headroom.

## 9. Tier 3 holds carryover
- **0 new signal-scan Tier 3 holds** across all 6 segments this run (each audit confirms none added). No canvas Tier 3 re-append performed by signal scan. Standing canvas Tier 3 items (R0/R1/R2/R3/R4 dedup + ICE Enterprise-vs-Colo + MMR Fiber entity-split) are out of signal-scan scope.

## 10. What needs your attention (top 3 — optional)
1. **Source development (highest leverage):** authorize wiring `bash curl` (or Chrome MCP) into the ATS job-board / PeeringDB / GitHub-commits / sam.gov source paths. NeoCloud already proved it works and recovered a real detection. This closes the recurring NO-A5/A8/A9 + Colo/MSP/Enterprise job-board blind spots in one change.
2. **HDCO GROUP (265768509166):** confirm whether `type = Customer` is correct (and why it's carrying a Hot prospect signal in an ICP segment). If it's a real customer, it belongs in a CS motion; if mis-typed, fix so future heat-pool builds include it.
3. **Tim Z cascade:** validate `weekly-signal-scan-ziemer-2026-06-15.xlsx` + the threaded list and forward to Tim Z when ready (still Phase-0 routed to you). And decide the **DT-AG carrier-parent** sourcing question (NeoCloud record exists; Tier-1 carrier parent absent from the Network Op pool).

---
*Artifacts: `weekly-reports/2026-06-15/weekly-signal-scan-{lieto,cunningham,ziemer}-2026-06-15.xlsx` · per-segment audits under `weekly-reports/2026-06-15/signal-scan/<segment>/` · canvas Run log row appended to F0B0AFSB9LN (verified single append).*
