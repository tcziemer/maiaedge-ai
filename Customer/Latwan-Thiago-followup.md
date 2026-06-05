# Latwan / Thiago Follow-Up

## Recommended documents to send

1. **MaiaEdge overview deck** — the slides you walked him through on the call. He explicitly asked for this. Sets the frame before the engineers dig in.
2. **PBC & PCE Datasheet** — answers the first questions his technical team will have: Q-in-Q handoff, jumbo frame handling, line-rate AES-256 encryption, dual 100GbE, deterministic PCE routing, no BGP/MPLS. This is the core technical reference.
3. **Integrated Switch (Port Extender) Datasheet** — relevant given he runs multi-customer aggregation; the 48-port fan-out is exactly the per-customer / per-VLAN use case he was probing.
4. **Carrier test / performance results** — he asked for these directly. Send the DIA end-to-end Ethernet performance data and any homologation status for LatAm.

Hold the business-case model and pricing detail for the technical call; lead with capability first.

---

## Draft follow-up email

**To:** Thiago
**Subject:** MaiaEdge follow-up: deck, datasheets, and getting your engineers on a call

Thiago,

Great meeting you. Latwan's footprint across 39 countries with DIA, broadband, fixed wireless, and Starlink is exactly the kind of network where federated private paths open up new services, so I enjoyed the conversation.

As promised, here is what we covered plus the technical detail for your team:

- The overview deck we walked through
- The Path Border Controller and Path Computation Engine datasheet (Q-in-Q handoff, jumbo frame handling, line-rate AES-256 encryption, deterministic routing with no BGP)
- The Integrated Switch datasheet for the per-customer port fan-out we discussed
- Carrier test results showing end-to-end Ethernet performance over DIA

A few things worth flagging for your engineers, since they map to what you asked about:

To connect two customer sites that only have DIA, your team provisions a private Ethernet path in minutes between a PBC at the site and a PBC in the data center. Ethernet in, Ethernet out, no IP addresses to manage. Because it is Layer 2, a cutover from fiber to Starlink does not reset the VPNs riding over it. And unlike reselling Megaport, you keep your brand, your customer relationship, and the full margin.

The 1G CPE for the customer premise ships in September. If you have a near-term need before then, I can offer the larger device as an interim path so you are not waiting.

The best next step is getting your technical team on a call so we can go as deep as they want. Who should I include, and what does your week after next look like?

We are already shipping our first equipment into Brazil through a local final-assembly partner, so we are set up to support the region.

Best,
Tim

Tim Ziemer
CRO and Co-Founder, MaiaEdge
