from scraper.api import get_posts
from scraper.database import create_database, insert_data
from config import TEAM_ID, CHANNEL_ID

def fetch_and_store():
    create_database()
    data = get_posts(TEAM_ID, CHANNEL_ID)
    insert_data(data)
