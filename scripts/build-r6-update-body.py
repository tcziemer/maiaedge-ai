"""Build the full update body for trigger R6 (Territory & Hygiene)."""
import json

LIST_PATH = r"C:\Users\coopf\.claude\projects\c--Users-coopf-OneDrive-Desktop-maiaedge-ai\fef313ea-11ab-456c-9509-fea9947fe891\tool-results\toolu_011WbMfaKRKAQueZ8v4xnVFZ.txt"
NEW_PROMPT = r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-new-prompt.json"
OUT_PATH = r"c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-update-body.json"

TRIGGER_ID = "trig_01BmhnoyxFVrNXuqGcNnW6FV"

with open(LIST_PATH, "r", encoding="utf-8") as f:
    text = f.read()
data = json.loads(text[text.find("{"):])
trigger = next(t for t in data["data"] if t["id"] == TRIGGER_ID)

with open(NEW_PROMPT, "r", encoding="utf-8") as f:
    new_content = json.load(f)["new_content"]

trigger["job_config"]["ccr"]["events"][0]["data"]["message"]["content"] = new_content

# Build a minimal update body — only include job_config (the changed field).
update_body = {"job_config": trigger["job_config"]}
with open(OUT_PATH, "w", encoding="utf-8") as f:
    json.dump(update_body, f, ensure_ascii=False)

print(f"Wrote {OUT_PATH}; new content length {len(new_content)}")
