# Weekly Signal Scan — Cross-ICP Run Report (Aggregator)

**Date (CT):** 2026-06-01 (Monday) · **Aggregator stage end:** ~2:32pm CT
**Cycle runtime:** 8:30am (signal-scan-colo) → ~2:32pm (aggregator) ≈ 6h
**Verdict:** ⚠️ QUIET week — **1 total HubSpot signal write fleet-wide**, 0 NEW accounts, 0 Apollo consumed. All 6 per-segment audit files present; all 3 rep DMs dispatched.

---

## 1. Run header
- Per-segment audit files present: **6 / 6** (colo, fiber, neocloud, networkop, msp, enterprise)
- Total HubSpot signal writes across 6 segments: **1** (NeoCloud only — SoftBank AI Cloud)
- Total heat promotions: **1** (SoftBank Cold → Warm)
- Total NEW accounts auto-enriched: **0**
- Apollo consumed fleet-wide: **0 / 250** sub-cap (W22: 0/850, 850 remaining)
- Tag basis: **first post-split Monday** — prior-Monday (2026-05-25) aggregator artifacts ABSENT on disk → everything tagged NEW / CARRYOVER, no source-coverage delta available.

## 2. Per-segment summary
| Segment | Audit | Target | Matched | NEW | Writes | Score dist (8-11/12-17/18-26/27+) | Heat promos | Tier Δ | Apollo | Source cov |
|---|---|---|---|---|---|---|---|---|---|---|
| Colo | ✓ | 459 | 1 | 0 | 0 | 0/0/0/0 (1 below-floor: Digital Realty BCN1 s4) | 0 | 0 | 0/35 | ~8✓/13 |
| Fiber | ✓ | 989 | 1 (dedup no-op) | 0 | 0 | 0/0/0/0 | 0 | 0 | 0/35 | 13✓/13 |
| NeoCloud | ✓ | 154 | 1 | 0 | **1** | 0/0/0/**1** | **1** (Cold→Warm) | 0 (frozen) | 0/55 | ~11✓/13 |
| Network Op | ✓ | 404 | 0 | 0 | 0 | 0/0/0/0 (5 below-floor) | 0 | 0 | 0/50 | ~9✓/22 |
| MSP/Aggregator | ✓ | 336 | 0 | 0 | 0 | 0/0/0/0 | 0 | 0 | 0/20 | 8✓/12 robust |
| Enterprise | ✓ | 8 | 0 | 0 | 0 | 0/0/0/0 | 0 | 0 | 0/55 | ~17✓/33 |
| **TOTAL** | **6/6** | **2,350** | **3** | **0** | **1** | **0/0/0/1** | **1** | **0** | **0/250** | — |

## 3. Cross-ICP heat distribution rollup (today's writes)
Only 1 write today → SoftBank AI Cloud = Warm. Fleet-wide heat **delta vs prior Monday: N/A** (no 2026-05-25 aggregator artifact on disk). For reference, the trailing-30-day signal pool surfaced in rep DMs carries: Hot 14 / Warm 17 / Cool 30 / Cold 0 (61 records).

## 4. Rep DM dispatch table
| Rep | Owner ID | Slack target | Count | NEW | CARRIED | LIGHT (8-11) | CARRYOVER | Top account |
|---|---|---|---|---|---|---|---|---|
| Tim Lieto (East) | 161889085 | U0A973L1HFF (direct) | 28 | 0 | 0 | 6 | 28 (incl 6 LIGHT) | CoreWeave (s33) |
| Ken Cunningham (West) | 162339176 | U0AE1PGCB6C (direct) | 19 | 0 | 0 | 0 | 19 | DataBank (s30) |
| Tim Ziemer (Intl) | 159350430 | U0A24D9RJLS (→ Cooper) | 14 | 1 (SoftBank) | 0 | 0 | 13 | Princeton Digital Group (s30) |

All 3 body DMs + threaded full-list tables dispatched cleanly (no Slack errors, no retries). xlsx written for all 3 reps (one tab per segment + Legend). Tim Z DM annotated "validate before forwarding"; ziemer xlsx written to disk for manual attach.

Fill-down note: natural fresh-signal pool was 1 record (SoftBank, Ziemer). Lieto/Cunningham had 0 fresh in-territory. Per the three-tier fill-down, rep lists were built from the trailing-30-day signal pool (Carryover News). Lieto reached 28 and Cunningham 19; Cunningham could not reach the 25 floor (West 30-day pool exhausted at 19). Ziemer 14 (Intl pool exhausted).

## 5. Source coverage delta vs prior Monday
No prior-Monday aggregator artifact → **no delta computable**. First per-segment baseline established this week. **3-week ✗ streak watches initiated** (auto-flag at 3 consecutive Mondays):
- NeoCloud: IX member pages, Greenhouse/Lever/Ashby job boards
- Network Op: NO-A5 (GitHub commit feeds), NO-A8 (procurement), NO-A9 (job boards), StockTitan/EDGAR direct, supplier newsrooms
- MSP: FCC Daily Digest, Greenhouse/Lever/Ashby TSD boards, CompTIA, FedRAMP Marketplace, Gartner/Forrester, Frost & Sullivan
- Enterprise: American Banker, Modern Healthcare, NelsonHall, several medium-tier (WSJ/CIO Journal, Bisnow, Mergermarket, Crunchbase, HIMSS, RIS, conference agendas)
None are streaks yet (first occurrence).

## 6. Anomalies
1. **[MATERIAL] Stage-1 spec query is broken under event-date semantics.** The aggregator prompt's `last_signal_date = today` query returned **0 records** — correct, because per the 2026-05-28 Signal Engine Unification `last_signal_date` is now the **event date**, not the detection/write date. SoftBank (written today) carries `last_signal_date = 2026-05-25`. The spec'd query will return 0 every Monday going forward. Population was rebuilt from the 6 per-segment audit files (authoritative "what was written today") + a HubSpot 30-day carryover query. **Recommend Cooper patch the aggregator Stage-1 to drive off the audit files and/or `hs_lastmodifieddate = today`.**
2. **No prior-Monday artifacts (2026-05-25).** First Monday after the 2026-05-28 per-segment split; last Monday ran the (now-archived) monolithic and left no aggregator xlsx on disk. All records tagged NEW/CARRYOVER; no source-coverage delta.
3. **BIG Fiber territory misassignment** (320875891447): owner = Tim Z (International) but HQ = Sunnyvale, CA → belongs to Ken/West. Surfaced by the fiber scan; route to R6 / Cooper for correction (not corrected here).
4. **Quiet week is genuine and corroborated**: Colo, Fiber, NetOp, MSP, Enterprise all reported QUIET in-window independently. Material moves clustered just before the 5/18 window edge (Vocus CTO 5/12, AT&T/T-Mobile/Verizon D2D JV 5/14, Heartland Fiber 5/15) — flagged as carryover for the 2026-06-08 window by their segments.

## 7. R3 dup flags (for next 2am ET R3 run)
- **SoftBank AI Cloud** (324007728852, softbank.jp) — domain shared with SoftBank parent; R3 HIGH-priority dedup flagged in the record's own account_brief. NeoCloud scan re-confirms.
- **IREN / Iris Energy** (323971392219 iren.com vs 315977374429 irisenergy.* / 240444244684) — multiple IREN records noted on canvas SF-001; already in R3 queue.
- Digital Realty (193856795322) surfaced below-floor only; already a single pool record, no new dup.

## 8. Apollo budget post-run
- Aggregator consumed: **0** (read-only).
- Fleet-wide Signal Scan consumed: **0 / 250** sub-cap (all 6 segments QUIET, no NEW-account enrichment).
- Weekly W22 (week_start 2026-05-25): **0 / 850** consumed, **850 remaining**.
- Projection for rest of W22: R1 (M-F, ≤30/run), R2 (M-F, ≤50/run), R8 (Fri, 175), R6 (M-F, ≤5/run). Even at sub-caps, weekly draw stays within 850. Ample headroom.

## 9. Tier 3 holds carryover
**0** new signal-scan Tier 3 holds created across all 6 segments this run. No per-segment scan appended a signal-scan Tier 3 item to canvas F0B0AFSB9LN (existing canvas Tier 3 items belong to R0/R1/R3 scopes). Canvas count check: nothing to re-append; **confirmed**. One Run log row appended successfully (verified).

## 10. What needs Cooper's attention (top 3)
1. **Patch the aggregator Stage-1 query.** As written, `last_signal_date = today` returns 0 under event-date semantics — the aggregator only works because it falls back to audit files + 30-day carryover. Make that the documented path, or query `hs_lastmodifieddate = today` scoped to the 5 signal fields. This is the single most important fix.
2. **BIG Fiber → reassign to Ken/West** (HQ Sunnyvale CA; currently Tim Z). Hand to R6.
3. **Quiet-week cadence.** 1 net-new signal fleet-wide. Rep DMs were carryover-filled (working as designed), but if quiet weeks recur, act on the MSP scan's EMEA-source-promotion recommendation and consider widening the 14-day detection window for low-velocity segments. Several strong moves (Vocus, D2D JV, Heartland) sat just outside the window and will likely also miss 2026-06-08 — worth a manual look.

---
*Artifacts: weekly-reports/2026-06-01/weekly-signal-scan-{lieto,cunningham,ziemer}-2026-06-01.xlsx · this report. Canvas F0B0AFSB9LN Run log row appended (⚠️). Apollo budget unchanged (0 consumed).*
