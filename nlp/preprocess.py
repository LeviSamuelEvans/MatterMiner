import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load('en_core_web_md')
sentiment_analyzer = SentimentIntensityAnalyzer()

def preprocess_text(text):
    return nlp(text)

def analyze_sentiment(text):
    return sentiment_analyzer.polarity_scores(text)
