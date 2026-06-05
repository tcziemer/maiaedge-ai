# Engineering Services Budget Scenarios: $500K vs $1M
**Nexus Hubbard -- Multi-Building Connectivity Architecture**  
**Prepared by:** MaiaEdge / Pearce  
**Date:** May 12, 2026  
**Reference:** MaiaEdge_LNTP_DRAFT_2026-05-06, Exhibit A

---

## Framing

The LNTP scope as written commits to six distinct deliverable categories across a 12-week engagement: baseline architecture assumptions, Phase 1 LLD for four buildings, a procurement-ready BOM with long-lead identification, an expansion architecture to 65 buildings, interface coordination across carriers and contractors, and a construction-ready handoff package that supports GMP conversion. The budget cap determines how many qualified engineers we can field, for how long, and how deeply we can work each deliverable. The scenarios below are built on the rate assumptions and staffing models described under the methodology note.

**Methodology note:** The analysis uses a blended bill rate of approximately $185/hr for the combined MaiaEdge/Pearce engineering team, reflecting a mix of principal architects, senior network engineers, design engineers, and project management. At that rate, $500K purchases roughly 2,700 billable hours and $1M purchases roughly 5,400 hours. Travel and out-of-pocket expenses are excluded from hour counts and assumed to consume 5-8% of each budget.

---

## Scenario A: $500,000 Cap

### Team Composition (12 weeks)
At $500K, after reserving approximately $35K for travel and third-party costs, the billable hour pool is roughly 2,500 hours. A realistic 12-week team configuration at that budget:

- 1 Lead Network Architect (50% time)
- 1 Senior Design Engineer (75% time)
- 1 Project Manager / Coordination Lead (50% time)
- Pearce ISP/OSP contribution (limited to 20% time, ~1 engineer)

This is a lean two-person-equivalent engagement. It can move fast on a narrow scope but has very limited capacity for parallel workstreams.

### What Gets Delivered by Day 90

**Baseline Architecture and Interface Documents (T+2):** Deliverable is achievable at $500K. The kickoff, technical input request, and baseline assumptions document are straightforward to produce. This milestone is not budget-sensitive.

**Phase 1 LLD -- Four Buildings (T+4):** Achievable, but with constraints. The MMR and carrier hotel architecture can be designed to a competent LLD. Per-building connectivity and interbuilding fiber mesh design will be completed for the four Anthropic buildings, but depth of documentation and peer review will be limited. Design review cycles with Nexus will need to be efficient; there is no budget cushion for significant rework iterations. If Owner inputs (Anthropic building plans, MMR dimensions, confirmed power/cooling specs) arrive late, this milestone slips and the remaining schedule compresses.

**BOM, MTO, and Long-Lead Identification (T+6):** This is where $500K begins to show strain. A well-structured BOM for four buildings of ISP and network infrastructure -- covering fiber distribution panels, ODF frames, rack and cabinet specifications, PBC hardware, cabling, and associated hardware -- can take several hundred hours to produce at the component level. At $500K, the BOM delivered at T+6 weeks will be a high-confidence estimate of major categories and quantities, but it will not be a line-item procurement-ready package. Long-lead items (ODF frames, specialty fiber, active optical equipment) can be flagged and ranked by lead time, which is the most critical risk-mitigation output. Detailed vendor-level specs and data sheets will be preliminary, not final.

**Expansion Architecture to 65 Buildings (T+8):** At $500K, this becomes a reference architecture document with conceptual fiber expansion models rather than a fully engineered buildout plan. The scalable topology and modular template will be defined, but capacity planning assumptions will be directional rather than validated by detailed design work. This is adequate for investment narrative purposes but would require significant additional engineering before it could support procurement or construction decisions.

**Construction-Ready Handoff Package (T+12):** The Phase 1 handoff package will be structurally complete -- site installation sequences, high-level cost model, per-building duration estimates -- but the cost basis supporting GMP conversion will carry wider uncertainty bands than ideal. GMP conversion at 60% design is Nexus's stated goal; at $500K and four buildings, the 60% threshold may be reachable, but it will depend heavily on the quality and timeliness of Owner-provided design inputs. If inputs are delayed even two to three weeks, the T+12 construction-ready package arrives at the GMP conversation with gaps that will slow Nexus's downstream contracting.

### Day 90 State at $500K
Phase 1 four-building LLD is complete and defensible. Long-lead item categories are identified but not fully spec'd for purchase orders. The expansion architecture is conceptual. GMP conversion is possible but will require Nexus to accept wider uncertainty in the cost basis. Procurement for long-lead items can begin in parallel with finalizing specs, but PO placement will likely trail the 90-day mark by four to six weeks.

**Risk:** Scope is tightly scoped to four buildings. If Nexus confirms nine buildings as the working basis (Project Apex), $500K is insufficient and the engagement either narrows to a subset of the nine-building scope or requires budget amendment before reaching T+6.

---

## Scenario B: $1,000,000 Cap

### Team Composition (12 weeks)
At $1M, after reserving approximately $60K for travel, third-party review, and out-of-pocket costs, the billable hour pool is approximately 5,100 hours. A realistic 12-week team configuration:

- 1 Lead Network Architect (full time)
- 2 Senior Design Engineers (full time)
- 1 Pearce ISP/Physical Layer Lead (full time)
- 1 Project Manager / Coordination Lead (75% time)
- 1 Technical Documentation Engineer (50% time)

This is effectively a five-person engagement with parallel workstreams running simultaneously. Design, documentation, and coordination can proceed in parallel rather than sequentially.

### What Gets Delivered by Day 90

**Baseline Architecture and Interface Documents (T+2):** Same as Scenario A. This milestone is straightforward and not budget-sensitive.

**Phase 1 LLD -- Four Buildings (T+4):** Delivered with greater depth. The LLD package includes the full MMR and carrier hotel architecture, per-building connectivity design, interbuilding fiber mesh, and a detailed interface block diagram showing responsibility handoffs by contractor. At this budget, design review cycles with Nexus, Michels, and AppWell can be accommodated without compressing the schedule. If the Anthropic building plans are used as a design template (the cookie-cutter approach Nick described), the LLD for buildings two through four can be parallelized with the lead architect's review rather than serialized.

**BOM, MTO, and Long-Lead Identification (T+6):** This is the most meaningful difference between the two scenarios. At $1M, the BOM delivered at T+6 is a genuine procurement-ready package: component-level for major categories, with manufacturer and model specifications, estimated quantities per building, and lead time ranges by item. The Pearce physical layer lead can build out the ISP BOM (fiber distribution panels, racks, cabinets, pre-terminated cable, IDF/MDF hardware) in parallel with the MaiaEdge team building the network active equipment BOM (PBC hardware, ODF frames, optical components). Long-lead items are not just flagged -- they come with recommended order timing relative to the Q4 2026 / Q1 2027 MMR go-live target. This is the output that allows Nexus to actually place purchase orders inside the 90-day window, which is their stated risk-mitigation objective.

**Expansion Architecture to 65 Buildings (T+8):** The expansion document at $1M is an engineered reference architecture, not a narrative framework. It includes a validated fiber expansion model, buildout templates at the per-building level, a capacity planning model with assumptions and sensitivities, and modular design patterns that Nexus can hand to any future engineering team without re-sourcing the design rationale. This document becomes a durable asset for investor and lender diligence, not just a contractor alignment tool.

**Construction-Ready Handoff Package (T+12):** The Phase 1 handoff package is complete and GMP-ready. The cost model carries defensible unit costs, validated against current vendor pricing from the BOM work. Per-building installation duration estimates are grounded in the physical design rather than rule-of-thumb benchmarks. The cost basis package supports Nexus's selection of a GMP, NTE, or alternative commercial structure with sufficient specificity to hold up in lender review. GMP conversion at 60% design -- Nexus's stated threshold -- is achievable within the 90-day window.

### Day 90 State at $1M
Phase 1 four-building LLD is complete and construction-ready. The BOM for long-lead items is procurement-ready, and Nexus can place purchase orders with reasonable confidence during Q4 2026. The expansion architecture is engineered to a level that supports investor and lender diligence. GMP conversion is on track. If Nexus confirms nine buildings as the working basis, the $1M envelope can absorb a modest scope expansion on the expansion architecture deliverable (T+8) without amending the agreement, provided the Phase 1 LLD scope remains at four buildings.

**Risk:** The $1M scenario still depends on receiving Owner design inputs at or near engagement kickoff. A three-week delay in the Anthropic building plans or MMR specifications will compress the T+4 through T+6 deliverables into a shorter window. At five engineers, there is more capacity to absorb that compression than at Scenario A's team size, but it is not unlimited.

---

## Side-by-Side Comparison

| Deliverable | $500K Outcome | $1M Outcome |
|---|---|---|
| Baseline Architecture Document (T+2) | Complete | Complete |
| Phase 1 LLD -- 4 buildings (T+4) | Complete, limited review cycles | Complete, parallel workstreams, peer-reviewed |
| BOM / Long-Lead Identification (T+6) | High-level categories flagged; not procurement-ready | Component-level, procurement-ready; POs can be placed |
| Expansion Architecture (T+8) | Conceptual framework | Engineered reference architecture; supports investor diligence |
| Construction-Ready Handoff (T+12) | Structurally complete; wider cost uncertainty | GMP-ready; defensible unit costs and duration estimates |
| GMP Conversion at 60% Design | Possible; cost basis carries risk | On track; cost basis is defensible |
| 9-Building Scope Absorption | Not feasible without amendment | Manageable on expansion architecture deliverable |
| Long-Lead PO Timing | 4-6 weeks after Day 90 | Within Day 90 window |

---

## Recommendation

The $1M engagement is the right structure for this project. The practical difference between the two scenarios is not effort level -- it is whether Nexus can place long-lead purchase orders during the 90-day window or six weeks after it. That timing gap directly affects their Q4 2026 / Q1 2027 MMR go-live target. Given that Nexus has explicitly stated the engagement is schedule-driven rather than budget-driven, the additional $500K is best understood as schedule insurance, not cost padding.

The $500K scenario is defensible if Nexus confirms a strict four-building scope and is prepared to accept a BOM that needs one to two additional weeks of refinement before it supports procurement-ready POs. It is not defensible if the working basis shifts to nine buildings, or if Owner design inputs arrive with any meaningful delay.

In either scenario, the budget should be structured as a not-to-exceed with monthly cost reporting and an 80% drawdown notification, as the LNTP draft prescribes. The actual spend may well come in below the cap -- particularly if the Anthropic cookie-cutter design simplifies the per-building LLD work materially -- but holding the cap at $1M preserves optionality if the scope expands or input delays create rework cycles.
