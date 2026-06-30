# MaiaEdge Port Extender (Integrated Switch) Datasheet

> Source: Integrated Switch.docx + published Port Extender datasheet (maiaedge.io/resources/port-extender-datasheet). The product is marketed as the **MaiaEdge Port Extender**; "integrated switch" is the descriptor.

## Product Overview

The MaiaEdge Port Extender is an integrated 1RU switch designed exclusively for the Path Border Controller (PBC). It scales connectivity without adding complexity, providing an additional 48 ports of expanded port capacity for the PBC and delivering a complete turnkey solution for high-density cross-connect capacity.

High-density 10/25GbE for cross-connects in colocation facilities: the Port Extender provides a 48-port 10GbE/25GbE plus 8-port 100GbE switch in a compact 1RU form factor.

The Port Extender connects to a Path Border Controller via 100GbE uplinks. The PBC treats the Port Extender as extended port capacity, with all paths and policies managed centrally by the Path Computation Engine (PCE). No additional routing configuration or protocol stacks are required on the Port Extender itself.

## Ideal For

- Meet-me rooms and carrier hotels requiring high-density cross-connect capacity
- Colocation facilities offering tenant interconnection services
- Network edges where port count exceeds a single PBC deployment

## Specifications

### Performance & Capacity

| Spec | Value |
|---|---|
| Switching capacity | 2.0 Tbps I/O bandwidth |
| Packet buffer | 32 MB transient capture buffer |
| Latency | Less than 500 ns port-to-port (cut-through mode) |

### Interfaces

| Spec | Value |
|---|---|
| Tenant ports | 48 x SFP28, 10GbE / 25GbE |
| Fabric uplink ports | 8 x QSFP28, 100GbE |
| Management | Rear CPU/BMC shared Ethernet (RJ45), Serial Console (RJ45), USB (Type A) |
| Transceivers | SFP28 up to 2W, QSFP28 up to 5.5W power; DAC (to 5m passive) |

### Switching Features

| Spec | Value |
|---|---|
| Forwarding tables | Unified Forwarding Tables up to 48K; MPLS labels; up to 324K L3 LPM; up to 18K ACLs |
| Content-aware processing | Layer 2-7 packet classification, FCoE |
| Overlay / tunneling | DCB, TRILL, Virtual Port (VM) switching, L2 GRE, NVGRE, VXLAN (encap/decap TEP) |
| Energy efficiency | EEE 802.3az |
| Instrumentation | Transient capture buffer, packet timestamp, buffer statistics |

### Compute & System Management

| Spec | Value |
|---|---|
| Processor | Intel Denverton x86 (up to 8-core) |
| Memory | 8-32 GB ECC DDR4 |
| Storage | Configurable M.2 SSD |
| BMC | Integrated BMC plane, IPMI 2.0 compliant |

### Physical & Environmental

| Spec | Value |
|---|---|
| Form factor | 1U EIA rackmount |
| Dimensions (H x W x D) | 44 mm x 438 mm x 520 mm |
| Max power consumption | Less than 500W maximum (typical less than 350W at 25°C) |
| Power supplies | 1+1 redundant, hot-swappable PSUs (100-240VAC auto-ranging or 180-300VDC auto input) |
| Cooling | 3+1 redundant fans; front-to-back and back-to-front airflow configurations |
| Operating temperature | 0°C to 45°C |
| Operating humidity | 5% to 90% non-condensing |
| MTBF | In excess of 150,000 hours |
