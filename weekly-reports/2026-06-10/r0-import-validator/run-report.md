CRM Guardian - Import Validator - 2026-06-10 - 0 domain-corrected, 0 renamed, 1 flagged, 0 held

Run summary: 3 records scanned, buckets [0 MISDOMAIN / 0 RENAMABLE / 2 MATCH / 1 HARD_FLAG / 0 DEAD_DOMAIN / 0 AMBIGUOUS], 3 HubSpot writes, 0 errors

What needs Cooper's attention:
- 1 hard-flagged company - Filter HubSpot Companies -> customer_segment = "Flagged for deletion". Smoke-test placeholder record.
- 0 Tier 3 holds.
- 0 medium-confidence corrections to verify.

Run health: GREEN
- 0 errors, 0 Tier 3, all 3 writes succeeded.

Errors: slack_read_canvas returned a transient "connector not responding" error on the first call; succeeded on retry (canvas read OK). Non-blocking.

---

## Hard-flagged (auto-flag for deletion, HIGH confidence)

```
| HubSpot ID    | Old name | Domain                    | Entity at domain                          | Reason code              | last_enriched_date | web_search summary |
| ------------- | -------- | ------------------------- | ----------------------------------------- | ------------------------ | ------------------ | ------------------ |
| 326738821852  | (blank)  | zzzsmoketestprospect.com  | none - smoke-test placeholder, no business | Hard junk / non-business | 2026-06-10 (stamped) | Domain returns no identifiable business in search; name self-describes as a smoke-test prospect; HubSpot record has a blank company name, so no MISDOMAIN redemption path exists. |
```

## MATCH (no enriched-field write; left for R1 Fresh Enrichment at 10:00 AM CT)

```
| HubSpot ID    | Name     | Domain        | Entity at domain                                          | signal_heat default | web_search summary |
| ------------- | -------- | ------------- | --------------------------------------------------------- | ------------------- | ------------------ |
| 326866083559  | Cyfuture | cyfuture.com  | Cyfuture - Indian data center / colocation / cloud hosting / BPO provider since 2001; Tier III certified DCs in Noida, Jaipur, Raipur; MeitY-empaneled. Name matches domain. | Cold (written) | cyfuture.com + cyfuture.cloud + datacenters.com profile + LinkedIn all confirm same entity. In-ICP candidate (Colo / NeoCloud) - R1 will classify. |
| 326927535860  | CMDB360  | cmdb360.com   | CMDB-360 - configuration management database SaaS for MSPs (auto-discovery of cloud/on-prem assets via "Satellite" agents; OCI/AWS/Azure/GCP). Name matches domain. | Cold (written) | cmdb360.com + Microsoft/Oracle marketplace listings + ServiceNow docs confirm same entity. Software vendor, not an operator - R1 will adjudicate ICP fit (likely non-ICP). |
```

## Renames - review
None this run.

## Domain Corrections - review
None this run.

## Tier 3 held
None this run.

---

Bucket rationale notes:
- CMDB360 passes the R0 name-vs-domain check (the entity at cmdb360.com IS CMDB360). R0 validates name-vs-domain plausibility only; ICP fit is R1's call. CMDB360 is a legitimate software business and not in any hard-flag category, so MATCH is correct and it was NOT auto-flagged. R1's Path gamma eviction is Apollo-free, so no Apollo waste risk in deferring.
- No customer-protection (closed-won) records, no MaiaEdge own record (124293230301), no already-flagged records in the candidate set.
