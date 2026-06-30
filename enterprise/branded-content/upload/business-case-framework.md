# MaiaEdge Business Case Framework

Canonical framework for quantified, defensible business cases and the segment/account deliverables built on them. Single source of truth: the `branded-doc` skill (funnel stage 5), the `account-brief` skill, the post-call leave-behind business-case extension, and the `branded-content` enterprise project all point here. Do not duplicate this content elsewhere.

Segment-flex runs on the per-segment Pillar Framework, which lives canonically in `context/core/messaging-framework.md` (§ Cross-Segment Pillar Framework). Lead every business case with the account's segment pillars; never cross segments.

---

## A. Segment Business Case (any of the 6 ICPs)

A **10-section analytical deliverable** that quantifies the buyer's economics. Dense, defensible, built to be read by an operator's CFO or VP Network. Produce as a branded PDF (via `branded-doc`) OR as long-form markdown.

**The 10-section framework:**

1. **Executive Summary** - one paragraph: situation, pain, MaiaEdge approach, expected outcome.
2. **The Buyer's Situation** - segment-specific framing pulled from the segment cheatsheet (who they are, what they do, how the market currently treats them).
3. **Quantified Pain** - the status-quo cost (turn-up time, stranded capacity, deal loss, SLA penalties, manual coordination). Use real metrics from the segment cheatsheet + signal catalog where available; build defensible assumption tables otherwise.
4. **Status Quo Cost** - rough annualized $ cost of the pain (opportunity cost + direct + indirect).
5. **The MaiaEdge Approach** - carrier infrastructure positioning, the segment-specific pillar framework, "your team provisions in minutes" with ownership.
6. **Use Cases** - 3-5 use cases from `context/sales/use-case-taxonomy.md` that apply to this segment, each with a one-paragraph framing.
7. **ROI Model** - the math: turn-up time savings, new revenue from sub-10-min provisioning, monetization of stranded capacity, cloud on-ramp economics from `context/product/cloud-onramp-business-case.md` + `context/product/economic-impact-acg-whitepaper.md`. Build a defensible 3-scenario model: conservative / likely / optimistic.
8. **Risk + Mitigation** - operational, technical, competitive risk, and how MaiaEdge mitigates each.
9. **Implementation Path** - POC to production. 60-day POC framing, decision gates. Reference `context/hubspot/poc-schema.md` for structure.
10. **Decision Criteria + Next Steps** - what the buyer should evaluate, what we propose as the next step.

**Process:**

1. **Segment lock** - load the segment cheatsheet + `context/copy-strategy/segment-messaging.md` + `context/copy-strategy/segment-language.md`. Only this segment's vocabulary.
2. **Signal grounding** - pull cataloged signals from `context/signals/[segment]-signals.md` to anchor sections 2/3.
3. **Economics** - pull from `context/product/cloud-onramp-business-case.md` + `context/product/economic-impact-acg-whitepaper.md` + `context/sales/pricing-reference.md` + `context/sales/use-case-taxonomy.md`.
4. **Proof points** - pull from `context/product/proof-points.md` (anonymized) + `context/sales/edge-ai-thesis-montauk.md` (if neocloud / AI colo).
5. **Competitive frame** - pull from `context/core/competitive-positioning.md` + `context/core/differentiation-naas-aggregator.md`. Name competitors only in detailed sections, never headline copy.
6. **Author** - all 10 sections. Defensible math. No marketing fluff. The operator's CFO is the reader.
7. **Render (optional)** - if a branded PDF is requested, invoke the `branded-doc` skill.

---

## B. Account-Specific Business Case

Combines `account-brief` skill output with the segment business case framework. Pulls real HubSpot data for the account, current signals from the segment catalog, and produces a tailored 10-section deliverable for a named prospect.

1. **Account brief** - invoke `account-brief` for the named account.
2. **Segment business case** - run framework A for the account's segment.
3. **Tailor** - replace generic segment framing with account-specific signals, named pain from call intelligence, real deal history.
4. **ROI model** - use the account's actual scale (route miles, sites, GPU capacity, etc.) instead of segment averages.
5. **Next steps** - tie to the account's HubSpot deal stage and owner.
6. **Deliver** - branded PDF + supporting markdown.

**Heat + Tier sort (prioritizing account-specific business-case work):** sort the target list by `signal_heat` first (Hot / Warm / Cool / Cold), then by `account_tier`. Hot accounts get the writing budget first; cold high-tier accounts are strategic ABM targets (`hs_is_target_account = true`) and warrant the investment regardless of heat. Heat compute spec: `context/account-tiering/tier-compute-spec.md` §11.5. Tier is inverted: Tier 1 = highest priority.

---

## C. Slide-Deck Outline

The `branded-doc` skill renders PDFs, not PowerPoint/Keynote. For decks, produce:

1. **Slide-by-slide outline** following the brand visual system (palette, font, eyebrow numbering, peer-tone copy, no em dashes).
2. **Markdown source** for each slide the user can paste into a template.
3. **Design notes per slide** (color, layout, icon, the visual element that supports the message).

Reference `context/sales/golden-pitch-key-slides.md` for the existing deck's slide-by-slide structure; match that visual language.

---

## D. Business Case Rigor (non-negotiable)

- **Defensible math.** Cite the source for any number, or label it explicitly as an assumption with a sensitivity range.
- **Three scenarios.** Conservative / likely / optimistic. Never a single point estimate.
- **No marketing fluff.** The reader is an operator's CFO or VP Network; they discount anything that reads like a brochure.
- **Risk section is mandatory.** A business case without acknowledged risk reads as a sales pitch.
- **Implementation path tied to POC structure.** Reference `context/hubspot/poc-schema.md`. 60-day POC is the standard framing.
- **Earned-Problem framing for the buyer's situation.** Canonical: `context/outreach/email-writing-rules.md` § The Earned-Problem Doctrine. Frame the buyer's pain as the predictable challenge of their stated growth path ("as your AI workloads scale, the path between facilities becomes the bottleneck"), never as a verdict on their current setup. Run the offense test: would the operator's CFO read any line as "your network is bad"? If yes, reframe to forward-state.

## E. Common failures to avoid

| Failure | Fix |
|---|---|
| Generic segment framing (could apply to any operator) | Pull specific cataloged signals + the segment cheatsheet's "what's different" section |
| ROI math without an assumption table | Build a 3-scenario assumption table; cite source or label as assumption |
| Missing risk section (reads as a pitch) | Section 8 is mandatory: operational + technical + competitive risk |
| Cross-segment vocabulary (colo terms in a fiber case) | Run segment vocabulary lock before authoring; re-check every paragraph |
| Neocloud with operator-sovereignty language ("keep your customer") | They ARE the customer; lead with DETERMINISTIC / PRIVATE / INSTANT, data sovereignty only |
