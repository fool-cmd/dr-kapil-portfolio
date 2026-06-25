import json
try:
    with open('extracted.txt', 'r', encoding='utf-8-sig') as f:
        line = f.read().strip()
    if line:
        data = json.loads(line)
        with open('extracted_bio.md', 'w', encoding='utf-8') as out:
            out.write(data['content'])
except Exception as e:
    print("Error:", e)
