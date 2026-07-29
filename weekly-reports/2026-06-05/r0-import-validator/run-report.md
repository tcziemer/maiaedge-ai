CRM Guardian - Import Validator - 2026-06-05 - 0 domain-corrected, 2 renamed, 0 flagged, 1 held

Run summary: 4 records scanned, buckets = 2 RENAMABLE (HIGH) + 1 MATCH + 1 R3-dedup hold + 0 MISDOMAIN + 0 HARD_FLAG + 0 DEAD_DOMAIN + 0 AMBIGUOUS, 3 HubSpot writes (1 batch), 0 errors.

What needs Cooper's attention:
- 1 new Tier 3 / R3-dedup hold this run (indatelservices.com 326184182509) - duplicate of existing INDATEL record; routed to R3 for dedup verification + merge.
- 5 carryover R0 Tier 3 holds remain pending (Cooper has not acted on any; all re-checked against current HubSpot state, all unchanged): teampoka.com (325800222448, now identified as Poka Lambro dup -> R3), gatco.net (324524875475, entity ambiguous), columbus-networks/finetechnologies.co (324597786339, MISDOMAIN vs RENAMABLE directional ambiguity), g.softbank.co.jp (325335795443, SoftBank subdomain -> R3 dedup), us.ntt.net (325335796410, NTT backbone subdomain -> R3 dedup).
- 0 medium-confidence corrections to verify.

Run health: YELLOW (all writes succeeded; new + carryover Tier 3 holds present).

Errors: None.

---

Trigger window: createdate GTE 2026-06-04T14:03:42Z (24h, ET) AND last_enriched_date IS EMPTY AND customer_segment NEQ "Flagged for deletion", excluding MaiaEdge own record 124293230301. Total candidates = 4 (single page). Apollo credits consumed: 0.

## Renames (HIGH, auto-applied)

```
| HubSpot ID    | Old name | New name              | Domain (kept)        | Owner        | web_search basis |
|---------------|----------|-----------------------|----------------------|--------------|------------------|
| 326166406893  | (blank)  | Hotwire Communications| hotwiremail.com      | Tim Lieto    | hotwiremail.com is Hotwire Communications' customer webmail + contact domain (socialmedia@hotwiremail.com); Fision FTTH operator across FL/NC/SC/TX/GA/AZ/NV/CA/PA; canonical hotwirecommunications.com. 2+ sources (hotwirecommunications.com, BroadbandNow, HighSpeedInternet). |
| 326217545464  | (blank)  | GVTC Communications   | gvtc.net             | Ken Cunningham| gvtc.net = GVTC (Guadalupe Valley Telephone Cooperative), South-Central TX fiber co-op + wholesale carrier-ethernet transport (SA/Austin/Dallas/Houston); canonical gvtc.com. 2+ sources (gvtc.com, LinkedIn, BBCmag wholesale launch). |
```
signal_heat=Cold default written on both. last_enriched_date left blank (R0 rename is not a definitive enrichment gate; R1 picks up at 10:00 AM CT).

## MATCH (passed clean to R1)

```
| HubSpot ID    | Name             | Domain               | Owner        | Basis |
|---------------|------------------|----------------------|--------------|-------|
| 326196119272  | Cityside Networks| citysidenetworks.com | Ken Cunningham| Name = domain. Cityside Networks (dba Cityside Fiber) is a real SoCal/Orange County FTTP operator (Irvine, Lake Forest, Mission Viejo, Tustin, Dana Point), 5-Gig fiber. HIGH confidence MATCH. |
```
signal_heat=Cold default written (new record, no signal history). last_enriched_date left blank for R1.

## R3-dedup hold (new Tier 3 this run)

```
| HubSpot ID    | Name    | Domain              | Owner     | Why held |
|---------------|---------|---------------------|-----------|----------|
| 326184182509  | (blank) | indatelservices.com | Tim Lieto | Duplicate of existing INDATEL record (indatel.com, ID 322761764552, Fiber Operator / Regional CLEC, tier_3). indatelservices.com and indatel.com resolve to the same member-owned nationwide rural fiber aggregator (Overland Park KS, 400K+ route miles, 700+ RLECs). account_brief already present from prior touch. Routed to R3 for dedup verification + merge. No segment write; last_enriched_date left blank. |
```

## Carryover R0 Tier 3 holds (re-evaluated, all CARRY)

```
| date_first_surfaced | HubSpot ID    | Name/slug          | Domain             | Status |
|---------------------|---------------|--------------------|--------------------| -------|
| 2026-06-04          | 325800222448  | (blank)            | teampoka.com       | CARRY - now identified as Poka Lambro Telecom dup (poka.com 320876610271); routed to R3 dedup. Unchanged. |
| 2026-05-27          | 324524875475  | (blank)            | gatco.net          | CARRY - entity ambiguous (GATCO Bathware / GATCO Global UK / GATS Telecom diverge), India-registered. Unchanged. |
| 2026-05-27          | 324597786339  | columbus-networks  | finetechnologies.co| CARRY - directional ambiguity (slug Columbus/Liberty Networks; domain unrelated FL MSP; MISDOMAIN vs RENAMABLE unresolved). Unchanged. |
| 2026-06-02          | 325335795443  | (blank)            | g.softbank.co.jp   | CARRY - SoftBank mail subdomain artifact; dup of SoftBank records; routed to R3 dedup. Unchanged. |
| 2026-06-02          | 325335796410  | (blank)            | us.ntt.net         | CARRY - NTT Global IP Network backbone subdomain; near-dup of NTT (277437319928). Routed to R3 dedup. Unchanged. |
```
No carryover items drained (Cooper acted on none between runs).

## Hard stops honored
- MaiaEdge own record 124293230301 excluded by trigger query.
- No closed-won deals among candidates (no customer-protection trigger).
- No HARD_FLAG / DEAD_DOMAIN buckets this run; no last_enriched_date stamps written.
