import requests
import json
from textblob import TextBlob

def get_article_titles(q):
    url_key = "58285a2ce5d3d51746d30bd5cd5dbe92"
    url = "https://gnews.io/api/v3/search?"
    response = requests.get(url, {'q': q, 'token': url_key})
    content = response.json()
    titles = []
    for i in range(0, 10):
        titles.append(content['articles'][i]['title'])
    return titles

def perform_sentiment_analysis(q):
    titles = get_article_titles(q)
    polarity = 0
    subj = 0
    for i in range(0, 10):
        polarity += TextBlob(titles[i]).sentiment.polarity
        subj += TextBlob(titles[i]).sentiment.subjectivity
    subj = subj / 10
    print(polarity)
    subjectivity = "ERROR"
    opinion = "ERROR"
    if (-.1 < polarity < 0) or (.1 > polarity > 0):
        opinion = "neutral"
    if -.3 < polarity < -.1:
        opinion = "slightly negative"
    if -.7 < polarity <= -.3:
        opinion = "negative"
    if polarity <= -.7:
        opinion = "extremely negative"
    if .3 > polarity > .1:
        opinion = "slightly positive"
    if .7 > polarity >= .3:
        opinion = "positive"
    if polarity >= .7:
        opinion = "extremely positive"

    if subj < .1:
        subjectivity = "very objective"
    if subj < .4:
        subjectivity = "slightly objective"
    if subj < .7:
        subjectivity = "subjective"
    if subj > .7:
        subjectivity = "very subjective"
    return [opinion, subjectivity]

print()