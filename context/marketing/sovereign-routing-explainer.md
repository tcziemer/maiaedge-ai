# Sovereign Routing: What It Is and Why It Matters

## The Problem with How Routing Works Today

Today, when traffic leaves your network, BGP (Border Gateway Protocol) decides where it goes. BGP is the routing protocol that underpins the internet — but it wasn't designed with sovereignty in mind. It optimizes for reachability, not for *your* preferences. Your traffic might traverse networks in jurisdictions you'd rather avoid, pass through infrastructure you don't trust, or take paths you have no visibility into. You don't choose the route. BGP does.

For carriers, enterprises, and governments handling sensitive data, this is a significant — and largely invisible — risk.

---

## What Sovereign Routing Means

Sovereign routing is the ability to define *how* and *where* your traffic travels, not just *that* it gets there. Rather than delegating path decisions to BGP, you set the policy. You choose the route based on what matters to you — jurisdiction, latency, cost, trust, or carrier preference — and the network enforces it deterministically.

Tim Ziemer described it this way in conversation with Telstra InfraCo:

> *"It's like using Waze for traffic — I want to avoid highways, I want to stay on local streets. You can actually create the ability to route according to the things that are important to you. I don't want to route across mainland China. I want to route to the US through this path."*

The analogy is precise: just as Waze lets you set routing preferences rather than defaulting to the fastest route, sovereign routing lets network operators set policy-based preferences rather than defaulting to BGP's least-cost path.

---

## How MaiaEdge Enables It

MaiaEdge replaces BGP path decisions with a Path Computation Engine (PCE) — a cloud-based orchestrator that calculates and enforces deterministic, policy-driven paths across the network. Rather than running routing protocols at every node in the field, the PCE computes paths centrally and programs the Path Border Controllers (PBCs) with the right forwarding instructions.

This approach is modeled on how hyperscalers like Amazon and Microsoft manage their own backbone networks — not with BGP, but with graph-database-driven path computation. MaiaEdge brings the same concept to the wide area network and makes it available to any operator.

The result is multipath routing with genuine policy control:

- Route traffic to avoid specific countries, carriers, or infrastructure
- Prefer private fiber over public internet where latency or security demands it
- Fill remaining capacity over DIA where fiber doesn't reach, without manual reconfiguration
- Enforce routing policy consistently across federated partner networks, not just your own

And critically — this works across operator boundaries. When Telstra InfraCo federates with a partner using MaiaEdge, the sovereign routing policies travel with the path. You don't lose control at the handoff point.

---

## Why This Matters for Telstra InfraCo

Australia's critical infrastructure — defense, government, financial services — operates under increasing pressure to demonstrate data sovereignty. Where traffic flows matters as much as whether it flows. The ability to route deterministically, avoiding specific jurisdictions or network infrastructure, is no longer a nice-to-have for these sectors; it's becoming a procurement requirement.

Telstra InfraCo, with its $1.6B intercity fiber build and existing national footprint, is positioned to offer sovereign routing as a differentiated, high-margin service — particularly for defense, government, and enterprise customers who cannot rely on BGP to make the right decisions for them.

MaiaEdge makes this possible without requiring Telstra to run complex routing stacks at every edge point. The intelligence lives in the PCE. The PBC enforces it. The customer gets deterministic, policy-compliant paths delivered as a service.

---

## The Summary

Sovereign routing means your network does what *you* tell it to do — not what BGP decides. MaiaEdge replaces opaque, uncontrollable routing decisions with policy-driven path computation that respects jurisdictional boundaries, carrier preferences, and security requirements. For operators like Telstra InfraCo serving defense, government, and enterprise customers, this is both a technical capability and a commercial differentiator.

*Stop routing by default. Start routing by design.*
