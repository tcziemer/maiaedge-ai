# AI Networking — Consolidated Research Notes

*Consolidated: May 2026 | Audience: Tim Z / MaiaEdge strategy*

This is a single-file working document covering the full conversation: the high-level landscape, vendor positions, training vs inference, the AI on-ramp competitive set, key terminology, and follow-up threads to drill into.

---

## 1. Executive Summary

The data center network has flipped from north-south (perimeter / client-server) to east-west (GPU-to-GPU) as AI workloads dominate. The fabric is now a peer of the GPU itself — it determines job-completion time on training, and tail latency on inference.

The industry has converged on a three-tier conceptual model: **scale-up** (intra-rack, NVLink class), **scale-out** (cluster fabric, InfiniBand or AI-grade Ethernet), and **scale-across** (cross-DC / WAN, where carriers and on-ramp providers play). Training and inference are bifurcating into different network designs — training is throughput / lossless / all-to-all, inference is latency / many-small-flows / increasingly distributed.

Vendor landscape: Nvidia owns the high end full-stack (NVLink + Quantum InfiniBand + Spectrum-X). Cisco is pushing Silicon One G300 + Nexus HyperFabric. Juniper (HPE) is selling AI-Native Networking + Apstra. Intel is the open-Ethernet flag-bearer via Gaudi 3 and the Ultra Ethernet Consortium. At the on-ramp / scale-across layer, Equinix Fabric and Megaport are the two real players; PacketFabric is materially diminished.

---

## 2. The Core Shift — East-West Becomes the Dominant Pattern

Traditional data centers were designed around north-south traffic. AI workloads have inverted the model. Inside a GPU cluster, every step of training requires GPUs to exchange gradients, activations, and parameters with every other GPU in the job. Industry estimates put east-west above 76% of total data center traffic, and inside an AI pod it is essentially 100%.

Scale numbers to anchor the conversation: a single Nvidia DGX H100 generates up to 3.2 Tbps of network bandwidth (eight 400G NICs). A 1,000-GPU training cluster needs a non-blocking fabric capable of sustaining 400+ Tbps of all-to-all traffic with near-zero packet loss and microsecond-level tail latency.

The three-tier conceptual frame the industry has converged on:

- **Scale-up** — intra-rack accelerator-to-accelerator domain. Nvidia NVLink, AMD Infinity Fabric, custom backplanes. Multi-terabit-per-GPU.
- **Scale-out** — cluster fabric stitching racks into a pod. InfiniBand vs AI-grade Ethernet competing here.
- **Scale-across** — wide-area / cross-DC / metro layer. Carriers, exchanges, on-ramp providers like Megaport and Equinix. Most strategic for distributed inference.

Google's Virgo announcement (2026) made this tiering explicit: separate fabrics for accelerator-to-accelerator, cluster east-west, and north-south services. Topologies are also flattening — Virgo replaces three-tier with two-layer; rail-optimized designs replace classic Clos.

---

## 3. Vendor Positions

### Cisco

Cisco is leaning into Ethernet as the unifying AI fabric. Headline: **Silicon One G300**, a 102.4 Tbps switching ASIC with on-chip 200G SerDes and 1.6T port support, announced Cisco Live EMEA February 2026. Powers Nexus 9000 (DC) and 8000 (service provider/AI). On top: **Nexus HyperFabric AI** — turnkey, full-stack AI cluster solution co-engineered with Nvidia. Job-aware telemetry, Splunk integration. Strategic narrative: enterprise AI doesn't want to assemble its own fabric, and Cisco can sell the whole rack.

### Juniper (now HPE)

Pitch: **AI-Native Networking** — using AI to run the network plus an Ethernet fabric optimized for AI workloads. Stack: QFX (400G/800G leaf) + PTX (spine), managed by **Apstra** (intent-based fabric automation), with **Marvis** as the AIOps/GenAI assistant. Opened the **Ops4AI Lab** in Sunnyvale as a multivendor validation environment. Claims: up to 85% reduction in deployment time, 90% lower ops cost, measurable JCT improvements. Differentiation vs Cisco: openness and multivendor — Switzerland of AI fabrics.

### Nvidia

The only player that owns the full stack — GPU, NIC (BlueField/ConnectX), switch — and sells it as such.

- **NVLink** (NVLink Switch with GB200/B300) — scale-up inside the rack, multi-terabit per-GPU bandwidth Ethernet cannot touch.
- **Quantum InfiniBand** (Quantum-X800, 800G end-to-end) — gold standard for scale-out training fabrics. Ultra-low latency, in-network compute (SHARP).
- **Spectrum-X** — Ethernet platform engineered to behave like InfiniBand. Spectrum-4 switches + BlueField-3 SuperNICs. Proprietary congestion control (NCC) reacts faster than DCQCN. Claim: 1.6× higher effective bandwidth than off-the-shelf Ethernet.
- **Spectrum-XGS** — multi-data-center scale-across.
- **BlueField Astra** — unified network control across AI clusters.

### Intel

Open-Ethernet flag-bearer. **Gaudi 3** AI accelerator: every chip ships with 24 integrated 200G Ethernet ports — the accelerator IS the NIC. Scale-out is native Ethernet, no proprietary fabric required. Leading the **Ultra Ethernet Consortium (UEC)** — industry body building Ethernet enhancements for AI (improved congestion control, telemetry, multi-pathing, link-level reliability). UEC NICs in volume through 2026. Building an **AI NIC chiplet** to license via Intel Foundry. Anti-lock-in narrative: open Ethernet plus Gaudi at meaningfully lower cost than Nvidia.

Note: Tofino was Intel's programmable switch silicon line acquired from Barefoot. Intel exited Tofino in 2023 — no longer part of the AI-fabric story.

---

## 4. Training vs. Inference Architectures Are Diverging

Until recently the industry talked about "AI infrastructure" as one thing. That's collapsing.

**Training** is a throughput-optimized, all-to-all, lossless, bandwidth-hungry workload. Job-completion time is measured in days; tail latency on a single collective stalls thousands of GPUs. Training fabrics are large, dense, non-blocking, rail-optimized (each GPU's NIC goes to a different leaf so failure domains and congestion patterns are decorrelated). They tolerate cost in exchange for performance. InfiniBand and Spectrum-X dominate.

**Inference** is the opposite. Many-small-flows, latency-sensitive, increasingly distributed — closer in shape to traditional web traffic than to training. The bottleneck is increasingly **memory bandwidth** and **network latency** to retrieve KV-cache and route requests across replicas, not raw FLOPs. Google engineers have publicly stated network latency and memory dominate compute at inference scale. As a result, inference is moving outward — to colo edge, to MSP-adjacent locations, to wherever data and users are. Inference networking looks much more like a carrier/metro problem than a single-fabric problem.

This split is the single most important architectural story of 2026 and is where the on-ramp / interconnect layer becomes strategic.

---

## 5. AI On-Ramp Competitive Drill-Down

### What "AI on-ramp" means here

All these players are **Software-Defined Cloud Interconnect (SDCI) / Network-as-a-Service** providers. They sit between an enterprise endpoint and a destination (hyperscaler, neocloud, inference endpoint, SaaS, colo). The pitch: don't backhaul to public internet, don't wait three months for a cross-connect — log into a portal, click, get an L2/L3 virtual circuit in minutes, pay by hour or month. "AI on-ramp" framing is the same NaaS story aimed at one specific destination class — GPU clouds, GPUaaS, AI services.

### Equinix Fabric — the incumbent platform play

The gorilla. ~280 data centers in 70+ metros. Decades of meet-me-room gravity means hyperscalers, carriers, neoclouds, and enterprises are already physically present in their buildings. Equinix Fabric is the software layer that lets any tenant cross-connect to any other tenant programmatically.

2026 moves are aggressive:

- **March 2026:** Distributed AI Hub launched.
- **April 2026:** Fabric Intelligence layered on top — AI-driven control plane that automates how connections get provisioned, sized, rerouted across the distributed footprint.
- Direct connectivity marketed to neoclouds (CoreWeave, Lambda, Nebius, Groq) alongside the traditional hyperscalers.
- Ceiling raised: 400 Gbps physical ports, 100 Gbps virtual circuits standard.
- **Distributed forwarding plane** — no traffic-trombone back to a central router (real architectural advantage over Megaport for east-west AI flows).
- AI infrastructure backbone: 270+ DCs across 77 markets.

Strategic posture: *"We are the place where AI meets the enterprise — bring your data, plug into any GPU cloud, run inference at the edge of our footprint."* Positioning as the neutral aggregation point, not just a pipe.

### Megaport — the carrier-neutral software fabric

Opposite of Equinix. They don't own buildings. Software-defined L2 fabric overlaying **700+ data centers across 80+ data center operators** — Equinix yes, but also Digital Realty, CoreSite, NTT, Iron Mountain, Vantage, regional operators. If you're a customer in a non-Equinix building, Megaport reaches you and Equinix Fabric doesn't.

For AI: launched **Megaport AI Exchange (MAIX)** — existing fabric repackaged with neocloud and GPUaaS providers as featured destinations. Real partnerships exist (SHARON AI APAC, others).

Two architectural caveats for AI:

- **Centralized data plane / cloud router** — traffic between two endpoints can backhaul to a regional aggregation point, adding latency. For inference, this is a real concern.
- Virtual circuit ceilings historically lower than Equinix (10 Gbps was the typical max, though they've been raising — verify current numbers for specific deals).

Strategic posture: *"We give you AI on-ramp anywhere your colo footprint already lives — including the buildings Equinix doesn't own."* Reach over depth.

### PacketFabric — materially diminished, do not over-weight

Originally pitched here as the third pole alongside Equinix and Megaport (with the Massed Compute integrated GPUaaS+NaaS bundle from January 2026). On verification: this picture is misleading.

- **2023:** Merged with Unitas Global, restructured under **Digital Alpha** (PE).
- **2024–2025:** Roughly **10 rounds of layoffs** across 2.5 years. Headcount down 70–80%. Two rounds each cut 50%.
- **Current:** ~74 employees per ZoomInfo. Down from many hundreds at peak.
- **Late 2025 / 2026:** Still publishing — PacketFabric.ai (Dec 2025), Massed Compute bundle (Jan 2026). Operating, but as a much smaller PE-owned entity.

Important: **the Massed Compute partnership is not market validation.** Both companies are Digital Alpha portfolio companies — their PE owner stitching two distressed assets together. Internal housekeeping, not third-party traction.

**Corrected view:** AI on-ramp is realistically a **two-horse race between Equinix Fabric and Megaport**, with regional/specialty players like Console Connect (HGC), Lumen NaaS, and incumbent carrier offerings (AT&T, Verizon, BT, Telstra) worth tracking. PacketFabric is alive on paper but should not be modeled as a credible third pole.

### Side-by-side

| Dimension | Equinix Fabric | Megaport (incl. MAIX) | PacketFabric |
|---|---|---|---|
| Owns physical DCs | Yes (~280) | No (overlay across 80+ operators) | No |
| DC reach | 280 Equinix DCs | 700+ DCs across many operators | NA-centric, narrower |
| Cloud on-ramps | 225+ | 365+ services | Smaller catalog |
| Forwarding plane | Distributed | Centralized cloud router | Distributed |
| Top virtual circuit | 100 Gbps | ~10 Gbps (historically) | 10 Gbps tier |
| Physical port ceiling | 400 Gbps | 100 Gbps | 100 Gbps |
| AI-specific product | Distributed AI Hub + Fabric Intelligence | Megaport AI Exchange | Massed Compute bundle (intra-PE) |
| Neocloud partnerships | CoreWeave, Lambda, Nebius, Groq | SHARON AI, broader catalog | Massed Compute (sister co.) |
| Operational health | Strong | Strong | Diminished, ~74 staff |

### Strategic implications for MaiaEdge

Three honest observations:

1. **Equinix is the only one playing a full platform game.** Distributed AI Hub + Fabric Intelligence is them trying to become the operating system for distributed AI.
2. **None of these are carrier-grade federated private networks.** They're all SDCI / virtualized overlay plays riding on top of underlying transport. For workloads requiring deterministic SLAs, multi-tenant physical isolation, or sovereign / regulated traffic handling, the gap MaiaEdge points at is real.
3. **Neocloud relationships are non-exclusive and shifting fast.** CoreWeave Direct Connect runs over both Equinix Fabric and Megaport. Lambda, Nebius, Groq multi-home. The "AI on-ramp" market is becoming a commodity layer — differentiation moving up-stack (control planes, observability, inference routing, KV-cache locality awareness).

Most useful framing: these are not competitors in the same plane — they're potential partners or layer-above customers of a federated carrier fabric. The opportunity is in being the underlying transport they ride on.

---

## 6. Glossary — Key Terms

**FLOPs** — Floating-point operations per second. Raw arithmetic horsepower. The industry has moved past treating this as the gating constraint.

**Memory bandwidth** — How fast data moves between GPU compute cores and the GPU's own memory (HBM — High Bandwidth Memory stacks on the GPU package). Modern LLMs are large enough that the GPU spends most of its time waiting for weights and activations to arrive — chip is memory-bound, not compute-bound. Why HBM3e/HBM4 matter so much.

**KV-cache** — "Key-Value cache." When an LLM generates token by token, every new token attends to all previous tokens. The intermediate Key and Value tensors from earlier tokens are stored and reused — that's the KV-cache. Per-session, can be tens of GB. When inference traffic gets routed to a different GPU than the one holding the user's KV-cache, the system must rebuild it (slow) or fetch it across the network (where network latency dominates).

**Network latency** — Round-trip packet time. Different from bandwidth. For inference (short request, millions of them), round-trip time matters more than pipe size.

**Replicas** — Multiple copies of the same model running on different GPUs/servers/sites for load balancing and fault tolerance. Production LLM services run hundreds of replicas behind a router. **Session affinity** = sending returning users back to the replica with their warm KV-cache. When affinity breaks, KV-cache state ferries between replicas across the network.

**The combined point** — Old story: more FLOPs = faster AI. New story: chips have more FLOPs than they can feed; bottleneck is (a) HBM-to-cores throughput, and (b) network round-trips to find the right replica and pull session state. Second half makes inference a *networking* problem.

### Gaudi 3 vs. IPU — name-collision unpacked

- **Intel Gaudi 3** = AI accelerator (GPU-class chip from Habana Labs acquisition). Does the AI math. 24 × 200G Ethernet ports on chip.
- **Intel IPU** = Infrastructure Processing Unit = DPU/SmartNIC. Network plumbing — moves packets, offloads infrastructure work from the CPU. Same product category as Nvidia BlueField, AMD Pensando, AWS Nitro. Marquee product: Mount Evans (E2000), co-developed with Google.
- **Graphcore IPU** = Intelligence Processing Unit = third-party AI accelerator (GPU competitor). Different vendor, confusing name. Graphcore acquired by SoftBank 2024, mostly faded from front-line AI conversation.

**Cheat sheet:** Gaudi 3 = does the AI math. Intel IPU = moves the packets. Graphcore IPU = does the AI math (different vendor, confusingly named).

---

## 7. Open Threads to Drill Into Next

1. InfiniBand vs Spectrum-X vs Ultra Ethernet — three-way race and where each wins.
2. Rail-optimized topologies — why they replaced classic three-tier Clos.
3. The inference-distribution problem — KV-cache locality, retrieval, metro fabrics.
4. ~~Megaport vs Equinix Fabric vs PacketFabric for AI on-ramp~~ ✅ done above.
5. Co-packaged optics and the silicon-photonics shift coming with 1.6T.
6. Security implications of east-west AI traffic — "lateral movement at line rate" (Akamai).
7. Hyperscaler in-house fabrics — Google Virgo, AWS scalable reliable diagram (SRD), Microsoft Azure HPC fabrics — and what they signal about merchant-vendor positioning.
8. Carrier NaaS layers — AT&T, Verizon, BT, Telstra, Lumen — and how they overlap or compete with Megaport/Equinix.

---

## 8. Sources

### Landscape & traffic patterns
- [AI Data Center Networking: How GPU Clusters Are Changing Network Design](https://www.thenetworkdna.com/2026/03/ai-data-center-networking-how-gpu.html)
- [East-West Is the New North-South — Akamai](https://www.akamai.com/blog/security/2026/jan/east-west-north-south-rethink-security-ai-driven-data-center)
- [Introducing Virgo Network megascale data center fabric — Google Cloud](https://cloud.google.com/blog/products/networking/introducing-virgo-megascale-data-center-fabric)
- [Nvidia BlueField Astra — SDxCentral](https://www.sdxcentral.com/news/nvidias-bluefield-astra-brings-unified-network-control-to-ai-clusters/)

### Cisco
- [Cisco Silicon One G300 announcement](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m02/cisco-announces-new-silicon-one-g300.html)
- [Cisco Nexus HyperFabric AI Reference Architecture](https://www.cisco.com/c/en/us/products/collateral/data-center-networking/nexus-hyperfabric/hyperfabric-ai-era-ds.html)
- [Cisco Secure AI Factory with NVIDIA](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m03/cisco-secure-ai-factory-with-nvidia-GTC-2026.html)

### Juniper
- [Juniper Ops4AI Lab](https://www.juniper.net/us/en/solutions/data-center/ai-infrastructure/ops4ai-lab.html)
- [Juniper AI-Native Networking — SDxCentral](https://www.sdxcentral.com/news/juniper-networks-pushes-forward-on-ai-native-networking-with-hardware-software-updates/)

### Nvidia
- [NVIDIA Networking Solutions](https://www.nvidia.com/en-us/networking/)
- [NVIDIA Spectrum-X Ethernet Platform](https://www.nvidia.com/en-us/networking/spectrumx/)
- [InfiniBand vs RoCE vs Spectrum-X Decision Guide](https://www.spheron.network/blog/gpu-networking-infiniband-roce-spectrum-x-guide/)

### Intel
- [Intel Gaudi 3 + Ultra Ethernet — Network World](https://www.networkworld.com/article/2086991/intel-flexes-ai-chops-with-gaudi-3-accelerator-new-networking-for-ai-fabrics.html)
- [Intel looks to Ultra Ethernet — Converge Digest](https://convergedigest.com/intel-looks-to-ultra-ethernet-as-its-ai-fabric/)

### Training vs Inference
- [Training vs Inference Infrastructure — Introl](https://introl.com/blog/training-vs-inference-infrastructure-optimizing-ai-workload-patterns)
- [AI Inference crisis: latency and memory trump compute — SDxCentral](https://www.sdxcentral.com/news/ai-inference-crisis-google-engineers-on-why-network-latency-and-memory-trump-compute/)

### On-ramp / Megaport / Equinix / PacketFabric
- [Equinix Distributed AI Hub launch (Mar 2026)](https://newsroom.equinix.com/2026-03-11-Equinix-Unveils-the-Distributed-AI-Hub-to-Simplify-and-Secure-Enterprise-AI-Infrastructure)
- [Equinix Fabric Intelligence launch (Apr 2026)](https://newsroom.equinix.com/2026-04-15-Equinix-Accelerates-Enterprise-AI-Workloads-with-Launch-of-Fabric-Intelligence)
- [Equinix unveils distributed AI infrastructure — Network World](https://www.networkworld.com/article/4063434/equinix-unveils-distributed-ai-infrastructure-targeting-inferencing-cloud-connectivity.html)
- [Megaport AI Exchange product page](https://www.megaport.com/ecosystem/ai-exchange/)
- [Introducing Megaport AI Exchange](https://www.megaport.com/blog/introducing-megaport-ai-exchange/)
- [SHARON AI × Megaport partnership](https://www.businesswire.com/news/home/20250930510258/en/SHARON-AI-Collaborates-With-Megaport-to-Enable-Advanced-Connectivity-to-Cloud-Enterprise-and-Research-Customers-Globally)
- [Equinix Fabric vs Megaport architecture comparison](https://community.equinix.com/discussions/or/how-does-the-fabric-cloud-router-compare-to-the-megaport-cloud-router/1617)
- [PacketFabric × Unitas merger announcement](https://packetfabric.com/press-releases/packetfabric-and-unitas-global-complete-merger)
- [PacketFabric Glassdoor reviews on layoff rounds](https://www.glassdoor.com/Reviews/PacketFabric-rounds-of-layoff-Reviews-EI_IE3047054.0,12_KH13,29.htm)
- [CoreWeave Direct Connect documentation](https://docs.coreweave.com/products/networking/direct-connect/about-direct-connect)
