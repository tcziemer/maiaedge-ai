**To:** Nick Jones <nick@nexus-datacenters.com>
**Cc:** Ben Heichelbech <benh@nexus-datacenters.com>
**Subject:** Nexus Hubbard, Campus Interconnection & Fiber Distribution Conceptual Architecture

---

Nick, Ben,

Following up on this morning's Connectivity Design draft, attached is a companion view we pulled together today: the Campus Interconnection & Fiber Distribution Conceptual Architecture. Where the first document framed the end-to-end signal flow, this one drills into the physical fiber distribution across the campus and shows how every layer is built for East/West diversity and A/B redundancy.

What it shows:

- Full campus topology with the Carrier Hotel acting as the central interconnect building (Core Fabric / IXC), feeding Data Hall #1 and Data Hall #2 over diverse East and West campus fiber paths.
- External carriers entering through separate East and West vaults via diverse underground paths, with OSP-to-ISP transition occurring at the MDF/EF entrance rooms in each facility.
- A consistent hierarchical distribution model at every building: Vault, Zero Vault, MDF/EF, End of Row (EOR), Top of Rack (ToR), with dual A/B paths preserved all the way to the equipment.
- The MaiaEdge Path Border Controller positioned at the ToR layer in both the MMR and the data halls, providing the automation and service abstraction between the interconnect domain and the consumption domain.
- A simplified single-line version of the same architecture on page 2, useful when walking non-engineering stakeholders through the flow.

The design principles called out on the diagram (diversity, A/B redundancy, carrier neutrality, scalability, automation and service agility) are intentional carry-throughs from your Fiber & Interconnection Strategy and Carrier Hotel Basis of Design, so the two documents should line up cleanly when your team reviews them side by side.

As before, this is a working draft meant to anchor the conversation. Happy to adjust naming to match your Basis of Design conventions, add or remove layers of detail, or build a version tailored for the financing discussion. If a short walkthrough would help, just let me know what times work this week.

Regards,

Tim

Tim Ziemer
CRO / Co-founder
+1 (612) 840-2493
timziemer@maiaedge.io
77 S. Bedford St. Suite #150
Burlington, MA 01803 | maiaedge.io

*Attachment: Campus Interconnection & Fiber Distribution Conceptual Arch. 4.22.26.pdf*
