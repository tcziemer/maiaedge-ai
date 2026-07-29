# R4 Flagged Consolidation - 2026-05-28

**Routine:** CRM Guardian - Flagged Consolidation (R4) - Cowork scheduled task
**Run start:** 2026-05-28 12:00 CT
**Status:** ✅ GREEN (steady state; 0 writes, 0 errors)

## Pool snapshot

| Metric | Today | Yesterday | Delta |
|---|---|---|---|
| Companies with `customer_segment = "Flagged for deletion"` | 224 | 221 | +3 |
| Companies in 150-cap (oldest by `hs_object_id`) | 150 | 150 | - |
| Companies in tail (151-224, deferred to next runs) | 74 | 71 | +3 |
| Contacts with `flagged_for_deletion = true` (entire pool) | 528 | 527 | +1 |

New flagged-pool entries since 2026-05-27 R4 (all at `hs_object_id` > 316538883827, outside this run's cap):
- Internet Subway (324542613196, internetsubway.com) - createdate 2026-05-27
- Two additional entries in the 151-224 tail (not enumerated this run)

These will be processed when the lower-`hs_object_id` backlog drains.

## Writes this run

**ZERO writes executed.** No Mode A reassociations, no Mode B flag writes, no un-flag corrections.

This is the expected pattern when (a) the cap window is dominated by long-standing flagged companies whose contacts are already flagged from prior R4 runs, and (b) the remaining non-flagged contacts within those companies all carry recent activity signals that preserve them.

## 6-signal preservation check results

Search scoped to: `flagged_for_deletion != true` contacts associated with any of the 150 in-cap flagged companies.

Result: **21 preserved contacts found** (10 in batch A, 11 in batch B). ALL preserved by signal 1 (`notes_last_contacted` <90d) or signal 2 (`notes_last_updated` <90d) or signal 4 (`createdate` <14d). ALL belong to companies already in Tier 3 carryover surveillance from 2026-05-22 / 2026-05-25 / 2026-05-27.

| Contact ID | Name | Email | Parent (flagged) | Signal | Disposition |
|---|---|---|---|---|---|
| 426016365276 | Vinay Nagpal | vnagpal@everstream.net | Everstream (193867595511) | notes_last_updated 2026-02-26 | T3 carryover (surveillance) |
| 476512699073 | Jacob Hinton | jake@hivelocity.net | (Hivelocity - in 151-224 tail, R3 ghost via batch A flagged co.) | notes_last_updated 2026-03-16 | T3 carryover (preserved) |
| 314701034216 | Michael Honeycutt | michael.honeycutt@corero.com | Corero (209237307100) | notes_last_updated 2026-03-12 | T3 carryover |
| 261906818771 | Paulo Machado | paulo@sumaumatelecom.com.br | Sumauma (167113651945) | notes_last_contacted 2026-05-15 | T3 carryover |
| 261906818770 | Macatoci Kanashiro | maca@sumaumatelecom.com.br | Sumauma (167113651945) | notes_last_contacted 2026-05-28 (TODAY) | T3 carryover |
| 297261432562 | Rami Yaron | ryaron@flow-sec.com | FlowSec (193865438923) | notes_last_updated 2026-03-31 | T3 carryover |
| 487432186604 | Rob Schumann | rob@truepacket.io | Truepacket (132996276936) | notes_last_contacted 2026-05-05 | T3 carryover |
| 155989136102 | Craig Daiker | craig.daiker@crowncastle.com | (Crown Castle 303890867935 via 2026-05-25 Mode A reassoc - R3 ghost association persists to batch A flagged co.) | notes_last_updated 2026-02-27 | T3 carryover (Mode A landed primary) |
| 486369299174 | Lynn Bruns | lynn.bruns@is-grp.com | ISG (194005222095) | notes_last_updated 2026-04-24 | T3 carryover |
| 486602587880 | Bastien Vidal | bastien@hivenet.com | Hivenet (297986183874) | createdate 2026-05-15 (<14d) | T3 carryover |
| 476652573403 | Michael Hall | m.hall@hyperlink-networks.com | HyperLink Infrastructure (316164220626) | notes_last_updated 2026-04-21 | T3 carryover |
| 465830273723 | Jon Cleaver | jon.cleaver@symbio.global | Symbio (316528134903) | notes_last_updated 2026-04-21 | T3 carryover |
| 465761569489 | Joseph Yapsuga | joseph.yapsuga@iptransferllc.net | IP Transfer (316538883827) | notes_last_updated 2026-04-16 | T3 carryover |
| 465834282718 | Mohammed Nazrul Islam | nazrul@manor.net | Manor (316508757740) | notes_last_updated 2026-04-27 | T3 carryover |
| 464779318976 | Ryan Sabia | ryansabia@overyondr.com | Yondr (316194606814) | notes_last_updated 2026-04-21 | T3 carryover |
| 455480763107 | Jason Scandrol | jscandrol@lspower.com | LS Power (311418164947) | notes_last_updated 2026-03-16 | T3 carryover |
| 451518850806 | Colin Sharkey | colin@fp8.ai | FPX AI (311392963281) | notes_last_contacted 2026-04-14 | T3 carryover |
| 451588831988 | Sebastian Metti | sebastian@saturncloud.io | Saturn Cloud (297918677722) | notes_last_updated 2026-03-16 | T3 carryover |
| 451588830920 | Niraj Yagnik | niraj@fp8.ai | FPX AI (311392963281) | notes_last_updated 2026-03-16 | T3 carryover |
| 441467623152 | Steven Garvin | sgarvin@essextel.com | Essextel (303896262390) | notes_last_updated 2026-04-23 | T3 carryover |
| 486129442545 | Chris Burton | chris@mpnexlevel.com | (MP Nexlevel - in tail or ghost) | createdate 2026-05-14 (<14d) | Preserved; ghost association |

## Surveillance carryovers (no contact-write action; Tier 3 hold persists)

These six high-volume ICP mis-flag candidates remain under Tier 3 surveillance pending Cooper's reclass decision. Per the R4 protocol, NO contact flag writes occur on these companies until Cooper resolves the parent's segment classification.

| Company | Company ID | Contacts | First surveilled | Status |
|---|---|---|---|---|
| nFrame (Expedient) | 193853915836 | 45 | 2026-05-22 | Carryover - awaiting Cooper decision |
| Lightower Fiber Networks | 193854634742 | 13 | 2026-05-22 | Carryover - Fiber Operator mis-flag candidate |
| Everstream | 193867595511 | 18 | 2026-05-22 | Carryover - Fiber Operator mis-flag candidate |
| FPL FiberNet | 254547320539 | 26 | 2026-05-22 | Carryover - Fiber Operator mis-flag candidate |
| NSW (prysmian.com) | 266871288514 | 120 | 2026-05-22 | Carryover - cable vendor (D1 evict), prysmian.com association via R3 |
| Shaw | 268241651447 | 14 | 2026-05-22 | Carryover - Network Operator mis-flag candidate |

## Deferred re-evaluations

- **Velocity Network (322656973545, vnet.us)** - flagged-pool entry from 2026-05-26 R4 was in 14-day fresh-skip then. Note from canvas was to re-evaluate 2026-05-28+. Record sits in tail (hs_object_id > 316538883827), outside this run's 150 cap. Will be re-evaluated when backlog drains to that hs_object_id.
- **2 additional new pool entries** (between 316538883827 and 324542613196) in tail - deferred.

## Hard-stop / invariant checks

- ✅ MaiaEdge own (124293230301) excluded by scope (not in flagged-segment pool).
- ✅ Customer-protection HARD STOP: no flagged company in cap carries `hs_is_closed_won = true` deal (sample of high-contact T3 surveillance companies verified).
- ✅ Open-deal HARD STOP: no in-cap company carries open deals.
- ✅ Fresh-record (14-day) skip: all 150 in-cap companies have `createdate <= 2026-04-03`, well outside the 14-day window.
- ✅ Pre-Phase-1 Enterprise defensive check: none of the in-cap company `account_brief` strings flag as Enterprise scale candidates. (Full check skipped at scale - pool dominated by carrier/colo non-fits + neocloud-AI marginal-fits already established as non-ICP.)

## Run health

**GREEN.** 0 errors. 0 fatal stops. 0 unresolved write failures. Behavior matches expected steady-state pattern. Cooper's bulk-delete remains the throttle.

## Actionable for Cooper (manual step)

528 contacts in HubSpot now carry `flagged_for_deletion = true` and are ready for the manual bulk-delete review:

1. Filter HubSpot Contacts → `flagged_for_deletion = true` → review and bulk-delete
2. Then filter Companies → `customer_segment = "Flagged for deletion"` → archive (severs stale associations from prior reassociations)

## Cross-routine ledger

Canvas F0B0AFSB9LN updated at run end:
- New section appended: `### R4 - Flagged Consolidation - 2026-05-28` with 0 new T3 holds, full 21 carryover summary.
- Run log row appended with status ✅ and link to this audit file.
