CRM Guardian - Stale Re-Enrichment - 2026-06-08 - 0 Tier 2 flagged, 2 Tier 3 held

Run summary: 10/100 processed (writes) · buckets: 7 Filter-B RE_ENRICH_FULL + 3 Filter-C pre-spread completions · 9 Tier 1/stamped, 0 Tier 2 eviction, 2 Tier 3 held · Apollo: 0/50 used (0/850 weekly W24, 850 remaining) · Freshness: GREEN (steady state)

Today = 2026-06-08 (Mon), 120-day cutoff = 2026-02-08, TZ America/New_York.

Trigger pool:
- Filter A (last_enriched_date < 2026-02-08, exclude Flagged-for-deletion + MaiaEdge own): 0 records.
- Filter B (never-enriched + customer_segment populated, exclude Flagged-for-deletion): 8 raw -> 7 net (MaiaEdge own 124293230301 hard-stopped). These are exactly the 7 low_5069 ICP records R1 wrote (un-stamped) this morning and explicitly handed to R2/D7 for re-validation.
- Filter C (rotation pre-spread; A+B net = 7 < 40 -> fired): oldest-enriched not-yet-stale pool is the Feb/Apr `Other` micro-record cohort (oldest dated 2026-02-24, due to go Filter-A stale ~2026-06-24). Processed 3 genuine field-completions; deferred the opaque remainder (see below). The real Sept cliff (May-migration cohort, ~3,000 records) is NOT in the oldest-ASC view, so re-stamping these Feb records is low-leverage; they will hit the normal stale path on their own due-date.

What needs Cooper's attention:
- 2 Tier 3 holds - see canvas F0B0AFSB9LN section "R2 Stale Re-Enrichment 2026-06-08":
  1. BlueRim Networks (326179855037) - DEDUP: web research confirms BlueRim was acquired by Smartaira on 2022-01-01 (assets/employees/customers absorbed, brand retired -> "Smartaira 360"). Smartaira already exists as ICP record 267091939028 (MSP/Aggregator, tier_4). R1 classified BlueRim Fiber Operator this morning at low_5069; R2 set segmentation_confidence = manual_review_required + dedup account_brief, NO date stamp. Route to R3 for merge.
  2. MMR Fiber Solutions / SouthWestern Power Group (175221473010) - SURPRISE ICP + identity ambiguity. Record is Other tier_5 under domain southwesternpower.com (the utility/power developer parent, MMR Group subsidiary). But the fiber arm MMR Fiber Solutions (separate domain mmrfiber.com) is building an open-access wholesale long-haul/middle-mile dark fiber network across AZ-NM (Albuquerque, Tucson, Phoenix, El Paso) explicitly targeting carriers, service providers and hyperscalers -> a real Fiber Operator ICP (Long Haul / Backbone, likely emerging/under-construction). NOT auto-written: the combined-name record + wrong domain + separate fiber-arm domain is a genuine entity-split ambiguity. Recommend split or domain-correct to mmrfiber.com + reclassify to Fiber Operator. No write, no stamp.
- 0 eviction Tier 2 (no Flagged-for-deletion writes this run).
- 0 segment transitions hard-flipped. (BlueRim's Fiber Op label left in place pending R3 merge; only confidence downgraded.)
- T-Systems family note for R3: T-Systems Brasil (326188915439) stamped this run; T-Systems Iberia + T-Systems parent also exist (R1 06-08). Validate/merge per D2 wholesale-arm policy.
- ~16 Filter-C opaque Feb-2024-dated `Other` micro-records DEFERRED to a dedicated field-completion pass (they carry a segment label but are missing all 7 enriched narrative fields; re-stamping unverified would violate date-bump discipline). They will surface on Filter A at their natural ~2026-06-24 stale date. List: LB Networks, Pai Telecom, HDTandem, Bumblebee Networks, Network Planning Solutions, JapTel, LATINO COMMUNICATIONS CORP, MasNegocio, WIT ONE, Associated Carrier Transport, Innovative Telecom, ALCASAGAR, UNO, BNS Inc, HGC (hgcconstruction.com - likely general contractor, possible No-ICP-fit on re-research), Global Convergence Solutions.

Run health: GREEN

Errors: None.

---

Detail - records processed (writes):

Filter B (RE_ENRICH_FULL re-validation of R1's same-day low_5069 writes) - 6 keepers upgraded low_5069 -> medium_7089 + last_enriched_date stamped 2026-06-08; signal_heat unchanged (Cold); account_tier unchanged (R1-fresh, no modifier change); owners unchanged:
| ID | Name | Segment / Sub-segment | Tier | Note |
| 326171165415 | Hal Service (WiC) | Fiber Operator / Regional CLEC | tier_3 | Owns regional fiber + ASN AS44092 (N. Italy); single-marker clear. |
| 326350146243 | Blue Cross NC | Enterprise-CustomerSegment / Financial Services | tier_3 | $10B health insurer; Enterprise scale gate passes on in-house net eng. Financial-Services sub-segment per R1's E1 insurer tiebreaker (defensible vs Healthcare Systems). |
| 326188915439 | T-Systems Brasil | Enterprise-CustomerSegment / Outsourcing Services | tier_3 | D2 parent inheritance (T-Systems / Deutsche Telekom). Thin independent BR footprint; flagged to R3 for T-Systems family dedup. |
| 326350145260 | Verve Cloud | MSP/Aggregator / Cloud + Telecom Hybrid MSP | tier_2 | account_brief + recent_news refreshed: Digerati DIVESTED controlling interest (~$29M rev); now operates independently of former distressed parent (distress framing removed). |
| 326350145243 | Telvantis | MSP/Aggregator / Telecom Aggregator MSP | tier_2 | Wholesale voice (Mexedia group); core voice unit being acquired by Spectral Capital (Dec 2025), ongoing operation. |
| 326188916410 | EQUADEX | MSP/Aggregator / Cloud + Telecom Hybrid MSP | tier_2 | Small French MS cloud integrator w/ small owned DCs + connectivity positioning; weakest ICP case but sub-segment fits. |

Filter B - 1 Tier 3 dedup hold (NO stamp): BlueRim Networks (326179855037) -> manual_review_required + dedup brief (see attention list).

Filter C (rotation pre-spread) - 3 genuine field-completions stamped 2026-06-08 (were missing all 7 enriched fields; researched + full briefs written; classification confirmed Other; confidence kept high_90):
| ID | Name | Classification | Note |
| 300724801216 | Clockwork.io | Other (tier_2) | Network clock-sync / cloud latency-optimization software vendor (Stanford spinout 2018; Nasdaq/Wells Fargo/RBC). D1 software vendor. |
| 316621828848 | Speedflow | Other (tier_4) | UK VoIP wholesale + MediaCore Class-4 softswitch/billing software vendor. |
| 316621828846 | didXL | Other (tier_4) | Poland wholesale DID / virtual-number + cloud-telephony SaaS (150+ countries); no owned network. |

Apollo: 0 credits this run (all firmographics already populated/current; classifications from public web research + HubSpot reads). Sub-cap 50/run, used 0 of 50. Weekly W24: 0/850, 850 remaining.

Cross-routine ledger: appended "R2 Stale Re-Enrichment 2026-06-08" section to canvas F0B0AFSB9LN (Run-log row + 2 Tier 3 holds). No prior R2 carryovers to drain (R2 Tier-3 queue confirmed empty since 2026-05-25 audit; standing canvas holds are R0/R1/R3 scope).
