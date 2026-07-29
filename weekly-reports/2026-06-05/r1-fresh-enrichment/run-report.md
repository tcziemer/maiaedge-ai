CRM Guardian - Fresh Enrichment - 2026-06-05 - 2/100 processed · 0 Tier 3 held

*Pool:* 18 candidates raw -> 16 Tier 3 client-side excluded -> 2 processed · cap 100 (steady state) · drain projection: 0 days (pool drained)

*Path counts (this run):*
- Path alpha full enrichment: 2 processed -> 2 ICP writes, 0 re-routed to gamma
- Path beta re-research: 0 processed
- Path gamma eviction: 0 processed

*Apollo:* 0 credits this run · 0/850 weekly (W23) · 850 remaining for week. Both records classified from public web research; state/country and firmographics clear, no Apollo gaps.
*Git:* JSON updated locally (best-effort commit not attempted from Cowork; on-disk report + canvas Run-log row are the audit trail of record)

*Path alpha - Full ICP enrichments (named, grouped by segment):*
- Operator ICP (Fiber):
  - AcceleCom (Fiber Operator / Long Haul / Backbone - Fiber operator / tier_2 / high_90) - Louisville KY wholesale + business fiber operator, Georgia's largest middle-mile network provider (acquired Georgia Public Web 2022). Multiple carriers (Vyve, LiveOak) ride its backbone; FTTH partnerships (Truvista, LiveOak, Vyve). Owner Tim Lieto (KY HQ = East, unchanged). State corrected Georgia -> Kentucky to reflect HQ per territory model (both East, owner unchanged).
  - BTC Broadband (Fiber Operator / Regional CLEC - Fiber operator / tier_3 / high_90) - 110-year-old independent local exchange carrier (Bixby Telephone Company), Bixby OK; fiber broadband + residential/business voice + hosted cloud comms (MaxUC). Name set from blank (support@mybtc.com is BTC Broadband's official support address - HIGH confidence match). State set Oklahoma, owner Ken Cunningham (OK = West, unchanged).
- No Enterprise classifications this run.
- No scale-gate failures routed to gamma.

*Path beta - Top 5 reclassifications:* none this run.

*Path gamma - Eviction summary:* 0 Partner Target keeps · 0 Flagged for deletion · 0 MISDOMAIN re-routes.

*What needs Cooper's attention:*
- 0 Tier 3 holds added this run.
- 0 records flagged for deletion this run.
- 0 partial-gate failures.
- Note: 16 of 18 raw candidates were Tier 3 client-side excluded - ALL are genuine standing R3-dedup stubs / Tier 3 holds (GVTC/Hotwire/Cityside/INDATEL email-subdomain + brand-overlap stubs flagged by R3 2026-06-05; us.ntt.net, g.softbank.co.jp, Digital Fortress, Verizon-wireless, columbus-networks MISDOMAIN, gatco, Synnap, Spartan DC, Attobahn, Tract Capital, teampoka standing holds; ResetData frozen-tier B2 no-op). None are genuinely-fresh ICP records being missed - verified each against canvas context.
- Recurring loop reminder (already escalated): ResetData (324591600333) keeps reappearing in Filter Group B2 because account_tier is blank and hs_is_target_account=true freezes the tier write. Cooper fix: set account_tier manually OR clear hs_is_target_account so the algo can assign tier_1 (Sovereign AI default).

*End-of-pipeline self-checks (D5 §9):*
1. Sub-segment nullness: PASS - both ICP writes carry a populated company_sub_segment.
2. Confidence-evidence alignment: PASS - both high_90 cite named positive evidence (AcceleCom middle-mile wholesale identity + carriers riding backbone; BTC operating ILEC fiber + business Ethernet/voice in defined OK region).
3. Disqualifier audit: PASS (vacuous) - 0 Other-via-eviction or D1 MATCH writes this run.
4. Catch-all guard: PASS - BTC = Regional CLEC (catch-all) backed by POSITIVE evidence (operating local-exchange fiber operator with business services), not exclusion-by-default; AcceleCom = Long Haul/Backbone (non-catch-all).

*Run health:* GREEN - full pool processed (2/2 non-excluded), 0 errors, gate-pass rate 100%, no Apollo cap pressure.

*Errors:* None.

---

```
Path alpha full ICP write table
| Account        | HubSpot ID    | Segment        | Sub-segment                          | Tier   | Confidence |
| -------------- | ------------- | -------------- | ------------------------------------ | ------ | ---------- |
| AcceleCom      | 326325637881  | Fiber Operator | Long Haul / Backbone - Fiber operator| tier_2 | high_90    |
| BTC Broadband  | 326286037697  | Fiber Operator | Regional CLEC - Fiber operator       | tier_3 | high_90    |
```

```
Path beta reclassification table
(none this run)
```

```
Path gamma eviction table
(none this run)
```

```
Tier 3 hold table
(none added this run)
```

```
Partial gate failure table
(none this run)
```
