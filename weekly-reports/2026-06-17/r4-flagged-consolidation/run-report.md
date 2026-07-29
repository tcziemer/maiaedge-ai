CRM Guardian - Flagged Consolidation - 2026-06-17 - 2 contacts flagged, 0 reassociated, 25 Tier 3 held
================================================================================================

Run summary: 355 flagged companies in pool (MaiaEdge own 124293230301 confirmed absent) - 125 zero-contact (no-op, archive-ready) - 230 with contacts. Tier 1 writes: 2 contact flags. Reassociations: 0 (Mode A handled upstream by R3 same-day; verified). Tier 3 holds: 18 preserved-contact companies + 7 ambiguous-domain contacts.

Method note: processed the FULL non-fit (Mode B) universe across the whole pool rather than the prior oldest-150-by-hs_object_id slice, so every genuine flag candidate was evaluated (82 Mode B companies < 150 cap). Mode A duplicates verified, not re-written (see Mode A section).

> WHAT NEEDS COOPER'S ACTION (surfaced by the CRM Ops Daily Digest):
> 1. Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete. Current CRM-wide count: 376 contacts flagged for deletion (+2 this run).
> 2. Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs stale associations; 355 flagged companies, 125 of them zero-contact and clean to archive now).
> CAUTION: 18 flagged companies still carry an active/fresh contact with no ICP primary (Tier 3 table below) - review those before archiving so an active relationship is not orphaned.

Run health: GREEN
 - 0 errors, both Tier 1 writes succeeded and verified, 0 mis-flag investigations.
 - Tier 3 items are steady-state carryover (active contacts on flagged non-fit companies), not new failures - consistent with the 2026-06-15/06-16 GREEN runs.

Errors: None.

------------------------------------------------------------------------------------------------
PROCESSING BREAKDOWN
------------------------------------------------------------------------------------------------

MODE A - DUPLICATES (119 companies / 436 contacts) - preserved via R3 reassociation, NO writes this run
  R3 (Duplicate Accounts, daily 2am ET) flags each duplicate with reason 'Duplicate (merged): contacts
  reassociated to primary X' and performs the reassociation. Spot-verified the named ICP primaries are
  live ICP records with contact counts consistent with reassociation having occurred:
    - Verizon (192899501812)  Network Operator T1  486 contacts  <- absorbed Verizon Wireless (114) + one.verizon.com (3) duplicates
    - Thrive (193034821365)   MSP/Aggregator T2     62 contacts  <- absorbed Thrive duplicate (11)
    - Hut 8 (324208873163)    NeoCloud T1           17 contacts
    - Riot Platforms (297892337355) NeoCloud T1      22 contacts
    - Sify (322877846251)     Data Center Colo T1    4 contacts
  LOAD-BEARING ASSUMPTION (flagged): contacts on the 119 duplicate records are reachable via their
  active ICP primary, so they are PRESERVED (not flagged) and not re-reassociated. Any residual
  un-reassociated contact is caught by R6's orphan-contact drain after Cooper archives the duplicate.
  No data-loss path. Diverges from prior runs that re-ran a handful (6-17) of Mode A adds; those were
  same-day-new dupes already handled by today's 2am R3.

MODE B - GENUINE NON-FITS (111 companies / 279 contacts) - no ICP primary, flag non-preserved contacts
  - 29 companies skipped: company createdate <= 14 days (Invariant E fresh-record grace); ~36 contacts deferred to a future run.
  - 82 companies processed (243 contacts evaluated):
      210  already flagged_for_deletion=true from prior runs (resolved, no-op)
       23  preserved - activity <=90d / created <=14d / subscriber (held on company)
        1  protected - opportunity lifecycle + open deal (anthonys@broadstar.com)
        2  boundary-preserved - last activity 92d (just past the 90d line; held per Invariant F)
        5  ambiguous email domain vs company domain (held, shared-contact safety)
        2  NEW Mode B flags written (Tier 1) -- see table

HARD STOPS / GATES
  - Open-deal hard stop (Invariant D): flag-target companies checked -> 0 open deals. No company-level open-deal blocks among processed non-fits.
  - Customer-history hard stop (Invariant C): 0 closed-won among processed companies.
  - Pre-Phase-1 Enterprise defensive check (C-bis): 24 account_brief keyword candidates examined; ALL
    created/enriched after the 2026-05-11 Enterprise ICP promotion (already judged under current framing)
    and are legitimate non-fits/dupes (e.g. furniture wholesaler, BPO, $22.7B industrial distributor
    explicitly rejected against the Enterprise scale gate). 0 genuine pre-promotion Enterprise mis-flags.

```
MODE B - NEW FLAGS (Tier 1, applied + verified)
| Contact ID    | Name           | Email                     | Company (id)                  | Reason code | Signals
|---------------|----------------|---------------------------|-------------------------------|-------------|--------
| 406499305150  | Varun Malhi    | e16varunpm@iima.ac.in     | IIM Ahmedabad (277387036380)  | No ICP fit  | 0 activity, lead, created 137d, academic institution
| 494730568436  | Christopher Fox| cfox@mjminnovations.com   | MjM Innovations (325339396851)| No ICP fit  | 0 activity, lead, created 15d, domain-verified employee
```

MODE A - REASSOCIATIONS: none this run (R3-owned; see Mode A section).

```
TIER 3 HELD - active/fresh contacts on flagged non-fit companies (no ICP primary; review before archive)
| Company (id)                          | Active contacts | Note
|---------------------------------------|-----------------|-----
| Novita AI (300372855493)              | 3               | preserved/active
| ?fp8.ai                               | 2               | unmappable email domain (fp8.ai) - cannot confirm employer, held
| Dragonfly Internet (322355279547)     | 2               | preserved/active
| FPX AI (311392963281)                 | 2               | preserved/active
| ?backbonedigital.com                  | 2               | unmappable email domain (backbonedigital.com) - cannot confirm employer, held
| ?broadstar.com                        | 1               | unmappable email domain (broadstar.com) - cannot confirm employer, held
| FlowSec (193865438923)                | 1               | preserved/active
| Essextel (303896262390)               | 1               | preserved/active
| IP Transfer (316538883827)            | 1               | preserved/active
| Manor (316508757740)                  | 1               | preserved/active
| HyperLink Infrastructure, LLC (316164220626) | 1               | preserved/active
| Commercial Electronics (322877970151) | 1               | preserved/active
| BitStream (322400659175)              | 1               | preserved/active
| Würth Industry North America (322795603660) | 1               | preserved/active
| Allegion (322639574776)               | 1               | preserved/active
| I & S Group (323231323868)            | 1               | preserved/active
| Eric Hanselman (323149135546)         | 1               | preserved/active
| Truepacket (132996276936)             | 1               | preserved/active
| Attobahn, Inc. (324610914007)         | 1               | preserved/active
| CarrierX (209233708749)               | 1               | preserved/active
| Saturn Cloud (297918677722)           | 1               | preserved/active
| ?att.com                              | 1               | unmappable email domain (att.com) - cannot confirm employer, held
| ?clinellc.com                         | 1               | unmappable email domain (clinellc.com) - cannot confirm employer, held
```

Note: the 2 boundary-preserved contacts (sebastian@saturncloud.io 451588831988; jscandrol@lspower.com
455480763107, both last-activity 92d) will become flag-eligible on the next run once clearly past the 90-day window.

Cross-routine ledger: appended one Run-log row (status GREEN) + an R4 Tier 3 carryover note to canvas F0B0AFSB9LN.
Prior 52 R4-owned Tier 3 holds (dated 2026-05-22) re-affirmed as still-open steady-state; approaching 30-day auto-demote.