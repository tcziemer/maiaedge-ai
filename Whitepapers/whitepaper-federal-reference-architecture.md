# Federal Transport Reference Architecture

**A reference architecture for high-assurance federal transport on the Intel IPU.**
*Multi-path. Deterministic. PQC-ready. Transparent to inline Type-1 encryption.*

---

## Executive Summary

Federal transport designs today balance high throughput, classified-grade encryption, and resilient diversity. Each property is solvable in isolation. The cost curve breaks when a program tries to scale all of them at once: every additional diverse path means another pair of inline Type-1 encryptors at hundreds of thousands of dollars apiece, another L3 integration, another lead time. Software SD-WAN does not address this bottleneck and cannot deliver the deterministic envelope that radar, integrated air defense, and distributed inference workloads require.

This paper describes a reference architecture for an outer transport layer that sits cleanly beneath the program's existing inline encryption stack. It runs on an Intel Infrastructure Processing Unit (IPU) class of silicon. It is Layer 2 transparent, so the inline Type-1 encryptors and the L3 routing design above it remain in their certified positions. It carries traffic across fiber, LEO satellite, and commercial internet as a blended underlay, turning multi-path diversity into a software-defined property rather than a per-path procurement. It is software-upgradeable to CNSA 2.0, aligned to the January 1, 2027 post-quantum cryptography mandate.

The architecture is implemented today by MaiaEdge on Intel IPU silicon. Validation work pairing the implementation with fielded inline encryption equipment is in progress.

---

## The Federal Transport Problem

Several constraints shape any serious federal transport architecture. The reference architecture in this paper is designed against the ones that show up most often when programs evaluate modern transport options at the bandwidth and assurance levels current missions require.

### Fiber lead times block program timelines

Dedicated fiber installation in federal venues regularly runs 90 to 180 days from order to lit service. Program timelines do not accommodate that lead time. Programs need a path that can stand up on commercial internet or LEO satellite immediately, then transition to fiber when fiber arrives, without re-architecting the network or re-keying inline encryptors.

### Bandwidth-class Type-1 paths are expensive to provision in parallel

Federal high-assurance networks are already built for resilience. Programs run diverse routing, redundant paths, and well-understood failover handled at the L3 design layer. The constraint is not the absence of resilience. It is the cost and lead time of provisioning resilient capacity at the bandwidth modern missions require.

A redundant Type-1 encrypted path at 100 Gbps means a pair of inline encryptors per path, at hundreds of thousands of dollars per encryptor, manufactured in low volumes and managed under special handling and certification overhead. Each new physical path, whether fiber, LEO satellite, or commercial internet, carries its own encryptor inventory and its own integration into the L3 routing posture before it can carry production traffic. The result is that programs typically buy and deploy one or two diverse paths over months, not five or six paths over weeks.

The reference architecture changes this cost curve. A single MaiaEdge transport, sitting beneath the program's existing inline Type-1 encryption, can carry traffic across multiple underlay paths without requiring an additional Type-1 encryptor pair per path. Path diversity becomes a software-defined property of the outer transport rather than a per-path procurement.

### Software SD-WAN cannot meet the determinism envelope

Software-based packet processing introduces variability. Throughput, jitter, and latency drift under load and across paths. For radar-adjacent workloads, integrated air defense networks, distributed inference, and any system relying on Precision Time Protocol (PTP), microsecond-class consistency is the requirement. A software data plane cannot deliver it.

---

## Why the IPU Class of Silicon Matters

The Intel Infrastructure Processing Unit is a hardware-accelerated networking engine that executes the data plane in silicon, separate from the host CPU. For the federal transport problem, the silicon class brings properties a software-only data plane cannot match.

### Hardware-accelerated, line-rate packet processing

The IPU forwards, encapsulates, and encrypts packets at line rate without consuming host CPU cycles. Encryption is not a bottleneck. Throughput envelopes scale to 100 Gbps and beyond without the multi-core scaling penalties that limit x86 software SD-WAN platforms.

### Deterministic data plane behavior

Because the data plane runs in dedicated silicon, packet processing latency and jitter are tightly bounded. There is no operating system scheduler in the path. There is no contention with workload software for compute resources. The result is the kind of consistent throughput, jitter, and latency envelope that PTP-dependent and time-sensitive workloads require.

### Isolation between data plane and control plane

The control plane runs separately from the IPU data plane. This is an architectural property federal programs care about: the data plane has no dependency on a shared general-purpose operating system, no exposure to the broad attack surface of host software, and continues forwarding at line rate even if the control plane is unreachable.

The IPU class of silicon is the foundation that makes the rest of this architecture possible. Equivalent properties cannot be achieved on a software-only data plane running on commercial server CPUs.

---

## The Reference Architecture

The architecture is composed of an outer transport function running on Intel IPU silicon at each network boundary, a control plane running in customer-managed cloud, and a Layer 2 transparency property that lets the inline encryption stack and L3 routing design above behave as if they were on a single end-to-end Ethernet path. The inner encryptors fielded by the program remain in their certified position; the outer transport carries them across diverse underlay paths without their participation.

![Federal Reference Architecture](assets/diagrams/federal-architecture-diagram.svg)

### Outer transport function on the IPU

A 1RU appliance at each network boundary. Dual 100 Gbps interfaces. Stateless forwarding. Line-rate AES-256-GCM encryption. Sub-2-microsecond latency overhead. The appliance executes path instructions; it does not compute them.

### Control plane in customer-managed cloud

A path computation engine that maintains a global view of the topology, computes optimal end-to-end paths against policy and SLA constraints, programs the appliances over a secure channel, and collects hop-by-hop telemetry continuously. The control plane runs in customer-managed cloud infrastructure. No data-plane traffic transits the control plane.

### Layer 2 transparency

The outer transport carries Layer 2 frames end to end. Anything above it, IPsec tunnels, MPLS, BGP-routed networks, and inline Type-1 encryption sessions, sees an end-to-end Ethernet path. This is the architectural property that enables the rest of the paper: encryptor transparency, a blended diverse underlay, and clean integration with existing federal network designs.

---

## Architectural Property: Transparent to Inline Type-1 Encryption

The federal high-assurance encryption stack is not going away, and the reference architecture is not designed to replace it. It is designed to sit cleanly underneath it.

### The outer / inner pattern

| Layer | Function | Provided by |
|---|---|---|
| Inner encryption | Type-1 / classified, link-level | HAIPE inline encryptors fielded today (TACLANE family from General Dynamics Mission Systems, layer-2 high-speed encryptors from Viasat, and equivalents) |
| Outer transport | Hardware-accelerated, multi-path, PQC-ready | This reference architecture, implemented on Intel IPU silicon |

The outer transport encapsulates and encrypts at line rate with AES-256-GCM. The inner encryptor handles Type-1 confidentiality at link level. Each layer does what it is certified to do, with no overlap and no interference.

### Why this matters operationally

Programs that have already certified an inline Type-1 encryptor do not have to re-certify the transport layer. Programs evaluating a new mission do not have to choose between high-assurance encryption and modern transport capabilities. The reference architecture is encryptor-agnostic at this layer: any standards-conformant Layer 2 inline encryptor in the path is supported.

---

## Architectural Property: Diversity Below the L3 Design

Federal programs already build for path diversity. The reference architecture changes where that diversity lives in the stack: instead of being an L3 routing exercise that requires per-path encryption, integration, and certification, it becomes a property of the outer transport, blending mixed underlay paths beneath an unchanged inner encryption stack.

### A blended underlay

Fiber, LEO satellite (Starlink and equivalents), and commercial internet all coexist as candidate paths beneath the outer transport. The control plane treats them as a single blended underlay, selecting against policy, latency, jitter, and SLA constraints continuously. A program can stand up on commercial internet on day one, add LEO when sovereignty or geographic posture demands it, and transition to fiber when fiber arrives, without re-architecture.

### Why this matters above the underlay

Because the outer transport carries Layer 2 frames, IPsec tunnels, BGP-routed connections, and the inline Type-1 encryptors above it see a stable end-to-end path while the underlay blends. IPsec rekeying continues normally on its own schedule. The L3 routing design is unchanged. The program does not have to re-engineer its high-assurance encryption stack to gain underlay diversity.

This is the operational difference between the reference architecture and conventional SD-WAN diversity. SD-WAN handles path selection at Layer 3, where it interacts with the rest of the routing design. The reference architecture handles it at Layer 2, where it interacts with nothing the program has already certified.

---

## Architectural Property: PQC and CNSA 2.0 Readiness

The Commercial National Security Algorithm Suite 2.0 mandate takes effect January 1, 2027. Equipment in National Security Systems networks must be CNSA 2.0 conformant or demonstrate a software-upgradeable path to conformance.

The reference architecture is software-upgradeable to CNSA 2.0 algorithms. Cryptographic primitives in the data plane (currently AES-256-GCM and elliptic-curve key exchange) are designed to be replaced with CNSA 2.0 approved algorithms (ML-KEM, ML-DSA, SLH-DSA, and CNSA 2.0 symmetric profiles) through software update without hardware change.

This addresses the Harvest-Now-Decrypt-Later threat model that drives the mandate: traffic intercepted today must be safe against tomorrow's quantum decryption capability. Programs deploying the reference architecture today inherit a path to CNSA 2.0 conformance ahead of the mandate date.

---

## Architectural Property: Deterministic Throughput and Jitter

Some federal workloads are deeply time-sensitive. Integrated air defense networks. Radar data fusion. Distributed inference at the tactical edge. Any system that depends on Precision Time Protocol synchronization. These workloads do not tolerate jitter.

Because the data plane runs in IPU silicon, packet processing produces a tight, predictable envelope. There is no operating system scheduler, no software interrupt latency, no garbage collection pause. Throughput holds at line rate. Jitter is bounded in microseconds, not milliseconds. Latency is consistent across the diverse paths.

The architectural claim is narrow and important: **the determinism envelope of this transport class is suitable for next-generation missile defense, integrated air defense, distributed inference, and other workloads where PTP synchronization and microsecond-class consistency are operational requirements.**

Software-only data planes cannot make this claim. The class of silicon matters.

---

## Deployment Posture

The reference architecture is designed to meet federal programs where they are, rather than impose a single deployment or commercial model.

### Available today

- The control plane runs on AWS today. The same control plane image deploys into AWS GovCloud.
- The data plane appliance is operational and shipping.
- 100% US-developed software, 100% US-designed hardware integrated in the United States on Intel IPU silicon, 100% US-based engineering team.
- Customer-controlled deployment posture: the implementer does not require visibility into customer data planes, traffic, or operational telemetry.

### Adaptable per program requirements

- FIPS 140-3 validation through third-party accreditation is achievable. The implementer undertakes this work as a program requires it.
- IL5 deployment is open and would be pursued alongside program-specific accreditation.
- The control plane can be adapted to customer-managed environments outside AWS through targeted engineering scoped to the program.

This posture is intentional. The architecture is built to fit the program's accreditation, deployment, and commercial vehicle, rather than dictate them.

---

## About MaiaEdge

MaiaEdge is carrier infrastructure for federated private networking. The implementation described in this paper is the company's reference deployment of the architecture on Intel IPU silicon.

The founding team built two prior carrier infrastructure companies: Acme Packet (the Session Border Controller used by 90% of carriers, sold to Oracle) and 128 Technology (a software-defined WAN platform fielded across all branches of the United States Department of Defense, acquired by Juniper). The DOD experience at 128 Technology, particularly the work on five-eyes information exchange, sovereign routing, and outer / inner encryption integration, directly informs the architecture in this paper.

100% US-developed software. 100% US-designed hardware integrated in the United States on Intel IPU silicon. 100% US-based engineering team. Headquartered in Boston, Massachusetts.

---

## Validation in Progress

MaiaEdge is currently validating this reference architecture across topologies that pair the IPU-based transport with fielded inline Type-1 encryption equipment.

Measurement focus:

- Throughput envelope at 100 Gbps with inline Type-1 encryption in path.
- Path-blending behavior across fiber, LEO, and commercial internet, with the inner encryption stack and L3 routing posture left unchanged.
- Jitter and latency consistency under path loss and recovery.
- CNSA 2.0 cryptographic primitives in the data plane.

Validation reports will be published as the work completes.

---

## For Technical Conversations

For follow-up on this reference architecture, contact:

**Timothy Ziemer, CRO, MaiaEdge**

timziemer@maiaedge.io

---

*MaiaEdge · Carrier infrastructure for federated private networking · Private paths. Any network. Instantly.*
