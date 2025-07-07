# memory_parser.py

import sys
from pathlib import Path
import requests

# Get the source file path from CLI
src = Path(sys.argv[1])
text = src.read_text(encoding='utf-8')

# Payload (no system prompt needed, LM Studio will use active preset)
payload = {
    "model": "nous-capybara-7b",
    "messages": [
        {
            "role": "user",
            "content": text
        }
    ],
    "temperature": 0.3,
    "max_tokens": 1024
}

# POST request to local LM Studio
response = requests.post("http://127.0.0.1:1234/v1/chat/completions", json=payload)
data = response.json()["choices"][0]["message"]["content"].strip()

# Output paths
json_file = src.with_suffix('.parsed.json')
md_file = src.with_name(f"{src.stem}.parsed.md")

# Write output
json_file.write_text(data, encoding='utf-8')
md_file.write_text(f"```json\n{data}\n```", encoding='utf-8')

# Unicode-safe print (Windows-safe)
print(f"Parsed {src.name} -> {json_file.name} & {md_file.name}")
