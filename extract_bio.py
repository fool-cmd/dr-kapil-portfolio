import json
try:
    with open(r'C:\Users\PREDATOR\.gemini\antigravity\brain\16ea2a36-0830-48f6-8c39-f7397675e133\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            if data.get('type') == 'USER_INPUT' and 'content' in data:
                if 'The read more should include this' in data['content'] or 'Who is Dr. Kapil Rijal?' in data['content']:
                    with open('full_user_prompt.txt', 'w', encoding='utf-8') as out:
                        out.write(data['content'])
                    print("Found and saved!")
                    break
except Exception as e:
    print("Error:", e)
