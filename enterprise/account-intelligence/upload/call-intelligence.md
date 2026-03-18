# MaiaEdge Call Intelligence Database

**Purpose:** Consolidated call intelligence from all prospect/customer conversations, organized by segment with extracted proof points, objections, and competitive intelligence.
**Last Updated:** February 2026
**Sources:** 14 call summaries + 1 meeting analysis + 1 resonance analysis

---

## By Segment

### Colocation

#### CyrusOne
- **Company Profile:** CyrusOne is a major colocation provider with multiple data centers (Carrollton, Dallas, San Antonio) offering on-premises cloud connectivity through proprietary on-ramps and Megaport partnerships.
- **Key Contacts:** Tim Streeter (Director of Interconnection, Champion/Decision Maker), Tim Cunningham (Interconnection/Telecom Lead, Technical Evaluator), Chuck Roberts (Network/Solutions Team)
- **Current State:** Uses Megaport for cloud connectivity and multi-cloud access; has proprietary cloud on-ramps (e.g., direct Azure on-ramp in San Antonio); internal backbone connecting sites (Dallas to San Antonio); largely manual provisioning. No relationship with Equinix due to competitive dynamics.
- **Pain Points Expressed:**
  - Loss of sovereignty via Megaport/fabric dependencies — customers develop direct Megaport relationships, CyrusOne loses leverage if Megaport reprices
  - No visibility past the cloud handoff — "Once the handoff is to AWS, that's it. Sorry, there's nothing else we can help you with."
  - Manual provisioning with 30-60 day cycles and error-prone configurations
  - Equinix competitive friction prevents service expansion — "Equinix is one of our competitors, so [we don't have access to their fabric today]."
- **Ah-Ha Moments:**
  - End-to-end cloud visibility demo showing AWS VPC status visible within MaiaEdge portal — prospect immediately resonated: "Yeah, that right there is something that customers and us have dealt with constantly."
  - Equinix access without competitive relationship — using third-party MaiaEdge customer (IENTC or Atlantech) to hold Equinix port while CyrusOne appears to customer
  - Carrollton use case mapped to infrastructure (Carrollton DC → Equinix port → global reach via federation)
- **Objections Raised:**
  - Engineering team may resist BGP replacement and CLI elimination — how handled: Ziemer reframed around business outcomes (EBITDA, agility); Streeter deferred to internal engineering review — Resolved? Partially
  - Equinix competitive relationship — how handled: Offered federation path via third-party partner — Resolved? Partially; specific arrangement needs definition
  - Website thin on content/credibility — how handled: Ziemer disclosed intentional stealth mode, committed to new website live within days, shared funding status — Resolved? Yes
- **Competitive Intel:** Megaport (deployed in-facility, margin compression risk), Equinix (competitor, creating strategic friction). Tim Streeter remarked internal stakeholders may be skeptical of BGP replacement.
- **MaiaEdge Fit:** Maintains brand sovereignty while expanding connectivity reach; enables access to Equinix fabric services without direct competitive relationship; provides end-to-end visibility across cloud handoffs; reduces operational burden through self-service portal.
- **Status/Next Steps:** Internal engineering team review underway; deeper technical call planned after review; PTC (Hawaii) provides informal connection opportunity.

### Fiber Operators

#### Arvig
- **Company Profile:** Regional fiber operator/service provider in Minnesota with extensive statewide reach touching ~200+ MSAs; provides wholesale video, wholesale internet, and wholesale transport to smaller rural carriers; recently renegotiated Cologix contract ($350/month per cross-connect); has Megaport leasing dark fiber from them.
- **Key Contacts:** Mike Miller (Business lead/deal sponsor), Scott Shekels (Sales), Ben Wiechman (Network Engineering Manager), David Schornack (Senior leadership/decision maker), Dylan Hanten (Network Engineer)
- **Current State:** PBC test unit deployed in Saint Cloud POP for months; does not offer cloud on-ramp services; current response to customer cloud requests is "We don't provide it, but we can get you to Databank and then it's on you"; fiber/wave connectivity to Equinix in Chicago and Rackspace in Equinix.
- **Pain Points Expressed:**
  - No cloud on-ramp offering; losing revenue they can't quantify — "We never use the word cloud on ramp here." "We don't know how much [revenue we're missing] because we don't understand that business at all."
  - Customer demand growing and being deflected — Scott confirmed 3-4 customer requests in recent months (Revnet specifically mentioned)
  - No Equinix on-ramp in Minneapolis creates geographic opportunity — "Equinix is the number one colo provider in the planet and they don't have an on-ramp or an off-ramp here in Minneapolis."
  - Sovereignty loss with current fabric models — "Megaport has published pricing. So your ability to bundle together cloud services in your circuits are highly diminished because customer just says, well I know it's Megaport."
  - Cross-connect cost burden — $350/month per cross-connect at Cologix; one-port-unlimited-virtual-connections model would reduce per-customer costs
- **Ah-Ha Moments:**
  - Minneapolis on-ramp opportunity — Tim explained Equinix has no on-ramp in Minneapolis and Arvig already has fiber + rackspace at Equinix Chicago; Mike immediately engaged and mapped existing infrastructure
  - Wholesale cloud on-ramp to rural telcos — Mike immediately grasped model: "So what you're saying is we could give them connectivity into Equinix or Megaport on a per slice basis, like a VLAN."
  - Fiber islands/Hansen Telephone use case — Ben Wiechman spontaneously identified specific customer (Hansen Telephone) where MaiaEdge would solve known problem: "With all their little islands, this would be really good product."
  - Revenue pull-forward via DIA — concept of starting immediately with DIA and replacing with fiber later clearly resonated
  - End-to-end visibility into cloud (AWS/Azure troubleshooting) — Tim showed ability to identify customer cloud misconfigurations; technical team resonated with scenario of 5-hour phone calls blamed on Arvig when issue is AWS misconfiguration
- **Objections Raised:**
  - "We don't understand the cloud on-ramp business at all" — how handled: Tim offered business case analysis with specific math: 50-70% gross margins on cloud on-ramp, breakeven at 3-4 customers on shared port — Resolved? Partially
  - Are customers even asking for this? — how handled: Scott self-corrected confirming 3-4 recent requests; Dylan also confirmed some — Resolved? Yes
  - How do we monetize/evangelize this? — how handled: Tim described marketplace, ConnectBase, word of mouth, and Minneapolis on-ramp positioning — Resolved? Partially
- **Competitive Intel:** Megaport (leasing dark fiber from Arvig; published pricing seen as negative), Equinix (no on-ramp in Minneapolis), Cologix/Databank (current colo providers; $350/mo cross-connect pain), Lumen (mentioned as "not very happy that we exist" — competitive validation), Zeo (Mike asked if MaiaEdge similar; Tim differentiated on complexity/cost)
- **MaiaEdge Fit:** Package cloud connectivity (AWS, Azure) for customer base including 200+ smaller telco MSA partners; become Minneapolis/Minnesota on-ramp hub; wholesale cloud on-ramp to small carrier partners; monetize existing infrastructure; understand cloud on-ramp business model and economics.
- **Status/Next Steps:** PBC already deployed in Saint Cloud; internal Arvig sync scheduled to determine next steps; technical deep-dive with Kyle Blackwell offered; access to existing PBC unit for exploration; business case analysis to be shared (referenced Atlantech pricing as model).

#### Ocean Networks
- **Company Profile:** Fiber operator working with University of Hawaii on Hawaii Inter-Island fiber system (state-backed project); connects to providers from South Pacific, Australia, and New Zealand; working on equipment placement at Doctor Fortress (Honolulu data center); Fred's data center has connections to broader regional providers.
- **Key Contacts:** Cliff Miyake (Project Lead), Steve Brock (Construction Manager - telecom veteran), Chris Zane (University of Hawaii IT - project authority for Hawaii Inter Island system)
- **Current State:** Building Hawaii Inter Island fiber system; no current fiber connection between Hawaii and mainland for traffic exchange; waiting on Spectrum for NNI paperwork to tie network to addresses across Hawaii.
- **Pain Points Expressed:**
  - Lack of mainland connectivity for traffic ingestion — "They've tried to send connection traffic to Hawaii already and we weren't able to take care of that for them."
  - Need for redundancy/failover paths — Steve noted: "One of the things that we deal with in submarine cable is sometimes we'll have tributaries that have latency issues or something and we'll wanna switch it across."
  - Training and sales enablement for new technology — Steve: "The long lead time stuff is gonna be training, you know, sales guys how to use it and training... getting the UH guys figured out who they wanna connect to."
- **Ah-Ha Moments:**
  - Early problem statement slide showing NNI challenges — Steve: "I'm loving what I'm seeing."
  - Federation topology and marketplace demonstration — Steve: "It's got the wheels turning, boys."
  - End-to-end visibility demo showing path through Equinix to AWS — Chris: "Very neat. Good concept."
  - Simple setup/deployment explanation — Steve: "I'd like to dunk this one. It looks fun."
  - Repeated exposure generating use cases — Cliff: "Each time I see it, all it does is generate more use scenarios than I'm trying to figure out how we get those all going."
- **Objections Raised:**
  - Interface type limitations (SDH for submarine cable) — how handled: Acknowledged Ethernet-only approach, emphasized AES-256-GCM encryption for security — Resolved? Partially; customer accepted answer but noted for future
  - Security/visibility concerns across federated paths — how handled: Explained sovereignty model (topology hidden between orgs), encryption, multi-tenancy — Resolved? Yes
- **Competitive Intel:** None explicitly mentioned
- **MaiaEdge Fit:** Create mainland-to-Hawaii gateway for traffic exchange; access cloud on-ramps (AWS, Azure) without building infrastructure; connect to rural provider ecosystem via Indetel federation; provide white-labeled self-service portal to customers.
- **Status/Next Steps:** Agreement expected signed early the following week; Cliff meeting Fred/Rosa at Doctor Fortress to confirm space/power; calls scheduled with Cogent and Zale for Hawaii-LA connectivity; Kyle Blackwell to run POC checklist after agreement signed.

#### Flo Networks
- **Company Profile:** Service provider/carrier with existing network infrastructure and current NNI/interconnection methods; very OPEX-sensitive organization that capitalizes hardware and keeps support/maintenance as separate annual items.
- **Key Contacts:** Manuel (Technical/Business Development)
- **Current State:** Works with vendors using separate hardware and support contracts; has some current provisioning capability; preparing internal pitch for executive team (meeting scheduled November 10); very sensitive to pricing model fit.
- **Pain Points Expressed:**
  - OPEX sensitivity / procurement model constraints — "We are very opex sensitive, so we always prefer to split that. I mean hardware and support as a separate item." "The way we work with other vendors, we keep it separate... we push the hardware. It's something that we capitalize and then we keep the support and maintenance on a yearly basis as a separate item."
  - Internal buy-in challenge — "I need to find a way to sell it internally." "It's something that we are doing somehow... with what we have today... there are some advantages of doing it [with MaiaEdge]."
  - Need for test validation / proof points — "Probably that can speed up the process because basically... we're going to be the same."
- **Ah-Ha Moments:**
  - Tim offered to share test results from Mexico carrier deployment (EXFO validation, jumbo frames, failover testing) — Manuel: "Probably that can speed up the process because basically... we're going to be the same."
  - Explanation of independent VLAN domain per port (vs ENNI limitations) — immediate affirmation ("OK, OK"); recognized technical differentiation
  - Tim mentioned marketplace capabilities and carrier network expansion (London, Frankfurt, Paris, Los Angeles, Ashburn) — Manuel: "This is quite important for me." Strong interest in marketplace demo
  - Tim mentioned meetings with Orange and Colt showing industry momentum — Continued engagement and request for follow-up materials
- **Objections Raised:**
  - Prefers split hardware + subscription model over bundled IaaS — "The way we work with other vendors, we keep it separate... we push the hardware. It's something that we capitalize and then we keep the support and maintenance on a yearly basis as a separate item." — how handled: Tim acknowledged feedback, noted other carriers pushed for same model, indicated flexibility — Resolved? Partially; flexibility indicated but pricing model not finalized
- **Competitive Intel:** None explicitly mentioned
- **MaiaEdge Fit:** Deploy MaiaEdge fabric for network automation; leverage marketplace to expand service offerings to customers; present solution to executive team; understand marketplace capabilities before proceeding with POC.
- **Status/Next Steps:** Pricing information and flexibility discussion needed before full engagement; marketplace deep-dive demo scheduled for later in week post-Encompass; POC planned but Manuel wants to understand marketplace capabilities first; executive meeting November 10 is time-sensitive opportunity.

### Network Operators

#### Verizon
- **Company Profile:** Major service provider with existing Equinix fabric partnerships; in process of integrating Equinix APIs for cloud on-ramp (AWS, Azure); uses bookended CPE model (pizza box at customer premises); peers with major carriers (AT&T, etc.); currently covers only 5 of 10 markets customers want.
- **Key Contacts:** Chris Painter (Network/Transport Engineer)
- **Current State:** Has existing Equinix fabric partnerships; bookended CPE model for managing VLANs and multi-service Ethernet over Type 4 / off-net circuits (e.g., AT&T NNI); currently peer with major carriers but lack visibility into off-net segments; cloud on-ramp to smaller/newer providers (GPU-as-a-service) still largely manual.
- **Pain Points Expressed:**
  - Limited fiber footprint creates lost deals — "I'm only in five of the 10 that they want... it's going to go to somebody else." "It's not like an SDN network where you can just cherry pick the access. It's either on my fabric or you're not."
  - Manual cloud provider onboarding — "Everything right now is pretty much manual... even to get that Z-side token is manual."
  - API development cost and maintenance burden — "If I can enable Internet access and cut down some of the IT costs of developing the APIs, close that portal instead..."
  - No visibility into off-net / partner segments — "We do an annual with AT&T, we put our box on the end of it, it's a V-line to us. We don't know anything about what's going on with AT&T — this would give us a lot more visibility."
  - Resistance to adding "another box in the network" — "Everything they're doing right now is against another box in the network. You've got your vendors, you chose your vendors."
- **Ah-Ha Moments:**
  - DIA/Internet as underlay between PBCs — Chris had visible moment of reframing: "Maybe I'm thinking about this all wrong... I connect to whoever at 100 gig Internet. They can order 100 gig Internet at the side and your box is gonna build the layer two over Internet."
  - Multi-provider topology demo (Arvig, Revnet, Atlantek all connected over DIA to single PBC in Portland, ME) — Chris: "I like the idea of... you go into whatever that location, say hey I'll hit Arvig, and then all the Arvig sites — if I've got your box to get into Arvig, then Arvig can say here's my 1,000 addresses that can now on-ramp into my network."
  - Equinix API integration already built (Verizon wouldn't have to develop) — Chris: "I hate to tell you, but you put a couple of these in and all your work that you did on your APIs into Equinix, we've already done it... I like that."
  - 5G / Fixed Wireless Access use case (potential Internet underlay) — Chris visibly lit up: "I'm definitely interested in this Internet on-ramp... thinking about 5G, fixed wireless access... I can do a bunch of 300 Meg connections out."
- **Objections Raised:**
  - "Another box in the network" — how handled: Ziemer pivoted to reference architecture where Verizon may not need box in some topologies (PBC sits at partner like Arvig, not in Verizon network) — Resolved? Partially; acknowledged but not fully resolved
  - Bandwidth definition ambiguity over Internet underlay — "What bandwidth would you sell — a 200 Meg EVC? Is that what you would sell? How do you define the bandwidth?" — how handled: Tim explained operator defines ingress rate cap at path creation; on metro Ethernet or fiber can provide guaranteed CIR with oversubscription — Resolved? Partially; understood but needs internal (gold vs. silver tier) discussion
  - Azure Express Route provisioning flow complexity — "I can't hide FIX from — 'cause I gotta choose the provider for where the hosted connection is." — how handled: Woody confirmed known constraint; APIs are to Equinix, not directly to Azure; reverse provisioning via cloud profile is workaround; direct Azure integration on roadmap — Resolved? Partially
- **Competitive Intel:** Equinix Fabric (existing partnership), Megaport, Console Connect, Lumen Fabric, AT&T (access provider). Lumen/Bell Labs call mentioned for next week (indicating MaiaEdge actively engaging competitive SP accounts, creating urgency).
- **MaiaEdge Fit:** Extend fabric reach to off-net locations using Internet/DIA/5G/FWA as underlay; use as automation/federation layer for cloud on-ramps, reducing internal development costs; partner with regional fiber operators (e.g., Arvig) to extend reach at metro level; maintain customer sovereignty (partners shouldn't see how Verizon segments traffic).
- **Status/Next Steps:** Follow-up sync in couple weeks; Chris needs to "sell upward" to boss and peer transport engineer; pitch deck needs tailoring for VP/director audience focused on revenue expansion, footprint economics, reduced API development cost; 1-gig CPE form factor actively needed for customer premise/FWA backhaul.

#### Telstra InfraCo
- **Company Profile:** Manages Australia's passive infrastructure — fiber, exchanges, fixed network sites, pits/pipes, mobile towers — as separate business unit; $2B+ in national infrastructure programs including $1.6B intercity fiber expansion (14,000 km), copper recovery, satellite access node rollout (300 nodes, 4,000 km dark fiber), and data center upgrades.
- **Key Contacts:** Kathryn Jones (Program Director, National Infrastructure)
- **Current State:** Manages extensive passive fiber infrastructure; has significant existing — and underutilized — fiber assets; network contains stranded/excess capacity.
- **Pain Points Expressed:**
  - Stranded/underutilized fiber capacity — "Using [what we've got already] and working out OK, well, that would still meet the capacity requirements or the latency requirements… rather than going and actually building — and that's uneconomical." "We're trying to stop [overbuild] — that's a huge drain on our P&L."
  - Static, opaque infrastructure — existing fiber behaves as fixed asset with no visibility into availability or traffic movement — Kathryn's own framing: "So you're making a static piece of digital infrastructure programmable and actually visible."
  - Wide band access overbuild — customers request new builds when capacity already exists nearby
- **Ah-Ha Moments:**
  - Abilash explained placing PBC on fiber makes it programmable and visible (capacity-aware, policy-driven, dynamically routable) — Kathryn restated unprompted: "So you're making a static piece of digital infrastructure programmable and actually visible." Indicates genuine comprehension and resonance.
  - Tim described PBC speaks language of fiber at Ethernet handoff, enabling deterministic multi-operator paths with sovereignty — Kathryn immediately connected to access fiber reuse challenge and overbuild problem
- **Objections Raised:**
  - Megaport relationship concern — Telstra InfraCo already in conversations with Megaport — how handled: Positioned MaiaEdge as complementary and additive; infrastructure makes Megaport more efficient while enabling services beyond Megaport frame — Resolved? Partially; Kathryn accepted framing but asked for clear articulation in written materials for product team
- **Competitive Intel:** Megaport (active conversation); MaiaEdge positioned as complementary, not competitive
- **MaiaEdge Fit:** Programmable, discoverable fiber with ability to dynamically find and allocate existing capacity based on cost, latency, or routing policy; end-to-end visibility across multi-operator circuits; monetize excess fiber; introduce product team (Dipan Patel) for deeper technical evaluation.
- **Status/Next Steps:** Kathryn will personally brief Dipan Patel (head of product) during upcoming two-week Europe trip and facilitate introduction; written differentiation material needed before product team meeting; Australia/Asia-Pacific signaled as MaiaEdge's first international market priority.

#### euNetworks
- **Company Profile:** Pan-European fiber operator; 17 countries, ~590 data centers; backbone connecting hyperscalers and DC operators across Frankfurt, London, Amsterdam, Paris, Dublin; extensive owned infrastructure including hollow-core fiber.
- **Key Contacts:** Carl Delaney (Head of Product), Paul Weterman (Director, Product Management — Ethernet, Internet & Cloud Connect Services), Danielle Reilly (VP Commercial Management)
- **Current State:** Historically "very, very focused" on on-net strategy; own extensive fiber infrastructure across Europe ("in every single data center in Europe"); already have Big 5 cloud on-ramps (AWS, Azure, Google, Oracle, IBM) fully automated with API integration and immediate turn-up via customer portal; direct NNIs with cloud providers (not through Equinix fabric); Sonata-based APIs published at connected.eunetworks.com; existing API integration with Ecotel; use Salesforce for inventory and proprietary in-house APIs for router configuration (Juniper, Huawei).
- **Pain Points Expressed:**
  - Loss of visibility when off-net — "once traffic leaves your network, it's a black hole. When performance degrades, it's endless troubleshooting and finger pointing"
  - Manual provisioning delays for off-net/Type 2 connections — "it costs a lot of money and takes a lot of time to set up these type 2 connections"
  - Customer sovereignty concerns with third-party fabrics — "who owns the customer then? Because then you have to turn it over to Megaport or turn your customer over to Equinix"
  - Complexity of multi-provider integration — Paul: "the business support systems and the NIM on our side, network inventory management that needs to be updated... all the Juniper and Huawei routers that need to be configured... that's not like, you know, you put in a PBC and then hey, a magic wand and everything will work"
  - Limited off-net opportunities captured — "Opportunities are largely off net no bid. But if it's 70% on net and 30% off net, yes, then we would like to have a seamless solution"
- **Ah-Ha Moments:**
  - End-to-end visibility demo across network boundaries showing path-level SLA metrics — Paul engaged more deeply asking technical follow-ups about measurement methodology and pinpointing issues
  - Explanation of publishing services to federated marketplace — Paul: "That's interesting" when Tim described ability to publish cloud on-ramps wholesale without building white-labeled portal themselves
  - Demo showing Arvig (remote fiber provider) customer accessing AWS through Centra's network — Paul asked clarifying questions indicating genuine interest in Type 2 federation use case
- **Objections Raised:**
  - "What's new here? This is what Equinix is doing today." — "I can buy a 10 gig or 100 gig port of fabric. I can slice it up in VLANs, resell it to different customers. So what's new here?" — how handled: Pivoted to federation across multiple carriers, DIA flexibility, sovereignty, and end-to-end visibility as differentiators — Resolved? Partially; Paul continued engaging but remained skeptical
  - "It's too abstract — I don't fully understand how it integrates with our systems" — "I'm struggling with understanding how this actually works with integrating the networks" and "I still don't fully get it, but I need to let this sink in" — how handled: Offered to include Amplify, ConnectBase, and Diego Nieto (Digital Transformation Director) in follow-up call; explained Sonata adapter approach — Resolved? No; key blocker requiring follow-up
  - "Can't commit resources for POC on short notice" — "I don't see any opportunity to free up resource or engineers to assist this in such short notice" — how handled: Accepted; agreed to follow up in 2 weeks (Q2 2025) — Resolved? Yes; appropriately deferred
  - "How do you control quality on DIA? There's no SLA on DIA." — how handled: Positioned DIA as instant-start option with fiber replacement later; referenced growing enterprise acceptance — Resolved? Partially; use case clarity needed
- **Competitive Intel:** Equinix Fabric (existing conversations), Megaport; euNetworks already evaluating ConnectBase, Trunk Star, Ice Blue for accelerated quoting
- **MaiaEdge Fit:** Seamless off-net service delivery with visibility; low-touch automation for quoting and provisioning; wholesale cloud on-ramp revenue opportunity; selective extension (70% on-net, 30% off-net); automated NNI provisioning with minimal human intervention.
- **Status/Next Steps:** Deferred to Q2 2025 re-engagement; Ecotel installation happening in 2 weeks (should be live proof point by Q2); CMC Networks also being set up (potential reference); need to demonstrate integration path with existing Sonata APIs; Danielle Reilly (VP Commercial) appears most aligned with value prop (speed, automation, low-touch); Luc (formerly Telstra, now Google) made warm introduction; future engagement should involve Diego Nieto (Digital Transformation Director).

### MSP / Aggregators

#### Granite Telecom
- **Company Profile:** 23-year-old service aggregator based in Boston (Quincy HQ) with ~100 sales reps in Atlanta; does NOT own fiber network infrastructure; relies on reselling carrier services (primarily AT&T); has core network for transport/backhaul but no last-mile fiber assets; sells multi-location circuit deployments to enterprises (e.g., 100+ locations per deal).
- **Key Contacts:** Shane Hoff (VP of Strategic Partnerships, 23-year company veteran, day-one employee)
- **Current State:** Existing relationship with MaiaEdge founders from Acme Packet and 128 Technology days; depends on carrier provisioning cycles (60-90+ days waiting on AT&T); limited control over middle-mile connectivity; automation stops at network borders; complex manual processes for multi-carrier connections.
- **Pain Points Expressed:**
  - Long provisioning cycles — "If we're just reselling, you know whatever AT&T DIA fiber and we have no NNI... it still takes us you know 60 days to whatever to install it because we're waiting on AT&T."
  - Complex multi-stakeholder coordination — "We got to coordinate with people on site. We got to deal with the carriers. We got to place orders, wait for them to do their part and you know, drop off, install, turn up, test, managed services need to be installed as well."
  - Limited differentiation — Enterprise customers drag feet then "want to deliver tomorrow" — whoever executes quickest wins
- **Ah-Ha Moments:**
  - Tim explained Granite could tap into 2,200 underlying fiber operators (who built AT&T's LTE network) at 80% lower cost — Shane engaged more deeply, asked clarifying questions about marketplace concept
  - Tim described "marketplace for carriers" like Amazon for network services — Shane: "So kind of a marketplace, kind of a hub in a way too, that allows you to bypass some of these things that are inefficient for all of us."
  - Tim explained Granite could both buy AND sell services on marketplace (monetize excess capacity) — Shane asked about cloud on-ramp capabilities before connection dropped
- **Objections Raised:**
  - "We don't own fiber" — how handled: Tim: "100% which is also why this is such a cool technology for you because what you do have is a lot of services that you sell and connect to a lot of different networks" — Resolved? Yes
  - "Out of my area of expertise" — how handled: Tim offered to connect with technical folks, show visuals — Resolved? Partially; deferred to internal team
  - "Not the decision maker" — how handled: Tim acknowledged, Shane offered to connect to right people — Resolved? Yes; pathway established
- **Competitive Intel:** AT&T (primary carrier relationship), Verizon/Lumen (IXCs mentioned), Megaport/PacketFabric/Equinix Fabric (positioned as not competing — MaiaEdge is infrastructure provider vs. NaaS), Juniper/HPE (former relationship context with 128 Technology)
- **MaiaEdge Fit:** Faster circuit turn-up; new revenue channels through agent/commission programs; strategic partnership opportunities; ability to access 2,200 fiber operators at 80% lower cost than AT&T; "marketplace for carriers" concept for operating without owning fiber.
- **Status/Next Steps:** Shane will message Brian O'Connell (key internal contact) internally; MaiaEdge to send one-pager/simple collateral; technical deep-dive scheduled with appropriate Granite team; keep Shane copied on all future communications; discuss agent/referral program separately; interest in revenue-sharing/agent opportunities (not resale model).

#### AccuTech
- **Company Profile:** 30-year bootstrapped SI/MSP with offices in UK, US, and Singapore; co-owned by Bhavesh Mehta and his wife Priti; deeply embedded with Microsoft as Azure Local delivery partner (part of ISD — Microsoft Professional Services); has SKUs with Cisco and Lenovo; 30-year track record with no losses; nominated by Microsoft to deliver sovereign cloud training on behalf of OEMs.
- **Key Contacts:** Bhavesh Mehta (Co-Owner/Director)
- **Current State:** 30-year track record, never made a loss; deeply personal financial stake (bootstrapped through extremely lean periods including personal pension funds); deeply embedded in Azure Local ecosystem since Windows Server 2012 R2; first Azure Stack HCI customer was Kodak in 2013; engineers were 16-24 months ahead of market designing/testing/validating Azure Local solutions; have proprietary sizing and scoping tools better than Microsoft's; built SKU-based service catalog (Azure Local deployment per node, SDN per cluster, VDI per user, stretch cluster per data center); speaking at Microsoft Ignite; can sell through Lenovo and Cisco; seeing explosive demand last 18 months with severe skills gap in market ("Microsoft just drags and grabs us to do everything").
- **Pain Points Expressed:**
  - Connectivity is missing link in their Azure Local stack — "You offer the bit in between that has always been missing."
  - Overwhelming demand with insufficient delivery capacity — "The only people on the planet who could do this very well are Accutech. Microsoft just drags and grabs us to do everything. So now we need lots and lots of help."
  - Capital constraints limiting growth despite strong revenue — "There's only so much finances you can carry forever."
  - Microsoft historically poor at marketing and executing Azure Local — "Microsoft has really screwed this whole thing up — very poorly marketed, very poorly executed."
- **Ah-Ha Moments:**
  - Tim described marketplace concept (carrier-to-carrier NNIs enabling third-party carriers to sell Azure Local connectivity through Accutech's stack) — Bhavesh: "This is super exciting, Tim. Honestly, this needs a really good face-to-face meeting. I think this has got a lot of legs."
  - Tim described IaaS model (no title transfer on hardware, MSA licensing extending to customer's customers) — Bhavesh immediately mapped to Accutech's own SKU-based service model; strong mutual recognition of commercial fit
  - Bhavesh raised Satya Nadella's Davos remarks pivoting Microsoft narrative from AI public cloud to sovereign cloud — both agreed positioned perfectly to ride this wave together; Bhavesh: "Which is fantastic for all of us, right? That's going to be what we want to capitalize on."
- **Objections Raised:**
  - Concern about MaiaEdge's ability to scale globally alongside Accutech — how handled: Tim cited $20M raise ($30M total), well-capitalized investors, ability to scale rapidly once product-market fit proven; "You don't have to worry about us scaling with you. Just give us a shot." — Resolved? Yes
- **Competitive Intel:** None explicitly mentioned
- **MaiaEdge Fit:** Connect London Equinix DC to MaiaEdge network as first milestone; establish commercial MSA to resell MaiaEdge connectivity as a SKU; embed MaiaEdge invisibly into Azure Local service stack (customers get connectivity as part of outcome without understanding how delivered); build Center of Excellence in London DC demonstrating full Azure Local + MaiaEdge stack to OEMs and Microsoft; expand to Singapore DC; eventually consume multi-cloud (AWS, Azure) through MaiaEdge.
- **Status/Next Steps:** Tim Z to send MSA + pricing in single email; follow-up call to review; plan face-to-face with product and pre-sales teams from both sides; capacity requirement (1G/10G/100G) still unknown — use Dave Williams/Revnet deployment as baseline reference; both companies at inflection points simultaneously — strong mutual urgency on both sides.

#### Datum
- **Company Profile:** Virtual infrastructure / edge network provider with 18 Equinix PoP locations (via partner NetActuate) across US using shared routers, IP blend, and their own AS; built virtual overlay CNI called "Galactic VPC" as virtualized backbone; have bare metal and VM infrastructure with direct cross-connects and peers to IXP with AWS/GCP; also functioning as neocloud intelligence provider with customer relationships to Together.ai, Inference.net, RunPod, Modal.
- **Key Contacts:** Zach Smith (CEO/Co-founder), Shelby Lindsey (Incoming Backbone Lead, ex-Equinix)
- **Current State:** 18 Equinix PoP locations with no private backbone between their own locations (running on internet/IXP routing); Shelby Lindsey joining next month to run backbone (came from Equinix, will be key technical evaluator); meeting neocloud customers (Together.ai, Inference.net, RunPod, Modal) to qualify problem and appetite.
- **Pain Points Expressed:**
  - Data movement from cloud object storage to GPU/inference locations too slow and expensive — "The problem is, it's too slow. And there's a secondary thing, which is too expensive, but it's too slow."
  - Neocloud/GPU providers have zero network observability — "Most people don't even know that they have an observability problem, but they know that they're too slow."
  - GPU providers in poorly-connected data centers with IT-admin-level networking — "There's some sort of enterprise Cisco switch as their core interface to the router, to the internet, with a single uplink... they had saturated their switch, couldn't actually push the packets."
  - Serverless GPU platforms (RunPod, Modal) can't control capacity partner networks — "They're dealing with these random GPU miner guys out there... the way they build a customer, they're on the hook for the SLA."
  - Datum's own locations aren't connected via private backbone — "We have not set up any sort of private connectivity or backbone between any of our locations."
- **Ah-Ha Moments:**
  - Groq benchmark (ex-Megaport team building 35 Equinix PoPs in 6 months, anycast + backbone → sub-100ms inference globally) — Zach: "That's how they got below 100 milliseconds in all places... that's the second scenario that I think is actually much easier, because we're going to turn this around and get it to that GPU farm in Kansas. And that we can actually control way easier."
  - Federation flywheel + native storage (as more MSPs join, Datum gets better paths without building) — Zach: "Well, I mean, this is where it gets kind of fun, because then you have Wasabi, you have R2, we try and get them natively on here versus Direct Connect... that's where it starts to get interesting."
  - AWS Service Link convergence — Zach: "I was gonna say the exact same thing" confirming strong alignment on Service Link as low-friction path for non-technical neocloud customers
- **Objections Raised:**
  - Direct Connect/end-state architecture has too much friction for neocloud customers — "They're not doing VPC configuration for every customer... they don't want to deal with it. They're just like, here's my bucket, here's my file." — how handled: Team agreed on phased approach (Datum-side PBC deployment + CNAME/anycast proxy zero customer changes, graduate to Direct Connect for larger customers) — Resolved? Yes; phased go-to-market agreed
  - Bandwidth scale uncertainty — "Well, you'll tell us when we pound you from every one of our locations for everything, all the time." — how handled: Abilash acknowledged streaming better than polling at scale, committed to adding; no hard capacity commitment — Resolved? Partially; further technical scoping needed
- **Competitive Intel:** Groq (aspirational benchmark), Zayo and Verizon (too slow/bureaucratic), implied need to differentiate from direct Megaport/Equinix
- **MaiaEdge Fit:** Offer disruptive low-friction latency path for inference customers without expanding edge infra; native observability exposed as developer-friendly cloud service; private optimized paths between GPU/inference and cloud object storage (AWS S3, GCP, Azure, R2, Wasabi); AWS Service Link partnership for frictionless private connectivity; become virtual backbone/federated network for AI infrastructure providers; phased deployment model (CNAME → observability → Direct Connect → Service Link).
- **Status/Next Steps:** Zach to speak with Together.ai, Inference.net, RunPod, and Modal to qualify problem and appetite; follow-up call Thursday or Friday of following week; explore joint working session at GTC (NVIDIA conference, March); co-design session (New York or GTC) with neocloud customers at table; streaming telemetry on product roadmap; target accounts for joint go-to-market pilot (Together.ai, Inference.net, RunPod, Modal).

### Neoclouds (via Datum Intelligence)

#### Datum (Neocloud Intelligence)
- **Neocloud Customer Insights:** Datum provides intelligence on Together.ai, Inference.net, RunPod, Modal
- **Key Intelligence:**
  - Together.ai: Has latency/performance issues moving data from cloud object storage to GPU clusters; interested in optimized connectivity
  - Inference.net: Active customer with same speed/cost problems; also dealing with inconsistent routing and public internet reliance
  - RunPod: Serverless GPU platform with 200K+ active users; constantly debugging infrastructure partner problems; SLAs tied to capacity partners they don't control; dealing with random GPU miner partners
  - Modal: Similar serverless GPU use case; interested in optimized paths to data and computation
- **Collective Pain Point:** GPU/inference providers are "in the GPU business" — not network experts; have zero network observability; know they're too slow but don't know why; need abstraction layer that makes connectivity invisible
- **MaiaEdge Fit:** Developer abstraction layer ("just plug in and go"), private paths to object storage, native observability, easy button for hybrid cloud + on-prem GPU workloads

#### White Fiber
- **Company Profile:** Owns and operates data centers in Iceland, Montreal, North Carolina (eventual 100MW facility); offers GPU compute (H100, GB200), cloud services (Neo Cloud), managed services, storage; partners with DriveNets for scheduled fabric / RoCE-based networking; direct relationship with DriveNets' founders and CTO; customer mix spans AI training clusters (64-128 machines / up to 1024 GPUs), inference, resellers.
- **Key Contacts:** Tom Parker (Director)
- **Current State:** Actively repositioning toward enterprise SaaS and longer-term contracts (away from short-term spot GPU customers); working on hybrid connectivity solutions for customers with on-prem + cloud workloads; DriveNets handling East-West (GPU cluster networking); seeking North-South / inter-network solutions.
- **Pain Points Expressed:**
  - Hybrid connectivity for GPU/inference customers is manual and clunky — "A lot of hybrid customers — they might have some workloads in Azure but then they want to use us for GPU. How do you connect those together?" versus having them set up VPN
  - Engineering overhead to maintain API integrations — "If we buy in, if I send my network guys and we write automation and integrations for Equinix or Megaport — well now I've got to have them rewrite all that same stuff. And for a new startup that comes along making waves, that's a heavy lift to do that."
  - Inference latency is real and growing constraint — "Inference is super latency — time-to-response — anything you do to bring that down, that's the real value."
- **Ah-Ha Moments:**
  - White-label portal + API abstraction across Megaport/Equinix — Tom understood and validated sovereignty/stickiness angle: "So you can extract the — we have the contract with Megaport, but then the customer goes, 'Okay, it's White Fiber's direct connect to AWS or whatever.' It's on the back end."
  - Oversubscription economics (100G port 2-3x cost of 10G, margin arbitrage) — Tom visibly engaged; reframed commercial model in terms of margin optimization
  - Inference + edge compute use case (Azure Local / AWS Outposts) — Tom confirmed active customer need
- **Objections Raised:**
  - Tom flagged he's not technical decision-maker (network architect out, Tom on PTO) — how handled: Ziemer offered to follow up with slide deck for Tom to circulate, then schedule technical demo — Resolved? Partially; next step agreed, timing deferred to mid-February
- **Competitive Intel:** DriveNets (complementary for East-West fabric, not competitive); MaiaEdge positioned for North-South / inter-network
- **MaiaEdge Fit:** More complete GPU/cloud offering for hybrid enterprise customers; "write once, plug into multiple providers" integration model (engineering effort doesn't repeat per fabric/provider); more predictable longer-term enterprise contracts; solve hybrid connectivity (on-prem + GPU cloud); reduce engineering overhead for API integrations.
- **Status/Next Steps:** Target mid-February follow-up (after Feb 19); Tom will share deck with network team in interim; tentative goal to get network architect on technical demo call; MaiaEdge closed $20M Series A day before call (positive reception).

### International

#### Ecotel
- **Company Profile:** German service provider with connections to multiple fiber operators; operating in fragmented German fiber market with numerous regional providers; prior relationship with 128 Technology (Juniper acquisition); Alexander met Tim pre-COVID in Germany.
- **Key Contacts:** Alexander Wiese (Lead Contact, prior relationship), Matthias Belz (Technical), Peter Winkler (Technical)
- **Current State:** Prior relationship with MaiaEdge team (Alexander met Tim pre-COVID, saw earlier product demo via Markets Together); Marcus (Ecotel colleague) recently met Tim at Capacity London event; warm deal with strong existing relationship.
- **Pain Points Expressed:**
  - Fragmented fiber market coordination — Multiple fiber providers require complex coordination to deliver unified services
  - Cloud access complexity — Need to provide AWS/Azure/SAP connectivity without manual BGP configuration or turning customers over to third-party fabrics
  - Customer sovereignty when off-net — Want to maintain customer relationships and visibility when providing services through partner networks
  - Development overhead for fabric-like capabilities — Competitive pressure to offer self-service portal and instant provisioning without building
- **Ah-Ha Moments:**
  - Tim mentioned ConnectBase / Trunk Star integration for location data and stitching together fiber provider coverage — Alexander: "OK. This will be great, especially in the fragmented fibre market in Germany."
  - Full demo walkthrough showing live customer paths (Arvig to AWS via Centra) — Alexander: "Impressive. Impressive to be honest. It happened a lot since the last time I saw this portal."
  - Tim showed white-label portal capability — Alexander: "White labeling is always good to be honest."
  - Demonstration of margin stacking across federated providers — Alexander verbally confirmed understanding: "Yeah, yeah, yeah"
  - Tim mentioned multi-language portal capability — Alexander expressed interest in German localization
- **Objections Raised:** None raised. Reception overwhelmingly positive. No technical, commercial, or implementation objections voiced. Only constraint: timing coordination for internal resources.
- **Competitive Intel:** None mentioned
- **MaiaEdge Fit:** Unify connectivity across German fiber operators through automated federation; provide cloud on-ramps (AWS, Azure, SAP) to customer base without manual BGP configuration; offer white-labeled self-service portal under Ecotel branding; maintain sovereignty over customer relationships when using partner networks; multi-language portal support (German).
- **Status/Next Steps:** POC confirmed — 2 PBCs shipping to Frankfurt and Düsseldorf; targeting first week of December implementation; MaiaEdge sending Kyle Blackwell for hands-on support; related EU deployments (CMC Networks — London, IENTC — Frankfurt); Ecotel as gateway to German market and fragmented European markets; potential case study: "Unifying Germany's fragmented fiber market"; Q2 2025 proof point for euNetworks re-engagement if successful.

#### Deepak Karpoor (UAE)
- **Company Profile:** Independent advisor; left Verizon in 2024; exploring go-to-market opportunity in UAE AI ecosystem; spent time in Riyadh, Abu Dhabi, Dubai; warm intro to CEO of Core42 (G42's commercialization arm); 24-year Verizon veteran; focused on UAE AI ecosystem commercialization.
- **Key Contacts:** Deepak Karpoor (Independent Advisor, former Verizon)
- **Current State:** UAE/Saudi have world-class AI infrastructure (GPU, sovereign clouds) built by external experts; ecosystem is fragmented with zero commercial or operational infrastructure binding it together; exploring partnership/channel opportunity, not direct sale.
- **Pain Points Expressed:**
  - Fragmentation / zero visibility across sovereign AI infrastructure — "Currently there is zero visibility across all of it. Everything is so fragmented."
  - Developers can't operationalize their own software — "I asked them, if I want to do a POC of your capability, what kind of security and network infrastructure do I need to spin up an instance of your software? And they have no idea."
  - No MSP/partner ecosystem exists — "That entire thing doesn't exist. There are too many things in pockets."
  - Sovereignty requirements are non-negotiable — "Sovereign infrastructure is — there is measurable, certifiable means of showing every bit of the infrastructure is UAE bound. Nothing at the data or control level is outside of the UAE."
- **Ah-Ha Moments:**
  - Tim described end-to-end visibility including VPC attachment status and per-path telemetry — Deepak: "That last slide was powerful. That is something that could be extremely helpful if we can get every visibility of every segment performance of every segment... And policy control can be automated across all segments from a single place."
  - Tim explained sovereign routing (ability to assign routing policy, keep data in-country, unlike BGP; PCE can run locally in-country) — Deepak: "Love it. That's music."
  - Tim confirmed MaiaEdge doesn't require ripping and replacing existing infrastructure — Deepak: "I don't aspire to rebuild what you're doing. If you have capabilities, I want to be able to very rapidly leverage some of it and get them to realize value soon."
- **Objections Raised:**
  - Legacy Verizon mental model (NNIs managed by capacity planning teams; carriers protective of network sovereignty; SD-WAN co-opted by AT&T/Verizon) — "Maybe I'm burdened by the legacy infrastructure at Verizon." — how handled: Tim validated concern, drew SD-WAN analogy (incumbents forced to participate as federation threat grows); reframed around edge compute and AI inference use cases — Resolved? Partially; Deepak remained engaged but acknowledged needing more time; full demo needed
  - "Is MaiaEdge just another NaaS fabric?" (concern it's another Megaport/Equinix Fabric requiring customers to hand over relationship) — how handled: Tim clearly differentiated (MaiaEdge is infrastructure/intelligence for operators, not resold network; operators maintain branded portal, customer sovereignty, visibility) — Resolved? Yes
- **Competitive Intel:** Alkira/Aviatrix implied as comparators ("spaghetti generators" provision complex cloud routing); positioned MaiaEdge as simpler (Layer 2 native Ethernet paths directly into VPCs without cloud routers)
- **MaiaEdge Fit:** End-to-end ecosystem visibility across fragmented UAE AI infrastructure; developer abstraction layer ("just plug in and go"); regional hub model (UAE as sovereign AI services hub for Eastern Hemisphere); crawl-walk-run framework showing phased path; visibility across every segment, measured against 2031 objectives.
- **Status/Next Steps:** Channel/partnership opportunity, not direct sale; G42/Core42 already on MaiaEdge's radar (Tim just had call on that); Pascal Cavin (former Verizon, Middle East focus) made referral — strong signal for formal partner/referral program; Orange actively in conversations about federated marketplace; iintc (Mexican carrier) cited as live deployment (auto manufacturer edge compute); Deepak has pending CEO meeting at Core42 and actively building pitch (near-term window to shape positioning); full demo needed (demo should prioritize end-to-end visibility dashboard, sovereign routing policy controls, VPC native access without cloud router, federation marketplace with UAE-specific scenario).

### Other

#### Gintert (Jason Gintert / Bits in Flight / USNUA)
- **Company Profile:** Independent consultant; formerly HPE/Aruba/Juniper reseller channel; evaluating MaiaEdge for customer building secure, managed edge data enclosures (8-10 rack units, ruggedized/secure); end customer in early prototype stage (no defined connectivity model).
- **Key Contacts:** Jason Gintert (Independent Consultant & Co-Founder/President, USNUA)
- **Current State:** End customer building secure data enclosures-as-a-service across diverse locations (downtown Chicago to rural Oklahoma); serving multiple buyer types (municipal, federal, SP); prototype stage with undefined connectivity model; Jason trying to design "easy button" connectivity reference architecture.
- **Pain Points Expressed:**
  - Transport uncertainty at edge sites (fiber, DIA, Starlink, anything) — "They don't know what they're gonna have access to."
  - Managing networking for unsophisticated end-buyers — "Who's gonna manage the shit in this thing? Like, to get stuff places? And they're like, well, we didn't really think about that."
  - MTU/fragmentation complexity over IP transport — "I still am having a hard time with the MTU thing... I'm sure there are a lot of network engineers who have been burned by MTU problems."
  - White-box/custom switch support complexity — "Who supports it, and when something breaks... I would think it would be such a pain in the ass."
- **Ah-Ha Moments:**
  - Federation flywheel/ecosystem value — Jason: "Now that you've shown me the whole thing, I'm like... it's actually pretty cool. It's cool in that the more successful you guys are, and the more PBCs you get connected, the bigger my customers' network reach could be."
  - Per-path SLA telemetry/"flight recorder" — Jason: "Wow... that's amazing. Yeah, that's really cool."
  - Zero-touch/smart hands deploy (RevNet/Guam analogy) — Jason: "Yeah, I get it. It fits the model I'm looking for."
  - Layer 2 transparent failover over Starlink — Jason: "Wow. All right."
- **Objections Raised:**
  - White-box/custom switch supportability — how handled: Tim acknowledged lesson from 128T; MaiaEdge pivoting to SW license model on Cisco/Juniper/Arista switches; custom via professional services — Resolved? Yes/Partially; Jason agreed SW license approach made sense
  - MTU/fragmentation skepticism — how handled: Tim explained auto-frag/defrag between PBCs; transparent to applications; referenced 128T experience — Resolved? Partially; Jason accepted explanation but noted wants technical deep-dive session
- **Competitive Intel:** None mentioned (Aruba 10K, Cisco, Arista mentioned as switch support options)
- **MaiaEdge Fit:** Transport-agnostic connectivity (DIA, fiber, Starlink, any available); deploy-and-forget reference architecture; federation/marketplace access for connectivity reach; referral/rebate partner model (not resale).
- **Status/Next Steps:** Deal very early (end customer prototyping enclosures); not active sales cycle; relationship-building and reference architecture influence; revisit in 60-90 days; Jason wants NDA, pricing/positioning docs, partnership program details, technical deep-dive, white papers; Jason personality: entrepreneurial, anti-bureaucracy, values autonomy; has network ("few folks" beyond this customer, USNUA presidency, consultant background = connector/influencer).

---

## Extracted Proof Points

| Customer | Quote (Exact Words) | Segment | Usage Context | Cold Outreach OK? (Anonymized Only) | Post-Engagement Named OK? |
|---|---|---|---|---|---|
| Bhavesh Mehta (Accutech) | "You offer the bit in between that has always been missing." | MSP | Describing MaiaEdge's core value prop for Azure Local stack | "Offers the connectivity layer missing from incumbent cloud infrastructure stacks" | Yes — already engaged |
| Bhavesh Mehta (Accutech) | "People don't really need to know, but everything works." | MSP | Describing desired white-label/invisible integration | "Infrastructure should feel transparent to end users" | Yes |
| Bhavesh Mehta (Accutech) | "You're building an infrastructure with potholes and you can't drive your Ferrari over it." | MSP | Re: AI company deploying without network fundamentals | "AI infrastructure fails without proper networking foundation" | Yes |
| Mike Miller (Arvig) | "So what you're saying is we could give them connectivity into Equinix or Megaport on a per slice basis, like a VLAN." | Fiber Operator | Moment of comprehension on one-port-many-customers model | "Enables wholesale connectivity slicing for regional operators" | Yes |
| Ben Wiechman (Arvig) | "With all their little islands, this would be really good product." | Fiber Operator | Unprompted identification of Hansen Telephone use case | "Solves fiber fragmentation challenges for rural operators" | Yes |
| Scott Shekels (Arvig) | "Actually, in the last few months, we've had three or four asked about it. I'm seeing an increase." | Fiber Operator | Market demand validation | "Cloud on-ramp demand is emerging in regional operator segments" | Yes |
| Tim Cunningham (CyrusOne) | "Once the handoff is to AWS, that's it. Sorry, there's nothing else we can help you with." | Colocation | Current state frustration | "Colocation operators lose visibility at cloud handoff points" | Yes |
| Tim Streeter (CyrusOne) | "Or we provision it on behalf of our clients and we are in control of their network." | Colocation | Desired state: white-label sovereignty | "Operators need control and visibility for white-label cloud services" | Yes |
| Tim Streeter (CyrusOne) | "Yeah, that right there is something that customers and us have dealt with constantly." | Colocation | Resonance on end-to-end visibility | "End-to-end cloud visibility is table-stakes for modern operators" | Yes |
| Zach Smith (Datum) | "Everybody who's basically got space and power and capital is like, I'm in the GPU business. And they don't know a lot about this other stuff." | Neocloud | Describing GPU provider market blindness | "GPU/inference providers have networking expertise gaps" | Yes |
| Zach Smith (Datum) | "Most people don't even know that they have an observability problem, but they know that they're too slow." | Neocloud | Positioning observability as latent pain | "Lead with performance pain before selling observability" | Yes |
| Zach Smith (Datum) | "It's virtual telco." | Neocloud | Self-framing of what Datum is building with MaiaEdge | "Platform-as-backbone positioning for neocloud operators" | Yes |
| Zach Smith (Datum) | "If we can do this without them having to do that — like, that would be really powerful... like, it's magic." | Neocloud | Bar for product experience (easy button requirement) | "Solutions must feel like magic, not projects" | Yes |
| Zach Smith (Datum) | "We're pretty early, which is awesome, because we can all do stuff." | Neocloud | Signal of openness to co-development | "Early-stage partnership signal; willingness to shape roadmap" | Yes |
| Alexander Wiese (Ecotel) | "This will be great, especially in the fragmented fibre market in Germany." | Fiber Operator | Resonance on federation for European markets | "Federation solves fragmented European fiber market challenges" | Yes |
| Alexander Wiese (Ecotel) | "Impressive. Impressive to be honest. It happened a lot since the last time I saw this portal." | Fiber Operator | Product velocity and maturity signal | "Returning prospects see rapid product evolution" | Yes |
| Alexander Wiese (Ecotel) | "White labeling is always good to be honest." | Fiber Operator | White-label portal feature resonance | "White-label sovereignty is key differentiator for service providers" | Yes |
| Alexander Wiese (Ecotel) | "I think it's really straightforward, so I got it." | Fiber Operator | Product simplicity validation | "Product message is clear and intuitive" | Yes |
| Alexander Wiese (Ecotel) | "I'm really looking forward to test this, to be honest." | Fiber Operator | Strong buying signal | "Prospect eager to move to POC immediately" | Yes |
| Deepak Karpoor (UAE) | "They have very, very good infrastructure... To operationalize it, really commercialize it — there are blaring gaps." | International | UAE ecosystem commercialization gap articulation | "Sovereign infrastructure without operationalization = unrealized value" | Yes |
| Deepak Karpoor (UAE) | "They will not know they have made magic. Because in one word they could see those things. Here they will not be able to see." | International | Visibility pitch framing | "Invisibility of ecosystem progress without unified observability" | Yes |
| Deepak Karpoor (UAE) | "I asked them what security and network infrastructure do I need to spin up a POC of your software. They have no idea. These developers are researchers. They're biotech guys. Space tech guys. Nobody knows anything about network and security." | International | Developer enablement gap validation | "Researchers/scientists lack network/security knowledge for infrastructure" | Yes |
| Deepak Karpoor (UAE) | "That last slide was powerful. That is something that could be extremely helpful if we can get every visibility of every segment performance of every segment... And policy control can be automated across all segments from a single place." | International | Telemetry/visibility moment of resonance | "Spontaneous validation of telemetry/visibility story" | Yes |
| Deepak Karpoor (UAE) | "I don't aspire to rebuild what you're doing. If you have capabilities, I want to be able to very rapidly leverage some of it and get them to realize value soon." | International | Ideal partner profile articulation | "Looking for execution layer, not competing product" | Yes |
| Jason Gintert (Gintert) | "They're gonna be in regions where they don't know what they're gonna have access to... I wonder if MaiaEdge could do what I'm thinking — transport-independent service, being able to get Layer 2 services wherever you want them." | MSP | Core edge deployment use case in prospect words | "Transport-agnostic connectivity for ruggedized edge deployments" | Yes |
| Jason Gintert (Gintert) | "Who's gonna manage the shit in this thing? And they're like, we didn't really think about that." | MSP | "Easy button" messaging validation | "Operators need to abstract networking complexity from customers" | Yes |
| Jason Gintert (Gintert) | "The more PBCs you get connected, the bigger my customers' network reach could be. That's pretty cool." | MSP | Spontaneous federation flywheel articulation | "Federation compounding effect understood by prospects" | Yes |
| Tom Parker (White Fiber) | "So you can extract the — we have the contract with Megaport, but then the customer goes, 'Okay, it's White Fiber's direct connect to AWS or whatever.' It's on the back end." | Neocloud | White-label + sovereignty understanding | "APIs abstract provider relationships; customer sees branded connection" | Yes |
| Tom Parker (White Fiber) | "Once you have that integration, it's yeah — it makes you sticky. Having the 'right once, run anywhere' kind of thing." | Neocloud | Multi-provider API abstraction as moat | "Vendor switching costs created through abstraction layer" | Yes |
| Tom Parker (White Fiber) | "Inference is super latency — time to response — anything you do to bring that down, that's the real value." | Neocloud | GPU/inference value prop | "Latency reduction is highest value for inference platforms" | Yes |
| Tom Parker (White Fiber) | "It definitely seems interesting — it would usually make our offering a bit more robust, especially when you get a lot of hybrid customers." | Neocloud | Hybrid connectivity gap validation | "Hybrid (on-prem + cloud) connectivity is key product gap" | Yes |
| Chris Painter (Verizon) | "I'm only in five of the 10 that they want... it's going to go to somebody else." | Network Operator | Lost deal articulation | "Limited footprint creates lost sales; direct revenue impact" | Yes |
| Chris Painter (Verizon) | "It's not like an SDN network where you can just cherry pick the access. It's either on my fabric or you're not." | Network Operator | All-or-nothing fabric model pain | "Autonomous fabric builds lack flexibility for footprint extension" | Yes |
| Chris Painter (Verizon) | "I don't have to drag fiber everywhere — I want to give you the layer two solution everywhere." | Network Operator | DIA-as-underlay economic justification | "Economics of DIA vs. fiber extension for remote sites" | Yes |
| Chris Painter (Verizon) | "We don't know anything about what's going on with AT&T — this would give us a lot more visibility of what's going on there." | Network Operator | Off-net visibility pain articulation | "Visibility into partner segments drives better troubleshooting" | Yes |
| Chris Painter (Verizon) | "You can scale your footprint without scaling costs." | Network Operator | Footprint economics anchor | "Core economic message for service provider expansion" | Yes |
| Chris Painter (Verizon) | "Maybe I'm thinking about this all wrong... I connect to whoever at 100 gig Internet. They can order 100 gig Internet at the side and your box is gonna build the layer two over Internet." | Network Operator | Moment of reframing on DIA model | "Mental model shift from dedicated fiber to DIA underlay" | Yes |
| Kathryn Jones (Telstra) | "So you're making a static piece of digital infrastructure programmable and actually visible." | Fiber Operator | Core value prop in customer words | "Fiber as programmable, discoverable asset (not just cost base)" | Yes |
| Kathryn Jones (Telstra) | "We're trying to stop [overbuild] — that's a huge drain on our P&L." | Fiber Operator | Stranded fiber monetization urgency | "Existing overbuilt fiber as P&L drag; need dynamic allocation" | Yes |
| Kathryn Jones (Telstra) | "Using what we've got already and working out… would that still meet the capacity requirements… rather than going and actually building." | Fiber Operator | Fiber reuse over new construction | "Dynamic allocation of existing capacity vs. new build economics" | Yes |
| Manuel (Flo Networks) | "We never use the word cloud on ramp here." | Fiber Operator | Market underpenetration validation | "Regional operators unaware of cloud on-ramp opportunity" | Yes |
| Manuel (Flo Networks) | "We don't provide it, but we can get you to Databank and then it's on you." | Fiber Operator | Current customer experience gap | "Default response abandons customer to third party" | Yes |
| Manuel (Flo Networks) | "We're missing some of that revenue. We don't know how much because we don't understand that business at all." | Fiber Operator | Blind spot and hidden revenue | "Executive admission of market gap; urgency to act" | Yes |
| Manuel (Flo Networks) | "I need to find a way to sell it internally." | Fiber Operator | ROI/business case requirement | "Operators need executive-ready materials for internal selling" | Yes |
| Manuel (Flo Networks) | "More than simplifying the provisioning process for our own customers... I would like to see the marketplace and see and understand it so I can talk about it." | Fiber Operator | Marketplace perceived as key value driver | "Marketplace is primary value, not just automation" | Yes |
| Manuel (Flo Networks) | "That's one of the reasons why ENNI doesn't scale very well is 'cause you run out of VLANs pretty quickly." | Fiber Operator | Technical differentiation vs. ENNI | "Independent VLAN domains per port = scalability advantage" | Yes |
| Shane Hoff (Granite) | "It's making sense to me. I don't quite get all of it, I'll be honest, but I think we'll pull the right people in and we can vet it out a little bit more and figure out how it can become part of the puzzle for us." | MSP | Honest engagement despite complexity | "Need for simpler collateral; signals internal champion needed" | Yes |
| Shane Hoff (Granite) | "Once they sign a contract, they want to deliver tomorrow. And one of the things that can help determine who wins and loses is who's able to execute the quickest." | MSP | Speed-to-revenue value prop | "Execution speed is competitive differentiator for service aggregators" | Yes |
| Shane Hoff (Granite) | "We got to coordinate with people on site. We got to deal with the carriers. We got to place orders, wait for them to do their part." | MSP | Provisioning complexity pain articulation | "Multi-stakeholder coordination is operational burden" | Yes |
| Paul Weterman (euNetworks) | "We don't want to throw human beings at it. We want to do this in a very automated way from the start." | Network Operator | Automation as priority for off-net strategy | "Captures automation as minimum bar for off-net" | Yes |
| Paul Weterman (euNetworks) | "If it's 70% on net and 30% off net, yes, then we would like to have a seamless solution to be able to offer that commercially competitive and also give the customer good experience technically." | Network Operator | Realistic off-net use case framing | "Defines incremental extension, not transformational shift" | Yes |
| Paul Weterman (euNetworks) | "Opportunities are largely off net no bid." | Network Operator | Revenue leakage from off-net inability | "Currently walking away from off-net deals" | Yes |
| Paul Weterman (euNetworks) | "I still don't fully get it, but I need to let this sink in." | Network Operator | Abstraction complexity barrier | "Need simpler explanation for service provider audience" | Yes |
| Paul Weterman (euNetworks) | "That's not like, you know, you put in a PBC and then hey, a magic wand and everything will work." | Network Operator | Integration concern with existing systems | "Need to address BSS/NIM/router config reality" | Yes |
| Carl Delaney (euNetworks) | "If we're going off net and we're seeing worse margins, how do we control the experience and drive the best possible customer experience?" | Network Operator | Margins + experience as core value prop | "Summarizes key pain: maintaining SLAs off-net with lower margins" | Yes |

---

## Key Objections Heard Across All Calls

| Objection | Who Said It | Segment | Recommended Rebuttal |
|---|---|---|---|
| "Another box in the network" / internal resistance to new CPE | Chris Painter (Verizon), generic internal stakeholder concern | Network Operator | Offer reference architecture where PBC sits at partner side (e.g., Arvig), not in your network. Emphasize CPE sovereignty and white-label angle. If needed, focus deployment at aggregation points first. |
| "We don't understand the cloud on-ramp business at all" | Scott Shekels (Arvig, initially) | Fiber Operator | Offer business case analysis with specific math: 50-70% gross margins, breakeven at 3-4 customers on shared port. Provide templated cloud on-ramp business case. Share comparable operator success stories. |
| "Is this just another Megaport/Equinix Fabric?" / Will we lose customer relationships? | Deepak Karpoor (UAE), Tom Parker (White Fiber implied) | International / Neocloud | Clearly differentiate: MaiaEdge is infrastructure + intelligence for *operators*, not a resold network. Operators maintain branded portal, customer sovereignty, and visibility. Megaport/Equinix are NaaS; MaiaEdge enables *you* to be the fabric. |
| "How do we monetize this / evangelize it?" | Scott Shekels (Arvig) | Fiber Operator | Describe marketplace discovery (ConnectBase integration), word of mouth, and specific positioning (e.g., Minneapolis on-ramp hub). Provide go-to-market playbook. Position as new revenue stream, not cost optimization. |
| "We have existing Megaport relationship / in conversations with them" | Kathryn Jones (Telstra), euNetworks team | Fiber Operator / Network Operator | Positioned as complementary and additive. MaiaEdge makes Megaport more efficient while enabling services beyond Megaport's frame (federation with non-Megaport carriers, sovereign routing, end-to-end visibility). Not either/or. |
| "Can't commit resources for POC on short notice" | Paul Weterman (euNetworks) | Network Operator | Respect timeline constraints. Defer to Q2 2025 appropriately. Offer to lead with proof points (Ecotel, CMC Networks) in follow-up. Position as nurture, not lost deal. |
| "I'm not the technical/financial decision-maker" | Tom Parker (White Fiber), Shane Hoff (Granite) | Neocloud / MSP | Provide shareable materials (slide deck, one-pager). Offer to schedule technical deep-dive with actual decision-makers. Leverage warm introduction from known contact (e.g., Brad for Jason Gintert). |
| "MTU/fragmentation complexity over IP transport" / skepticism about technical approach | Jason Gintert (Gintert) | MSP | Explain auto-frag/defrag between PBCs (transparent to applications). Reference 128T production experience as proof. Offer technical deep-dive session on fragmentation/reassembly architecture. |
| "White-box/custom switch supportability" / "Who supports it when it breaks?" | Jason Gintert (Gintert) | MSP | Acknowledge lesson from 128T. Explain pivot to SW license model on popular Cisco/Juniper/Arista switches. Custom integration via professional services. Software model reduces support burden. |
| "What's new here vs. Equinix Fabric?" | Paul Weterman (euNetworks) | Network Operator | Differentiate on: (1) federation across multiple carriers (not just one fabric), (2) DIA flexibility, (3) operator sovereignty/visibility, (4) end-to-end observability across provider boundaries. Create battle card clarifying Equinix Fabric vs. MaiaEdge positioning. |
| "It's too abstract / I don't fully understand integration with our systems" | Paul Weterman (euNetworks) | Network Operator | Offer to include technical integrators (Amplify, ConnectBase). Explain Sonata adapter approach. Simplify demo to focus on user workflows, not architecture. Include integration specialists in follow-up call. |
| "How do you control quality on DIA? There's no SLA on DIA." | Paul Weterman (euNetworks) | Network Operator | Position DIA as instant-start option with fiber replacement later. Reference growing enterprise acceptance of DIA for WAN. Discuss tiered SLAs (best-effort DIA vs. guaranteed-bandwidth fiber). Not a blocker for initial pilots. |
| "Bandwidth definition ambiguity over Internet underlay" / "How do you sell a 200 Meg EVC over best-effort broadband?" | Chris Painter (Verizon) | Network Operator | Explain operator defines ingress rate cap at path creation. On metro Ethernet or fiber, operator can provide guaranteed CIR with oversubscription. Position as tiered service: gold/silver/bronze tiers. DIA = silver tier with performance tracking. |
| "Azure Express Route provisioning complexity" / "I can't hide the provider location" | Chris Painter (Verizon) | Network Operator | Acknowledge known constraint (APIs to Equinix, not directly to Azure). Explain reverse provisioning via cloud profile as workaround. Note direct Azure integration on roadmap. This is implementation detail, not blocker. |
| "Existing infrastructure has limited programmatic ways to sell excess capacity dynamically" | euNetworks resonance (implicit) | Fiber Operator | Frame MaiaEdge as "inventory activation layer." Position as tool to make existing fiber work harder without rebuilding. Lead with asset monetization messaging, not technology. |
| "BGP replacement / CLI elimination resistance" | Tim Streeter (CyrusOne) implied engineering concern | Colocation | Reframe around business outcomes (EBITDA, agility). Use SAP/accountant analogy (transformation of underlying tools). Ask team to approach with open mind. Offer to demonstrate business impact before technical review. |
| "Need for test validation / proof points" | Manuel (Flo Networks) | Fiber Operator | Share sanitized test results from similar deployment (Mexico carrier EXFO results, 100% pass rate). Create reference customer program. Establish proof-point playbook. Accelerates sales cycle when prospects can leverage comparable success stories. |
| "Hardware cost / OPEX vs. CapEx procurement preference" | Manuel (Flo Networks) | Fiber Operator | Acknowledge this feedback; indicate flexibility to accommodate split CapEx/OpEx pricing. Work with finance team on carrier-appropriate terms (1/3/5-year lease, annual support split). Build pricing flexibility into commercial model. |
| "How will SLAs work with white-labeling?" | Alexander Wiese (Ecotel) | Fiber Operator | Acknowledged for follow-up. Need to clarify white-label SLA model: who owns SLA accountability, how metrics are reported, customer visibility into performance. Document in white-label offering materials. |
| "Operators need to focus on 70% on-net opportunity; off-net is incremental" | Paul Weterman (euNetworks) | Network Operator | Respect this framing. Pitch as complementary to on-net strategy, not replacement. Position for high-value off-net deals (70/30 split). Don't oversell off-net as primary go-to-market. Meet them where they are. |

---

## Competitive Intelligence from Calls

| Competitor | What Was Said | Who Said It | Implication for MaiaEdge |
|---|---|---|---|
| **Megaport** | "Megaport has published pricing. So your ability to bundle together cloud services in your circuits are highly diminished because customer just says, well I know it's Megaport." | Mike Miller (Arvig) | Margin compression risk with Megaport; opportunity for sovereignty/white-label alternative |
| **Megaport** | Leasing dark fiber from Arvig (511 to Databank Eagan). Published pricing seen as negative by Tim (margin compression). | Tim Ziemer assessment (Arvig call) | Megaport visibility creates pricing pressure; MaiaEdge offers operator-controlled pricing |
| **Megaport** | "Megaport is an active conversation at Telstra InfraCo." | Kathryn Jones (Telstra) | Megaport positioned as complementary partner, not competitive threat; integration story needed |
| **Megaport** | Mentioned as provider for off-net segments; concern is losing customer relationships if Megaport is the primary fabric. | CyrusOne, euNetworks | White-label/sovereignty positioning is MaiaEdge wedge vs. Megaport NaaS model |
| **Equinix Fabric** | "Equinix is one of our competitors, so [we don't have access to their fabric today]." | Tim Streeter (CyrusOne) | Competitive friction between colocation providers and Equinix; federation via third-party MaiaEdge customer is workaround |
| **Equinix Fabric** | "I can buy a 10 gig or 100 gig port of fabric. I can slice it up in VLANs, resell it to different customers. So what's new here?" | Paul Weterman (euNetworks) | Equinix perceived as primary competitive threat for established SPs; need clear differentiation (federation, sovereignty, end-to-end visibility) |
| **Equinix Fabric** | Arvig already has fiber/rackspace at Equinix Chicago; no Equinix on-ramp in Minneapolis creates geographic opportunity gap for MaiaEdge | Tim Ziemer assessment (Arvig) | Geographic gaps in Equinix coverage = opportunity for federation with regional operators |
| **Equinix** | "There's certain clients that ask if we can have access to connect to the Equinix fabric. And today we don't really... 'cause Equinix is one of our competitors." | Tim Streeter (CyrusOne) | CyrusOne sees Equinix as both competitor (colocation) and potential fabric partner (cloud); MaiaEdge solves this tension through federation |
| **Lumen** | "Lumen is not very happy that we exist" — competitive validation from Arvig context | Tim Ziemer assessment | Market recognizes MaiaEdge as disruptive to incumbent carrier/fiber provider models |
| **Lumen** | Mentioned as part of Verizon's existing partnerships; Lumen/Bell Labs call mentioned for next week (competitive intel on competing SP accounts) | Chris Painter (Verizon) | MaiaEdge actively engaging competitive SP accounts; creates urgency for Verizon decision |
| **Lumen Fabric** | Mentioned alongside Equinix, Megaport, Console Connect as incumbent fabric offering | Chris Painter (Verizon) | Incumbent carriers building proprietary fabrics; MaiaEdge federated model bypasses need for direct Lumen relationship |
| **Zeo** | Mike asked if MaiaEdge similar to Zeo's self-provisioning waves. | Mike Miller (Arvig) | Zeo perceived as potential competitor for network automation; Tim differentiated on complexity/cost (Zeo/Lumen spent tens/hundreds of millions) |
| **Alkira / Aviatrix** | Positioned as "spaghetti generators" that provision complex cloud routing behind scenes. | Tim Ziemer / Deepak Karpoor discussion (Deepak) | MaiaEdge differentiation: simpler (Layer 2 native Ethernet paths directly into VPCs, no cloud router needed) |
| **DriveNets** | White Fiber partner for scheduled fabric / RoCE-based networking (East-West fabric); complementary, not competitive. | Tom Parker (White Fiber) | DriveNets handles cluster networking; MaiaEdge handles inter-network (North-South). Positioned as complementary. |
| **Orange** | Active in conversations with MaiaEdge about federated marketplace model | Tim Ziemer reference (Deepak call) | Major European carrier interest in federation model; timing signal for broader carrier engagement |
| **Colt** | Mentioned as meeting partner; industry momentum signal | Manuel (Flo Networks) | Carrier/SP market consolidating around federation/marketplace concepts |
| **AT&T** | "If we're just reselling, you know whatever AT&T DIA fiber and we have no NNI... it still takes us you know 60 days to whatever to install it because we're waiting on AT&T." | Shane Hoff (Granite) | AT&T's provisioning cycles (60-90+ days) create pain; MaiaEdge's automation offers differentiation for resellers |
| **Verizon** | Mentioned as IXC (Granite context); also as major incumbent carrier with their own fabric initiatives | Shane Hoff (Granite), Chris Painter context | Verizon building internal layer-two-over-Internet initiatives; MaiaEdge already solved this problem |
| **Exerio** | Described as pure commercial aggregator (quote brokering, not technology-driven automation) | euNetworks resonance analysis | euNetworks appreciates technology-driven automation over quote brokering; MaiaEdge is infrastructure-first, not aggregation-first |
| **Equinix** | "Equinix is the number one colo provider in the planet and they don't have an on-ramp or an off-ramp here in Minneapolis." | Scott Shekels / Tim observation (Arvig) | Geographic gaps in Equinix coverage create franchise opportunity for regional operators like Arvig |
| **Groq (NVIDIA acquisition)** | Built 35 Equinix PoPs in 6 months with own Layer 2 backbone, achieving sub-100ms inference globally. | Zach Smith (Datum) | Aspirational benchmark for Datum; MaiaEdge enables neocloud to achieve similar outcomes without 6-month fiber build |
| **Juniper/128 Technology** | Prior relationship context; Ecotel mentioned prior relationship with 128T; Granite/Accutech context with founders | Multiple contacts | MaiaEdge team (Acme Packet, 128T pedigree) has credibility with operators familiar with Juniper/Acme history; use as trust signal |
| **Cisco** | Mentioned for switch support; existing Verizon bookended CPE model | Chris Painter (Verizon), product context | Cisco dominating enterprise switch market; MaiaEdge SW license model on Cisco switches reduces support friction vs. white-box |
| **Juniper / Huawei** | euNetworks uses for router configuration (proprietary in-house APIs) | Paul Weterman (euNetworks) | Integration complexity concern for euNetworks; Sonata adapter approach needed to abstract existing router configs |
| **SAP** | Mentioned as cloud provider target (S/4HANA integration interest from Ecotel) | Tim reference (Ecotel) | SAP as emerging vertical opportunity; integrate SAP cloud connectivity as dedicated use case |

---

## Ah-Ha Moments (Cross-Referenced)

| Moment | Company | What Triggered It | Why It Matters |
|---|---|---|---|
| One-port-many-customers model clicks | Arvig | Tim explained one-port-unlimited-VLANs model enabling wholesale to 200+ MSA telco partners | Business model suddenly makes sense for regional operators; revenue multiplier insight |
| Equinix access without competitive relationship | CyrusOne | Offered third-party MaiaEdge customer (IENTC/Atlantech) as Equinix port holder | Solves competitive friction; CyrusOne can access Equinix without direct relationship |
| Minneapolis on-ramp opportunity | Arvig | Tim noted Equinix has no on-ramp in Minneapolis + Arvig has Equinix Chicago fiber | Geographic positioning opportunity; market gap identified by prospect |
| Fiber islands use case | Arvig | Ben Wiechman spontaneously identified Hansen Telephone as customer with disconnected fiber islands | Internal champion activation; self-identifying use case = buying signal |
| Federation flywheel | Gintert / multiple | Tim explained as more PBCs connect, ecosystem value compounds | "Magic" moment; network effect understood intuitively |
| Virtual telco framing | Datum | Zach Smith self-described as "virtual telco" what Datum building with MaiaEdge | Operator sees themselves in positioning; ready to build on that identity |
| End-to-end visibility into VPC | CyrusOne | Demo showing AWS VPC status visible in MaiaEdge portal | "Yeah, that right there is something customers and us have dealt with constantly." — Technical moment of resonance |
| Repurposing idle/excess capacity | euNetworks | Business Development contact responded to "inventory activation layer" framing | Asset monetization messaging lands harder than technology pitch |
| Marketplace as new business channel | euNetworks | "I really like the marketplace focus... you can open up shop for people you haven't done business with yet" | European hub positioning for global carriers; new revenue stream, not just automation |
| Security & sovereign routing | euNetworks | Path control for AI/financial services clients; AES-256-GCM, country-level avoidance | Compliance requirements articulated; features become table-stakes, not differentiators |
| DIA as Internet underlay | Verizon | Chris mentally reframed from "need dedicated fiber" to "use any Internet, layer 2 over it" | Cost/footprint expansion model suddenly viable; operational model shift |
| Groq benchmark relevance | Datum | Tim mentioned Groq building 35 PoPs in 6 months achieving sub-100ms globally | Aspirational but achievable vision; MaiaEdge as execution vehicle for similar outcomes |
| AWS Service Link convergence | Datum | Zach spontaneously said "I was gonna say the exact same thing" when Tim mentioned Service Link | Alignment on low-friction model for non-technical neocloud customers |
| Programmable infrastructure | Telstra | Kathryn reframed: "So you're making static infrastructure programmable and actually visible" | Customer-voice articulation of core value; ready for testimonial use |
| Zero-touch provisioning for edge | Gintert | Smart hands deploy model (Guam hospital scenario) immediately resonated | Fits enclosure-as-a-service model without requiring local expertise |
| Layer 2 transparent failover over Starlink | Gintert | Tim explained failover transparent even over DHCP/Starlink | Transport uncertainty concern visibly resolved; de-risks edge deployments |
| White-label sovereignty | White Fiber | Tom understood "you have contract with Megaport, customer sees White Fiber direct connect" | Stickiness/moat concept landed; margin protection through abstraction |
| Multi-provider write-once integration | White Fiber | Tom grasped "write once, run anywhere" across Megaport/Equinix/future providers | Switching costs through integration; appeals to engineering efficiency concerns |
| Marketplace & new partner access | euNetworks BD contact | "Marketplace focus so you can open up shop for people you haven't done business with yet" | European hub positioning; APAC/Middle East carrier gateway opportunity |
| Automated NNI provisioning | euNetworks BD contact | "The route is already planned. MaiaEdge activates it — automatically." | Operational bottleneck elimination; 60-90 day cycle → same-day visibility |
| Payload transparency demo | multiple | Showed ability to see into cloud (AWS, Azure, GCP) from network side | Visibility beyond handoff point was repeated "aha" for colocation/SP buyers |
| Marketplace traction / carrier network expansion | Flo Networks | Tim mentioned London, Frankfurt, Paris, Los Angeles, Ashburn as new carrier deployments | Industry momentum; FOMO signal (others already moving forward) |
| Neocloud observability problem | Datum | "Most people don't know they have observability problem, but they know they're too slow" | Lead with latency, close with observability; phased value realization |

---

## Overall Market Intelligence

### Key Market Themes

**1. Fragmentation as Core Problem**
- Regional operators (Arvig, Ecotel, Ocean Networks, Telstra) all struggle with fragmented underlying infrastructure
- No programmatic way to stitch together disparate fiber providers
- MaiaEdge federation model directly solves this pain; messaging should lead with "unified view of fragmented network"

**2. Connectivity-as-Invisible-Infrastructure**
- Across all segments, prospect ideal is that connectivity "just works" without customer involvement
- Bhavesh (Accutech): "People don't really need to know, but everything works"
- Jason (Gintert): Deploy-and-forget model for unsophisticated buyers
- Messaging implication: emphasize automation and abstraction, not features

**3. Sovereignty > Optimization**
- Operators (CyrusOne, Telstra, euNetworks, Ecotel) want to maintain customer relationships and visibility
- Willing to trade some efficiency for control; willing to pay for white-label/branded experience
- Megaport/Equinix seen as margin-compressing because customer relationships shift
- MaiaEdge white-label positioning is core differentiator vs. incumbent NaaS

**4. Speed-to-Revenue as Tiebreaker**
- Multiple prospects (Granite, Verizon, euNetworks) identified execution speed as competitive winner
- 60-90 day provisioning cycles seen as unacceptable; same-day/week activation as table-stakes
- Automation messaging should emphasize "weeks not months" as primary value

**5. Developer/Researcher Blind Spot**
- GPU providers, AI startups, neocloud operators don't have networking expertise (Datum, White Fiber, Deepak UAE)
- Traditional NaaS solutions require too much customer-side config (VPC setup, BGP, Express Route setup)
- Opportunity for "abstraction layer" positioning in emerging AI/GPU segment

**6. Marketplace Concept Lands Organically**
- Multiple prospects spontaneously resonated with federation/marketplace idea
- Shane (Granite): "Amazon for network services" analogy worked immediately
- Zach (Datum): Federation flywheel understood intuitively
- Messaging implication: lead with marketplace concept early in sales engagement

**7. Geographic Arbitrage Opportunity**
- Regional operators (Arvig, Ocean Networks, Ecotel) see value in accessing major cloud hubs without building infrastructure
- Minneapolis as example: no Equinix on-ramp, Arvig has Chicago connection
- Federated model enables access without fiber build; "extend without capital" messaging strong

**8. Multi-Segment Applicability**
- Same core pain (connectivity fragmentation, manual provisioning, sovereignty loss) appears across fiber operators, MSPs, network operators, colos, neocloud
- One-message applicability across segments (with vertical-specific customization)

### Competitive Positioning Opportunities

1. **vs. Megaport/Equinix Fabric:** Lead with sovereignty, white-label portal, federation across multiple carriers (not locked to one fabric), end-to-end visibility
2. **vs. Incumbent Carriers (Verizon, AT&T, Lumen):** Lead with speed, simplicity, federation model that doesn't require carrier permission, DIA-as-interim path, footprint extension without fiber build
3. **vs. SD-WAN/Alkira:** Lead with Layer 2 simplicity (no cloud router needed), native infrastructure approach (not overlay), pure connectivity vs. application management
4. **vs. Internal builds (CMS, euNetworks):** Lead with "focus on your core; let us handle federation," speed-to-value, reduced engineering burden

### Operator Profile Insights

**Most Receptive Segments:**
1. **Regional Fiber Operators** (Arvig, Ocean Networks, Ecotel, Telstra) — fragmentation problem is acute; federation directly solves; revenue opportunity clear
2. **Neocloud/GPU Providers** (Datum, White Fiber) — latency/observability pain is acute; traditional NaaS too complex; abstraction layer positioned as competitive necessity
3. **MSPs Without Fiber** (Granite) — can't build infrastructure themselves; marketplace access = new business line; footprint extension without capital

**Most Challenging Segments:**
1. **Major Incumbent Network Operators** (Verizon, euNetworks) — internal political friction; existing vendor relationships; requires executive sponsorship to overcome "another box" objection
2. **Pure Colos** (CyrusOne) — engineering team BGP/CLI resistance; need for internal champion coaching; timeline extended

**Most Strategic:**
1. **Accutech + Azure Local** — unlocks sovereign cloud/AI as new market segment; Tim flagged as "on-ramp to hockey stick"; positioned early in category

---

## References for Sales Engagement

- **For Fiber Operator Pitch:** Lead with "fragmented market coordination," "cloud access simplification," "white-label sovereignty." Use Ecotel as warm proof point (German market success).
- **For MSP Without Fiber:** Lead with "footprint extension," "marketplace new business line," "2,200 fiber operators access." Use Granite as archetype.
- **For GPU/Neocloud:** Lead with "latency/observability," "infrastructure abstraction," "write-once-run-anywhere integration." Use Datum/White Fiber as proof points.
- **For Network Operators:** Lead with "off-net strategy automation," "customer sovereignty," "DIA flexibility for non-lit buildings." Acknowledge "another box" objection upfront; offer reference architecture showing partner-side deployment.
- **For Colocation:** Lead with "end-to-end cloud visibility," "Equinix access without competitive conflict," "customer relationship control." Use CyrusOne scenario.

---

## Deal Momentum & Timeline Summary

| Company | Status | Timeline | Confidence |
|---|---|---|---|
| Accutech | Discovery → Partnership | Q1 2026 (face-to-face planned) | High (already customer of Dave Williams/Revnet) |
| Arvig | Discovery → Technical Deep-Dive | Q1 2026 (next call scheduled) | Medium (customer demand validated, team alignment needed) |
| CyrusOne | Discovery → Internal Review | Q1 2026 (engineering review underway) | Medium (strong interest, internal politics risk) |
| Datum | Discovery → Co-Design | Q1 2026 (GTC March meeting planned) | High (CEO engaged, phased go-to-market agreed) |
| Ecotel | POC Confirmed | Q4 2025 (ships early December) | High (warm deal, zero objections, Alexander leading) |
| Flo Networks | Discovery → Pricing/Marketplace Demo | Q4 2025 (exec meeting Nov 10 drives timeline) | Medium-High (needs internal selling, timeline sensitive) |
| Granite | Discovery → Internal Champion Engagement | Q1 2026 (Brian O'Connell next step) | Low-Medium (early stage, needs education) |
| Gintert (Bits in Flight) | Discovery → Technical Demo | Q1 2026 (60-90 day revisit) | Low (very early, end customer prototyping) |
| Ocean Networks | POC Confirmed | Q1 2026 (agreement signed, implementation early 2026) | High (strong buying signals, Kyle POC walkthrough planned) |
| Telstra | Strategic → Q2 2025 Re-Engagement | Q2 2026 (Dipan Patel meeting planned) | High (Kathryn championing, australia priority) |
| euNetworks | Nurture → Q2 2025 Re-Engagement | Q2 2026 (deferred due to internal GTM) | Medium (not ready now, Ecotel/CMC will be proof points) |
| Verizon | Discovery → Internal Selling | Q1 2026 (Chris needs deck for boss meeting) | High (multiple aha moments, 5G/FWA timing, Chris momentum) |
| White Fiber | Discovery → Technical Demo | Q1 2026 (target mid-February) | Medium (network architect needed for decision) |
| Deepak Karpoor (UAE) | Channel/Partnership → Full Demo | Q1 2026 (Core42 meeting pending, full demo needed) | Medium (partnership opportunity, not direct sale) |

---

**Document prepared by:** MaiaEdge Sales & Product Intelligence
**Classification:** Internal Use Only / Confidential
**Next Review:** March 2026 (post-GTC, post-Ecotel POC, post-euNetworks Q2 re-engagement)
