#!/usr/bin/env python3
"""
Extract candidate headlines from a saved web_fetch HTML response.

Usage:
    python3 headline_extract.py <html_file> <segment> <window_start> <window_end>

Args:
    html_file       Path to a saved HTML response file (UTF-8).
    segment         One of: colocation | fiber | neocloud | network-operator | msp-aggregator | enterprise
    window_start    YYYY-MM-DD (inclusive)
    window_end      YYYY-MM-DD (inclusive)

Output (stdout):
    JSON array of {date, headline_text, link_url, signal_keyword_matched, company_candidates[]},
    sorted by (date desc, keyword-match-count desc).

Strategy (deterministic, no LLM):
    1. Parse HTML with regex (no BeautifulSoup dependency required).
    2. Scan <a href="...">text</a> blocks site-wide.
    3. For each anchor: extract text + ±300-char surrounding context.
    4. Parse date from context (ISO, US, "April 28, 2026", "28 April 2026").
    5. Keep candidates where date is within window AND ≥1 segment-keyword matches.
    6. Extract company-name candidates: cap-case multi-word phrases ending in
       Inc/LLC/Corp/Corporation/Co/Ltd/AG/S.A./Holdings/Group/Networks/
       Communications/Fiber/Telecom/Cloud/Data Centers/Datacenters/Bank/Financial/
       Health/Healthcare/Hospital/Systems/Services/Solutions/Stores/Industries/
       Distribution (last 11 added 2026-05-14 with Enterprise segment promotion).
    7. Dedup by (link_url, headline_text). Sort.

Exit codes:
    0  success (JSON written to stdout)
    1  argv parse error
    2  file read error
"""
import sys
import json
import re
import html
from datetime import datetime, date

if len(sys.argv) != 5:
    sys.stderr.write("Usage: headline_extract.py <html_file> <segment> <window_start> <window_end>\n")
    sys.exit(1)

HTML_PATH = sys.argv[1]
SEGMENT = sys.argv[2]
WINDOW_START = sys.argv[3]
WINDOW_END = sys.argv[4]

# Per-segment keyword catalog - keep in sync with context/signals/[segment]-signals.md.
KEYWORD_CATALOG = {
    "colocation": [
        "greenfield", "site selection", "permit", "groundbreaking", "lease",
        "anchor tenant", "liquid cooling", "interconnection", "hire", "exec",
        "M&A", "acquired", "PE", "private equity", "MW", "campus", "facility",
        "data center", "data centers", "datacenter", "hyperscale",
    ],
    "fiber": [
        "BEAD", "fiber", "broadband", "IRU", "dark fiber", "lit",
        "M&A", "acquired", "PE", "private equity", "8-K", "ABS", "refinancing",
        "consortium", "JV", "joint venture", "wholesale", "FTTH", "ILEC", "CLEC",
    ],
    "neocloud": [
        "GPU", "AI factory", "convertible notes", "facility", "campus",
        "hyperscaler", "anchor tenant", "PeeringDB", "MLPerf", "lease", "8-K",
        "Lepton", "NCP", "Exemplar", "MW", "training", "inference", "Nvidia",
        "H100", "H200", "B100", "B200", "Rubin", "Blackwell",
    ],
    "network-operator": [
        "PCF", "private connectivity fabric", "earnings", "transcript",
        "CTO", "CNO", "divestiture", "spin-off", "CAMARA", "Nephio",
        "TMF AN", "SRv6", "PCEP", "SR-TE", "CTrO", "CDO", "automation",
        "AI-RAN", "NaaS", "wholesale",
    ],
    "msp-aggregator": [
        "acquisition", "private equity", "carrier", "TSD", "AI practice",
        "CRO", "VP SE", "VP Sales", "ScanSource", "earnings", "channel",
        "agent", "master agent", "TBI", "Telarus", "Avant", "Bridgepointe",
    ],
    # Enterprise (Multi-DC ICP) added 2026-05-11.
    # Signal codes E-A1 through E-A7 plus universal U1/U2/AP-7/FR-1 + sub-segment vertical
    # vocabulary for Financial Services / Healthcare Systems / Retail and Distribution /
    # Outsourcing Services. Anchor account: Meijer.
    "enterprise": [
        # E-A1 New DC build / expansion / major capacity add
        "data center", "DC build", "DC expansion", "capacity add", "MW",
        "groundbreaking", "campus", "facility expansion",
        # E-A2 M&A close (announcement OR close)
        "M&A", "acquired", "merger", "acquisition", "agreement to acquire",
        # E-A3 AI/GPU workload announcement requiring Enterprise GPU connectivity
        "AI", "GPU", "Nvidia", "workload", "training", "inference", "AI factory",
        # E-A4 Network exec hire
        "VP Network", "Director Network", "Principal Network",
        "Network Infrastructure", "Chief Information Officer", "CIO",
        "Chief Security Officer", "CSO", "CISO", "hire", "appoint",
        # E-A5 Regulatory enforcement / new framework effective date
        "NY DFS", "Part 500", "HHS OCR", "PCI DSS", "PCI v4", "DORA", "CTPP",
        "HIPAA", "California AB 749", "breach notification", "regulatory",
        "enforcement action", "consent order",
        # E-A6 Equinix Fabric / Megaport / PacketFabric / Console Connect customer-win
        "Equinix Fabric", "Megaport", "PacketFabric", "Console Connect",
        "customer story", "case study", "customer win",
        # E-A7 SOX 10-K disclosure of network / IT modernization
        "10-K", "modernization", "SOX", "network transformation",
        "infrastructure modernization", "digital transformation",
        # Sub-segment vertical vocabulary - Financial Services
        "bank", "financial services", "insurer", "payment network", "FFIEC",
        # Sub-segment vertical vocabulary - Healthcare Systems
        "hospital", "health system", "healthcare", "Epic", "EHR",
        # Sub-segment vertical vocabulary - Retail and Distribution
        "retailer", "distribution center", "warehouse", "stores",
        "peak readiness", "freeze",
        # Sub-segment vertical vocabulary - Outsourcing Services
        "BPO", "outsourcing", "delivery center", "seat ramp", "Cognizant",
        "Concentrix", "TaskUs", "Webhelp", "Majorel",
    ],
}

DATE_PATTERNS = [
    # ISO: 2026-04-28
    (r"\b(\d{4})-(\d{2})-(\d{2})\b",
     lambda m: date(int(m.group(1)), int(m.group(2)), int(m.group(3)))),
    # US: 04/28/2026
    (r"\b(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/(\d{4})\b",
     lambda m: date(int(m.group(3)), int(m.group(1)), int(m.group(2)))),
    # "April 28, 2026"
    (r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})\b",
     lambda m: date(int(m.group(3)),
                    {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
                     "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}[m.group(1)],
                    int(m.group(2)))),
    # "28 April 2026"
    (r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
     lambda m: date(int(m.group(3)),
                    {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,
                     "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}[m.group(2)],
                    int(m.group(1)))),
]

def parse_date(s):
    for pat, fn in DATE_PATTERNS:
        m = re.search(pat, s)
        if m:
            try:
                return fn(m)
            except (ValueError, KeyError):
                pass
    return None

try:
    ws = datetime.strptime(WINDOW_START, "%Y-%m-%d").date()
    we = datetime.strptime(WINDOW_END, "%Y-%m-%d").date()
except ValueError as e:
    sys.stderr.write(f"Date parse error: {e}\n")
    sys.exit(1)

def in_window(d):
    return d is not None and ws <= d <= we

try:
    with open(HTML_PATH, encoding="utf-8", errors="ignore") as f:
        raw = f.read()
except (OSError, IOError) as e:
    sys.stderr.write(f"Cannot read {HTML_PATH}: {e}\n")
    sys.exit(2)

keywords = KEYWORD_CATALOG.get(SEGMENT, [])
if not keywords:
    sys.stderr.write(f"Unknown segment: {SEGMENT}. Valid: {list(KEYWORD_CATALOG.keys())}\n")
    sys.exit(1)

anchor_re = re.compile(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
company_suffix_re = re.compile(
    r'\b([A-Z][a-zA-Z0-9&.\-]+(?:\s+[A-Z][a-zA-Z0-9&.\-]+){0,4})\s+'
    r'(Inc|LLC|Corp|Corporation|Co|Ltd|AG|S\.A\.|Holdings|Group|Networks|Communications|'
    r'Fiber|Telecom|Cloud|Data\s+Centers?|Datacenters?|'
    r'Bank|Financial|Health|Healthcare|Hospital|Systems|Services|Solutions|'
    r'Stores|Industries|Distribution)\b'
)
tag_strip = re.compile(r'<[^>]+>')

results = []
seen = set()

for m in anchor_re.finditer(raw):
    href = html.unescape(m.group(1))
    text = tag_strip.sub(' ', m.group(2))
    text = html.unescape(text).strip()
    text = re.sub(r'\s+', ' ', text)
    if len(text) < 20 or len(text) > 300:
        continue

    pos = m.start()
    context = raw[max(0, pos - 300): pos + 300]
    d = parse_date(context)
    if not in_window(d):
        continue

    matched_kws = [k for k in keywords if k.lower() in text.lower() or k.lower() in context.lower()]
    if not matched_kws:
        continue

    companies = list({cm.group(0) for cm in company_suffix_re.finditer(text + " " + context)})

    key = (href, text)
    if key in seen:
        continue
    seen.add(key)

    results.append({
        "date": d.isoformat(),
        "headline_text": text,
        "link_url": href,
        "signal_keyword_matched": matched_kws,
        "company_candidates": companies[:5],
    })

results.sort(key=lambda r: (r["date"], len(r["signal_keyword_matched"])), reverse=True)
print(json.dumps(results, indent=2))
