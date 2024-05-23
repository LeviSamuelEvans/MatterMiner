import pytest
from nlp.search import search_comments

def test_search_comments():
    results = search_comments("test query")
    assert len(results) > 0
