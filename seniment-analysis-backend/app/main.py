# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# app = FastAPI()

# # Allow requests from the React frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # React dev server URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class SentimentRequest(BaseModel):
#     text: str

# @app.post("/analyze")
# def analyze_sentiment(request: SentimentRequest):
#     text = request.text.lower()
#     positive_words = ['good', 'great', 'excellent', 'amazing', 'love']
#     negative_words = ['bad', 'poor', 'terrible', 'disappointing', 'hate', 'worse']

#     score = sum(1 for word in text.split() if word in positive_words) - \
#             sum(1 for word in text.split() if word in negative_words)

#     sentiment = "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
#     strengths = [word for word in text.split() if word in positive_words]
#     weaknesses = [word for word in text.split() if word in negative_words]

#     return {
#         "sentiment": sentiment,
#         "strengths": ", ".join(strengths) if strengths else None,
#         "weaknesses": ", ".join(weaknesses) if weaknesses else None,
#     }

# @app.get("/")
# def read_root():
#     return {"message": "Hello from FastAPI"}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

class SentimentRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(request: SentimentRequest):
    # Use the Hugging Face model to analyze sentiment
    result = sentiment_pipeline(request.text)

    # Extract the label and score from the result
    sentiment = result[0]["label"]
    confidence = result[0]["score"]

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPIii"}






