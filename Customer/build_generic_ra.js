// Build a generic Reference Architecture docx based on the Centra v5 doc
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, PageOrientation, LevelFormat,
  HeadingLevel, BorderStyle, WidthType, ShadingType, PageNumber, PageBreak,
  TabStopType, TabStopPosition, ImageRun,
} = require('docx');

const DIAGRAM_PATH = "/sessions/nifty-determined-turing/diagram.png";
const diagramBuffer = fs.readFileSync(DIAGRAM_PATH);
const LOGO_PATH = "/sessions/nifty-determined-turing/logo.png";
const logoBuffer = fs.readFileSync(LOGO_PATH);
// Logo native: 1962 x 508 → aspect ~3.86:1

// ---------- Style helpers ----------
const border = { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" };
const cellBorders = { top: border, bottom: border, left: border, right: border };
const headerShade = { fill: "1F2937", type: ShadingType.CLEAR, color: "auto" };
const altShade   = { fill: "F7F7F7", type: ShadingType.CLEAR, color: "auto" };
const calloutShade = { fill: "FFF4D6", type: ShadingType.CLEAR, color: "auto" };
const cellMargins = { top: 100, bottom: 100, left: 140, right: 140 };

// US Letter content width: 12240 - 1440*2 = 9360 DXA
const CONTENT_W = 9360;

function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120, line: 300 },
    ...opts,
    children: Array.isArray(text)
      ? text
      : [new TextRun({ text, ...(opts.run || {}) })],
  });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 320, after: 160 },
    children: [new TextRun({ text, bold: true, size: 36, color: "1F2937" })],
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 240, after: 120 },
    children: [new TextRun({ text, bold: true, size: 28, color: "1F2937" })],
  });
}

function h3(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_3,
    spacing: { before: 200, after: 100 },
    children: [new TextRun({ text, bold: true, size: 24, color: "1F2937" })],
  });
}

function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80, line: 280 },
    children: [new TextRun(text)],
  });
}

function bulletRuns(runs) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 80, line: 280 },
    children: runs,
  });
}

function tCell(text, opts = {}) {
  const isHeader = !!opts.header;
  const runProps = isHeader
    ? { bold: true, color: "FFFFFF", size: 22 }
    : { size: 22 };
  const colWidth = opts.width;
  return new TableCell({
    borders: cellBorders,
    width: { size: colWidth, type: WidthType.DXA },
    margins: cellMargins,
    shading: isHeader ? headerShade : (opts.shade || undefined),
    children: (Array.isArray(text) ? text : [text]).map(t =>
      typeof t === "string"
        ? new Paragraph({ children: [new TextRun({ text: t, ...runProps })] })
        : t
    ),
  });
}

// Generic 2-column table builder with header
function table2(headerRow, dataRows, colWidths) {
  const [w1, w2] = colWidths;
  const rows = [
    new TableRow({
      children: [
        tCell(headerRow[0], { header: true, width: w1 }),
        tCell(headerRow[1], { header: true, width: w2 }),
      ],
      tableHeader: true,
    }),
    ...dataRows.map((r, i) =>
      new TableRow({
        children: [
          tCell(r[0], { width: w1, shade: i % 2 === 1 ? altShade : undefined }),
          tCell(r[1], { width: w2, shade: i % 2 === 1 ? altShade : undefined }),
        ],
      })
    ),
  ];
  return new Table({
    width: { size: w1 + w2, type: WidthType.DXA },
    columnWidths: [w1, w2],
    rows,
  });
}

function table3(headerRow, dataRows, colWidths) {
  const [w1, w2, w3] = colWidths;
  const rows = [
    new TableRow({
      children: [
        tCell(headerRow[0], { header: true, width: w1 }),
        tCell(headerRow[1], { header: true, width: w2 }),
        tCell(headerRow[2], { header: true, width: w3 }),
      ],
      tableHeader: true,
    }),
    ...dataRows.map((r, i) =>
      new TableRow({
        children: [
          tCell(r[0], { width: w1, shade: i % 2 === 1 ? altShade : undefined }),
          tCell(r[1], { width: w2, shade: i % 2 === 1 ? altShade : undefined }),
          tCell(r[2], { width: w3, shade: i % 2 === 1 ? altShade : undefined }),
        ],
      })
    ),
  ];
  return new Table({
    width: { size: w1 + w2 + w3, type: WidthType.DXA },
    columnWidths: [w1, w2, w3],
    rows,
  });
}

// Callout box
function callout(title, body) {
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [CONTENT_W],
    rows: [
      new TableRow({
        children: [
          new TableCell({
            width: { size: CONTENT_W, type: WidthType.DXA },
            margins: { top: 200, bottom: 200, left: 280, right: 280 },
            shading: calloutShade,
            borders: {
              top: { style: BorderStyle.SINGLE, size: 4, color: "E0A800" },
              bottom: { style: BorderStyle.SINGLE, size: 4, color: "E0A800" },
              left:  { style: BorderStyle.SINGLE, size: 24, color: "E0A800" },
              right: { style: BorderStyle.SINGLE, size: 4, color: "E0A800" },
            },
            children: [
              new Paragraph({
                spacing: { after: 100 },
                children: [new TextRun({ text: title, bold: true, size: 24 })],
              }),
              ...(Array.isArray(body) ? body : [body]).map(text =>
                new Paragraph({
                  spacing: { after: 80, line: 280 },
                  children: [new TextRun({ text, size: 22 })],
                })
              ),
            ],
          }),
        ],
      }),
    ],
  });
}

// ---------- Content ----------
const titlePage = [
  new Paragraph({
    alignment: AlignmentType.LEFT,
    spacing: { after: 320 },
    children: [new ImageRun({
      type: "png",
      data: logoBuffer,
      transformation: { width: 220, height: 57 },
      altText: { title: "MaiaEdge logo", description: "MaiaEdge logo", name: "MaiaEdgeLogo" },
    })],
  }),
  new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: "REFERENCE ARCHITECTURE", bold: true, color: "C2410C", size: 22 })],
  }),
  new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: "Federated Interconnection Platform", bold: true, size: 56, color: "1F2937" })],
  }),
  new Paragraph({
    spacing: { after: 160 },
    children: [new TextRun({ text: "Example deployment model", italics: true, size: 28, color: "374151" })],
  }),
  new Paragraph({
    spacing: { after: 320, line: 320 },
    children: [new TextRun({
      text: "An illustrative reference architecture for delivering carrier-neutral, AI-ready interconnect and multi-cloud onramp services across a five-site national footprint, anchored by a single fabric hub. Site names, capacities, and customer details in this document are generic placeholders intended to convey the deployment model.",
      italics: true, size: 22, color: "374151",
    })],
  }),
  table2(
    ["", ""],
    [
      ["Prepared for", "Sample / Illustrative Customer"],
      ["Sponsor",      "[Customer sponsor — name, title]"],
      ["Prepared by",  "MaiaEdge"],
      ["Document",     "Generic reference architecture · Example v1"],
    ],
    [2400, 6960]
  ),
  new Paragraph({ spacing: { before: 400 }, children: [new TextRun({ text: "CONFIDENTIAL — Shared as an example reference architecture", color: "6B7280", size: 20, italics: true })] }),
  new Paragraph({ children: [new PageBreak()] }),
];

// 1. Executive Summary
const section1 = [
  h1("1. Executive Summary"),
  p("This document describes a federated MaiaEdge deployment for an interconnect operator building the next generation of carrier-neutral, AI-ready interconnection facilities across high-growth, underserved markets. As the operator's footprint expands, every new site multiplies the operational complexity of stitching carriers, clouds, and customers together. The MaiaEdge platform absorbs that complexity, turns cross-site interconnect into an automated, software-defined service, and converts the operator's physical fiber footprint — together with DIA-only sites that have no dedicated wave — into a single national, monetizable interconnection fabric."),
  p("This reference architecture proposes a federated MaiaEdge deployment across five primary sites: a Hub Site (Region A), a Northeast Site (Region B), two West-region Sites (Region C and Region D), and a Central Site (Region E). The Hub Site is designated as the External Fabric Hub, landing the external fabric handoff (e.g., Equinix Fabric, Digital Realty Service Fabric, or a similar provider) and providing on-demand cloud onramps to AWS, Azure, GCP, and SaaS / partner providers. Dedicated long-haul wavelengths connect the Northeast Site and both West Sites to the Hub for premium, deterministic transport. The Central Site demonstrates a key property of the architecture: even without dedicated fiber, a site can join the fabric and reach every service through the redundant DIA-1 / DIA-2 mesh. MaiaEdge Path Border Controllers (PBCs) and Port Extenders at each site terminate carrier and customer fibers, replace the static Meet-Me Room (MMR) with a software-driven cross-connect plane, and stitch encrypted Layer-2 paths across every site, regardless of whether it has waves or only DIA."),
  callout(
    "Why this matters",
    "Every site becomes a programmable interconnection node — whether it is wave-connected (Hub, Northeast, West-1, West-2) or DIA-only (Central). New customers and partners self-provision cross-connects in minutes; carriers, hyperscalers, and content providers attach to a single fabric; the operator and its tenants see every service end-to-end, path-by-path and hop-by-hop; and the operator earns recurring revenue on every virtual port and cloud onramp sold through the MaiaEdge Marketplace."
  ),
  new Paragraph({ spacing: { before: 200, after: 120 }, children: [new TextRun({ text: "Strategic Outcomes at a Glance", bold: true, size: 26 })] }),
  table2(
    ["Business Outcome", "How the Architecture Delivers It"],
    [
      ["Faster time-to-revenue per site",      "Software-driven cross-connects let the operator light up a new tenant or carrier in minutes, not weeks of MMR cabling."],
      ["Differentiated AI / hyperscaler offer", "Encrypted L2 paths across diverse DIAs and a Hub-Site external fabric deliver low-latency, multi-cloud onramp from any site."],
      ["Higher revenue per cabinet",           "MaiaEdge Marketplace converts physical ports into recurring virtual port, cross-connect, and cloud onramp revenue streams."],
      ["Operational leverage",                 "One unified control plane replaces site-by-site manual processes, letting a small NOC team operate the full national footprint."],
      ["Coverage without fiber lock-in",       "DIA mesh extends the fabric to sites such as the Central Site where dedicated fiber waves are not yet available — no need to wait for new builds."],
      ["End-to-end service visibility",        "Every tenant service is observable path-by-path and hop-by-hop across the entire fabric — turning a chronic colo-customer pain into a differentiated operator value-add."],
      ["Carrier, cloud, and content (C3) magnetism", "Federated fabric makes the operator an attractive landing point for partners; every new partner increases the value of the marketplace flywheel."],
    ],
    [3400, 5960]
  ),
  new Paragraph({ children: [new PageBreak()] }),
];

// 2. About the Customer (now generic)
const section2 = [
  h1("2. About the Example Operator"),
  p("The illustrative customer profile referenced in this architecture is a carrier-neutral interconnection data center operator focused on high-demand, high-growth markets. The operator is purpose-built around the Carrier, Cloud, and Content (C3) ecosystem — the three customer segments whose interconnect needs are accelerating fastest in the AI era. The site footprint, capacities, and connectivity details below are generic placeholders chosen to show how the architecture scales across a mix of wave-connected and DIA-only sites."),
  h3("Example Site Footprint Referenced in this Architecture"),
  table3(
    ["Site", "Role in the Architecture", "Connectivity Profile"],
    [
      ["Hub Site (Region A)", "External Fabric Hub. External fabric on-ramp landing site.", "Carrier-neutral 2N / N+1 facility. Regional MMR. Wave terminus for the Northeast and both West Sites. External fabric uplink."],
      ["Northeast Site (Region B)", "Northeast interconnection node. Wave to the Hub.", "Regional carrier-neutral telecom facility. Long-haul fiber from multiple regional carriers. Regional NNI presence."],
      ["West Site 1 (Region C)", "West interconnection node. Wave to the Hub.", "Existing in-region presence; pairs with West Site 2 for in-market diversity."],
      ["West Site 2 (Region D)", "West interconnection node. Wave to the Hub. AI-ready power profile.", "Mid-size purpose-built interconnection data center with AI-ready power density and growth runway."],
      ["Central Site (Region E)", "Central / Midwest interconnection node. DIA-only — no dedicated wave.", "Larger Tier III+ facility. Reaches the fabric and external fabric hub via redundant DIA-1 / DIA-2 mesh — proving the architecture works without fiber."],
    ],
    [2200, 3300, 3860]
  ),
  h3("Strategic Drivers"),
  p("This architecture is shaped by three observable realities in the market:"),
  bullet("AI workloads are reshaping interconnect demand. Training and inference traffic spans GPU clusters, object stores, and multi-cloud tenants — all of which require deterministic, low-latency, and encrypted paths between sites and clouds."),
  bullet("Carrier-neutrality is the competitive moat. The architecture must preserve and amplify the operator's neutral position by giving every carrier, cloud, and content provider equal, programmatic access to every site."),
  bullet("Marketplaces win the C3 ecosystem. Sites that turn physical interconnect into an on-demand, self-service product capture more share of the C3 wallet than sites that rely on manual MMR provisioning. A site without dedicated fiber must still be able to participate — this architecture ensures it can."),
  new Paragraph({ children: [new PageBreak()] }),
];

// 3. Reference Architecture Overview
const section3 = [
  h1("3. Reference Architecture Overview"),
  p("At a high level, the architecture deploys a federated MaiaEdge fabric across all five example sites. Each site contains a redundant pair of MaiaEdge Path Border Controllers (PBCs) and Port Extenders that terminate customer fibers, carrier fibers, and the operator's internal cabinets. PBCs across sites are stitched together over two diverse Dedicated Internet Access (DIA) meshes — DIA-1 and DIA-2 — each running on independent fiber paths and providers."),
  p("The Hub Site is designated the External Fabric Hub. It carries the wave into the External Fabric (e.g., Equinix Fabric, Digital Realty Service Fabric, or an equivalent on-demand interconnection platform), which in turn provides on-demand cloud onramp into AWS, Azure, GCP, and a broad set of SaaS and partner providers. Three additional long-haul waves — Northeast ↔ Hub, West-1 ↔ Hub, and West-2 ↔ Hub — give wave-connected sites a deterministic path to the hub and to the cloud onramp. The Central Site joins the same fabric without a dedicated wave, using the DIA-1 / DIA-2 mesh to reach the Hub and every cloud onramp the hub exposes. Every L2 path between PBCs is encrypted and authenticated at line rate, regardless of whether it traverses a dedicated wave or the DIA underlay."),
  h3("Architecture Diagram"),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 120 },
    children: [new ImageRun({
      type: "png",
      data: diagramBuffer,
      transformation: { width: 624, height: 351 },
      altText: {
        title: "Federated Interconnection Reference Architecture diagram",
        description: "Five-site federated MaiaEdge fabric. Hub Site lands the External Fabric (e.g., Equinix Fabric, Digital Realty Service Fabric) and provides cloud onramps to AWS, Azure, GCP, and SaaS / partners. Northeast Site is wave-connected to the Hub. West Site 1, West Site 2, and Central Site reach the fabric via redundant DIA-1 and DIA-2 meshes; Central Site has no dedicated wave.",
        name: "ReferenceArchitectureDiagram",
      },
    })],
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 240 },
    children: [new TextRun({
      text: "Figure 1. MaiaEdge federated architecture across five example sites. The Hub Site hosts the External Fabric handoff; the Northeast Site is wave-connected to the Hub; West Site 1, West Site 2, and the Central Site reach the fabric and external hub via the redundant DIA-1 / DIA-2 mesh. The Central Site is DIA-only — no dedicated wave required.",
      italics: true, size: 20, color: "6B7280",
    })],
  }),
  h3("Reading the Diagram"),
  table2(
    ["Element", "Meaning"],
    [
      ["Solid red line",         "Primary DIA mesh path (DIA-1) between PBCs."],
      ["Solid yellow / orange line", "Secondary DIA mesh path (DIA-2) — physically and provider-diverse from DIA-1."],
      ["Purple line",            "Wave from the Hub Site into the External Fabric (cloud onramp)."],
      ["Olive / khaki lines",    "Waves between sites: Northeast ↔ Hub, West-1 ↔ Hub, West-2 ↔ Hub."],
      ["Green strands",          "Carrier fiber strands terminating into the carrier cage and PBC."],
      ["Yellow strands",         "Customer fiber strands terminating into the carrier cage and PBC."],
      ["Purple box at the Hub",  "Hub site — designated External Fabric Hub."],
      ["Black dashed box",       "External Fabric (Equinix Fabric / Digital Realty Service Fabric / equivalent, plus AWS, Azure, GCP, SaaS / partners)."],
      ["Central Site (no waves)","Fabric participation via DIA mesh only — no dedicated fiber required to reach the hub."],
    ],
    [2400, 6960]
  ),
  new Paragraph({ children: [new PageBreak()] }),
];

// 4. Core Components
const section4 = [
  h1("4. Core Components"),
  h2("4.1 MaiaEdge Path Border Controller (PBC)"),
  p("The Path Border Controller is the cornerstone of the architecture. It is a 1RU appliance that combines Layer-2 and Layer-3 functions, terminates carrier and customer fibers, and establishes encrypted, authenticated paths to every other PBC in the fabric. PBCs are deployed in redundant pairs at every site so that any single device, line card, or upstream fiber failure is absorbed without customer impact."),
  bullet("Dual 100 Gbps uplink ports per PBC for carrier and DIA-mesh connectivity (200G interfaces on roadmap)."),
  bullet("Line-rate encryption and authentication on every L2 path; no separate IPsec concentrator or third-party security overlay required."),
  bullet("Centralized control plane via the MaiaEdge Path Computation Engine (PCE) — no per-site BGP, VLAN, or stitching logic to maintain."),
  bullet("Deploys at the network boundary — carrier hotels, MMRs, and PoPs — exactly matching the operator's site topology."),
  h2("4.2 MaiaEdge Port Extender"),
  p("The Port Extender is a companion switch that scales tenant port density on each PBC pair. Each Port Extender adds up to 48 additional tenant-facing ports under the same control plane and security model as the PBC. This lets the operator grow customer density inside a cabinet without re-architecting the underlying fabric or introducing a second management layer."),
  h2("4.3 DIA Mesh (DIA-1 / DIA-2)"),
  p("Inter-site connectivity uses two diverse Dedicated Internet Access (DIA) circuits as the underlay. DIA-1 and DIA-2 are deliberately sourced from different upstream providers and routed over physically diverse fiber paths wherever feasible. MaiaEdge PBCs build encrypted L2 tunnels over both DIA meshes simultaneously, so a failure of any single carrier, fiber path, or DIA provider triggers automatic re-routing without human intervention. The DIA mesh is the workhorse that lets a DIA-only site (such as the Central Site in this example) fully participate in the fabric, before any dedicated wave is in place."),
  h2("4.4 Long-Haul Wave Services"),
  p("For premium, deterministic transport between primary sites, the operator supplements the DIA mesh with dedicated wavelengths terminating at the Hub Site: Northeast ↔ Hub, West-1 ↔ Hub, and West-2 ↔ Hub. Waves provide an SLA-grade, low-jitter underlay for high-bandwidth tenant flows and are exposed to customers as a premium service tier in the MaiaEdge Marketplace. Sites without a wave (the Central Site in this example) operate on DIA mesh only; the operator may add dedicated waves as those markets justify the build."),
  h2("4.5 Carrier Cage and MMR Modernization"),
  p("The carrier cage at each site terminates incoming carrier fibers (green strands) and customer fibers (yellow strands) directly into the MaiaEdge PBCs. The PBCs effectively serve as a software-defined Meet-Me Room: any carrier port can be stitched to any customer port — locally or across sites — through the MaiaEdge control plane, replacing manual cross-connect tickets with API- and portal-driven provisioning."),
  h2("4.6 External Fabric Hub"),
  p("The Hub Site is the External Fabric Hub. It carries the wave into the External Fabric (Equinix Fabric, Digital Realty Service Fabric, or a similar on-demand interconnection platform), which in turn provides on-demand cloud onramp into AWS, Azure, GCP, and a broad set of SaaS and partner providers. Because the External Fabric is reached through MaiaEdge, every other site — Northeast, West-1, West-2, and the Central Site — inherits the same multi-cloud onramp without needing its own physical fabric port. The Central Site specifically reaches this onramp over the DIA mesh, demonstrating that fabric participation is not gated by dedicated long-haul fiber."),
  h2("4.7 MaiaEdge Marketplace"),
  p("The Marketplace is the commercial expression of the fabric. The operator — and its partner providers — can advertise and sell products such as cross-site L2 connectivity, cloud onramps, partner-to-partner peering, and value-added services through a unified portal and API. Provisioning is automated end-to-end: a customer order results in encrypted L2 paths and PBC port assignments without any change-control ticket or truck roll, regardless of whether the underlay is a dedicated wave or the DIA mesh."),
  new Paragraph({ children: [new PageBreak()] }),
];

// 5. Service Catalog
const section5 = [
  h1("5. Service Catalog Enabled by the Architecture"),
  p("The architecture is intentionally designed to expose services that match the buying patterns of carrier, cloud, and content (C3) customers, and to make those services orderable through both portal and API."),
  table3(
    ["Service", "What the Operator Sells", "Underlying Architecture"],
    [
      ["Cross-site Private L2",        "Encrypted Layer-2 circuits between any two operator sites at customer-selectable bandwidths.", "MaiaEdge PBC encrypted L2 paths over the DIA-1 / DIA-2 mesh, augmented by wave services where available."],
      ["Multi-Cloud Onramp",           "On-demand virtual connections from any operator site (including the DIA-only Central Site) to AWS, Azure, GCP, and supported SaaS providers.", "External Fabric hub at the Hub Site; cross-site stitching via MaiaEdge."],
      ["Programmable Cross-Connect (Virtual MMR)", "Self-service cross-connects between any two ports inside a site, provisioned in minutes.", "PBC + Port Extender as software-defined MMR."],
      ["Premium Wave Services",        "Dedicated long-haul wavelengths for high-bandwidth, deterministic flows into the Hub Site.", "Northeast ↔ Hub, West-1 ↔ Hub, West-2 ↔ Hub waves; complement DIA mesh for premium tiers."],
      ["Partner-to-Partner Peering",   "Federated peering between operator-hosted partners and partners hosted in other MaiaEdge-enabled providers.", "MaiaEdge federated control plane; trust and policy enforced per partner."],
      ["AI / GPU Interconnect",        "Low-latency, encrypted paths between AI compute, storage, and inference endpoints across sites.", "DIA mesh + line-rate encryption on PBCs; waves where available; AI-ready sites provide power and density."],
    ],
    [2200, 3300, 3860]
  ),
  new Paragraph({ children: [new PageBreak()] }),
];

// 6. Resiliency
const section6 = [
  h1("6. Resiliency and Redundancy Model"),
  p("Resiliency is engineered at every layer so that no single failure removes a customer service. The principles below are reflected directly in the diagram."),
  table2(
    ["Failure Domain", "Protection Mechanism"],
    [
      ["PBC device failure",            "Redundant PBC pair at every site; live failover with no session loss."],
      ["Port Extender failure",         "Tenants can be dual-homed across two Port Extenders within the cabinet."],
      ["Carrier fiber cut (single strand)", "Strand-1 / Strand-2 termination per cabinet; PBC re-homes tenant traffic."],
      ["Single DIA provider outage",    "DIA-1 and DIA-2 meshes are provider- and path-diverse; PBCs continuously use both. Critical for any DIA-only site such as the Central Site in this example."],
      ["Wave outage (Northeast / West-1 / West-2 ↔ Hub)", "Affected site's traffic falls back to the DIA-1 / DIA-2 mesh automatically; service continues at DIA performance until the wave is restored."],
      ["Site outage at a non-hub site", "DIA mesh routes traffic around the impacted site; remaining sites continue to reach the Hub and External Fabric."],
      ["Hub site impairment",           "Local services unaffected at other sites; cloud-onramp failover plan activated. Long-term roadmap: a second External Fabric Hub for full hub redundancy."],
    ],
    [3000, 6360]
  ),
];

// 7. Security
const section7 = [
  h1("7. Security and Trust Model"),
  p("Security is built into the fabric itself rather than bolted on. Every L2 path between PBCs is encrypted and authenticated at line rate — protecting tenant traffic across the DIA mesh and waves alike, without requiring per-tenant VPN concentrators or out-of-band crypto appliances. Tenant isolation, policy enforcement, and audit are managed centrally."),
  bullet("Encryption: line-rate encryption on every inter-PBC L2 path. Keys are rotated and managed centrally by the MaiaEdge control plane."),
  bullet("Authentication: every PBC mutually authenticates with its peers; rogue or swapped devices cannot join the fabric."),
  bullet("Tenant isolation: each customer is logically isolated end-to-end; cross-tenant leakage is prevented at the PBC silicon, not by post-hoc ACLs."),
  bullet("Federated trust: partner-to-partner peering uses explicit, auditable trust policies — the operator controls who can advertise into its marketplace and what they may see."),
  bullet("Operational separation: the operator's management traffic is logically separated from tenant data planes on every PBC."),
  new Paragraph({ children: [new PageBreak()] }),
];

// 8. End-to-End Service Visibility
const section8 = [
  h1("8. End-to-End Service Visibility"),
  p("One of the most chronic, unsolved problems in the colocation industry is what happens when a tenant says \"my service is slow.\" The customer can see only their own end. The colo provider can see only its own facility and underlay. Carriers can see only the segments they operate. The result is finger-pointing, long mean-time-to-resolution, and a recurring trust tax on the colo-customer relationship."),
  p("The MaiaEdge architecture eliminates this opacity. Because every L2 path between sites is constructed and managed by the MaiaEdge control plane, the fabric itself produces continuous, path-aware telemetry — and the operator and its tenants can see exactly how each service is performing, path-by-path and hop-by-hop, end-to-end."),
  h3("8.1 What the Operator and its Customers Can See"),
  bullet("Per-service path view: for every tenant service, the exact path through the fabric — from the ingress PBC port, across the chosen underlay (wave or DIA), to the egress PBC port at the destination site or cloud onramp."),
  bullet("Hop-by-hop telemetry: latency, jitter, loss, and utilization measured at every PBC hop along the path, with deltas between hops to localize impairments."),
  bullet("Underlay correlation: when a service degrades, the operator can immediately tell whether the cause is the wave, a specific DIA provider, a carrier strand, or a tenant-side configuration — no triage call required."),
  bullet("Per-tenant SLA visibility: tenants see their own service performance against the contracted tier (premium wave vs. best-effort DIA), exposed through the Marketplace portal and API."),
  bullet("Historical and real-time: streaming telemetry for live troubleshooting plus rolled-up history for capacity planning, SLA reporting, and post-incident review."),
  h3("8.2 Why This is a Differentiator"),
  table2(
    ["Industry Pain Point", "How the Architecture Resolves It"],
    [
      ["Customer reports degradation; cause is unknown", "Path view + hop-by-hop telemetry localize the impairment in seconds, before a ticket even opens."],
      ["Finger-pointing between colo, carrier, and customer", "Single source of truth across every hop — including DIA underlay segments — removes ambiguity about who owns the issue."],
      ["Tenants have no visibility once traffic leaves their cabinet", "Tenants see their own service performance end-to-end through the Marketplace portal."],
      ["Long MTTR on cross-site or cloud-onramp issues", "Operators can pinpoint the offending hop or wave/DIA segment immediately and re-route via the alternate underlay."],
      ["SLA disputes are hard to resolve", "Per-service, per-tier telemetry provides the evidence base for SLA credits or premium-tier upsell conversations."],
      ["DIA-only sites feel \"second class\"", "Same end-to-end visibility applies to DIA paths — tenants on DIA-only sites get the same observability story as wave-connected sites."],
    ],
    [3400, 5960]
  ),
  h3("8.3 How It is Delivered"),
  bullet("PBCs emit streaming telemetry on every L2 path they participate in — both wave and DIA underlays — to the MaiaEdge Path Computation Engine (PCE)."),
  bullet("PCE correlates per-hop telemetry into per-service path views and exposes them through portal, API, and webhooks for the operator's CRM, ticketing, and observability stacks."),
  bullet("Tenant-scoped views are filtered automatically: each customer sees only the paths and metrics that belong to its services."),
  bullet("Alarms and anomaly detection are wired into the operator's NOC tooling, with rich context (path, hops, underlay, tenant) included in every alert."),
  new Paragraph({ children: [new PageBreak()] }),
];

// 9. Operational Model
const section9 = [
  h1("9. Operational Model"),
  p("The architecture is designed so that one small operations team can run the full national fabric. Day-to-day operations shift from hands-on cabling and ticket-driven cross-connects to API-driven service orchestration."),
  h3("9.1 Day-0: Site Bring-up"),
  bullet("Install redundant PBC pair and Port Extenders in each new cabinet."),
  bullet("Terminate carrier and customer fibers from the carrier cage into the PBCs."),
  bullet("Provision DIA-1 and DIA-2 circuits with diverse providers; bring up encrypted L2 paths. (For wave-connected sites, also bring up the wave to the Hub Site.)"),
  bullet("Register the new site in the MaiaEdge control plane and Marketplace — sites without a wave are activated identically."),
  h3("9.2 Day-1: Customer / Carrier Onboarding"),
  bullet("Customer or carrier port assigned via the MaiaEdge portal or API."),
  bullet("Cross-connect, L2 path, or cloud onramp ordered — provisioning completes in minutes, not weeks."),
  bullet("Billing meter starts automatically against the ordered service tier."),
  h3("9.3 Day-2: Steady-state Operations"),
  bullet("Single pane of glass for fabric health, capacity, and tenant SLAs across wave and DIA underlays."),
  bullet("Streaming telemetry from every PBC into the operator's observability stack."),
  bullet("Automated change windows; no manual MMR ticket queue."),
  bullet("API-first integration with the operator's CRM, ticketing, and billing systems."),
];

// 10. Business Outcomes
const section10 = [
  h1("10. Business Outcomes and Monetization Model"),
  p("The architecture is engineered to convert physical fiber, wave, and DIA investments into a recurring, software-driven revenue model. The outcomes below are the primary business cases for the deployment."),
  table3(
    ["Outcome", "Indicative Lever", "Why the Architecture Enables It"],
    [
      ["Higher revenue per port",   "Convert physical ports into multiple billable virtual services.", "PBC + Port Extender expose each physical port as many software-defined services that can be sold, metered, and renewed independently."],
      ["Faster time-to-revenue",    "Days-to-minutes provisioning for new tenants.",                    "Automated cross-connect and cloud-onramp eliminate ticket queues and truck rolls."],
      ["Lower operating cost per site", "One unified control plane vs. site-specific tooling.",         "Federated MaiaEdge management replaces site-by-site MMR processes."],
      ["New revenue: cloud onramp", "Sell AWS / Azure / GCP onramp from every site.",                   "External Fabric hub at the Hub Site is reachable from every site via wave or DIA — including DIA-only sites with no dedicated fiber."],
      ["Two-tier transport pricing","Premium wave tier and best-effort DIA tier for the same logical service.", "Same MaiaEdge L2 service offered over wave (premium SLA) or DIA (best-effort) — same provisioning, different commercial tier."],
      ["Visibility-as-a-product",   "Sell a paid \"observability\" tier (or include it in premium) so tenants can see their own service end-to-end.", "Per-service, hop-by-hop telemetry from every PBC; tenant-scoped views in the Marketplace portal."],
      ["Lower MTTR and ticket volume", "Cut time-to-resolve cross-site / onramp issues and reduce inbound tickets per tenant.", "Path-aware telemetry localizes impairments before tickets open and removes finger-pointing across colo / carrier / customer."],
      ["Marketplace flywheel",      "Each new partner increases value of every existing port.",         "Federated control plane lets partners advertise into and consume from the MaiaEdge Marketplace."],
    ],
    [2200, 3300, 3860]
  ),
  new Paragraph({ children: [new PageBreak()] }),
];

// 11. Roadmap
const section11 = [
  h1("11. Suggested Phased Roadmap"),
  p("The deployment is naturally phased so the operator earns revenue and operational experience as the footprint grows."),
  table3(
    ["Phase", "Scope", "Outcome"],
    [
      ["Phase 0 — Pilot",                 "Deploy redundant PBCs at the Hub Site and one second site (e.g., the Northeast Site). Bring up DIA-1 / DIA-2 mesh and the Northeast ↔ Hub wave. Stand up the External Fabric hub at the Hub Site.", "Validate L2 path performance, encryption, and self-service provisioning. First Marketplace transactions on a pilot tenant set."],
      ["Phase 1 — National Mesh",         "Extend PBCs to West-1, West-2, and the Central Site. Activate full DIA mesh. Light West-1 ↔ Hub and West-2 ↔ Hub waves.", "Every site is interconnect-ready and Marketplace-enabled. The Central Site is live on DIA-only, demonstrating the fabric extends beyond the wave footprint."],
      ["Phase 2 — Marketplace Scale-out", "Onboard initial wave of carrier, cloud, and content partners. Publish service catalog. Integrate with the operator's CRM and billing.", "First recurring marketplace revenue; partner-driven port density growth."],
      ["Phase 3 — Federation",            "Federate the MaiaEdge fabric with partner providers; expose operator interconnect in third-party marketplaces and vice versa.", "Operator reach extends beyond owned sites; flywheel acceleration."],
      ["Phase 4 — Wave Densification & Second Hub", "Add a Central-Site wave (when justified) and a second External Fabric Hub for hub redundancy and East/West cloud-onramp diversity.", "Premium-tier coverage matches the entire footprint; full hub-level HA."],
    ],
    [2200, 3960, 3200]
  ),
  new Paragraph({ children: [new PageBreak()] }),
];

// 12. Risks
const section12 = [
  h1("12. Key Risks and Mitigations"),
  table2(
    ["Risk", "Mitigation"],
    [
      ["Hub-site dependency for cloud onramp",     "Roadmap includes a second External Fabric Hub; near-term mitigation via route diversity within the external fabric provider."],
      ["DIA provider concentration — especially impactful for DIA-only sites", "Two diverse providers from day one; quarterly review of carrier diversity and route-disjoint testing. The Central Site is the canary site for DIA-only performance assurance."],
      ["Wave-tier customer expectations for non-wave sites", "Service catalog clearly differentiates wave (premium SLA) from DIA (best-effort) tiers; DIA-only customers buy the DIA tier explicitly."],
      ["Operational change for staff (manual MMR → API)", "Phased rollout with MaiaEdge enablement and shadow-running existing MMR process during pilot."],
      ["Marketplace cold-start (few initial partners)", "Anchor on existing operator carrier and cloud partners in Phase 2; use federation in Phase 3 to import demand."],
      ["Encryption / compliance concerns from regulated tenants", "Line-rate L2 encryption + auditable tenant isolation; mapping to common compliance frameworks documented as part of onboarding."],
    ],
    [3400, 5960]
  ),
];

// 13. Glossary
const section13 = [
  h1("13. Glossary"),
  table2(
    ["Term", "Definition"],
    [
      ["PBC",            "Path Border Controller. MaiaEdge's 1RU edge appliance combining L2/L3 and line-rate encryption."],
      ["PCE",            "Path Computation Engine. The cloud-based MaiaEdge control plane that computes optimal paths and enforces SLAs across PBCs."],
      ["Port Extender",  "Companion switch that adds up to 48 tenant-facing ports under the PBC control plane."],
      ["DIA",            "Dedicated Internet Access — high-capacity carrier circuits used as the underlay for the MaiaEdge mesh. The sole underlay for sites without dedicated fiber."],
      ["Wave",           "Dedicated long-haul wavelength service. In this example: Northeast ↔ Hub, West-1 ↔ Hub, West-2 ↔ Hub, plus Hub ↔ External Fabric."],
      ["MMR",            "Meet-Me Room — the colocation room where carriers and tenants traditionally cross-connect; here, replaced by software."],
      ["External Fabric","An on-demand interconnection platform for cloud onramps and partner peering (e.g., Equinix Fabric, Digital Realty Service Fabric, or similar)."],
      ["Hub Site",       "Designated site that lands external fabric services for the rest of the footprint."],
      ["C3",             "Carrier, Cloud, Content — the operator's primary customer ecosystem."],
      ["Marketplace",    "MaiaEdge's commercial layer for advertising, ordering, and provisioning fabric services."],
    ],
    [2200, 7160]
  ),
];

// 14. Next Steps
const section14 = [
  h1("14. Recommended Next Steps"),
  bullet("Confirm the in-scope sites and fiber inventories at each location with the operator's operations team."),
  bullet("Validate diverse DIA provider candidates per site — with extra rigor for any DIA-only site given the absence of a dedicated wave."),
  bullet("Agree on the Phase-0 pilot scope (Hub Site + one second site), success criteria, and target go-live."),
  bullet("Align Marketplace integration on CRM, ticketing, and billing endpoints."),
  bullet("Schedule joint operational readiness review prior to Phase-1 rollout."),
  new Paragraph({ spacing: { before: 400 }, alignment: AlignmentType.CENTER, children: [new TextRun({ text: "— End of document —", italics: true, color: "6B7280", size: 22 })] }),
];

// ---------- Build doc ----------
const doc = new Document({
  creator: "MaiaEdge",
  title: "Federated Interconnection Platform — Reference Architecture (Generic)",
  description: "Generic example reference architecture for a federated interconnection platform deployment.",
  styles: {
    default: {
      document: { run: { font: "Arial", size: 22 } },
    },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: "1F2937" },
        paragraph: { spacing: { before: 320, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: "1F2937" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: "1F2937" },
        paragraph: { spacing: { before: 200, after: 100 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [
          new Paragraph({
            tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
            spacing: { after: 60 },
            children: [
              new ImageRun({
                type: "png",
                data: logoBuffer,
                transformation: { width: 100, height: 26 },
                altText: { title: "MaiaEdge logo", description: "MaiaEdge logo", name: "MaiaEdgeLogoHeader" },
              }),
              new TextRun({ text: "\tReference Architecture · Generic Example", size: 18, color: "6B7280", italics: true }),
            ],
            border: { bottom: { color: "E5E7EB", style: BorderStyle.SINGLE, size: 4, space: 4 } },
          }),
        ],
      }),
    },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
            children: [
              new TextRun({ text: "MaiaEdge · Federated Interconnection Platform · Confidential", size: 18, color: "6B7280" }),
              new TextRun({ text: "\tPage " }),
              new TextRun({ children: [PageNumber.CURRENT], size: 18 }),
            ],
            border: { top: { color: "E5E7EB", style: BorderStyle.SINGLE, size: 4, space: 4 } },
          }),
        ],
      }),
    },
    children: [
      ...titlePage,
      ...section1,
      ...section2,
      ...section3,
      ...section4,
      ...section5,
      ...section6,
      ...section7,
      ...section8,
      ...section9,
      ...section10,
      ...section11,
      ...section12,
      ...section13,
      ...section14,
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("/sessions/nifty-determined-turing/mnt/Customer/MaiaEdge-Federated-Interconnection-Reference-Architecture-Generic.docx", buf);
  console.log("OK — wrote generic reference architecture");
});
