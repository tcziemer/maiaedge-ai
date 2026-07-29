CRM Guardian - Flagged Consolidation - 2026-06-01 - 3 contacts flagged, 0 reassociated, 0 new Tier 3 held

Run summary: 150 flagged companies processed (in-cap) · 125 not-yet-flagged contacts evaluated on the 67 in-cap companies that carry contacts (big-6 surveillance set evaluated as carryover, see below) · 3 Tier 1 Mode B flags / 0 Mode A reassociations / 0 un-flag corrections / 0 NEW Tier 3 holds · 0 errors

Pool: 243 flagged companies (+19 since 2026-05-28's 224). In-cap = first 150 by hs_object_id ASC. Off-page tail = 93 (hs_object_id > 316298284744) deferred to next run.

WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (this severs the stale associations from reassociated contacts)

Cooper bulk-delete actionable: ~531 contacts with flagged_for_deletion = true (prior 528 on 2026-05-28 + 3 from this run; HubSpot is source of truth for the exact live count).

Run health: GREEN
- 0 errors, 0 customer-protection HARD STOPs, 0 open-deal HARD STOPs, 0 fresh-record skips in-cap, 0 mis-flag investigations, all 3 writes succeeded.
- Carryover Tier 3 holds present (preserved-contact companies + big-6 surveillance) but 0 NEW this run, so GREEN per the established convention.

Errors: None

---

INVARIANT CHECKS (in-cap 150)
- C Customer protection (closed-won): 0 flagged companies carry deals. No HARD STOP.
- D Open-deal HARD STOP: 0 deal-bearing companies in-cap. No skips.
- E Fresh-record (createdate within 14d, cutoff 2026-05-18): 0 in-cap (latest company createdate is 2026-04-01). No skips.
- C-bis Pre-Phase-1 Enterprise defensive check: 0 in-cap companies match an Enterprise vertical (no bank/insurer/hospital/health-system/retailer/distribution/BPO scale profile). No Enterprise mis-flag holds.

---

MODE B FLAGS (Tier 1, surfaced) - 3 contacts

| Contact | ID | Email | Company (flagged) | Createdate | Reason |
| --- | --- | --- | --- | --- | --- |
| Bastien Vidal | 486602587880 | bastien@hivenet.com | Hivenet (297986183874) | 2026-05-15 | No notes activity; lifecyclestage=lead; 0 deals; 0 POC; not opted-out; 14-day fresh window expired. Hivenet's only contact -> Hivenet drops off the carryover T3 list. |
| Anuj Malhotra | 486598631146 | anuj.malhotra@sifycorp.com | Sify Technologies Ltd. (251651866344) | 2026-05-15 | No notes activity; lifecyclestage=lead; 0 deals; 0 POC; not opted-out; 14-day fresh window expired. |
| Sharad Agrawal | 487432186600 | sharad.agrawal@sterlingwilson.com | (assoc. flagged co, Edged cluster) | 2026-01-30 | No activity since creation; lifecyclestage=lead; 0 deals; 0 POC; not opted-out. Long-dormant, clean Mode B. |

---

MODE A REASSOCIATIONS - 0

No HIGH-confidence ICP-primary duplicate match surfaced for any preserved contact in-cap. (R3 Duplicate Accounts owns dedup-primary reassociation; nothing handed to R4 this run.)

---

PRESERVED CONTACTS - carried as Tier 3 (no ICP primary, no action) - all CARRYOVER, 0 NEW

Preserved-contact companies (recent activity within 90d, cutoff 2026-03-03):
- HyperLink Infrastructure (316164220626) - Michael Hall, notes 2026-04-21
- Yondr (316194606814) - Ryan Sabia, notes 2026-04-21
- LS Power (311418164947) - Jason Scandrol, notes 2026-03-16
- FPX AI (311392963281) - Colin Sharkey (notes 2026-04-14) + Niraj Yagnik (2026-03-16)
- Saturn Cloud (297918677722) - Sebastian Metti, notes 2026-03-16
- Edged Data Centers (251566704352) - Frank Scandariato, notes 2026-03-16
- Essextel (303896262390) - Steven Garvin, notes 2026-04-23
- Corero (209237307100) - Michael Honeycutt, notes 2026-03-12
- Bluebird Network (316163237567) - Chris Melloway, notes 2026-04-22
- Sumauma (167113651945) - Paulo Machado (2026-05-15) + Macatoci Kanashiro (2026-05-29)
- FlowSec (193865438923) - Rami Yaron, notes 2026-03-31
- Truepacket (132996276936) - Rob Schumann, notes 2026-05-05

R3 ghost associations (preserved, no action): Hivelocity/Jacob Hinton (476512699073), Crown Castle/Craig Daiker, MP Nexlevel/Chris Burton (486129442545, already flagged).

---

BIG-6 CARRYOVER SURVEILLANCE (contact-heavy, awaiting Cooper reclass decision) - unchanged

Excluded from per-contact re-fetch this run (established T3 surveillance, contacts already evaluated/flagged in prior runs; re-fetching adds nothing):
- nFrame (Expedient) 193853915836 (45 contacts) - MSP reclass candidate
- Lightower Fiber Networks 193854634742 (13) - archive + reassoc candidate
- Everstream 193867595511 (18) - Fiber Operator reclass candidate
- FPL FiberNet 254547320539 (26) - Fiber Operator reclass candidate
- NSW / Prysmian 266871288514 (120) - cable manufacturer, manual contact-preservation pass
- Shaw 268241651447 (14) - dead-brand archive candidate

---

DEFERRED (off-page, hs_object_id > 316298284744) - 93 companies for next run
Includes any newly-flagged records added since 2026-05-28 that sort above the 150 cap.

---

LEDGER ACTIONS
- Read canvas F0B0AFSB9LN at run start; Routine 4 carryover items re-affirmed (no Cooper manual resolution detected to drain).
- Appended one Run-log row (status emoji per convention). 0 NEW Tier 3 holds appended (all preserved are carryover).
