# Sub-Segment Qualification (Pointer)

**Status:** Pointer file. The single source of truth for sub-segment classification logic is the full reference:

> `context/account-tiering/sub-segment-qualification-full.md` (the consolidated file, formerly "file 06")

It carries §3 D1 global disqualifiers, §4 D2 wholesale-arm policy, §5 D3 disambiguation flowcharts (all 6 ICPs), §6 per-sub-segment anchor lists + confidence rules, §7 Greenfield migration patterns, §8 industry sources. Companion working docs in the same folder: `d1-global-disqualifiers.md`, `d2-wholesale-arm-policy.md`, `d3-disambiguation-flowcharts.md`, `icp-deep-dives/` (6 B-and-C deep-dives per ICP).

Every skill that classifies records (R1 Fresh Enrichment, R2 Stale Re-Enrichment, Weekly Signal Scan, R-Tier-Audit, D7 Edge Case Resolution, `segment-classification`, `edge-case-researcher`, `company-enrichment`, `import-processor`, `account-sourcing`) reads this pointer first and then loads the full reference for deep-dive content. This file is intentionally short so skills do not each duplicate the 30-row sub-segment table.

## The 30 active sub-segments (verified via HubSpot MCP 2026-05-14)

Internal values are CASE-SENSITIVE. See `context/hubspot/hubspot-values.md` for the case-sensitivity quirks.

### Network Operator(Tier 1 / VNO) - 5 sub-segments

- `Tier 1 Carrier - Network Op`
- `Pure Wholesale Carrier - Network Op`
- `Cable MSO Enterprise Division - Network Op`
- `International Backbone Specialist - Network Op`
- `Subsea cable operator` (new 2026-05-14; no `- Network Op` suffix)

### Fiber Operator - 6 sub-segments

- `Regional CLEC - Fiber operator`
- `Long Haul / Backbone - Fiber operator`
- `Dark Fiber Specialist - Fiber Operator` (capital "O")
- `Tier 2 National Wholesale - Fiber operator`
- `Regional Cable Operator - Fiber operator`
- `Municipal / Cooperative - Fiber operator`

### Data Center Colo Provider - 4 sub-segments

- `Standard - colo`
- `AI Signals - colo`
- `Modular - colo`
- `Hyperscale Wholesale - colo`

### NeoCloud - 5 sub-segments

- `Large Scale GPU - Neocloud`
- `Tier 1 Inference - Neocloud`
- `AI Infrastructure providers - Neocloud` (lowercase "p")
- `Sovereign AI Clouds - Neocloud`
- `Crypto to AI - Neoclouds` (trailing "s")

### MSP/Aggregator - 5 sub-segments

- `Telecom Aggregator - MSP`
- `Managed Network Services - MSP` (`- MSP` suffix post-Phase 1.7c.1)
- `TSD Technology Services Distributor - MSP`
- `Master Agent - MSP`
- `Cloud + Telecom Hybrid MSP - MSP`

### Enterprise-CustomerSegment - 4 sub-segments

- `Financial Services - Enterprise`
- `Healthcare Systems - Enterprise`
- `Retail and Distribution - Enterprise`
- `Outsourcing Services - Enterprise`

### Cross-segment - 1 sub-segment

- `Greenfield` - REAL sub-segment per Cooper feedback 2026-05-14. Pairs with EITHER `Data Center Colo Provider` OR `NeoCloud` customer_segment parent. For actively-being-built colocation and neocloud companies (Series A-C funded, sites under construction). Auto-migration rule: R2 reclassifies into the operational sub-segment when the first operational site goes live.

**Total active: 30.**

## Retired (archived 2026-05-13, Phase 1.6 - DO NOT USE)

- `Co-op/consortium` (renamed to `Municipal / Cooperative - Fiber operator`)
- `External Extension - Network operator` (migrated to `network_op_track` field)
- `Internal + external unification - Network Operator` (migrated to `network_op_track` field)

`import-processor` rejects writes to these values with a clear error message.

## What file 06 contains (read for full content)

| File 06 section | Topic |
|---|---|
| §1 | Executive summary |
| §2 | Live HubSpot enum state (30 values verified 2026-05-14) |
| §3 | Global disqualifiers (D1) - applied BEFORE sub-segment routing |
| §4 | Wholesale-arm-vs-parent policy (D2) |
| §5 | Per-ICP disambiguation flowcharts (D3) - 6 flowcharts, all <=7 decisions deep |
| §6 | Per-sub-segment deep dives - definitions, quantitative markers, anchors, confidence rules. Full 12-section deep-dives in `context/account-tiering/icp-deep-dives/B-and-C-{icp}.md` |
| §7 | Contact persona mapping (30 sub-segments x 4 personas) |
| §8 | Industry taxonomy alignment (FCC BDC, PeeringDB, Synergy Research, Omdia TSD, NAICS, etc.) |
| §9 | At-scale classification readiness assessment (D4) + D5 operational layer |
| §10 | Recommended Phase 3 deliverables |

## Quarterly anchor refresh

Per Cooper RevOps calendar, the anchor lists in file 06 §6 are re-validated quarterly. Next refresh: 2026-08-14.

## See-also

- `context/account-tiering/tier-compute-spec.md` - tier computation algorithm; reads `(customer_segment, company_sub_segment)` produced by D3+D5
- `context/account-tiering/enrichment-protocols.md` - operational D5 v2 protocols (5-stage research-first workflow + per-sub-segment evidence questions)
- `context/hubspot/property-schema.md` - full property schema with case-sensitivity reference
- `context/hubspot/hubspot-values.md` - exact internal value reference
