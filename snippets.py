from db import get_connection
from rapidfuzz import process
import json

def add_snippet(snippet):
    conn = get_connection()
    cursor = conn.cursor()
    # Insert snippet (without tags)
    cursor.execute("""
        INSERT INTO snippets (title, description, code, language, category)
        VALUES (?, ?, ?, ?, ?)
    """, (snippet['title'], snippet['description'], snippet['code'],
          snippet['language'], snippet['category']))
    snippet_id = cursor.lastrowid
    # Insert tags
    for tag in snippet.get('tags', []):
        if tag.strip():
            cursor.execute("INSERT INTO tags (snippet_id, tag) VALUES (?, ?)", (snippet_id, tag.strip()))
    conn.commit()
    conn.close()

def list_snippets():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, code, language, category FROM snippets")
    rows = cursor.fetchall()
    for row in rows:
        snippet_id, title, description, code, language, category = row
        # Fetch tags
        cursor.execute("SELECT tag FROM tags WHERE snippet_id = ?", (snippet_id,))
        tags = [t[0] for t in cursor.fetchall()]
        print(f"Title: {title}\nDescription: {description}\nLanguage: {language}\nCategory: {category}\nTags: {', '.join(tags) if tags else 'None'}\nCode:\n{code}\n{'-'*40}")
    conn.close()

def search_snippets(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, code FROM snippets")
    rows = cursor.fetchall()
    snippet_texts = [r[1] for r in rows]
    matches = process.extract(query, snippet_texts, limit=10, score_cutoff=50)
    if not matches:
        print("No matching snippets found.")
        return
    for match_text, score, idx in matches:
        snippet_id = rows[idx][0]
        cursor.execute("SELECT title, description, language, category FROM snippets WHERE id = ?", (snippet_id,))
        snippet_data = cursor.fetchone()
        title, description, language, category = snippet_data
        cursor.execute("SELECT tag FROM tags WHERE snippet_id = ?", (snippet_id,))
        tags = [t[0] for t in cursor.fetchall()]
        print(f"Title: {title}\nDescription: {description}\nLanguage: {language}\nCategory: {category}\nTags: {', '.join(tags) if tags else 'None'}\nCode:\n{match_text}\n{'-'*40}")
    conn.close()

def export_snippets_to_json(file_path="snippets_export.json"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, code, language, category FROM snippets")
    snippets = cursor.fetchall()
    result = []
    for sn in snippets:
        cursor.execute("SELECT tag FROM tags WHERE snippet_id=?", (sn[0],))
        tags = [t[0] for t in cursor.fetchall()]
        result.append({
            "title": sn[1],
            "description": sn[2],
            "code": sn[3],
            "language": sn[4],
            "category": sn[5],
            "tags": tags
        })
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)
    conn.close()
    print(f"✅ Exported {len(result)} snippets to {file_path}")

def import_snippets_from_json(file_path="snippets_export.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for snippet in data:
        add_snippet(snippet)
    print(f"✅ Imported {len(data)} snippets from {file_path}")