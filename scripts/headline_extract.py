#!/usr/bin/env python3
"""
Extract candidate headlines from a saved web_fetch HTML response.

Usage:
    python3 headline_extract.py <html_file> <segment> <window_start> <window_end> [--keywords k1,k2,...]

Output (stdout):
    JSON array of {date, headline_text, link_url, signal_keyword_matched, company_candidates[]}.

Strategy (no LLM, deterministic):
    1. Parse HTML with BeautifulSoup, fall back to regex if html5lib unavailable.
    2. Pull <a> tags inside common article containers (article, .post, .article, [class*=story], [class*=headline]).
    3. For each candidate: extract anchor text + nearest visible date string within +/-200 chars.
    4. Date parsing: try ISO (YYYY-MM-DD), US (MM/DD/YYYY), "April 28, 2026", "28 April 2026", "2026-04-28T..." -- discard anything not parseable.
    5. Keep candidates where parsed date is within window.
    6. Score keyword match: case-insensitive substring search over anchor text + 100-char trailing context.
    7. Pull company-name candidates: cap-case multi-word noun phrases of length 1-4 ending in Inc/LLC/Corp/Ltd/AG/S.A./Holdings/Group/Networks/Communications/Fiber/Telecom/Cloud/Data Centers OR matching a known target-domain root.
    8. Return JSON array, sorted by score descending.
"""
import sys, json, re, html
from datetime import datetime, date

WINDOW_START = sys.argv[3]
WINDOW_END = sys.argv[4]
SEGMENT = sys.argv[2]
HTML_PATH = sys.argv[1]

# Per-segment keyword catalog -- keep in sync with context/signals/[segment]-signals.md
KEYWORD_CATALOG = {
    "colocation": ["greenfield", "site selection", "permit", "groundbreaking", "lease", "anchor tenant", "liquid cooling", "interconnection", "exec", "hire", "M&A", "acquired", "PE", "private equity", "MW", "campus", "facility"],
    "fiber": ["BEAD", "fiber", "broadband", "IRU", "dark fiber", "lit", "M&A", "acquired", "PE", "private equity", "8-K", "ABS", "refinancing", "consortium", "JV", "joint venture", "wholesale"],
    "neocloud": ["GPU", "AI factory", "convertible notes", "facility", "campus", "hyperscaler", "anchor tenant", "PeeringDB", "MLPerf", "lease", "8-K", "Lepton", "NCP", "Exemplar", "MW"],
    "network-operator": ["PCF", "private connectivity fabric", "earnings", "transcript", "CTO", "CNO", "divestiture", "spin-off", "CAMARA", "Nephio", "TMF AN", "SRv6", "PCEP", "SR-TE", "CTrO", "CDO"],
    "msp-aggregator": ["acquisition", "private equity", "carrier", "TSD", "AI practice", "CRO", "VP SE", "ScanSource", "earnings", "channel"],
}

DATE_PATTERNS = [
    (r"\b(\d{4})-(\d{2})-(\d{2})\b", lambda m: date(int(m[1]), int(m[2]), int(m[3]))),
    (r"\b(0?[1-9]|1[0-2])/(0?[1-9]|[12]\d|3[01])/(\d{4})\b", lambda m: date(int(m[3]), int(m[1]), int(m[2]))),
    (r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})\b",
     lambda m: date(int(m[3]), {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}[m[1]], int(m[2]))),
    (r"\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b",
     lambda m: date(int(m[3]), {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}[m[2]], int(m[1]))),
]

def parse_date(s):
    for pat, fn in DATE_PATTERNS:
        m = re.search(pat, s)
        if m:
            try: return fn(m)
            except: pass
    return None

def in_window(d):
    if not d: return False
    ws = datetime.strptime(WINDOW_START, "%Y-%m-%d").date()
    we = datetime.strptime(WINDOW_END, "%Y-%m-%d").date()
    return ws <= d <= we

# Read HTML
with open(HTML_PATH, encoding="utf-8", errors="ignore") as f:
    raw = f.read()

# Find anchor blocks
anchor_re = re.compile(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
results = []
keywords = KEYWORD_CATALOG.get(SEGMENT, [])

for m in anchor_re.finditer(raw):
    href = html.unescape(m.group(1))
    text = re.sub(r'<[^>]+>', ' ', m.group(2))
    text = html.unescape(text).strip()
    if len(text) < 20 or len(text) > 300: continue

    # Search +/-300 chars around the anchor for date
    pos = m.start()
    context = raw[max(0, pos-300): pos+300]
    d = parse_date(context)
    if not in_window(d): continue

    # Keyword match
    matched_kws = [k for k in keywords if k.lower() in text.lower() or k.lower() in context.lower()]
    if not matched_kws: continue

    # Company candidates: capitalized multi-word phrases ending in known suffixes
    company_re = re.compile(r'\b([A-Z][a-zA-Z0-9&.\-]+(?:\s+[A-Z][a-zA-Z0-9&.\-]+){0,4})\s+(Inc|LLC|Corp|Ltd|AG|S\.A\.|Holdings|Group|Networks|Communications|Fiber|Telecom|Cloud|Data\s+Centers?|Datacenters?)\b')
    companies = list({mm.group(0) for mm in company_re.finditer(text + " " + context)})

    results.append({
        "date": d.isoformat(),
        "headline_text": text,
        "link_url": href,
        "signal_keyword_matched": matched_kws,
        "company_candidates": companies[:5],
    })

# Dedup by (link_url, headline_text); sort by date descending then keyword count
seen = set()
deduped = []
for r in results:
    key = (r["link_url"], r["headline_text"])
    if key in seen: continue
    seen.add(key)
    deduped.append(r)
deduped.sort(key=lambda r: (r["date"], len(r["signal_keyword_matched"])), reverse=True)

print(json.dumps(deduped, indent=2))
