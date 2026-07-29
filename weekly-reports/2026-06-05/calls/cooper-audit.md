# Cooper Audit - Daily Sales Activity Brief - 2026-06-05

## Run meta
- Run time: 2026-06-05 19:00 ET (6pm CT fire). Weekday OK.
- Held window: 2026-06-04 19:00 -> 2026-06-05 19:00 ET (rolling prior-run -> now, gapless ~24h).
- Set window: same; true forward MEETING bookings only.
- Upcoming window: 2026-06-05 19:00 -> 2026-06-12 19:00 ET. Upcoming CALL query = 0.
- Tracked sellers: Tim Lieto, Ken Cunningham, Tim Ziemer, Markus Hendrich. (Tory Teague still has no owner ID - not yet added.)

## Dedup
- MEETING 373684232891 -> collapsed into CALL 374116827894 (SBA/Technium twin).
- MEETING 369260239585 -> collapsed into CALL 374223647439 (Movi twin).
- No owner-less duplicates in window this run.

## FRESH/DEAL classification log
| Engagement | Owner | Class | Basis |
|---|---|---|---|
| SBA Edge/Technium 374116827894 | Tim Z | DEAL | Technium-Lab $5k presentationscheduled open |
| Myakka 374164718284 | Ken | FRESH | no associated open deal |
| Movi/HDCO 374223647439 | Tim Lieto | DEAL | HDCO open Movi-CPE $600k qualifiedtobuy + $400k 100G |
| ambiFOX 374199437014 | Tim Z | FRESH | no associated deal |

## MEDDPICC writes (silent side effect)
### Tier 1 fills (1)
- Jared Benson (SBA Edge, id 465811045113) -> meddpicc_pain_contact. Empty pre-write; clear attributable evidence from today's call (circuits arrive after edge site delivered, stalling activation; wants outsourced provisioning + 24/7 monitoring). #PAIN_PROVISIONING #PAIN_OPERATIONAL. Write confirmed (updatedAt 2026-06-05T23:06:26Z).

### Tier 1 refreshes (0) / Tier 2 DRIFT (0) / Tier 3 holds (0)

### Skipped (5)
- Michael Joseph (Technium CTO, num_notes 165): all 6 fields smart-filled today, matches call. Skip.
- Mark Ackaway (Myakka, num_notes 19): competition/criteria/use_case smart-filled today. Skip.
- William Baines (Myakka, @dragonfly.net, num_notes 7): fields smart-filled today; primary company may resolve to Dragonfly (Flagged for deletion). Skip + flag.
- Victor Rodriguez (HDCO/Movi, num_notes 100): all fields smart-filled today. Skip.
- Daniel Gebing (ambiFOX, num_notes 13): comprehensive from prior call; today's logged meeting note adds no new MEDDPICC category. Skip. (s.bartels / Lisa Kemper: admin, no evidence - skip silently.)

Note: HubSpot smart-fill populated most prospect-contact MEDDPICC fields at call-log time (~22:59 ET today). Only Jared Benson's pain field was a clean empty + clear-evidence backfill.

## Data-quality flags
1. Myakka pricing call (374164718284) is associated to Dragonfly Internet (customer_segment = "Flagged for deletion", the acquirer) alongside the active ICP company Myakka. Active prospect contact William Baines carries an @dragonfly.net email. Confirm the primary-company association resolves to Myakka before R4/Flagged-Consolidation touches the Dragonfly parent, so live deal contacts are not swept.
2. SBA Edge is tier_3 Colo in Brazil (international) but the engagement owner is Tim Z (International) - consistent. SBA Edge recent_news empty / signal_heat Cold despite an active partner-brokered intro - candidate for a signal refresh.

## Calendar movement
- NEW: SegraFiber 6/8 (Ken), United Teleports 6/10 (Ken), 702 Communications 6/12 (Ken), Crosslake 6/8 (Tim Lieto).
- PUSHED: Myakka 6/5 -> 6/10 (Ken) - held today, follow-up rebooked.
- TRANSITIONED TO HELD: SBA/Technium (373684232891), Movi (369260239585).
- DROPPED: none. Mplify Board (6/9) unchanged.

## Per-recipient FOR YOU routing decisions
- Abilash (CEO): Movi expansion (customer expansion / board narrative); SBA Edge new logo (partner-led intro).
- Tim Z (CRO): AmbiFox PoC (his own International deal, next steps); Movi expansions advancing under Tim Lieto (supply-chain timing watch).
- Cooper (RevOps): Dragonfly/Myakka data-quality flag; MEDDPICC fill summary (routine health).

## DM delivery
- Abilash U06RVK9NTQR (D0A2YNPVB96) ts 1780700841.910119 - delivered.
- Tim Z U08CMD5PMQE (D0A2817RE68) ts 1780700867.432969 - delivered.
- Cooper U0A24D9RJLS (D0A2YNL1TA4) ts 1780700892.893139 - delivered.
Shared body byte-identical across all three; only FOR YOU differs. Run GREEN.
