# Cooper Audit - Daily Sales Activity Brief - 2026-06-10

Run fired ~6:01 PM CT. Status GREEN: 6/6 DMs delivered first attempt, 0 HubSpot writes, 0 errors.

## Windows + watermark
- Held: 2026-06-09 19:00 ET -> 2026-06-10 19:01 ET (rolling prior-run -> now). Watermark CONTINUOUS vs 6/9 run_meta (no widening).
- Late-log catch-up: createdate in same window, hs_timestamp floor 2026-05-27. 0 catch-up hits (all 3 held calls occurred in-window).
- Set: same window, true forward bookings only. Upcoming: -> 2026-06-17 19:01 ET.
- Seen-engagement ledger: 2 entries loaded (6/9), 0 collisions, 3 appended this run.

## Held detection + dedup
3 conversations, each a CALL + MEETING twin pair (6 objects -> 3 canonical):
| Canonical CALL | Collapsed MEETING | Account | Rep |
|---|---|---|---|
| 375023066841 | 374916279996 | BroadStar / RocNet | Tim Lieto |
| 375031178994 | 373499554501 | Myakka | Ken |
| 375056552672 | 374188036845 | United Teleports (via NCTC) | Ken |

## Set measurement (4 true bookings)
- 374916279996 BroadStar quick sync - created 6/9 8:14 PM ET for 6/10 11:00 ET -> forward booking, Tim Lieto, DEAL (book-and-hold; also Held)
- 375024702155 Technium / SBA - created 6/10 for 6/11 9:30 ET, Tim Lieto, DEAL ($5k Technium - Lab, presentationscheduled)
- 375031680752 Cirrascale - created 6/10 for 6/15 16:00 ET, Tim Lieto, FRESH, Tier 1 NeoCloud
- 375026009848 Pearce sync - created 6/10 for 6/16 11:00 ET, Tim Z, FRESH
- EXCLUDED as auto-logs (createdate ~= timestamp, HUBSPOT_MEETINGS): the 3 held CALL objects.

## Trend baseline (5 prior runs: 6/3-6/9)
held_fresh avg 2.0 (today 2 FLAT) - held_deal avg 0.6 (today 1 FLAT, abs delta <1) - set_fresh avg 1.4 (today 2 FLAT, abs delta <1) - set_deal avg 0.6 (today 2 UP).

## Calendar movement vs 6/9 snapshot
NEW x4 (Cirrascale T1, Technium/SBA T2, FiberLight T2 window-roll, Pearce). Transitioned-to-held x2 (Myakka, United Teleports). 702 Comms + Fusion unchanged. 0 PUSHED / PULLED IN / DROPPED.

## Calendar-connection health (Stage 2.6, trailing 7d)
- Tim Lieto: 4+ calendar-sourced objects. Ken: 4+. Tim Z: 1 (Pearce sync). Markus: 1 (the untitled artifact - counts as calendar-sourced, so not a zero flag, but quality-flagged below).
- All 3 held calls were calendar-sourced (HUBSPOT_MEETINGS). No hand-logged-not-calendar-sourced pattern. NO sync flags this run.

## MEDDPICC - 0 writes (FILLED 0 / REFRESHED 0 / DRIFT 0 / HELD 0 / SKIPPED 7)
HubSpot native smart-fill ran at 22:20Z (before this run) and populated all 6 contact-level fields on every associated contact with content extracted from TODAY's calls. Per the matrix (populated + matches most-recent transcript) every field is a silent skip:
- Anthony Salamoni 489067118326 (BroadStar): 6/6 fields current (site-scaled pricing ask, NAT alternative, 4x10 QSFP, wk-of-6/15 install metrics).
- David Clar 415247650542 (RocNet): 6/6 current.
- Mark Ackaway 484589650637 (Myakka): 6/6 current (self-build alternative, E-Rate metrics, MicroTik VLAN criteria).
- William Baines 484536816318: current; @dragonfly.net (parent Flagged for deletion) would gate writes anyway.
- Craig Pedersen / Andrew Esparza (NCTC) / Bob Tynan (RocNet): partner contacts, no deal scope; smart-fill stamped NOT_DISCUSSED variants from the 96s recording. No CRM Guardian action.
Observation for Cooper: the native smart-fill pass is now consistently beating this routine to the write (3rd consecutive run with 0 fills needed). The Stage 5 backfill is becoming a verification layer rather than a writer - fine, but worth knowing.

## Data hygiene flags
1. United Teleports: NO company record exists; held discovery call associated to NCTC + RocNet only. Create + associate. (Also in your FOR YOU.)
2. Fast Wave 323666965217 (Flagged for deletion) still associated to BroadStar call/deal - flagged 6/9, persists. Sever before R4.
3. Dragonfly Internet 322355279547 (Flagged for deletion) associated to Myakka held call.
4. Markus untitled meeting 374360388287 (6/16 4:30 AM ET, no company/title) - 3rd consecutive day. Excluded from Upcoming + Set.
5. United Teleports call recording cut at 96s (notetaker uninvited by NCTC host) - no substantive transcript; Ken asked to debrief.

## Audit-dropped engagements
- MEETING 374854181581 Tim/Sorell 6/16 (internal - MaiaEdge Fellow) - excluded from Upcoming.
- MEETING 374360388287 Markus untitled - excluded (artifact).
- No non-tracked-owner engagements found in any pool this window.

## FOR YOU routing log
- Abilash: Cirrascale T1 calendar add; NCTC channel producing. (2)
- Tim Z: BroadStar leadership pricing decision; small-operator pricing-fit pattern (Myakka + BroadStar). (2)
- Cooper: 4 hygiene items above. (4)
- Tim Lieto: BroadStar proposal gated on pricing + PoC wk 6/15; Technium/SBA 6/11; Cirrascale prep. (3)
- Ken: United Teleports debrief; Myakka post-July-4 reconnect + leave-behind. (2)
- PT: BroadStar PoC install wk 6/15 (Miami Mon/Tue, 4x10 QSFP question, shipment risk). (1)

## DM delivery (all first-attempt)
Abilash https://maia-edge.slack.com/archives/D0A2YNPVB96/p1781132798793699
Tim Z https://maia-edge.slack.com/archives/D0A2817RE68/p1781132823646299
Cooper https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781132851039789
Tim Lieto https://maia-edge.slack.com/archives/D0A9UNDR5EW/p1781132876967519
Ken https://maia-edge.slack.com/archives/D0AE4AGC5KJ/p1781132900966629
PT https://maia-edge.slack.com/archives/D0A28180WG4/p1781132924504809
