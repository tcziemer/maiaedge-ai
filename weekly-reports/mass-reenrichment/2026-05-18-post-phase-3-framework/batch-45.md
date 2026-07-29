# Mass Re-Enrichment Sweep — 2026-05-18-post-phase-3-framework — Batch 45

**Run date:** 2026-05-19
**Sweep kickoff:** 2026-05-18
**Records processed:** 50/50 written, 4 notes attached, 0 failures
**Path mix:** LIGHT 46 · MEDIUM 1 (Modal) · FULL 3 (Chugwater + ICS Advanced + NDemand) · HOLD 0
**Apollo:** 0 credits (enforcement disabled; sweep outside the 850/wk cap)
**Pool drain:** 609 → 559 remaining
**Sort:** hs_object_id ASC, starting after 297906089717
**Pattern flavor:** US small-fiber-heavy (45 of 50 are rural ILECs / co-ops / regional CLECs already bucketed correctly under Phase 3). Net 3 reclassifications.

---

## Notable changes (FULL + MEDIUM paths)

### 297918677702 — Chugwater Telephone (FULL reclass)
- Path: FULL
- Domain: chugtelco.com
- Segment: `Data Center Colo Provider` → `Fiber Operator`
- Sub-segment: `Standard - colo` → `Regional CLEC - Fiber operator` (legacy auto-migration: no)
- Confidence: high_90 → high_90
- Tier: tier_3 → tier_3 (no change; Standard-colo default T3 = Regional-CLEC-fiber default T3)
- Apollo: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Chugwater Telephone is the FTTH ILEC subsidiary of Mountain West Technologies serving the Chugwater WY town (Wyoming's first 100% fiber-served community, ~Chugwater to Torrington corridor). Parent MWT's "Data Center of the Rockies" in Casper was misattributed as Chugwater's. The colo footprint belongs on a separate MWT parent record. ChugTel is fiber + voice + business internet for a single-town ILEC market, not colocation.

### 297940265680 — ICS Advanced Technologies (FULL reclass + tier demotion)
- Path: FULL
- Domain: ics-llc.net
- Segment: `Fiber Operator` (unchanged)
- Sub-segment: `Long Haul / Backbone - Fiber operator` → `Regional CLEC - Fiber operator`
- Confidence: high_90 → high_90
- Tier: tier_2 → tier_3 (within-fiber demotion; defaults shift)
- Apollo: no
- web_searches: 1
- Completeness Gate: pass
- Reason: ICS Advanced Technologies (Ames IA, founded 2002) is an MDU-focused turnkey amenity ISP for multi-family residential properties across IA + IL + 9 states. 20-year MDU specialist on the Calix Broadband Platform; grew MDU connections 125% in 2024 (8K residential units in 12 months). Not a long-haul/backbone operator — Regional CLEC fits the MDU-focus model.

### 297918677708 — NDemand (FULL eviction → Flagged for deletion)
- Path: FULL
- Domain: ndemand.com
- Segment: `Fiber Operator` → `Flagged for deletion`
- Sub-segment: `Regional CLEC - Fiber operator` → (cleared)
- Confidence: low_5069 → high_90
- Tier: tier_3 → (n/a — non-ICP segment, tier irrelevant)
- Apollo: no
- web_searches: 1
- Completeness Gate: pass (eviction gate)
- Reason: NDemand is a fixed-wireless WISP (Shelby/Nacogdoches/San Augustine/Panola counties, East Texas). Primarily wireless, not fiber-first. Does not match any of the 6 active ICP segments and is not useful as a competitive or partner reference. Per Cooper's aggressive Flagged for deletion rule, eviction over Other.

### 297918677710 — Modal Labs (MEDIUM news fill)
- Path: MEDIUM
- Domain: modal.com
- Segment: `NeoCloud` (unchanged)
- Sub-segment: `Tier 1 Inference - Neocloud` (unchanged)
- Confidence: high_90 → high_90
- Tier: tier_2 → tier_2 (default holds; no signal field writes from this path)
- Apollo: no
- web_searches: 1
- Completeness Gate: pass
- Reason: Prior `recent_news_or_trigger_event` field was empty despite material funding activity. Filled with: $87M Series B at $1.1B post-money Sept 2025 (Lux Capital) → unicorn 23 months after Series A → $300M ARR Apr 2026 (up from $119M Dec 2025) → in talks for $150-250M raise at $4.5B valuation May 2026 with Accel/Redpoint. Recommend Signal Scan pickup of the $4.5B-valuation talks for hot/white-hot tier modifier.

---

## LIGHT path (46 records, stamp-only)

All 46 records cleared LIGHT path with `last_enriched_date = 2026-05-19` stamp-only writes. The prior framework had bucketed them correctly under Phase 3 defaults; tier recompute is a no-op for every record (defaults align with current values, no signal modifiers fire on records with null signal fields).

### Regional CLEC - Fiber operator (29 records)

297918677700 Corn Belt Telephone · 297918677703 Home Communications · 297918677704 Nsight · 297918677706 Magazine Telephone Company · 297918677707 Relyant Communications · 297918677712 ZochNet · 297918677715 NextLight · 297918677716 Valliant Telephone Company · 297918677717 Glasford Telephone · 297918677718 Gorham Telephone · 297918677719 Lynnville Telephone Company · 297918677721 Albany Mutual Telephone Association · 297934868195 Allied Telecom Group · 297934868197 Smart City Telecom · 297934868199 Peoples Telecommunications · 297934868206 Empire Telephone Corporation · 297934868209 Industry Telephone Company · 297934868210 Haviland Broadband · 297934868211 Riviera Telephone · 297936668404 NEK Broadband · 297936668406 Polar Communications · 297936668408 Hancock Telephone · 297936669375 Wilson Communications · 297936669376 Pathway Com-Tel · 297940265683 PellaFiber · 297940265684 Peoples Services · 297940265685 Northeast Nebraska Telephone Company · 297940265688 VTX Communications · 297940265693 Ardmore Telephone · 297940265694 Estherville Communications · 297940265695 TVN & Trenton Telephone · 297944750826 Nebraska Central Telephone Company · 297944750828 Rock Port Telephone · 297944750829 Nucla-Naturita Telephone Company · 297944750831 Mutual Telephone Company of Morning Sun, Iowa

### Municipal / Cooperative - Fiber operator (10 records)

297918677713 Palmetto Rural Telephone Cooperative · 297918677720 Hershey Cooperative Telephone Company · 297934868198 Cheyenne River Sioux Tribe Telephone Authority · 297934868207 Mon-Cre Telephone Cooperative, Inc. · 297936669371 Central Texas Telephone Cooperative · 297936669372 Planters Telephone Cooperative · 297940265689 Lake Region Electric Cooperative · 297940265696 Progressive Rural Telephone Co-Op, Inc.

### Long Haul / Backbone - Fiber operator (4 records)

297934868196 Blackfoot Communications · 297940265697 FastTrack Communications · 297944750827 Stanton Telecom

---

## Anomalies / followups

1. **Chugwater colo misattribution**: parent Mountain West Technologies (mwtn.net) operates "Data Center of the Rockies" in Casper, WY. Worth a separate HubSpot record check for MWT — that colo legitimately belongs as a Standard - colo on the parent. Flag for account-sourcing follow-up.
2. **News date format drift**: ~15 of the LIGHT-path records use `YYYY-MM:` prefix on `recent_news_or_trigger_event` instead of the canonical `[YYYY-MM-DD]`. Not blocking, but cosmetic cleanup opportunity for a future bulk-format pass.
3. **Smart City Telecom (297934868197)** has a hospitality-fiber niche (Disney + Orange County Convention Center exclusive since 2003). Currently Regional CLEC T3 — fits but could warrant a sub-segment carve-out if MaiaEdge sees more event/venue fiber operators. Not a problem this batch.

---

## Continuation token

```
SWEEP_NAME=2026-05-18-post-phase-3-framework
SWEEP_KICKOFF_DATE=2026-05-18
NEXT_BATCH=46
BATCH_SIZE=50
APOLLO_ENFORCEMENT=disabled
SEGMENT_SCOPE=all_active_icp
POOL_REMAINING=559
HOLD_POLICY=NONE (best-effort classify)
SORT=hs_object_id ASC
LAST_PROCESSED_HS_OBJECT_ID=297944750831
```
