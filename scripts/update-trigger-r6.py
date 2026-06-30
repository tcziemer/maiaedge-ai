"""Build the update body for R6 (Territory & Hygiene) — replace the stale
`customer_segment = "Enterprise"` gotcha with the post-rename equivalent.
Outputs the new prompt content to stdout for the RemoteTrigger update call."""

import json

PATH = r"C:\Users\coopf\.claude\projects\c--Users-coopf-OneDrive-Desktop-maiaedge-ai\fef313ea-11ab-456c-9509-fea9947fe891\tool-results\toolu_011WbMfaKRKAQueZ8v4xnVFZ.txt"

TRIGGER_ID = "trig_01BmhnoyxFVrNXuqGcNnW6FV"

OLD = '`customer_segment = "Enterprise"` is MSP/Aggregator (legacy). Do not "fix" it.'
NEW = '`customer_segment = "MSP/Aggregator"` is the ICP MSP/Aggregator value (renamed from the deleted `Enterprise` on 2026-05-07). Real enterprise consumers use `Enterprise-CustomerSegment` (non-ICP).'

with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()
data = json.loads(text[text.find("{"):])

for t in data["data"]:
    if t["id"] != TRIGGER_ID:
        continue
    content = t["job_config"]["ccr"]["events"][0]["data"]["message"]["content"]
    if OLD not in content:
        print("STALE STRING NOT FOUND in R6 prompt — abort")
        raise SystemExit(1)
    new_content = content.replace(OLD, NEW)
    out = {
        "before_len": len(content),
        "after_len": len(new_content),
        "occurrences_replaced": content.count(OLD),
        "new_content": new_content,
    }
    with open(r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-new-prompt.json", "w", encoding="utf-8") as out_f:
        json.dump(out, out_f, ensure_ascii=False, indent=2)
    print(f"before={out['before_len']} after={out['after_len']} replaced={out['occurrences_replaced']}")
    print("Wrote new content to scripts/r6-new-prompt.json")
    break
else:
    print("Trigger not found")
    raise SystemExit(1)
