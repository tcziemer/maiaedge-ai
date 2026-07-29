# Mass Re-Enrichment Sweep — Batch 34
**Sweep:** 2026-05-18-post-phase-3-framework
**Date:** 2026-05-19
**Records processed:** 50/50
**Path mix:** LIGHT 41 · MEDIUM 9 · FULL 0 · HOLD 0
**Apollo this batch:** 0 credits (Apollo-free path dominant)
**Pool drain:** ~1,096 remaining post-batch (was 1,146 pre-batch)

---

## Trigger query results
- HubSpot search: customer_segment IN [6 active ICPs] AND (last_enriched_date < 2026-05-18 OR NULL) AND hs_object_id != 124293230301
- Total pool: 1,146 records
- Pagination: sort by `hs_object_id ASC` (date-sorted pagination wrapped on page 2 with 6/10 dupes; switched to id-sort for stable pagination - see Operating Notes)

---

## MEDIUM-path writes (9 records)

### Lightpath Fiber (43191653059) - DOMAIN TYPO FIX
- Path: MEDIUM
- Domain: `lighpathfiber.com` -> `lightpathfiber.com` (typo correction; entity is Altice USA's commercial fiber arm)
- Segment: Fiber Operator (unchanged)
- Sub-segment: Long Haul / Backbone - Fiber operator (unchanged)
- Tier: tier_2 (unchanged)
- Brief: regenerated with domain correction note
- Reason: Identity sanity check surfaced spelling typo on domain

### HGC Global Communications (132992626402) - SUB-SEGMENT PROMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Regional CLEC - Fiber operator` -> `Tier 2 National Wholesale - Fiber operator`
- Confidence: medium_7089 -> high_90
- Tier: tier_3 -> tier_2
- Reason: Hutchison Global Communications is international wholesale carrier with POPs Large 50-99 across APAC + Europe + NA + ME + Africa. Owns subsea cables (Asia-Pacific Cable Network). Tier 2 international wholesale scale. NATIONAL-OPERATOR UNDER-TIERING PATTERN (carry-forward).

### Cirion Technologies (133506047726) - SUB-SEGMENT PROMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Long Haul / Backbone - Fiber operator` -> `Tier 2 National Wholesale - Fiber operator`
- Tier: tier_2 (unchanged)
- Reason: LATAM Lumen successor with 65K route miles across 17 markets and 18 DCs across 20 countries. Tier 2 regional wholesale scale, not just Long Haul.

### IENTC Telecom (153481186012) - WITHIN-FIBER PROMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Regional CLEC - Fiber operator` -> `Long Haul / Backbone - Fiber operator`
- Tier: tier_3 (unchanged)
- Reason: 25K+ km of deployed fiber, "one of the highest capacity long-haul networks in Latin America" per company own description. Sole concession holder for Queretaro/Guanajuato, one of 20 nationwide PH telephone network operators.

### Astound (153994139338) - WITHIN-FIBER RECLASSIFICATION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Long Haul / Backbone - Fiber operator` -> `Regional Cable Operator - Fiber operator`
- Tier: tier_2 (unchanged)
- Reason: Astound Broadband is the 6th-largest US cable + fiber MSO (Stonepeak owned). MSO classification is the accurate sub-segment, not Long Haul/Backbone.

### Converge ICT Solutions (154117927663) - SUB-SEGMENT PROMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Regional CLEC - Fiber operator` -> `Tier 2 National Wholesale - Fiber operator`
- Tier: tier_3 -> tier_2
- Reason: Largest Philippine fiber-to-the-home operator, PSE-listed, 4,000 employees, $660M revenue, 50K+ route miles. National scale. NATIONAL-OPERATOR UNDER-TIERING PATTERN (carry-forward).

### MTA / Matanuska Telephone Association (154227754741) - WITHIN-FIBER DEMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Long Haul / Backbone - Fiber operator` -> `Municipal / Cooperative - Fiber operator`
- Tier: tier_2 -> tier_4
- Reason: Alaska's largest member-owned telecom cooperative. Coop is the accurate sub-segment; Long Haul/Backbone was misclassification. WITHIN-FIBER DEMOTION PATTERN (carry-forward, cumulative ~22).

### Flo Networks (185543487196) - SUB-SEGMENT PROMOTION + TIER PROMOTION
- Path: MEDIUM
- Segment: Fiber Operator (unchanged)
- Sub-segment: `Regional CLEC - Fiber operator` -> `Tier 2 National Wholesale - Fiber operator`
- Tier: tier_3 -> tier_2
- Reason: Cross-border US-Mexico operator (formerly Transtelco) with 30,000+ route miles unified binational fiber, 15-country reach across Americas, one of the largest IP Transit providers in Mexico. NATIONAL-OPERATOR UNDER-TIERING PATTERN (carry-forward).

### GCI Liberty (192883329741) - FLAGGED FOR DELETION (DUPLICATE)
- Path: MEDIUM
- Segment: `Fiber Operator` -> `Flagged for deletion`
- Sub-segment: unchanged (record flagged regardless)
- Tier: unchanged (irrelevant once flagged)
- Reason: GCI Liberty Inc. was a Liberty Media spinoff combined with GCI in 2018; acquired by Charter Communications via Liberty Broadband in 2020 and no longer exists as standalone entity. The standalone GCI record (hs_object_id 175217873639) is the primary. DUPLICATE-PAIR PATTERN (carry-forward) — R4 Flagged Consolidation will reassociate any salvageable contacts/deals to primary GCI before archive.

---

## LIGHT-path writes (41 records)

All 41 records had `last_enriched_date` stamped to `2026-05-19`. No property changes (framework-consistent at read time, all 7 enriched fields present and within 2-4 sentence cap, sub-segment in 30 active values, no legacy-string detection on account_brief).

### Records (id, name, current segment / sub-segment / tier, notes):

| ID | Name | Segment | Sub-segment | Tier | Notes |
|---|---|---|---|---|---|
| 43761506022 | Alteva | MSP/Aggregator | Telecom Aggregator - MSP | T2 | PA mid-Atlantic aggregator |
| 103770391285 | Ark Data Centers | Data Center Colo Provider | Standard - colo | T3 | Cedar Rapids IA, Carlyle Group owned |
| 103770392271 | Ecotel Communication | MSP/Aggregator | Telecom Aggregator - MSP | T2 | German B2B telco, Frankfurt listed |
| 107187281647 | Lumen Technologies | Fiber Operator | Tier 2 National Wholesale - Fiber operator | T2 | Brief recently updated (Alkira acquisition); Tier 1 Carrier promotion candidate deferred (sells via fiber wholesale) |
| 132656728805 | EdgePresence | Data Center Colo Provider | Modular - colo | T1 | Edge DC developer, DataBank investment |
| 132994503414 | Volico Data Centers | Data Center Colo Provider | Standard - colo | T3 | Small FL colo |
| 132996285135 | Data Canopy | Data Center Colo Provider | Standard - colo | T3 | Bensalem PA |
| 132996285136 | AtlasEdge | Data Center Colo Provider | Standard - colo | T3 | Dec 2025 Templus 9-DC divestiture announced - close pending; flag for future review |
| 132996285137 | Convergia | MSP/Aggregator | Telecom Aggregator - MSP | T2 | LATAM aggregator Quebec HQ |
| 133486361310 | NTT Global Data Centers | Data Center Colo Provider | AI Signals - colo | T1 | Subsidiary of NTT DOCOMO BUSINESS (rebranded 2025); separate from NTT DOCOMO mobile carrier (batch 33) |
| 133493528256 | Windstream Wholesale | Fiber Operator | Tier 2 National Wholesale - Fiber operator | T2 | Operates as Uniti Wholesale post-merger |
| 133546028788 | Aptum Technologies | Data Center Colo Provider | Standard - colo | T3 | Toronto HQ, hybrid cloud + colo |
| 133570302699 | EverFast Fiber | Fiber Operator | Regional CLEC - Fiber operator | T3 | KC metro fiber |
| 133827394280 | Momentum | MSP/Aggregator | Telecom Aggregator - MSP | T2 | UCaaS, 750+ carrier partners |
| 142602067695 | 702communications | Fiber Operator | Regional CLEC - Fiber operator | T3 | Fargo-Moorhead area |
| 153560500973 | Ocean Networks | Fiber Operator | Long Haul / Backbone - Fiber operator | T2 | HIFL subsea cable participant - SUBSEA OPERATOR candidate (deferred for D7 verification, classification reasonable as Long Haul for now) |
| 154117927664 | Home Telecom | Fiber Operator | Regional CLEC - Fiber operator | T3 | SC regional |
| 154227594971 | Glo Fiber | Fiber Operator | Regional CLEC - Fiber operator | T3 | Shentel subsidiary mid-Atlantic |
| 154255869681 | Optimum Business | Fiber Operator | Regional Cable Operator - Fiber operator | T3 | Altice USA brand 21 states |
| 155473925856 | RevNet | Data Center Colo Provider | AI Signals - colo | T1 | Very small (3 emp); brief acknowledges scale verification needed |
| 174215644876 | Transaction Network Services | Fiber Operator | Regional CLEC - Fiber operator | T3 | Vertical financial services network; MSP/Aggregator candidate deferred (POPs Enterprise 100+, $409M rev) |
| 174907029202 | Arelion | Network Operator(Tier 1/VNO) | Pure Wholesale Carrier - Network Op | T1 | Formerly Telia Carrier; duplicate of Telia Carrier (192888735460) - R3 to resolve |
| 175109006031 | eX2 Technology, a Vivacity Company | Fiber Operator | Regional CLEC - Fiber operator | T3 | Midwest fiber/wireless |
| 175147508420 | Alluvion Communications | Fiber Operator | Regional CLEC - Fiber operator | T3 | Rural AZ tribal |
| 175156545265 | Dobson Cellular Operations | Fiber Operator | Regional CLEC - Fiber operator | T3 | Brief flagged "likely defunct" but recent_news (Nov 2025 fiber expansion Stringtown OK) contradicts; defer verification to next R2 |
| 175162002122 | Hilliary | Fiber Operator | Regional CLEC - Fiber operator | T3 | Rural OK/TX |
| 175162002127 | MOX Networks | Fiber Operator | Dark Fiber Specialist - Fiber Operator | T2 | Confidence bumped medium_7089 -> high_90; recent subsea cable participation (Topaz, Firmina) |
| 175172795115 | Mediacom Communications Corp. | Fiber Operator | Regional Cable Operator - Fiber operator | T3 | 22 states cable+fiber |
| 175176463065 | Kansas Fiber Network | Fiber Operator | Long Haul / Backbone - Fiber operator | T2 | KS/OK/MO/CO; POPs 50-99 |
| 175178260205 | Armstrong Business | Fiber Operator | Regional CLEC - Fiber operator | T3 | PA Armstrong Group subsidiary |
| 175178260210 | MBS Fiber | Fiber Operator | Regional CLEC - Fiber operator | T3 | Mid-Georgia small operator |
| 175181858521 | Granite Telecommunications | MSP/Aggregator | Telecom Aggregator - MSP | T2 | $1.6B+ POTS/voice aggregator |
| 175183656684 | AireSpring | MSP/Aggregator | Telecom Aggregator - MSP | T2 | National aggregator $45M rev |
| 175183656686 | IG NETWORKS | MSP/Aggregator | Telecom Aggregator - MSP | T2 | LATAM aggregator BA HQ |
| 175217873639 | GCI | Fiber Operator | Regional CLEC - Fiber operator | T3 | $14.2B annualrevenue suspect (probably wrong, GCI is ~$1B - data quality flag) |
| 175225132733 | Frontier | Fiber Operator | Tier 2 National Wholesale - Fiber operator | T2 | Verizon merger closing 2026 (FCC approved May 2025); flag for post-close R3 dedup vs Verizon |
| 177901485783 | NUSO | MSP/Aggregator | Telecom Aggregator - MSP | T2 | CCaaS/UCaaS Missouri HQ |
| 186793926376 | vyvebb (Vyve Broadband) | Fiber Operator | Regional CLEC - Fiber operator | T3 | Regional cable+fiber 16 states |
| 192879360699 | Telefonica | Network Operator(Tier 1/VNO) | Tier 1 Carrier - Network Op | T1 | Spanish global incumbent (multiple subsidiary records possible) |
| 192879703758 | Spectrum | Network Operator(Tier 1/VNO) | Cable MSO Enterprise Division - Network Op | T1 | $211.9B annualrevenue suspect (Charter is ~$54B - data quality flag, same value as NaviSite per batch 33) |
| 192883329781 | Aurora Fiber Optic | Fiber Operator | Regional CLEC - Fiber operator | T3 | Small MN operator (3 emp) |

---

## Tier writes summary
- **Promotions (toward T1):** 3 (HGC T3->T2, Converge ICT T3->T2, Flo Networks T3->T2)
- **Demotions (toward T5):** 2 (MTA T2->T4, GCI Liberty flagged-for-deletion)
- **Skipped (hs_is_target_account=true):** 0

## Sub-segment auto-migrations: 0
No legacy values detected (Tier 1 Global Incumbent, AI - Colocation Operator, Managed Network Services - Network Operator).

## Greenfield migrations: 0
None matched the operational milestone / abandonment / stall pattern.

## Segment changes (cascade fired): 1
- GCI Liberty: Fiber Operator -> Flagged for deletion (R4 will handle contact reassociation to primary GCI)

## Customer-protection HOLDs: 0
No customer (closed-won) records were proposed for ICP->non-ICP downgrade.

## Completeness Gate fails (held for next batch): 0
All MEDIUM-path records passed the completeness gate (all 7 enriched fields present and within 2-4 sentence cap).

## Manual-review HOLDs: 0

---

## Patterns observed this batch

### CONTINUING — National operator under-tiering (cumulative ~36, +3 this batch)
- HGC Global Communications (international wholesale, Hong Kong) — T3->T2
- Converge ICT Solutions (largest PH FTTH, 4000 emp) — T3->T2
- Flo Networks (US-Mexico cross-border, 30K+ route miles, 15 countries) — T3->T2
- Cirion Technologies — sub-segment promotion (T2 stays, was correctly tiered)

### CONTINUING — Within-fiber demotions (cumulative ~22, +1 this batch)
- MTA (Matanuska Telephone Association) — Long Haul/Backbone misclassified as backbone scale when actually member-owned coop. Demoted to Municipal/Cooperative, T2->T4.

### CONTINUING — Within-fiber reclassification (cumulative ~3 this sweep)
- Astound Broadband — Long Haul/Backbone -> Regional Cable Operator (6th-largest US MSO, accurate MSO classification)

### CONTINUING — Duplicate-pair pattern (cumulative ~2, +1 this batch)
- GCI Liberty (defunct since 2020 Charter/Liberty Broadband merger) -> Flagged for deletion as duplicate of primary GCI

### CONTINUING — Holding-co/post-merger confusion (cumulative 3)
- NTT entity tree: NTT Global Data Centers (this batch) is correctly subsidiary of NTT DOCOMO BUSINESS (rebranded 2025 from NTT Communications). Distinct from NTT DOCOMO mobile carrier flagged in batch 33. Validates the parent-subsidiary classification approach.
- GCI Liberty similar pattern (defunct standalone, primary survives)

### NEW (this batch) — Domain typo correction
- Lightpath Fiber: `lighpathfiber.com` -> `lightpathfiber.com`. Suggests Identity Sanity Check is worth running on all records lacking deal activity. Cumulative typo finds this sweep: ~1.

### CONTINUING — Subsea cable operator candidate (cumulative 0 promoted, watch list maintained)
- Ocean Networks (Pooler GA) — HIFL Cable participant (Hawaii Inter-Island Fiber Loop) — currently Long Haul/Backbone, defer to D7 for verification of pure-play subsea operator status. Carry forward.
- MOX Networks — Topaz + Firmina cable capacity acquisition; not pure-play subsea, confirmed Dark Fiber Specialist.

### NEW (this batch) — Pending-merger flag
- Frontier — Verizon merger (FCC approved May 2025); close pending 2026. Currently still classified standalone; R3 to handle dedup post-close.

---

## Data-quality follow-ups added

1. **GCI annualrevenue = $14.177B is wrong.** Actual GCI revenue ~$1B (matches their employee count and Alaska market position). Likely Liberty Broadband consolidated revenue or similar mis-attribution. Apollo refresh recommended next R2.
2. **Spectrum annualrevenue = $211.9B is wrong.** Charter's actual revenue ~$54B. Same value found on NaviSite per batch 33 — bad-data pattern (could be Spectrum Cable Group's consolidated entity number, or copy/paste error). Apollo refresh recommended next R2.
3. **NTT consolidation aftermath.** NTT Communications -> NTT DOCOMO BUSINESS rebrand (2025) may have created duplicate records. Confirm NTT Global Data Centers (this batch), NTT Communications (legacy domain), NTT DOCOMO BUSINESS (potential new record). Tim Z to review international NTT records.
4. **Frontier-Verizon merger close** — once closed, Frontier record should be reassociated/merged into Verizon. R3 + Cooper review.
5. **Templus-AtlasEdge divestiture** — 9 DCs sold to Templus per Dec 2025 announcement. Once closed, AtlasEdge entity scope reduces materially. New Templus colo entity may emerge — account-sourcing follow-up.
6. **Telia Carrier / Arelion duplicate** — confirmed by brief itself (HID 192888735460). R3 to resolve.

---

## Apollo budget
- This batch: 0 credits
- Sweep cumulative: 0 (APOLLO_ENFORCEMENT="disabled", Apollo-free path dominant)

## Errors
None. 50/50 writes succeeded across 7 batches (5+4+10+10+10+10+1).

## Run health: GREEN

---

## Drain status
- Done in this sweep: 1,700 / 2,795 expected pool (61%)
- Remaining: ~1,096 (was 1,146 pre-batch)
- ETA: ~22 more batches at BATCH_SIZE=50
