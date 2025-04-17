# model/train_model.py

import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load Flipkart dataset
dataset = load_dataset("ml-hub/flipkart-reviews-dataset")
df = dataset["train"].to_pandas()

# Rename and map sentiment
df = df.rename(columns={'review_text': 'text', 'review_rating': 'label'})

def map_rating_to_sentiment(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

df['sentiment'] = df['label'].apply(map_rating_to_sentiment)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# Create model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model/sentiment_model.pkl")
print("✅ Model trained and saved to model/sentiment_model.pkl")
