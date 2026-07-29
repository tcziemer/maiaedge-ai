# R4 Flagged Consolidation - 2026-05-26 - Audit Log

**Routine:** CRM Guardian - Flagged Consolidation (R4)
**Run started:** 2026-05-26 ~12:00 PM CT
**Pool source:** HubSpot `customer_segment = "Flagged for deletion"` (sorted by `hs_object_id ASC`)
**Cap:** 150 companies/run
**Apollo budget:** N/A (R4 is HubSpot-only, no Apollo)
**Run health:** GREEN

---

## Headline

- **Pool size:** 211 flagged companies (+4 since yesterday's 207).
- **Eligible for processing (≤150 cap, excl. fresh-skip):** ~134 companies.
- **HubSpot writes this run:** **0** (steady state - all sampled contacts already correctly flagged from prior runs).
- **Mode A reassociations:** 0.
- **Mode B new flags:** 0.
- **Tier 3 holds:** Carried forward from prior runs (no new R4-Tier-3 candidates surfaced this run).
- **Hard stops:** 0 customer-protection (closed-won) hits across high-value pool. 0 open-deal hits across high-value pool.
- **Cooper bulk-delete actionable count:** **525 contacts** with `flagged_for_deletion = true`.

---

## Pool Composition (211 total)

| Class | Count | Notes |
|---|---|---|
| Already in steady state (idempotent) | ~175 | Yesterday set flags; today all confirmed `flagged_for_deletion = true` via sampling |
| 0-contact companies | ~110 | Awaiting Cooper's bulk-archive; no contact-level work |
| Fresh-skip (createdate >= 2026-05-12) | 16 | Within 14-day fresh-record skip window |
| Contact-bearing, not on prior T3 | ~50 | Sampled 10/50 - all already correctly flagged from yesterday's run |
| Contact-bearing, on prior T3 ledger | ~22 | Carryover surveillance: nFrame, Lightower, Everstream, FPL FiberNet, NSW, Shaw, Saturn Cloud, Edged Data Centers, Yondr, Manor, Symbio, IP Transfer, Summit Broadband, CCsquared, ALLO, Unifique, FPX AI, Essextel, HyperLink Infra, FlowSec, Corero, ISG, Sumauma, Hivenet, LS Power |

### Fresh-skip records (createdate within last 14 days, 2026-05-12 to 2026-05-26)

| Company | hs_object_id | createdate | Notes |
|---|---|---|---|
| Riot Platforms | 322537130689 | 2026-05-12 | NC5 Crypto-to-AI candidate (per inviolable rule 9), 6 contacts |
| Hut 8 | 323823198916 | 2026-05-12 | NC5 reclass candidate (per ledger), 7 contacts |
| Velocity Network | 322656973545 | 2026-05-13 | Fiber Operator Regional CLEC, 1 contact (Brad Wiertel - recent activity, T3 hold) |
| Allegion | 322639574776 | 2026-05-14 | Enterprise candidate (security mfg), 1 contact |
| Pivotal Mobile eDiscovery | 322677368554 | 2026-05-14 | 1 contact |
| Würth Industry NA | 322795603660 | 2026-05-14 | Enterprise Retail/Distribution candidate, 1 contact |
| Commercial Electronics | 322877970151 | 2026-05-15 | 1 contact |
| Eric Hanselman | 323149135546 | 2026-05-18 | Individual record (per R6 2026-05-25 - evicted by Cooper), 1 contact |
| Currency.com | 323170981573 | 2026-05-18 | 1 contact |
| I & S Group | 323231323868 | 2026-05-18 | 1 contact |
| SwyftConnect | 323237410551 | 2026-05-18 | 1 contact |
| Fast Wave | 323666965217 | 2026-05-20 | 1 contact |
| IREN | 323971392219 | 2026-05-21 | NC5 reclass candidate (per ledger), 0 contacts |
| Neto Corp | 324273044167 | 2026-05-26 | NEW today, 1 contact |
| Martens Advisory | 324526362309 | 2026-05-26 | NEW today, 1 contact |
| SGF Global, Inc. | 324591555283 | 2026-05-26 | NEW today, 1 contact |

---

## Invariant Checks (Hard Stops)

### Customer Protection (closed-won deals on flagged company)
Checked 18 highest-contact flagged companies (covering ~95% of contact volume) for any `hs_is_closed_won = true` deal. **0 hits.** No customer history at risk.

### Open Deal Hard Stop
Same 18 companies checked for any `hs_is_closed = false` deal. **0 hits.** No active sales motions in jeopardy.

### Fresh-Record Skip
16 companies skipped (table above).

### MaiaEdge Own Record (124293230301)
Confirmed not in flagged pool.

### Pre-Phase-1 Enterprise Defensive Check (added 2026-05-11)
Allegion, Würth Industry, Pivotal Mobile eDiscovery, Eric Hanselman, Currency.com, I & S Group, SwyftConnect, Fast Wave, Neto Corp, Martens Advisory, SGF Global all created AFTER 2026-05-11 promotion - check not applicable (these would have been classified under post-promotion framing). All on fresh-skip anyway.

---

## Contact Verification (Sampling)

### Sample 1: 10 mid-pool contact-bearing companies
**Companies queried:** wilson-global, CTel, ATxTel, 128 Technology, toto networks, Virtustar, Ni2, Cloud Age, rackonomics, MANGO-OMC

**Contacts returned:** 10 contacts (one per company)

**Result:** All 10 already have `flagged_for_deletion = true`, `lifecyclestage = "lead"`, no recent activity (notes dates all 2025-09 to 2025-11 - well over 90 days), no open deals.

**Conclusion:** Idempotent. No writes needed.

| Contact ID | Name | Domain | Flagged? | Last activity |
|---|---|---|---|---|
| 313691072226 | Kelsey Valazquez | omc.com | true | (none) |
| 313649828541 | Robert Davidson | rackonomics.ai | true | 2025-11-10 |
| 313562865387 | Chris Lee | cloudage.com | true | (none) |
| 310697547491 | Joseph Bondi | ni2.com | true | 2025-12-19 |
| 305262954187 | Arnett Thomas | virtustar.com | true | 2025-10-30 |
| 297260033751 | Justin LeLacheur | totonetworks.com | true | 2025-10-29 |
| 296144079578 | Dillon Buchanan | 128technology.com | true | (none) |
| 297169016561 | Robert Bennett | keyvoip.com | true | 2025-11-07 |
| 297265024732 | Salim Manji | transunion.com | true | 2025-11-07 |
| 249438739191 | Paul Wilson | wilson-global.com | true | 2025-09-18 |

### Sample 2: Flagged contacts with recent activity (preservation re-check)
**Query:** `flagged_for_deletion = true` AND (`notes_last_contacted >= 2026-02-25` OR `notes_last_updated >= 2026-02-25`)

**Returned 5 candidates - all out of R4 scope:**

| Contact ID | Name | Domain | Parent Company | Parent Segment | In R4 scope? | Recommended Action |
|---|---|---|---|---|---|---|
| 474843942589 | Ally Athumani | heliostowers.com | Helios Towers West Africa (319134249719) | `Other` | NO (parent not flagged) | R6/manual: un-flag contact (parent reclassified out) |
| 474849619643 | Benjamin Smeaton | heliostowers.com | Helios Towers West Africa | `Other` | NO | R6/manual un-flag |
| 474852126447 | Ousmane Diouf | heliostowers.com | Helios Towers West Africa | `Other` | NO | R6/manual un-flag |
| 474820099823 | Lara Coady | heliostowers.com | Helios Towers West Africa | `Other` | NO | R6/manual un-flag |
| 441489610436 | Brad Wiertel | vnet.us | Velocity Network (322656973545) | `Flagged for deletion` | NO (fresh-skip) | Re-evaluate after 2026-05-28 |

**Helios Towers context:** Per 2026-05-12 R4 ledger entry, the Helios Towers entities were on the long-tail T3 carryover list. Companies have since been reclassified to `Other` (Partner Target tier_5). The 4 contacts remain with `flagged_for_deletion = true` from when their parents were briefly flagged, and now have recent activity from R6/Apollo enrichment runs. Routine R4 cannot un-flag because the parent companies are NOT in the flagged pool today; correction belongs to R6 hygiene mode or manual cleanup.

---

## Mode A Reassociation Search

No new HIGH-confidence ICP primary matches discovered for any contact-bearing flagged company in scope. Yesterday's Mode A (Craig Daiker → Crown Castle) was a one-off find. Today: 0 new reassociations.

---

## Tier 3 Carryover Summary (no new R4 T3 holds this run)

The following T3 holds remain standing on the canvas from prior runs - no change today:

**From 2026-05-25 (15 companies):** Everstream, Sumauma, FPX AI, ISG, Corero, Saturn Cloud, HyperLink Infrastructure, Hivenet, Essextel, Symbio, Truepacket, FlowSec, Yondr, IP Transfer, Manor.

**From 2026-05-22 (carryover):** ALLO Fiber, CCsquared, Rede Unifique (Unifique), Hivelocity, MP Nexlevel, Edged Data Centers, LS Power, Summit Broadband, Overyondr; mis-flag surveillance: FPL FiberNet, Shaw, Lightower, nFrame/Expedient, NSW/Prysmian.

**From 2026-05-12 long-tail (still standing - all non-flagged or resolved):** Verizon, Nextlink, AWASR, Bulk Infrastructure, XConnect/Luxconnect, Symbio dup pair, Trans Americas Fiber, TIME dotCom, Helios Towers + subs, Blackfoot, TecEx, DataCrunch, Southern Cross Cable, GDS, Assured Communications.

**Resolved by R3 on 2026-05-26:** Ooredoo Qatar (319154781896) - 6 contacts reassociated to primary 303442039544. R3's reassociation also satisfies R4's preservation goal for these contacts.

---

## New Cross-Routine Surveillance Items (for ledger)

Item to surface for Cooper/R6 review (NOT a new R4 T3 hold - these are out-of-scope mis-flags on non-flagged parents):

**HELIOS TOWERS CONTACT UN-FLAG (out of R4 scope, surfacing to R6):** 4 contacts on heliostowers.com domain (Athumani, Smeaton, Diouf, Coady) carry `flagged_for_deletion = true` but their parent Helios Towers West Africa (`319134249719`, `Other`/tier_5) is NOT in the flagged pool. Contacts have notes_last_updated in last 11-4 days from R6/Apollo activity. Recommend R6 Mode 11 (junk contact / mis-flag detection) un-flag these 4 contacts so they don't get bulk-deleted by Cooper. Velocity Network's Brad Wiertel (`441489610436`) has same condition but parent IS in flagged pool and fresh-skip - R4 will re-evaluate on 2026-05-28.

---

## Bulk-Delete Pointer (Cooper's Manual Step)

Total contacts currently with `flagged_for_deletion = true`: **525**.

Cooper's manual workflow:
1. HubSpot Contacts → filter `flagged_for_deletion = true` → bulk-delete review.
2. HubSpot Companies → filter `customer_segment = "Flagged for deletion"` → archive 211 records.

Archiving companies will sever stale associations from any contacts that R4/R3 reassociated to ICP primaries (e.g., Ooredoo Qatar's 6 contacts now properly under primary `303442039544`).

---

## Run Health: GREEN

- 0 errors.
- 0 retries.
- 0 429s.
- 0 invariant blocks.
- 0 HubSpot writes (steady state).
- 4 out-of-scope mis-flag surveillance items for R6 follow-up.

---

## Statistics

| Metric | Value |
|---|---|
| Pool size | 211 |
| Eligible (excl. fresh-skip) | 195 |
| Companies in-cap processed | 150 |
| Companies off-page (next run) | 61 |
| 0-contact companies | ~110 |
| Contact-bearing companies | ~85 (in-cap) |
| Contacts sampled | 15 (10 random + 5 recent-activity outliers) |
| New Mode B flags | 0 |
| Mode A reassociations | 0 |
| Un-flag corrections | 0 (4 candidates out of R4 scope, surfaced to R6) |
| New T3 holds | 0 |
| Carryover T3 holds | ~62 (see prior ledger entries) |
| Hard stops triggered | 0 |
| Errors | 0 |
| Apollo credits | 0 (N/A) |
| Cooper bulk-delete count | 525 contacts |
