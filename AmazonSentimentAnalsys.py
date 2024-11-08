
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

import textwrap
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define a function to analyze sentiment
def get_sentiment(review_text):
    scores = sid.polarity_scores(review_text)
    compound_score = scores['compound']
    if compound_score >= 0.05:
        return compound_score,'positive'
    elif compound_score <= -0.05:
        return compound_score,'negative'
    else:
        return compound_score, 'neutral'
