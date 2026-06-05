# LMaaS Rapid Validation Tests
## Assumption Stress-Test Framework | March 2026 | Board Internal

---

## How to Use This Document

Each test targets one critical assumption behind the LMaaS strategy. For each test:

- **Assumption** -- what has to be true for LMaaS to work
- **Kill criteria** -- the result that would kill or materially damage the thesis
- **Pass criteria** -- the result that validates the assumption
- **Test method** -- the fastest way to get a definitive answer
- **Data source** -- who or what provides the answer
- **Owner** -- suggested person to run the test
- **Timeline** -- target days to completion
- **Status** -- Not started / In progress / Pass / Fail / Inconclusive

Tests are ordered by **dependency**: later tests assume earlier ones passed. The first four are existential -- if any fails, the model needs fundamental redesign.

---

## Tier 1: Existential Tests (Must Pass to Proceed)

### Test 1: Wholesale eLine Economics

**Assumption:** Fiber operators will sell eLines to MaiaEdge at wholesale rates that support the unit economics in the business case ($350-$550/mo for 500M-1G).

**Kill criteria:** Wholesale eLine pricing from 2+ fiber operators exceeds $700/mo for 1G, destroying the margin spread vs. Megaport equivalent ($1,000/mo). Or: fiber operators refuse to offer wholesale rates to a company with no existing circuit volume.

**Pass criteria:** At least 2 of 3 target fiber operators quote wholesale eLine rates at or below $550/mo for 1G, consistent with the Atlantech model.

**Test method:** Request indicative wholesale pricing from 3 fiber operators (Arvig, Segra, Atlantech) for 10-circuit bulk eLines in their metro footprints. Frame as "wholesale buyer evaluating bulk circuit purchase for managed service platform." No binding commitment needed -- indicative quotes are sufficient.

**Data source:** Fiber operator wholesale/carrier sales teams (not enterprise sales).

**Owner:** Timothy Ziemer / Abilash Menon (leverage existing relationships).

**Timeline:** 10-15 business days for indicative quotes.

---

### Test 2: Fiber Operator Long-Haul Profile

**Assumption:** A meaningful number of US fiber operators have the full "Arvig profile" -- metro fiber footprint + owned long-haul route to a major cloud exchange + existing rack/cage at the destination.

**Kill criteria:** Fewer than 5 US fiber operators have the full profile across the top 10 AWS Direct Connect metros. This means the cleanest version of the model (Leg 1 + Leg 2 from same operator) doesn't scale nationally.

**Pass criteria:** 8+ fiber operators identified with the full profile, covering at least 5 of the top 8 Direct Connect metros.

**Test method:** Build a matrix of the top 25 regional fiber operators by metro footprint. For each, research: (a) owned long-haul routes, (b) presence at Equinix/CoreSite/Cyrus One facilities, (c) rack/cage at cloud exchange locations. Start with publicly available route maps and interconnection directories, then validate with 3-4 phone calls.

**Data source:** Equinix/CoreSite interconnection directories (public), fiber operator route maps, PeeringDB, targeted outreach.

**Owner:** Timothy Ziemer (BD) + Cooper Kennedy (research support).

**Timeline:** 5-7 business days for desk research; 10-15 for phone validation.

---

### Test 3: Regulatory / Licensing Gatekeep

**Assumption:** LMaaS does not trigger CLEC licensing or telecom reseller requirements that would add 6-12 months of regulatory process before revenue.

**Kill criteria:** Outside counsel determines LMaaS requires state-by-state CLEC licensing or FCC authorization before offering service. This adds $50-100K in legal costs and 6-18 months of delay per state.

**Pass criteria:** Counsel confirms LMaaS can operate as a managed service / information service provider without CLEC/reseller licensing, or that a lightweight registration (not full CLEC) is sufficient and achievable in under 60 days.

**Test method:** Engage telecom regulatory counsel for a 2-hour assessment. Provide the three-leg architecture diagram and the commercial model (MaiaEdge buys wholesale circuits, bundles with PBC technology, sells managed service to enterprise). Key question: does this look like resale of telecom services, or delivery of a managed information service that happens to use telecom inputs?

**Data source:** Telecom regulatory attorney (Wiley Rein, Kelley Drye, or equivalent).

**Owner:** Timothy Ziemer (commission the opinion).

**Timeline:** 5-10 business days for initial assessment; 15-20 for written opinion.

---

### Test 4: Enterprise Willingness to Pay

**Assumption:** Enterprise customers will pay a bundled MRC for end-to-end managed private connectivity at or near Megaport-equivalent pricing ($800-$1,200/mo for 1G) rather than assembling their own solution.

**Kill criteria:** 5+ enterprise prospect conversations reveal that (a) they already have last-mile circuits they won't replace, (b) their IT procurement won't approve a new vendor category, or (c) price sensitivity is extreme -- they won't pay more than $500/mo for 1G cloud onramp regardless of the managed service wrapper.

**Pass criteria:** At least 3 of 8 enterprise prospects express clear buying intent at the proposed price range, with identified budget holders and a plausible 90-day purchase timeline.

**Test method:** Structured discovery calls with 8-10 enterprise prospects in the Ashburn metro area. Use existing HubSpot pipeline + Tim Lieto's territory relationships. Script the conversation around three questions: (1) How do you connect to AWS today and what does it cost? (2) Would a single-vendor, fully managed private path from your building to AWS at $X/mo be interesting? (3) Who approves this spend and what's the typical cycle?

**Data source:** Enterprise prospects in Ashburn metro (Tim Lieto pipeline).

**Owner:** Tim Lieto (calls) + Timothy Ziemer (analysis).

**Timeline:** 15-20 business days to complete 8 conversations.

---

## Tier 2: Model Viability Tests (Must Pass to Scale)

### Test 5: Wholesale Agreement Execution Speed

**Assumption:** A fiber operator wholesale agreement can be executed in under 90 days, enabling revenue within 6 months of Phase 1 kickoff.

**Kill criteria:** Legal/procurement cycles at target fiber operators exceed 6 months. Their wholesale teams require volume commitments MaiaEdge can't meet, or their contract templates impose liability terms that are unacceptable.

**Pass criteria:** At least 1 fiber operator confirms willingness to execute a master wholesale agreement within 60-90 days, with reasonable terms (no volume minimums above 10 circuits, standard telecom liability caps).

**Test method:** Initiate wholesale agreement discussions with the most receptive fiber operator (likely Atlantech given existing relationship). Request their standard wholesale template. Have MaiaEdge counsel redline. Measure the calendar time from first request to executable draft.

**Data source:** Atlantech wholesale/legal team; MaiaEdge counsel.

**Owner:** Timothy Ziemer.

**Timeline:** Run concurrently with Test 1. Measure elapsed time -- the test result IS the timeline.

---

### Test 6: Operational Lift Reality Check

**Assumption:** MaiaEdge can stand up minimum viable service provider operations (provisioning, billing, SLA management, customer support) for Phase 1 without hiring more than 1-2 additional heads.

**Kill criteria:** Operational analysis reveals that Phase 1 requires a billing platform ($100K+), a 24/7 NOC, or 4+ additional hires before first customer -- making the working capital requirement 3-5x the business case estimate.

**Pass criteria:** A credible Phase 1 operations plan exists that uses existing tools (HubSpot for CRM, lightweight billing like Stripe/Chargebee, existing engineering for provisioning) with 1-2 additional hires (provisioning ops + customer success).

**Test method:** Map every operational process required for a single LMaaS customer end-to-end: order intake, fiber operator circuit ordering, PBC provisioning, billing, SLA monitoring, trouble ticketing, and renewal. For each process, identify: can it be done manually at Phase 1 scale (10-20 customers)? What breaks at 50 customers? What breaks at 200?

**Data source:** Internal (Kyle Blackwell for provisioning, Cooper Kennedy for billing/CRM).

**Owner:** Cooper Kennedy (ops mapping) + Kyle Blackwell (technical provisioning).

**Timeline:** 5-7 business days.

---

### Test 7: Channel Conflict Assessment

**Assumption:** Existing PBC subscription partners (especially Atlantech) will accept geographic segmentation without damaging the relationship.

**Kill criteria:** Atlantech or other key partners indicate they would view LMaaS in Ashburn as a competitive threat and would reconsider their PBC relationship. Or: partner agreements contain exclusivity language that prohibits MaiaEdge from offering services in overlapping markets.

**Pass criteria:** Atlantech confirms (formally or informally) that MaiaEdge operating LMaaS in defined hub markets does not conflict with their plans, especially if MaiaEdge offers them the wholesale supply role (selling eLines to MaiaEdge in their footprint).

**Test method:** Review existing partner agreements for exclusivity or non-compete clauses. Then have a candid conversation with the Atlantech relationship owner. Frame: "We're considering offering a managed service in major hubs where we'd buy wholesale eLines from you. You'd earn recurring circuit revenue. You'd continue to own secondary markets with PBC subscriptions. Does this work for you?"

**Data source:** Existing partner agreements (legal review) + Atlantech relationship owner.

**Owner:** Timothy Ziemer (conversation) + counsel (agreement review).

**Timeline:** 3-5 business days for agreement review; conversation within 10 days.

---

### Test 8: AWS Interconnect Last Mile Competitive Timeline

**Assumption:** AWS Interconnect Last Mile will remain in gated preview long enough (12-18 months) for MaiaEdge to establish fiber operator relationships and build network effects before it becomes broadly available.

**Kill criteria:** AWS announces general availability of Interconnect Last Mile with 5+ carrier partners within the next 6 months, covering the same top metros MaiaEdge is targeting. This compresses the window to near-zero.

**Pass criteria:** AWS Interconnect remains in gated preview through Q4 2026 with limited carrier partners (Lumen + AT&T only), giving MaiaEdge 12+ months to build the federated network before the point solution matures.

**Test method:** (a) Monitor AWS announcements and re:Invent previews. (b) Talk to 2-3 AWS partner network contacts to understand the GA timeline and carrier onboarding pipeline. (c) Talk to 1-2 Lumen contacts to understand their experience with the preview -- is it smooth or struggling?

**Data source:** AWS Partner Network contacts, Lumen contacts, public AWS announcements.

**Owner:** Abilash Menon (AWS relationships) + Timothy Ziemer.

**Timeline:** Ongoing monitoring; initial intelligence within 10 business days.

---

## Tier 3: Scale Tests (Must Pass Before Phase 2)

### Test 9: DIA Tier Viability for Non-Long-Haul Markets

**Assumption:** For markets where the fiber operator lacks owned long-haul to a cloud exchange, a DIA-based Leg 2 can deliver acceptable latency and reliability at a price point that still supports the business case.

**Kill criteria:** DIA-based Leg 2 adds >5ms latency variability and reduces the service to "good enough" rather than "deterministic" -- undermining the core differentiation. Or: DIA Leg 2 cost exceeds $400/mo, destroying margins for the lower-tier product.

**Pass criteria:** DIA Leg 2 delivers <3ms additional latency with <1ms jitter in test markets, at a cost that supports a viable (if lower-margin) product tier.

**Test method:** Use IENTC's existing Mexico-Miami DIA deployment as a benchmark (22ms confirmed). Deploy a test circuit in one non-long-haul market and measure latency, jitter, and packet loss over a 30-day period.

**Data source:** IENTC performance data + new test circuit measurements.

**Owner:** Kyle Blackwell (engineering).

**Timeline:** 30 days (Phase 2 prerequisite, not Phase 1 blocker).

---

### Test 10: NeoCloud GTM Receptivity

**Assumption:** NeoCloud providers will view MaiaEdge's LMaaS fabric as a valuable enterprise access layer and will co-market or refer enterprise customers.

**Kill criteria:** 3+ NeoCloud conversations reveal they see no value in private last-mile connectivity (their customers don't ask for it), or they're building their own connectivity solutions, or they won't engage without MaiaEdge having 50+ enterprise customers first.

**Pass criteria:** At least 1 NeoCloud provider (Datum.net, Together.ai, or RunPod) agrees to a pilot where their enterprise customers can access GPU clusters through the MaiaEdge fabric, with a defined referral or co-marketing arrangement.

**Test method:** Structured conversations with 3-5 NeoCloud providers. Lead with: "Your enterprise customers are paying 20-40% egress premiums and connecting over public internet. We can deliver them to you on private, dedicated paths with guaranteed latency. Would your sales team position this as a feature?"

**Data source:** NeoCloud provider BD/partnerships teams.

**Owner:** Timothy Ziemer + Abilash Menon.

**Timeline:** 15-20 business days.

---

## Execution Dashboard

| # | Test | Timeline | Owner | Dependency | Status |
|---|------|----------|-------|------------|--------|
| 1 | Wholesale eLine Economics | 10-15 days | TZ/AM | None | Not started |
| 2 | Fiber Operator Long-Haul Profile | 5-15 days | TZ/CK | None | Not started |
| 3 | Regulatory / Licensing | 5-20 days | TZ | None | Not started |
| 4 | Enterprise Willingness to Pay | 15-20 days | TL/TZ | None | Not started |
| 5 | Wholesale Agreement Speed | 60-90 days | TZ | Test 1 pass | Not started |
| 6 | Operational Lift | 5-7 days | CK/KB | None | Not started |
| 7 | Channel Conflict | 3-10 days | TZ | None | Not started |
| 8 | AWS Competitive Timeline | 10 days + ongoing | AM/TZ | None | Not started |
| 9 | DIA Tier Viability | 30 days | KB | Phase 2 gate | Not started |
| 10 | NeoCloud GTM Receptivity | 15-20 days | TZ/AM | Phase 2 gate | Not started |

**Critical path:** Tests 1-4 run in parallel. All four must pass before committing capital to Phase 1. Tests 5-8 run concurrently during the first 30 days. Tests 9-10 are Phase 2 prerequisites.

**Total time to go/no-go decision on Phase 1: approximately 20 business days** (4 calendar weeks) if tests run in parallel.

---

## Decision Framework

**Green light for Phase 1:** Tests 1-4 all pass. No Tier 1 test returns a kill result.

**Conditional proceed:** 3 of 4 Tier 1 tests pass, and the failing test has a credible workaround (e.g., Test 2 shows fewer operators than hoped, but enough for 3 metros).

**Redesign required:** 2+ Tier 1 tests fail. The core model needs structural changes before capital commitment.

**Kill:** Test 3 (regulatory) returns a hard fail requiring CLEC licensing in target states, or Test 1 shows wholesale economics that don't work and can't be renegotiated.

---

*Prepared March 2026. For MaiaEdge Board internal use.*
