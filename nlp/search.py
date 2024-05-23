import sqlite3
from nlp.preprocess import preprocess_text
from config import DATABASE

def search_comments(query):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT body FROM comments")
    comments = c.fetchall()
    conn.close()

    query_doc = preprocess_text(query)

    results = []
    for comment in comments:
        comment_doc = preprocess_text(comment[0])
        similarity = query_doc.similarity(comment_doc)
        results.append((comment[0], similarity))

    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results

# Path: nlp/preprocess.py
