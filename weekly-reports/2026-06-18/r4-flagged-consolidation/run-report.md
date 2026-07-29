# CRM Guardian - Flagged Consolidation - 2026-06-18 - 7 contacts flagged, 69 reassociated, 42 Tier 3 held

Run start: 2026-06-18 ~12:00 PM CT (cron `0 12 * * 1-5`). Timezone for all date math: America/New_York.

Run summary: **150 flagged companies processed** (cap reached) of **233 flagged-with-contacts** in queue (**359 flagged total**) · **477 contacts evaluated** · **351 idempotent-confirmed** already-flagged (skipped, no re-write) · **7 Mode B new flags (Tier 1)** · **69 Mode A reassociations (Tier 1/2)** · **1 flag clear (Tier 1)** · **42 Tier 3 holds** · **76 contact writes, 0 failures** · 0 company-level hard-stop skips (no deals on any of the 150) · 0 bulk-guardrail defers (the 2 >10-contact records, NSW/120 and Shaw/14, were already fully resolved by prior runs).

> **WHAT NEEDS COOPER'S ACTION (surfaced by the digest):**
> 1. Filter HubSpot **Contacts** -> `flagged_for_deletion = true` -> review and **bulk-delete**. (7 newly flagged this run; 351 confirmed-standing from prior runs.)
> 2. Then filter **Companies** -> `customer_segment = "Flagged for deletion"` -> **archive** (severs the stale associations left behind by the 69 contact reassociations done this run).

**Partial run:** company cap = 150/run. 83 flagged-with-contacts companies remain (offset 150+) for the next run, plus 126 flagged companies with 0 contacts (no-op).

## Run health: YELLOW
- Writes all succeeded (76/76); 42 Tier 3 holds present + several dedup/data-quality items surfaced for R3/R5. No errors, no aborts.

## Errors / API failures
None. 0 HubSpot 4xx/5xx, 0 enum 400s, 0 write failures across all 5 processing slices. (One known-enum trap proactively avoided: contacts reassociated to `MSP/Aggregator` primaries got owner-only sync, no `customer_segment` write, per the contact-segment enum gap.)

---

## MODE A - REASSOCIATIONS (applied; contact moved to ICP primary + owner mirrored, segment mirrored where contact enum allows)

69 contacts on flagged duplicate/wholesale-arm/acquired records reassociated to their live ICP primary. These are HIGH-confidence (exact domain OR exact normalized-name) matches only.

| Flagged company (id) | ICP primary (id, segment) | Contacts reassociated |
|---|---|---|
| Sacred Wind Communications (297858169567) | Sacred Wind Communications (326160068331, Fiber) | John Badal (441453196992) |
| Bluebird Network (316163237567) | Bluebird Network (323821758151, Fiber) | Chris Melloway (486362106616) |
| Sunrise GmbH (316598421225) | Sunrise GMBH (316149788367, Fiber) | Matthias Schuler (465836017394) |
| Summit Broadband (317745346241) | Summit Broadband (266240399089, Fiber) | Luis Llop (497838127832), Anthony Raso (464325764800), Sean Magrath (441537060551), Theresa Fletcher (441491355333), Charisse Kissenberth (441478747889) |
| TELESYSTEM (318223234757) | Telesystem (193866158811, MSP/Agg) | Carol Willison (492044473020), Lori Graber (471651180243), Michael Staten (492121957052) |
| Assured Communications (319124813514) | Assured Communications (251587604208, Colo) | Timothy Parker (471675103957), Debbie Brooks (471673523958), Joel Ogren (374739717823) |
| Ooredoo Qatar Wholesale (319154781896) | Ooredoo Qatar AI Cloud (303442039544, NeoCloud) | 6 contacts (474845872874, 474820100814, 474849619647, 474852126449, 474848086768, 474846202585) |
| Vocus Wholesale (319182113497) | Vocus (251600877280, Network Op) | James Ward (465763409613) |
| TIME dotCom (319197750998) | TIME DotCom Berhad (268204721857, Network Op) | 5 contacts (474852255456, 474852255457, 474791668447, 474765851360, 474815909600) |
| MyRepublic Indonesia (319298011839) | MyRepublic Indonesia (319135958773, Network Op) | 3 contacts (474820100812, 487719439082, 474847701712) |
| Alfa Lebanon (319299872495) | Alfa Lebanon (319135943411, Network Op) | Dany Ighnatios (474791595759) |
| PrimeTel (319492475594) | Primetel (316287384263, Fiber) | Kyriaki Ioannidou (471651185354) |
| ALLO Communications (320861822686) | ALLO Communications (264241842927, Fiber) | Nat Evans (273917167313), Scott Clark (273879200472), Bret Oltman (273870064319), Cody Neer (491977146048) |
| Open Systems, Inc (320873011949) | Open Systems (326284199634, MSP/Agg) | Robert Muller (451518855871), Jeroen Wisse (471678757572 - also flag-cleared) |
| Northwest Open Access Network (322364279513) | Noanet (296851879628, Fiber) | 4 contacts (464387124927, 464270904004, 464327513823, 441456811768) |
| Holston Electric Cooperative (322388062952) | Holston Electric Cooperative (322393364204, Fiber) | Sam Trent (484511204032) |
| ETC Communications / Ellijay (322405956290 / 322630266612) | ETC Communications (322836352712, Fiber) | Jason Smith (492127751896), Franklin Rigdon (484480023266) |
| Schurz Communications (322405958358) | Schurz Broadband Group (292748566217, Fiber) | 5 contacts (484521340622, 484588420857, 484517983957, 464297671408, 441504356029) |
| Riot Platforms, Inc. (322537130689) | Riot Platforms (297892337355, NeoCloud) | 5 contacts (485538990831, 485559057092, 485534768831, 485190860527, 440779003629) |
| Velocity Network (322656973545) | Velocity Network (303879483067, MSP/Agg) | Brad Wiertel (441489610436) |
| altafiber (322686735045) | Altafiber (320874452702, Fiber) | Steve Meek (497856034517), Richard Huffner (441453191927), Roger Werth (492000234176) |
| Wave Rural Connect (322843549388) | Wave Rural Connect primary (322813184756, Fiber) | D.J. Bull (484588421819), Hayden Hall (494734156505) |
| Shawnee Communications (322837059312) | Shawnee primary (322613092036, Fiber) | Michael Guffy (484559275722) |
| Giant Communications (324498817751) | Giant primary (324525206259, Fiber) | Mohammad Yacoub (492029733573) |
| Hut 8 (323823198916) | Hut 8 (324208873163, NeoCloud) | 7 contacts (485167749844, 485129836247, 440631018225, 440706366140, 440640108268, 440629326523, 357882472137) |

## MODE B - STANDALONE FLAGS (applied, Tier 1) - contacts flagged_for_deletion = true

7 contacts on genuine non-fit companies with no activity in 90 days, no open deal, no POC, no opt-out, not a duplicate.

| contactId | Name | Company (id) | Why not preserved |
|---|---|---|---|
| 457325245128 | Nate Hubert | Backbone Digital (292440159935) | notes_last_updated 2026-03-17 (pre-90d); lead; no deal/POC/optout; non-fit |
| 425980340966 | Dave Perrill | Backbone Digital (292440159935) | notes_last_updated 2026-03-17 (pre-90d); lead; non-fit |
| 451588831988 | Sebastian Metti | Saturn Cloud (297918677722) | notes 2026-03-16 (pre-90d); lead; MLOps SaaS non-fit |
| 451588830920 | Niraj Yagnik | FPX AI (311392963281) | notes 2026-03-16 (pre-90d); GPU-marketplace non-fit |
| 455480763107 | Jason Scandrol | LS Power (311418164947) | notes 2026-03-16 (pre-90d); power-producer non-fit |
| 480213417720 | Charlie Nelson | Activate (321173470912) | no notes activity; "Mentor" at 501(c)(3) fellowship; non-fit |
| 492050676457 | Marsha Ricciardi | Centerline (324591653605) | no notes activity; network-construction contractor; non-fit |

## CLEARS (applied, Tier 1) - previously flagged contact reactivated

| contactId | Name | Company | Signal |
|---|---|---|---|
| 471678757572 | Jeroen Wisse | Open Systems (reassoc -> 326284199634) | notes_last_contacted + notes_last_updated 2026-06-18 (today); @open-systems.com = primary domain. Flag cleared and reassociated to ICP primary. |

## TIER 3 - HELD FOR REVIEW (no write; left in active pool)

42 unique holds. Two recurring patterns: (A) preserved contact on a genuine non-fit with no ICP primary - awaits Cooper archive; (B) **duplicate-of-ICP companies whose contacts' emails match a live ICP primary domain but the company-to-company match is fuzzy-only (suffix / sibling-domain diff)** - deliberately NOT flagged, routed to R3 merge.

| Company / Contact (id) | Reason |
|---|---|
| Truepacket / Rob Schumann (487432186604) | Preserved (contacted 2026-05-05); no ICP primary [carryover re-affirmed] |
| FlowSec / Rami Yaron (297261432562) | Preserved (2026-03-31); no ICP primary [carryover] |
| CarrierX / Michael Ching (494765969108) | Preserved (2026-06-03); no ICP primary [carryover] |
| ISG (194005222095) + I&S Group (323231323868) / Lynn Bruns (486369299174) | Preserved (2026-06-04); contact @is-grp.com belongs to I&S Group; association to ISG/isginc.com likely spurious -> **R3/R5 dedup** |
| EdgeCloudLink / Guy Marom (485896627901), Yuval Bachar (440783060708) | Preserved; primary ECL (303423288018) is fuzzy-only (ecldc.com vs edgecloudlink.com) -> R3 merge |
| Novita AI / Ding Wang (499028985573), Wayne Wong (499009956581), Ben Li (498971625146) | Preserved (fresh, created 2026-06-08); no ICP primary (GPU non-fit) |
| Saturn Cloud / Hugo Shi (499014648564) | Preserved (fresh, 2026-06-08); no ICP primary |
| Madison Communications (303871311568) / Mary Westerhold (441572856521), Dennis Russell (464336157378), Justin Waldrop (464352977600) | Dup-of-ICP: all @gomadison.com = live Fiber primary (316197317360); held not flagged -> **R3 merge** |
| DayStarr Communications / Collin Rose (441516928719) | Preserved (President, 2026-06-17); primary DayStarr (298011233984) fuzzy-only (daystarrfiber.net vs daystarr.net) -> R3 |
| Essextel / Steven Garvin (441467623152) | Preserved (2026-04-23); no ICP primary [carryover] |
| FPX AI / Dhyay Bhatt (499014385355), Veronika Bhatt (499007497938), Colin Sharkey (451518850806) | Preserved; no ICP primary (GPU non-fit) [carryover] |
| HyperLink / Michael Hall (476652573403) | Preserved (2026-04-21); no ICP primary [carryover] |
| Yondr / Ryan Sabia (464779318976) | Preserved (2026-04-21); primary Yondr Group (251593594608) not exact-name match -> R3 |
| Manor / Mohammed Nazrul Islam (465834282718) | Preserved (2026-04-27); no ICP primary [carryover] |
| Symbio / Jon Cleaver (465830273723) | Preserved (2026-04-28); name-match primary Symbio (320873732840) is segment "Other", not ICP |
| IP Transfer / Joseph Yapsuga (465761569489) | Preserved (2026-04-16); no ICP primary [carryover] |
| Airtel Business / Yashnath Issur (467679488707) | Preserved (2026-04-29); primary Airtel Africa/Nxtra (316210812646) not exact-name match -> R3 |
| Bluebird Network / Benjamin Martens (464387124928) | Unpreserved but @bluebirdnetwork.com = legacy domain of live Fiber primary (323821758151); held not flagged -> R3 merge |
| Tract Capital / Graham Williams (482948942567) | Preserved; canonical Tract (tract.com) is Partner Target, not ICP -> fuzzy only |
| Indiana Cable & Broadband Assoc / Joseph Dant (483252979426) | Preserved; dedup primary (321975558846) is Partner Target, not ICP |
| Lantern Lab / Jonathan Gibbs (480163874517) | Preserved (2026-05-18); UX consultancy non-fit, no ICP primary |
| Dragonfly / Butch Brock (484486877931), William Baines (484536816318) | Preserved (Baines 2026-06-10); residential FWA ISP non-fit, no ICP primary [carryover] |
| BitStream / Charles Baldwin (484521260785) | Preserved; non-fit, no ICP primary [carryover] |
| Allegion / Andrew Erdos (486168348355) | Preserved; security-hardware mfr non-fit [carryover] |
| Riot Platforms / Kyle Lanckriet (486362107578) | Preserved; @coresite.com email contradicts Riot primary -> held for review |
| Aristotle (322623862501) / L. Elizabeth Bowles (484535495355) | Preserved; canonical Aristotle (aristotlebroadband.com) vs flagged aristotleweb.com -> domain mismatch, fuzzy only |
| Würth Industry / Jason Tredup (486162222835) | Preserved (2026-05-15); $22.7B industrial distributor = Watch List not Enterprise ICP; no primary [carryover] |
| Commercial Electronics / Teresa Cunningham (484483303160) | Preserved (2026-05-18); no ICP primary [carryover] |
| Eric Hanselman / Eric Hanselman (486370012871) | Preserved (2026-05-06); personal blog, no ICP primary [carryover] |
| SwyftConnect / Robert Segrave (484517998305) | Preserved (2026-05-18); fuzzy-only primary (Swyft Fiber) -> no HIGH-confidence |
| Fast Wave / Anthony Salamoni (489067118326) | Preserved + protected (lifecyclestage=opportunity, open deal, 2026-06-10); @broadstar.com not the company record - held [carryover broadstar] |
| Attobahn / Darryl Grey (491957624545) | Preserved (contacted 2026-06-18 today); no ICP primary [carryover] |
| Mediacom Communications (324591652598) - 5 contacts | Dup-of-ICP: all @mediacomcc.com = live Fiber primary Mediacom Communications Corp. (175172795115); fuzzy company match (mediacomcable.com vs mediacomcc.com) -> **R3 merge**; held not flagged |
| Harmoni Towers / Sara Brummer (491998255837) | Dup of record 324599576298 (same pitowers.com) but that record is "Other" not ICP -> no valid Mode A target; held -> R3 |

## Cross-routine handoffs surfaced this run (for R3 / R5 / awareness)

- **R3 dedup (Mode A blocked by fuzzy company match, contacts belong to live ICP primary by email domain):** Madison Communications -> 316197317360; Mediacom -> 175172795115; Bluebird (Benjamin Martens) -> 323821758151; EdgeCloudLink -> 303423288018; DayStarr -> 298011233984; Yondr -> 251593594608; Airtel Business -> 316210812646; Harmoni Towers -> 324599576298 (Other). These are reassociation candidates, NOT deletions.
- **R3/R5 cross-association:** Lynn Bruns (486369299174) associated to both ISG (isginc.com) and I&S Group (is-grp.com); her email is-grp.com indicates I&S Group is correct.
- **Awareness (not an action this run):** fresh contacts (created 2026-06-08) are being added to already-flagged non-fit GPU/MLOps records (Novita AI x3, FPX AI x2, Saturn Cloud x1). A sourcing/enrichment process is creating contacts on flagged non-fits - worth confirming the source isn't re-polluting the flagged pool.

## Method note
Processed as 5 disjoint 30-company slices (offset 0/30/60/90/120, sorted hs_object_id ASC for stable pagination). Per-contact 6-signal preservation + 4 protection filters applied; Mode A reassociation gated to HIGH-confidence (exact domain OR exact normalized-name) ICP-segment primaries only; >10-unresolved-contact companies guarded against bulk-flagging. No company-record writes, no `last_enriched_date` bumps (per R4 stamping policy). All writes `confirmationStatus = CONFIRMATION_WAIVED_FOR_SESSION`.
