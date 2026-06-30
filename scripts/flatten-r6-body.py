import json
with open(r'c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-update-body.json', 'r', encoding='utf-8') as f:
    body = json.load(f)
with open(r'c:\Users\coopf\OneDrive\Desktop\maiaedge-ai\scripts\r6-update-body-line.json', 'w', encoding='utf-8') as f:
    json.dump(body, f, ensure_ascii=False)
print("Wrote one-line JSON")
