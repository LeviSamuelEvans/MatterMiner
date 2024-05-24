import spacy

# larger model with word vectors
nlp = spacy.load('en_core_web_md')

def preprocess_text(text):
    return nlp(text)
