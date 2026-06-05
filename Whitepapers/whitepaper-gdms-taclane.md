# TACLANE + MaiaEdge: Reference Architecture

**A reference architecture for bandwidth-class federal programs deploying GDMS TACLANE across diverse underlay paths.**
*TACLANE inline. MaiaEdge outer transport on Intel IPU. Each in its certified position.*

---

## Executive Summary

GDMS TACLANE is the fielded standard for high-assurance inline encryption across United States federal programs. MaiaEdge is a hardware-accelerated outer transport built on Intel Infrastructure Processing Unit (IPU) silicon. This paper describes how the two pair to address one of the persistent problems in federal program deployment today: lighting bandwidth-class diverse paths fast enough to keep pace with mission timelines.

In the reference architecture, TACLANE pairs sit exactly where they sit today, inline at each endpoint, providing classified-grade encryption end to end. MaiaEdge sits beneath them as a Layer 2 transparent outer transport that blends fiber, LEO satellite, and commercial internet into a single managed underlay. TACLANE handles confidentiality. MaiaEdge handles transport. Each does what it is best at, and neither has to be re-certified to deploy alongside the other.

The opportunity is shared. Programs that have been transport-gated can stand up TACLANE pairs in days rather than months. Diverse paths that previously could not be lit fast enough become candidates for high-assurance traffic. Higher-bandwidth TACLANE variants enter programs that used to settle for less because the underlying transport could not be deployed on the program's timeline.

MaiaEdge welcomes a conversation with GDMS about joint validation of this reference architecture, with TACLANE in path, at MaiaEdge's Boston facility or the GDMS engineering presence in Taunton.

---

## A Shared Opportunity

Federal programs in 2026 need two things from their transport architecture: encrypted throughput at the bandwidth modern missions demand, and resilient diversity across underlays the program can deploy on its actual timeline. TACLANE solves the encryption side at high assurance. The transport side is where program timelines still slip.

A federal program ready to field TACLANE pairs at 10 Gbps, 100 Gbps, or beyond is often waiting on something other than the encryption itself. Dedicated fiber installs at federal venues regularly run 90 to 180 days from order to lit service. New diverse paths require their own L3 integration before they can carry production traffic. Coordination across multiple transport vendors, underlay types, and certification reviewers extends the schedule further. By the time the transport is ready, the mission window has often moved.

The TACLANE pairs were ready months earlier.

The reference architecture in this paper moves transport off the critical path so that TACLANE deployments are no longer waiting on it. Both companies see their products fielded sooner, in more programs, across more underlays.

---

## What the Architecture Does

The architecture is composed of TACLANE pairs at each endpoint in their fielded role, the MaiaEdge Path Border Controller (PBC) on Intel IPU silicon at each network boundary as the outer transport, and a path computation engine running in customer-managed cloud that orchestrates the underlay selection. Layer 2 transparency ties the layers together: anything above the outer transport, including the TACLANE session itself, sees an end-to-end Ethernet path while the underlay blends fiber, LEO, and commercial internet beneath it.

![Reference Architecture: TACLANE + MaiaEdge](assets/diagrams/taclane-architecture-diagram.svg)

### TACLANE in its certified position

TACLANE pairs sit exactly where the program has fielded them: inline at each endpoint, providing classified-grade encryption end to end. The reference architecture introduces no new component into the certified path, requires no change to TACLANE's certification posture, and does not modify the operational model TACLANE customers and program offices are already familiar with. From TACLANE's perspective, the reference architecture is an Ethernet path.

### MaiaEdge on the IPU as the outer transport

Beneath the TACLANE pair at each end, the MaiaEdge PBC executes path instructions from a cloud-managed control plane, encrypts at line rate with AES-256-GCM, and continues forwarding deterministically even if the control plane is unreachable. Sub-2-microsecond latency overhead. 100 Gbps line-rate throughput. Hardware-accelerated packet processing yields a tight, predictable jitter envelope, well-suited to the time-sensitive workloads TACLANE customers run.

### Layer 2 transparency

Because the outer transport carries Layer 2 frames, TACLANE sessions, IPsec tunnels above TACLANE, and the L3 routing design behind it see a stable end-to-end path while the underlay blends. TACLANE rekeying continues normally on its own schedule. The L3 routing design is unchanged. Programs do not have to re-engineer the high-assurance encryption stack to gain underlay diversity.

---

## Why This Matters for TACLANE Programs

The reference architecture expands the addressable footprint of TACLANE in three concrete ways.

Programs that have been transport-gated can field TACLANE on the program's actual timeline. Many mission profiles already identified TACLANE as the right answer on the encryption side, then deferred or descoped because the transport could not be deployed in time. With MaiaEdge accelerating the transport side, those deployments move from deferred to active, with TACLANE pairs in path from day one.

Diverse paths that previously could not be lit fast become candidates for high-assurance traffic. LEO satellite, commercial internet, and partner-provided underlays are all in scope when the outer transport handles them as a blended fabric. Each new path that becomes a candidate is a new potential TACLANE deployment at the endpoint pair lighting it.

Higher-bandwidth TACLANE variants get pulled into programs that would otherwise settle for less. When the transport was the bottleneck, programs sized down to what they could deploy. With transport accelerated, programs can reach for the bandwidth class the mission actually requires.

In each case, the joint footprint grows. The reference architecture deploys MaiaEdge alongside TACLANE in programs that previously could not field either at the necessary speed.

---

## Performance Characteristics Worth Validating Together

The architecture should be measured against the metrics that matter to the federal customer. Each of these is a question MaiaEdge can answer alone in a lab. Each is more credible answered jointly with TACLANE in path.

Throughput at line rate, end to end. Does the outer transport hold the bandwidth class the program is procuring TACLANE for? Sub-2-microsecond outer-transport latency overhead suggests yes; joint measurement confirms it.

Jitter and latency consistency, end to end. TACLANE customers expect a deterministic envelope from the underlying transport. The reference architecture is designed to preserve that envelope across the diverse underlay. Joint validation puts numbers on it.

Underlay-blend behavior. Does TACLANE see a stable session as the outer transport blends fiber, LEO, and commercial internet? IPsec rekeying continues on its own schedule; TACLANE rekeying is unaffected by the path change. Joint measurement validates the operational story.

Failure recovery. As underlay paths drop and recover, does TACLANE remain operational without re-keying or operator intervention? This is where the Layer 2 transparency property earns its keep.

The output of joint validation is a small set of measurements that program offices can rely on when scoping new TACLANE deployments at modern bandwidths.

---

## CNSA 2.0 Alignment

The Commercial National Security Algorithm Suite 2.0 mandate takes effect January 1, 2027. Both TACLANE and the MaiaEdge outer transport are on certification paths aligned to that mandate. The reference architecture is positioned to enter programs in 2026 and remain conformant as the standard transitions. Joint validation surfaces any cryptographic gaps between the layers early enough to address them ahead of the mandate date, on both sides.

---

## A Joint Validation, Should GDMS Wish to Pursue It

MaiaEdge would welcome a working session with GDMS engineers to validate this reference architecture with a TACLANE pair in path. The shape of that session is, of course, GDMS's call. One workable footprint:

- Two MaiaEdge PBCs at the endpoints
- One TACLANE pair, GDMS-supplied or program-loaned
- Three underlay transports concurrent: fiber, LEO satellite, commercial internet
- Topology: TACLANE → MaiaEdge PBC → blended underlay → MaiaEdge PBC → TACLANE
- Independent measurement at each layer, attributable to each product

A short joint results brief, co-authored and co-branded, would land naturally as a deliverable. Such a brief would position the two products as fielded together rather than as substitutes, and would give program offices an artifact they can act on when scoping new deployments.

Geographic note: GDMS' Taunton engineering presence is roughly an hour from MaiaEdge's Boston headquarters. A working session could be scheduled at either facility, or at a neutral lab, depending on what works best for GDMS.

---

## About MaiaEdge

MaiaEdge is carrier infrastructure for federated private networking. The implementation described in this paper is the company's reference deployment of the architecture on Intel IPU silicon.

The founding team built two prior carrier infrastructure companies: Acme Packet (the Session Border Controller used by 90% of carriers, sold to Oracle) and 128 Technology (a software-defined WAN platform fielded across all branches of the United States Department of Defense, acquired by Juniper). The DOD experience at 128 Technology, particularly the work on five-eyes information exchange, sovereign routing, and outer-and-inner encryption integration, directly informs the architecture in this paper.

100% US-developed software. 100% US-designed hardware integrated in the United States on Intel IPU silicon. 100% US-based engineering team. Headquartered in Boston, Massachusetts.

---

## For Joint Engagement

For follow-up on this reference architecture, contact:

**Timothy Ziemer, CRO, MaiaEdge**

timziemer@maiaedge.io

---

*MaiaEdge · Carrier infrastructure for federated private networking · Private paths. Any network. Instantly.*
