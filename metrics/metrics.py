import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from nlp.preprocess import analyze_sentiment

DATABASE = "reddit.db"

def get_total_comments():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM comments")
    total_comments = c.fetchone()[0]
    conn.close()
    return total_comments

def get_unique_authors():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT COUNT(DISTINCT author) FROM comments")
    unique_authors = c.fetchone()[0]
    conn.close()
    return unique_authors

def get_most_active_authors(limit=5):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT author, COUNT(*) as count FROM comments GROUP BY author ORDER BY count DESC LIMIT ?", (limit,))
    most_active_authors = c.fetchall()
    conn.close()
    return most_active_authors

def get_average_comment_length():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT AVG(LENGTH(body)) FROM comments")
    avg_length = c.fetchone()[0]
    conn.close()
    return avg_length

def get_comments_over_time():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT created_utc FROM comments")
    timestamps = [datetime.utcfromtimestamp(row[0]) for row in c.fetchall()]
    conn.close()
    return timestamps

def get_sentiment_distribution():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT body FROM comments")
    comments = [row[0] for row in c.fetchall()]
    conn.close()

    sentiments = [analyze_sentiment(comment)['compound'] for comment in comments]
    return sentiments

def plot_comments_over_time():
    timestamps = get_comments_over_time()
    dates = [ts.date() for ts in timestamps]
    dates.sort()

    plt.hist(dates, bins=50)
    plt.xlabel('Date')
    plt.ylabel('Number of Comments')
    plt.title('Comments Over Time')
    plt.savefig('comments_over_time.png')

def print_metrics():
    print("Data Metrics")
    print("============")
    print(f"Total number of comments: {get_total_comments()}")
    print(f"Number of unique authors: {get_unique_authors()}")

    print("\nMost active authors:")
    for author, count in get_most_active_authors():
        print(f"{author}: {count} comments")

    print(f"\nAverage length of comments: {get_average_comment_length():.2f} characters")

if __name__ == "__main__":
    print_metrics()
    #plot_comments_over_time()
