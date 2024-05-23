import sqlite3
from config import DATABASE


def create_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS comments
                 (id TEXT PRIMARY KEY, body TEXT, author TEXT, created_utc REAL)"""
    )
    conn.commit()
    conn.close()


def insert_data(comments):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    for comment in comments:
        c.execute(
            "INSERT OR REPLACE INTO comments (id, body, author, created_utc) VALUES (?, ?, ?, ?)",
            (comment["id"], comment["body"], comment["author"], comment["created_utc"]),
        )
    conn.commit()
    conn.close()
