# R4 Flagged Consolidation - 2026-05-27 - Audit Log

**Routine:** CRM Guardian - Flagged Consolidation (R4)
**Run started:** 2026-05-27 ~12:00 PM CT (17:15 UTC)
**Pool source:** HubSpot `customer_segment = "Flagged for deletion"` (sorted by `hs_object_id ASC`)
**Cap:** 150 companies/run
**Apollo budget:** N/A (R4 is HubSpot-only, no Apollo)
**Run health:** GREEN

---

## Headline

- **Pool size:** 221 flagged companies (+10 since yesterday's 211).
- **Eligible for processing (in-cap 150, ASC by hs_object_id):** 150 companies (0 fresh-skip in in-cap).
- **HubSpot writes this run:** **1** (1 Mode B contact flag).
- **Mode A reassociations:** 0.
- **Mode B new flags:** 1 (Mary Westerhold / Madison Telco).
- **Un-flag corrections:** 0.
- **Tier 3 holds:** 22 preserved contacts in 19 carryover companies; no NEW R4 T3 items today (all already on ledger from 2026-05-25 / 2026-05-22 / 2026-05-12 runs).
- **Hard stops:** 0 customer-protection. 0 open-deal (in-cap has 0 deal-bearing companies). 0 MaiaEdge own. 0 Enterprise misflag.
- **Cooper bulk-delete actionable count:** **527 contacts** with `flagged_for_deletion = true` (+2 since yesterday's 525: my +1 Mary write, +1 Aaron Santos flagged overnight by another routine).

---

## Pool Composition (221 total, 150 in-cap, 71 off-page)

| Class | Count | Notes |
|---|---|---|
| In-cap zero-contact companies | 76 | Awaiting Cooper's bulk-archive; no contact-level work |
| In-cap contact-bearing companies | 74 | 359 total contacts; 23 not-yet-flagged; 1 needed Mode B flag |
| In-cap deal-bearing companies | 0 | Clean; no open-deal hard stops |
| Off-page (next run) | 71 | hs_object_id 316625421017 → highest; 50 visible + 21 unfetched tail |
| Fresh-skip in off-page slice | 6+ | aristotleweb.com, Ellijay, Allegion, Velocity Network, Pivotal Mobile eDiscovery, Würth Industry NA (all created 2026-05-13 to 2026-05-14) |

### Pool growth (+10 since 2026-05-26 211 baseline)

R1 Fresh Enrichment this morning produced 5 HARD_DELETE writes (per ledger run-log row 9). Plus 5 more from R6 or other paths. Those 10 net-new flagged records sit at the top of the hs_object_id tail and will be in the off-page slice for tomorrow's run.

---

## Invariant Checks (Hard Stops)

### B. Scope
All 150 in-cap records confirmed `customer_segment = "Flagged for deletion"`.

### C. Customer Protection (closed-won deals)
0 in-cap companies have any associated deals (num_associated_deals = 0 across the full 150). No customer-history risk.

### C-bis. Pre-Phase-1 Enterprise Defensive Check
Keyword scan against the four Enterprise sub-segments produced 5 false-positive matches:

| Company | hs_object_id | Why keyword matched | Why NOT Enterprise |
|---|---|---|---|
| C7 Data Centers | 254538313409 | "operations" in brief | Acquired by DataBank 2017 - defunct standalone, correct flag |
| ColoSpace | 254561398507 | "operations" in brief | Acquired by FirstLight - defunct, correct flag |
| OneSource Cloud Corporation | 254561398510 | "operations" in brief | Telecom Expense Management (TEM) - not multi-DC Enterprise |
| Pac-West Telecomm | 254626062055 | "operations" in brief | Chapter 11 2010, acquired by Granite - defunct |
| vXchnge | 263729676986 | "operations" in brief | Wound down 2021 - defunct |

None are genuine Enterprise (no bank/insurer/hospital/retailer/BPO signal). 0 Tier 3 escalations.

### D. Open Deal Hard Stop
In-cap deal-bearing count = 0. No open-deal hard stops triggered.

### E. Fresh-Record Safety
In-cap fresh-skip count = 0. The freshly-flagged records (createdate ≥ 2026-05-13) are all in the off-page tail (next run).

### MaiaEdge Own Record (124293230301)
Confirmed not in flagged pool.

---

## Contact Evaluation (in-cap 74 contact-bearing companies, 359 total contacts)

### Query 1 - Candidates for Mode B flag (flagged_for_deletion != true, parent in pool)

**Returned: 23 contacts.** All evaluated against 6-signal preservation check.

| Status | Count |
|---|---|
| Preserved (fresh-create signal 6) | 2 |
| Preserved (notes_last_updated within 90d, signal 2) | 16 |
| Preserved (notes_last_contacted within 90d, signal 1) | 4 |
| NOT preserved (Mode B candidate) | **1** |

#### NOT-preserved → Mode B flag (1 contact, written)

| Contact ID | Name | Email | Parent Company | Reason |
|---|---|---|---|---|
| 441572856521 | Mary Westerhold | mjschwartz@madisontelco.com | Madison Telephone Co | createdate 2026-02-26 (outside 14d fresh + activity boundary); no notes; lifecyclestage=lead; 0 deals; not opted-out; no POC; 90 days inactive |

**Write executed:** `manage_crm_objects` updateRequest → `flagged_for_deletion = true`. Success (1/1).

**Note:** Email username (`mjschwartz`) does not match contact name (Mary Westerhold) - likely a Madison Telco shared inbox or stale alias. Does not affect Mode B decision.

#### Preserved with NO ICP primary available → Tier 3 carryover (22 contacts on 19 companies)

All 22 were already on the cross-routine ledger from prior runs. No NEW T3 items today.

| Parent Company | hs_object_id | Domain | Preserved Contacts | Activity Signal |
|---|---|---|---|---|
| Hivenet | 297986183874 | hivenet.com | Bastien Vidal | createdate 2026-05-15 (fresh) |
| MP Nexlevel | 254570392308 | mpnexlevel.com | Chris Burton | createdate 2026-05-14 (fresh) |
| HyperLink Infrastructure | 316164220626 | hyperlink-networks.com | Michael Hall | upd 2026-04-21 |
| Symbio | 316528134903 | symbio.global | Jon Cleaver | upd 2026-04-28 |
| IP Transfer | 316538883827 | iptransferllc.net | Joseph Yapsuga | upd 2026-04-16 |
| Manor | 316508757740 | manor.net | Mohammed Nazrul Islam | upd 2026-04-27 |
| Yondr / Overyondr | 316194606814 | overyondr.com | Ryan Sabia | upd 2026-04-21 |
| LS Power | 311410965191 | lspower.com | Jason Scandrol | upd 2026-03-16 |
| FPX AI | 311392963281 | fp8.ai | Colin Sharkey + Niraj Yagnik | upd 2026-04-16 / 2026-03-16 |
| Saturn Cloud | 297918677722 | saturncloud.io | Sebastian Metti | upd 2026-03-16 |
| Edged Data Centers | (TBD) | edged.us | Frank Scandariato | upd 2026-03-16 |
| Essextel | 303896262390 | essextel.com | Steven Garvin | upd 2026-04-23 |
| Everstream | 193867595511 | everstream.net | Vinay Nagpal (flagged_for_deletion=false explicit) | upd 2026-02-26 (exactly at 90d boundary - preserve per invariant F) |
| Hivelocity | (in pool) | hivelocity.net | Jacob Hinton | upd 2026-03-16 |
| Corero | 209237307100 | corero.com | Michael Honeycutt | upd 2026-03-12 |
| Sumauma | 167113651945 | sumaumatelecom.com.br | Paulo Machado + Macatoci Kanashiro | nlc 2026-05-15 |
| FlowSec | 193865438923 | flow-sec.com | Rami Yaron | nlc 2026-03-31 |
| Truepacket | 132996276936 | truepacket.io | Rob Schumann | nlc 2026-05-05 |
| Crown Castle (flagged-parent entry) | (in pool) | crowncastle.com | Craig Daiker (flagged_for_deletion=false explicit, already reassoc to ICP 303890867935 on 2026-05-25) | upd 2026-02-27 |
| ISG | 194005222095 | is-grp.com | Lynn Bruns | nlc 2026-04-24 |

**Conclusion:** All 22 preserved contacts already surfaced to Cooper via the ledger on 2026-05-22 / 2026-05-25. No domain has a HIGH-confidence ICP primary match this run (Mode A search returned 0 new results). Craig Daiker's reassociation to Crown Castle (303890867935) was completed yesterday and remains intact.

### Query 2 - Un-flag corrections (flagged=true with recent activity, parent in pool)

**Returned: 0 contacts.** No preservation reversals within the in-cap 150 pool. (Yesterday's surveillance item for Helios Towers contacts remains out of R4 scope - parents not flagged.)

---

## Mode A Reassociation Search

For each preserved contact's domain, searched HubSpot for HIGH-confidence ICP primary match (exact normalized domain or name). **0 new matches.**

All 22 preserved-contact domains either ARE the flagged company itself (no ICP twin exists), or have no companion ICP record in HubSpot. Cooper-flagged reclass candidates (Everstream, FPL FiberNet, Hut 8, IREN, etc.) remain on the ledger awaiting Cooper's decision to either reclass-the-flagged or surface for D7.

---

## Tier 3 Carryover Summary (no new R4 T3 holds this run)

All standing T3 items from prior runs remain unchanged:

**From 2026-05-25 (15 companies):** Everstream, Sumauma, FPX AI, ISG, Corero, Saturn Cloud, HyperLink Infrastructure, Hivenet, Essextel, Symbio, Truepacket, FlowSec, Yondr, IP Transfer, Manor.

**Mis-flag surveillance from 2026-05-22:** FPL FiberNet (Fiber Op reclass), Everstream (Fiber Op reclass), Shaw (dead-brand archive), Lightower (archive + reassoc), nFrame/Expedient (MSP reclass), NSW/Prysmian (cable mfr - correct exclude, manual contact preservation), Crown Castle parent entry (reclass).

**NC5 fresh-skip mis-flag candidates from 2026-05-22:** Hut 8 (now out of fresh window 2026-05-26+; recheck on next run), IREN (out of fresh window 2026-05-26+; recheck).

**Carryover from 2026-05-12/13 long-tail:** Verizon, Nextlink, AWASR, Bulk Infrastructure, XConnect/Luxconnect, Trans Americas Fiber, TIME dotCom, Helios Towers + subs (4 out-of-scope contact mis-flags from R6 referral), Blackfoot, TecEx, DataCrunch, Southern Cross Cable, GDS, Assured Communications, C Spire MISDOMAIN, Sparklight Carrier MISDOMAIN.

---

## Cross-Routine Surveillance Items (NOT new R4 T3 holds)

Carried from yesterday's run; no change:

* **R6 referral - 4 Helios Towers contacts** carry `flagged_for_deletion=true` while parent Helios Towers West Africa (319134249719, customer_segment=`Other`, tier_5) is NOT in flagged pool. Out of R4 scope. R6 Mode 11 should un-flag.
* **R4 future re-eval - Brad Wiertel** (441489610436, vnet.us) carries `flagged_for_deletion=true` with recent activity; parent Velocity Network (322656973545) is fresh-skip (createdate 2026-05-13) - re-evaluate next run when fresh window expires (2026-05-28+).

---

## Bulk-Delete Pointer (Cooper's Manual Step)

Total contacts currently with `flagged_for_deletion = true` in HubSpot: **527** (+2 since yesterday).

Cooper's manual workflow:
1. HubSpot Contacts → filter `flagged_for_deletion = true` → review (527) and bulk-delete.
2. HubSpot Companies → filter `customer_segment = "Flagged for deletion"` → archive 221 records.

Archiving the 221 companies will sever stale associations from contacts that R3/R4 reassociated to ICP primaries (Craig Daiker → Crown Castle, Ooredoo Qatar Wholesale → primary).

---

## Run Health: GREEN

- 0 errors.
- 0 retries.
- 0 429s.
- 0 invariant blocks (no hard stops triggered).
- 1 successful write (Mode B flag on contact 441572856521).
- 0 net new R4 T3 holds (all preserved contacts already on ledger from prior runs).

---

## Statistics

| Metric | Value |
|---|---|
| Pool size | 221 |
| In-cap (hs_object_id ASC, cap 150) | 150 |
| Off-page (next run) | 71 |
| Fresh-skip in in-cap | 0 |
| Fresh-skip in off-page slice | 6+ |
| Zero-contact in in-cap | 76 |
| Contact-bearing in in-cap | 74 |
| Total contacts evaluated | 359 (23 non-flagged candidates pulled) |
| Preserved (signals 1/2/5/6) | 22 |
| New Mode B flags | 1 |
| Mode A reassociations | 0 |
| Un-flag corrections | 0 |
| New T3 holds | 0 |
| Carryover T3 holds | ~62 (unchanged) |
| Hard stops triggered | 0 |
| Customer-protection / Enterprise-misflag blocks | 0 |
| Errors | 0 |
| HubSpot writes | 1 (succeeded) |
| Apollo credits | 0 (N/A) |
| Cooper bulk-delete count | 527 contacts |
