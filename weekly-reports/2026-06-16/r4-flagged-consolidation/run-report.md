CRM Guardian - Flagged Consolidation - 2026-06-16 - 0 contacts flagged, 0 reassociated, 23 Tier 3 company holds (all carryover, 0 new / 0 drained)

Run summary: 342 flagged companies in queue (up 2 from 340 on 06-15) - 70 fresh-skip (company createdate <14d, invariant E) - 272 eligible - oldest-150 company cap processed (78 with contacts / ~319 contact evaluations + 72 zero-contact) - 122 eligible carried to next run (78 with contacts).
Net HubSpot writes: 0 (0 Mode B flags / 0 Mode A reassociations / 0 flag-clears / 0 company writes). Read-only run. 0 Apollo.
Hard stops: 0 closed-won, 0 open-deal, 0 Enterprise C-bis mis-flags. Every eligible flagged company has num_associated_deals = 0, so invariants C (customer-history) and D (open-deal) are clean across the entire eligible pool this run.

WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs the stale associations from prior-run reassociations)
> Queue is STABLE at 342 flagged companies - no companies have been archived since the 06-15 run. The bulk-delete + archive review is the release valve that lets the oldest-150 cap window advance onto the carried backlog (see Structural note below).

Tier 3 holds: 23 company-level holds in the tables below (19 preserved-contact companies + 4 big-duplicate companies). All are carryovers re-affirmed; 0 new holds, 0 drained. No company-level write needed (all are already customer_segment = "Flagged for deletion").

Run health: YELLOW
- Tier 3 holds present + 3 mis-flag suspects surfaced (Sumauma active today, ALLO Communications, TELESYSTEM). 0 errors, 0 failed writes (0 writes attempted).

Errors: None.

==================================================================
CONTACT DISPOSITION (in-cap oldest-150 companies, ~319 contact evaluations)
==================================================================
- 292 contacts already flagged_for_deletion = true -> idempotent confirm, no write.
- 27 contacts unflagged -> ALL preserved (none eligible for Mode B flag this run). Breakdown:
  - fresh createdate <14d (signal 6): 7  (Ding Wang, Wayne Wong, Ben Li, Hugo Shi, Dhyay Bhatt, Veronika Bhatt, Michael Ching)
  - active notes <90d (signals 1/2): 13 (Paulo Machado 06-16, Macatoci Kanashiro, Lynn Bruns 06-04, John Badal 06-10, Collin Rose 06-11, Guy Marom, Yuval Bachar, Steven Garvin, Colin Sharkey, Rami Yaron, Rob Schumann, Michael Hall, Chris Melloway)
  - 90-day boundary safe-default (invariant F, activity 91-92d): 6 (Jason Scandrol, Sebastian Metti, Nate Hubert, Niraj Yagnik, Dave Perrill, + boundary set)
  - ICP-linked (associated to a non-flagged ICP primary -> reachable, do not flag): Varun Malhi -> AVAIO Digital (Data Center Colo Provider, 251564892901)
- 0 flagged-but-now-active contacts found (reverse check on notes_last_contacted AND notes_last_updated >= 2026-03-18 returned 0) -> 0 flag-clears.

```
MODE A - CONSOLIDATIONS (applied this run): NONE
| Duplicate | Primary | Contacts Reassociated | Contacts Flagged (dup) | Company Flagged | Reason |
|-----------|---------|-----------------------|------------------------|-----------------|--------|
| (none this run - prior-run reassociations on Bluebird Network / HyperLink / Summit Broadband / Schurz / etc. already complete; those contacts sit on their ICP primaries and await company archive) |

MODE B - STANDALONE FLAGS (applied this run): NONE
| Company | Owner | Contacts Flagged | Contacts Preserved | Company Flagged? | Reason |
|---------|-------|------------------|--------------------|------------------|--------|
| (none - the only unflagged-contact candidate, Varun Malhi @ IIM Ahmedabad, is ICP-linked to AVAIO Digital and was preserved, not flagged) |
```

==================================================================
TIER 3 - HELD FOR REVIEW (23 company-level, all carryover re-affirmed)
==================================================================

```
PRESERVED-CONTACT HOLDS (in-cap; company flagged, >=1 active/fresh/ICP-linked contact -> contact NOT flagged, no ICP primary to reassociate to)
| Company | ID | Preserved contact(s) | Signal | Note |
|---------|-----|---------------------|--------|------|
| Truepacket | 132996276936 | Rob Schumann | contacted 05-05 | non-fit, no ICP primary |
| Sumauma | 167113651945 | Paulo Machado (06-16 TODAY), Macatoci Kanashiro (05-29) | active rep convo | MIS-FLAG: Brazilian Network Op/Fiber mislabeled Enterprise-CustomerSegment - recommend unflag/reclassify |
| FlowSec | 193865438923 | Rami Yaron | notes 03-31 | non-fit, no ICP primary |
| I&S Group (ISG) | 194005222095 | Lynn Bruns | contacted 06-04 | non-fit architecture firm, no ICP primary |
| CarrierX | 209233708749 | Michael Ching | created 06-03 (fresh+active) | no ICP primary |
| EdgeCloudLink | 292754052811 | Guy Marom (05-20), Yuval Bachar (03-30) | active <90d, Colo | no exact non-flagged ICP primary |
| Backbone Digital | 292440159935 | Nate Hubert, Dave Perrill | boundary ~91d (Other) | safe-default preserve, no ICP primary |
| Sacred Wind Communications | 297858169567 | John Badal | notes 06-10 (Fiber Op) | active; reassoc/preserve |
| Saturn Cloud | 297918677722 | Hugo Shi (06-08 fresh), Sebastian Metti (boundary) | NeoCloud | possible mis-flag (see NeoCloud cluster) |
| DayStarr Communications | 303871312594 | Collin Rose | notes 06-11 (Fiber Op) | active; reassoc/preserve |
| The Compute Index / fp8 | 311410965191 | Colin Sharkey (04-14), Niraj Yagnik (boundary) | NeoCloud | possible mis-flag (see NeoCloud cluster) |
| FPX AI | 311392963281 | Dhyay Bhatt, Veronika Bhatt | created 06-08 (fresh) | NeoCloud-adjacent fresh leads |
| LS Power | 311418164947 | Jason Scandrol | notes 03-16 (boundary ~92d) | safe-default preserve |
| Essextel | 303896262390 | Steven Garvin | notes 04-23 (Fiber Op) | no ICP primary |
| Bluebird Network | 316163237567 | Benjamin Martens, Chris Melloway | Fiber Operator (reassoc 06-08) | awaiting archive |
| HyperLink Infrastructure, LLC | 316164220626 | Michael Hall | notes 04-21 (Fiber Op) | reassoc 06-08; awaiting archive |
| Novita AI | 300372855493 | Ding Wang, Wayne Wong, Ben Li | created 06-08 (fresh) | NeoCloud leads - possible mis-flag |
| IIM Ahmedabad | 277387036380 | Varun Malhi | assoc to AVAIO Digital (Colo ICP, 251564892901) | preserved via ICP link - do not flag |

BIG-DUPLICATE COMPANY-LEVEL HOLDS (contacts already flagged on prior runs; one-by-one consolidation is the wrong tool -> R3 dedup-merge / Cooper bulk-archive)
| Company | ID | Contacts | Disposition |
|---------|-----|----------|-------------|
| NSW | 266871288514 | 120 | D1-disqualified cable manufacturer (Prysmian); contacts flagged 06-08 -> Cooper bulk-archive |
| FPL FiberNet | 254547320539 | 26 | duplicate -> R3 dedup-merge / archive |
| Shaw | 268241651447 | 14 | acquired by Rogers -> R3 dedup-merge / archive |
| Lightower Fiber Networks | 193854634742 | 13 | -> Zayo -> R3 dedup-merge / archive |

CARRIED BEYOND 150-COMPANY CAP (read-only verified this run; route to R3, NOT R4)
| Company | ID | Unflagged contacts | Why deferred |
|---------|-----|--------------------|--------------|
| Verizon (duplicate) | 325110366958 | ~114 verizonwireless.com consumer-side | contacts created 06-05 -> still in 14-day grace; large dup -> R3 dedup-merge to real Verizon ICP record |
| SoftBank (g.softbank.co.jp duplicate) | (carried) | ~24 | contacts created 06-08 -> still in 14-day grace; -> R3 dedup-merge |
| 78 carried with-contact companies total | - | 266 contacts | beyond oldest-150 cap; predominantly fresh-createdate or reassociated-ICP contacts (no missed flaggable work) |

MIS-FLAG SUSPECTS (NOT flagged; carryover from 06-15; recommend Cooper review)
| Company | ID | Why | Recommendation |
|---------|-----|-----|----------------|
| Sumauma | 167113651945 | active rep conversation (Paulo Machado contacted 06-16); Brazilian telecom mislabeled Enterprise-CustomerSegment | unflag + reclassify Network Op/Fiber |
| ALLO Communications | 320861822686 | legitimate regional Fiber Operator (Nelnet; NE/CO/AZ) sitting in deletion pool; contacts seg=Fiber Operator | unflag + reclassify Fiber Operator |
| TELESYSTEM | 318223234757 | managed IT/UCaaS (Block Communications); plausible MSP/Aggregator ICP | review (unflag/reclassify) |
```

==================================================================
LEDGER DRAIN (prior R4 Tier 3 holds re-evaluated against current pool)
==================================================================
- 0 drained. All prior named holds remain in the flagged pool (verified via current pool membership): Truepacket, FlowSec, ISG, CarrierX, EdgeCloudLink, Essextel, Sumauma, Symbio, Steadfast, Manor, IP Transfer, NSW, FPL FiberNet, Shaw, Lightower, Verizon-dup, Fast Wave, Dragonfly all still flagged.
- Bits in Flight (326674182894): now FRESH-SKIP (created 06-09, <14d) - prior open-deal hold not re-evaluated this run; ages into consolidation ~06-23.
- Fast Wave (323666965217) + Dragonfly Internet (322355279547): still flagged, in carried-beyond-cap set - standing holds re-affirmed (not drained; my 06-16 first-pass "drained" read was a key-type bug, corrected here).
- Conclusion: Cooper has not run the bulk-archive since 06-15, so nothing drained. This is expected.

==================================================================
STRUCTURAL NOTE FOR COOPER (re-affirmed; scale concern)
==================================================================
Flagged pool is 342. With the 150-company cap (oldest by hs_object_id) + 70 fresh-skip, the cap window now covers only 78 of the 156 eligible with-contact companies. The other 78 with-contact companies (incl. the big Verizon 114 / SoftBank / FPL 26 duplicates) sit beyond the window and only advance once the oldest flagged companies are archived. The window advances ONLY when Cooper bulk-archives the flagged pool. Two-part release valve:
  (1) Cooper: run the Contacts (flagged_for_deletion=true) bulk-delete + Companies (Flagged for deletion) archive review.
  (2) R3 dedup-merge the large duplicate clusters (Verizon, SoftBank, FPL FiberNet, NSW, Shaw, Lightower) - these are duplicate/defunct cleanups, not per-contact R4 work.
Until then, R4 will keep re-confirming the same oldest-150 idempotently (0 net writes, as today and 06-15).
