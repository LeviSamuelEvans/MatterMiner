from flask import Flask, request, render_template
from nlp.search import search_posts

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_posts(query)
    return render_template('results.html', query=query, results=results[:5])
