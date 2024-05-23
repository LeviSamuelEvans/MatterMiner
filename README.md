# RedditMiner

RedditMiner is a tool for crawling and analyzing comments from Reddit subreddits. It uses the Reddit API to fetch comments, stores them in an SQLite database, and provides a web interface for querying and analyzing the data using natural language processing (NLP).

## Features

- Crawl comments from any specified subreddit
- Store comments in an SQLite database
- Perform NLP on comments for similarity search
- Simple web interface for querying and displaying results

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/RedditMiner.git
    cd RedditMiner
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the SpaCy model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Configuration

Create a `config.py` file in the root directory of the project with the following content:

```python
# Configuration variables

REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USER_AGENT = "your_user_agent"
DATABASE = "reddit.db"
