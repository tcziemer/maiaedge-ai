CRM Guardian - Flagged Consolidation - 2026-06-11 - 54 contacts newly flagged, 6 reassociated, 33 Tier 3 held

Run summary: 150 flagged companies processed (page 1 of 305 total; cap 150/run) · 359 contacts evaluated across 77 contact-bearing companies (73 companies had 0 contacts) · 54 net-new Mode B flag writes + 6 reassociations (Tier 1-2) + 33 Tier 3 holds · 320 contacts now carry flagged_for_deletion=true (54 new + 266 idempotent confirms) · ~143 companies fully resolved this run (73 zero-contact + 70 all-contacts-resolved)

WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs the stale associations left by the 6 contact reassociations this run)

Tier 3 holds: 33 preserved contacts with no unique ICP primary to reassociate to (detail table below). 0 company-level holds (no closed-won deals, no open deals, no fresh-record skips, no Enterprise mis-flags in this batch).

Run health: YELLOW
- Writes all succeeded; Tier 3 holds present (preserved contacts awaiting an ICP primary).
- 1 non-fatal error encountered and resolved (see Errors).

Backlog note: 305 flagged companies total; 150 processed this run, ~155 remain for subsequent runs (drains in ~1 more run at 150/run cap).

Errors:
- Contacts object `customer_segment` enum does NOT include `MSP/Aggregator`. On the Symbio reassociation (Jon Cleaver -> Symbio Networks), the segment-mirror write was rejected ("MSP/Aggregator was not one of the allowed options"). Resolved by writing the association + hubspot_owner_id and omitting customer_segment. Allowed contact-level values observed: NeoCloud / Enterprise-CustomerSegment / Network Operator(Tier 1 / VNO) / Data Center Colo Provider / Fiber Operator / Other. ACTION: contact-level segment-mirror on reassociation should skip MSP/Aggregator (and any value not in the contact enum) rather than fail. Company-level segment is unaffected.

================================================================
REASSOCIATIONS (preserved contacts moved to a unique HIGH-confidence ICP primary; Tier 1-2)
================================================================

| Source flagged company | id | Contact | -> ICP primary | Primary id | Primary segment | Owner synced |
|---|---|---|---|---|---|---|
| Symbio | 316528134903 | Jon Cleaver | Symbio Networks | 316502492875 | MSP/Aggregator | 159350430 (segment-mirror skipped, see Errors) |
| EdgeCloudLink | 292754052811 | Guy Marom | EdgeCloudLink (ECL) | 303423288018 | (ICP) | yes |
| EdgeCloudLink | 292754052811 | Yuval Bachar | EdgeCloudLink (ECL) | 303423288018 | (ICP) | yes |
| Bluebird Network | 316163237567 | Benjamin Martens | Bluebird Network | 323821758151 | Fiber Operator | 161889085 (Tim Lieto) |
| Bluebird Network | 316163237567 | Chris Melloway | Bluebird Network | 323821758151 | Fiber Operator | 161889085 (Tim Lieto) |
| HyperLink Infrastructure | 316164220626 | Michael Hall | HyperLink Infrastructure | 298009434824 | Fiber Operator | 161889085 (Tim Lieto) |

================================================================
MODE B FLAGS (contacts set flagged_for_deletion=true; 54 net-new this run)
================================================================
Net-new flag writes by partition:
- ColoHouse (254570392308): Steve Chapin - was flagged_for_deletion=false on a flagged company, corrected to true (not preserved, no ICP primary).
- 5c.ai (303285145301): 8 contacts (all flagged=false -> Mode B; "5C Data Centers" name-token rejected as different entity).
- Edged Data Centers (251566704352): 4 contacts (Edged Energy edged.us is active ICP but contacts not preserved).
- Partition D long tail: 41 net-new flags across wilson-global, CTel, ATxTel, 128 Technology, toto networks, Virtustar, Ni2, Cloud Age, rackonomics, MANGO-OMC, CarrierX, Corero, On Air Telecom, All Access Telecom, Sify, Steadfast, Rowan Digital, EIS Visual, PowerBridge, Backbone Digital, Troy Cablevision, Saturn Cloud, Hivenet, Atlantic Metro, nFrame, Essextel, Casair, HyperLink, Dorial Telecom, Sumauma(0 - all preserved), etc.

A further ~266 contacts across NSW (120), nFrame/Expedient (45), FPL FiberNet (26), Lightower (13), US Internet (7), Lanck (7), Netmore (5), Bulk (5), and small companies already carried flagged_for_deletion=true (idempotent confirms; no write needed).

================================================================
TIER 3 HELD (preserved contacts; NO write - awaiting ICP primary or manual disambiguation)
================================================================

| Company | id | Held contacts | Reason |
|---|---|---|---|
| Shaw | 268241651447 | 14 (all) | Two Rogers primaries (Rogers Communications 317259348704 Fiber Operator; Rogers Communications Canada Inc. 251587604216 Network Operator(Tier 1/VNO)) - no unique HIGH; cannot safely reassociate. Disambiguate canonical Rogers primary, then a follow-up R4 pass reassociates. All 14 already flagged=true. |
| FPX AI | 311392963281 | 4 (Dhyay Bhatt 499014385355, Veronika Bhatt 499007497938, Colin Sharkey 451518850806, Niraj Yagnik 451588830920) | Preserved (2 fresh createdate >=2026-05-28; Colin contacted 2026-04-14; Niraj updated 2026-03-16). No ICP primary for fpx.world / "FPX". |
| Novita AI | 300372855493 | 3 (Ding Wang 499028985573, Wayne Wong 499009956581, Ben Li 498971625146) | Fresh records, createdate 2026-06-08. |
| Backbone Digital | 292440159935 | 2 (Nate Hubert 457325245128, Dave Perrill 425980340966) | Preserved (notes_last_updated 2026-03-17). No ICP primary for backbone.digital. |
| Saturn Cloud | 297918677722 | 2 (Sebastian Metti 451588831988, Hugo Shi 499014648564) | Sebastian preserved (notes 2026-03-16); Hugo fresh (createdate 2026-06-08). No ICP primary. |
| Sumauma | 167113651945 | 2 (Paulo Machado 261906818771, Macatoci Kanashiro 261906818770) | Preserved (notes 2026-05-15 / 2026-05-29). No ICP primary for sumaumatelecom.com.br. |
| ISG | 194005222095 | 2 (Lynn Bruns 486369299174, Leila Hussein 90767828679) | Lynn preserved (notes 2026-06-04), ISG Technology primary 264035618536 domain-mismatch (is-grp.com != isgtech.com) - not unique HIGH. Leila lifecyclestage=other - protection filter. |
| Manor | 316508757740 | 1 (Mohammed Nazrul Islam 465834282718) | Preserved (notes_last_updated 2026-04-27). No ICP primary for manor.net. |
| Truepacket | 132996276936 | 1 (Rob Schumann 487432186604) | Preserved (notes 2026-05-05). No ICP primary for truepacket.io. |
| FlowSec | 193865438923 | 1 (Rami Yaron 297261432562) | Preserved (notes 2026-03-31). No ICP primary for flow-sec.com. |
| CarrierX | 209233708749 | 1 (Michael Ching 494765969108) | Preserved (notes 2026-06-03). No ICP primary for carrierx.com. |
| Essextel | 303896262390 | 1 (Steven Garvin 441467623152) | Preserved (notes_last_updated 2026-04-23). No ICP primary for essextel.com. |
| LS Power | 311418164947 | 1 (Jason Scandrol 455480763107) | Preserved (notes_last_updated 2026-03-16). No ICP primary for lspower.com in ICP segments. |

Tier 3 contact total: 33.

================================================================
NOTABLE FINDINGS (for R3 / Cooper - duplicate / sourcing follow-ups)
================================================================
- FPL FiberNet (254547320539): all 26 contacts are @crowncastle.com. Crown Castle (303890867935, Fiber Operator) is an active ICP record. Looks like a stale duplicate import of an early Crown Castle brand. Contacts not preserved so Mode B was correct, but R3/Cooper should consider merging/archiving the FPL FiberNet company record directly.
- nFrame (Expedient) (193853915836, 45 contacts @expedient.com) and nFrame (303849415362): no active Expedient ICP record exists to reassociate to. Expedient is a real colo/managed-services provider - candidate for R1 re-evaluation / fresh sourcing.
- Shaw -> Rogers: two competing Rogers primary records (Fiber Operator vs Network Operator(Tier 1/VNO)) need de-duplication (R3) before the 14 held Shaw contacts can be reassociated.

================================================================
RUN PARAMETERS
================================================================
- Activity window cutoff (90d, ET): 2026-03-13. Fresh-record cutoff (14d, ET): 2026-05-28.
- ICP primary segments: Data Center Colo Provider / Fiber Operator / Network Operator(Tier 1 / VNO) / MSP/Aggregator / NeoCloud / Enterprise-CustomerSegment.
- No Apollo calls (R4 is HubSpot-internal). All writes confirmationStatus=CONFIRMATION_WAIVED_FOR_SESSION.
- Reference: scheduled-task prompt (inlines pre-deletion-audit Steps 0-5, 6-signal preservation, Mode A/B). MaiaEdge own record 124293230301 excluded.
