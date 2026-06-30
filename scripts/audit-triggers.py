import json
import sys

PATH = r"C:\Users\coopf\.claude\projects\c--Users-coopf-OneDrive-Desktop-maiaedge-ai\fef313ea-11ab-456c-9509-fea9947fe891\tool-results\toolu_011WbMfaKRKAQueZ8v4xnVFZ.txt"

with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()
start = text.find("{")
data = json.loads(text[start:])

ids_of_interest = {
    "trig_01XTjFhegfVTCtSpZXEDY5Ce",
    "trig_01Rw3KUsEXj2eoKKRKRCgGCZ",
    "trig_01BmhnoyxFVrNXuqGcNnW6FV",
    "trig_01WyVys2Jpi88JsoU5Pa4qve",
    "trig_011jpGwhJQS8dJY3i7qU1StA",
    "trig_01Uw6RXKwGbjZfS2WaPeudKw",
}

needles = [
    "Enterprise (legacy",
    "Enterprise (MSP",
    "legacy naming",
    "Dark Fiber - Commercial Enterprise",
    "MSP/Aggregator gotcha",
    "is `Enterprise`",
    "= `Enterprise`",
    "= \"Enterprise\"",
    "value `Enterprise`",
    "internal value is `Enterprise`",
    "value Enterprise",
]

for t in data["data"]:
    if t["id"] not in ids_of_interest:
        continue
    name = t.get("name") or "(no name)"
    content = t["job_config"]["ccr"]["events"][0]["data"]["message"]["content"]
    flags = [n for n in needles if n in content]
    print(f"{t['id']} | len={len(content)} | flags={flags}")
    print(f"  name: {name}")
    if flags:
        for n in flags:
            idx = content.find(n)
            snippet = content[max(0, idx-80):idx+len(n)+80].replace("\n", " ")
            print(f"  >>> {n!r}: ...{snippet}...")
    print()
