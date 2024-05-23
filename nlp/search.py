import sqlite3
from nlp.preprocess import preprocess_text
from config import DATABASE

def search_posts(query):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT message FROM posts")
    posts = c.fetchall()
    conn.close()

    query_doc = preprocess_text(query)

    results = []
    for post in posts:
        post_doc = preprocess_text(post[0])
        similarity = query_doc.similarity(post_doc)
        results.append((post[0], similarity))

    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results
