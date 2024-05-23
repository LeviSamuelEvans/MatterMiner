from scraper.api import get_comments
from scraper.database import create_database, insert_data

def fetch_and_store(subreddit_name, limit=100):
    create_database()
    comments = get_comments(subreddit_name, limit)
    insert_data(comments)
