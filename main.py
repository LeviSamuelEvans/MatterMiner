import argparse
from scraper.fetch_data import fetch_and_store


def main():
    """
    Crawl a subreddit and store comments.

    Parameters
    ----------
        subreddit : str
            The name of the subreddit to crawl.
        limit : int, optional
            The number of comments to fetch. Defaults to 100.
    """
    parser = argparse.ArgumentParser(
        description="Crawl a subreddit and store comments."
    )
    parser.add_argument(
        "subreddit", type=str, help="The name of the subreddit to crawl"
        "E.g, input MachineLearning for r/MachineLearning."
    )
    parser.add_argument(
        "--limit", type=int, default=1000, help="The number of comments to fetch"
    )
    args = parser.parse_args()

    fetch_and_store(subreddit_name=args.subreddit, limit=args.limit)
    print("Data fetched and stored successfully.")


if __name__ == "__main__":
    main()
