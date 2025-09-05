import sqlite3

DB_FILE = "snippets.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def create_tables():
    conn = get_connection()
    c = conn.cursor()
    # Snippets table
    c.execute("""
    CREATE TABLE IF NOT EXISTS snippets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        code TEXT NOT NULL,
        language TEXT,
        category TEXT
    )""")
    # Tags table
    c.execute("""
    CREATE TABLE IF NOT EXISTS tags (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        snippet_id INTEGER,
        tag TEXT,
        FOREIGN KEY(snippet_id) REFERENCES snippets(id)
    )""")
    conn.commit()
    conn.close()
