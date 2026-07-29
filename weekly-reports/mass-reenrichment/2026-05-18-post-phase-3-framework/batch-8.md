# Mass Re-Enrichment Sweep — Batch 8 Audit Log

**SWEEP_NAME:** 2026-05-18-post-phase-3-framework
**SWEEP_KICKOFF_DATE:** 2026-05-18
**BATCH:** 8
**RUN_DATE:** 2026-05-18
**BATCH_SIZE:** 50
**VERIFY_DEPTH:** leverage-and-patch
**APOLLO_ENFORCEMENT:** disabled
**SEGMENT_SCOPE:** all_active_icp

## Summary

- Records processed: 50/50
- Pool at batch start: 2,403
- Pool at batch end: 2,363
- Path mix: LIGHT 0 · MEDIUM 50 · FULL 0 · HOLD 0
- Apollo this batch: 0 credits (Apollo-free batch — sufficient existing data + 2026-01 records already had Apollo state/country populated)
- Tier writes: 0 promotions, 0 demotions, 0 skipped (hs_is_target_account)
- Sub-segment auto-migrations: 0
- Greenfield migrations: 0
- Segment changes (cascade fired): 0
- Customer-protection HOLDs: 0
- Completeness Gate fails: 0
- Manual-review HOLDs: 0
- Run health: GREEN

## Systemic patterns this batch

1. **Marketing bleed** in account_brief was UNIVERSAL on the 2026-01-17/18 colo/MSP records — every record had at least one variant of "MaiaEdge offers...", "MaiaEdge can help...", "MaiaEdge is well-positioned...", or "strong fit for MaiaEdge". Stripped on all 50.
2. **4-paragraph overlong account_brief** was systemic — tightened to 2-4 sentences on all 50.
3. **Stale recent_news_or_trigger_event** on majority of records — cleared (per §7.4 ≥90d rule with no Signal Scan write in last 7d).
4. **fabric_provisioning_approach missing** on ~8 records — set to "manuallegacy_processes" where brief indicated no NaaS, set to specific combos where Megaport/Console Connect/PacketFabric mentioned.
5. **No em dashes** detected in provisioning_landscape this batch (good).
6. **No tier changes needed** — all records already at correct default tier with no signal modifiers active.

## Notable records flagged for follow-up

### R3 Dedup candidates (canvas F0B0AFSB9LN append)
- **ColoHouse (254570392308)** — rebranded to Hivelocity 2025-02; legacy record exists alongside active Hivelocity record (254575820474)
- **Hivelocity (254575820474)** — new combined entity post-ColoHouse merger; dedup vs legacy ColoHouse
- **TelJet (264450748139)** — acquired by Tech Valley Communications 2013 (now FirstLight Fiber); brand defunct; consolidation candidate
- **The Nexus Group / Scipio Technologies (264414880443)** — rename HubSpot record name "The Nexus Group" → "Scipio Technologies"
- **Sungard Availability Services (264413011662)** — wind-down post-2022 Ch.11; divisions sold to 11:11 Systems and others; deletion candidate
- **Westelcom Networks (264260027125)** — acquired by SLIC Network Solutions 2025-05
- **US Internet (254570392307)** — acquired by T-Mobile 2025-09-02
- **RagingWire Data Centers (254574022375)** — now operates as NTT Global Data Centers Americas
- **Secured Network Services (264635347667)** — acquired by Thrive 2025-02-13
- **Steadfast Networks (264355635947)** — acquired by ColoHouse 2021-12, now part of Hivelocity portfolio

### D7 Review candidates
- **Psychz Networks (264413011659)** — infrastructure_profile Facilities: Enterprise (50+) inconsistent with 30-employee headcount; likely PoPs at partner colos misclassified as owned facilities
- **Teraswitch (264241842934)** — Regional CLEC label arguable; bare-metal hosting + global wholesale connectivity hybrid model
- **Provision Data Services (264241842933)** — Vancouver BC HQ but Dallas geographic_focus; likely partner-colo reseller rather than actual colo operator; downgraded segmentation_confidence to low_5069

## Per-record outcomes

### Chunk 1 (10 records)
1. **Psychz Networks (264413011659)** — MEDIUM — brief regen, fabric_provisioning_approach set to "megaport;homegrownproprietary_platform", cleared stale news (2025-04-21). Flagged for D7 (infra/headcount mismatch).
2. **XMission (254951523061)** — MEDIUM — brief regen, cleared stale news (2024-05-30).
3. **RochesterColo (264592334575)** — MEDIUM — brief regen, fabric_provisioning_approach set to "manuallegacy_processes", cleared stale relaunch news.
4. **PCI Broadband (263729676024)** — MEDIUM — brief regen, fabric_provisioning_approach set to "manuallegacy_processes", cleared stale news (2026-01-08).
5. **Voonami (264432390893)** — MEDIUM — brief regen.
6. **SYPTEC (254572221116)** — MEDIUM — brief regen.
7. **New York Internet / NYI (264594125515)** — MEDIUM — brief regen, cleared stale Megaport 10yr news.
8. **SBA Edge (264590543562)** — MEDIUM — brief regen, fabric_provisioning_approach set to "manuallegacy_processes", cleared stale Millicom news.
9. **One Data Center America (264588752577)** — MEDIUM — brief regen.
10. **zColo (264588752576)** — MEDIUM — brief regen, fabric_provisioning_approach set to "megaport;console_connect;homegrownproprietary_platform".

### Chunk 2 (10 records)
11. **Performive (254951523063)** — MEDIUM — brief regen, cleared stale Renovus/CloudFirst news.
12. **Provdotnet (254951524032)** — MEDIUM — brief tightening (4 paragraphs → 4 sentences), cleared stale CloudSigma news.
13. **Navegalo (255118549739)** — MEDIUM — brief regen, cleared stale Bogota news.
14. **Vaultas (254554504938)** — MEDIUM — brief tightening.
15. **Colocation America (254538313410)** — MEDIUM — brief regen, cleared stale CEO appointment news.
16. **Roller Network (254561398509)** — MEDIUM — brief regen, cleared stale 2FA news.
17. **ColoHouse (254570392308)** — MEDIUM — brief notes Hivelocity rebrand (2025-02), flagged for R3 dedup.
18. **Skybox Datacenters (254566823652)** — MEDIUM — brief regen, cleared stale Prologis/HMC news.
19. **ColoCrossing (254566823655)** — MEDIUM — brief expansion, cleared mixed-date news.
20. **TelJet (264450748139)** — MEDIUM — brief regen with defunct/integrated context (2013 acquisition by Tech Valley → FirstLight Fiber). Flagged for R3 dedup; segment unchanged (no closed-won check this batch).

### Chunk 3 (10 records)
21. **EdgeCore Digital Infrastructure (264588752578)** — MEDIUM — brief regen, $235M debt financing context preserved, cleared news field.
22. **Prime Data Centers (254541933251)** — MEDIUM — brief regen, **infrastructure_profile corrected** Mid-Size (5-19) → Large (20-49) (22 facilities), cleared stale ENERGY STAR news.
23. **The Nexus Group / Scipio Technologies (264414880443)** — MEDIUM — brief regen noting Scipio rename, flagged for R3/R6 name reconciliation.
24. **Sungard Availability Services (264413011662)** — MEDIUM — brief regen with wind-down context, flagged for R3/R4 deletion review.
25. **TenHats (264254416574)** — MEDIUM — brief regen, cleared stale survey news.
26. **Westelcom Networks (264260027125)** — MEDIUM — brief regen, SLIC acquisition context, flagged for R3 dedup.
27. **Teraswitch (264241842934)** — MEDIUM — brief regen, classification flagged for D7 review.
28. **NETdepot (264450748135)** — MEDIUM — brief regen, cleared stale VMware→VergeIO news.
29. **Stafford Associates (264450748136)** — MEDIUM — brief regen.
30. **MOD Mission Critical (266112191164)** — MEDIUM — brief regen, cleared stale 365 Data Centers news.

### Chunk 4 (10 records)
31. **Rowan Data Centers (264450748137)** — MEDIUM — brief regen, Project Temple 300MW context preserved.
32. **Priseda (264270693063)** — MEDIUM — brief regen, $29M Prosperity Drive acquisition context preserved.
33. **Natcoweb (263560994529)** — MEDIUM — brief tightening (4 paragraphs → 3 sentences).
34. **RagingWire Data Centers (254574022375)** — MEDIUM — brief regen with NTT Global Data Centers Americas naming, flagged for R3 dedup vs NTT parent.
35. **US Internet (254570392307)** — MEDIUM — brief regen with T-Mobile 2025-09-02 acquisition, flagged for R3 dedup vs T-Mobile.
36. **Hivelocity (254575820474)** — MEDIUM — brief regen with ColoHouse merger + Digital Realty deal context, flagged for R3 dedup vs ColoHouse legacy record.
37. **Unisecure (264594125516)** — MEDIUM — brief tightening (4 paragraphs → 3 sentences).
38. **Racksquared (254566823650)** — MEDIUM — brief expansion, cleared stale Louisville news.
39. **Element Critical (264450748122)** — MEDIUM — brief tightening with consolidated activity timeline.
40. **Sentinel Data Centers (264254416578)** — MEDIUM — brief tightening with $3B development pipeline context.

### Chunk 5 (10 records)
41. **CentriLogic (264594125509)** — MEDIUM — brief regen, cleared stale CrewAI partnership news.
42. **Xecunet (264594125523)** — MEDIUM — brief regen.
43. **TeleSource Communications (264635347665)** — MEDIUM — brief tightening (4 paragraphs → 3 sentences).
44. **WorldSpice Technologies (264601326329)** — MEDIUM — brief regen.
45. **Solutrix (264635347671)** — MEDIUM — brief regen.
46. **Netrepid (264601327292)** — MEDIUM — brief regen with Alerify data center sale context, cleared stale news.
47. **Secured Network Services / SNS (264635347667)** — MEDIUM — brief regen with Thrive acquisition (2025-02-13), flagged for R3 dedup.
48. **Provision Data Services (264241842933)** — MEDIUM — brief regen noting Vancouver-vs-Dallas geographic inconsistency, **segmentation_confidence downgraded to low_5069**, flagged for D7 review.
49. **Steadfast Networks (264355635947)** — MEDIUM — brief regen noting ColoHouse 2021-12 acquisition → Hivelocity 2025-02 rebrand, flagged for R3 dedup vs Hivelocity record.
50. **Springs Hosting (264432390884)** — MEDIUM — brief regen with SOC 2 2025 context, cleared stale news.

## Drain status

- Sweep cumulative processed: ~368 records (50 this batch + ~318 prior batches)
- Total pool remaining: 2,363
- Estimated total pool size at kickoff: ~2,731 (368 done + 2,363 remaining)
- Drain ETA: ~47 more batches at BATCH_SIZE=50

## Apollo budget

- This batch: 0 credits consumed
- Sweep cumulative: 0 credits (Apollo not yet needed - sweep operates in leverage-and-patch mode, refreshing existing 2026-01 enrichment data rather than re-running Apollo)
