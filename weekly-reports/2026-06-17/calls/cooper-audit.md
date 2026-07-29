# Cooper Audit - Daily Sales Activity Brief - 2026-06-17

Run time: 2026-06-17 19:00 ET (6:00 PM CT fire). Delivery: GREEN, all 7 DMs first attempt.

## Run windows
- Held: 2026-06-16 19:52 ET -> 2026-06-17 19:00 ET (rolling prior-run -> now, ~23h). Watermark continuous: held_start == prior run held_end (6/16 19:52 ET). No gap back-fill.
- Late-log catch-up: createdate in held window AND hs_timestamp >= 2026-06-03 19:00 ET (14d floor). 0 late-log catch-ups (no past-dated meeting was logged in-window). No [late log] tags this run.
- Set: same window as Held. Set = MEETINGs created in-window with a future timestamp; same-day CALL auto-logs (createdate ~= timestamp) excluded.
- Upcoming: 2026-06-17 19:00 ET -> 2026-06-24 19:00 ET.

## Roster change (per prompt standing directive)
- Tory Teague verified active with HubSpot owner ID **165480917** (search_owners). Per the prompt ("once he has an owner ID, add him as a 5th tracked seller everywhere this roster appears"), Tory is added this run to: filter list, bucket list, rep table, rep_breakdown JSON, seen-ledger. Tory held FiberLight (376794629831) today.
- Tracked sellers now (5): Tim Lieto 161889085, Ken Cunningham 162339176, Timothy Ziemer 159350430, Markus Hendrich 164949459, Tory Teague 165480917.

## Per-rep activity
| Rep | SetF | SetD | Held | Up7d |
|---|---|---|---|---|
| Tim Lieto | 0 | 1 | 0 | 4 |
| Ken Cunningham | 0 | 0 | 0 | 0 |
| Tim Ziemer | 0 | 0 | 1 | 0 |
| Markus Hendrich | 0 | 0 | 1 | 0 |
| Tory Teague | 0 | 0 | 1 | 0 |
| TOTAL | 0 | 1 | 3 | 4 |

## FRESH vs DEAL classification log
Held:
- Bouygues Telecom (CALL 376491279095) - 0 deals -> FRESH
- Nexus Data Centers (CALL 376657408735) - 0 deals -> FRESH
- FiberLight (CALL 376794629831) - 0 deals -> FRESH
Set:
- Colony Compute (MEETING 376690168529, booked today 6/17 for 6/22) - open deal "Colony Compute - Pilot" $50k, qualifiedtobuy (not closed) -> DEAL (SetD)

## Trend baseline (today vs trailing 5 weekdays)
- Prior runs used: 2026-06-10, 06-11, 06-12, 06-15, 06-16 (LIVE, 5 on disk)
- Averages: held_fresh 3.8, held_deal 0.6, set_fresh 3.0, set_deal 0.6
- Today: held_fresh 3, held_deal 0, set_fresh 0, set_deal 1
- Tags: held_fresh FLAT (3 vs 3.8; |diff|<1), held_deal FLAT (0 vs 0.6), set_fresh DOWN (0 vs 3.0), set_deal FLAT (1 vs 0.6)

## Calendar movement (vs 2026-06-16 snapshot)
- NEW: Colony Compute (376690168529) 6/22, Tim Lieto, Tier 1 AI colo (DEAL - $50k pilot); GDT (375345631968) 6/24, Tim Lieto, Tier 5 partner target (newly inside 7d window; createdate 6/12)
- PUSHED / PULLED IN / DROPPED: none
- Transitioned to held: Bouygues MEETING twin 375421348573, Nexus MEETING twin 376448123601, FiberLight MEETING twin 375007944392 (all -> their canonical CALLs)
- Reached slot, no notes: Omada follow-up 376435253953 (6/17 2:00pm, Tim Lieto)
- Carried unchanged: Globalgig 6/19 (Tier 2 MSP/Aggregator), Tim Lieto 30-min intro 6/23

## MEDDPICC writes (silent; contact-level)
FILLED (Tier 1):
| Contact | ID | Field | Why |
|---|---|---|---|
| Harold Alexanian (Bouygues) | 465830273757 | meddpicc_use_case | Empty; clear transcript evidence (cross-border Ethernet Federation + sovereign EU routing + instant provisioning). |
| Chuck Girt (FiberLight) | 441475175120 | meddpicc_use_case | Empty; clear transcript evidence (self-service multi-provider provisioning, monetization/marketplace, cloud on-ramp, sovereignty). |

REFRESHED: 0. DRIFT (Tier 2): 0. HOLDS (Tier 3): 0.

SKIPPED:
- Nick Jones (Nexus, 473151480559): all 6 MEDDPICC fields smart-filled from today's transcript - skip-match.
- Kristyn Shaughnessy (Technium, 486150012634): all 6 fields smart-filled today - skip-match.
- Harold/Chuck infrastructure: left empty (call did not detail their own network assets in attributable form; avoid degrading). pain/competition/criteria/metrics for both were HubSpot smart-filled today - skip-match.

Note: contact-level MEDDPICC syncs up to deal-level automatically; no deal-level writes attempted. No contractsent/closed contacts in scope. Write call: 2 processed, 2 updated, 0 failed.

## Stage 5.7 Data Hygiene Auto-Fix
- AUTO-FIX applied: 0. No orphan contact->company associations (all held-call contacts resolve to a single company by business-domain match and are already associated), no unambiguous field corrections surfaced. Colony Compute / GDT upcoming meetings are properly associated to company + deal.
- DEFERRED to owning routine (no Cooper action item):
  - Nexus Data Centers (Texas) owned by Tim Ziemer (International); FiberLight (Texas) owned by Tory Teague - territory re-derive is R6's domain. Defer.
  - Ecoblox (UAE) owned by Tim Lieto (East) - carryover from 6/16; R6 territory. Defer.
  - STACKIT / Schwarz Digits company unenriched - carryover; R1/R2/R10. Defer.
  - Nexus campus-size refresh (CRM 612 MW / 2,000 acres vs today's call 7.2 GW permitted / 3,000 acres / 1.6 GW phase 1) - enrichment narrative field, out of this routine's write scope. Defer to Signal Scan / R2.
- ESCALATED to Cooper: 0 (no orphan not owned by a routine).

## Calendar-connection / auto-log health (Stage 2.6, 7d)
- Tim Lieto: healthy - Colony Compute / Globalgig / GDT / 30-min MEETINGs + Internal Oracle HUBSPOT_MEETINGS call. Omada follow-up reached slot, no notes (logging gap, not sync).
- Tim Ziemer: healthy - Nexus + FiberLight HUBSPOT_MEETINGS calls.
- Markus Hendrich: healthy - Bouygues HUBSPOT_MEETINGS call + MEETING twin.
- Tory Teague: healthy - FiberLight HUBSPOT_MEETINGS call (first tracked activity; calendar-sourced).
- Ken Cunningham: 0 calendar-sourced objects this window; per 6/16 audit, also 0 prior - third straight quiet day. No sign of broken sync (no hand-logged-not-calendar-sourced calls); treated as load/activity signal -> Tim Z, not a Cooper sync flag.
- No Socket-pattern (hand-logged, not calendar-sourced) held calls this run.

## Logging-health items
- Omada follow-up (376435253953, Tim Lieto, 6/17 2:00pm) reached slot, no completion notes -> Tim Lieto + Cooper.
- ambiFOX POC ($50k, presentationscheduled; Markus, 6/16) still no completion notes two days on (absent from today's late-log catch-up) -> PT + Cooper.

## Per-recipient FOR YOU routing
- abilash: Nexus Tier 1 campus kickoff; Bouygues Tier 1 intro; FiberLight + Tory's first call.
- tim_z: Nexus (his call) next step; FiberLight (Tory + him); Ken quiet 3rd day; Bouygues (Markus).
- cooper: Tory roster add; logging health (Omada + ambiFOX); MEDDPICC 2 fills; run health + deferrals.
- tim_lieto: Colony Compute pilot 6/22 (set today); Omada follow-up no-notes; week ahead (Globalgig/30-min/GDT). Filtered to owner 161889085.
- ken_cunningham: 0 owned items -> FOR YOU omitted (shared body only).
- pt: ambiFOX POC no-notes; Nexus/FiberLight shaping toward eval (POC radar).
- hannah: body only, no FOR YOU (per standing rule).

## Delivery (DM links)
- Abilash (U06RVK9NTQR): https://maia-edge.slack.com/archives/D0A2YNPVB96/p1781738066208249
- Tim Z (U08CMD5PMQE): https://maia-edge.slack.com/archives/D0A2817RE68/p1781738091715829
- Cooper (U0A24D9RJLS): https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781738109163989
- Tim Lieto (U0A973L1HFF): https://maia-edge.slack.com/archives/D0A9UNDR5EW/p1781738124183119
- Ken Cunningham (U0AE1PGCB6C): https://maia-edge.slack.com/archives/D0AE4AGC5KJ/p1781738137937119
- PT (U06RVKNTRPB): https://maia-edge.slack.com/archives/D0A28180WG4/p1781738152608559
- Hannah Roberts (U09BYB61FCN): https://maia-edge.slack.com/archives/D0A2HB6T38R/p1781738165725069

## Stage 9 - Cross-routine ledger (canvas F0B0AFSB9LN)
- Tier 3 holds this run: 0 (nothing to drain, nothing to append).
- Canvas is known oversized (>1M chars). Per the prompt's degraded path, with 0 Tier 3 holds nothing accumulates, so the live canvas append was NOT attempted (avoids a 1M-char read into context + phantom double-append). Intended Run-log row recorded here instead:
  `| 2026-06-17 19:00 ET | Daily Sales Activity Brief | ✅ | 3 held (all FRESH, 2 Tier 1: Bouygues + Nexus), 1 SetD (Colony Compute $50k), 4 upcoming; Tory Teague added as 5th tracked seller; 2 MEDDPICC use_case fills; 7/7 DMs GREEN | https://maia-edge.slack.com/archives/D0A2YNL1TA4/p1781738109163989 |`

## Tooling notes
- Association hydration via search_crm_objects associatedWith (companies/contacts/deals/tickets) per the proven pattern; inline associations not returned by the search payload in this tenant.
- Slack standard-markdown contract (**bold**, fenced code blocks, _italic_); arrows rendered as -> ; account-header separator middle-dot.
- No git operations (local markdown only).
