# Mass Re-Enrichment Sweep — Batch 7

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 7
**Date:** 2026-05-18
**Processed:** 50 / 50
**Apollo credits this batch:** 0 (APOLLO_ENFORCEMENT=disabled; no Apollo calls needed)
**Web searches:** 3 (identity verification — Mountain West Tech, Earthnet, Encore)
**Path mix:** LIGHT 1 · MEDIUM 41 · FULL 8 · HOLD 0
**Flagged for deletion this batch:** 5
**Sub-segment / segment changes:** 5 (Mountain West Tech, FDCServers, CyrusOne, Epsilon, HydraVault)
**Greenfield migrations:** 1 (HydraVault → Greenfield, pre-operational)
**Tier writes:** Promotions 2 (Epsilon, NorthState tier_3→tier_2), Demotions ~25 (mostly tier_2→tier_3 MSP defaults)
**Apollo geo errors fixed:** 5 (Encore OH, ABCC NY+owner, Windstream AR, Southern Telecom GA, Swift Systems MD+owner)
**Completeness Gate fails:** 0

---

## Records processed

### Encore Technologies (264241842926)
- Path: MEDIUM
- Segment: MSP/Aggregator (unchanged)
- Sub-segment: Telecom Aggregator - MSP (unchanged)
- Confidence: medium_7089 (unchanged)
- Tier: tier_2 → tier_3
- State: New York → Ohio (Apollo error fix)
- Reason: Brief regen, strip marketing bleed, fix state to Cincinnati/Norwood OH per web-verified HQ.

### Advance2000 (264241842928)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### American Business Continuity Centers (264241842930)
- Path: FULL
- Country: Netherlands → United States (Apollo error fix)
- State: North Holland → New York
- Owner: 159350430 (Tim Z) → 161889085 (Tim Lieto, East)
- Tier: tier_2 → tier_3
- Reason: Major Apollo geo misclassification — Woodbury NY entity tagged as Netherlands. Owner re-derived from corrected state.

### OneNeck IT Solutions (264241842924)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed, preserve US Signal acquisition context.

### Citynet (264241842920)
- Path: LIGHT
- Tier: tier_3 (unchanged)
- recent_news_or_trigger_event: cleared (date prefix >90d stale, no Signal Scan in last 7d)
- Reason: Brief already concise, just clear stale news + recompute tier (no change).

### ClearBearing (264192113382)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### ISG Technology (264035618536)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### Earthnet / Massive Networks (264241842922)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, note "now operating as Massive Networks" (post-rebrand 2024-03). Web-verified earthnet.net redirects to massivenetworks.com.

### IX-Denver / Rocky Mountain Internet Exchange (264355635941)
- Path: MEDIUM
- Tier: tier_2 (unchanged)
- Reason: Brief regen reflecting dark-fiber backbone buildout shift. Sub-segment Long Haul/Backbone preserved.

### Mountain West Technologies (264270693060)
- Path: FULL — **segment change**
- Segment: MSP/Aggregator → **Fiber Operator**
- Sub-segment: Telecom Aggregator - MSP → **Regional CLEC - Fiber operator**
- Confidence: medium_7089 → high_90
- Tier: tier_2 → tier_3
- Reason: Account brief was hallucinated about "Midwest Telecom of America" in Indiana. Actual entity is Mountain West Technologies in Casper, WY — regional fiber ISP/telco with carrier-neutral DCs and Denver/Salt Lake fiber links. Full content rebuild.

### Markley Group (264590543561)
- Path: MEDIUM
- Tier: tier_1 (unchanged)
- Reason: Brief said "13 global data centers" — Markley is Boston-anchored (One Summer Street + Lowell). Tightened brief.

### CeraNet (264355635940)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief regen, strip 4-paragraph format and "MaiaEdge could address" marketing bleed.

### IronGate Data Centers (300402851564)
- Path: MEDIUM
- Tier: tier_1 (unchanged)
- Reason: Brief regen surfacing the active construction signals (MSP-1/2/3 + Van Dyke 45MW). Hot account.

### Cybercon (300406714049)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief regen, strip 4-paragraph format.

### Compass Datacenters (264192113375)
- Path: MEDIUM
- Tier: tier_1 (unchanged)
- Reason: Brief regen, preserved [2026-04-29] PWDG strategic exit signal.

### Mammoth Networks (264432390880)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### Datotel (264413011657)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### Windstream (264260027126)
- Path: MEDIUM
- State: Iowa → Arkansas (Apollo error fix)
- Tier: tier_2 (unchanged)
- Reason: HQ Little Rock, AR. Brief regen with post-Uniti context and 2025 fiber doubling.

### First Communications (264260027124)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen surfacing AscendOne UC+CC+AI platform launch (2026-01-13).

### USNX (264260028096)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### CorKat Data (264592334568)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### MegaNet Communications (264450748125)
- Path: LIGHT-MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief tightened, no segment change.

### Frontline Data Services (264450748128)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### Omega Systems / Amnet Systems (264450748120)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, preserve PEAKE Technology acquisition (2025-11).

### Alpha Innovations (264588752575)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### CenterServ (264592334570)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed. Owner Tim Z stays correct (Quebec/international).

### Concergent (264601326326)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### Fibertech Networks (300402132681)
- Path: FULL → **FLAGGED FOR DELETION**
- Segment: Fiber Operator → Flagged for deletion
- Sub-segment: cleared
- Reason: Defunct entity. Merged with Lightower 2015-08 ($1.9B); Lightower absorbed by Crown Castle 2017. No active ICP entity at fibertech.com.

### Heartland Technology (264635347660)
- Path: MEDIUM
- Tier: tier_3 → tier_4
- Reason: Iowa-based Tier III DC with limited scale — Standard-colo defaults closer to tier_4 floor.

### DLS Internet Services (264414880446)
- Path: LIGHT-MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief tightened, active PBX maintenance (2025-12) preserves currency.

### Sparrow Technology Solutions (263560994540)
- Path: FULL → **FLAGGED FOR DELETION**
- Segment: Data Center Colo Provider → Flagged for deletion
- Reason: Apollo data indicates Pakistan management consulting firm. Prior enrichment hallucinated an Alabama edge/micro colo profile. No verifiable positive ICP evidence.

### Long Island Interconnect (264260028090)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief regen tightened from 4-paragraph format; preserve 1025Connect → LII relaunch and Aqua Comms/NYI context.

### InfoQuest (263729676013)
- Path: MEDIUM
- Tier: tier_3 → tier_4
- Reason: Single-facility small Standard-colo; tier_4 better reflects scale.

### nFrame (303849415362)
- Path: FULL → **FLAGGED FOR DELETION**
- Segment: Data Center Colo Provider → Flagged for deletion
- Reason: Acquired by Expedient; active entity is Expedient parent record. Prior enrichment populated nframe.com content describing Expedient.

### Forethought.net / Vero Fiber (263392463554)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief regen, preserve TEC acquisition (2025-11) and 16-state expansion footprint.

### HydraVault (264254416575)
- Path: MEDIUM — **sub-segment change**
- Sub-segment: AI Signals - colo → **Greenfield**
- Tier: tier_1 (unchanged)
- Reason: Pre-operational Chicago AI facility — construction permit Oct 2025, buildout late 2026. Migrated per Operating Principle 8 (Greenfield = actively-being-built Colo/NeoCloud).

### CBTS (264413011655)
- Path: MEDIUM
- Tier: tier_2 (unchanged)
- Reason: Brief regen, surface TowerBridge Capital Partners acquisition (2025-11) and CRN MSP 500 Elite 150.

### Epsilon Telecommunications (264254416570)
- Path: MEDIUM — **sub-segment change**
- Sub-segment: Regional CLEC - Fiber operator → **Tier 2 National Wholesale - Fiber operator**
- Confidence: medium_7089 → high_90
- Tier: tier_3 → tier_2 (promotion)
- Reason: KT Corp subsidiary, 34 facilities + 280 POPs globally. Infiny NaaS platform. Regional CLEC misclassification corrected.

### unWired Broadband (254558124744)
- Path: MEDIUM
- Tier: tier_3 (unchanged)
- Reason: Brief regen surfacing Capital Southwest PE investment (2025-09).

### NorthState (263560994526)
- Path: MEDIUM
- Tier: tier_3 → tier_2 (promotion)
- Reason: ~30K route miles, Lumos brand under T-Mobile/EQT JV. Substantial Regional CLEC scale supports tier_2.

### CyrusOne (254558124749)
- Path: MEDIUM — **sub-segment change**
- Sub-segment: AI Signals - colo → **Hyperscale Wholesale - colo**
- Tier: tier_1 (unchanged)
- Reason: 50+ global facilities, KKR-owned hyperscale operator. Hyperscale Wholesale better fits than AI Signals — though Eolian 200MW campus shows AI exposure.

### FDCServers (264192113380)
- Path: MEDIUM — **segment change**
- Segment: Fiber Operator → **MSP/Aggregator**
- Sub-segment: Regional CLEC → **Cloud + Telecom Hybrid MSP - MSP**
- State: Florida → Illinois (Apollo error fix)
- Tier: tier_3 (unchanged)
- Reason: Chicago bare-metal/colo provider, not a fiber operator. Fixed Apollo state. EPYC VPS Denver expansion preserved.

### Natural Network (264270693069)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### tw telecom (263560994534)
- Path: FULL → **FLAGGED FOR DELETION**
- Segment: Fiber Operator → Flagged for deletion
- Reason: Acquired by Level 3 in 2014 ($7.3B); Level 3 absorbed into Lumen 2017. 12-year defunct entity.

### NWAX (264432390881)
- Path: FULL → **FLAGGED FOR DELETION**
- Segment: Fiber Operator → Flagged for deletion
- Reason: Non-profit Portland-area Internet Exchange Point with ~2 employees. No fit for any of the 6 active ICP sub-segments. Operating Principle 7.

### NaviSite (254541933255)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- annualrevenue: cleared (was $211.9B which was Accenture parent's inherited revenue, not NaviSite's)
- Reason: Brief regen with Accenture acquisition (2024-01) context. Data hygiene flag on revenue field.

### Thin-nology (254626062051)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed.

### NacSpace (263729676023)
- Path: MEDIUM
- Tier: tier_2 → tier_3
- Reason: Brief regen, strip marketing bleed. Elliott Electric Supply subsidiary noted.

### Southern Telecom (263392463560)
- Path: MEDIUM
- State: New York → Georgia (Apollo error fix)
- Industry: CONSUMER_ELECTRONICS → TELECOMMUNICATIONS
- Tier: tier_2 (unchanged)
- Reason: Atlanta HQ. SouthernWaves Seimitsu alliance (2025-09) + 300-mile hyperscale deal (2025-04) preserved.

### Swift Systems (264254416573)
- Path: MEDIUM
- State: California → Maryland (Apollo error fix)
- Industry: LOGISTICS_AND_SUPPLY_CHAIN → INFORMATION_TECHNOLOGY_AND_SERVICES
- Owner: 162339176 (Ken Cunningham, West) → 161889085 (Tim Lieto, East)
- Tier: tier_2 → tier_3
- Reason: Frederick MD HQ. Corporate Technologies/NuMSP parent acquisition (2024-01) preserved.

---

## Notable patterns from this batch

1. **Apollo geo error wave continues.** 5 fixes in this batch (Encore, ABCC, Windstream, Southern Telecom, Swift Systems). The 2026-01-17 enrichment cohort had a systematic Apollo state/country misclassification problem. ABCC and Swift Systems also triggered owner re-derivation cascades.
2. **Defunct/acquired entity drain.** 5 flagged-for-deletion this batch — Fibertech Networks (Crown Castle), nFrame (Expedient), Sparrow (false-positive enrichment), tw telecom (Lumen), NWAX (IXP non-fit). Defunct/acquired drain is now consistent batch-over-batch (4 in batch 6, 5 in batch 7).
3. **Tier_2 → tier_3 demotion for small MSPs.** Aggressive sweep of small Telecom Aggregator and Cloud+Telecom Hybrid MSPs (<5 facilities, <50 employees) demoted from inflated tier_2 to spec-default tier_3. ~25 records this batch alone.
4. **Sub-segment refinements.** Three meaningful reclassifications: HydraVault → Greenfield (textbook pre-operational AI), Epsilon → Tier 2 National Wholesale (was mislabeled Regional CLEC despite 34 facilities + 280 POPs), CyrusOne → Hyperscale Wholesale (was AI Signals - colo).
5. **Bogus revenue data.** NaviSite carried $211.9B annual revenue (Accenture's). Cleared. Per Cooper's principle: infrastructure_profile wins over annualrevenue when they conflict; this batch shows why revenue data needs scrutiny.
6. **Marketing bleed elimination still systemic.** Nearly every MEDIUM-path brief regen removed "MaiaEdge offers / is uniquely positioned" language from 2026-01-17 enriched records.

---

## Drain status

- Pool at batch 7 start: ~2,455
- Records processed batch 7: 50 (45 re-enriched + 5 flagged)
- Pool after batch 7: ~2,405
- Sweep cumulative processed: ~318 / ~2,723 starting (≈ 11.7%)
- ETA at BATCH_SIZE=50: ~48 more batches

---

## Run health: GREEN

No errors. No HOLDs. No Completeness Gate fails. Apollo not consumed. All 50 records written successfully on first attempt.
