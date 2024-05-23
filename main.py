from scraper import fetch_data
from nlp import search
from web import app

if __name__ == "__main__":
    # Fetch data from Mattermost
    fetch_data.fetch_and_store()

    # Start the web application
    app.run()
