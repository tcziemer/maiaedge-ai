CRM Guardian - Fresh Enrichment - 2026-06-17 - 2/100 processed · 2 Tier 3 held

Run summary: 12 raw candidates -> 10 standing-hold client-side excludes -> 2 processable, both resolved to Tier 3 dedup holds at Stage 0 (identity/dedup). 0 ICP writes, 0 evictions, 0 Apollo credits. 2 HubSpot property writes (name correction + dedup briefs + manual_review_required). Run health YELLOW.

--------------------------------------------------------------------------------

Pool: 2 processable candidates (12 raw, 10 excluded) · cap 100 (steady state) · drain projection: 0 days (full drain; pool empty after exclusions)

Path counts (this run):
- Path alpha full enrichment: 0 processed -> 0 ICP writes, 0 re-routed to gamma
- Path beta re-research: 0 processed -> 0 reclassified, 0 Tier 3 holds
- Path gamma eviction: 0 processed -> 0 Partner Target keeps, 0 Flagged for deletion, 0 MISDOMAIN re-routes
- Stage 0 dedup resolution: 2 Tier 3 dedup holds (both candidates resolved at identity/dedup stage; neither needed alpha/beta/gamma research depth)

Apollo: 0 credits this run · 2/850 weekly (W25) · 848 remaining for week
Git: best-effort commit handled in Apollo budget post-run step

--------------------------------------------------------------------------------

CANDIDATE RESOLUTION (2 processable)

1. Nextlink Internet (R0 had named it "NXLink") - 328126464704 - team.nxlink.com
   - Trigger source: Filter Group A (blank customer_segment). R0 Import Validator renamed it from blank to "NXLink" this morning and wrote an "NXAI CCaaS" brief.
   - Resolution: TIER 3 DEDUP HOLD -> R3. team.nxlink.com is Nextlink Internet's customer-portal / email subdomain (Nextlink Internet = Hudson Oaks, Texas fixed-wireless and fiber WISP). It duplicates canonical Nextlink Internet record 320811765445 (Fiber Operator / Regional CLEC - Fiber operator, high_90, tier_3).
   - Decisive evidence: the 3 contacts already associated to this record all carry @team.nxlink.com emails and are Nextlink Internet people tagged customer_segment = Fiber Operator (Bill Baker CEO bbaker@team.nxlink.com, Claude Aiken Chief Strategy Officer caiken@team.nxlink.com, Allyson Koehler Sales Director akoehler@team.nxlink.com). Web search confirms nxlink.com is Nextlink Internet's domain (support@team.nxlink.com), distinct from the unrelated NXAI CCaaS product which lives at nxlink.ai.
   - Writes: name corrected to "Nextlink Internet"; dedup account_brief written; segmentation_confidence = manual_review_required. NO customer_segment / sub_segment / account_tier / last_enriched_date / signal_heat. State (TX), country (US), owner (Ken, West) left as-is - all correct for Nextlink Internet.
   - NOTE: this was NOT evicted. It is a real Fiber Operator duplicate, not junk. An eviction here would have been wrong. The contact-email evidence overturned R0's NXAI read.

2. Schwarz Digits - 327944646384 - digits.schwarz
   - Trigger source: Filter Group A (blank customer_segment). R0 renamed it from blank to "Schwarz Digits" + wrote a brief this morning (correctly).
   - Resolution: TIER 3 PARENT-DEDUP HOLD -> R3. Schwarz Digits is the digital-services division of Germany's Schwarz Group (Lidl / Kaufland parent) and is the corporate parent of STACKIT, which already exists as an active NeoCloud / Sovereign AI Clouds - Neocloud record (326722976497, tier_1, owner Tim Z). STACKIT's own brief and recent_news already capture the same flagship trigger event - the 11 billion euro, 200 MW, 100,000-GPU sovereign AI campus at Luebbenau, Brandenburg, which STACKIT operates. Classifying Schwarz Digits as a parallel NeoCloud would duplicate the rep target.
   - Writes: parent-dedup account_brief written; segmentation_confidence = manual_review_required. NO customer_segment / sub_segment / account_tier / last_enriched_date / signal_heat. R0's name (Schwarz Digits), owner (Tim Z, International), state (Baden-Wuerttemberg), country (Germany) left as-is - all correct.

--------------------------------------------------------------------------------

What needs Cooper's attention:
- 2 Tier 3 dedup holds, both to R3 (Duplicate Accounts). See canvas F0B0AFSB9LN section "R1 Fresh Enrichment 2026-06-17 - Tier 3 holds added".
  - 328126464704 (Nextlink Internet / team.nxlink.com) -> merge into canonical Nextlink Internet 320811765445 and reassociate the 3 @team.nxlink.com contacts to the primary.
  - 327944646384 (Schwarz Digits) -> associate as parent of STACKIT 326722976497, or merge.
- R0 wrong-entity note (process observation, no action required): R0 Import Validator's 2026-06-17 run misidentified team.nxlink.com as NXAI's NXLink CCaaS. Root cause: nxlink.com (Nextlink Internet, Texas ISP) was conflated with nxlink.ai (NXAI, the CCaaS product). R0's rename was reasonable (anchoring a blank-name import) but the brief was wrong-entity; R1 corrected name + brief. Flagging only in case the .com-vs-.ai / product-vs-operator conflation recurs in R0's identity step.
- 0 Flagged for deletion this run.
- 0 partial gate failures.

Run health: YELLOW
- Full processable drain (2/2), 0 errors, 0 Apollo pressure, backlog not elevated. YELLOW because both candidates resolved to Tier 3 dedup holds (0 definitive classifications). These are mechanical dedup artifacts (a subdomain duplicate and a parent-of-existing-ICP), not classification ambiguity, so they are correctly routed to R3 rather than guessed.

Errors: None

End-of-pipeline self-checks (all vacuously PASS - 0 definitive classifications this run):
1. Sub-segment nullness check: PASS (0 records written to an ICP customer_segment).
2. Confidence-evidence alignment check: PASS (0 high_90 writes; both writes are manual_review_required dedup holds).
3. Disqualifier audit check: PASS (0 Other / eviction / D1 MATCH writes).
4. Catch-all guard check: PASS (0 Regional CLEC / Standard - colo / Telecom Aggregator classifications).

--------------------------------------------------------------------------------

Tier 3 hold table:

```
| Account                        | HubSpot ID   | Path          | Ambiguity / Reason                                                                                   |
| ------------------------------ | ------------ | ------------- | ---------------------------------------------------------------------------------------------------- |
| Nextlink Internet (was NXLink) | 328126464704 | Stage 0 dedup | team.nxlink.com email/portal subdomain of Nextlink Internet; dup of 320811765445; R3 merge + contact reassoc |
| Schwarz Digits                 | 327944646384 | Stage 0 dedup | Parent (Schwarz Group digital arm) of STACKIT NeoCloud 326722976497; R3 associate-as-parent or merge |
```

Path alpha full ICP write table: (none this run)
Path beta reclassification table: (none this run)
Path gamma eviction table: (none this run)
Partial gate failure table: (none this run)

--------------------------------------------------------------------------------

Pre-flight standing-hold excludes applied (10, each verified present in canvas F0B0AFSB9LN via grep):

```
| HubSpot ID   | Account            | Standing hold owner |
| ------------ | ------------------ | ------------------- |
| 326713856698 | t.ht.hr            | R0 2026-06-09 subdomain artifact |
| 326642118391 | wechsler.ch        | R0 2026-06-09 ambiguous identity |
| 326735614690 | SoftBank Capital   | R3 dedup            |
| 326731977463 | bertellifamily.org | R0 2026-06-09 non-business |
| 326207777466 | terrycorder.com    | R6 dead-site (Cooper-owned) |
| 326188916440 | Poly-AI            | R3 dedup (Poly-AI/PolyAI pair) |
| 326350146247 | PolyAI             | R3 dedup (Poly-AI/PolyAI pair) |
| 326171165395 | ConvergeOne        | R3 dedup (vs C1)    |
| 326196119272 | Cityside Networks  | R3 dedup (vs Cityside Fiber) |
| 324597786339 | columbus-networks  | MISDOMAIN (finetechnologies.co) |
```

Run parameters:
- Trigger query: 5 filterGroups (A blank segment, B1 ICP sub_segment blank, B2 ICP tier blank, C Unknown, D low-conf Other/Partner). Sort createdate DESC, cap 100. Returned 12. MaiaEdge own (124293230301) not present.
- Customer-protection / closed-won hard stops: none triggered.
- Apollo credits consumed: 0 (both candidates Tier 3 dedup holds; no ICP firmographic gap to fill).
- web_search: 4 total (NXLink/NXAI x1, Schwarz Digits/STACKIT x1, nxlink.com/Nextlink x1, plus the R0-report cross-check). web_fetch: 0.
- HubSpot writes: 1 batch, 2 objects (328126464704, 327944646384), 0 errors, 0 retries.
