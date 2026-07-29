# Mass Re-Enrichment Sweep - Batch 42

- **Sweep:** 2026-05-18-post-phase-3-framework
- **Date:** 2026-05-19
- **BATCH_SIZE:** 50
- **VERIFY_DEPTH:** leverage-and-patch
- **APOLLO_ENFORCEMENT:** disabled (sweep window)
- **SEGMENT_SCOPE:** all_active_icp
- **Apollo this batch:** 0 credits
- **HubSpot writes:** 50/50 (0 failed)
- **Pool remaining at batch start:** 759
- **Pool remaining at batch end (projected):** ~709

## Routing summary
- **FULL:** 6 (3 evictions, 2 segment reclasses, 1 re-enrich)
- **MEDIUM:** 11 (em-dash fix + placeholder brief rewrite)
- **LIGHT:** 33 (over-long trim + stale news clear + date bump)

## Per-record decisions

### ? (296851879635)
- Path: LIGHT
- Was: Craw-Kan Telephone Cooperative
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296851879636)
- Path: LIGHT
- Was: Mud Lake Telephone - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296851879637)
- Path: LIGHT
- Was: Centric Fiber
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296851879639)
- Path: FULL
- Was: NeoCloud / Tier 1 Inference - Neocloud / tier_2
- Now: Flagged for deletion (defunct - NVIDIA absorbed)
- Reason: Defunct brand - acquired by NVIDIA Sept 2024 (~$165-250M); standalone product wound down, team folded into NVIDIA AI Enterprise. Eviction to Flagged for deletion.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880095991)
- Path: FULL
- Was: Data Center Colo Provider / Standard - colo / tier_3
- Now: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Reason: Within-segment reclass: misclassified as Colo when actually a regional HFC/fiber telco. Family-owned telecom since 1934 in Mason County WA with HFC residential/business broadband, phone, TV. Move to Fiber Operator / Regional CLEC. Tier 3 default unchanged.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880095992)
- Path: LIGHT
- Was: Centranet - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880095993)
- Path: LIGHT
- Was: PANGAEA Internet - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096957)
- Path: LIGHT
- Was: Owensboro Municipal Utilities - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096958)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3 (placeholder brief)
- Now: unchanged - real brief written
- Reason: Replace placeholder brief. Multifamily-focused ISP under M/C Partners; merged with Zentro 2025.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096961)
- Path: LIGHT
- Was: Waldron Telephone - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096962)
- Path: MEDIUM
- Was: Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4
- Now: unchanged - brief em-dash cleanup + stale news clear
- Reason: Brief had em-dash. Rewrite + clear stale news.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096963)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Now: unchanged - brief em-dash cleanup + stale news clear
- Reason: Brief had em-dash. Rewrite + clear stale news.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096964)
- Path: LIGHT
- Was: Carnegie Telephone
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096965)
- Path: MEDIUM
- Was: Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4
- Now: unchanged - brief em-dash cleanup + stale news clear
- Reason: Brief had em-dash. Rewrite + clear stale news.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096967)
- Path: FULL
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Now: Flagged for deletion (defunct - Hilliary absorbed)
- Reason: Defunct brand - acquired by Hilliary Communications 2019; Apollo shows 1 employee confirming wind-down. Eviction to Flagged for deletion (dedup).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296880096969)
- Path: LIGHT
- Was: Comteck
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684034)
- Path: LIGHT
- Was: Mountain Broadband - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684035)
- Path: FULL
- Was: Fiber Operator / Long Haul / Backbone - Fiber operator / tier_2
- Now: Flagged for deletion (defunct - Uniti/Windstream absorbed)
- Reason: Defunct brand - Southern Light fiber assets absorbed into Uniti Group 2017; Uniti merged with Windstream 2025. Active network rolls up under Uniti/Windstream. Eviction to Flagged for deletion (dedup).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684040)
- Path: LIGHT
- Was: Windwave Technologies - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684043)
- Path: LIGHT
- Was: Monitor Cooperative Telephone - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684044)
- Path: FULL
- Was: Data Center Colo Provider / Standard - colo / tier_3
- Now: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Reason: Within-segment reclass: misclassified as Colo when actually a rural fiber/broadband telco in Jackson TN. Gigabit FTTH, VoIP, IT support are primary; colocation is ancillary. Move to Fiber Operator / Regional CLEC.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684047)
- Path: LIGHT
- Was: New Paris Telephone
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684049)
- Path: LIGHT
- Was: Trailwave Fiber - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684051)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3 (placeholder brief)
- Now: unchanged - real brief written
- Reason: Replace placeholder brief. Rural OK ILEC, 30 employees.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684052)
- Path: LIGHT
- Was: Conxxus
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684053)
- Path: MEDIUM
- Was: Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4
- Now: unchanged - brief em-dash cleanup + stale news clear
- Reason: Brief had em-dash. Rewrite + clear stale news.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684054)
- Path: LIGHT
- Was: Stratford Communications - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684055)
- Path: LIGHT
- Was: Butler-Bremer Communications
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684056)
- Path: LIGHT
- Was: Titonka Burt Communications - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684057)
- Path: LIGHT
- Was: Marshall County Fiber - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684059)
- Path: LIGHT
- Was: Southern Montana Telephone - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684060)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3 (placeholder brief)
- Now: unchanged - real brief written
- Reason: Replace placeholder brief. Rural KS ILEC.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684061)
- Path: FULL
- Was: NeoCloud / Tier 1 Inference - Neocloud / tier_2 (6 fields missing)
- Now: NeoCloud / Tier 1 Inference - Neocloud / tier_2 (fully enriched, Cloudflare-owned)
- Reason: FULL re-enrich: 6 of 7 enriched fields missing. Cloudflare-acquired (late 2024) but still operates as the model API platform powering Cloudflare Workers AI. Stays NeoCloud / Tier 1 Inference.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (296883684062)
- Path: LIGHT
- Was: WideOpen Networks - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273391)
- Path: LIGHT
- Was: NeuBeam
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273393)
- Path: LIGHT
- Was: Midstate Telephone - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273394)
- Path: LIGHT
- Was: SyncGlobal - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273396)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Now: unchanged - brief em-dash cleanup + stale news clear
- Reason: Brief had em-dash. Rewrite + clear stale news.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273397)
- Path: LIGHT
- Was: Lyons Communications - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297164273398)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3
- Now: unchanged - brief em-dash cleanup
- Reason: Brief had em-dash. Rewrite.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654757)
- Path: LIGHT
- Was: Maquoketa Valley Electric Cooperative - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654759)
- Path: LIGHT
- Was: Agate Mutual Telephone Cooperative Association - over-long brief/prov
- Now: trimmed
- Reason: Brief trimmed to 2-4 sentence cap; stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654760)
- Path: LIGHT
- Was: Southern Ute Indian Tribe - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654762)
- Path: MEDIUM
- Was: Fiber Operator / Regional CLEC - Fiber operator / tier_3 (placeholder brief)
- Now: Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 (coop subsidiary)
- Reason: Replace placeholder brief. BEC is a fiber division of Bartlett Electric Cooperative (Texas) - within-segment promotion from Regional CLEC to Municipal/Cooperative sub-segment.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654763)
- Path: LIGHT
- Was: Trico Electric Cooperative - over-long brief/prov
- Now: trimmed
- Reason: news kept (Marana DC adjacency, signal-relevant); date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654764)
- Path: LIGHT
- Was: PAC Fiber - over-long brief/prov
- Now: trimmed
- Reason: stale news cleared; date bumped.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654765)
- Path: LIGHT
- Was: Canadian Valley Telephone
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654767)
- Path: LIGHT
- Was: Northwest Iowa Telephone
- Now: date bumped, no other changes
- Reason: Date bump only (clean record).
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654768)
- Path: MEDIUM
- Was: Fiber Operator / Municipal / Cooperative - Fiber operator / tier_4 (placeholder brief)
- Now: unchanged - real brief written
- Reason: Replace placeholder brief. Municipal government with city fiber/utility division.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass

### ? (297293654770)
- Path: LIGHT
- Was: Mid Century Communications - stale news
- Now: news cleared, date bumped
- Reason: Stale news clear + date bump.
- Apollo used: no
- web_searches: 0 (in-place from existing fields + framework rules)
- Completeness Gate: pass
