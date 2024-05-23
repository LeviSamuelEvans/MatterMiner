# RedditMiner

RedditMiner is a tool for crawling and analysing comments from Reddit subreddits. It uses the Reddit API to fetch comments, stores them in an SQLite database, and provides a web interface for querying and analysing the data using natural language processing (NLP).

## Features

- Crawl comments from any specified subreddit
- Store comments in an SQLite database
- Perform NLP on comments for similarity search
- Simple web interface for querying and displaying results

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LeviSamuelEvans/RedditMiner
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
```

Replace your_client_id, your_client_secret, and your_user_agent with your Reddit API credentials.

## Usage

### Crawling comments
To crawl comments from a specified subreddit and store them in the database, run:

```python

python main.py subreddit_name --limit 100


```
Replace subreddit_name with the name of the subreddit you want to crawl and --limit with the number of comments to fetch (default is 100).

### Running a web interface

To start the web interface, run:

```
python web/app.py

```

Open your browser and navigate to http://127.0.0.1:5000/ to use the interface.