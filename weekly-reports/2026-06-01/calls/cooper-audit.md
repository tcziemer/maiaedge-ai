# Cooper Audit - Daily Sales Activity Brief - 2026-06-01

## Run meta
- Run time: 2026-06-01 ~20:13 ET (late fire vs nominal 4pm CT cadence).
- Held window: 2026-05-29 16:00 ET -> 2026-06-01 15:59 ET (Monday weekend catch-up ~72h). End fixed at today 15:59 ET per spec; calls 16:00-20:13 ET today will roll into tomorrow's window.
- Set window: same as held. Upcoming window: now -> +7d.

## Engagement pools
- Held (CALL, timestamp in window): 4 total, all external, all tracked-rep, all survived skip rules.
- Set (MEETING, createdate in window): 5 found; 4 tracked (1 unmapped owner dropped - see below). All 4 FRESH (no open deals).
- Upcoming (MEETING, next 7d): 15 found; 14 tracked (1 unmapped dropped). CALL upcoming: 0.

## Tracked-rep filter - dropped to audit only
- MEETING 373010767566 "Austausch" - owner 164949459 (UNMAPPED, ambiFOX/German), created 6/1, ts 6/2 14:30. Not Lieto/Ken/Ziemer -> excluded from brief table and counts.

## FRESH / DEAL classification (Held)
| Engagement | Company | Class | Open deal |
|---|---|---|---|
| 372458409694 Movi cont'd | HDCO Group | DEAL | Movi - CPE expansion $600k qualifiedtobuy |
| 372844545751 Commercial Discussion | Acuutech | DEAL | Acuutech presentationscheduled (close 4/30 past) |
| 372940742345 Technium POC | Technium | DEAL | Technium - Lab $5k presentationscheduled (close 5/29 past) |
| 373004329678 AT&T Update | AT&T | FRESH | none |

Held mix: fresh 1, deal 3, total 4. Set mix: fresh 4, deal 0, total 4.

## Trend baseline (now LIVE)
Prior runs used: 2026-05-26, 2026-05-27, 2026-05-28 (3 -> trend tags active). Missing: 2026-05-29 (Fri, routine did not fire).
Averages: held_fresh 1.67, held_deal 0.33, set_fresh 3.33, set_deal 0.33.
Tags: Held Fresh FLAT, Held Deal UP, Set Fresh FLAT, Set Deal FLAT.

## Calendar movement
Intended compare = Fri 5/29, but that run did not fire (no upcoming-snapshot.json). Used most-recent available snapshot (Thu 5/28) for a 4-day comparison; noted in brief. No DROPPED items. 3 PUSHED (HDCO/Movi 5/29->6/4, Broadstar+RocNet 5/29->6/2, ONUG 1h minor), 9 NEW (incl. Tier 1 Digital Realty + 1623 Farnam), 3 transitioned-to-held (Acuutech, Technium, AT&T).

## MEDDPICC backfill (silent side effect) - 0 writes
Policy: contact-level fields only; skip closed/contractsent deals; fill empty, refresh-with-care, never degrade.

| Contact | Company | Deal stage | Decision | Reason |
|---|---|---|---|---|
| Victor Rodriguez | HDCO Group | qualifiedtobuy (open) | TIER 3 HOLD | All MEDDPICC fields already richly populated/auto-maintained (num_notes 96). Friday call adds CTO-approval + $500k advance + GPU hosting; buying_process field still reflects pre-approval state - expect HubSpot smart auto-fill to refresh. Held rather than overwrite a rich tagged field. |
| Bhavesh Mehta | Acuutech | presentationscheduled (open) | SKIP | Fields already reflect today's commercial call (18 pilots, 12/36/60 licensing, group CEO stakeholder). meddpicc_pain references older Jan 8 call (topic not central today) -> preserve. |
| Chris Painter | AT&T | no deal (FRESH) | SKIP | MEDDPICC already current and reflects today's call (90-120d provisioning, 200k loc/160 POPs, July mtg, Arun champion). |
| Michael Joseph | Technium | presentationscheduled (open) | SKIP | Today's call = note-taker housekeeping only; fields already tagged NOT_DISCUSSED for this call. No evidence to extract. |

Net writes: 0 (1 Tier 3 hold, 3 skip). Consistent with conservative default-not-to-write and with this tenant's smart-auto-fill owning the MEDDPICC fields.

## Data-quality flags (for Cooper)
- Acuutech deal (312671967952) close date 4/30 in the past.
- Technium - Lab deal (323891060419) close date 5/29 in the past; POC slipped to 6/1.
- HDCO Group (265768509166) is the "Movi" account flagged "company not found" 5/26-5/28 - resolved.
- Sip Navigator + MaiaEdge Intro (372522791611, 372931022529) company association ambiguous (Imperium Data Networks vs Acronym Solutions) - both Tim Z.

## DM delivery
- Abilash (D0A2YNPVB96): first send ts 1780359746.728819 carried Cooper's FOR YOU by mistake; correction DM ts 1780359769.158579 sent with Abilash's FOR YOU. Shared body intact.
- Tim Z (D0A2817RE68): ts 1780359795.206029 - clean.
- Cooper (D0A2YNL1TA4): ts 1780359821.129699 - clean (incl. note of the Abilash correction).
All 3 recipients received the shared body + their correct FOR YOU. Run = YELLOW (one mis-send corrected).
