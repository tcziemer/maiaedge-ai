# Mass Re-Enrichment Sweep — Batch 4

**Sweep:** `2026-05-18-post-phase-3-framework`
**Batch:** 4
**Date:** 2026-05-18
**Operator:** Cowork CRM Guardian
**Records processed:** 50 / 50
**Pool drain:** 2,605 → 2,555 (-50 records, -1.92% of pool)
**Path mix:** LIGHT 7 · MEDIUM 35 · FULL 8 · HOLD 0
**Apollo this batch:** 0 credits (no Apollo enrich calls; existing Apollo data <180 days for all records)
**Sweep cumulative Apollo:** 0 credits (APOLLO_ENFORCEMENT=disabled)
**Tier writes:** 0 promotions · 0 demotions · 1 skipped (hs_is_target_account=true: Nexus Data Centers)
**Sub-segment auto-migrations:** 0 (no legacy 1-to-1 mapping triggers in this batch)
**Sub-segment reclassifications:** 2 (Zenlayer Fiber→MSP Cloud+Telecom Hybrid; Blueprint Projects Standard→Greenfield)
**Segment changes (cascade):** 1 (Zenlayer: Fiber Operator → MSP/Aggregator)
**Customer-protection HOLDs:** 0
**Completeness Gate fails:** 0
**Manual-review HOLDs:** 0 (HOLD policy = NONE per sweep operating notes)
**Records flagged for deletion this batch:** 7

---

## Records flagged for deletion

| ID | Name | Reason |
|---|---|---|
| 255118549732 | Yrix | No substantive web presence at yrix.org. Prior recent_news referenced Yondr Group Johor sale (different company). |
| 254627886801 | LightSpeed Technologies | Self-described "fixed wireless and network services provider", 5 emp Canton OH. WISP retail = D1 disqualifier vs Fiber Operator ICP. |
| 254561398510 | OneSource Cloud Corporation | OUTSOURCING_OFFSHORING industry, 10,001 emp, TEM (telecom expense management) company. Not a colo operator. |
| 264590543557 | Cavalier Telephone | Defunct CLEC absorbed into Windstream (via Talk America 2007, PaeTec 2010, Windstream 2011). country=Netherlands and industry=LOGISTICS wrong. |
| 254574022376 | Data-Tech | Generic Tampa SMB IT MSP. No network aggregation evidence. Pure managed IT/cloud/security. |
| 263729676986 | vXchnge | Divested colo portfolio to H5 (7 facilities, 2022) and Cologix (Santa Clara, Minneapolis). Effectively wound down as colo operator. |
| (carryover from prior batches) | — | Sweep cumulative flagged-for-deletion will be totaled at sweep close. |

---

## Sub-segment / segment changes

| ID | Name | Change |
|---|---|---|
| 254561398515 | Blueprint Projects | Standard - colo → Greenfield (Compass Datacenters division building Georgetown DC $160M / 25 MW; Phase 1 Q4 2026). Country Australia→US, state NSW→Texas, owner Tim Z→Tim Lieto. |
| 255207759567 | Zenlayer | customer_segment Fiber Operator → MSP/Aggregator; sub-segment Regional CLEC - Fiber operator → Cloud + Telecom Hybrid MSP - MSP. Global edge cloud / NaaS-adjacent with 290+ PoPs across 70+ countries, bare metal + SD-WAN + CDN + edge compute. |

---

## Data quality bugs surfaced + patched

| ID | Name | Bug | Fix |
|---|---|---|---|
| 254627886803 | Krypt | recent_news_or_trigger_event referenced "Evocative" partnership with Megaport (wrong company) | Cleared. |
| 254951524028 | Peace Communications | recent_news referenced "Scipio Technologies" MSP 501 ranking (wrong company) | Cleared and replaced with framework-consistent brief. |
| 317145733819 | Nexus Data Centers | annualrevenue = $97,400,737,900 ($97.4B) — clearly bogus for a 300-emp Greenfield colo | Cleared (Apollo to refresh later). |
| 254574022373 | Cyxtera Technologies / Centersquare | infrastructure_profile = Facilities: Large (20-49) but brief documents 80 facilities | Corrected to Facilities: Enterprise (50+). |
| 254570392305 | HorizonIQ | infrastructure_profile = Facilities: Small (<5) but they operate 9 global Tier III DCs; account_brief contained "IaaS" descriptor (violates "Carrier infrastructure" rule) | Corrected to Facilities: Mid-Size (5-19); brief rewritten without "IaaS". |
| 264035618531 | DÄSTOR | infrastructure_profile = Facilities: Small (<5) but brief documents 5 facilities | Corrected to Facilities: Mid-Size (5-19). |
| 254572221119 | Smart City | state=Nevada but HQ=Lake Buena Vista FL | Corrected to Florida. |
| 254561398515 | Blueprint Projects | country=Australia state=NSW but operations Texas (Georgetown DC + Taylor DC) | Corrected to US / Texas; owner Tim Lieto. |
| 254558124746 | On-Ramp Indiana | provisioning_landscape text was truncated mid-sentence ("Furthermore...") | Rewrote without em dashes and complete sentences. |

---

## Duplicate flagged (for R3 Duplicate Accounts to merge)

| Primary | Duplicate | Notes |
|---|---|---|
| 254574022373 Cyxtera Technologies | 254572220151 Evoque Data Centers | Both now operate as Centersquare under Brookfield ownership (combined April 2024, $1B expansion Oct 2025, 80 facilities). Both records updated to reference each other and the unified Centersquare brand pending R3 merge. |

---

## Em dash fixes (CLAUDE.md inviolable rule — "no em dashes in customer-facing fields")

`provisioning_landscape` rewritten on 23 records this batch. `account_brief` rewritten on multiple records where em dashes were embedded or sentence count exceeded the 2-4 conciseness cap.

---

## Per-record audit

### Chunk 1 (10 records, all date 2026-01-10)

| ID | Name | Path | Segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|
| 254572220153 | OpenColo | LIGHT | unchanged | unchanged | no | Cleared stale recent_news (Arelion PoP Oct 2025); date bump. |
| 254565004007 | Metanet Hosting | LIGHT | unchanged | unchanged | no | Cleared stale recent_news (60 Hudson facility Feb 2025); date bump. |
| 254570392303 | Silicon Valley Colocation | MEDIUM | unchanged | unchanged | no | account_brief + provisioning_landscape rewritten without em dashes. |
| 266047383268 | CityNAP | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten without em dash; stale news cleared. |
| 254538313412 | Lobo Internet Services | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten without em dash. |
| 254570392309 | WANSecurity | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten without em dash. |
| 254561398514 | UnitedLayer | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten; stale recent_news cleared. |
| 254558124753 | NetcroHosting | LIGHT | unchanged | unchanged | no | Cleared stale recent_news; date bump. |
| 254575820476 | Russellville Electric Plant Board | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten without em dash; stale news cleared. |
| 254574022369 | X2nsat | MEDIUM | unchanged | unchanged | no | provisioning_landscape rewritten without em dash; stale news cleared. |

### Chunk 2 (10 records)

| ID | Name | Path | Segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|
| 300402132689 | Hostway | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed. |
| 254561398515 | Blueprint Projects | FULL | sub-seg Standard→Greenfield | unchanged | no | Country/state correction Australia/NSW → US/TX; owner Tim Z→Tim Lieto; brief regenerated for greenfield context; news refreshed (Compass Datacenters division, Phase 1 Q4 2026). |
| 254627886803 | Krypt | MEDIUM | unchanged | unchanged | no | Cleared data-quality bug in recent_news (referenced Evocative); em dashes fixed. |
| 254570392305 | HorizonIQ | MEDIUM | unchanged | unchanged | no | infrastructure_profile corrected Small→Mid-Size; brief regenerated without "IaaS" descriptor; news refreshed. |
| 254574022371 | Host Color | LIGHT | unchanged | unchanged | no | Cleared stale recent_news. |
| 254572220147 | SecureNet | MEDIUM | unchanged | unchanged | no | brief tightened to 4 sentences; stale news cleared. |
| 303849415377 | Xfernet | MEDIUM | unchanged | unchanged | no | brief + provisioning_landscape rewritten without em dashes. |
| 264035617494 | Datacate | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed. |
| 255118549732 | Yrix | FULL | → Flagged for deletion | n/a | no | No web presence verified; prior data referenced Yondr Group's Johor sale (different company). |
| 254558124748 | Lincoln Rackhouse | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed; stale news cleared. |

### Chunk 3 (10 records)

| ID | Name | Path | Segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|
| 254626062060 | Synergy Broadband | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed. |
| 254627886801 | LightSpeed Technologies | FULL | → Flagged for deletion | n/a | no | Self-described WISP, 5 emp Canton OH; D1 disqualifier. |
| 254951524028 | Peace Communications | MEDIUM | unchanged | unchanged | no | Cleared data-quality bug (Scipio Tech news); brief + provisioning_landscape rewritten. |
| 255207759567 | Zenlayer | FULL | Fiber Operator → MSP/Aggregator; sub-seg Regional CLEC → Cloud + Telecom Hybrid MSP - MSP | unchanged (tier_3) | no | Reclassified per global edge cloud / 290+ PoPs / bare metal + SD-WAN profile. |
| 300469447414 | Evocative | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed; stale HorizonIQ news cleared. |
| 254538313408 | OSO Grande Technologies | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed; stale news cleared. |
| 254566823653 | LightWave Networks | MEDIUM | unchanged | unchanged | no | brief + provisioning_landscape rewritten without em dashes. |
| 254541933254 | Lake Region Technology & Communications | MEDIUM | unchanged | unchanged | no | brief tightened; stale news cleared. |
| 254627886799 | Senawave | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed; brief tightened; stale news cleared. |
| 255207759562 | Hawaii Pacific Teleport | MEDIUM | unchanged | unchanged | no | provisioning_landscape em dash fixed; brief tightened; stale news cleared. |

### Chunk 4 (10 records)

| ID | Name | Path | Segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|
| 254561398510 | OneSource Cloud Corporation | FULL | → Flagged for deletion | n/a | no | TEM (telecom expense management) company, 10,001 emp BPO profile. Not a colo. |
| 255118549738 | Implex | LIGHT | unchanged | unchanged | no | brief expanded slightly for clarity; date bump. |
| 254572221119 | Smart City | MEDIUM | unchanged | unchanged | no | state Nevada → Florida; brief tightened; stale news cleared. |
| 254547320542 | Fireline Broadband | LIGHT | unchanged | unchanged | no | brief tightened to 3 sentences; date bump. |
| 254572220151 | Evoque Data Centers | MEDIUM | unchanged | unchanged | no | Brief notes duplicate with Cyxtera (now Centersquare); news refreshed; flagged for R3 merge. |
| 254558124746 | On-Ramp Indiana | MEDIUM | unchanged | unchanged | no | Completed truncated provisioning_landscape; brief tightened. |
| 317145733819 | Nexus Data Centers | MEDIUM | unchanged | tier_1 SKIPPED (hs_is_target_account=true) | no | Cleared bogus $97.4B annualrevenue; news refreshed (612 MW Hubbard AI campus); em dashes fixed. |
| 317201515200 | HudsonIX | MEDIUM | unchanged | unchanged | no | brief tightened to 3 sentences; news refreshed (60 Hudson 2 MW high-density AI hall). |
| 254574022373 | Cyxtera Technologies | MEDIUM | unchanged | unchanged | no | infrastructure_profile Large→Enterprise; brief rewritten as Centersquare (post-Brookfield); news refreshed ($1B expansion to 80 facilities); duplicate-flag with Evoque. |
| 322837059315 | Long Lines | LIGHT | unchanged | unchanged | no | brief tightened; recent_news kept (Fiber Connect 2026 attendance is fresh). |

### Chunk 5 (10 records)

| ID | Name | Path | Segment (old → new) | Tier (old → new) | Apollo | Notes |
|---|---|---|---|---|---|---|
| 264590543557 | Cavalier Telephone | FULL | → Flagged for deletion | n/a | no | Defunct CLEC, absorbed into Windstream. |
| 254574022376 | Data-Tech | FULL | → Flagged for deletion | n/a | no | Generic SMB IT MSP, no network aggregation evidence. |
| 254574022377 | Colo Solutions | MEDIUM | unchanged | unchanged | no | brief tightened from 4 paragraphs to 3 sentences. |
| 263729676986 | vXchnge | FULL | → Flagged for deletion | n/a | no | Divested colo portfolio to H5/Cologix; operationally wound down. |
| 264432390886 | Awecomm Technologies | MEDIUM | unchanged | unchanged | no | brief tightened; stale news cleared. |
| 264432390891 | Technology Solutions of SC | MEDIUM | unchanged | unchanged | no | brief tightened to 3 sentences. |
| 254626062053 | TelNet Worldwide | MEDIUM | unchanged | unchanged | no | news refreshed (IPFone acquisition March 2025 context); brief expanded. |
| 264450748127 | 24Shells | LIGHT | unchanged | unchanged | no | Stale $250K debt funding news cleared; brief expanded. |
| 264414880447 | ACD.net | LIGHT | unchanged | unchanged | no | Stale 2024 fiber expansion news cleared; brief tightened. |
| 264035618531 | DÄSTOR | MEDIUM | unchanged | unchanged | no | infrastructure_profile Small→Mid-Size (corrects 5-facility footprint); news cleared; brief tightened. |

---

## Sweep cumulative status (post batch 4)

| Metric | Value |
|---|---|
| Total batches fired | 4 |
| Total records processed | 160 |
| Total flagged for deletion | (sweep cumulative TBD - this batch contributed 7) |
| Pool starting size | 2,715 |
| Pool current size | 2,555 |
| Pool drain | -160 records (-5.9%) |
| Apollo cumulative | 0 credits (APOLLO_ENFORCEMENT=disabled, no enrich calls fired) |
| ETA to sweep complete | ~51 more batches at BATCH_SIZE=50 |

## Run health: GREEN

No errors, no rate limits, no concurrent-batch detection, no Completeness Gate fails.

## Notable patterns to watch in subsequent batches

1. **Em dashes in `provisioning_landscape`** are systemic - the prior enrichment pass templated language with em dashes throughout. Expect ~70-80% of records this sweep to need provisioning_landscape rewrites.
2. **Stale `recent_news_or_trigger_event`** (>90 days old, no date prefix) on virtually every 2026-01-10-enriched record. Bulk clearing or refreshing depending on materiality.
3. **Data-quality bugs in `recent_news_or_trigger_event`** referencing wrong companies (Krypt→Evocative, Peace Communications→Scipio, Evoque→HorizonIQ acquisition) suggest the prior enrichment pass had cross-record contamination. Worth a separate audit.
4. **Defunct or absorbed entities** that should have been flagged earlier (Cavalier Telephone absorbed into Windstream, vXchnge divested, OneSource is TEM not colo) - aggressive flag policy is catching these.
5. **infrastructure_profile inconsistencies** with account_brief stated facility counts (HorizonIQ, Cyxtera, DÄSTOR) - prior enrichment may have used Apollo headcount as a proxy for facility count rather than reading the brief.
6. **Cyxtera ↔ Evoque duplicate** for the merged Centersquare entity - R3 should pick this up.
7. **Country/state misclassification** (Blueprint Projects US labeled Australia/NSW; Smart City Lake Buena Vista FL labeled Nevada; Yrix US/Montana but Amsterdam HQ described) - likely Apollo defaulting to closest match when the canonical record didn't resolve.

---

**End of batch 4 audit log.**
