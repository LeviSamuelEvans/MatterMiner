import sqlite3
from config import DATABASE

def create_database():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS posts
                 (id TEXT PRIMARY KEY, message TEXT, user_id TEXT, channel_id TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    for post_id, post_data in data['posts'].items():
        c.execute("INSERT OR REPLACE INTO posts (id, message, user_id, channel_id, timestamp) VALUES (?, ?, ?, ?, ?)",
                  (post_id, post_data['message'], post_data['user_id'], post_data['channel_id'], post_data['create_at']))
    conn.commit()
    conn.close()
