import sqlite3
import json
import os
from datetime import datetime
from config import load_config

DB_PATH = load_config().get('DB_PATH', 'smartdocs.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id TEXT,
        ext TEXT,
        task TEXT,
        result_type TEXT,
        result_json TEXT,
        created_at TEXT
    )''')
    conn.commit()
    conn.close()

def cache_result(doc_id, ext, task, result_type, result):
    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO results (doc_id, ext, task, result_type, result_json, created_at)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (doc_id, ext, task, result_type, json.dumps(result), datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def get_cached_result(doc_id, ext, task, result_type):
    conn = get_db()
    c = conn.cursor()
    c.execute('''SELECT result_json FROM results WHERE doc_id=? AND ext=? AND task=? AND result_type=? ORDER BY created_at DESC LIMIT 1''',
              (doc_id, ext, task, result_type))
    row = c.fetchone()
    conn.close()
    if row:
        return json.loads(row['result_json'])
    return None 