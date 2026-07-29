# CRM Guardian - Flagged Consolidation - 2026-06-10 - 6 contacts flagged, 17 reassociated, 4 Tier 3 holds

Run summary: 150 flagged companies processed (of 301 in queue; per-run cap 150) - 269 contacts preservation-evaluated - 6 Tier 1 new flags / 17 Tier 1-2 reassociations (+flag cleared) / 4 Tier 3 hold groups - 73 zero-contact companies fully resolved (await archive) - 11 duplicate companies already R3-reassociated (no action).

Run health: YELLOW
- Writes succeeded (23/23 contact writes, 0 failed). Tier 3 holds present (name-collision + Expedient investigation). Partial run: 151 companies remain for next run (cap reached).

Errors: None. No invariant-C (closed-won) or invariant-D (open-deal) blocks fired - 0 of 150 companies had associated deals. No <14-day fresh-company skips. C-bis Enterprise defensive check: 30-day backfill window elapsed (2026-06-10); reason scan of all 77 with-contact companies surfaced no Enterprise mis-flags (all clearly non-ICP: animal health, PR/consultancy, wholesale voice, VPN apps, bitcoin-mining hosting, etc.).

> WHAT NEEDS COOPER'S ACTION (surfaced by the digest):
> 1. Filter HubSpot Contacts -> flagged_for_deletion = true -> review and bulk-delete
> 2. Then filter HubSpot Companies -> customer_segment = "Flagged for deletion" -> archive (severs stale associations from the 17 reassociated contacts)
> 3. Review the 4 Tier 3 hold groups below before archiving the affected companies.

## Writes executed this run

### Mode B - new contact flags (6)
Genuine non-fit companies; contacts not preserved, not protected.
- Novus International (animal health): 4 contacts -> flagged_for_deletion=true (464762474230, 464764609219, 464764609210, 464767533808)
- Saturn Cloud (MLOps, non-fit): 1 contact (457796906724)
- 1 blank-email contact (451617063647)

### Mode A - reassociations to ICP primary + flag cleared (17 contacts, 5 duplicate companies)
| Flagged duplicate | ICP primary | Contacts reassociated |
|---|---|---|
| ColoHouse (254570392308) | Hivelocity (Colo) (254575820474) | 1 |
| Steadfast Networks (264355635947) | Hivelocity (Colo) (254575820474) | 2 |
| 5c.ai (303285145301) | 5C Data Centers (Colo) (264355635939) | 8 |
| Bluebird Network (316163237567) | Bluebird Network/Fiber (Fiber) (323821758151) | 2 |
| Edged Data Centers (251566704352) | Edged Energy (Colo) (251592703686) | 4 |

## Tier 3 holds (NEW - need Cooper review)

1. **Unifi (316282051272) name collision** - 2 contacts are @ui.com (Ubiquiti Inc, the UniFi product line), NOT Telekom Malaysia's "Unifi" broadband brand (the flagged record's intended primary 316203554529). Held - did NOT reassociate to Telekom Malaysia. Recommend: detach from the TM-dup record; either standalone Ubiquiti record or delete. (471118763748 Young Kao, 471119406830 Alan Huang)

2. **nFrame / Expedient cluster investigation** - 44 @expedient.com contacts under "nFrame (Expedient)" (193853915836, flagged "Defunct") are already flagged_for_deletion=true from prior runs, BUT the reason states "Expedient is the surviving brand" and a separate nFrame record (303849415362) also points to Expedient as canonical. If an active Expedient ICP record exists, these 44 contacts should be REASSOCIATED, not deleted. Held for Cooper - no flag change made this run. Recommend: confirm whether Expedient is an active ICP company in CRM; if so, reassociate these 44 before any bulk-delete.

3. **10 acquisition-consolidation "duplicates" with no exact-match primary** - flagged as duplicate of an acquirer with a different name/domain (not a true exact-match duplicate). No HIGH-confidence (exact domain/name) primary resolvable, so contacts held rather than reassociated:
   - Cloud Age -> Connectbase ("if one exists"); Lightower -> Zayo; Troy Cablevision -> C Spire; US Internet -> T-Mobile; Globix (no primary named); Atlantic Metro -> 365 Data Centers; FPL FiberNet -> Crown Castle Fiber / Zayo (two named, ambiguous); RagingWire -> NTT Global Data Centers; Shaw -> Rogers; nFrame -> Expedient.
   - Recommend: Cooper confirm each acquirer primary (or treat as standalone) so a future run can reassociate.

4. **21 preserved contacts on genuine non-fit companies** - recent activity (<=90d) or fresh (<=14d createdate) or active lifecyclestage. No ICP primary exists (company is a true non-fit), so held - not flagged, not reassociated. Safe default per invariant F.

## No-action buckets
- 73 zero-contact flagged companies: fully resolved, await Cooper's company archive.
- 11 duplicate companies already reassociated by R3 (contacts on primary): United Cooperative Services, Layer3, Citizens Telephone Cooperative, Sify Technologies, EdgeCloudLink, MTA|Alasconnect, Armstrong Group, S&T Communications, Rowan Digital, Bulk Infrastructure, Symbio.
- 179 Mode B contacts already flagged_for_deletion=true (idempotent, no-op).

## Carryover
- 151 flagged companies not reached this run (cap 150 of 301). Next run continues the drain (sorted by hs_object_id ASC).

Ledger: appended Run-log row + Tier 3 block to canvas F0B0AFSB9LN. Note: canvas is ~909KB; full prior-item drain was limited by canvas size - new items appended after the most recent run-log row.
