import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def get_reddit_instance():
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                         client_secret=REDDIT_CLIENT_SECRET,
                         user_agent=REDDIT_USER_AGENT)
    return reddit

def get_comments(subreddit_name, limit=100):
    reddit = get_reddit_instance()
    subreddit = reddit.subreddit(subreddit_name)
    comments = []
    for comment in subreddit.comments(limit=limit):
        comments.append({
            "id": comment.id,
            "body": comment.body,
            "author": str(comment.author),
            "created_utc": comment.created_utc
        })
    return comments
# Path: scraper/fetch_data.py