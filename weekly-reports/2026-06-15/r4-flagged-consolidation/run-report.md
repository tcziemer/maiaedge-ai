CRM Guardian - Flagged Consolidation - 2026-06-15 - 0 contacts flagged, 0 reassociated, 38 Tier 3 held (32 contacts + 5 bulk-dup companies + 1 open-deal company)

Run summary: 340 flagged companies in queue (up from 315 on 06-12 - weekend R0/R1/R2 evictions accrued, no Cooper archive yet) - 217 have contacts, 123 are zero-contact (resolved, awaiting archive). Of the 217 with contacts: 150 eligible (createdate < 2026-06-01) - exactly the 150-company cap, all evaluated, no eligible carryover - and 67 fresh (createdate >= 2026-06-01, invariant-E skip, age in 06-15 through 06-26). Of the 150 eligible: 5 bulk-dup/defunct companies held company-level (218 contacts NOT churned one-by-one - R3 territory) + 145 processed. 168 primary-homed contacts evaluated across the 145; ~101 secondary-association contacts on these companies are homed on other primaries and were scope-excluded (no action).

Net writes this run: 0. (Mode B flags: 0 - all stale contacts were already flagged in prior runs. Reassociations: 0 new - the 6 from 06-12 persist as ADD-only associations awaiting source-company archive. Clears: 0 - no flagged contact regained activity. Idempotent already-flagged confirms: 123.) A near-zero-write run is the correct steady state: the eligible pool is the same aged pool drained 06-11/06-12, every genuine non-fit contact on it is already flagged, and the weekend's new evictions are all still inside the 14-day fresh-record grace window.

WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete. (123 R4-confirmed flagged contacts in this run's eligible pool alone; the full flagged_for_deletion=true pool is larger across all prior runs.)
> Then: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (340 companies; archival severs the stale ADD-only associations left by the 6 reassociations carried from 06-12).
> URGENT MIS-FLAG (NEW this run): ALLO Communications (320861822686, allofiber.com) is a legitimate regional Fiber Operator (Nebraska / Colorado / Arizona; Nelnet subsidiary) sitting in the deletion pool. All 3 of its contacts carry customer_segment = "Fiber Operator". Recommend: remove the Flagged-for-deletion segment and reclassify Fiber Operator before any bulk archive. R4 did NOT flag its contacts.
> STANDING (carry from 06-12): Bits in Flight (326674182894) open deal "H5 Data Centers - Partner Reg" (329189257947) - resolve deal-company attachment or unflag. Fast Wave (323666965217) / Anthony Salamoni open deal + opportunity - reassociate Anthony to Broadstar ICP (323981908725) then archive Fast Wave (invariant D held it again this run).

Run health: YELLOW
- 0 writes attempted, 0 failed (clean read-only pass; nothing required a write).
- Tier 3 holds present (38) including 2 mis-flag investigations (ALLO Communications, TELESYSTEM).
- 0 closed-won customer-protection stops, 0 Enterprise C-bis mis-flags in this batch. 0 eligible companies carry an open deal (only standing Bits in Flight, which is zero-contact + fresh).

Errors: None.

================================================================
RUN PARAMETERS
================================================================
- Today (ET): 2026-06-15. Activity window cutoff (90d, ET): 2026-03-17. Fresh-record cutoff (14d, ET): 2026-06-01.
- Scope rule: only contacts whose PRIMARY company (associatedcompanyid) is a flagged record are evaluated. 168 primary-homed in scope; ~101 secondary-association contacts excluded.
- ICP primary segments: Data Center Colo Provider / Fiber Operator / Network Operator(Tier 1 / VNO) / MSP/Aggregator / NeoCloud / Enterprise-CustomerSegment.
- Company cap 150/run hit exactly (150 eligible = cap); no eligible company deferred past cap. 5 bulk-dup companies within the 150 held company-level rather than churned.
- 6-signal preservation evaluated per contact (notes_last_contacted 90d / notes_last_updated 90d / open deal / open POC ticket / lifecyclestage in customer-opportunity-subscriber / createdate 14d). Protection filters: hs_email_optout (none observed), opportunity/customer lifecycle, open deal, open POC. hs_email_optout absent on all 168 (no CAN-SPAM holds).
- POC overlap: no flag candidates this run, so no POC cross-check required (consistent with 06-12 zero overlap).
- No Apollo, no web. Read-only run - no manage_crm_objects calls issued. MaiaEdge own record 124293230301 excluded by scope.

================================================================
QUEUE COMPOSITION (340 flagged companies)
================================================================
```
123  zero-contact companies ............ resolved, awaiting Cooper archive (no R4 action)
217  companies with contacts
      67  fresh (createdate >= 2026-06-01) . invariant-E skip; age in 06-15 -> 06-26
     150  eligible (createdate < 2026-06-01) . ALL evaluated this run (= cap)
            5  bulk-dup/defunct ........... Tier 3 company-level hold (R3 territory)
          145  processed ................. 168 primary-homed contacts evaluated
```

Fresh-cohort notables (invariant-E skip, age in over the next ~11 days): Verizon 325110366958 (114 contacts, verizonwireless.com import dup of ICP Verizon - R3 dedup-merge BEFORE it ages in 06-15+, one-by-one is the wrong tool), g.softbank.co.jp 325335795443 (24, subdomain dup), Hotwire Communications 326166406893/326182458088 (dup pair), IFX Networks 326188915438, Telecentro 326207775473, Thrive 326350145248 (11), SambaNova/STACKIT/Recursal/NexGen/Denvr (06-08 NeoCloud-scan evictions), Nextlink Internet 327020509900, Union Transtel 327020648154.

================================================================
NET-NEW WRITES (Tier 1 / Tier 2)
================================================================
NONE. Mode B flags: 0. Reassociations: 0. Clears: 0.

Decision detail on the 5 contacts a naive 6-signal pass would have flagged (all correctly NOT flagged):

| Contact | id | Company | Reason NOT flagged |
|---|---|---|---|
| Michael Staten (CFO) | 492121957052 | TELESYSTEM 318223234757 | Company is a mis-flag suspect (telesystem.us = TeleSystem managed IT/UCaaS, Block Communications - plausible MSP/Aggregator ICP) with a recently-touched sibling contact (Carol Willison nlu 06-12). Held company-level Tier 3; do not flag contacts on a likely-mis-flagged ICP company. |
| Cody Neer (Dir Mktg/Sales) | 491977146048 | ALLO Communications 320861822686 | Company is an unambiguous Fiber Operator ICP wrongly in the deletion pool. Held; recommend unflag + reclassify. |
| Jason Scandrol | 455480763107 | LS Power 311418164947 | notes_last_updated 2026-03-16 = 1 day outside the 90d window AND part of a uniform 03-16 bulk-maintenance touch across 3 unrelated records. Invariant F (activity at the 90d boundary -> preserve, safe default). Held. |
| Sebastian Metti (Founder) | 451588831988 | Saturn Cloud 297918677722 | Same 03-16 boundary/maintenance touch. Invariant F preserve. Held. |
| Niraj Yagnik (Co-founder/CTO) | 451588830920 | fp8.ai (primary in flagged set) | Same 03-16 boundary/maintenance touch. Invariant F preserve. Held. |

================================================================
IDEMPOTENT CONFIRMS (123 contacts already flagged_for_deletion=true, still 6-signal-negative, no write)
================================================================
Across 74 companies. These remain correctly queued for Cooper's bulk-delete. Largest concentrations:
```
Lanck Telecom (316196415210) ........ 7    | Novus International (316285596350) .. 4
US Internet (254570392307) .......... 6    | Intelepeer (318223398591) .......... 3
Internet Subway (324542613196) ...... 5    | (single-contact companies) ......... 47
```
Multi-contact remainder (2 each): Phoenix Communications, CarrierX, Troy Cablevision, Trainy, 5c.ai, OneSource Cloud, Directlink Technologies, Corero, BHC. Plus 47 single-contact flagged companies (Internet-Subway/Phoenix evictions from 06-12, the 11-2025 Enterprise-CustomerSegment import cohort, and 06-08 NeoCloud-scan evictions). 21 of the 123 sit on companies whose contact email-domain differs from the company domain (e.g. waystar.com, hivelocity.net, solvoglobal.com, exabeauty.com) - all confirmed in-scope by the associatedcompanyid filter, flags stand.

================================================================
REASSOCIATIONS CARRIED FROM 06-12 (ADD-only; awaiting source-company archive - NO re-write)
================================================================
These 6 contacts were reassociated to their ICP primary on 06-12. MCP associations are ADD-only, so each still shows under its flagged source company until Cooper archives it. No action this run.

| Contact | id | Flagged source | -> ICP primary (06-12) |
|---|---|---|---|
| Steve Meek | 497856034517 | altafiber 322686735045 | Altafiber 320874452702 (Fiber Operator) |
| Richard Huffner | 441453191927 | altafiber 322686735045 | Altafiber 320874452702 |
| Jason Smith | 492127751896 | ETC Communications 322405956290 | ETC Communications 322836352712 (Fiber Operator) |
| Hendra Gunawan | 474847701712 | MyRepublic Indonesia 319298011839 | MyRepublic Indonesia 319135958773 (Network Op) |
| James Ward | 465763409613 | Vocus Wholesale 319182113497 | Vocus 251600877280 (Network Op) |
| Imad Siraj | 485129836247 | Hut 8 323823198916 | Hut 8 324208873163 (NeoCloud) |

================================================================
GRACE-PERIOD PRESERVES (contact createdate within 14d - re-evaluate as they age)
================================================================
8 contacts on eligible companies whose CONTACT records are fresh (created 06-03 to 06-08): Ding Wang / Wayne Wong / Ben Li (Novita AI 300372855493), Hugo Shi (Saturn Cloud 297918677722), Dhyay Bhatt / Veronika Bhatt (FPX AI 311392963281), Steve Meek (altafiber - also reassoc), Luis Llop (Summit Broadband 317745346241), Michael Ching (CarrierX 209233708749, also activity 06-03). No action; natural re-evaluation post-14d.

================================================================
TIER 3 HELD - BULK-DUP / DEFUNCT COMPANIES (company-level hold; one-by-one consolidation is the wrong tool -> R3)
================================================================
| Company | id | Contacts | Owner | Disposition |
|---|---|---|---|---|
| NSW (Prysmian) | 266871288514 | 120 | Tim Z | prysmian.com = Prysmian subsea cable MANUFACTURER (NSW = Norddeutsche Seekabelwerke). Cable vendor -> D1-evicted per subsea policy, no ICP primary. Recommend Cooper bulk-archive; do NOT churn 120 contacts. |
| nFrame (Expedient) | 193853915836 | 45 | Tim Lieto | expedient.com = Expedient (real colo / managed cloud). Likely dup of an ICP Colo record. Recommend R3 dedup-merge check before archive. |
| FPL FiberNet | 254547320539 | 26 | Ken | fplfibernet.com legacy (FPL/NextEra fiber arm). Recommend R3 dedup / bulk handling. |
| Shaw | 268241651447 | 14 | Tim Z | shaw.ca - Shaw Communications acquired by Rogers (2023), legacy brand. Recommend R3 merge into Rogers ICP or bulk-archive. |
| Lightower Fiber Networks | 193854634742 | 13 | Ken | lightower.com defunct (absorbed into Crown Castle Fiber / Zayo). Recommend R3 merge into Zayo ICP or bulk-archive. |

================================================================
TIER 3 HELD - PRESERVED CONTACTS (no write; awaiting ICP primary or Cooper decision)
================================================================
32 contacts. NEW mis-flag investigations at top; remainder are carryovers re-confirmed against today's pool.

| Company | id | Held contact(s) | Signal | Reason / recommendation |
|---|---|---|---|---|
| ALLO Communications | 320861822686 | Cody Neer 491977146048, Nat Evans 273917167313, Scott Clark 273879200472 | Nat/Scott nlu 05-08 | NEW. Legit regional Fiber Operator (allofiber.com) wrongly flagged; all 3 contacts segment=Fiber Operator. Recommend unflag + reclassify Fiber Operator. |
| TELESYSTEM | 318223234757 | Carol Willison 492044473020 (+ Michael Staten 492121957052) | Carol nlu 06-12 | NEW. telesystem.us = TeleSystem managed IT/UCaaS (Block Communications). Recently-touched contact; plausible MSP/Aggregator ICP. Recommend review for unflag/reclassify. |
| Sumauma | 167113651945 | Macatoci Kanashiro 261906818770, Paulo Machado 261906818771 | contacted 05-29, nlu 06-12 | Active rep conversation on a flagged Brazilian telecom. Contact seg mislabeled Enterprise-CustomerSegment; entity is Network Op/Fiber. Recommend review (unflag/reclassify), not delete. |
| Dragonfly Internet | 322355279547 | Butch Brock 484486877931, William Baines 484536816318 | Baines contacted 06-10 | Carry 06-12. Active conversation; no ICP primary for dragonfly.net. Recommend unflag + reclassify Fiber Operator (rural AL/FL fiber). |
| Fast Wave | 323666965217 | Anthony Salamoni 489067118326 | opportunity + open deal + contacted 06-10 | Carry 06-12. Invariant D (open deal) + opportunity protection. Recommend reassociate Anthony to Broadstar ICP 323981908725, then archive Fast Wave. |
| I & S Group | 323231323868 | Lynn Bruns 486369299174 | contacted 06-04 | Carry. is-grp.com != isgtech.com (ISG Technology 264035618536) - not unique HIGH. Merge suggestion only. |
| Attobahn, Inc. | 324610914007 | Darryl Grey 491957624545 | contacted 05-26, nlu 06-04 | Carry. No ICP primary. |
| Würth Industry North America | 322795603660 | Jason Tredup 486162222835 | nlu 05-15 | Carry. Possible Enterprise (Retail and Distribution) scale-gate candidate - consider R1/R2 re-eval, not deletion. |
| Allegion | 322639574776 | Andrew Erdos 486168348355 | nlu 05-15 | Carry. Security-products manufacturer (Manufacturing = Watch List, not Enterprise ICP). No primary. |
| Truepacket | 132996276936 | Rob Schumann 487432186604 | contacted 05-05 | Carry. Tactical-edge/DoD architect contact preserved; no ICP primary. |
| FlowSec | 193865438923 | Rami Yaron 297261432562 | contacted 03-31 | Carry. flow-sec.com security consultant; no ICP primary. |
| Eric Hanselman | 323149135546 | Eric Hanselman 486370012871 | contacted 05-06 | Carry. Industry analyst (person-as-company, hanselman.net). Keep as reference or delete after contact preserved elsewhere. |
| Holston Electric Cooperative | 322388062952 | Sam Trent 484511204032 | nlu 05-18 | Carry. No ICP primary. |
| BitStream | 322400659175 | Charles Baldwin 484521260785 | nlu 05-14 | Carry. No ICP primary. |
| aristotleweb.com | 322623862501 | L. Elizabeth Bowles 484535495355 | nlu 05-14 | Carry. No ICP primary. |
| SwyftConnect | 323237410551 | Robert Segrave 484517998305 | nlu 05-18 | Carry. No ICP primary. |
| Ellijay | 322630266612 | Franklin Rigdon 484480023266 | nlu 05-14 | Carry. MEDIUM-confidence dup of ETC Communications 322836352712 (ellijay.com vs etcnow.com) - merge suggestion, not auto-reassociated. |
| Commercial Electronics | 322877970151 | Teresa Cunningham 484483303160 | nlu 05-18 | Carry. No ICP primary. |
| Tract Capital | 321983866611 | Graham Williams 482948942567 | nlu 05-19 | Carry. Fiber-infra PE investor; no ICP primary. |
| IP Transfer | 316538883827 | Joseph Yapsuga 465761569489 | nlu 04-16 | Carry. No ICP primary. |
| Manor | 316508757740 | Mohammed Nazrul Islam 465834282718 | nlu 04-27 | Carry. No ICP primary for manor.net. |
| The Compute Index / fp8.ai | 311410965191 | Colin Sharkey 451518850806, Niraj Yagnik 451588830920 | Colin contacted 04-14; Niraj 03-16 boundary | Carry. fp8.ai NeoCloud contacts; no ICP primary. |
| LS Power | 311418164947 | Jason Scandrol 455480763107 | nlu 03-16 boundary | Boundary-preserve (invariant F). Energy/power DC-development; no ICP primary. |
| Saturn Cloud | 297918677722 | Sebastian Metti 451588831988 | nlu 03-16 boundary | Boundary-preserve. saturncloud.io ML-platform (non-carrier); no ICP primary. |
| Backbone Digital | 292440159935 | Dave Perrill 425980340966 | nlu 03-17 | Carry. Other segment; no ICP primary. |
| CarrierX | 209233708749 | Michael Ching 494765969108 | contacted 06-03 (also grace) | Carry. Active/fresh contact; no ICP primary. |

================================================================
CROSS-ROUTINE LEDGER DRAIN (R4 items re-evaluated at run start)
================================================================
All standing R4 holds from 06-12 re-checked against today's flagged pool: every held company remains customer_segment="Flagged for deletion" (queue grew 315 -> 340; Cooper has not run a bulk-archive since 06-12), so none could be drained as Cooper-resolved. All carried forward (see Tier 3 tables above). The 6 reassociated source companies (altafiber, ETC, MyRepublic, Vocus, Hut 8) likewise remain flagged awaiting archive only. New items added to ledger this run with [2026-06-15] prefix: ALLO Communications mis-flag, TELESYSTEM mis-flag, Sumauma active-conversation mis-flag.
