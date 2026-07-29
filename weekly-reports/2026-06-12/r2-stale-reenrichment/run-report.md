# CRM Guardian - Stale Re-Enrichment - 2026-06-12 - 7 Tier 2 flagged, 1 Tier 3 held

Run summary: 40/100 processed (39 written, 1 held) · FULL 1 / LIGHT 39 (7 evictions, 21 brief-fills, 10 re-verifications, 1 hold) / RECLASSIFY 0 / DEFER 0 · Tier 1: 32 / Tier 2: 7 / Tier 3: 1 new + 3 standing carried · Apollo: 0 used / 850 remaining (W24, sub-cap 50 untouched) · Freshness: GREEN

What needs Cooper's attention:
- 7 eviction Tier 2 - Filter HubSpot Companies -> customer_segment = "Flagged for deletion" (all verified 0 deals, reason codes set)
- 1 segment transition to verify - Integrity Advanced Technologies reclassified Fiber Operator -> MSP/Aggregator (see below)
- 1 NEW Tier 3 hold - Confluence Research (re-verification failed)
- 3 records deferred to next run (cap math): Fiber Gaming Network, Gaichu Managed Services, Sterling and Wilson

Run health: GREEN

Errors: None

---

## Trigger query

Today 2026-06-12 (ET), 120-day cutoff 2026-02-12.

- Filter A (last_enriched_date < 2026-02-12, active segments): **0 records** - active pool fully rotated.
- Filter B (never enriched + segment populated): **1 net** - Integrity Advanced Technologies (327026419390), R1's same-day low_5069 unstamped handoff per the 2026-06-08 precedent. MaiaEdge own record did not appear (hard-stop filter held).
- Filter C rotation pre-spread (A+B = 1 < 40): fired. Active pool 3,406 with last_enriched_date >= 2026-02-12. Pulled 45 oldest-enriched (2026-02-24 to 2026-04-27 cohort); 3 were standing canvas Tier 3 holds (excluded); took 39 of the remaining 42 to reach the 40-candidate target; deferred 3 newest-position records to next run.

## FULL path (1)

**Integrity Advanced Technologies (327026419390, integrityatech.com) - RECLASSIFIED + stamped.**
R1 classified Fiber Operator / Long Haul / Backbone at low_5069 this morning (route-mile scale unverified) and handed to R2. Deep-dive findings: the site's "400,000 route miles of dark fiber" claim cannot be owned plant (larger than the entire US dark fiber market leaders combined) and the disclosed partner ecosystem (KBR, Teya, SecureG, CyberKinetics, construction/services firms) contains zero carrier asset owners - consistent with aggregated partner capacity marketed for resale. Business model: tribally owned (Teya ANC + Integrity Technologies Corp JV, Dec 2024) network solutions reseller through federal contract vehicles, with adjacent cyber/SD-WAN/IT services, 13 DC interconnects.

- customer_segment: Fiber Operator -> **MSP/Aggregator**, company_sub_segment: **Telecom Aggregator - MSP**, segmentation_confidence: low_5069 -> **medium_7089** (best-fit per F.3; fiber-ownership evidence collapsed under scrutiny, so no genuine 2-way ambiguity; medium not high because the company is young with thin disclosure)
- account_tier: tier_2 unchanged (Telecom Aggregator default T2, no signal modifiers, 0 associated deals verified, hs_is_target_account not set)
- signal_heat: Cold unchanged (last_signal_date null)
- 7 enriched fields refreshed; recent_news left blank (formation event Dec 2024 is stale; no last_signal_date written)
- Completeness Gate: PASS -> last_enriched_date = 2026-06-12 (resolves the R1 handoff loop)
- Owner: Ken Cunningham unchanged (ND = West). Contact segment-mirror skipped (contact customer_segment enum lacks MSP/Aggregator)

## LIGHT path (39)

### Evictions - Tier 2, date bumped (7)

```
| Company                            | ID           | Reason code | Evidence                                              |
|------------------------------------|--------------|-------------|-------------------------------------------------------|
| Nashoba Valley Technical High Sch. | 286492707559 | No ICP fit  | Vocational high school, Westford MA                   |
| CodeDay                            | 193853195001 | No ICP fit  | Student hackathon nonprofit                           |
| IIM Ahmedabad                      | 277387036380 | No ICP fit  | Academic business school, Gujarat India               |
| LANEX                              | 271875845881 | No ICP fit  | Generic WI web/software agency, non-telecom verticals |
| North American Space Institute     | 320311807732 | No ICP fit  | Space workforce certification JV, 5 employees         |
| BT International Services (Korea)  | 318106540786 | No ICP fit  | Seoul insurance co; import name-confusion artifact    |
| Telemetro Reporta                  | 318207597276 | No ICP fit  | Panamanian TV broadcaster                             |
```

All 7 verified 0 associated deals (single batched deals query) before flagging. flagged_for_deletion_reason written in the same update as the segment flip; briefs rewritten with trailing eviction clause. Eviction line drawn at zero commercial adjacency to telecom/infrastructure (schools, nonprofits, wrong-vertical entities, generic agencies) - consistent with the 2026-06-11 eviction set; telecom-ecosystem references (analysts, media, vendors, contractors, hyperscalers) kept.

### Keeper brief-fills + sentinels + heat Cold + stamp (21)

Web-verified: Vytal (Winnipeg fiber network construction), GigRx / SP Data Digital (fiber-sales BPO), Oculum (white-label UC PaaS into carriers), Iometrix (Mplify/MEF accredited certification lab), GeoResults by Opensignal (telecom prospecting data), Canoga Perkins (alive - MWC Barcelona 2026, SyncMetra 5G timing), QKS Group (analyst, ex-Quadrant Knowledge Solutions), Tower Engineering Solutions (Congruex tower engineering - **name fixed** from "testower.us"), Appledore Research (**name fixed** from "appledorerg").
Knowledge-briefed (stable public entities): OpenAI, Amdocs, HubSpot, Alibaba Cloud, Tencent Cloud, Weka, Arqit, Nile (NaaS competitive reference), Greenhill/Mizuho, Vertical Systems Group, Atlantic-ACM, RTInsights.
All received: account_brief (2-4 sentences), infrastructure_profile = "None Identified", fabric_provisioning_approach = "none_identified", signal_heat = Cold (where blank), last_enriched_date = 2026-06-12. Tier no-op (Other/Partner Target, compute_tier Step A0 exit).

### Keeper re-verifications - sentinels + heat backfill + stamp, existing April briefs retained (10)

MNJ Technologies, TeleGeography, FreeWheel, Ubiquiti (PT tier_3), Tele-Plus, Telx Computers, Star Solutions (PT tier_4), Clear-Com, Davis Infrastructure (PT tier_4), JAWAB.

### Tier 3 held - no write, no date bump (1 new)

```
| Company             | ID           | Reason                                                                              |
|---------------------|--------------|-------------------------------------------------------------------------------------|
| Confluence Research | 192890159856 | confluenceresearch.com.au: 2x web_search inconclusive (no AU entity surfaces),       |
|                     |              | domain unfetchable this session. Re-verification failed - held for next run.        |
```

### Standing holds carried forward unprocessed (3)

MMR Fiber / SouthWestern Power 175221473010 (R3 entity-split), team.telstra.com 316598423243 (R3 subdomain dedup), Intercontinental Exchange 311326703342 (R2 2026-06-10 hold, Enterprise-vs-Colo disambiguation awaiting Cooper).

### Deferred to next run (3)

Fiber Gaming Network 320364986071, Gaichu Managed Services 318231691995, Sterling and Wilson 277439113953 (pre-spread cap math; all 2026-04-27 cohort, return at front of tomorrow's Filter C queue).

## Partial Enrichment - held for next run

None.

## Recent news cleared (stale)

None (no candidate carried a stale last_signal_date; Integrity's was null).

## Writes + budget

4 HubSpot batches: 10/10, 10/10, 10/10, 9/9 - 0 failures. Apollo: 0 credits (LIGHT path Apollo-free by design; FULL pass resolved via web research; Apollo MCP interactive-confirm guardrail unavailable in scheduled runs). W24 weekly: 0/850 consumed. apollo-budget.json updated.

## Notes

- Pre-spread continues working the late-September cliff: today re-stamped the remainder of the 2026-04-27 cohort; next due-dates stagger to ~2026-10-10.
- The 2026-04-27 cohort is now fully drained except the 3 deferrals + 1 hold; tomorrow's Filter C will begin pulling the early-May cohort.
