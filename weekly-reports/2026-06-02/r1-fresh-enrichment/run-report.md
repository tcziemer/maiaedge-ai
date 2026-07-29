CRM Guardian - Fresh Enrichment - 2026-06-02 - 10/10 processed · 3 Tier 3 held

*Pool:* 10 candidates (17 raw, 7 Tier 3 client-side excluded) · cap 100 · drain projection: 0 days (pool fully drained this run)

*Path counts (this run):*
- Path α full enrichment: 6 processed → 5 ICP writes, 0 re-routed to γ (GetOnward re-routed γ→α as surprise ICP)
- Path β re-research: 4 processed → 0 reclassified, 3 Tier 3 holds (dedup), 1 frozen-tier no-op (ResetData)
- Path γ eviction: 1 processed → 0 Partner Target keeps, 1 Flagged for deletion, 0 MISDOMAIN re-routes

*Apollo:* 0 credits this run · 0/850 weekly (W23) · 850 remaining for week
*Git:* deferred (concurrent routine holding .git/index.lock); JSON updated locally

*Path α - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Fiber / Network Op):
  - GSL Networks / Global Secure Layer (Network Operator(Tier 1 / VNO) / International Backbone Specialist - Network Op / tier_1 / medium_7089) - Australia, Tim Z. Mid-market global IP transit + DDoS specialist (AS137409, 4,600+ peers).
  - Telia Company (Network Operator(Tier 1 / VNO) / Tier 1 Carrier - Network Op / tier_1 / high_90) - Sweden, Tim Z. Nordic/Baltic incumbent; confirmed NOT a dup of divested Telia Carrier/Arelion (teliacarrier.com) or Telia Lietuva (telia.lt).
  - Plumas-Sierra Rural Electric Cooperative (Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 / high_90) - California, Ken. PST fiber subsidiary + ~$67M CPUC middle-mile grants.
  - Optage / K-Opticom (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90) - Japan, Tim Z. Kansai Electric FTTH (eo HIKARI) + Osaka DCs.
  - GetOnward / Onward (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90) - California, Ken. SURPRISE ICP: formerly Inyo Networks, registered CA/NV CLEC, runs Digital 395 middle-mile + municipal broadband partnerships. Pre-scored LIKELY_NON_ICP on name, re-routed γ→α after research.
- Enterprise ICP (Multi-DC): none this run.
- Enterprise scale-gate failures routed to Path γ: none this run.

*Path β - Top 5 reclassifications:* None (no segment shifts; 4 β records resolved to 3 dedup Tier 3 holds + 1 frozen-tier no-op).

*Path γ - Eviction summary:*
- 0 Partner Target keeps · 1 Flagged for deletion (MJM Innovations - No ICP fit, transit-management software vendor)

*What needs Cooper's attention:*
- 3 Tier 3 dedup holds (routine R3 handoffs) - see canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-02" + table below. All 3 are duplicate/email-subdomain artifacts of existing clean ICP records; R3 should consolidate/archive.
- 1 Flagged for deletion (MJM Innovations 325339396851) in HubSpot Companies filter customer_segment = "Flagged for deletion".
- RECURRING: ResetData (324591600333) reappears daily via Filter Group B2 (account_tier blank + hs_is_target_account=true freezes the tier write). Already escalated 2026-05-28/29 + 06-01. Resolution: set account_tier manually OR clear hs_is_target_account so the algo assigns tier_1 (Sovereign AI default).
- 0 records partial-enriched (no gate failures).

*Run health:* YELLOW (full cap processed, 0 errors, 100% gate-pass on attempted writes, no Apollo pressure; YELLOW only because 3 routine R3 dedup Tier 3 holds were added).

*End-of-pipeline self-checks (D5 §9):*
1. Sub-segment nullness check: PASS - all 5 ICP writes carry a populated company_sub_segment.
2. Confidence-evidence alignment: PASS - 4 high_90 writes (Telia, Plumas-Sierra, Optage, GetOnward) each carry named anchor/evidence reasoning; GSL is medium_7089 (mid-market scale acknowledged).
3. Disqualifier audit: PASS - 0 "Other" eviction writes this run; the 1 Flagged-for-deletion (MJM) cites a No-ICP-fit rationale.
4. Catch-all guard: PASS - both Regional CLEC writes (Optage, GetOnward) cite positive facilities-based-fiber evidence, not exclusion-by-default.

*Errors:* None

---

```
Path alpha - Full ICP write table
| Account                                  | HubSpot ID    | Segment                          | Sub-segment                                    | Tier   | Confidence  |
| GSL Networks (Global Secure Layer)       | 325323216629  | Network Operator(Tier 1 / VNO)   | International Backbone Specialist - Network Op  | tier_1 | medium_7089 |
| Telia Company                            | 325333996232  | Network Operator(Tier 1 / VNO)   | Tier 1 Carrier - Network Op                    | tier_1 | high_90     |
| Plumas-Sierra Rural Electric Cooperative | 325339396852  | Fiber Operator                   | Municipal / Cooperative - Fiber operator       | tier_4 | high_90     |
| Optage (K-Opticom)                       | 325339396848  | Fiber Operator                   | Regional CLEC - Fiber operator                 | tier_3 | high_90     |
| GetOnward (Onward)                       | 325326814914  | Fiber Operator                   | Regional CLEC - Fiber operator                 | tier_3 | high_90     |
```

```
Path beta reclassification table
| Account | HubSpot ID | Was -> Became | Confidence delta |
| (none)  | -          | -             | -                |
```

```
Path gamma eviction table
| Account          | HubSpot ID    | Outcome              | Reason                                                                     |
| MJM Innovations  | 325339396851  | Flagged for deletion | No ICP fit: transit-management software vendor, no carrier reference value |
```

```
Tier 3 hold table
| Account                       | HubSpot ID    | Path | Ambiguity                                                                  |
| Digital Fortress (dfcolo.com) | 325323215608  | beta | Duplicate of 264034894551 (digital-fortress.com, Standard - colo); R3 consolidate |
| us.ntt.net (no name)          | 325335796410  | beta | NTT GIN email-subdomain artifact; dup of NTT 277437319928; R3 consolidate  |
| g.softbank.co.jp (no name)    | 325335795443  | beta | SoftBank email-subdomain artifact; dup of SoftBank Corp; recurring import; R3 |
```

```
Partial gate failure table
| Account | HubSpot ID | Path | Missing fields |
| (none)  | -          | -    | -              |
```
