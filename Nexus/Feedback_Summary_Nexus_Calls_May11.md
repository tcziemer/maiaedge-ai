# Feedback Summary: Nexus Hubbard -- May 11 Calls
**Prepared by:** Tim Ziemer  
**Date:** May 12, 2026  
**Source calls:** MaiaEdge/Pearce/Nexus alignment call (Mon 5/11 AM) + Pearce internal debrief (Mon 5/11)  
**Documents in scope:**  
- Nexus Hubbard IXP Contractor Engagement Pack v3  
- MaiaEdge_LNTP_DRAFT_2026-05-06 (Engineering Services Agreement)

---

## Part 1 -- Contractor Engagement Pack v3

These are the points we need to address in writing before the next Nexus touchpoint. The goal is to be helpful and specific without making Nick look underprepared in front of his investors.

### 1. Building Count Basis Needs to Be Declared

The document references three different building counts in close proximity: 4 buildings (Anthropic Phase 1), 9 buildings (Project Apex), and up to 65 buildings as the long-term expansion target. For the engineering services agreement and any downstream BOMs or procurement plans, we need Nexus to formally confirm whether the working basis is 4 or 9 buildings. The answer changes scope and hours materially. We should ask them to state this explicitly in their next response to us.

Nick suggested on the call that 9 may now be the operative number for Project Apex, but the LNTP Exhibit A still scopes Phase 1 as four buildings. We cannot sign off on deliverable timelines or BOM commitments until this is locked.

### 2. IXP Switching Fabric -- Scope and Source of Requirements (Arista, Ciena 6500, PVC Fabric)

Section 4.4 of the Engagement Pack references a BGP spine-leaf IXP switching fabric, and Section 4.5 references the Ciena 6500 RLS as an open line system. Separately, the meeting notes from our Monday morning call flagged references to Arista switching platforms and a PVC/optical fabric component (CNR 6500 variant) that none of us could trace back to a clear owner or decision.

We need Nexus to clarify:
- Who authored those IXP gear references and on what basis
- Whether the IXP switching fabric (Phase 2) is carrier-provided, Nexus-procured, or in scope for our engineering engagement
- Whether the Ciena 6500 / CNR 6500 references are placeholders or committed vendor selections

Until this is answered, we should treat these as open placeholders and say so explicitly in our feedback. We should not author a BOM or procurement recommendation around equipment whose ownership is still undetermined.

### 3. Design Basis -- Anthropic Building Plans Required Before Detailed Engineering Starts

Nick confirmed on the call that Nexus intends to cookie-cutter the Anthropic data hall design for the carrier hotel and meet-me room. That is sensible and simplifies engineering considerably. It also means that until we have access to those plans, we are working from assumptions rather than from a real design basis.

The feedback to Nexus should say clearly: our engineering services engagement and the timelines we have committed to in the LNTP assume we receive the Anthropic building design package (or a comparable reference design) at or near engagement kickoff. If that package is not available on Day 1, the T+4 and T+6 week deliverable targets slide accordingly.

Phrasing it this way protects Pearce and MaiaEdge without implying Nexus has failed to plan. Frame it as a standard design-build input protocol: we need X from Owner by date Y to hit milestone Z.

### 4. Responsibility Matrix (Section 7.7) -- MMR Scope Not Granular Enough

Nick acknowledged on the call that the carrier hotel and MMR section of the responsibility matrix is too high-level. He said he wanted help making it more specific, and that there are probably three to five major sub-categories within the MMR scope that need individual owner assignments.

Our feedback should offer to co-develop a more detailed interface block diagram and responsibility matrix for the MMR, covering at minimum: carrier fiber handoff at the vault/ODF, inside plant from vault to MMR, cage build-out and demarcation, cross-connect fabric (ODF to PBC), and the PBC integration layer. This is squarely in our lane and positions us well.

Suggested format: a simple color-coded block diagram (carrier scope in one color, Pearce/Michels in another, MaiaEdge in a third) with a companion matrix showing Engineering, Procurement, and Installation responsibility for each element.

### 5. MMR-2 Phasing

The document references a future carrier hotel expansion zone for MMR-2 (visible in the campus architecture diagram) but does not define when it would be built, what it would require, or how the Phase 1 design should accommodate it. If MMR-2 is a real possibility within the 5-year horizon, the conduit routing, cable plant sizing, and fiber distribution architecture for Phase 1 should be designed to accommodate it without major excavation.

We should flag this in feedback and ask Nexus to confirm whether MMR-2 should be a design consideration for the current engineering engagement or deferred.

### 6. Commissioning and O&M Stakeholders Not Reflected

The call confirmed that Inconnex is the commissioning provider and Salute is the O&M provider. Neither appears prominently in the Engagement Pack's contractor list or responsibility matrix. Since both of their requirements will influence design decisions (especially operator requirements for monitoring, labeling, physical plant standards, and acceptance criteria), they need to be looped into design reviews early.

Our feedback should recommend that Nexus confirm the correct legal entity names for both providers and include them in the next design review session.

---

## Part 2 -- Engineering Services Agreement (LNTP)

These are the changes we want to discuss with Abilash and our attorney before returning a redline to Nexus. Target: deliver a redline by May 12.

### 1. Budget Cap -- Revise from $500K to $1M

The draft LNTP caps the engagement at $500,000. Nick confirmed on the 5/11 call that $1M is defensible and likely acceptable to Nexus, provided we can justify the hours and the scope. He also noted precedent from similar projects (cooling, power engineering engagements on the same campus) where $1M is the established baseline for this type of work.

Our position should be to request the cap be revised to $1,000,000 (not to exceed), with monthly cost reporting against actuals. We commit to notify Nexus at 80% drawdown and to provide a scope-to-hours reconciliation in each monthly report. This protects both sides.

### 2. Deliverable Timelines Must Be Conditioned on Owner-Provided Inputs

Exhibit A commits to specific deliverables on a fixed schedule (T+2 weeks, T+4 weeks, T+6 weeks, T+12 weeks). Those timelines assume we receive from Nexus, on or around Day 1: the confirmed list of Phase 1 buildings, the Anthropic design package or equivalent reference design, existing infrastructure drawings, MMR location and dimensions, and the designated Owner technical point of contact.

The LNTP should include language that the target schedule in Exhibit A runs from the date we receive the last required Owner input, not from the contract execution date. We are not in a position to commit to T+4 LLD delivery if we are still waiting for basic design references three weeks in.

Suggested add to Exhibit A, Section 6 (Open Items): "Target schedule milestones are contingent on timely receipt of Owner-provided design inputs. Milestone dates shall be extended day-for-day for each calendar day that Owner-provided inputs required by the preceding milestone remain outstanding."

### 3. "Procurement-Ready Packages" Language Is Overcommitting

Exhibit A states that engineering services will "deliver procurement-ready packages for long-lead items within approximately twelve (12) weeks." This language was flagged hard on the Pearce side as a dangerous commitment. A procurement-ready BOM for thousands of ISP components across four to nine buildings requires a completed design basis, a full conduit path study, and IDF/MDF counts -- none of which exist yet.

We need to qualify this language. The commitment should be to identify and flag long-lead item categories and estimated quantities once design reaches sufficient maturity, not to deliver a complete procurement-ready BOM as a fixed 12-week deliverable. If Nexus pushes back, the response is: we can deliver procurement-ready packages in 12 weeks, but only if we receive the Owner design inputs by Day 1 and the design reviews proceed without rework cycles.

### 4. Exhibit B -- Billing Rates Still Blank

Exhibit B currently reads "[Contractor to Provide]." This needs to be populated before we return the redline. We should work with Pearce to agree on the rate card for their personnel and include MaiaEdge rates for the network engineering scope. The rate card should be valid through December 31, 2026 as the LNTP currently states.

### 5. "Cookie Cutter" Design Reference -- Protective Language

If Nexus intends to replicate the Anthropic building design, our agreement should acknowledge this explicitly. When one party's design standards (in this case, Anthropic's) will govern the deliverable, the engineering contractor's liability for design choices made by the owner's tenant should be limited. We should ask counsel to review whether any language in the LNTP inadvertently creates liability for design decisions that are not ours to make.

### 6. Termination for Convenience -- No Minimum Notice Period

Section 6 of the LNTP allows Nexus to terminate for convenience "immediately upon delivery of written notice." There is no minimum notice period and no demobilization fee. Given that our team will be mobilizing personnel and potentially subcontractors, we should ask for at minimum a 10-business-day notice period with a modest demobilization fee to cover committed costs. This is standard on professional services engagements of this size.

### 7. Insurance Limits -- Confirm Obtainability

Exhibit C requires Commercial General Liability at $5M per occurrence / $10M aggregate and an additional $5M Excess Liability policy. Before signing, Pearce and MaiaEdge should confirm with their respective brokers that these limits are obtainable at reasonable premium. If they are not standard for a company at our revenue scale, we will need to negotiate the limits down or request a waiver for the Excess layer.

---

## Summary of Next Steps

The two immediate deliverables are:

1. A short feedback response to Nick on the Engagement Pack -- 2 pages max, written in a tone that is collaborative and constructive. The goal is to give him specific things to go confirm internally, not to critique the document. Bill will reach out to Jim Salvato to get boilerplate language for the collaborative design engagement framing.

2. A redlined LNTP returned to Nexus -- primarily addressing the budget cap ($500K to $1M), the deliverable timeline conditionality, and the procurement-ready packages language. Abilash to align with attorney before sending.

Both should go to Nick by end of day May 12.
