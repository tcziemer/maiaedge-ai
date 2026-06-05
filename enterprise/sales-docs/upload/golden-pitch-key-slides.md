# MaiaEdge Golden Pitch â€” Key Slides

> Converted from: 21037 MaiaEdge_Golden Pitch-KeySlides.pptx

## Slide 1
1  Â© 2026 MaiaEdge

## Slide 2
Cover title
Subtitle
2  Â© 2026 MaiaEdge

## Slide 3
Divider line 1line 2
Subtitle line 1
3  Â© 2026 MaiaEdge

## Slide 4
Al Infrastructure Demand
Tools today are not built to enable this. 
Â© 2026 MaiaEdge, Inc. | Confidential
Enterprise Expectations
Competitive Pressure
AI Inference changes and demand for instant, high-bandwidth private connectivity.
Customers accustomed to instant cloud and security services.
Tighter margins. Competitors who can deliver more, faster. 
Industry Landscape 
Placeholder. MaiaEdge team to determine what the first slide should be. 
Tim, still struggling with this one. I donâ€™t know if the audience wants the history lesson, but I also understand the challenge of the industry landscape feeling too macro for the people we talk to. 

## Slide 5
6 months of complex provisioning
Operation friction limits ability to meet customer demands
NaaS Fabric = loss of sovereignty
Reality  
NOTE: Keeping as separate slides for proofing round. We can combine as a build for final deliverable (currently a morph), but this will also add complexity for editability where text will be layered.
NOTE: Should we add any pain points from the reference slide?e.g., 700 Aggregate switches, etc. 
2 slides is fine for simplicity. This feels more cohesive. 
We can keep the SPs all the same size. Don't need the squiggly lines around the SPs.Â 
We could bring in some of the pain points if we can represent them as adding to the operation friction, without the slide getting too busy.  
Manual Configs
DC Cross Connects Ordered 
100 Edge POPs
700 aggregate switches 
VLAN negotiation 
Added a couple labels. 
Label: Meet me room
Label: NNI Bottleneck

## Slide 6
Reality 
NOTE: Pulled pain points from speaker notes
On-rampMany simply canâ€™t reach those fabrics easily
SovereigntyNo one wants to hand over the customer relationship
ComplexityItâ€™s hard to front-end those systems without heavy development
Standard Ethernet NNI IP Based and Cloud Native NNI
NOTE: Do we need to label this diagram and, if so, should previous diagram also have label?
Label: Centralized NaaS Fabrics 

## Slide 7
Current Reality: A Manual bottleneck at massive scale
This operational friction limits the ability to profitably scale DC interconnect, wholesale Ethernet, and cloud on-ramps.
Â© 2026 MaiaEdge, Inc. | Confidential
Manual Provisioning
Pain Points
Every new circuit needs multi-team VLAN negotiation
Manual, per-device
configurations on
aggregators at both ends
Complex coordination
with data center operators
for cross-connects.
Inconsistent, per-device
configs for different
service classes..
800k existing EVC Configs
700 Aggregate switches
100 Edge POPs
Reference slide â€“ another way to show the complexity of stitching together isolated networks. 

## Slide 8
8  Â© 2026 MaiaEdge
Showing 
Complex and time consuming to connect each customer to the DC. No connective thread between the DCs or connected or connected but manual to provision across them. 
Expensive and manual to connect to cloud 

## Slide 9
SyncHub Federates Infrastructure.
MaiaEdge Federates Network.
Without MaiaEdge
With MaiaEdge
CORVA 
SyncHub
$$
$$
$$
$$
$$
$$
CORVA 
SyncHub
MaiaEdge provides the network orchestration layer for CORVA Middle.
Deploy PBC.    Few clicks.   Then instant connectivity across Fiber or DIA between 2 ethernet endpoints.
6-9 months
6-9 months
6-9 months
6-9 months
+
Â© 2025 MaiaEdge, Inc. | Confidential
Reference Slide. Donâ€™t need to update. 

## Slide 10
The Shift:Federated Private Networking  
Automated provisioning 
across siloed domains 
Ecosystem that protects sovereignty
End-to-end visibility
An operator-owned and managed private network ecosystem. 

## Slide 11

## Slide 12
12  Â© 2026 MaiaEdge
The Infrastructure
Push-button easy and hardwire simple
Path Border Controller (PBC)
Dual 100 GBPS interfaces
Merges layer 2 and 3 
Plug and play at the edge
Path Computation Engine (PCE)
Cloud-native orchestration 
End-to-end visibility 
Multi-tenancy 

## Slide 13
13  Â© 2026 MaiaEdge
The Infrastructure
Push-button easy and hardwire simple
Path Border Controller (PBC)
Dual 100 GBPS interfaces
Merges layer 2 and 3 
Plug and play at the edge
Path Computation Engine (PCE)
Cloud-native orchestration 
End-to-end visibility 
Multi-tenancy 
Port Extender
Integrated switch 
48x 10/25G & 8x 100G ports
Less than 500ns port to port
Have image of  switch with logo more defined. 
Guessed at key bullets. Moved the longer stats to the notes. 

## Slide 14
Instant Private Connectivity, Anywhere  
Match format of previous slides, Add side bar to call out key points: 
Automated provisioning â€“ No routing protocols 
Merge L2 and L3 
End to end visibility and QoS control 

## Slide 15
SERVICE NNI
Sovereign
Merge this slide with the above slide. â€“Â Build is fine 
Text: 
â€œAutomated provisioning 
End to end visibility
Sovereignty in-tactâ€ 
(partner with NaaS, donâ€™t hand over customer relationship). 
Want to show that it can be a provier between Megaport. Donâ€™t need network Provider #6 in the second slide

## Slide 16
16  Â© 2026 MaiaEdge
Solution 
Seamless fabric between DCs 
Automated provisioning between DCs 
Hop by hop visibility between DCs 
Simplify access to cloud and the rest of the world through federated partnerships. 

## Slide 17
17  Â© 2026 MaiaEdge
We can ditch the laptop idea.Â 

## Slide 18
18  Â© 2026 MaiaEdge
We can ditch the laptop idea.Â 

## Slide 19
Old/ Reference Slides
19  Â© 2025 MaiaEdge

## Slide 20
The Shift - Federated Private Networking 
20  Â© 2025 MaiaEdge
Automated provisioning across siloed domains
Ecosystem that protects sovereignty
End-to-end performance control and hop-by-hop insights 
Your 
Network
Other Carriers
Can talk to both scenarios onone slide

## Slide 21
21  Â© 2025 MaiaEdge
Core Network
Untouched
Fiber/DIA to other POPs or DCs
Additional Details to speak to common questions.
Infrastrcuture not NaaSÂ 
PBCs are placed at the Ethernet boundary, not in the routing core.
No BGP, MPLS, or other core protocol changes are required.
Works with your existing aggregator switch infrastructure.
The PBC only sees traffic connected to its port and does not inject your core network state.

## Slide 22
End to End Connectivity Model
Integrated switch - plug-and-play
Drop-in deployment at the site
Turnkey Dropbox-style visibility
Integrated with Equinix APIs
Primary
Secondary
v
POP B
Primary
Secondary
v
POP A
Switching Fabric
Fiber
Fiber
Customer 2
Customer1
DIA
DIA
End-to-End Encryption between PBCs
Primary transport: Fiber connectivity
Failover options: DIA-based backup
No routing protocols required
v
Â© 2026 MaiaEdge, Inc. | Confidential

## Slide 23
Title in gold using Tomorrow bold in sentence case at54pts
Subtitle in white using Arial regular in sentence case at 24pts
Â© 2026 MaiaEdge

## Slide 24
24  Â© 2026 MaiaEdge
Body copy first level in black using Arial regular in sentence case at 24pts
Body copy first level in black using Arial regular in sentence case at 24pts
Body copy second level in black using Arial regular in sentence case at 20pts
Body copy third level in black using Arial regular in sentence case at 18pts
Body copy third level in black using Arial regular in sentence case at 18pts
Title in black using Tomorrow bold in sentence case at 40pts

## Slide 25
25  Â© 2026 MaiaEdge

## Slide 26
26  Â© 2026 MaiaEdge
Order of colors used
01
02
03
04
05
06

## Slide 27
27  Â© 2026 MaiaEdge
Default settings
Line style
Arial at 18pt
Default text box
Top/left
Black
Line spacing 1.0
Space before 6pts
For Alt Text Styles only â€“ use layout placeholders for bulleted lists
Style Default
NOTE: Arrow style is for visual reference and due to PPT limitations, canâ€™t be set as default. 
Please apply this style manually.
SIZE
STYLE
Theme fonts
Tomorrow (heading)
Arial (body)
Header in Tomorrow bold
Body copy in Arial regular 
Sentence case