from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body schema
class ReviewRequest(BaseModel):
    text: str

# Sample text for testing
sample_text = "i liked the product but customer service was bad"
sample_text1 = "i did not like  the product and the customer service was bad"


# Dummy ML prediction function (Replace this with real model)
def predict_sentiment(text):
    # Simple rule-based logic for demo
    positive_words = ['liked', 'good', 'great', 'excellent']
    negative_words = ['bad', 'poor', 'terrible', 'worst']
    
    text = text.lower()
    pos_count = sum(1 for word in positive_words if word in text)
    neg_count = sum(1 for word in negative_words if word in text)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"

# API endpoint for sentiment analysis
@app.post("/predict")
def analyze_review(review: ReviewRequest):
    sentiment = predict_sentiment(review.text)
    return {"sentiment": sentiment}

# Test endpoint with sample text
@app.get("/test")
async def test_sentiment():
    sentiment = predict_sentiment(sample_text)
    return {
        "text": sample_text,
        "sentiment": sentiment
    }

@app.get("/")
async def root():
    return {"message": "Welcome to Sentiment Analysis API"}
