"""
MaiaEdge Partner Doc PDF Builder
Generates branded PDFs from the partner-doc markdown sources using brand.css
and a shared cover/section template.
"""
import re
import shutil
from pathlib import Path
import markdown
from weasyprint import HTML

HERE = Path(__file__).parent
MD_DIR = Path("/sessions/practical-confident-mayer/mnt/partner docs/markdown")
OUT_DIR = Path("/sessions/practical-confident-mayer/mnt/partner docs/final")
OUT_DIR.mkdir(parents=True, exist_ok=True)

DOCS = [
    {
        "md":          "cheatsheet-colocation.md",
        "out_pdf":     "Cheat-Sheet-Colocation.pdf",
        "title":       "Colocation",
        "title_accent": "Cheat Sheet.",
        "segment_tag": "Partner Cheat Sheet",
        "segment_sub": "MaiaEdge for Colocation Operators (Standard + AI)",
        "subtitle":    "Use this when you're calling on data center operators, carrier hotels, "
                       "interconnection facilities, or AI-ready colos.",
        "icon":        "DC Cabinet.svg",
    },
    {
        "md":          "cheatsheet-fiber-operator.md",
        "out_pdf":     "Cheat-Sheet-Fiber-Operator.pdf",
        "title":       "Fiber Operator",
        "title_accent": "Cheat Sheet.",
        "segment_tag": "Partner Cheat Sheet",
        "segment_sub": "MaiaEdge for Fiber Operators",
        "subtitle":    "Use this when you're calling on regional CLECs, long-haul backbones, "
                       "dark fiber specialists, or muni / co-op fiber operators.",
        "icon":        "Topology.svg",
    },
    {
        "md":          "cheatsheet-network-operator.md",
        "out_pdf":     "Cheat-Sheet-Network-Operator.pdf",
        "title":       "Network Operator",
        "title_accent": "Cheat Sheet.",
        "segment_tag": "Partner Cheat Sheet",
        "segment_sub": "MaiaEdge for Tier 1 / Tier 2 Carriers",
        "subtitle":    "Use this when you're calling on national or global carriers, MPLS "
                       "providers, or wholesale connectivity operators.",
        "icon":        "Router.svg",
    },
    {
        "md":          "cheatsheet-neocloud.md",
        "out_pdf":     "Cheat-Sheet-Neocloud.pdf",
        "title":       "Neocloud",
        "title_accent": "Cheat Sheet.",
        "segment_tag": "Partner Cheat Sheet",
        "segment_sub": "MaiaEdge for GPU Cloud Providers",
        "subtitle":    "Use this when you're calling on Lambda, Crusoe, Voltage Park, Together AI, "
                       "Nebius, Groq, Cirrascale, IREN, and similar GPU-as-a-service operators.",
        "icon":        "Lab Server.svg",
    },
    {
        "md":          "cheatsheet-msp-aggregator.md",
        "out_pdf":     "Cheat-Sheet-MSP-Aggregator.pdf",
        "title":       "MSP / Aggregator",
        "title_accent": "Cheat Sheet.",
        "segment_tag": "Partner Cheat Sheet",
        "segment_sub": "MaiaEdge for MSPs, TSDs, TAs, and NaaS Platform Operators",
        "subtitle":    "Use this when you're calling on Telarus, AppDirect, Upstack, AVANT, "
                       "Bridgepointe, Intelisys, Sandler, or NaaS platforms like Console Connect.",
        "icon":        "Customers.svg",
    },
    {
        "md":          "product-quick-reference.md",
        "out_pdf":     "Product-Quick-Reference.pdf",
        "title":       "Product",
        "title_accent": "Quick Reference.",
        "segment_tag": "Partner Edition",
        "segment_sub": "MaiaEdge Hardware + Software Reference",
        "subtitle":    "The technical detail you need to handle a customer's "
                       "\"show me the architecture\" question. Pair this with MaiaEdge 101.",
        "icon":        "MaiaEdgeBox_black and yellow.svg",
    },
]


def parse_markdown(md_text):
    lines = md_text.splitlines()
    out = []
    skipped_h1 = False
    skipped_intro = 0
    for line in lines:
        if not skipped_h1:
            if line.startswith("# "):
                skipped_h1 = True
                continue
            if line.strip() == "":
                continue
            out.append(line)
        else:
            stripped = line.strip()
            if skipped_intro < 4 and (
                stripped.startswith("**") or stripped.startswith("*") or
                stripped == "" or stripped == "---"
            ):
                skipped_intro += 1
                continue
            out.append(line)
    text = "\n".join(out)
    # Ensure numbered/bulleted lists have a blank line before them so markdown
    # parses them as lists rather than inline text.
    text = re.sub(
        r"(?m)^(?!\s*$)(?![\-\*\+]\s)(?!\d+\.\s)(?!#)(?!\>)(.+)\n(\s*\d+\.\s)",
        r"\1\n\n\2", text,
    )
    text = re.sub(
        r"(?m)^(?!\s*$)(?![\-\*\+]\s)(?!\d+\.\s)(?!#)(?!\>)(.+)\n([\-\*\+]\s)",
        r"\1\n\n\2", text,
    )
    return text


def md_to_html(md_text):
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
    return md.convert(md_text)


def replace_code_blocks_with_diagrams(html, doc_md):
    """For Product Quick Reference, swap the 3 ASCII code blocks for designed
    PNG diagrams. Detects the blocks by their unique opening text."""
    if "product-quick-reference" not in doc_md:
        return html
    diagrams = [
        ("[Customer Portal", "assets/architecture-diagram.svg", "MaiaEdge System Architecture"),
        ("1. Deploy PBC at network boundary", "assets/activation-flow-diagram.svg", "Activation Flow"),
        ("[Operator's Customer]", "assets/cloud-onramp-diagram.svg", "Cloud On-Ramp Architecture"),
    ]
    for opener, png, alt in diagrams:
        # Allow optional whitespace/newlines after <code> before the opener
        pattern = re.compile(
            r"<pre><code>\s*" + re.escape(opener) + r".*?</code></pre>",
            re.DOTALL,
        )
        replacement = f'<div class="diagram"><img src="{png}" alt="{alt}"/></div>'
        html, n = pattern.subn(replacement, html, count=1)
        if n == 0:
            print(f"WARN  No match for diagram: {opener!r}")
    return html


def post_process_html(html):
    """Apply brand styling rules to raw markdown HTML output."""
    parts = re.split(r"(<h2>.*?</h2>)", html, flags=re.DOTALL)
    rebuilt = []
    section_count = 0
    open_section = False
    for part in parts:
        m = re.match(r"<h2>(.*?)</h2>", part, flags=re.DOTALL)
        if m:
            if open_section:
                rebuilt.append("</section>")
            section_count += 1
            num = f"{section_count:02d}"
            title = m.group(1).strip()
            rebuilt.append(
                f'<section class="section">\n'
                f'<div class="eyebrow"><span class="num">{num}</span>'
                f'{eyebrow_label(title)}</div>\n'
                f'<h1 class="section-title">{title}</h1>\n'
            )
            open_section = True
        else:
            rebuilt.append(part)
    if open_section:
        rebuilt.append("</section>")
    html = "".join(rebuilt)
    html = re.sub(r"<h3>(.*?)</h3>", r'<h2 class="sub-title">\1</h2>', html, flags=re.DOTALL)

    def group_blockquotes(match):
        bqs = re.findall(r"<blockquote>(.*?)</blockquote>", match.group(0), flags=re.DOTALL)
        items = []
        for q in bqs:
            inner = q.strip()
            inner = re.sub(r"^\s*<p>(.*)</p>\s*$", r"\1", inner, flags=re.DOTALL).strip()
            items.append(f'<div class="pain-quote">{inner}</div>')
        return f'<div class="pain-grid">\n' + "\n".join(items) + "\n</div>"
    html = re.sub(r"(?:<blockquote>.*?</blockquote>\s*)+", group_blockquotes, html, flags=re.DOTALL)

    def style_table(match):
        tbl = match.group(0)
        ths = re.findall(r"<th[^>]*>(.*?)</th>", tbl, flags=re.DOTALL)
        classes = []
        if len(ths) >= 4:
            classes.append("wide")
        joined = " ".join(t.lower() for t in ths)
        if any(k in joined for k in ("question", "objection", "the pitch", "rebuttal", "good answer", "customer says", "your response")):
            classes.append("qa")
        if classes:
            return tbl.replace("<table>", f'<table class="{" ".join(classes)}">')
        return tbl
    html = re.sub(r"<table>.*?</table>", style_table, html, flags=re.DOTALL)
    html = re.sub(r"<hr\s*/?>", "", html)
    return f'<div class="md">{html}</div>'


def eyebrow_label(title):
    t = title.lower()
    if "know your customer" in t: return "ICP PROFILE"
    if "problems we solve" in t: return "PROBLEMS / SOLUTIONS"
    if "pain points" in t: return "PAIN POINTS"
    if "discovery" in t: return "DISCOVERY"
    if "objection" in t: return "OBJECTIONS"
    if "competitive" in t: return "COMPETITIVE"
    if "persona" in t: return "PERSONA TALK TRACKS"
    if "proof" in t: return "PROOF POINTS"
    if "exclusion" in t: return "EXCLUSIONS"
    if "vocabulary" in t: return "LANGUAGE"
    if "sub-segment" in t or "cheat code" in t: return "SUB-SEGMENT GUIDE"
    if "geographic" in t: return "GEOGRAPHY"
    if "track a" in t: return "TRACK A / TRACK B"
    if "ai signal" in t: return "AI SIGNAL DETECTION"
    if "special" in t: return "SPECIAL CASES"
    if "system in one picture" in t: return "ARCHITECTURE"
    if "pbc" in t and "path border" in t: return "PBC HARDWARE"
    if "pce" in t and "path computation" in t: return "PCE SOFTWARE"
    if "port extender" in t: return "PORT EXTENDER"
    if "layer 2.5" in t: return "LAYER 2.5"
    if "path gets activated" in t: return "ACTIVATION FLOW"
    if "transport flexibility" in t: return "TRANSPORT"
    if "cloud on-ramp" in t: return "CLOUD ON-RAMP"
    if "deployment patterns" in t: return "DEPLOYMENT PATTERNS"
    if "subscription" in t: return "WHAT'S INCLUDED"
    if "sku" in t: return "SKU REFERENCE"
    if "does not need" in t: return "WHAT YOU DON'T NEED"
    if "faq" in t: return "FAQ"
    if "where to get help" in t: return "ENGAGE"
    return "SECTION"


COVER_HTML = """\
<section class="cover">
  <div class="cover-eyebrow">{segment_tag}</div>
  <div class="cover-meta">Confidential<br/>For Partner Use</div>
  <img src="assets/logo-white.svg" alt="MaiaEdge" class="cover-logo"/>
  <div class="cover-icon-block">
    <div class="cover-icon"><img src="assets/{icon}" alt=""/></div>
    <div>
      <div class="cover-segment-tag">{segment_tag}</div>
      <div class="cover-segment-sub">{segment_sub}</div>
    </div>
  </div>
  <h1 class="cover-title">{title}<br/><span class="accent">{title_accent}</span></h1>
  <p class="cover-sub">{subtitle}</p>
  <div class="cover-tagline-block">
    <p class="cover-tagline">Private paths. Any network. Instantly.</p>
    <p class="cover-tagline-sub">Carrier infrastructure for federated private networking</p>
  </div>
</section>
"""

PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} - MaiaEdge Partner</title>
<link rel="stylesheet" href="brand.css"/>
</head>
<body>
{cover}
{body}
</body>
</html>
"""


def build(doc):
    md_path = MD_DIR / doc["md"]
    md_text = md_path.read_text(encoding="utf-8")
    cleaned = parse_markdown(md_text)
    raw_html = md_to_html(cleaned)
    raw_html = replace_code_blocks_with_diagrams(raw_html, doc["md"])
    body_html = post_process_html(raw_html)
    cover = COVER_HTML.format(**doc)
    full_html = PAGE_TEMPLATE.format(title=doc["title"], cover=cover, body=body_html)
    html_path = HERE / f"_build_{Path(doc['md']).stem}.html"
    html_path.write_text(full_html, encoding="utf-8")
    pdf_path = OUT_DIR / doc["out_pdf"]
    HTML(filename=str(html_path), base_url=str(HERE)).write_pdf(str(pdf_path))
    print(f"OK  {doc['out_pdf']}  ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    for d in DOCS:
        build(d)
    src = HERE / "MaiaEdge-101-Branded.pdf"
    if src.exists():
        shutil.copy(src, OUT_DIR / "MaiaEdge-101.pdf")
        print(f"OK  MaiaEdge-101.pdf  (copied)")
    print("\nAll outputs in:", OUT_DIR)
