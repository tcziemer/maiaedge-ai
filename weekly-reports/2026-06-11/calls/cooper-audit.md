# Daily Sales Activity Brief - Cooper Audit - 2026-06-11 (Thu)

Run fired 6:01 PM CT / 7:01 PM ET. Status: GREEN. All 6 DMs delivered first attempt.

## Windows + watermark

- Held window (rolling): 2026-06-10 19:01 ET -> 2026-06-11 19:01 ET. Watermark continuous vs prior run (prior held_end 06-10 19:01) - no gap, no widening.
- Set window: same as Held. Upcoming: 06-11 19:01 -> 06-18 19:01 ET.
- Late-log catch-up window: createdate in held window, event-time floor 2026-05-28 19:01 ET. Result: 0 late logs.
- Seen-engagement ledger: loaded 5 entries; 0 candidates filtered (no re-reports); appended 2 new held IDs post-run; nothing older than 30d to trim.

## Engagement pools (raw -> final)

- CALL hs_timestamp in window: 2 (375208925919 Technium/SBA 9:30 ET 12.7min; 375264121548 Mike/Tim 16:00 ET 7.6min). Both Tim Lieto, both HUBSPOT_MEETINGS calendar-sourced, both with transcript.
- MEETING hs_timestamp in window: 2 - both twins of the above, collapsed by fuzzy cluster (title + ts +-90min + owner):
  - MEETING 375024702155 -> CALL 375208925919 (canonical: CALL carries summary + transcript)
  - MEETING 375235111642 -> CALL 375264121548
- Created-in-window (Set superset): 2 CALLs (auto-logs, createdate ~= timestamp, HUBSPOT_MEETINGS -> EXCLUDED from Set) + 2 MEETINGs (true forward bookings -> Set):
  - 375235111642 Mike/Tim: created 14:49 ET for 16:00 ET same day (book-and-hold, legitimate Set + Held overlap)
  - 375214606020 Intro to MaiaEdge / Arc Compute: created 11:30 ET for 6/16 09:00 ET (Tim Z)
- Upcoming pool: 8 raw -> 6 after drops (see below).

## Filters applied

- Internal-Only: both held calls EXTERNAL (Technium + SBA Edge companies; contacts Michael Joseph @techniumnetworking.com, Jared Benson @sbasite.com).
- Skip rules: none triggered (durations 12.7min / 7.6min, summaries present, no Flagged-for-deletion companies).
- Dropped from Upcoming (audit only):
  - MEETING 374854181581 Tim/Sorell 6/16 - internal (Sorell = MaiaEdge Fellow).
  - MEETING 374360388287 untitled, Markus, 6/16 04:30 ET - no title/company. 4th consecutive day. Data hygiene item.
- Non-tracked-owner engagements: none encountered this window.

## FRESH/DEAL classification log

| Engagement | Pool | Tag | Basis |
|---|---|---|---|
| 375208925919 Technium/SBA | Held | DEAL $5k presentationscheduled | Technium - Lab 323891060419 open |
| 375264121548 Mike/Tim | Held | FRESH | zero deals associated to the call object (see hygiene flag - gap, not reality) |
| 375235111642 Mike/Tim booking | Set | FRESH | mirrors canonical call |
| 375214606020 Arc Compute | Set | FRESH | no deals on meeting; net-new account conversation |

## Trend baseline

Trailing 5 weekday files used: 06-04, 06-05, 06-08, 06-09, 06-10.
- held_fresh avg 2.0 (today 1 -> DOWN) · held_deal avg 0.8 (today 1 -> FLAT)
- set_fresh avg 1.4 (today 2 -> FLAT, +20% rule not met on absolute +1) · set_deal avg 1.0 (today 0 -> DOWN)

## Calendar movement (vs 06-10 snapshot)

- NEW: Arc Compute 375214606020 · Tim Z · 6/16 09:00 ET · tier_1 NeoCloud. Rendered in brief (1 item).
- Transitioned to held: Technium/SBA 375024702155 (not DROPPED).
- Unchanged: 702 Communications, Fusion Broadband, Cirrascale, Pearce, FiberLight. No PUSHED / PULLED IN / DROPPED.

## Stage 2.6 calendar-connection health (7d, estimated from run pulls + 06-10 audit)

- Tim Lieto: 6+ calendar-sourced objects (today's 2 HUBSPOT_MEETINGS calls + twins + Cirrascale booking). Healthy.
- Ken Cunningham: 2+ (6/10 Myakka + United Teleports HUBSPOT_MEETINGS calls). Healthy.
- Tim Ziemer: 2 (Pearce 6/10, Arc Compute 6/11 bookings). Healthy.
- Markus Hendrich: 1 (untitled 6/8 artifact) - not zero, but the only calendar object is title-less; tracked as data-quality, not sync-failure.
- No zero-count rep; both held calls calendar-sourced -> no Socket-pattern flag. No Cooper FOR YOU calendar item beyond the Markus untitled note.

## MEDDPICC FILLED / REFRESHED / DRIFT / HELD

Zero writes this run. Native HubSpot smart-fill pass at 22:38Z (5:38 PM CT, pre-fire) had already populated/refreshed all 6 contact-level fields on both call participants with this call's content.

| Contact | Company | Decision | Basis |
|---|---|---|---|
| Jared Benson 465811045113 | SBA Edge | SKIP all 6 | populated + matches most-recent transcript (90-190d circuit delay, stranded assets, REIT cap, pod form factor, #USECASE_INTERNAL) |
| Michael Joseph 424214627034 | Technium | SKIP all 6 | populated + matches (same call) |
| Michael Joseph (Mike/Tim call) | Technium | SKIP | thin transcript, coordination touch - no MEDDPICC-grade evidence; fields current |

Deal-stage gate: Technium - Lab at presentationscheduled (not contractsent / closed) - writes permitted, none needed. Tier 3 holds: 0. Tier 2 DRIFT: 0.

## Data-quality observations (routed to Cooper FOR YOU)

1. Mike/Tim call 375264121548 not associated to open Technium - Lab deal 323891060419. Mechanical FRESH tag understates deal activity (Held mix shows 1F/1D instead of 0F/2D). Suggest associating call -> deal.
2. Markus untitled 6/16 meeting 374360388287 - 4th consecutive day, no title/company.

## FOR YOU routing decisions

- abilash (2): Tier 1 NeoCloud double-booking (Cirrascale 6/15 + Arc 6/16); SBA Edge 1k-2k site program shape + REIT constraint. Basis: Tier 1 logo intros + strategic narrative.
- tim_z (2): SBA Edge outsourced provisioning/monitoring ask via his contact Jared Benson, quote speed = gate; his 4-of-6 meeting load next 7d. Basis: CRO + owns Jared.
- cooper (2): association gap; Markus untitled 4th day + clean calendar health. Basis: data quality + routine health.
- tim_lieto (2): Technium - Lab quote gate (his deal, POC active); Cirrascale 6/15 prep. Basis: owner 161889085.
- ken_cunningham (1): 702 demo Fri 6/12 3:30 ET. Basis: owner 162339176, his only 7d item.
- pt (1): POC - Technium - Lab ticket 310651023072 (stage 3329075934, touched today 14:04 ET) - DIA-to-pod model, pod form-factor fit, quote gate. Basis: POC-attached account with held call today.

## Delivery

| Recipient | Link | Attempt |
|---|---|---|
| Abilash | https://maia-edge.slack.com/archives/D0A2YNPVB96/p1781219208727489 | 1 |
| Tim Z | https://maia-edge.slack.com/archives/D0A2817RE68/p1781219238147209 | 1 |
| Cooper | https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781219271121499 | 1 |
| Tim Lieto | https://maia-edge.slack.com/archives/D0A9UNDR5EW/p1781219300401849 | 1 |
| Ken | https://maia-edge.slack.com/archives/D0AE4AGC5KJ/p1781219316672619 | 1 |
| PT | https://maia-edge.slack.com/archives/D0A28180WG4/p1781219334873249 | 1 |

Shared body byte-identical across all six; only FOR YOU blocks differ. Formatting note: sent as standard markdown (**bold**) per the connected Slack MCP contract (server converts to mrkdwn); tables in code blocks, bullets/blockquotes per prompt.

## Autonomous-run notes

- Canvas F0B0AFSB9LN read returned 948K chars (oversized); run-log row appended as a dated end-of-canvas section matching the established pattern of prior daily-brief rows rather than in-place table surgery. No Tier 3 items of ours pending to drain (0 holds yesterday, 0 today).
- Stage 2.6 used counts derivable from this run + yesterday's audit instead of fresh per-rep 7d count queries (sufficient evidence, all reps clearly above zero).
