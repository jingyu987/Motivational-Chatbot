from textblob import TextBlob
from typing import List

def generate_response(user_input: str) -> str:
    pass









def get_sentiment(blob: TextBlob) -> tuple[int, int]:
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity

def extract(blob: TextBlob) -> List[str]:
    return blob.noun_phrases

