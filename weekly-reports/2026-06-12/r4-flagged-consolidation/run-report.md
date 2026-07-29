CRM Guardian - Flagged Consolidation - 2026-06-12 - 28 contacts flagged, 6 reassociated, 18 Tier 3 held

Run summary: 150 flagged companies in-cap (queue total 315, sorted hs_object_id ASC; pages 1-150 of yesterday's queue were consolidated 2026-06-11, so today targeted the unprocessed remainder: 104 carried companies + 4 newly flagged low-ID records + 42 fresh-record skips) · 64 contacts evaluated across 54 contact-bearing companies (38 zero-contact companies; 16 companies whose associated contacts are all homed on other primary companies - no action by scope rule) · 28 net-new Mode B flags + 6 Mode A reassociations (Tier 1-2) + 13 idempotent already-flagged confirms + 0 clears · 17 Tier 3 contact holds across 16 companies + 1 company-level open-deal hold · ~92 companies fully resolved this run · 19 companies carried past cap (all fresh-record cohort)

WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then: Filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs the stale associations left by the 6 contact reassociations this run)
> NEW + URGENT: Bits in Flight (326674182894) carries an OPEN deal "H5 Data Centers - Partner Reg" (329189257947, owner Cooper, created 06-09 AFTER the 06-08 flag). Either the flag is wrong or the deal is attached to the wrong company - resolve before this record ages into consolidation on ~06-22.

Tier 3 holds: 17 preserved contacts with no unique HIGH-confidence ICP primary (detail below) + 1 open-deal company hold. 0 closed-won protections, 0 Enterprise C-bis mis-flags in this batch.

Run health: YELLOW
- All 34 writes succeeded (3 flag batches 10/10/8 + 1 reassociation batch 6/6); read-back verified 34/34.
- Tier 3 holds present; open-deal company hold present (Bits in Flight).

Errors: None.

================================================================
INVARIANT-E FRESH-RECORD COHORT (61 companies - no writes, auto-resolves)
================================================================
Every company at queue position 255-315 has createdate >= 2026-05-29 (14-day grace cutoff). 42 fell inside today's 150-company cap and were logged as invariant-E skips; 19 were carried past cap (also all fresh). They re-enter eligibility as they age past 14 days, starting ~2026-06-15. Notable members:

| Company | id | Contacts | Note |
|---|---|---|---|
| Verizon | 325110366958 | 114 | verizonwireless.com import dup of ICP Verizon records (CLAUDE.md known dup-pair). All 114 contacts created 06-01/06-05 (fresh-preserved). Recommend R3 dedup-merge BEFORE R4 ages in - consolidating 114 contacts one-by-one is the wrong tool. |
| g.softbank.co.jp | 325335795443 | 24 | Subdomain dup artifact, already on R0/R3 ledger radar |
| one.verizon.com | 326188916423 | 3 | Subdomain dup artifact |
| Bits in Flight | 326674182894 | 0 | OPEN DEAL - see Cooper action above (invariant D will hard-stop consolidation regardless) |
| SambaNova / STACKIT / LuxProvide / Denvr / NexGen Cloud / Recursal etc. | - | 1-5 each | 06-08 NeoCloud-scan evictions; age in from 06-22 |
| Union Transtel | 327020648154 | 1 | R0 hard-flag 06-12; ages in 06-25 |

================================================================
REASSOCIATIONS (preserved contacts moved to a unique HIGH-confidence ICP primary; Tier 2)
================================================================

| Source flagged company | id | Contact | -> ICP primary | Primary id | Match basis | Segment + owner synced |
|---|---|---|---|---|---|---|
| Hut 8 | 323823198916 | Imad Siraj 485129836247 | Hut 8 | 324208873163 | Exact domain hut8.com | NeoCloud / 161889085 (Tim Lieto) |
| Vocus Wholesale | 319182113497 | James Ward 465763409613 | Vocus | 251600877280 | Exact domain vocus.com.au | Network Operator(Tier 1 / VNO) / 159350430 (Tim Ziemer) |
| ETC Communications - Ellijay Telephone Company | 322405956290 | Jason Smith 492127751896 | ETC Communications | 322836352712 | Exact domain etcnow.com | Fiber Operator / 161889085 |
| altafiber | 322686735045 | Steve Meek 497856034517 | Altafiber | 320874452702 | Normalized-name exact (altafiber; cinbell.com legacy domain vs altafiber.com) | Fiber Operator / 161889085 |
| altafiber | 322686735045 | Richard Huffner 441453191927 | Altafiber | 320874452702 | Normalized-name exact | Fiber Operator / 161889085 |
| MyRepublic Indonesia | 319298011839 | Hendra Gunawan 474847701712 | MyRepublic Indonesia | 319135958773 | Normalized-name exact (myrepublic.net.id vs myrepublic.co.id) | Network Operator(Tier 1 / VNO) / 159350430 |

Note: associations are ADD-only via MCP; contacts remain visible under both records until Cooper archives the flagged source companies. James Ward's reassociation also resolves the standing 2026-05-05 ledger hold (Vocus 251600877280 is now an active Network Operator ICP record - Cooper's reclassification confirmed in HubSpot).

================================================================
MODE B FLAGS (28 net-new flagged_for_deletion=true; Tier 1; all 6-signal-negative, no protection filters fired)
================================================================

| Company | id | Contact(s) flagged |
|---|---|---|
| Exa (exa.com - flow-simulation SW, not EXA Infrastructure) | 320876610270 | Charlie Thomas 465837562606, Philippine Pastier 471114300125 |
| Phoenix Communications | 324508030669 | Robert Koumbis 491982424809, Meagan Langevin 492003240642 |
| Internet Subway | 324542613196 | Adam Bell 492147415788, Ben Otto 492123207362, Thomas Matalavage 491978331869, Daniel Reibsamen 491978331868, Scott Shay 492127751892 |
| CodeDay (R2 evict 06-12) | 193853195001 | Tyler Menezes 296229264104 |
| LANEX (R2 evict 06-12) | 271875845881 | Josh Williams 401310534381 |
| Nashoba Valley Tech HS (R2 evict 06-12) | 286492707559 | Chris Egan 417818964689 |
| BT International Services Korea (R2 evict 06-12) | 318106540786 | Steve Allcock 471651185381 (no email) |
| Congruex | 324271404793 | Herkole Sava 492052425437 |
| MOBILY LLC | 324273199819 | Suhail Ishaq 492052425442 |
| Astound | 324508030666 | Shannon Eagleburger 492041284284 |
| gatco.net | 324524875475 | Javier de Mingo 491957304015 |
| Maquoketa Valley Electric Coop | 324525489884 | Kelly Gibbs 492137592559 |
| BAI Connect | 324534440655 | Terry Koosed 492150859494 |
| Spartan Data Centers | 324535363289 | Si Meng 491957163760 |
| Vistabeam | 324542613223 | Andrew Wicker 492150859488 |
| KNET Co. | 324566401761 | Randy Blunt 492028345051 |
| Home Telecom | 324599570160 | Judy Cronin 492003233527 |
| Bright House Networks | 324615281396 | Jan Edwards 492050676464 |
| Astound Broadband | 324617772770 | Lamar Horton 492003233486 |
| Grande Communications | 324617842385 | Sean Patty 492052216551 |
| 3 Rivers Communications | 324628854464 | Tim Hodges 492040575716 |
| Plumas Sierra REC | 324633547482 | Aaron Whitfield 492127413972 |

Idempotent confirms (already flagged=true, still 6-signal-negative, no write): 13 - Dylan Brown (Symbio), Ann Yanick / Matt Edic / Robyn Helgren (Intelepeer), Jeroen Wisse (Open Systems), Peter Ng (Layer3), Eric Eric (United Cable), Khaled Akram (Telegeeks), Craig Branson (Call48), Marie Holmberg (Teligent), Brian George (Pivotal), James Spina (Melita), David Ackerman (Currency.com).

================================================================
TIER 3 HELD (preserved contacts, NO write - awaiting ICP primary or Cooper decision)
================================================================

| Company | id | Held contact(s) | Reason / recommendation |
|---|---|---|---|
| Bits in Flight | 326674182894 | (0 contacts - company-level hold) | OPEN DEAL "H5 Data Centers - Partner Reg" 329189257947 (Cooper-owned, created 06-09, stage 3807265502). Invariant D. Resolve deal-company attachment or unflag. |
| Dragonfly Internet | 322355279547 | Butch Brock 484486877931, William Baines 484536816318 | Baines contacted 2026-06-10 (2 days ago) - ACTIVE rep conversation on a flagged company. No ICP primary for dragonfly.net. Recommend: unflag + reclassify Fiber Operator (rural AL/FL fiber ISP). |
| Fast Wave | 323666965217 | Anthony Salamoni 489067118326 | Protection filter: lifecycle=opportunity + open-deal assoc + contacted 06-10. Email is anthonys@broadstar.com; Broadstar ICP record 323981908725 (Fiber Operator, 2 deals) exists. Recommend: reassociate Anthony to Broadstar, then archive Fast Wave. Matches 06-09 Daily Brief hygiene flag. |
| Manor | 316508757740 | Mohammed Nazrul Islam 465834282718 | Carry from 06-11. Preserved (notes 04-27); no ICP primary for manor.net. |
| I & S Group | 323231323868 | Lynn Bruns 486369299174 | Contacted 06-04. ISG Technology 264035618536 is domain-mismatch (is-grp.com != isgtech.com) - not unique HIGH. Same disambiguation as 06-11 ISG hold (different record). |
| IP Transfer | 316538883827 | Joseph Yapsuga 465761569489 | Preserved (notes 04-16); no ICP primary. |
| Tract Capital | 321983866611 | Graham Williams 482948942567 | Preserved (notes 05-19); fiber-infra PE investor, no ICP primary. |
| Holston Electric Cooperative | 322388062952 | Sam Trent 484511204032 | Preserved (notes 05-18); no ICP primary. |
| BitStream | 322400659175 | Charles Baldwin 484521260785 | Preserved (notes 05-14); no ICP primary. |
| aristotleweb.com | 322623862501 | L. Elizabeth Bowles 484535495355 | Preserved (notes 05-14); no ICP primary. |
| Ellijay | 322630266612 | Franklin Rigdon 484480023266 | Preserved (notes 05-14). MEDIUM-confidence dup of ETC Communications 322836352712 (Ellijay Telephone consumer domain ellijay.com vs etcnow.com) - merge suggestion, not auto-reassociated per MEDIUM rule. |
| Allegion | 322639574776 | Andrew Erdos 486168348355 | Preserved (notes 05-15); security-products manufacturer (Manufacturing = Watch List, not Enterprise ICP); no primary. |
| Wurth Industry North America | 322795603660 | Jason Tredup 486162222835 | Preserved (notes 05-15). Possible Enterprise (Retail and Distribution) scale-gate candidate ($B+ industrial distributor) - consider R1/R2 re-eval instead of deletion. |
| Commercial Electronics | 322877970151 | Teresa Cunningham 484483303160 | Preserved (notes 05-18); no ICP primary. |
| Eric Hanselman | 323149135546 | Eric Hanselman 486370012871 | Contacted 05-06. Industry analyst (person-as-company record, hanselman.net). Decide: keep as Other/reference or delete after contact preserved elsewhere. |
| SwyftConnect | 323237410551 | Robert Segrave 484517998305 | Preserved (notes 05-18); no ICP primary. |
| Attobahn | 324610914007 | Darryl Grey 491957624545 | Preserved (contacted 05-26, notes 06-04); no ICP primary. |

================================================================
CROSS-ROUTINE LEDGER DRAIN (R4 items resolved at run start)
================================================================
10 of 14 standing 2026-05-05 R4 holds are NO LONGER in the flagged pool (Cooper/routines unflagged + reclassified per recommendation): DataCrunch, Vocus (-> Network Operator ICP, confirmed), EllaLink, Southern Cross, Yondr, Summit Broadband, DayStarr, Sparklight Carrier, Luck Grove, GDS Lebanon. The other 4 (Bluebird Network, HyperLink Infrastructure, Symbio, Airtel Business) were resolved via contact reassociations on 06-08/06-11 - companies remain flagged awaiting archive only. Drain note appended to canvas (no destructive section edits per phantom-append precaution).

================================================================
RUN PARAMETERS
================================================================
- Activity window cutoff (90d, ET): 2026-03-14. Fresh-record cutoff (14d, ET): 2026-05-29.
- ICP primary segments: Data Center Colo Provider / Fiber Operator / Network Operator(Tier 1 / VNO) / MSP/Aggregator / NeoCloud / Enterprise-CustomerSegment.
- Scope rule: only contacts whose PRIMARY company is the flagged record are evaluated (contacts homed on other companies are out of write scope; archive severs their secondary associations naturally).
- Open POC tickets checked (16 open tickets, 12 associated contacts) - zero overlap with evaluated contacts. Company-level deal checks: only Bits in Flight carries a deal in the entire 315-company queue.
- No Apollo calls. All writes confirmationStatus=CONFIRMATION_WAIVED_FOR_SESSION. MaiaEdge own record 124293230301 excluded.
- Queue drain projection: ~46 eligible companies remain pre-cohort-aging (Tier 3 holds + zero-contact stragglers); fresh cohort (61) ages in 06-15 through 06-25. Recommend R3 handles Verizon/softbank/one.verizon dups before then.
