#!/usr/bin/env python3
"""
Source coverage gate. Pass = >=80% of documented source URLs attempted per segment.

Usage:
    python3 check_source_coverage_gate.py <sources_attempted.json>

Exits 0 with JSON pass/fail report on stdout. Exits 1 only on file-read errors.
"""
import sys
import json

LOG = json.load(open(sys.argv[1]))
THRESHOLD = 0.80

# Documented source totals counted from context/signals/<segment>-signals.md
# "Sources for This Segment" sub-sections (Robust + Medium + Aspirational tiers).
# Recounted 2026-05-05; re-count whenever source lists change.
DOCUMENTED = {
    "colocation": 23,
    "fiber": 26,
    "neocloud": 29,
    "network-operator": 27,
    "msp-aggregator": 25,
}

report = {"per_segment": {}, "overall_pass": True, "missing_sources": {}}

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
        report["missing_sources"][seg] = (
            "see context/signals/" + seg + "-signals.md Sources sub-section "
            "minus attempted_urls"
        )

print(json.dumps(report, indent=2))
