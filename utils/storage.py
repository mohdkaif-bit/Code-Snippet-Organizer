import json
from pathlib import Path

SNIPPETS_FILE = Path("snippets.json")

def load_snippets():
    if SNIPPETS_FILE.exists():
        with open(SNIPPETS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_snippets(snippets):
    with open(SNIPPETS_FILE, "w", encoding="utf-8") as f:
        json.dump(snippets, f, indent=2)
