# D2 — Wholesale arm vs parent entity policy

**Problem:** Major incumbent telecoms operate named wholesale arms with distinct brands, websites, and sales orgs. Example pairs:

- Orange S.A. (parent, Tier 1 Carrier) vs Orange Wholesale International (the wholesale arm)
- NTT Group (parent, Tier 1 Carrier) vs NTT Communications wholesale arm vs NTT Global Data Centers (separate colo entity)
- BT Group (parent, Tier 1 Carrier) vs BT Wholesale vs BT Global (enterprise + international)
- Telstra (parent, Tier 1 Carrier) vs Telstra International (International Backbone Specialist)
- Telecom Italia (parent, Tier 1 Carrier) vs Sparkle (international wholesale)
- Bharti Airtel (parent, Tier 1 Carrier for India) vs Bharti Airtel International (International Backbone Specialist)
- Deutsche Telekom (parent, Tier 1 Carrier) vs T Wholesale vs Deutsche Telekom Global Carrier
- Tata Communications (the parent IS the wholesale/international vehicle; rare structurally)
- Lumen Technologies (parent) vs Lumen Wholesale book (not a separate entity post-divestiture)

Phase 2 ran into this with the 263 target_account international wholesale arms held on Network Op. The corrective pass classified them as `Tier 1 Carrier - Network Op` rather than demoting to Fiber Operator. That ad-hoc decision needs a policy.

## Policy (proposed)

### Default: One HubSpot record per legal entity that has its own DUNS / tax ID

| Scenario | Action |
|---|---|
| Parent and wholesale arm share legal entity (no separate DUNS) | **One record** under the parent legal name. The wholesale activity is a buying motion, captured in `network_op_track` (typically `external_extension`) and notes — not a separate record. |
| Wholesale arm is a separately-incorporated subsidiary with its own DUNS / tax ID | **Two records.** Parent + wholesale subsidiary. Cross-link via HubSpot association. Tier separately based on each entity's own scale. |
| Joint venture (Console Connect-style) | **Separate record** for the JV. Parent record stays under its primary sub-segment. |

### Sub-segment assignment when two records exist

For the parent record:
- If the parent has retail + enterprise + wholesale + international: `Tier 1 Carrier - Network Op`
- If the parent has lost retail and only operates wholesale today (post-Sparkle-sale-to-state scenario): `Pure Wholesale Carrier - Network Op`

For the wholesale-arm record:
- If the arm is primarily international wholesale: `International Backbone Specialist - Network Op`
- If the arm is primarily domestic wholesale IP transit / Tier 1 routing: `Pure Wholesale Carrier - Network Op`
- If the arm is metro/regional dark fiber: `Tier 2 National Wholesale - Fiber operator` (it's a Fiber sub-segment despite the carrier brand)

### Tier assignment

Each record gets its own tier per the framework. The parent typically lands at Tier 1 (Tier 1 Carrier default). The wholesale arm may land at Tier 1 or Tier 2 depending on its own scale.

`hs_is_target_account` can be set independently on each record. If a sales motion targets the parent's enterprise division, the parent record is the target. If targeting the wholesale division (e.g., for a federated-fabric partnership), the wholesale arm is the target.

### Confidence reasoning

For records where the entity is ambiguous (e.g., the HubSpot record is named "Tata Communications" — which IS the parent that primarily IS the wholesale arm), set `segmentation_confidence = manual_review_required` AND note in HubSpot reasoning string: "Wholesale arm ambiguity per D2 — pending decision on parent vs wholesale-arm record structure."

### Specific entity decisions (canonical list)

| Entity | HubSpot record | Sub-segment | Notes |
|---|---|---|---|
| Orange S.A. | Single record under Orange | Tier 1 Carrier - Network Op | Wholesale activity captured via `network_op_track = external_extension` |
| Orange Wholesale International | Separate record IF found in HubSpot with own contact set | International Backbone Specialist - Network Op | Cross-link to parent |
| NTT Group | Single record under NTT | Tier 1 Carrier - Network Op | |
| NTT Global Data Centers | **Separate record** (already exists per Phase 2 audit) | `AI Signals - colo` or `Hyperscale Wholesale - colo` per ownership/customer mix | Distinct legal entity per Cooper notes |
| NTT Communications wholesale | If separate record exists | International Backbone Specialist - Network Op | Cross-link |
| BT Group | Single | Tier 1 Carrier - Network Op | |
| BT Wholesale | Separate record if in HubSpot | Pure Wholesale Carrier - Network Op | |
| Telstra | Single | Tier 1 Carrier - Network Op | |
| Telstra International | Separate | International Backbone Specialist - Network Op | |
| Telecom Italia (TIM) | Single | Tier 1 Carrier - Network Op | |
| Sparkle (TIM) | Separate (pending Italian state sale H1 2026) | International Backbone Specialist - Network Op | Flag for review post-close; record may remain under Sparkle or merge into state-owned vehicle |
| Bharti Airtel (India/Africa) | Single | Tier 1 Carrier - Network Op | |
| Bharti Airtel International | Separate | International Backbone Specialist - Network Op | Cross-link |
| Deutsche Telekom | Single | Tier 1 Carrier - Network Op | T Wholesale + Deutsche Telekom Global Carrier are usually subsumed |
| T-Mobile US | Separate | Tier 1 Carrier - Network Op | Distinct legal entity (DT-majority-owned); mobile-first per Network Op Phase B findings — flag for `manual_review_required` on classification |
| Tata Communications | Single | International Backbone Specialist - Network Op (primary) | Manual review per file 05 |
| Spectrum | Single | Cable MSO Enterprise Division - Network Op | |
| Spectrum Enterprise | Per Phase 2 audit, separate record exists | Cable MSO Enterprise Division - Network Op | Cross-link to Spectrum parent |
| Comcast | Separate from Comcast Business | Cable MSO Enterprise Division - Network Op | |
| Comcast Business | Already separate | Cable MSO Enterprise Division - Network Op | Cross-link |
| Verizon | Per Phase 2 audit, duplicate of "Verizon Enterprise" | Tier 1 Carrier - Network Op | Recommend dedup |
| Verizon Enterprise | Same | Same | Same |
| Vodafone Group plc | Per Phase 2 audit, separate from Vodafone UK | Tier 1 Carrier - Network Op | Vodafone UK is the retail UK operator; Vodafone Group is the global parent — both can stand |
| Vodafone UK | Same | Tier 1 Carrier - Network Op | |
| China Telecom | Separate from China Telecom Global | Tier 1 Carrier - Network Op | |
| China Telecom Global | Already separate | International Backbone Specialist - Network Op | |
| Lumen Technologies | Single record | Tier 1 Carrier - Network Op (post-divestitures, drifting toward Pure Wholesale — flag for manual review at next quarterly anchor refresh per Network Op Phase B findings) | |

### Dedup recommendation

The Phase 2 audit flagged Verizon/Verizon Enterprise + Vodafone UK/Vodafone Group + China Telecom/China Telecom Global + NTT/NTT Global Data Centers as duplicate-pair candidates. **Run Routine 3 (Duplicate Accounts) over Tier 1 records to validate or merge.** The Wholesale Arm Policy distinguishes legitimate two-record cases (legal entity separation) from accidental duplicates (same DUNS).

### Encoding in skills

- `segment-classification/SKILL.md`: Add a "Wholesale arm check" decision step after parent identification. Logic: if the record name contains "{Parent} Wholesale", "{Parent} International", "{Parent} Global", check whether parent has its own record. If yes, classify the wholesale record per its primary activity; if no, classify both as combined entity under the parent's sub-segment.
- `company-enrichment/SKILL.md`: Stage 2 (web research) should explicitly check "is this a wholesale arm of a larger entity?" and capture parent name in a note for HubSpot reasoning string.
- `crm-hygiene/SKILL.md`: Flag any record where both parent and a named wholesale arm appear, for cross-link verification.

### When the policy conflicts with `hs_is_target_account` semantics

`hs_is_target_account = true` freezes `account_tier` only (per Phase 3 v3 master prompt). Wholesale-arm classification (this policy) operates on `customer_segment` and `company_sub_segment`, which are NOT frozen by the target_account flag. So D2 reclassifications proceed regardless of target_account status — only tier writes are held.
