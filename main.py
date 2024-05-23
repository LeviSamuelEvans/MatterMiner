from scraper.fetch_data import fetch_and_store

if __name__ == "__main__":
    # Fetch data from a subreddit
    fetch_and_store(subreddit_name="python", limit=100)
    print("Data fetched and stored successfully.")
