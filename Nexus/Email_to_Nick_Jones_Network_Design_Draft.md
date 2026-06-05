**To:** Nick Jones <nick@nexus-datacenters.com>
**Cc:** Ben Heichelbech <benh@nexus-datacenters.com>
**Subject:** Nexus Hubbard Carrier Hotel — Initial Network Design Draft

---

Nick,

Good talking to you as well — glad the timing works.

As promised, please find attached the initial draft of the **Nexus Carrier Hotel (MMR) and Data Center Connectivity Design**. It's aligned to the Fiber & Interconnection Strategy and the Carrier Hotel Basis of Design you shared last week, and is sized for the Phase 1 footprint with room to scale.

A few highlights to orient your review:

- **Two-domain architecture** — Carrier Hotel / MMR as the interconnection domain, Nexus buildings as the consumption domain, with a clean handoff between them.
- **MMR signal flow** — carrier dark fiber → carrier cage optical device → carrier patch panel → MMR ODF cross-connect → MaiaEdge patch panel → Path Border Controller (PBC).
- **Building extension** — diverse A/B dark fiber paths from the MMR into each Nexus building, landing in the IDF/ZDA, through dual MaiaEdge PBC cages, into the leaf/spine fabric and client workloads.
- **Scale & redundancy** — repeatable, modular model that accommodates the 18 carriers identified today with headroom to add more as demand grows, and scales from the initial 4 buildings to 18, with dual PBCs and independent physical routing to eliminate single points of failure.
- **End-to-end diagram** — multi-building view showing the MMR connected to four Nexus data centers over diverse dark fiber, suitable for the financing conversation.

This is a first revision intended to anchor the discussion — happy to iterate on any section, add detail where it's useful for your stakeholders, or adjust terminology to match the Basis of Design conventions. The document is marked MaiaEdge Confidential; please share internally and with financing stakeholders as needed.

If it's helpful, I'm glad to walk you and the team through it on a short call this week. Just let me know what works.

Regards,

Tim

Tim Ziemer
CRO / Co-founder
+1 (612) 840-2493
timziemer@maiaedge.io
77 S. Bedford St. Suite #150
Burlington, MA 01803 | maiaedge.io

*Attachment: Nexus_Connectivity_Design.pdf*
