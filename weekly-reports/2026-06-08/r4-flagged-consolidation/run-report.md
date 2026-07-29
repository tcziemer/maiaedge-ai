CRM Guardian - Flagged Consolidation - 2026-06-08 - 332 contacts flagged, 4 reassociated, 13 Tier 3 held

Run summary: 247 flagged-company pool · 150 in-cap processed (oldest by hs_object_id ASC; 97 carried to next run) · 75 with-contacts + 75 zero-contact · 349 contacts evaluated · 332 new Mode B flags (flagged_for_deletion=true) · 2 already-flagged (idempotent, no write) · 4 Mode A reassociations · 0 clears · 0 protection skips · 13 Tier 3 holds · 336 HubSpot writes · 0 hard stops (0 closed-won, 0 open deals, 0 open POC tickets across the 150; 0 Enterprise C-bis mis-flags)

WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs the stale associations left by the 4 reassociated contacts)

Tier 3 holds this run (13): preserved contacts on flagged non-fit/defunct/duplicate companies with no non-flagged ICP primary available for reassociation (held, not flagged, not reassociated) + 1 too-new company. Detail in the table below. Standing carryover (outside today's oldest-150 batch): Fast Wave (323666965217) - open-deal mis-flag from 2026-06-05, awaiting Cooper to remove flag + reclassify.

Run health: YELLOW
- Writes succeeded; Tier 3 holds present (preserved contacts with no ICP primary). No fatal errors.

Errors: None

---

## Reassociations (Mode A - preserved contact moved to non-flagged ICP primary; segment + owner synced)

| Contact ID | From (flagged company) | To (ICP primary ID) | Primary name |
|---|---|---|---|
| 486362106616 | Bluebird Network (316163237567) | 323821758151 | Bluebird Network |
| 476652573403 | HyperLink Infrastructure, LLC (316164220626) | 298009434824 | HyperLink Infrastructure |
| 451559667429 | Edged Data Centers (251566704352) | 251592703686 | Edged Energy |
| 467679488707 | Airtel Business (317223880415) | 316280383164 | Airtel Business |

## Mode B flags (flagged_for_deletion=true) by slice

| Slice | Companies | Contacts evaluated | New flags | Already flagged | Reassoc | Tier 3 |
|---|---|---|---|---|---|---|
| 1 | 1 | 120 | 120 | 0 | 0 | 0 |
| 2 | 12 | 56 | 55 | 0 | 1 | 2 |
| 3 | 20 | 58 | 53 | 0 | 1 | 3 |
| 4 | 21 | 58 | 54 | 2 | 1 | 1 |
| 5 | 21 | 57 | 50 | 0 | 1 | 6 |
| zero-contact | 75 | 0 | 0 | 0 | 0 | 1 |
| **TOTAL** | **150** | **349** | **332** | **2** | **4** | **13** |

Note on Mode B volume: this batch carried an unusually large new-flag count driven by NSW (266871288514, 120 contacts - Norddeutsche Seekabelwerke / Prysmian, a subsea-cable MANUFACTURER, D1-disqualified). All 120 NSW contacts were leads with no activity in the 90-day window, none opted out, none on open deals/POCs - flagged per Mode B. The full new-flag contact-ID lists are in the per-slice subagent outputs (HubSpot is the source of truth; filter Contacts -> flagged_for_deletion=true for the live set).

## Tier 3 held detail

| Company ID | Company | Reason |
|---|---|---|
| 316528134903 | Symbio | Preserved contact (Jon Cleaver, notes_last_updated 2026-04-28); no ICP primary on exact domain/name (symbio.one is segment Other) |
| 316538883827 | IP Transfer | Preserved contact (Joseph Yapsuga, notes_last_updated 2026-04-16); no ICP primary |
| 292754052811 | EdgeCloudLink | Preserved contacts (Guy Marom, Yuval Bachar); no ICP primary |
| 167113651945 | Sumauma | Preserved contacts (Paulo Machado, Macatoci Kanashiro); no ICP primary |
| 132996276936 | Truepacket | Preserved contact (Rob Schumann); no ICP primary |
| 194005222095 | ISG | Preserved contact Lynn Bruns (notes_last_contacted 2026-06-04); no non-flagged ICP primary (ISG Technology isgtech.com is distinct) |
| 209233708749 | CarrierX | Preserved contact (Michael Ching, createdate>=2026-05-25); no non-flagged ICP primary |
| 209237307100 | Corero | Preserved contact (Michael Honeycutt, notes_last_updated 2026-03-12); no non-flagged ICP primary |
| 264355635947 | Steadfast Networks | Preserved contact (Jacob Hinton, notes_last_updated 2026-03-16); no non-flagged ICP primary (Hivelocity not exact match) |
| 303896262390 | Essextel | Preserved contact (Steven Garvin, notes_last_updated 2026-04-23); no non-flagged ICP primary |
| 193865438923 | FlowSec | Preserved contact (Rami Yaron, notes_last_updated 2026-03-31); no non-flagged ICP primary |
| 316508757740 | Manor | Preserved contact (Mohammed Nazrul Islam, notes_last_updated 2026-04-27); no non-flagged ICP primary |
| 326259493574 | Komodor | Invariant E: created 2026-06-05, too new (<14 days) |
| 323666965217 | Fast Wave (carryover 2026-06-05) | Open-deal hard stop (Invariant D): open deal 'Broadstar - New Logo' $10K, presentationscheduled. Likely upstream mis-flag. Recommend remove Flagged-for-deletion + reclassify; resolve deal. (Outside today's oldest-150 batch.) |

## Carry-forward

97 flagged companies remain beyond today's 150-company cap (247 pool - 150 processed). They drain on the next R4 run (oldest by hs_object_id ASC). No Apollo consumed (R4 is HubSpot-internal). MaiaEdge own record (124293230301) excluded by scope.
