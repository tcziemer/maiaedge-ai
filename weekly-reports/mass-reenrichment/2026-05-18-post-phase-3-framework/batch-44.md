# Mass Re-Enrichment Sweep — Batch 44

**Sweep:** 2026-05-18-post-phase-3-framework
**Run date:** 2026-05-19
**Records processed:** 50 / 50
**Path mix:** LIGHT 39 · MEDIUM 10 · FIX_NEWS 1 · FULL 0 · HOLD 0
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Pool drain:** 50 → 609 remaining (was 659 at start of batch 44)
**Trigger query:** customer_segment IN [6 ICPs], NEQ Flagged for deletion, NEQ Customer, hs_object_id NEQ 124293230301, (last_enriched_date NULL OR LT 2026-05-18); sort hs_object_id ASC; limit 50.
**HubSpot writes:** 50/50 succeeded across 5 batches of 10. 16/16 notes created across 2 batches. Zero 4xx/5xx.

## Headline patterns

- **5 within-fiber reclassifications Regional CLEC → Municipal / Cooperative** (tier_3 → tier_4): CTS Media Group (Monticello+Wayne Co KY public utility), United Telephone Association (KS member-owned co-op since 1951), Peoples Communications (Peoples Telephone Cooperative TX), BrightRidge Broadband (BrightRidge Electric subsidiary TN), Sveconnect (SVEC subsidiary TN). Same Phase 3 D5 rule pattern from batch 43 — explicit mutual / member-owned / municipal / electric-co-op-subsidiary diagnostic phrases route to Muni/Co-op.
- **5 national / multi-state operator promotions** tier_3 → tier_2: Comporium (1000 emp, $355M rev, SC), Nuvera Communications (195 emp, $71.8M rev, MN, Fiber Connect 2026), Medicine Park Telephone (acquired TDS Telecom OK ops, +35K locations), FirstDigital Telecom (Equinix ECX fabric tagged, $200M Apollo Infrastructure Funds investment), Conexon Connect (9 states, Enterprise route miles, 119 emp, Fiber Connect 2026).
- **1 ICP → ICP segment correction** (Colo → Fiber): Optico Fiber (Critical Hub Networks' PR consumer fiber ISP, symmetric multi-gig FTTH) was mis-bucketed as Data Center Colo Provider — Phase 3 segment routing puts this in Fiber Operator / Regional CLEC.
- **1 Dark Fiber Specialist → Muni/Co-op demotion**: Parallax Systems (6-emp department of Richmond Power & Light, IN municipal utility, formally merged 2021-11). Dark Fiber Specialist sub-segment at tier_2 was clearly inflated for a 6-employee muni utility department.
- **1 within-fiber demotion** Long Haul → Regional CLEC: Baca Valley Telephone (tiny rural NM ILEC, Des Moines NM, ~2,600 sq mi territory). Misclassified as Long Haul / Backbone; reclass to Regional CLEC tier_3 (within-fiber demotion).
- **1 infrastructure_profile patch + tier promotion**: Triangle Communications (MT co-op) completed 100% fiber transition Jan 2026 across 24K sq mi over 10,200 mi buried fiber + 180 mi aerial. Prior record carried "Route Miles: Small (<1K)" — patched to "Route Miles: Large (10K-50K)". Hot signal (completed milestone Jan 2026) supports tier_3 → tier_2 on Regional CLEC default.
- **1 D1 IT-services eviction**: CTI Tech (ctitech.com, 30 emp Illinois, Apollo industry "IT Services", prior segmentation_confidence low_5069 already flagged the gap). No fiber operator evidence on record. Reclass Fiber Operator → Other.
- **1 cross-account news bleed scrub**: Inter Community Telephone (ictc.com, GA) recent_news_or_trigger_event field carried BEK Communications (ND, unrelated) news. Cleared the news field; classification (Regional CLEC) preserved.

## Pattern counters (cumulative through batch 44)

| Pattern | Δ batch 44 | Cum total |
|---|---:|---:|
| National operator under-tiering | 5 (Comporium, Nuvera, Medicine Park, FirstDigital, Conexon Connect) | ~50 |
| Within-fiber promotions | 5 (all to Municipal/Cooperative) | ~49 |
| Within-fiber demotions | 2 (Baca Valley Long Haul → Regional CLEC, Parallax Dark Fiber Specialist → Muni/Co-op) | ~27 |
| Template-bleed remediation in account_brief | 0 | ~32 |
| Cross-account news bleed (separate from template-bleed) | 1 (Inter Community Telephone) | 1 (new tracker) |
| Maritime/MSP misclassified as Telecom Aggregator | 0 | 6 |
| MaiaEdge value-prop bleed | 0 | ~35 |
| CPaaS/voice aggregator misclassified as Fiber Op | 0 | 8 |
| Pure satellite operator misclassified as Fiber Op | 0 | 3 |
| Subsea cable operator promotions | 0 | 5 |
| IX/Internet Exchange policy gap | 0 | 3 |
| R&E network framework gap | 0 | 1 |
| AI Signals - colo reclassifications | 0 | 5 |
| Sanctions-driven ICP→Other reclasses | 0 | 2 |
| Crypto-to-AI Neocloud reclasses | 0 | 1 |
| Cable-manufacturer D1 evictions | 0 | 1 |
| Dedup/identity evictions | 0 | 6 |
| Defunct-brand evictions | 0 | 4 |
| Tower-co D1 evictions | 0 | 1 |
| Colo→Fiber Op within-class reclassifications | 1 (Optico Fiber) | 3 |
| Wrong-entity-at-domain D1 eviction | 0 | 1 |
| IT-services D1 eviction | 1 (CTI Tech) | 2 |
| Infrastructure profile patch (band correction) | 1 (Triangle Communications Small→Large) | 1 (new tracker) |

## Per-record audit

### Evictions / segment reclassifications (full ICP → Other or cross-segment)

#### CTI Tech (297892337348)
- Path: MEDIUM (D1 eviction)
- Domain: ctitech.com
- Segment: Fiber Operator → **Other**
- Sub-segment: Regional CLEC → (cleared)
- Confidence: low_5069 → medium_7089
- Tier: tier_3 (preserved per Step A0)
- Apollo used: no
- web_searches: 0
- Reason: 30-emp Illinois IT services firm; prior segmentation_confidence low_5069 already flagged the gap; brief explicitly flagged "fiber operator classification may need review". D1 IT-services pattern.

#### Optico Fiber (297892337338)
- Path: MEDIUM (cross-segment Colo → Fiber)
- Domain: opticofiber.com
- Segment: Data Center Colo Provider → **Fiber Operator**
- Sub-segment: Standard - colo → Regional CLEC - Fiber operator
- Confidence: medium_7089 (held)
- Tier: tier_3 (held - matches Regional CLEC default)
- Apollo used: no
- web_searches: 0
- Reason: Critical Hub Networks brand; 100% company-owned fiber-optic network across Puerto Rico; symmetric multi-gig consumer plans (2.5G / 4G). Classic consumer FTTH operator. Phase 3 segment routing puts this in Fiber Operator / Regional CLEC, not Colo.

### Sub-segment migrations (within Fiber Operator parent)

#### Parallax Systems (297877949127)
- Path: MEDIUM
- Domain: parallax.ws
- Sub-segment: Dark Fiber Specialist - Fiber Operator → **Municipal / Cooperative - Fiber operator**
- Tier: tier_2 → **tier_4**
- Reason: 6-emp department of Richmond Power & Light (IN municipal utility), formally merged 2021-11. Dark Fiber Specialist sub-segment at tier_2 was inflated for a 6-employee muni utility department. Phase 3 Muni/Co-op default = tier_4.

#### Baca Valley Telephone (297894135484)
- Path: MEDIUM
- Domain: bacavalley.com
- Sub-segment: Long Haul / Backbone - Fiber operator → **Regional CLEC - Fiber operator**
- Tier: tier_2 → **tier_3**
- Reason: Tiny rural NM ILEC headquartered in Des Moines NM, ~2,600 sq mi territory. Long Haul / Backbone sub-segment doesn't fit this scale; Regional CLEC is the correct bucket. Within-fiber demotion.

### Within-fiber Regional CLEC → Municipal / Cooperative promotions (tier_3 → tier_4)

| ID | Name | Domain | Evidence |
|---|---|---|---|
| 297892336377 | Community Telecom Services | ctsmediagroup.com | Public utility jointly owned by city of Monticello + Wayne County KY |
| 297892337339 | United Telephone Association | unitedtelcom.net | Member-owned cooperative founded 1951, Dodge City KS |
| 297894134516 | Peoples Communications | peoplescom.biz | Peoples Telephone Cooperative Inc. (member-owned, 1952, TX) |
| 297894135488 | BrightRidge Broadband | mybrightridge.com | Municipal fiber broadband subsidiary of BrightRidge Electric (TN) |
| 297906089709 | Sveconnect | sveconnect.com | Not-for-profit subsidiary of Sequachee Valley Electric Cooperative (TN) |

### Tier promotions tier_3 → tier_2 (multi-state / national-scale within Regional CLEC)

| ID | Name | Domain | Evidence |
|---|---|---|---|
| 297877949141 | Comporium | comporium.com | 1000 emp, $355M rev, Mid-Size route miles, Rock Hill SC, since 1894 |
| 297888731893 | Nuvera Communications | nuvera.net | 195 emp, $71.8M rev, Mid-Size route miles, southern MN, Fiber Connect 2026 attendee |
| 297888731897 | Medicine Park Telephone | mptelco.com | Acquired TDS Telecom Oklahoma ops 2025-07 adding 35K locations; $65.9M build |
| 297894134515 | FirstDigital Telecom | firstdigital.com | Western US carrier, Equinix ECX fabric tagged in fabric_provisioning_approach, $200M Apollo Infrastructure Funds investment, Salt Lake City UT |
| 297906089713 | Conexon Connect | conexonconnect.com | 9-state Multi-Regional footprint, 119 emp, Enterprise route miles, Fiber Connect 2026 attendee |

### Triangle Communications (297894135485)
- Path: MEDIUM
- Domain: itstriangle.com
- Sub-segment: Regional CLEC - Fiber operator (unchanged)
- Tier: tier_3 → **tier_2**
- Infrastructure profile patch: "Route Miles: Small (<1K)" → "Route Miles: Large (10K-50K)"
- Reason: MT co-op completed 100% fiber transition Jan 2026 over 10,200 mi buried fiber + 180 mi aerial across 24K sq mi service territory. Existing infra band was 3+ orders of magnitude off. Hot signal (Jan 2026 milestone) supports tier promotion on Regional CLEC default (ceiling 1, floor 4).

### Cross-account news bleed scrub

#### Inter Community Telephone (297892337347)
- Path: FIX_NEWS
- Domain: ictc.com
- Segment / sub-segment / tier: held (Fiber Operator / Regional CLEC - Fiber operator / tier_3)
- Change: `recent_news_or_trigger_event` cleared. Prior content was BEK Communications (ND) news entries — completely unrelated company.
- Reason: ICTC is in Georgia; BEK is a North Dakota fiber operator. The news field had bleed from a different account record at some prior enrichment touch. Cleared to a placeholder; no replacement web research run (LIGHT discipline).

### LIGHT verify-and-patch (33 records, last_enriched_date stamp only)

All 33 LIGHT records pass the framework consistency check from §7.4c:
- 7 enriched fields present and consistent with sub-segment defaults
- account_brief framework-consistent (no MaiaEdge value-prop bleed, no template language, no cross-account bleed)
- News field has a date prefix or `[Date needed]` token
- Sub-segment is one of the canonical 30 active values

Stamp-only writes: 297877949125 (Mutual Telephone Co KS), 297877949130 (Maverix Broadband CO), 297877949132 (Siren Telephone WI), 297877949133 (Burkes Garden Telephone VA), 297877949134 (Kitsap PUD WA), 297877949136 (Hubbard Co-op IA), 297877949142 (Solarus WI), 297877949143 (Partner Communications Co-op IA), 297888731890 (Particle Communications TX), 297888731896 (NetCarrier PA), 297888732859 (Networkmaine ME — Long Haul kept; R&E middle-mile fits), 297888732860 (Oregon-Idaho Utilities), 297888732863 (Heart of Iowa Co-op), 297892336376 (Geneseo Communications IL), 297892337342 (Mid-Plains Rural TX co-op), 297892337343 (Hanson Communications), 297892337345 (Plumas-Sierra CA), 297892337346 (Grafton Telephone IL), 297892337350 (CoastConnect MS), 297892337351 (OCG Fiber NY), 297892337352 (Fulton/Arriva MS), 297892337353 (Dakota Central ND), 297894134519 (Anza Electric Co-op CA), 297894134520 (Ayrshire Farmers Mutual IA), 297894135482 (Xtel Communications NJ — small colo+telecom hybrid; held as Standard - colo with tier_3), 297894135483 (Mercury Broadband KS+IN), 297894135486 (DELTA Fiber NL — Long Haul kept; national operator), 297894135489 (ATC Communications ID), 297894135490 (Northeast Iowa Telephone), 297894135491 (Westphalia Telephone MI), 297906089710 (Farmers Rural Connect AR), 297906089712 (WesTel Systems IA), 297906089714 (Oran Mutual IA), 297906089717 (NTCNet NY).

## Errors / blockers

None. All 50 record writes and 16 note writes returned success. Apollo credits used: 0.

## Continuation token (for next session, hands-off resume)

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=45
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING≈609
HOLD_POLICY=NONE (best-effort classify, no Tier 3 canvas)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=297906089717
```
