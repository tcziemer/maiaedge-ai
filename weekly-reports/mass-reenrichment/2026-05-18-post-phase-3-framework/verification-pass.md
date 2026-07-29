# Mass Re-Enrichment Sweep — 2026-05-18-post-phase-3-framework — Verification Pass

**Run date:** 2026-05-19
**Mode:** Aggregate audit (per Cooper 2026-05-19 — skip full §11 mass tier recompute; verify distribution + confidence + spot-check classifications instead)
**Pool:** records with `last_enriched_date >= 2026-05-18`
**Total in pool:** 2,488 active ICP records (6 segments)
**Apollo:** 0 credits (read-only audit)
**Writes:** 0 (no drift correction this pass; steady-state R-Tier-Audit + R2 own the signal-modifier drift catch)

---

## Segment distribution (sums to 2,488)

| Segment | Count |
|---|---:|
| Fiber Operator | 1,164 |
| Data Center Colo Provider | 462 |
| Network Operator(Tier 1 / VNO) | 394 |
| MSP/Aggregator | 312 |
| NeoCloud | 152 |
| Enterprise-CustomerSegment | 4 |
| **Total** | **2,488** |

All 6 ICPs, no leakage to retired segments. Enterprise tiny (4) — expected given the Multi-DC hard gate (vertical AND $1B+ AND 3+ DCs OR Fabric/Megaport port OR in-house net eng).

## Confidence distribution (sums to 2,488)

| Confidence | Count | % |
|---|---:|---:|
| `high_90` | 1,731 | 69.6% |
| `medium_7089` | 628 | 25.2% |
| `low_5069` | 90 | 3.6% |
| `manual_review_required` | 0 | 0.0% |
| (missing) | 39 | 1.6% |

Cooper 2026-05-14 target: `manual_review_required` <5%. **Actual: 0%.** Confidence is strongly skewed toward `high_90` (best-fit + tiebreaker working as designed).

## Sub-segment values

200-record sample (sorted by hs_object_id ASC) shows **19 distinct sub-segment values, all from the 30 active set**. No retired/legacy strings detected:
- ❌ "Tier 1 Global Incumbent"
- ❌ "AI - Colocation Operator"
- ❌ "Managed Network Services - Network Operator"
- ❌ "Co-op/consortium"
- ❌ "External Extension - Network operator"
- ❌ "Internal + external unification - Network Operator"

All retired enums archived per Phase 1.6; sweep did not write any.

Case-sensitivity verified:
- `Dark Fiber Specialist - Fiber Operator` (capital O) ✓
- `AI Infrastructure providers - Neocloud` (lowercase p) ✓
- `Crypto to AI - Neoclouds` (trailing s) ✓
- `Network Operator(Tier 1 / VNO)` (no space before paren) ✓
- `Subsea cable operator` (lowercase, no `- Network Op` suffix) ✓
- `Managed Network Services - MSP` (post-Phase 1.7c.1) ✓

## Specialty sub-segment spot-checks

| Sub-segment | Pool total | Spot-check observations |
|---|---:|---|
| `Subsea cable operator` (new 2026-05-14) | 21 | Hawaiki Cable T1, BW Digital T1, EllaLink T2, Southern Cross T2, Seychelles Cable T1, FSM Telecom T2, Trans Pacific Networks T2, Inligo T2, Medusa T2 — all verified pure-play subsea operators; default T2 with hot signals pulling some to T1 ✓ |
| `Greenfield` | 24 | New Era Energy & Digital T2, Sailfish Digital T2, Tillion T2, Inferra T3, UrsaCloud T2 (NeoCloud parent), Montera T2, GridFree AI T2, Beacon T3, EdgeCloudLink T3, Starcloud T2 — all genuine Series A-C buildouts; T2/T3 split matches default T2 ceiling 1 floor 3 ✓ |
| `Master Agent - MSP` | 3 | Telarus (high_90, T3 — confirmed Master Agent anchor), TCG-Partners (low_5069, T3), Custom Communications III (medium_7089, T3). Thin verified-anchor list matches CLAUDE.md known data quality follow-up #6. ✓ |
| `Crypto to AI - Neoclouds` | 26 | Crusoe T1, IREN T1, Prometheus Hyperscale T1, HIVE T1, Moonshot T1, Keel T1, SOLUNA T1, Mawson T1, Greenidge T1, Soluna Computing T1 — all BTC-mining-to-AI conversions per Operating Principles #9. All at T1 (default T1 ceiling 1 floor 2) ✓ |
| `Hyperscale Wholesale - colo` | 26 | CyrusOne T1, Compass T1, CloudHQ T1, EdgeCore T1, CTP T1, Yondr T1, Fleet Data Centers T1, SUNeVision T1, Echelon T1 — all genuine hyperscale wholesale providers, all T1 ✓ |

## Outstanding gap (41 records, 1.6% of pool)

**39 records missing `segmentation_confidence`** but with valid segment + sub-segment + tier — looks like confidence stamp was skipped on a slice. Substantively correct (NTT, Telenor Norge, Globe Telecom, Liquid Telecom, Rakuten Mobile, Telecom Argentina, Kyivstar, Aion, Dimension Data, Cloud4C, Schurz Broadband, Speedcast, Network Innovations, etc).

**2 records missing `company_sub_segment`** — Medallion Communications (Colo, high_90, T3), Matrix (Colo, medium_7089, T2). Both fall under Colo null fallback (T3) which is what they got.

Recommendation: pick these up via R-Tier-Audit weekly null-fallback handler or D7 weekly edge case resolution. Not worth a dedicated write batch.

## Run summary

- ✅ 6 active ICPs only
- ✅ 0 retired enum values
- ✅ 0% `manual_review_required` (target <5%)
- ✅ All 5 spot-checked specialty sub-segments populated with correct anchors + reasonable confidence
- ✅ Tier distribution reasonable (T1/T2/T3 dominant, T4 sparse, T5 absent in sample — consistent with Municipal/Coop default T4 and most accounts not stacking stale+sustained-quiet modifiers)
- ⚠️ 41 records (1.6%) with small gaps in confidence / sub-segment — defer to R-Tier-Audit + D7

## Decision

**Skip the §11 mass tier recompute.** Classification produced by the sweep is clean. Mid-sweep signal-modifier drift will be caught by R-Tier-Audit (Friday 3pm CT) and R2 (daily M-F) at trivial cost.

Sweep is fully closed.

## Cooper's manual next steps

1. Re-enable steady-state R2 cron (`Stale_Re_Enrichment_Prompt.md`)
2. Restore `APOLLO_ENFORCEMENT = "enabled"` on the weekly 850 cap
3. Append the 41-record confidence/sub-segment gap to CLAUDE.md "Known Data Quality Follow-ups" if you want a paper trail
4. The 2 sticky HOLDs (Wyoming Hyperscale 321238936271, INDATEL 322761764552) remain owned by R3 + D7 per batch 58 DM — they had `last_enriched_date < 2026-05-18` so were correctly excluded from this verification pool

---

**Audit log written by Cowork verification pass run 2026-05-19.**
