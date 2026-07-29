# R1 Fresh Enrichment — 2026-05-28 (Thursday)

**Run mode:** Cowork scheduled task, 10:00 AM CT M-F fire
**Status:** ✅ GREEN — full pool drained, 0 errors after retry, all 4 self-checks PASS
**Apollo:** 0 credits consumed / 30 sub-cap / W22 0/850 weekly

---

## Pool

- Trigger query (5 filterGroups): **10 raw candidates**
- Tier 3 exclude set (144 IDs parsed from canvas F0B0AFSB9LN R0/R1/R2/R4 sections): **7 excluded**
- After exclusion: **3 candidates processed**
- Dynamic cap: 100/run (≤200 pool size — steady state)
- Drain projection: pool is below daily cap, no backlog

### Excluded by Tier 3 set
| HubSpot ID | Account | Source |
|---|---|---|
| 324597786339 | columbus-networks/finetechnologies.co | R1 hold 2026-05-27 (MISDOMAIN) |
| 324524875475 | GATCO | R1 hold 2026-05-26 (no public ID) |
| 324498712298 | Synnap | R1 hold 2026-05-26 (aspirational sovereign-AI claims) |
| 324535363289 | Spartan Data Centers | R1 hold 2026-05-26 (no public info) |
| 324610914007 | Attobahn, Inc. | R1 hold 2026-05-26 (pseudoscientific atto-speed claims) |
| 323981908725 | Broadstar (gigabitfiber.com) | R1 hold 2026-05-22 (dup of HS 193867595510, name mismatch) |
| 321983866611 | Tract Capital | R1 hold 2026-05-08 (dup of HS 264635347666 tract.com) |

---

## Path α — Full ICP enrichment (2 writes)

### Umniah — HS 324636275403 — umniah.com — Jordan

- **customer_segment:** Network Operator(Tier 1 / VNO)
- **company_sub_segment:** Tier 1 Carrier - Network Op
- **account_tier:** tier_3 ← Cooper fix-directly principle applied (emerging-market Jordan MNO over-tiered as tier_1 historical pattern)
- **segmentation_confidence:** medium_7089 (best-fit, no Tier 2/3 emerging-MNO sub-segment exists)
- **signal_heat:** Cold (new account default)
- **owner:** Tim Ziemer 159350430 (International) — already correct
- **last_enriched_date:** 2026-05-28

**Dedup note:** Umniah has a sister record `Umniah Wholesale` at HS 324208154349 / umniah.jo (Pure Wholesale Carrier - Network Op / tier_1 / high_90 / last_enriched 2026-05-19). The two records are legitimately separate entities — umniah.com is the retail/MNO consumer-facing brand; umniah.jo is the wholesale carrier interconnect arm. Both subsidiaries of Beyon (Bahrain Telecom Group). No dup write.

**Tier rationale:** Per Cooper's 2026-05-26 `r1_dont_flag_fix` principle — Jordan ~$300M-revenue regional MNO with ~1,750 employees is NOT a Tier 1 global incumbent (Verizon/AT&T scale). Best-fit sub-segment is "Tier 1 Carrier - Network Op" because no Tier 2/3 emerging-market MNO sub-segment exists, but tier value is dialed down to tier_3 to match actual regional scale. Fix-directly with audit note; not surfaced as review item.

### Twin Lakes Telephone Cooperative — HS 324628839134 — twinlakes.net — Tennessee

- **customer_segment:** Fiber Operator
- **company_sub_segment:** Municipal / Cooperative - Fiber operator
- **account_tier:** tier_3
- **segmentation_confidence:** high_90 (cooperative governance, FTTH 1G symmetric, RUS/RDOF/BEAD-eligible — classic Municipal/Cooperative pattern)
- **signal_heat:** Cold (new account default)
- **owner:** Tim Lieto 161889085 (East) ← **OWNER CORRECTION** from Ken Cunningham 162339176 (West). TN is one of the 30 East-region states per territory model.
- **last_enriched_date:** 2026-05-28

---

## Path β — Re-research / no-op (1 record)

### ResetData — HS 324591600333 — resetdata.com.au — Australia

**No write.** Record was fully enriched 2 days ago (2026-05-26) by R1 Path α with:
- customer_segment = NeoCloud
- company_sub_segment = Sovereign AI Clouds - Neocloud
- segmentation_confidence = high_90
- last_enriched_date = 2026-05-26
- hs_is_target_account = **true**
- account_tier = **null** (deliberately not written per freeze rule)
- owner = Tim Ziemer 159350430 (correct for Australia)

**Frozen-tier reappearance loop:** ResetData reappears in Filter Group B2 daily because `account_tier` is null while the rest of the ICP fields are populated. The inviolable rule freezes `account_tier` algorithmic writes whenever `hs_is_target_account = true`. R1 2026-05-26 deliberately honored this freeze; today I honor the same precedent — no tier write.

**Cooper review item:** If you want to break this loop, manually set `account_tier = tier_1` in HubSpot UI (Sovereign AI Clouds Neocloud + named-account override would naturally compute tier_1 ceiling). Alternative: refine R1 Filter Group B2 to exclude records where `hs_is_target_account = true`. Currently there are ~382 records with `hs_is_target_account = true`; some fraction may have blank `account_tier` and contribute to recurring R1 pool appearances.

---

## Path γ — Eviction (0 records)

No LIKELY_NON_ICP / LIKELY_JUNK candidates in pool today. All 7 excluded records were prior Tier 3 holds + R3 dup queue — no Path γ work.

---

## 4 End-of-pipeline self-checks

| Check | Result |
|---|---|
| 1. Sub-segment nullness on ICP writes | PASS (Umniah + Twin Lakes both have sub-segment populated) |
| 2. Confidence-evidence alignment | PASS (Twin Lakes high_90 cites cooperative governance + RUS/RDOF/BEAD pattern; Umniah medium_7089 N/A) |
| 3. Disqualifier audit | PASS by absence (no Path γ Other writes or D1 evictions) |
| 4. Catch-all guard (Regional CLEC / Standard - colo / Telecom Aggregator) | PASS by absence (Tier 1 Carrier + Municipal/Cooperative sub-segments; not catch-alls) |

---

## Errors encountered (resolved)

1. **infrastructure_profile + hyperscaler_proximity 400 on first Umniah write.** Initial values `"1-5 Facilities"` and `"None Identified"` (for hyperscaler_proximity) were rejected. Canonical values per HubSpot enum: `Facilities: Small (<5);Route Miles: Mid-Size (1K-10K);POPs: Mid-Size (10-49)` for infrastructure_profile and `None Known` (NOT `None Identified`) for hyperscaler_proximity. Retry succeeded. **Memory updated:** added `hubspot_hyperscaler_proximity_enum.md` to MEMORY.md index (file already existed from 2026-05-21 but wasn't indexed, parallel to the `hubspot_fabric_provisioning_approach_enum.md` lesson from 2026-05-22 R2 run).

---

## Apollo budget

- Sub-cap: 30/run
- Used this run: 0
- W22 weekly: 0/850, 850 remaining
- Git commit policy: best-effort (this is a local-file-only run for Cowork; no commit attempted).
