CRM Guardian - Import Validator - 2026-06-04 - 0 domain-corrected, 1 renamed, 2 flagged, 1 held

Run summary: 5 records scanned; buckets = 1 RENAMABLE / 1 MATCH / 2 HARD_FLAG / 1 Tier 3; 4 HubSpot writes; 0 errors.

What needs Cooper's attention:
- 1 NEW Tier 3 hold (teampoka.com 325800222448) - domain resolves to parking IPs (incl. 208.91.197.27, a known domain-parking address) with no identifiable business in web search and a blank HubSpot name. Suspected parked/dead but could not load the page to positively confirm a parked landing page, so held rather than auto-flagged.
- 4 carryover R0 Tier 3 holds re-checked against current HubSpot state; Cooper has not acted on any, all still blank/no-segment with no last_enriched_date. All carried forward unchanged.
- 2 hard-flagged companies (McGough, Latham & Watkins) - Filter HubSpot Companies -> customer_segment = "Flagged for deletion" to review/archive.

Run health: YELLOW
- 0 errors, all 4 writes succeeded, but 1 NEW Tier 3 hold present (suspected-parked domain unconfirmed).

Errors: None

---

## Domain Corrections (Tier 1/2)
None this run.

## Renames (Tier 1 - HIGH)

```
| ID            | Old name | New name  | Domain        | Evidence                                                                                          |
|---------------|----------|-----------|---------------|---------------------------------------------------------------------------------------------------|
| 325917807315  | (blank)  | LitFiber  | litfiber.org  | litfiber.org is LitFiber's contact/email domain (info@litfiber.org); LitFiber is a fiber-to-the-  |
|               |          |           |               | home ISP (Western KY; expanding OH + TX; Omni Fiber / Lit Fiber group, Oak Hill Capital). HIGH.   |
```

last_enriched_date left blank -> R1 Fresh Enrichment picks it up at 10:00 AM CT. signal_heat = Cold (new-record default).

## MATCH (no correction; queued for R1)

```
| ID            | Name              | Domain          | Notes                                                                                              |
|---------------|-------------------|-----------------|----------------------------------------------------------------------------------------------------|
| 325787887340  | Core Technologies | coretechinc.com | Name matches domain. CTI = Norcross GA carrier-services / wire-and-cable / IT / AV installation     |
|               |                   |                 | contractor, ~$8.4M rev, ~25 staff, federal-heavy. Telecom-services angle is borderline contractor   |
|               |                   |                 | vs MSP - left for R1 full classification rather than auto-flagged. signal_heat = Cold default.      |
```

## Hard-flagged (Tier 2 - HIGH)

```
| ID            | Name              | Domain      | Category              | Reason code  | Evidence                                                       |
|---------------|-------------------|-------------|-----------------------|--------------|----------------------------------------------------------------|
| 325905526482  | McGough           | mcgough.com | Construction contractor | No ICP fit | McGough is a Minneapolis-St. Paul commercial construction +    |
|               |                   |             |                       |              | development firm (est. 1956). Builds facilities, does not       |
|               |                   |             |                       |              | operate carrier infra/fiber/colo/network. HIGH.                |
| 325916440308  | Latham & Watkins  | lw.com      | Law firm / legal svcs | No ICP fit   | lw.com = Latham & Watkins LLP, global law firm (3,500+ lawyers).|
|               |                   |             |                       |              | Legal services, no ICP path. Not PARTNER_KEEP. HIGH.           |
```

last_enriched_date = 2026-06-04 stamped on both (definitive eviction).

## Tier 3 held (surface, no write)

```
| ID            | Name    | Domain        | Bucket    | web_search summary                                                                          |
|---------------|---------|---------------|-----------|---------------------------------------------------------------------------------------------|
| 325800222448  | (blank) | teampoka.com  | AMBIGUOUS | No business identifiable for teampoka.com in web search (closest hit teampoko.com is an      |
|               |         |               | / parked  | unrelated endurance-sports/FFXIV page). DNS resolves to parking IPs incl. 208.91.197.27 (a   |
|               |         |               |           | known domain-parking address) + Google registrar landing IPs. Suspected parked; page could  |
|               |         |               |           | not be loaded to confirm. Blank name offers no redemption. Held for Cooper.                  |
```

## Carryover R0 Tier 3 holds (re-checked, none resolved, all carried)

```
| date_first_surfaced | Record / domain                                  | ID            | Status                                                                 |
|---------------------|--------------------------------------------------|---------------|------------------------------------------------------------------------|
| 2026-05-27          | gatco.net                                        | 324524875475  | Unchanged (blank/no-segment). No clear public-entity match. CARRY.     |
| 2026-05-27          | columbus-networks / finetechnologies.co          | 324597786339  | Unchanged. MISDOMAIN vs RENAMABLE directional ambiguity. CARRY.        |
| 2026-06-02          | g.softbank.co.jp                                 | 325335795443  | Unchanged. Probable dup of SoftBank AI Cloud (324007728852); R3. CARRY.|
| 2026-06-02          | us.ntt.net                                       | 325335796410  | Unchanged. Near-dup of NTT (277437319928) / NTT GDC (133486361310); R3.|
```

Caps: 5 records scanned (well under 100-record cap). Apollo: 0 (Apollo-free routine). HubSpot writes: 4 (1 batch). Web searches: ~6.
