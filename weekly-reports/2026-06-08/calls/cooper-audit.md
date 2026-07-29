# Cooper Audit - Daily Sales Activity Brief - 2026-06-08

## Run meta
- Run time: 2026-06-08 19:00 ET (6pm CT fire).
- Held window: 2026-06-05 19:00 -> 2026-06-08 19:00 ET (rolling prior-run -> now, gapless Monday weekend catch-up ~72h; prior lastRunAt = Fri 6/5 19:00).
- Set window: same as held; 0 true external forward bookings.
- Upcoming window: 2026-06-08 19:00 -> 2026-06-15 19:00 ET; CALL upcoming = 0; 5 tracked-rep MEETINGs.
- Tracked reps: Tim Lieto (161889085), Ken Cunningham (162339176), Tim Ziemer (159350430), Markus Hendrich (164949459). Tory Teague still no owner ID.

## Engagement accounting
Held pool raw: 2 CALL + 3 MEETING in window.
- Segra CALL 374669997774 (+ MEETING twin 374199263980 collapsed) -> 1 held external call (Ken, FRESH).
- Sync Dario & Markus CALL 374583576275 (+ MEETING twin 374268543684) -> internal, dropped.
- Crosslake MEETING 374116121297 -> external, no content, dropped (window boundary).
Set pool raw: 2 MEETING created in window.
- Dario/Markus 374268543684 -> internal, drop.
- Untitled Markus 374360388287 (ts 6/16) -> no company/title, not counted as Set; outside 7-day upcoming window.
Net: Held 1, Set 0, Upcoming 5.

## FRESH/DEAL classification
- Segra: 0 associated deals -> FRESH.

## Pipeline mix + trend
- Held fresh/deal/total: 1/0/1. Set: 0/0/0.
- Trailing 5-weekday avg (6/1-6/5): held_fresh 2.4, held_deal 1.4, set_fresh 2.0, set_deal 0.2.
- Tags: held_fresh DOWN, held_deal DOWN, set_fresh DOWN, set_deal FLAT. Status LIVE (5 prior runs).

## Calendar movement vs Fri 6/5 snapshot
- NEW: Fusion Broadband (368678544084) 6/15 - Tim Z - pre-existing meeting rolled into horizon.
- transitioned_to_held: Segra (374669997774, real); Crosslake (374116121297, no content).
- 702 Communications 6/12 19:00->19:30 (<1h, noise, ignored). Mplify / Myakka / United Teleports unchanged. No PUSHED/PULLED IN/DROPPED.

## MEDDPICC writes (founder-invisible)
### Tier 1 FILLED
| Contact | Company | Fields | Evidence |
|---|---|---|---|
| Steve Hartman (id 297204007630) | Segra (Fiber, tier_2) | meddpicc_pain_contact, meddpicc_use_case | Segra demo 6/8: 90-day build delay risks customer loss, wants minutes-not-months provisioning on owned fiber; fiber operator monetizing 45k+ mi network via instant automated L2 + off-net reach / infra sharing. Both fields empty pre-write (num_notes 6). |
### Skipped (preserve)
- Steve Hartman meddpicc_metrics_contact + meddpicc_infrastructure_contact: already richly smart-filled today (lastmodified 22:56Z) - skip.
- Steve Hartman meddpicc_criteria_contact + meddpicc_competition_contact: decision criteria not discussed; no NaaS-fabric competitor named (off-net buys from Cox/Charter only) - skip.
### Tier 2 DRIFT: none. ### Tier 3 holds: none.

## Data-quality / routine-health flags (-> Cooper)
1. Markus Hendrich engagements lack company associations: "Sync Dario & Markus" (internal advisor sync) and untitled 6/16 booking (374360388287) both have 0 company - they can't be tracked as prospect activity, and the untitled booking is unclassifiable as a Set/prospecting signal. Recommend Markus associate companies on his HubSpot meetings.
2. Crosslake meeting (374116121297, Tim Lieto, 6/8 19:00 ET) reached its scheduled slot at window close with no summary/transcript; will surface in tomorrow's held window if notes land.
3. Dario Mussi (contact 469424617178) is a MaiaEdge advisor on a personal gmail; treated as internal for the Internal-Only Filter. If he should be excluded by domain, consider tagging him internal in HubSpot.

## FOR YOU routing decisions
- Abilash: Segra new-logo intro (notable TAM fiber logo).
- Tim Z: Segra follow-up nudge (no next step locked) + rep-load note (Ken-loaded week; Tim Lieto/Markus 0 external held).
- Cooper: 3 data-hygiene/health flags above + trend status + MEDDPICC fill count.

## DM delivery
- Abilash D0A2YNPVB96 ts 1780959952.909469 delivered.
- Tim Z D0A2817RE68 ts 1780959967.486229 delivered.
- Cooper D0A2YNL1TA4 ts 1780959983.196789 delivered.
All 3 shared-body byte-identical; FOR YOU unique per recipient. Run status GREEN.
