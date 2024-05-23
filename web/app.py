import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, render_template
from nlp.search import search_comments

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    results = search_comments(query)
    return render_template("results.html", query=query, results=results[:5])


if __name__ == "__main__":
    app.run(debug=True)
