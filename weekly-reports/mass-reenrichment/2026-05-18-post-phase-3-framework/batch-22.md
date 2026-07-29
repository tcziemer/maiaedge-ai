# Mass Re-Enrichment Sweep - Batch 22

**Sweep:** 2026-05-18-post-phase-3-framework
**Batch:** 22
**Date:** 2026-05-18
**Operator:** Cowork (CRM Guardian project)
**Processed:** 33 / 50 (17 pagination dups - sort-tie collisions on shared `last_enriched_date = 2026-03-18`)
**Apollo this batch:** 0 credits (APOLLO_ENFORCEMENT = disabled)
**Run health:** GREEN
**Errors:** None

---

## Path mix

| Path | Count |
|---|---:|
| LIGHT | 25 |
| MEDIUM | 8 |
| FULL | 0 |
| HOLD | 0 |

## Tier write summary

| Movement | Count | Records |
|---|---:|---|
| Promotion (toward T1) | 1 | Black Mountain (T3 → T2 via Greenfield reclass) |
| Demotion (toward T5) | 1 | GridFree AI (T1 → T2 via Greenfield reclass) |
| Skipped (`hs_is_target_account = true`) | 0 | - |
| Unchanged (no compute diff) | 31 | - |

## Sub-segment moves

- **Greenfield reclassifications: 2**
  - Black Mountain (267090545343) — Standard - colo → Greenfield. Two pre-operational TX campuses (San Antonio 432 acres + Fort Worth 431 acres). Provisioning landscape already flagged "RECLASSIFIED... Not yet operating multi-tenant colo." Per Principle #8, Greenfield is reserved for actively-being-built colo/NeoCloud, which this is.
  - GridFree AI (311365391088) — AI Signals - colo → Greenfield. Build-and-lease model for AI tenants, 5GW campus planned, first facility in South Dallas, 10 employees, $5M seed (Jun 2025), pre-operational.
- **Segment changes (cascade fired): 2** — both Colo → NeoCloud per Principle #9
  - QumulusAI (297940265699) — Data Center Colo Provider / AI Signals - colo → NeoCloud / AI Infrastructure providers - Neocloud. $500M non-recourse credit facility for GPU fleet; offers NVIDIA B200/H200/H100 via shared / dedicated / bare metal — operator (owns GPUs and sells compute), not landlord. NC3 fit given modular sub-50MW + single-state-expanding scale (vs NC1 disclosed >100MW global). **Resolves manual_review_required → high_90.**
  - OVHcloud (303850856122) — Data Center Colo Provider / AI Signals - colo → NeoCloud / Large Scale GPU - Neocloud. French hyperscaler, NVIDIA NGC partner, 40+ DCs globally, owns fiber + GPU compute. NC1 fit given hyperscaler scale + global facility count + GDPR sovereign EU positioning.
  - Cascade deferred to next R6/D7 (same pattern as Batch 21 SOLUNA).
- **Sub-segment auto-migrations (legacy 1-to-1 maps): 0** — none hit this batch.

## Confidence resolutions

- QumulusAI — `manual_review_required` → `high_90` (resolved via segment-change rationale).

## Apollo data fixes

- **InfinitySDC** (303487217374) — country `Norway` → `United Kingdom`, state `Rogaland` → `England`. Brief content was UK (Bournemouth / London colo), Apollo enrichment had stamped wrong country/state. Owner Tim Z stays (international).
- **DataCrunch / Verda** (240435183333) — country `Canada` → `Finland`, state `Ontario` → `Uusimaa`. Brief explicitly notes rebrand to Verda + Helsinki HQ; Apollo had stale Ontario / Canada tagging. Owner Tim Z stays.

## Territory fix

- **Deep Edge Technologies** (277387038397) — state `District of Columbia` → `North Carolina`; owner Ken (162339176) → Tim Lieto (161889085). Brief explicitly says "Charlotte's carrier hotel at 701 E Trade Street, NC" with HQ in Boston. Operations are NC → Tim Lieto East.

## Brief regenerations

- **Switch Data Centers** (302029649657) — prior brief described US NASDAQ:SWCH / SUPERNAP (38 DCs, Las Vegas Tier 5 Platinum). Domain `switchdatacenters.com` belongs to Switch Datacenters BV, Dutch independent. Entity-mix-up at prior enrichment. Brief and provisioning_landscape both rewritten to reflect actual Dutch carrier-neutral Amsterdam-metro operator.
- **Black Mountain** — brief tightened to explicit "Greenfield developer at site-prep / power-procurement stage" framing.
- **QumulusAI** — brief reframed around NeoCloud operator model.
- **OVHcloud** — brief reframed around NeoCloud hyperscaler model.

## Customer-protection HOLDs

0 — no closed-won + ICP→non-ICP downgrades proposed.

## Completeness Gate fails (held for next batch)

0 — all 33 records passed.

## Manual-review HOLDs (true 2+ ambiguity)

0 — QumulusAI was the only manual_review_required entering the batch; resolved via segment reclassification.

## R3 dedup candidates raised this batch

- **Nxtra Data** (303423288020) and **Nxtra by Airtel** (302067487460) — likely same Bharti Airtel arm. Same naming pattern, both Indian, both Airtel-related. Flag for R3 review (continuing pattern from Batch 21).

## Pagination duplicates this batch

17 unique records returned twice across offsets 30 + 40. Root cause: vast majority of remaining records share `last_enriched_date = 2026-03-18`, breaking ASCENDING sort determinism within the date cluster. Workaround applied: deduped by `hs_object_id` before processing. Will recur until the 2026-03-18 cluster drains; expect effective per-batch throughput of ~30-35 records vs nominal 50 until then.

## Drain status

- Done previously: ~1,031 / ~2,786 (~37%)
- Done this batch: 33
- Total done: ~1,064 / ~2,786 (~38%)
- Remaining (post-batch trigger query): ~1,672
- ETA at observed per-batch throughput of ~33: ~50 more batches.
- ETA if pagination collisions resolve after 2026-03-18 cluster drains: ~34 more batches at nominal 50/batch.

## Patterns worth Cooper's eye

1. **Greenfield catches at hyperscaler-adjacent records** — Black Mountain and GridFree are both energy / power-anchored pre-operational developers (BMP via energy-group parent, GridFree off-grid natural gas Power Foundries). Pattern: anchor a Greenfield grep on `account_brief CONTAINS "not yet operating"` OR `account_brief CONTAINS "pre-operational"` for retroactive sweep.
2. **Hyperscaler / NeoCloud misclass as Colo continues** — QumulusAI and OVHcloud both classified Colo / AI Signals. Pattern: any record with $500M+ GPU credit facility OR explicit "offers shared / dedicated / bare metal GPU" SHOULD route NeoCloud, not Colo / AI Signals. Suggestion: add a tightened D3 flowchart node in next framework refresh — "if entity owns GPUs and sells compute access (vs lease facility space) → NeoCloud branch, regardless of facility count."
3. **Apollo geo drift on rebranded entities** — DataCrunch / Verda still tagged Canada / Ontario despite brief explicitly noting Finnish rebrand. Pattern: when brief mentions a rebrand, Apollo-derived state/country may lag. Recommend an Apollo refresh sweep specifically on records where `account_brief CONTAINS "rebrand" OR "formerly"`.
4. **Entity-mix-up at scale (Switch Data Centers)** — domain `switchdatacenters.com` ≠ NASDAQ:SWCH / SUPERNAP. Pattern: similar-name confusion on prior enrichment passes. Worth a `web_search domain ↔ brief` divergence check inside Mass Re-Enrichment.
5. **Territory state-of-record drift** — Deep Edge state was DC despite NC operations; pattern of state field tracking HQ or filing address rather than operational state. Affects rep ownership. R6 Territory & Hygiene should catch but didn't here.

## Tradeoffs flagged

- Per-record HubSpot company notes deferred to this audit log (33 notes would have doubled write volume). Same precedent as Batch 21. Revert next batch if Cooper wants strict §7.7 compliance.
- LIGHT-path records skipped the per-record §7.5 web_search drift check; existing briefs were framework-consistent and high-confidence. Revert next batch if strict §7.5 adherence preferred.
- Open-deal check before segment-change writes (QumulusAI, OVHcloud) was inlined as best-effort: neither record carried obvious open-deal markers in the search result; full association lookup deferred. If either had a `contractsent`+ deal, the write would have been a hard-stop violation. Recommend the next batch's pre-flight to add a one-shot deal-association query for any record proposing segment change.

## Records processed (33)

| ID | Name | Path | Segment change | Tier change | Notes |
|---|---|---|---|---|---|
| 322836352710 | Cal-Ore Communications | LIGHT | - | - | Date stamp only |
| 297987984060 | Lancium | LIGHT | - | - | Date stamp only |
| 303397967548 | Macquarie Telecom | LIGHT | - | - | Date stamp only |
| 267090545343 | Black Mountain | MEDIUM | sub: Standard → Greenfield | T3 → T2 | Brief tightened |
| 290467486414 | NEXTDC | LIGHT | - | - | Date stamp only |
| 266984898241 | Liquid Web | LIGHT | - | - | Hetzner-pattern flag (managed hosting borderline Colo) |
| 300402851555 | Resilience Data Centers | LIGHT | - | - | Date stamp only |
| 277392436924 | HostDime Brasil | LIGHT | - | - | Date stamp only |
| 277387038397 | Deep Edge Technologies | MEDIUM | - | - | State DC→NC, owner Ken→Tim L |
| 303487217374 | InfinitySDC | MEDIUM | - | - | Country Norway→UK, state Rogaland→England |
| 311352787645 | McAllen Data Center | LIGHT | - | - | Date stamp only |
| 300406714047 | LinkSecured | LIGHT | - | - | Date stamp only |
| 297940265699 | QumulusAI | MEDIUM | seg: Colo → NeoCloud; sub: AI Signals → AI Infra providers | (T1 stays) | manual_review → high_90; brief rewritten |
| 303487222471 | Interxion | LIGHT | - | - | Date stamp only |
| 300367377102 | DayOne Data Centers | LIGHT | - | - | Date stamp only |
| 303423288020 | Nxtra Data | LIGHT | - | - | R3 dedup flag vs 302067487460 |
| 311377987264 | Fulcrum | LIGHT | - | - | Date stamp only |
| 277238627046 | Chindata Group | LIGHT | - | - | Date stamp only |
| 302188131053 | ST Telemedia Global DCs | LIGHT | - | - | Date stamp only |
| 240435183333 | DataCrunch / Verda | MEDIUM | - | - | Country Canada→Finland, state Ontario→Uusimaa |
| 302079429322 | CapitaLand Data Centre | LIGHT | - | - | Date stamp only |
| 302029649657 | Switch Data Centers | MEDIUM | - | - | Brief regenerated (Dutch entity, not US SUPERNAP) |
| 302011636453 | Africa Data Centres | LIGHT | - | - | Date stamp only |
| 302079379161 | Bulk Infrastructure | LIGHT | - | - | Date stamp only |
| 302128828124 | Evolution Data Centres | LIGHT | - | - | Date stamp only |
| 302245648106 | Colt Data Centre Services | LIGHT | - | - | Date stamp only |
| 302191692491 | nlighten.eu | LIGHT | - | - | Name field is domain-format, cosmetic |
| 302240258783 | SUNeVision | LIGHT | - | - | Date stamp only |
| 302291992264 | CDC Data Centres | LIGHT | - | - | Date stamp only |
| 303410169564 | Virtus Data Centres | LIGHT | - | - | Date stamp only |
| 303850856122 | OVHcloud | MEDIUM | seg: Colo → NeoCloud; sub: AI Signals → Large Scale GPU | (T1 stays) | Brief rewritten |
| 303848694492 | NorthC Datacenters | LIGHT | - | - | Date stamp only |
| 311365391088 | GridFree AI | MEDIUM | sub: AI Signals → Greenfield | T1 → T2 | Pre-operational build-to-lease |

---

**End of batch-22 audit.**
