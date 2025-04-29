import os
import json
import sqlite3
from datetime import datetime

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_DIR = os.path.join(BASE_DIR, "memory")
SHORT_TERM_FILE = os.path.join(MEMORY_DIR, "memory_short.json")
LONG_TERM_FILE = os.path.join(MEMORY_DIR, "memory_long.db")

# Garantir que o diretório existe
os.makedirs(MEMORY_DIR, exist_ok=True)

# Memória Curto Prazo (JSON)
class ShortTermMemory:
    def __init__(self):
        if not os.path.exists(SHORT_TERM_FILE):
            self.data = {}
            self._save()
        else:
            with open(SHORT_TERM_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self._save()

    def clear(self):
        self.data = {}
        self._save()

    def _save(self):
        with open(SHORT_TERM_FILE, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

# Memória Longo Prazo (SQLite)
class LongTermMemory:
    def __init__(self):
        self.conn = sqlite3.connect(LONG_TERM_FILE)
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def set(self, key, value):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO memory (key, value)
            VALUES (?, ?)
            ON CONFLICT(key) DO UPDATE SET value=excluded.value
        ''', (key, value))
        self.conn.commit()

    def get(self, key):
        cursor = self.conn.cursor()
        cursor.execute('SELECT value FROM memory WHERE key = ?', (key,))
        row = cursor.fetchone()
        return row[0] if row else None

    def delete(self, key):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM memory WHERE key = ?', (key,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT key, value FROM memory')
        return cursor.fetchall()

    def clear_all(self):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM memory')
        self.conn.commit()

    def close(self):
        self.conn.close()
