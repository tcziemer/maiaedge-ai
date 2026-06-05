#!/usr/bin/env python3
"""
Source coverage gate. Pass = >=80% of documented source URLs attempted per segment.

Usage:
    python3 check_source_coverage_gate.py <sources_attempted.json>

Input file format (sources_attempted.json):
{
  "colocation": [
    {"source_url": "...", "attempted_at": "...", "http_status": 200, "hits_count": 3, "status": "success"},
    {"source_url": "...", "attempted_at": "...", "http_status": 404, "hits_count": 0, "status": "4xx"}
  ],
  "fiber": [...],
  ...
}

Status values:
    "success"  -> source returned data (counts toward coverage)
    "empty"    -> source returned 200 but 0 in-window hits (counts toward coverage)
    "4xx"      -> client error (does NOT count)
    "5xx"      -> server error (does NOT count)
    "timeout"  -> timeout after retries (does NOT count)

Output (stdout): JSON pass/fail report with per-segment breakdown.

Exit codes:
    0  always (this script reports, does not throw)
    1  file-read error
"""
import sys
import json

if len(sys.argv) != 2:
    sys.stderr.write("Usage: check_source_coverage_gate.py <sources_attempted.json>\n")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        LOG = json.load(f)
except (OSError, IOError, json.JSONDecodeError) as e:
    sys.stderr.write(f"Cannot read {sys.argv[1]}: {e}\n")
    sys.exit(1)

THRESHOLD = 0.80

# Documented source totals per segment.
# Re-count from `context/signals/<segment>-signals.md` "Sources for This Segment"
# whenever the source lists are edited. Keep this dict authoritative for the gate.
#
# Last updated 2026-05-11 after catalog pruning (cut: county permits, state PUC dockets,
# ISO queues, Reddit, Wayback diffs, Glassdoor scrape, Indeed scrape, YouTube transcripts,
# TheOrg diffs, Public Slack channels, local business journals, state EDC press, PeeringDB
# as news source, MLPerf weekly, AnandTech, Reuters telco). Added: StockTitan (SEC mirror)
# across all 5 segments; crypto-to-AI outlets (CoinDesk, Bitcoin Magazine, Cryptopolitan,
# news.bitcoin.com) promoted to NeoCloud Robust; explicit Motley Fool + MarketBeat in
# earnings transcript entries (Fiber + Network Operator).
DOCUMENTED = {
    "colocation": 16,
    "fiber": 22,
    "neocloud": 24,
    "network-operator": 22,
    "msp-aggregator": 20,
    "enterprise": 33,
}

report = {
    "threshold": THRESHOLD,
    "per_segment": {},
    "overall_pass": True,
    "missing_sources_hint": {},
}

for seg, total in DOCUMENTED.items():
    rows = LOG.get(seg, [])
    attempted = sum(1 for r in rows if r.get("status") in ("success", "empty"))
    failed = sum(1 for r in rows if r.get("status") in ("4xx", "5xx", "timeout", "error"))
    coverage = attempted / total if total else 0
    seg_pass = coverage >= THRESHOLD

    report["per_segment"][seg] = {
        "attempted": attempted,
        "failed": failed,
        "total_documented": total,
        "coverage_pct": round(coverage * 100, 1),
        "pass": seg_pass,
    }

    if not seg_pass:
        report["overall_pass"] = False
        attempted_urls = sorted({r.get("source_url", "") for r in rows})
        report["missing_sources_hint"][seg] = (
            f"context/signals/{seg}-signals.md 'Sources for This Segment' "
            f"sub-section minus the {len(attempted_urls)} URLs already attempted"
        )

print(json.dumps(report, indent=2))
