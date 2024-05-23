import pytest
import sqlite3
from scraper.database import create_database, insert_data

def test_create_database():
    create_database()
    conn = sqlite3.connect('reddit.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='comments';")
    assert c.fetchone() is not None
    conn.close()

def test_insert_data():
    create_database()
    comments = [
        {"id": "1", "body": "Test comment", "author": "user1", "created_utc": 1625164800}
    ]
    insert_data(comments)
    conn = sqlite3.connect('reddit.db')
    c = conn.cursor()
    c.execute("SELECT * FROM comments WHERE id='1';")
    assert c.fetchone() is not None
    conn.close()
