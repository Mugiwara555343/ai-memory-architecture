#!/usr/bin/env python3
"""
memory_parser.py (Standalone Demo Version)

Parses markdown logs into JSON with a strict schema:
- YAML frontmatter: title, tags
- Inline metadata: Date, Tags, Tone
- Summary and Reflections blocks
"""

import json
from pathlib import Path
from datetime import datetime
from jsonschema import validate, ValidationError

# === CONFIG ===
MEMORY_DIR = Path(__file__).parent
OUTPUT_DIR = MEMORY_DIR

# === SCHEMA ===
SCHEMA = {
    "type": "object",
    "required": ["title", "timestamp", "raw_text", "plain_text"],
    "properties": {
        "title":       {"type": "string"},
        "timestamp":   {"type": "string", "format": "date-time"},
        "raw_text":    {"type": "string"},
        "plain_text":  {"type": "string"},
        "tags":        {"type": "array", "items": {"type": "string"}},
        "headers":     {"type": "array", "items": {"type": "string"}},
        "date":        {"type": "string"},
        "tone":        {"type": "string"},
        "summary":     {"type": "string"},
        "reflections": {"type": "array", "items": {"type": "string"}},
    },
    "additionalProperties": False
}


def validate_parsed(data: dict):
    validate(instance=data, schema=SCHEMA)


def parse_md_file(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    raw_text   = text.strip()
    plain_text = raw_text.replace("\n", " ")
    title      = md_path.stem
    tags, headers, reflections = [], [], []
    date_str, tone_str, summary_text = None, None, None
    in_summary = in_reflect = False

    for line in lines:
        if line.startswith("# "):
            h = line.lstrip("# ").strip()
            headers.append(h)
            if title == md_path.stem:
                title = h

        if line.startswith("**Date:**"):
            date_str = line.split("**Date:**", 1)[1].strip()
        if line.startswith("**Tags:**"):
            vals = line.split("**Tags:**", 1)[1].strip()
            tags = [t.strip().lstrip("#") for t in vals.split() if t.startswith("#")]
        if line.startswith("**Tone:**"):
            tone_str = line.split("**Tone:**", 1)[1].strip()

        if line.lower().startswith("**summary:**"):
            in_summary = True
            summary_text = ""
            continue
        if in_summary:
            if line.strip() == "" or line.strip().startswith("---"):
                in_summary = False
            else:
                summary_text += line.strip() + " "

        if line.lower().startswith("**core reflections:**"):
            in_reflect = True
            continue
        if in_reflect:
            if not line.startswith("-"):
                in_reflect = False
            else:
                reflections.append(line.lstrip("- ").strip())

    if date_str:
        try:
            dt = datetime.fromisoformat(date_str)
            timestamp = dt.isoformat() + "Z"
        except:
            timestamp = datetime.utcnow().isoformat() + "Z"
    else:
        timestamp = datetime.utcnow().isoformat() + "Z"

    parsed = {
        "title":       title,
        "timestamp":   timestamp,
        "raw_text":    raw_text,
        "plain_text":  plain_text,
        "tags":        tags,
        "headers":     headers,
        "date":        date_str,
        "tone":        tone_str,
        "summary":     summary_text.strip() if summary_text else None,
        "reflections": reflections,
    }

    parsed = {k: v for k, v in parsed.items() if v is not None}
    validate_parsed(parsed)
    return parsed


# === MAIN ===
if __name__ == "__main__":
    for md in MEMORY_DIR.glob("*.md"):
        out = OUTPUT_DIR / f"{md.stem}.parsed.json"
        try:
            data = parse_md_file(md)
            out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"[OK] Parsed: {md.name} → {out.name}")
        except ValidationError as ve:
            print(f"[SCHEMA ERR] {md.name}: {ve.message}")
        except Exception as e:
            print(f"[FAIL] {md.name}: {e}")
