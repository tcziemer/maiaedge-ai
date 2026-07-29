# Cooper Audit - Daily Sales Activity Brief 2026-06-12

Run fired 16:10 ET (earlier than the 6pm CT schedule). Delivery: GREEN - all 6 DMs first attempt.

## Run windows
- Held: 06/11 19:01 ET -> 06/12 16:10 ET (rolling prior-run -> now). Watermark continuous (held_start == prior held_end 19:01). No gap back-fill.
- Late-log catch-up: createdate in held window AND hs_timestamp >= 2026-05-29 (14d floor).
- Set: same as held. Upcoming: 06/12 16:10 -> 06/19 16:10 ET (CALL upcoming = 0).

## Pools (after filters)
- Held: 5, all FRESH. Set: 4, all FRESH. Upcoming: 6 (tracked reps).
- Per rep: Tim Lieto 3/1/1, Ken 0/1/0, Tim Z 0/3/4, Markus 1/0/1.

## Dedup / clustering
- CALL 375402556103 (Orchest) canonical; MEETING 375309232868 twin collapsed.
- CALL 375346929351 (702) canonical; MEETING 374027050703 twin collapsed.

## Late-log catch-up
- Lumen MEETING 375421016785 (Tim Z): held 6/10 04:30 ET, logged 6/12 13:47 ET. Surfaced Held [late log]. Not in seen-ledger before this run.

## FRESH/DEAL classification
- All 5 held + all 4 set = FRESH. Orchest, 702 companies have 0 associated deals. GlobalConnect/Lumen have no company record (-> no deal -> FRESH). Set: Orchest (book-and-hold), GDT (Partner Target), Pilot Fiber, Bouygues - none have deals.

## MEDDPICC writes (contact-level; sync up to deal)
| Contact | Company | Field | Action | Tier |
|---|---|---|---|---|
| Gonzalo Gabriel Rico (497845420787) | Orchest Technologies | meddpicc_infrastructure_contact | FILLED (was empty, lifetime calls 1) | Tier 1 fill |

Value written: "Asset-light telecom aggregator. Does not own physical infrastructure; leases Layer 1 / Layer 2 (DWDM) capacity from carriers and resells connectivity to large enterprise clients (referenced JP Morgan Chase) across the Latin American telecom market."

Skipped:
- Gonzalo Rico - pain/use_case/criteria/competition/metrics: not surfaced as a need on exploratory first call (confidence guard).
- 702 (Ken Budd): demo IN_PROGRESS, no content. Skip.
- GlobalConnect (Alexander Hoffmann): 2 sessions, no summary/company. Skip.
- Lumen (David Shacochis): late-log, no summary. Skip.

No deal-level writes (none permitted; all contact-level). No closed-won/lost contacts touched. No contractsent holds. 0 Tier 2 DRIFT, 0 Tier 3 holds.

## Calendar movement (vs 2026-06-11 snapshot)
- NEW: Bouygues Telecom 375421348573 (Markus) 6/17 09:00 ET - Tier 1 Network Operator (France).
- 702 transitioned upcoming->held (not flagged DROPPED; timestamp past at run-time).
- Cirrascale, Arc Compute, Pearce, FiberLight, Fusion Broadband unchanged.
- GDT (6/24) + Pilot Fiber (7/7) booked today but beyond 7d window (Set only).

## Calendar-connection / auto-log health (7d)
- Tim Lieto: healthy (Orchest HUBSPOT_MEETINGS + bookings).
- Ken: healthy (702 HUBSPOT_MEETINGS demo).
- Tim Z: NON-ZERO but quality flag - GlobalConnect (2) + Lumen are manually-logged MEETING objects, no summary, no company association. Routed to Cooper FOR YOU.
- Markus: non-zero (Bouygues booking) + untitled artifact 374360388287.
- No rep at zero. No hard calendar-sync flag.

## Data hygiene flags (-> Cooper)
1. Tim Z GlobalConnect (375419878088, 375401246410) + Lumen (375421016785): no company association, no summary. 3 international touches invisible beyond title.
2. Markus untitled meeting 374360388287 (6/16) - 5th+ consecutive day; recommend delete.
3. Kyle Blackwell (159701452) Oracle/MaiaEdge.io Intro 6/18 - external (Oracle) but untracked owner; not counted in Set/Upcoming.

## FOR YOU routing
- abilash: Tier 1 first-meeting stack (Bouygues/Cirrascale/Arc Compute); all-fresh prospecting day. [2 items]
- tim_z: Markus Bouygues Tier 1 prep; his 4-meeting week; log GlobalConnect+Lumen notes. [3]
- cooper: GlobalConnect/Lumen hygiene; Markus artifact; MEDDPICC 1 fill; trend baseline. [4]
- tim_lieto: Orchest exploratory only; Cirrascale 6/15 prep; booked GDT + Pilot Fiber. [3]
- ken_cunningham: 702 demo in progress - log summary. [1]
- pt: 0 items (no POC-attached accounts in pools); FOR YOU omitted, shared body only.

## DM links
- Abilash: https://maia-edge.slack.com/archives/D0A2YNPVB96/p1781295521952979
- Tim Z: https://maia-edge.slack.com/archives/D0A2817RE68/p1781295542209269
- Cooper: https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781295562832809
- Tim Lieto: https://maia-edge.slack.com/archives/D0A9UNDR5EW/p1781295594454099
- Ken Cunningham: https://maia-edge.slack.com/archives/D0AE4AGC5KJ/p1781295613744839
- Patrick Timmons: https://maia-edge.slack.com/archives/D0A28180WG4/p1781295632198369
