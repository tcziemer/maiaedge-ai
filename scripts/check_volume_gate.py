#!/usr/bin/env python3
"""
Volume-per-rep gate. Pass = each rep's final pool >= 25 OR carryover_pool documented as exhausted.

Usage:
    python3 check_volume_gate.py <scored.json>

Output: JSON pass/fail report. Exit 0 always; the runtime decides what to do based on the report.
"""
import sys, json
from collections import defaultdict

d = json.load(open(sys.argv[1]))
scored = d["scored"]
carryover_meta = d.get("carryover_pool_meta", {})  # rep -> {pool_size, exhausted: bool}

FLOOR = 25
report = {"per_rep": {}, "overall_pass": True, "holds": []}
counts = defaultdict(int)
for r in scored:
    counts[r["owner"]] += 1

for rep in ("lieto", "cunningham", "ziemer"):
    pool = counts.get(rep, 0)
    co_meta = carryover_meta.get(rep, {})
    co_pool_size = co_meta.get("pool_size", 0)
    co_exhausted = co_meta.get("exhausted", False)

    if pool >= FLOOR:
        rep_pass = True
        action = "post"
    elif co_exhausted:
        rep_pass = True
        action = "post_with_yellow_tag"
    else:
        rep_pass = False
        action = "hold_dm_post_under_coverage_alert"
        report["holds"].append(rep)
        report["overall_pass"] = False

    report["per_rep"][rep] = {
        "pool_size": pool,
        "carryover_pool_size": co_pool_size,
        "carryover_exhausted": co_exhausted,
        "pass": rep_pass,
        "action": action,
    }

print(json.dumps(report, indent=2))
