import pytest
from scraper.api import get_reddit_instance

def test_get_reddit_instance():
    reddit = get_reddit_instance()
    assert reddit is not None
    assert reddit.read_only == True  # ensure the instance is read-only!
