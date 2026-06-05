# Nexus Project Kickoff Email — Draft

**To:** Bill Bushman \<bill.bushman@pearce-services.com\>, Jim Salvato \<james.salvato@pearce-services.com\>, Josh Lanctot \<joshua.lanctot@pearce-services.com\>, Jeremy Gallagher \<Jeremy.Gallagher@pearce-services.com\>, Kristyn Shaughnessy \<kristynshaughnessy@maiaedge.io\>, Woody Acosta \<[woody@maiaedge.io]\>, Abilash [Last Name] \<[abilash@maiaedge.io]\>
**From:** Tim Ziemer \<timziemer@maiaedge.io\>
**Subject:** Nexus Hubbard — Kickoff: Background, Contacts, Documents and Next Steps

---

Team,

Good to get everyone together this morning. As promised, here is the reference email to get us all on the same page. One thing before anything else: everything on this project is under NDA. Nexus is very tight about this — there have already been press leaks. Nothing leaves this group without checking with me first.

**The Project**

Nexus is building a $64 billion AI data center campus on 2,000 acres in Hubbard, Texas. The location sits at the center of the Dallas-Houston-Austin triangle, equidistant from major fiber runs on either side, and at the intersection of three Permian Basin pipelines. That means they can generate their own power behind the meter through natural gas and large battery storage, no grid exposure. They have 14 carriers committed and are bringing in 11,600 fiber strands.

Their first customer is Anthropic. They originally contracted for four buildings and are close to exercising an option for ten. A second large customer is potentially 30 more buildings, possibly under contract within 60 days. Long term this campus is 64-65 buildings.

Ivan's vision is to land all that carrier fiber into a single centralized Meet Me Room rather than running thousands of strands into each building individually, then distribute across the campus through a programmable fabric. That programmable fabric is not just an architecture choice — it is central to his business model for how the campus operates and scales commercially. It is also why MaiaEdge is playing a central role here. Our Path Border Controller sits at the heart of that fabric and is what makes the whole thing automated and commercially viable at scale.

**Our Engagement**

MaiaEdge is prime on the engineering services contract. Pearce is our subcontractor on ISP and physical layer. Michels is the exterior OSP contractor and is already on site. They have submitted their first list of long-lead items for procurement, and there will be many more to follow as design matures. It will take us some time to get to the same place on the inside plant and network side, but the timing is tight and we need to move fast.

A note on NTP timing: Nexus is presenting our contract along with Michels and one other GC to Ivan today for final sign-off. NTP should follow shortly. Our 90-day schedule does not start until written NTP is in hand. We are pushing hard for an on-site kickoff in the first half of June — the second half does not work for our team.

**What We Are Delivering (90-Day Scope)**

The following is taken directly from our contract. These are the committed deliverables and target dates from NTP:

- Day 1 (T+0): Kickoff meeting, decision log, and Technical Input Request issued to Nexus
- T+2 weeks: Baseline Architecture Assumptions Document and Interface Block Diagram
- T+4 weeks: Low-Level Design (LLD) for all four Phase 1 buildings, MMR and carrier hotel architecture package, per-building connectivity design, and interbuilding fiber mesh design
- T+6 weeks: Bill of Materials (BOM), Material Takeoff (MTO), long-lead item identification and vendor recommendations, MaiaEdge PBC deployment specs, and vendor-neutral equipment specs and data sheets
- T+8 weeks: Expansion Architecture Document covering scale to 65 buildings, with capacity planning model
- T+12 weeks: Construction-Ready Handoff Package for Phase 1, per-building installation duration estimates, high-level cost model, and cost-basis package supporting downstream contracting decisions

Note what is out of scope: procurement execution, physical installation or commissioning, and carrier-specific custom design are not part of this engagement.

For the clock to start on Day 1, we need Nexus to confirm the four Phase 1 buildings, provide MMR location and dimensions, hand over existing infrastructure drawings, and designate a technical point of contact. Getting those inputs locked early is on our critical path.

**Our Team**

Tim Ziemer, Co-Founder and CRO, MaiaEdge (timziemer@maiaedge.io)
Abilash [Last Name], Co-Founder and CEO, MaiaEdge ([abilash@maiaedge.io])
Woody Acosta, Lead Network Engineer, MaiaEdge ([woody@maiaedge.io])
Kristyn Shaughnessy, Program Manager, MaiaEdge (kristynshaughnessy@maiaedge.io) — Kristyn is running point on project governance and coordination. She is the quarterback. If you need something, go to Kristyn.
Bill Bushman, VP Data Center Services, Pierce (bill.bushman@pearce-services.com) — Pacific time
Jim Salvato, Pierce (james.salvato@pearce-services.com) — OSP/ISP design lead, 30 years of fiber experience
Josh Lanctot, Pierce (joshua.lanctot@pearce-services.com) — telecom and fiber, 15 years AT&T background
Jeremy Gallagher, Sales Engineer, Pierce (Jeremy.Gallagher@pearce-services.com) — has been close to this project from the start and has already put together a substantial list of open questions

**Nexus Key Contacts**

Ivan Van der Walt, CEO and Founder — where the buck stops
Ben Heichelbech, Chief Engineer — lead on the ground
Nick Jones — our day-to-day contact on the vendor side. He is caught between Anthropic's timeline pressure and the banks' procurement requirements. Our job is to help him deliver.
Megan Claydon, SVP Commercial — manages contracts and procurement, represents the banking side

**Tools and Project Management**

Kristyn is standing up Confluence and Jira for project tracking and SharePoint for document storage. You will get an Atlassian invite from her shortly; it is not spam, please accept it. Nick has also agreed to start uploading Nexus documents to the SharePoint once it is live, so that becomes our pipeline for receiving their reference material. Until then, this email and the attached documents are your starting point.

**Before Tuesday**

Everyone on the engineering side, please compile your open technical questions and get them to Kristyn by end of day Monday. Jeremy already has a substantial list going. Jim and Josh are meeting Friday at 1pm ET to work through theirs. Woody, Abilash will get you up to speed today. There are no dumb questions here — the campus is literally a field right now. Do not assume anything.

Kristyn will send a Tuesday invite. The goal is to walk into our first Nexus meeting as one team with a clear, organized set of questions — not five companies that just met.

**Attached Documents**

Please review the Basis of Design and Fiber Strategy first.

1. Nexus Hubbard Campus Carrier Hotel Basis of Design (Dec 2025) — the foundational technical reference from Nexus. Start here.
2. Nexus Hubbard Campus Fiber and Interconnection Strategy (Feb 2026) — strategy behind the fiber architecture, pairs directly with the Basis of Design.
3. Nexus Apex Site Layout Rev 12.1 — full campus site plan for getting oriented to the physical scale.
4. Nexus Hubbard IXP Contractor Engagement Pack v3 — Nexus's own contractor document covering the IXP, responsibility matrix, and phasing. Important context for building your question list.
5. Nexus Carrier Hotel and Data Center Connectivity Design — MaiaEdge's connectivity design in progress. Two-domain architecture, MMR signal flow, and per-building extension model.
6. Campus Interconnection and Fiber Distribution Conceptual Architecture (Apr 2026) — campus-level fiber distribution diagram showing A/B redundancy, vault-to-top-of-rack hierarchy, and PBC placement.
7. MaiaEdge Nexus SOW No. 1 [Clean] — executed scope of work. Know what is in scope before we start.

Everything moves to SharePoint once Kristyn has it ready. More soon.

Tim

Tim Ziemer
Co-Founder and CRO, MaiaEdge Networks
+1 (612) 840-2493
timziemer@maiaedge.io

---

**Attachments:**
- NHG-TC-DB-00001_Nexus Hubbard Campus Carrier Hotel Basis of Design_Dec 2025.pdf
- Nexus Hubbard Campus Fiber & Interconnection Strategy_Feb 2026.pdf
- Nexus_Apex_2025_-_Site_Layout_Rev12.1-ANSI D 22x34.pdf
- Nexus Hubbard IXP. Contractor Engagement Pack v3.docx
- Nexus_Connectivity_Design.pdf
- Campus Interconnection & Fiber Distribution Conceptual Arch. 4.22.26.pdf
- [Clean] MaiaEdge_Nexus_SOW No.1.docx
