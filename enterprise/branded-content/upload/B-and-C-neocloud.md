# NeoCloud — Industry Taxonomy Alignment + Sub-Segment Deep Dives (Phase 3 working)

**Author:** Phase 3 pre-research (NeoCloud-only scope)
**Date:** 2026-05-14
**Purpose:** Verify, refresh, and extend the gold-standard sub-segment definitions at `context/segments/neocloud.md` lines 185-356. Source material for Phase 3 Step 6 (segment cheatsheet updates) and Step 10 (skill updates).

**Methodology:** Cross-walked SemiAnalysis ClusterMAX 2.1 (April 2026), Tom's Hardware / Northflank / RunPod comparison sets, public 10-K + 8-K filings for crypto-to-AI filers, EuroHPC AI Factory awards, NVIDIA partner press, GAIA-X member directory, and HubSpot live enum state (`working/00-hubspot-enum-verification.md`). All five HubSpot internal values preserved exactly as stored (case-sensitive, including the lowercase "p" in `AI Infrastructure providers - Neocloud` and the trailing "s" in `Crypto to AI - Neoclouds`).

**Cross-walk verdict:** The 5 HubSpot sub-segments map cleanly to the SemiAnalysis ClusterMAX tiering once the sovereignty axis is separated out. No HubSpot sub-segment rename is needed for NeoCloud. The deep-dive content in `context/segments/neocloud.md` is directionally correct but needs anchor refreshes (especially Sovereign AI — Nscale's valuation has jumped to $14.6B and Stargate UAE is now a hard anchor), the GPU-pricing trend reversal (H100 1-year contract pricing reversed direction in Q4 2025 → Q1 2026, now ~$2.35/hr/GPU and rising, not the $2.99/hr "still falling" framing from the April 2026 refresh), and explicit disambiguation for Tier 1 Inference vs AI Infrastructure providers (currently ambiguous in the existing deep dives).

---

## Industry Taxonomy Alignment

### The SemiAnalysis ClusterMAX system — and how MaiaEdge maps to it

The closest thing the industry has to a definitive NeoCloud taxonomy is **SemiAnalysis ClusterMAX 2.0** (launched Nov 2025, refreshed to v2.1 April 2026). It rates 84 GPU clouds across five tiers — Platinum, Gold, Silver, Bronze, UnderPerform — graded on cluster reliability, customer support, technical maturity, and storage/network design. As of ClusterMAX 2.1 (April 2026):

- **Platinum (1):** CoreWeave (only)
- **Gold (6):** Crusoe, Nebius, Oracle OCI, Microsoft Azure, Together AI, Lepton AI (NVIDIA-owned)
- **Silver (10):** AWS, Lambda, Vultr, Voltage Park, Cirrascale, Gcore, Firmus / Sustainable Metal Cloud, GMO, TensorWave, Scaleway
- **Bronze (12+):** Google Cloud, DataCrunch (now rebranded Verda), Hyperstack, Paperspace, Fluidstack, and others
- **UnderPerform:** Unnamed providers cited for SLA gaps, support failures, or undisclosed configs

ClusterMAX is **quality-graded** (does the cluster work well?) but is NOT segment-graded (what kind of NeoCloud is this?). The MaiaEdge 5-sub-segment taxonomy is orthogonal to ClusterMAX and answers a different question: **what does this company DO** (training-primary vs inference-primary vs reseller-plus-GPU vs sovereign-program vs power-rich-pivot), which is what determines the messaging angle, the buying committee, and the connectivity pain shape.

**Mapping:**

| MaiaEdge sub-segment | Typical ClusterMAX tier | What MaiaEdge taxonomy captures that ClusterMAX doesn't |
|---|---|---|
| Large Scale GPU - Neocloud | Platinum + Gold (training-heavy) | Multi-facility footprint count, training-vs-inference primary, hyperscaler-customer concentration |
| Tier 1 Inference - Neocloud | Gold + Silver (inference-focused) | Edge POP distribution, token-latency SLAs, developer/API customer profile |
| AI Infrastructure providers - Neocloud | Silver + Bronze (mid-market repositioning) | Pre-existing non-GPU cloud business + GPU bolt-on, white-label channel motion |
| Sovereign AI Clouds - Neocloud | Spans tiers (Silver-Bronze typical; Nscale is the outlier) | National-program origin, GDPR/DPDP/national-AI-policy gate, in-country PCE requirement |
| Crypto to AI - Neoclouds | Bronze (or unrated — most operate as landlords) | Power-first origin story, landlord vs operator business model, audit-failure risk |

### Where Sovereign AI lives in industry taxonomy

Industry doesn't have a clean "Sovereign AI" sub-segment — it gets bucketed by **national program**: EuroHPC AI Factories (13+ awarded, BSC Barcelona at ~€200M is the largest as of 2026), UK AIRR (Isambard-AI, £500M Sovereign AI Fund), IndiaAI program (~62k GPUs deployed Mar 2026), HUMAIN (KSA), G42's Stargate UAE ($30B / 1GW / 10 sq mi Abu Dhabi campus broke ground March 2026 with OpenAI, Oracle, NVIDIA, Cisco, SoftBank), Bpifrance France 2030. Press treats these as government infrastructure stories, not as a discrete cloud-provider category. MaiaEdge collapses them into one sub-segment because they share a connectivity requirement (jurisdictional path control, audit trails, in-country PCE deployment) that no other NeoCloud sub-segment has.

### Crypto-to-AI is the most ambiguous bucket

The classification test that disambiguates the messy middle:

**LANDLORD test (→ Colocation `AI Signals - colo`, NOT NeoCloud):**
- Primary revenue line on the 10-K is "hosting" / "colocation" / "capacity leasing" — i.e., the customer pays for power + space + cooling, not for GPU-hours
- Named anchor tenants (Microsoft, CoreWeave, Together) that bring their own GPUs
- IREN-Microsoft $9.7B 5-year contract (200MW liquid-cooled GPU infrastructure) is the canonical example — IREN is the landlord; Microsoft brings the GPUs. **IREN is `AI Signals - colo`**, not NeoCloud — even though IREN's own press calls itself "AI infrastructure"
- Core Scientific hosting CoreWeave's clusters → landlord → `AI Signals - colo`
- Galaxy Digital primarily hosts third-party GPU tenants → landlord (where their disclosed model is hosting; if they launch their own GPUaaS brand, reclassify)

**OPERATOR test (→ `Crypto to AI - Neoclouds`):**
- Company sells GPU-hours, inference endpoints, or training cluster access **under its own brand**
- Owns the GPU inventory (or has financed it directly, not via a tenant)
- IREN's "AI Cloud" division targeting $3.4B annualized AI cloud revenue end-2026 across 140k NVIDIA GPUs across 4.5GW pipeline → **dual-classify**: hosting book = AI Signals colo, AI Cloud book = `Crypto to AI - Neoclouds`. HubSpot should hold the **dominant revenue line** as primary classification, with the second flagged in reasoning string. As of May 2026 IREN's hosting book dominates, so primary = `AI Signals - colo`; revisit at end-2026.
- TeraWulf exiting Bitcoin entirely by end-2026 → pure-play crypto-to-AI; if its product page sells GPU-hours under TeraWulf brand → `Crypto to AI - Neoclouds`. If it leases capacity to a NeoCloud → `AI Signals - colo`
- Northern Data Group (now Northern Data AI) — its Taiga Cloud subsidiary IS a NeoCloud operator → `Crypto to AI - Neoclouds`

**Recommendation:** Add a `crypto_pivot_model` HubSpot field (values: `landlord_only`, `operator_only`, `hybrid_landlord_primary`, `hybrid_operator_primary`) so the boundary is encoded explicitly. Until that field exists, classifier reasoning string must state "dominant revenue line = X" verbatim.

### Industry buckets MaiaEdge might be missing

1. **Training-only vs inference-only vs hybrid axis** — industry distinguishes these clearly (CoreWeave is training-primary, Together/Groq/DeepInfra are inference-primary, Lambda is hybrid). MaiaEdge currently bundles training-primary into Large Scale GPU and inference-primary into Tier 1 Inference — works fine, but the messaging angle differs significantly (training = recompute tax + multi-facility distributed training; inference = token-latency SLA + edge POP failover) and the cheatsheet should make that primary-vs-secondary axis explicit.
2. **Serverless/function-based GPU (Modal, RunPod, Replicate, Baseten)** — these are NOT bare-metal GPU rentals; they're API/function platforms with their own scheduling. Currently they fall under `AI Infrastructure providers - Neocloud` but the connectivity pain is different (per-invocation rather than per-cluster). Acceptable for Phase 3 to keep them in AI Infrastructure providers; flag in `company_sub_segment_secondary` reasoning if needed.
3. **NVIDIA-owned/operated NeoClouds (DGX Cloud Lepton)** — Lepton is NVIDIA's own NeoCloud (acquired). For HubSpot classification, treat as Other/Hyperscaler-equivalent EXCLUSION (NVIDIA itself isn't a MaiaEdge customer), but treat its NCP/Exemplar partner list as a high-conviction prospect feed for the other NeoCloud sub-segments.

---

## `Large Scale GPU - Neocloud`

### Definition (sharpened on 4 axes)

| Axis | Value |
|---|---|
| Training vs Inference primary | **Training-primary** (most cluster-hours go to multi-day distributed training runs). Inference is secondary / inherited via the same cluster. |
| Multi-facility distribution count | **5+ regions** at minimum; canonical archetype is 10-50+ regions. CoreWeave at 43 DCs + 850MW (end-2025), targeting 1.7GW end-2026, is the upper anchor. |
| Customer mix | **Hyperscaler-anchored** (Microsoft, Meta, OpenAI, Anthropic = 60-90% of revenue) plus very large enterprise. Developer/long-tail customers exist but are not the revenue driver. |
| Sovereignty posture | **None or thin** — sells globally, runs on commodity carrier transport, no national-program origin. (Sovereign-program-origin companies belong in `Sovereign AI Clouds - Neocloud`.) |

### Quantitative markers

- **GPU count:** 50,000+ deployed GPUs (CoreWeave 250k, Lambda multi-tens-of-thousands, Crusoe / Nebius scaling fast)
- **Facility count:** 5-50 colocation facilities (rented, not owned)
- **Power capacity announced/committed:** 100MW+ minimum to qualify; Tier-1-of-this-sub-segment threshold is 500MW+
- **Revenue band:** $200M-$5B annualized (CoreWeave $2-3B+ run rate, Nebius scaling to 7x by end-2026, Lambda $400-500M+)
- **Customer base:** 3-10 anchor logos typical; hyperscaler concentration disclosed in S-1 / 10-K risk factors
- **Funding stage:** Public (CRWV, NBIS) or late-stage growth equity ($1B+ rounds typical); GPU-backed debt facilities common

### Required signals

- NVIDIA Cloud Partner (NCP) / Exemplar Cloud / DGX Cloud Lepton partner listing
- GPU-backed credit facility (Moody's / DBRS rated; SOFR+spread)
- Public 10-Q with "customer concentration" risk factor language
- 5+ public facility footprint or 100MW+ committed announced
- Hyperscaler anchor tenant press (Microsoft / Meta / OpenAI / Anthropic agreement)
- MLPerf Training submission (any round, last 18mo)

### Disqualifiers (EXCLUDE)

- **Pure GPU reseller with no owned/financed GPU inventory** → Aggregator, not NeoCloud
- **Pure managed services / MSP wrapping a cloud reseller** → MSP segment
- **Single facility, single market, <100MW announced** → too small; Tier 1 Inference or downgrade to Tier 2/3 within sub-segment
- **NVIDIA-owned NeoClouds (Lepton)** → Other (hyperscaler-equivalent), not MaiaEdge ICP

### Anchor companies (15 — geographic spread)

**North America:**
1. CoreWeave (US public — NASDAQ:CRWV) — Platinum ClusterMAX, 43 DCs, 850MW
2. Lambda Labs (US private — $1.5B+ funded) — Silver ClusterMAX
3. Crusoe Energy (US private — flared-gas + stranded-energy thesis) — Gold ClusterMAX
4. Voltage Park (US private) — Silver ClusterMAX
5. Applied Digital (US public — APLD — partial crypto heritage but now operates branded AI Cloud)

**EMEA:**
6. Nebius (NL/EU public — NASDAQ:NBIS, Yandex spin-out) — Gold ClusterMAX, Kansas + London B200/B300
7. Northern Data AI / Taiga Cloud (Germany) — crypto-to-AI heritage but its operator arm fits Large Scale GPU profile
8. Scaleway (France) — Silver ClusterMAX, OVHcloud-sibling positioning
9. Gcore (Luxembourg / global edge) — Silver ClusterMAX

**APAC + LATAM:**
10. Sustainable Metal Cloud / Firmus (Singapore + Norway, dual HQ — Australian roots) — Silver ClusterMAX
11. GMO Internet Group GPU Cloud (Japan) — Silver ClusterMAX
12. Yotta Data Services (India, NVIDIA partner — 20,000 Blackwell Ultra GPUs incoming) — also classifiable Sovereign AI; default Large Scale GPU if customer mix is global, Sovereign AI if customer mix is India-only public-sector
13. E2E Networks (India — public-listed) — same dual-classification rule
14. Nscale (UK/EU — boundary case; ~$1.1B Series B at $14.6B valuation Q4 2025; classifies as Sovereign AI primary, Large Scale GPU secondary)
15. Cerebras Cloud (US public — Cerebras WSE-based fabric — not GPU but functionally identical from a connectivity-pain standpoint; flag for review)

### Confusable-with comparison

| Looks like | Distinguish by |
|---|---|
| `AI Signals - colo` (Colocation) | Large Scale GPU **owns/finances** the GPUs and **rents** the colo space. AI Signals colo **owns** the colo space and **leases** it to GPU tenants. IREN-Microsoft → IREN is colo; Microsoft is the cloud operator. |
| `Tier 1 Inference - Neocloud` | Same physical footprint shape (multi-region) but Tier 1 Inference is **inference-primary** and customer-facing API; Large Scale GPU is **training-primary** and bare-metal-cluster customer-facing. CoreWeave runs both books but is training-dominant. |
| `AI Infrastructure providers - Neocloud` | Large Scale GPU is **GPU-first identity from inception**; AI Infrastructure providers (Vultr, DigitalOcean) are **non-GPU cloud first, GPU bolted on later**. |
| `Crypto to AI - Neoclouds` | Large Scale GPU has **no crypto-mining heritage**. Crypto-to-AI has explicit 10-K language pivoting from BTC. Northern Data AI / Taiga Cloud is the cleanest "graduated" case — its operator arm is Large Scale GPU, its hosting arm is AI Signals colo, its parent is Crypto-to-AI by lineage. Default primary = Crypto to AI for HubSpot. |

### Selling angle

**Lead with deterministic paths + recompute tax.** This sub-segment IS in pain today on inter-AZ latency (128 H100s at 35% utilization across 3 AZs is the canonical board-meeting line). CFO co-signs because every checkpoint rollback during training maps to direct $/GPU/month burn. Reference NCCL synchronous All-Reduce, the straggler problem, and the GPU debt wall ($870B industry-wide) explicitly when CFO is in the room. **Master pitch: connecting distributed AI infrastructure simply.** DETERMINISTIC pillar leads.

### HubSpot fields R1/R2 must populate

- `customer_segment` = `NeoCloud`
- `company_sub_segment` = `Large Scale GPU - Neocloud`
- `segmentation_confidence` per the framework
- `infrastructure_profile` — region count + MW announced + GPU class (H100/H200/B100/B200) + primary hyperscaler anchor named
- `account_tier` — Tier 1 if 5+ regions AND 500MW+ committed AND public/late-stage growth equity; Tier 2 if 2-4 regions AND 100MW+; Tier 3 if 1 region under 100MW
- `network_op_track` = `external_extension` (default — they're the customer, not a federation partner)
- `recent_news_or_trigger_event` — most recent NCP / debt / anchor tenant / region launch event

### Signal source coverage

Per `context/signals/neocloud-signals.md` — Tier A signals N-A0 through N-A11 all apply. Highest-yield for Large Scale GPU: N-A2 (new facility/region), N-A5 (GPU-backed debt), N-A7 (anchor tenant signing), N-A8 (colo lease 8-K), N-A11 (MLPerf submission). StockTitan SEC mirror is the primary tracker for the public filers (CRWV, NBIS, APLD).

### Contact personas

Large Scale GPU has the most mature buying committee of any NeoCloud sub-segment.

| Persona | Title patterns | Why they sign |
|---|---|---|
| **CTO / VP Engineering** (Tier 1 priority) | CTO, VP Engineering, VP Platform Engineering | Owns inference SLA + training throughput. Durable technical signer across all maturity stages. |
| **SVP/VP Infrastructure Engineering** (Tier 1) | SVP Infrastructure, VP Infra Eng, VP Cloud Infrastructure | Where neocloud networking responsibility actually sits — neoclouds rarely silo a "VP Network" title. RFP-facing. |
| **CFO** (co-signer at scale + public stage) | CFO, VP Finance | GPU financing dominates operating economics; signs infrastructure commitments under SEC 8-K Items 1.01 / 2.03. Cares about gross-to-net margin gap. |
| **Head of Platform** (SLA owner) | Head of Platform, VP Product, Director Platform Eng | Agentic-latency pain landlord. |
| **CEO / Founder** (early stage only — under 250 people) | CEO, Co-Founder, President | Pre-scale, owns the buying committee directly. |

**Disqualify outreach to:** Network Admin / IT Admin titles — too junior, no budget. VP Network titles — usually don't exist (neoclouds roll networking under infrastructure engineering).

### Confidence scoring rules

| Confidence | Required evidence |
|---|---|
| `high_90` | Named in ClusterMAX (any tier) + 5+ public facilities + GPU-backed debt or hyperscaler anchor + Large Scale GPU archetype match |
| `medium_7089` | 2 of the 3 above, OR all three but one weak corroboration |
| `low_5069` | 1 of the 3 above OR strong but ambiguous between Large Scale GPU and Tier 1 Inference |
| `manual_review_required` | Conflicting evidence; sovereign-program affiliation but global customer mix; crypto heritage that's still active mining; Cerebras-class wafer-scale (non-GPU) operators |

### Industry sources for ongoing validation

- **SemiAnalysis ClusterMAX 2.x rankings** (refreshed semiannually — track via `clustermax.ai` and `newsletter.semianalysis.com`)
- **NVIDIA Cloud Partner page + DGX Cloud Lepton partner list** (NVIDIA validates the segment)
- **StockTitan / SEC EDGAR** for CRWV, NBIS, APLD, IREN, HUT, CORZ, WULF (8-K Items 1.01 / 2.03 / 5.02; S-1 / 424)
- **Data Center Frontier** + **DCD** trade press
- **HPCwire + The Next Platform + ServeTheHome** for technical scale confirmations
- **MLCommons MLPerf** results (semiannual)
- **PeeringDB** + DE-CIX / AMS-IX / LINX / Equinix IX member lists (N-A9 / N-A10 signals)

---

## `Tier 1 Inference - Neocloud`

### Definition (sharpened on 4 axes)

| Axis | Value |
|---|---|
| Training vs Inference primary | **Inference-primary** — token-latency SLAs are the product. Training capacity may exist but is secondary or a per-customer feature. |
| Multi-facility distribution count | **15-50+ edge POPs / cities** — distributed by design. Many operate out of Equinix carrier hotels with minimal on-site staff. |
| Customer mix | **Developer-heavy + mid-market enterprise via API**. Some hyperscaler customers but not anchor-dependent. Per-token pricing model dominates. |
| Sovereignty posture | **None typically** — global API endpoint design; sovereign-AI inference is a niche extension some support (Together has done EU-only deployments). |

### Quantitative markers

- **Region/POP count:** 15-50+ cities for inference distribution
- **GPU count:** 5,000-50,000+ deployed (smaller than Large Scale GPU)
- **Revenue band:** $50M-$500M annualized
- **Customer base:** Developer/long-tail (10,000-100,000+ accounts on free + paid tiers) plus enterprise API contracts
- **Funding stage:** Series B-D growth equity; DeepInfra's $107M Series B (May 2026 — co-led by 500 Global + Georges Harik, NVIDIA participation) is the canonical 2026 round
- **Performance benchmark:** Sub-100ms TTFT (time-to-first-token) on Llama 70B-class models as published latency SLA

### Required signals

- **Published TPS / latency SLA** on the product / pricing page (e.g., Groq "1000 tok/s", Cerebras "1000+ tok/s on 405B", Together "<100ms TTFT")
- 20+ edge POPs or "global inference" positioning
- Hugging Face Inference Provider listing OR OpenAI-compatible API endpoint marketing
- Inference-specific product launch press (N-C4 signal)
- Per-million-tokens pricing model (vs per-GPU-hour)

### Disqualifiers (EXCLUDE)

- **Pure GPU reseller with no inference product / API** → Large Scale GPU or AI Infrastructure providers
- **Single-region inference only** → too small; Tier 3 within sub-segment or move to AI Infrastructure providers
- **Custom-silicon-only operators that don't own their own deployment** (i.e., they license chips but cloud runs through partners) → Other / equipment vendor

### Anchor companies (15 — geographic spread)

**North America:**
1. Together AI (US — Gold ClusterMAX, ~25 cities, 200MW)
2. Groq (US — Gold-equivalent before NVIDIA $20B acqui-hire Dec 2025; now part of NVIDIA — retains operations as Lepton stack; for HubSpot, classify Groq legacy customer base as Tier 1 Inference)
3. DeepInfra (US — $107M Series B May 2026)
4. Cirrascale (US — Silver ClusterMAX)
5. Cerebras Cloud (US — IPO-pending 2026; wafer-scale, not GPU but functionally inference-primary)
6. SambaNova Suite (US — SN50 chip Feb 2026, 405B world record)
7. Fireworks.ai (US — privately held; Lambda-tier inference)

**EMEA:**
8. Gcore (Luxembourg — Silver ClusterMAX, edge-heavy)
9. Mistral La Plateforme (France — primarily a model lab but operates own inference cloud)

**APAC:**
10. GMO Internet GPU Cloud (Japan — Silver ClusterMAX)
11. Sustainable Metal Cloud / Firmus (SG/Norway — also Large Scale GPU dual)
12. Sakana AI (Japan — model lab + emerging inference cloud; flag for review)

**Hybrid / boundary:**
13. RunPod Serverless (US — also AI Infrastructure providers; primary classification = Tier 1 Inference if serverless inference revenue dominates)
14. Modal Labs (US — serverless inference + GPU function platform; boundary case)
15. Baseten (US — serverless inference + Truss deployment)

### Confusable-with comparison

| Looks like | Distinguish by |
|---|---|
| `Large Scale GPU - Neocloud` | Large Scale GPU sells **bare-metal GPU-hours**; Tier 1 Inference sells **tokens/sec on a managed endpoint**. Both can be distributed. CoreWeave is training-primary; Together is inference-primary. |
| `AI Infrastructure providers - Neocloud` | Tier 1 Inference is **inference-product-FIRST identity**; AI Infrastructure providers are **general cloud with AI bolt-ons**. Vultr offers inference but isn't inference-primary; Together offers everything but inference IS the primary product. |
| **The cleanest test for Tier 1 Inference vs AI Infrastructure providers:** does the company publish a per-million-tokens price or a per-GPU-hour price as the primary pricing model? Per-million-tokens → Tier 1 Inference. Per-GPU-hour → AI Infrastructure provider (mid-market GPU rental) OR Large Scale GPU (top-end). |

### Selling angle

**Lead with token-latency SLA pain + the "no network team" reality.** This sub-segment notoriously has 1-2 IT admins instead of a network architect (Together AI's network person quit — well-documented in Datum channel intel). Customer complaint is "inference latency spiked from 60ms to 150ms and we have no idea if it's our carrier, AWS, or something in between." MaiaEdge value is **real-time telemetry + auto-failover across edge POPs**. Master pitch: deterministic + visible. **Don't lead with CFO ROI** — Tier 1 Inference operators are usually pre-profit / growth-stage and don't have CFO as the buying-committee chair. Founder/CEO is co-signer.

### HubSpot fields R1/R2 must populate

- `company_sub_segment` = `Tier 1 Inference - Neocloud`
- `infrastructure_profile` — POP count + advertised latency SLA + primary model classes served
- `account_tier` — Tier 1 if 20+ POPs AND $100M+ revenue AND named ClusterMAX Gold+; Tier 2 if 10-19 POPs; Tier 3 if <10 POPs
- `account_tier` default upgraded to **Tier 1 by default** per Phase 2 / Phase 3 framework signoff (Tier 1 Inference operators are highest-velocity NeoCloud sub-segment)
- `recent_news_or_trigger_event` — most recent latency-SLA / inference-product launch / funding round

### Signal source coverage

Per `neocloud-signals.md` — Tier A high-yield: N-A4 (enterprise customer win, especially first non-developer logo), N-A6 (network/SRE hiring spike — high signal here because they have nobody), N-A11 (MLPerf Inference submission). Hugging Face Spaces partner announcements are a Tier 1 Inference-specific source (model providers naming their NeoCloud infra partners). DeepInfra-class Series B announcements are N-B2.

### Contact personas

| Persona | Title patterns | Why they sign |
|---|---|---|
| **CEO / Founder** (Tier 1 priority — most Tier 1 Inference operators are founder-led, sub-250 people) | CEO, Co-Founder, President | Centralized authority; no dedicated network role. |
| **CTO** (Tier 1 priority when role exists) | CTO, VP Engineering | Inference SLA owner; same person handles roadmap + infra. |
| **CFO** (only at scale stage — Together, DeepInfra-class) | CFO, VP Finance | Series C+ companies have CFO; pre-C usually don't. |
| **Head of Platform** | Head of Platform, VP Product | When the product is the API, this persona is the SLA buyer. |
| **Network Admin / IT Admin** (the person wearing a networking hat who isn't a network engineer) | Network Admin, IT Admin, DevOps Lead | First to feel observability pain. Useful technical influencer, not signer. |

**Critical persona note:** Tier 1 Inference sub-segment is the **most likely to have NO VP Infrastructure title at all**. Founder + CTO + (rarely) Head of Platform is the entire technical buying committee. Don't over-prioritize searches for VP Infrastructure / Head of Networking — they don't exist at this stage.

### Confidence scoring rules

| Confidence | Required evidence |
|---|---|
| `high_90` | Published per-million-tokens pricing + 15+ POPs + ClusterMAX rated (any tier) + inference-primary self-positioning |
| `medium_7089` | 2 of the above |
| `low_5069` | 1 of the above OR strong inference focus but POP count under 10 |
| `manual_review_required` | Custom-silicon operators (Groq post-NVIDIA, Cerebras Cloud) — review whether to treat as Tier 1 Inference or excluded equipment-adjacent; serverless platforms (Modal, RunPod, Baseten) — review against AI Infrastructure providers boundary |

### Industry sources for ongoing validation

- **SemiAnalysis ClusterMAX** + **InferenceX by SemiAnalysis** (inference-specific benchmarking)
- **Hugging Face Spaces / Inference Providers** partner directory
- **Infrabase.ai inference API comparison** (64-provider table updated regularly)
- **Northflank** + **Fast.io** + **Clarifai** comparison content (track market-positioning shifts)
- **The Next Platform** + **HPCwire** for technical scale confirmations
- **MLCommons MLPerf Inference** results

---

## `AI Infrastructure providers - Neocloud`

(HubSpot internal value uses lowercase "p" in "providers" — preserve exact case)

### Definition (sharpened on 4 axes)

| Axis | Value |
|---|---|
| Training vs Inference primary | **Hybrid + neutral** — sells both, neither is primary. Many add GPU SKUs to a pre-existing general cloud product line. |
| Multi-facility distribution count | **5-30+ global regions** — usually broader than Tier 1 Inference because the parent cloud business already had global presence. |
| Customer mix | **Mid-market + developer + SMB**. Distinguishing feature: existing non-GPU cloud customer base (compute, storage, networking) PRECEDED the GPU offering. |
| Sovereignty posture | **Marketing-thin** — some support data-residency claims as a feature; very few operate as primary sovereign-AI clouds (those go in `Sovereign AI Clouds - Neocloud`). |

### Quantitative markers

- **Region count:** 5-30+ existing cloud regions (broader than Tier 1 Inference)
- **Revenue band:** $100M-$2B annualized — much wider band than other NeoCloud sub-segments
- **Customer base:** 100,000+ accounts typical (developer + SMB long-tail)
- **GPU mix:** H100 / H200 typical; B100/B200 newer; tends to lag Large Scale GPU on bleeding-edge silicon
- **Funding stage:** Mature private + public (Vultr private, DigitalOcean NYSE:DOCN), most have been profitable for years
- **Pricing model:** Per-hour GPU rental (vs Tier 1 Inference per-million-tokens). White-label / multi-tenant orchestration available.

### Required signals

- Existing non-GPU cloud product line (compute, object storage, managed databases) that PRECEDED the GPU offering
- Self-service GPU SKU on the price list (vs reserved-only)
- Channel / reseller / white-label program (Vultr, DigitalOcean, Fluidstack all have this)
- Multi-cloud bridge / Direct Connect / ExpressRoute messaging on the product site

### Disqualifiers (EXCLUDE)

- **GPU-first identity from inception with no prior general cloud business** → Large Scale GPU or Tier 1 Inference
- **Pure managed-services wrapper around AWS/Azure GPUs** → MSP segment
- **Sub-$50M revenue** → too small; AI Infrastructure providers archetype requires established cloud base

### Anchor companies (15 — geographic spread)

**North America:**
1. Vultr (US — Silver ClusterMAX, 32+ locations, virtualized GPU)
2. DigitalOcean (US public — NYSE:DOCN — Paperspace acquisition is the GPU arm)
3. Fluidstack (US — Bronze ClusterMAX; AI Infrastructure-primary white-label)
4. Modal Labs (US — serverless inference + GPU functions; boundary case with Tier 1 Inference)
5. RunPod (US — 200k+ users, 15+ GPU suppliers; serverless secondary brand)
6. Baseten (US — Truss-based serverless inference + Pro/Enterprise tiers)
7. Anyscale (US — Ray-based distributed compute on GPUs)
8. Replicate (US — model-API platform; boundary with Tier 1 Inference)

**EMEA:**
9. Hyperstack (UK — Bronze ClusterMAX)
10. OVHcloud (France — GPU SKUs added to existing cloud; partial Sovereign AI overlap via GAIA-X membership)
11. CIVO (UK — Kubernetes-native cloud with GPU)
12. Atlas Cloud (UK)

**APAC + global edge:**
13. Linode (now Akamai Cloud — Akamai acquired, GPU SKUs added)
14. Paperspace (now DigitalOcean — listed separately if HubSpot record is for legacy Paperspace brand)
15. Hugging Face Inference Endpoints (boundary case — Hugging Face's own inference cloud; classify as Tier 1 Inference if revenue dominantly inference, AI Infrastructure providers if model-hub-revenue dominant)

### Confusable-with comparison

| Looks like | Distinguish by |
|---|---|
| `Tier 1 Inference - Neocloud` | AI Infrastructure providers price **per-GPU-hour**; Tier 1 Inference prices **per-million-tokens**. AI Infrastructure providers had a non-GPU cloud BEFORE GPUs; Tier 1 Inference is inference-from-day-one. |
| `Large Scale GPU - Neocloud` | AI Infrastructure providers are **mid-market and below**; Large Scale GPU is **hyperscaler-anchored** with $200M+ revenue and 50k+ GPUs. Vultr at $200M+ rev with mid-market focus stays AI Infrastructure providers despite scale. |
| MSP segment | AI Infrastructure providers **own and operate** the cloud; MSPs **wrap** someone else's cloud. DigitalOcean owns DCs; an MSP reselling DO's GPU isn't an AI Infrastructure provider. |

### Selling angle

**Lead with multi-cloud bridge + white-label portal + "Mean Time To Innocence" (MTTI).** This sub-segment's pain is specifically the "walled garden" problem: their Direct Connect / virtual circuit equivalents are basic, customers demand AWS/Azure/GCP bridges, and they don't want to send customers to Megaport and lose the relationship. **Master pitch: instant customer on-ramp.** INSTANT pillar leads. Mean Time To Innocence (PCE proves the carrier failed, not them) is a value prop that resonates here more than any other NeoCloud sub-segment.

### HubSpot fields R1/R2 must populate

- `company_sub_segment` = `AI Infrastructure providers - Neocloud` (preserve lowercase "p")
- `infrastructure_profile` — region count + GPU class + presence of multi-cloud bridge product + white-label program y/n
- `account_tier` — Tier 1 if $500M+ revenue AND 20+ regions AND white-label program; Tier 2 if mid-range; Tier 3 if <5 regions or <$50M revenue
- Default Tier 2 (most AI Infrastructure providers are mid-market)

### Signal source coverage

Per `neocloud-signals.md` — high-yield: N-A2 (region expansion — these companies expand fast), N-A4 (enterprise customer win — first big logo is the scaling-wall trigger), N-A6 (network hiring), N-B2 (Series B+ funding), N-C4 (inference-focused product launch — these companies adding inference SKUs is the signal). DigitalOcean / Vultr / Akamai earnings calls disclose GPU as a line item — track quarterly.

### Contact personas

| Persona | Title patterns | Why they sign |
|---|---|---|
| **CEO** (Tier 1 — these companies are CEO-driven, often founder-CEO) | CEO, Co-Founder, President | Owns multi-cloud strategy + competitive positioning |
| **VP Product** (Tier 1 — distinguishing persona for this sub-segment) | VP Product, Head of Product, Chief Product Officer | Multi-cloud bridge + white-label is a PRODUCT decision more than a network decision |
| **VP Infrastructure / Cloud Operations** | VP Infrastructure, VP Cloud Ops, Director Cloud Operations | Operational complexity of multi-region GPU |
| **CTO** | CTO, VP Engineering | Technical validator, less of a primary buyer than at Large Scale GPU |
| **Head of Channel / Partnerships** (where white-label is a strategic priority) | VP Partnerships, Head of Channel, Director BD | White-label portal positioning |

**Distinguishing persona note:** AI Infrastructure providers is the one NeoCloud sub-segment where **VP Product is a primary buyer**. At Large Scale GPU and Tier 1 Inference, VP Product doesn't exist or isn't the buyer. Vultr / DigitalOcean / Fluidstack all have strong product leadership making multi-cloud bridge decisions.

### Confidence scoring rules

| Confidence | Required evidence |
|---|---|
| `high_90` | Pre-existing non-GPU cloud product line + self-service GPU SKU + multi-region (5+) + ClusterMAX listed or industry-recognized brand |
| `medium_7089` | 2 of the above |
| `low_5069` | 1 of the above OR strong GPU presence but unclear whether GPU-primary or cloud-primary identity |
| `manual_review_required` | Serverless platforms (Modal, Baseten, Replicate) — review against Tier 1 Inference boundary; Akamai/Linode-class infrastructure providers where AI is <10% of revenue |

### Industry sources for ongoing validation

- **Vultr / DigitalOcean / Akamai investor materials** + 10-Qs for public filers
- **RunPod / Northflank / Spheron / GMI Cloud comparison content** (these companies publish comparison blogs that map the space)
- **SemiAnalysis ClusterMAX** (Silver + Bronze tier)
- **Crunchbase + PitchBook** for Series B+ rounds in "AI Infrastructure" tag

---

## `Sovereign AI Clouds - Neocloud`

### Definition (sharpened on 4 axes)

| Axis | Value |
|---|---|
| Training vs Inference primary | **Both — gated by jurisdiction**. National program origin means they serve all workloads but only within the country/region. |
| Multi-facility distribution count | **2-10 in-country/in-region facilities typical**. Rarely global — global reach defeats the sovereignty thesis. Exception: Nscale (UK/EU + global edge via Armada partnership). |
| Customer mix | **Government + regulated-industry enterprise (defense, healthcare, financial services, pharma) within national borders**. Foreign customers are rare or explicitly forbidden. |
| Sovereignty posture | **HARD — defining axis**. GDPR (EU), DPDP (India), national AI program (UAE/KSA/Canada/UK), or sub-national equivalent. Compliance is the PRODUCT, not a feature. |

### Quantitative markers

- **Founding origin tied to a named national/regional AI program:** EuroHPC AI Factory award, UK AIRR, IndiaAI, HUMAIN (KSA), Stargate UAE (G42), Bpifrance France 2030, Canadian sovereign AI fund
- **In-country DC footprint:** 100% of compute in declared jurisdiction (national requirement, not preference)
- **Audit / compliance certifications:** SOC 2, ISO 27001, plus jurisdictional (GDPR DPA, India DPDP registration, EU AI Act Chapter VIII)
- **Funding:** Government grant / sovereign wealth co-investment is common (Aker / Norway in Nscale; Mubadala in G42; India MeitY in Yotta/E2E; Bpifrance in French operators)
- **Revenue band:** $50M-$2B+ (Nscale's $14.6B valuation is the high anchor; smaller national operators sub-$100M)

### Required signals

- **Triple-signal qualifier** (recommended — see open question below):
  1. **National AI program origin / government grant or co-investment** (canonical: EuroHPC AI Factory designation, UK AIRR partner, IndiaAI partner, HUMAIN partner, G42/Stargate partner, Bpifrance grant recipient)
  2. **Regulatory compliance gate** (GDPR + EU AI Act for EU; DPDP for India; UAE PDPL; FedRAMP-equivalent for the relevant jurisdiction)
  3. **In-country marketing language** + sovereign-cloud positioning on the company website / pitch deck
- Any single signal alone is `low_5069`. Two signals → `medium_7089`. All three → `high_90`.

### Disqualifiers (EXCLUDE)

- **Tier 1 carriers operating their own sovereign AI factory on their own backbone** (Deutsche Telekom, Orange, BT, KDDI, NTT) → Network Operator segment, not NeoCloud. They already own the path; MaiaEdge fit is thin.
- **Pure GAIA-X members with no actual sovereign-AI product** (many GAIA-X members are tech vendors, integrators, or regulated-industry buyers — not cloud operators)
- **US-headquartered NeoClouds with EU regions** — they're Large Scale GPU or AI Infrastructure providers with data-residency features, not sovereign clouds. The CLOUD Act-vs-GDPR conflict means a US-domiciled provider can't deliver sovereign-AI guarantees regardless of where the GPUs sit.
- **Sovereign AI as marketing buzzword without national-program origin** — common in cloud reseller marketing; reject without triple-signal qualifier.

### Anchor companies (15 — geographic spread, EMEA + APAC + MENA heavy)

**EMEA:**
1. Nscale (UK/EU — Aker-led $1.1B at $14.6B valuation; NVIDIA 300k chip supply + $500M investment; Armada partnership Feb 2026; LARGEST sovereign AI by funding)
2. BSC Barcelona AI Factory (Spain — EuroHPC, €200M, multi-country consortium Spain/Portugal/Türkiye/Romania)
3. Isambard-AI / NCC UK (UK AIRR core compute — Bristol; 21 exaflops Grace Hopper; £500M UK Sovereign AI Fund)
4. Scaleway (France — though dropped GAIA-X 2021, retains sovereign positioning; OVHcloud-sibling)
5. OVHcloud (France public — GAIA-X founding member; sovereign cloud for French government/regulated)
6. Atos / Bull / Eviden (France — sovereign HPC + AI for government/defense; restructuring 2024-2026)
7. Mistral La Plateforme (France — EU-only inference; boundary case with Tier 1 Inference)
8. Firmus Technologies (Norway + Australia — green sovereign cloud)
9. Atlas Cloud (UK — sovereign + general)

**APAC:**
10. Yotta Data Services (India — 20,000 NVIDIA Blackwell Ultra GPUs across Greater Noida + Navi Mumbai by Aug 2026; one of Asia's largest AI superclusters)
11. E2E Networks (India public — NVIDIA partner; MeitY IndiaAI deployment)
12. Tata Communications GPU Cloud (India — boundary case with Tier 1 Carrier Network Op)
13. SoftBank AI Cloud (Japan — METI sovereign AI grants)
14. NIPA Cloud / NSTDA-aligned (Thailand)

**MENA:**
15. G42 / Inception (UAE — Stargate UAE $30B / 1GW / 10 sq mi Abu Dhabi; OpenAI/Oracle/NVIDIA/Cisco/SoftBank consortium; 60% G42 stake; broke ground March 2026)

**Additional named anchors (16-20 — depth bench):**
16. HUMAIN (KSA — sovereign AI cloud)
17. Core42 (UAE — G42 subsidiary, sovereign cloud product)
18. Sakana AI (Japan — model lab + emerging sovereign-positioned inference)
19. Bahnhof / Glesys (Sweden — sovereign hosting + GPU)
20. Sustainable Metal Cloud / Firmus (cross-listed — Singapore HQ now)

### Confusable-with comparison

| Looks like | Distinguish by |
|---|---|
| `Large Scale GPU - Neocloud` | Sovereign AI is **jurisdiction-bound**; Large Scale GPU is **globally available**. CoreWeave-style global API ≠ sovereign. Nscale-style "UK-EU-only data path" = sovereign. |
| `AI Infrastructure providers - Neocloud` | OVHcloud is the boundary case — sells GPU SKUs to a global customer base BUT founded as a French sovereign cloud. Default to **Sovereign AI primary** if the company's PRIMARY brand identity is sovereign (OVHcloud marketing leads with French sovereignty); default to AI Infrastructure providers if sovereign is a secondary/marketing feature. |
| Tier 1 Carrier - Network Op (Network Operator segment) | If a company is a Tier 1 carrier running sovereign AI on its own backbone (Deutsche Telekom AI, Orange Sovereign Cloud, NTT sovereign), classify as **Tier 1 Carrier - Network Op** and put sovereign-AI-cloud activity in the reasoning string. MaiaEdge fit is thin because the carrier already owns the path. |
| `Crypto to AI - Neoclouds` | No overlap typically — crypto-to-AI operators are not national-program funded. Exception: rare US states with sovereign-data-center grants pulled into a crypto-pivot story; would still default to Crypto to AI. |

### Selling angle

**Lead with policy-based sovereign routing + jurisdictional audit trail + in-country PCE deployment.** PRIVATE pillar leads. Sovereignty isn't just where GPUs sit — it's where packets transit. BGP routes to cheapest path, ignoring jurisdictional boundaries. MaiaEdge's value: define "traffic MUST stay within EU" or "India-only paths" → PCE enforces programmatically. PCE runs in-jurisdiction (AWS GovCloud-equivalent or sovereign-cloud-hosted). Every hop logged with timestamp, carrier, geographic location. **Critical caveat:** the sovereign angle does NOT work for US NeoClouds — they get the same MaiaEdge product with the deterministic-paths angle, not sovereignty. Sovereignty is the angle when the prospect's customer base is regulated-industry-in-jurisdiction.

### HubSpot fields R1/R2 must populate

- `company_sub_segment` = `Sovereign AI Clouds - Neocloud`
- `infrastructure_profile` — declared jurisdiction(s), national program affiliation, compliance certifications, customer-base type (government/regulated/private)
- `account_tier` — Tier 1 if national-program-anchor + multi-DC + $100M+ revenue; Tier 2 mid-range; Tier 3 single-DC sovereign with <$50M revenue
- `recent_news_or_trigger_event` — most recent national program grant, regulatory milestone, sovereign-customer logo

### Signal source coverage

Per `neocloud-signals.md` — Tier B: N-B3 (Sovereign AI / Government Contract Win) is the primary signal. International sources: EuroHPC JU AI Factory awards page, GAIA-X Federation releases, IPCEI on Next-Gen Cloud, UK AIRR announcements, Bpifrance France 2030 grants, IndiaAI program releases, METI Japan AI cloud grants, HUMAIN/G42/Mubadala MENA wires.

**EuroHPC AI Factory award = greenfield-equivalent event for EU sovereign clouds.** Detection at award stage gives 6-18 months before GPU cluster comes online — same outreach timing as BEAD for fiber.

### Contact personas

| Persona | Title patterns | Why they sign |
|---|---|---|
| **CEO** (Tier 1 — often a public/political figure, especially at sovereign clouds with national program affiliation) | CEO, Managing Director, Director General | Political accountability + customer relationships with national governments |
| **VP Network / Head of Network** (Tier 1 — distinguishing persona — sovereign clouds OFTEN have this title, unlike other NeoCloud sub-segments) | VP Network, Head of Networking, Chief Network Architect, Network Director | Sovereign clouds carry telecom-DNA staff because the buyers (governments, defense) require network-engineering rigor |
| **Chief Compliance Officer / Head of Regulatory** (Tier 1 — unique to this sub-segment) | CCO, Head of Regulatory Affairs, Head of Compliance | Owns GDPR / DPDP / national-AI-policy gates |
| **CTO** | CTO, Chief Technology Officer | Technical signer |
| **CFO** (at scale + government-contract stage) | CFO | Government contracts have unique payment / award terms |

**Distinguishing persona note:** Sovereign AI Clouds is the ONLY NeoCloud sub-segment where **Chief Compliance Officer / Head of Regulatory** is a primary buyer persona, and the ONLY one where **VP Network** is a reliable title to search for (telecom-DNA staff legacy at national operators + national-program partners).

### Confidence scoring rules

| Confidence | Required evidence |
|---|---|
| `high_90` | Triple-signal qualifier: national program origin + regulatory compliance certification + in-country sovereign positioning marketing |
| `medium_7089` | Two of the three |
| `low_5069` | One signal — typically GAIA-X membership alone OR data-residency marketing alone |
| `manual_review_required` | Sovereign-AI marketing without national-program anchor; OVHcloud-class sovereign-vs-general boundary cases; Tier 1 carrier subsidiaries running sovereign AI products; US/UK dual-domiciled operators (CLOUD Act conflict review) |

**Open question — does GAIA-X membership alone qualify?** **NO.** GAIA-X has 200+ members across 8+ countries; most are vendors, integrators, or end-users — not cloud operators. Membership is a "European data sovereignty advocacy" signal, not a "sovereign AI cloud operator" signal. **The triple-signal qualifier is recommended.** A company with only GAIA-X membership and no other sovereign-program affiliation defaults to its underlying NeoCloud sub-segment (AI Infrastructure providers, Tier 1 Inference, etc.) with `recent_news_or_trigger_event` flagging GAIA-X membership.

### Industry sources for ongoing validation

- **EuroHPC JU AI Factory awards page** + per-factory release pages (Spain BSC, Italy CINECA, Germany Jülich, etc.)
- **GAIA-X Federation member directory** (use as a feeder list, NOT a definitive sovereign signal)
- **UK AIRR + Bristol Isambard-AI press**
- **IndiaAI / MeitY releases**
- **G42 / HUMAIN / Mubadala / Inception press**
- **Bpifrance France 2030 AI compute grants**
- **OpenAI for Countries** launch list (Stargate UAE is first; track follow-on countries)
- **NVIDIA Global Public Sector page**
- **Government procurement feeds:** SAM.gov, OJEU/TED (EU), GeM (India)

---

## `Crypto to AI - Neoclouds`

(HubSpot internal value has trailing "s" on "Neoclouds" — preserve exact case)

### Definition (sharpened on 4 axes)

| Axis | Value |
|---|---|
| Training vs Inference primary | **Hybrid where present, but secondary** — most crypto-to-AI operators are landlords primarily and only secondarily operate their own GPU cloud. Where they DO operate, training-primary is typical (raw GPU rental to AI companies). |
| Multi-facility distribution count | **1-15 sites** typical, geographically clustered near cheap power (Texas, Wyoming, Iceland, Quebec). Sites are LARGE (50-500MW each) but FEW. |
| Customer mix | **Where landlord:** 1-3 anchor tenants (Microsoft / CoreWeave / hyperscaler) leasing power + space + cooling. **Where operator:** mid-market GPU rental (their own brand) or selling to one large customer (IREN-Microsoft model). |
| Sovereignty posture | **None** — US-based primarily; cheap-power geography overrides any sovereignty thesis. |

### Quantitative markers

- **Origin signal:** 10-K / 10-Q with explicit Bitcoin mining heritage AND pivot language ("HPC hosting", "AI infrastructure", "GPU tenant", "AI cloud") on the same filer
- **Power capacity:** 100MW+ per site typical; high-density (100kW+/rack) cooling already deployed
- **Electricity cost:** $0.03/kWh or better (vs $0.08-0.12 industry average) — this is the structural differentiator
- **Revenue band:** $200M-$5B+ annualized; IREN's $3.4B annualized AI cloud revenue target end-2026 across 140k NVIDIA GPUs / 4.5GW pipeline is the top anchor
- **Funding stage:** Public almost exclusively (NASDAQ-listed) — IREN, CORZ, HUT, WULF, MARA, CLSK, BITF, APLD, GLXY all public
- **Customer concentration:** Often 60-90% revenue from a single anchor (IREN-Microsoft $9.7B / 5-year contract is the canonical case)

### Required signals

- Documented Bitcoin mining heritage (SEC 10-K) AND active pivot to AI/HPC
- Power-rich site profile (cheap kWh, high-density cooling)
- **CRITICAL — classify by dominant revenue line:**
  - Dominant revenue = hosting/colocation/capacity leasing → **`AI Signals - colo`** (Colocation segment), NOT NeoCloud
  - Dominant revenue = own-branded GPU-hours / AI Cloud product → **`Crypto to AI - Neoclouds`** (NeoCloud segment)
  - Hybrid: classify by dominant line; flag both in `company_sub_segment_secondary` reasoning

### Disqualifiers (EXCLUDE from NeoCloud, route elsewhere)

- **Pure hosting / colocation / capacity-leasing model with no own-branded GPU cloud** → `AI Signals - colo` (Colocation segment). IREN (as of May 2026), Core Scientific, most of Galaxy Digital's hosting book fall here.
- **Active Bitcoin mining still dominant revenue line** → too early; not yet a NeoCloud. Watch list. Re-evaluate quarterly.
- **Equipment vendors / hardware-only operators with no compute service** → Other.

### Anchor companies (15 — US-heavy with select international, dual-classified)

**Operator-primary (→ `Crypto to AI - Neoclouds`):**
1. **TeraWulf (US public — WULF)** — exiting Bitcoin entirely by end-2026, pure-play AI data center exposure
2. **Northern Data AI / Taiga Cloud (Germany)** — Taiga Cloud is the operator arm; pivoted from BTC mining; canonical international Crypto-to-AI operator
3. **Applied Digital (US public — APLD)** — operator + landlord hybrid; classifier should review quarterly which revenue line dominates; as of mid-2026 operator-branded "AI Cloud" growing
4. **Bitfarms (Canada/US — BITF)** — pivoting; review quarterly
5. **Hut 8 (US/Canada — HUT)** — GPU-as-a-service business launched + Far North Digital JV
6. **Mawson Infrastructure Group (US public)** — AI/HPC pivot mid-stage
7. **Soluna Holdings (US public)** — renewable + AI/HPC, smaller scale
8. **Stronghold Digital Mining (US public)** — pivot announced

**Hybrid / boundary (review quarterly — primary classification may flip):**
9. **IREN / Iris Energy (US public — IREN)** — $9.7B Microsoft contract makes hosting/landlord book dominant as of mid-2026 → primary classification today = `AI Signals - colo`; AI Cloud operator arm secondary. Re-evaluate end-2026 when 3.4B annualized AI cloud target hits.
10. **Core Scientific (US public — CORZ)** — primarily hosts CoreWeave + others → `AI Signals - colo` today; rejected $9B buyout offer to stay independent
11. **Galaxy Digital (US public — GLXY)** — hybrid asset manager / hosting; Helios West campus hosting; classify per dominant disclosed revenue
12. **Marathon Digital (MARA)** — primarily still mining; watch list for pivot
13. **CleanSpark (CLSK)** — primarily still mining; watch list

**Adjacent / boundary with other segments:**
14. **Cathedra Bitcoin** — small; watch list
15. **Argo Blockchain** — restructured; watch list / re-evaluate post-restructuring

### Confusable-with comparison

| Looks like | Distinguish by |
|---|---|
| `AI Signals - colo` (Colocation segment) | **This is THE key boundary**. Crypto-to-AI as a NeoCloud requires the operator to sell GPU-hours under its OWN brand. If it's leasing power + space + cooling to a third party that brings its own GPUs, it's colocation. Pressure-test IREN: $9.7B Microsoft contract = Microsoft brings GPUs = IREN is the landlord = `AI Signals - colo`. Pressure-test Core Scientific: hosts CoreWeave's clusters = landlord = `AI Signals - colo`. |
| `Large Scale GPU - Neocloud` | Both can be large multi-site operators. Distinguishing axis = origin story (BTC mining vs GPU-cloud-from-inception). Northern Data AI / Taiga Cloud is Large Scale GPU by scale but Crypto-to-AI by lineage → classify as Crypto-to-AI per origin (per `context/segments/neocloud.md`). |
| `Sovereign AI Clouds - Neocloud` | No overlap typically — crypto-to-AI is US-cheap-power-geography-driven; sovereign is jurisdiction-driven. |

**Recommended disambiguation policy (for `edge-case-researcher` skill):**

```
1. Does the company have documented Bitcoin mining heritage (10-K filing pre-2024)?
   NO → not Crypto-to-AI; classify by other axes
   YES → continue

2. Is Bitcoin mining still >50% of disclosed revenue?
   YES → too early; flag as Watch List, default `Crypto to AI - Neoclouds` with low_5069 confidence
   NO → continue

3. Is HPC/AI hosting/colocation > AI Cloud operator revenue?
   YES → primary classification = `AI Signals - colo` (Colocation segment), Crypto-to-AI secondary in reasoning
   NO → continue

4. Is AI Cloud operator (own brand selling GPU-hours) > 50% of revenue?
   YES → primary classification = `Crypto to AI - Neoclouds` (NeoCloud segment)
   AMBIGUOUS → `manual_review_required` + dual-classify in reasoning string
```

### Selling angle

**Lead with the Uptime Trap + tenant audit failure risk.** This sub-segment's pain is that their tenants (the GPU cloud operators or hyperscalers) demand 99.99% uptime and multi-path network redundancy, and the legacy mining facility doesn't have it. In crypto, 30 seconds of internet downtime = 30 seconds of lost mining revenue (annoying). In AI, 30 seconds during a 40TB training run = the whole job crashes (a million-dollar mistake). 59% of North American CIOs are cautious about retrofitted crypto facilities. **Master pitch: upgrades your power-rich facility from "mining shed" to "AI-grade data center."** DETERMINISTIC pillar leads but with a simple-fabric framing (they have power engineers, not network architects — don't sell complexity).

### HubSpot fields R1/R2 must populate

- `company_sub_segment` = `Crypto to AI - Neoclouds` (preserve trailing "s")
- `crypto_pivot_model` (NEW field recommended) = `landlord_only` | `operator_only` | `hybrid_landlord_primary` | `hybrid_operator_primary`
- `infrastructure_profile` — origin (BTC heritage), MW capacity, kWh cost, anchor tenant(s), AI Cloud product launched y/n
- `account_tier` — Tier 1 if 100MW+ AND anchor tenant signed AND operator arm launched; Tier 2 if pivoting / mid-stage; Tier 3 if still primarily mining
- `recent_news_or_trigger_event` — most recent 8-K hosting agreement, AI Cloud launch press, GPU procurement order

### Signal source coverage

Per `neocloud-signals.md` — Tier C: **N-C1 Crypto-to-AI Pivot Filing** is the primary signal. Tier A: N-A5 GPU-backed debt raise. WGMI ETF holdings + Hashrate Index monthly tracking. CoinShares reports (tracked $65B in miner AI/HPC contracts by Oct 2025). **Crypto-to-AI outlets promoted to Robust tier 2026-05-11:** CoinDesk + Bitcoin Magazine + Cryptopolitan + news.bitcoin.com surface miner-pivot signals 24-48 hours before mainstream trade press. StockTitan for the 10-K/10-Q pivot language searches.

### Contact personas

This sub-segment has THE most distinctive persona profile of any NeoCloud sub-segment — power-engineer-led, not infrastructure-engineer-led.

| Persona | Title patterns | Why they sign |
|---|---|---|
| **CEO / Founder** (Tier 1 — almost always founder-CEO, often public-company-CEO) | CEO, Co-Founder, Chairman | Owns pivot strategy + investor narrative + tenant-anchor relationships |
| **Chief Power Officer / VP Power Engineering** (Tier 1 — DISTINGUISHING persona — unique to Crypto-to-AI) | VP Power Engineering, Chief Power Officer, Director Energy | Owns the cheap-power strategic asset + cooling deployment |
| **CFO** (Tier 1 — co-signer; public-company governance + tenant-contract sizes) | CFO, VP Finance | $1B+ tenant contracts are 8-K material events |
| **VP Operations / VP Infrastructure** | VP Operations, VP Infrastructure, VP Data Center Operations | Tenant audit response + uptime SLA delivery |
| **CTO** (when present — many Crypto-to-AI operators don't have one) | CTO, Head of Technology | Technical validator; less of a buyer than at other NeoCloud sub-segments |
| **Network Architect** (almost never present — flag the GAP as the angle) | Network Architect, Head of Networking | Often NOT on staff; flag absence as the pitch — "you don't have to hire 5 CCIEs to pass tenant audits" |

**Distinguishing persona note:** Crypto-to-AI is the ONLY NeoCloud sub-segment where **Chief Power Officer / VP Power Engineering** is a primary technical buyer. Their domain is the cheap-kWh and high-density cooling. They sign network purchases that simplify the tenant audit response. **Founder + CFO + VP Power Engineering** is the typical 3-person buying committee.

### Confidence scoring rules

| Confidence | Required evidence |
|---|---|
| `high_90` | Documented BTC mining heritage (10-K) + AI Cloud operator brand launched + own-branded GPU-hours selling AND operator revenue > hosting revenue |
| `medium_7089` | Documented BTC heritage + AI Cloud launched (revenue split unclear) |
| `low_5069` | Documented BTC heritage + pivot language only (no operator brand launched yet) — Watch List status |
| `manual_review_required` | Hybrid landlord-operator with ambiguous revenue split (IREN, APLD, Core Scientific style) — quarterly review required; classifier defaults to dominant line per most recent 10-Q |

### Industry sources for ongoing validation

- **StockTitan + SEC EDGAR** for IREN, CORZ, HUT, WULF, BITF, MARA, CLSK, APLD, GLXY (8-K Item 1.01 hosting agreements + 5.02 + S-1 / 424 / Reg D)
- **CoinShares** + **Hashrate Index** + **WGMI ETF holdings** (monthly tracker)
- **CoinDesk + Bitcoin Magazine + Cryptopolitan + news.bitcoin.com** (Robust tier 2026-05-11)
- **Bernstein / Compass Point** equity research notes on the public filers
- **Per-company IR newsrooms** (IREN, Core Scientific, TeraWulf, Hut 8, etc.)
- **CoinShares Mining Report** (semi-annual)

---

## Cross-cutting clarifications addressed

### 1. Tier 1 Inference vs AI Infrastructure providers — cleanest test

**The pricing-model test wins.** Per-million-tokens pricing on the product page → Tier 1 Inference. Per-GPU-hour pricing → AI Infrastructure providers (or Large Scale GPU if hyperscaler-anchored). Both can be multi-region. Both can serve developers. The pricing model is what the product page declares the customer is buying. Encoded in `edge-case-researcher` flowchart below.

### 2. Sovereign AI qualification — does GAIA-X membership alone qualify?

**No.** Triple-signal qualifier required (national program origin + regulatory compliance gate + in-country sovereign positioning marketing). GAIA-X-only = secondary feature, default to underlying sub-segment.

### 3. Crypto-to-AI classification policy — pressure-tested against IREN, Core Scientific, Galaxy

- **IREN** (current state, May 2026): Microsoft $9.7B contract = Microsoft brings GPUs = IREN is landlord → primary `AI Signals - colo`. Re-evaluate end-2026 when IREN's own "AI Cloud" brand may dominate revenue.
- **Core Scientific:** hosts CoreWeave's clusters = landlord → `AI Signals - colo`. Rejected $9B buyout offer March 2026 to stay independent.
- **Galaxy Digital:** Helios + other hosting campuses host third-party tenants → primary `AI Signals - colo` per current disclosed revenue. Classify operator arm separately if their own GPU cloud brand becomes material.

**Disambiguation flowchart for `edge-case-researcher`:**

```
NEOCLOUD sub-segment disambiguation flowchart

1. Documented Bitcoin mining heritage (10-K pre-2024)?
   YES → continue to crypto-pivot branch
   NO → continue to non-crypto branch

CRYPTO-PIVOT BRANCH:
2a. Is BTC mining still >50% of revenue?
    YES → Watch List, low_5069 confidence on Crypto to AI - Neoclouds
    NO → continue
3a. Is HPC/AI hosting > AI Cloud operator revenue?
    YES → primary = AI Signals - colo (Colocation segment), Crypto-to-AI secondary
    NO → continue
4a. Is own-branded GPU-cloud operator revenue > 50%?
    YES → Crypto to AI - Neoclouds, high_90 / medium_7089 per evidence
    AMBIGUOUS → manual_review_required, dual-classify in reasoning

NON-CRYPTO BRANCH:
2b. Founded under a national AI program / sovereign grant / EuroHPC AI Factory / IndiaAI / HUMAIN / Stargate / Bpifrance?
    YES → continue to sovereign branch
    NO → continue to commercial branch

SOVEREIGN BRANCH:
3c. Triple-signal qualifier (national program + regulatory compliance + in-country marketing)?
    ALL 3 → Sovereign AI Clouds - Neocloud, high_90
    2 of 3 → Sovereign AI Clouds - Neocloud, medium_7089
    1 of 3 → low_5069; consider underlying-sub-segment default
4c. Is the parent a Tier 1 Carrier (DT, Orange, BT, KDDI, NTT) with sovereign AI as a product line?
    YES → reclassify as Tier 1 Carrier - Network Op (Network Operator segment), sovereign AI in reasoning string
    NO → keep Sovereign AI Clouds - Neocloud

COMMERCIAL BRANCH:
3d. Pricing model on product page = per-million-tokens?
    YES → Tier 1 Inference - Neocloud
    NO → continue
4d. Did the company have a non-GPU general cloud product line BEFORE adding GPU?
    YES → AI Infrastructure providers - Neocloud
    NO → continue
5d. Hyperscaler customer concentration 60%+ AND multi-facility 5+ AND GPU-first identity from inception?
    YES → Large Scale GPU - Neocloud
    NO → manual_review_required (likely sub-scale; consider Tier 3 or Watch List)
```

---

## Summary

This document refreshes the gold-standard NeoCloud sub-segment definitions for Phase 3 Step 6 (segment cheatsheet update) and Step 10 (skill updates). Key behaviors that should propagate to `skills/segment-classification`, `skills/company-enrichment`, and `skills/edge-case-researcher`:

1. **Anchor-company refresh** — 10-15 anchors per sub-segment with geographic spread (EMEA + APAC + MENA emphasis for Sovereign AI and Crypto-to-AI), all validated against May 2026 industry sources.
2. **The pricing-model test** distinguishes Tier 1 Inference (per-million-tokens) from AI Infrastructure providers (per-GPU-hour) cleanly.
3. **Triple-signal qualifier** for Sovereign AI Clouds — GAIA-X membership alone is NOT enough.
4. **Crypto-to-AI dominant-revenue-line test** disambiguates landlord (→ AI Signals colo) from operator (→ Crypto to AI Neoclouds). IREN is currently a landlord; Core Scientific is currently a landlord; Galaxy is currently a landlord. Re-evaluate quarterly.
5. **Persona deltas** by sub-segment captured for the contact-discovery skill — Large Scale GPU = CTO + VP Infra Eng + CFO; Tier 1 Inference = Founder/CEO + CTO (no VP Infra); AI Infrastructure providers = CEO + VP Product (distinguishing); Sovereign AI = CEO + VP Network + CCO (distinguishing); Crypto-to-AI = Founder + CFO + VP Power Engineering (distinguishing).
6. **Confidence rules** encoded per sub-segment with the universal "sub-segment confidence cannot exceed segment confidence" rule applied.
7. **Industry sources** named per sub-segment for ongoing classifier validation (SemiAnalysis ClusterMAX is the canonical NeoCloud rating; refresh quarterly).

---

*Cross-references: `context/segments/neocloud.md` lines 185-356 (existing deep dives — refresh with this content), `context/signals/neocloud-signals.md` (signal catalog), `working/00-hubspot-enum-verification.md` (live HubSpot enum state), `Phase 3/05 - Sub-segment definitions for cheatsheets.md` (gold-standard template + confidence framework from MSP/Fiber/Network Op work).*

*Industry sources consulted 2026-05-14: SemiAnalysis ClusterMAX 2.0 + 2.1 (Nov 2025 + April 2026), Tom's Hardware / Northflank / RunPod / Spheron / Hyperstack comparison content, public 10-K + 8-K filings (CRWV, NBIS, APLD, IREN, CORZ, HUT, WULF, BITF, MARA), EuroHPC JU AI Factory awards (BSC + 6 others), Nscale press (Aker / NVIDIA / Armada), Stargate UAE press (G42 / OpenAI / Oracle / NVIDIA / Cisco / SoftBank), Yotta + E2E Networks NVIDIA Blackwell partner press, GAIA-X Federation member directory, DeepInfra Series B announcement (May 2026), Compute Forecast + Last Week in AI newsletters, Bernstein / Tikr / FinancialContent equity research on IREN and crypto-to-AI pivots.*
