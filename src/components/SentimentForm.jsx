import React, { useState } from 'react';
import Sentiment from 'sentiment';

const SentimentForm = () => {
    const [review, setReview] = useState('');
    const [result, setResult] = useState(null);

    const analyzeSentiment = () => {
        const sentiment = new Sentiment();
        const analysis = sentiment.analyze(review);

        const sentimentResult = analysis.score > 0
            ? 'Positive'
            : analysis.score < 0
            ? 'Negative'
            : 'Neutral';

        const strengths = [];
        const weaknesses = [];

        const positiveWords = ['good', 'great', 'excellent', 'amazing', 'love'];
        const negativeWords = ['bad', 'poor', 'terrible', 'disappointing', 'hate'];

        review.toLowerCase().split(' ').forEach((word) => {
            if (positiveWords.includes(word)) strengths.push(word);
            if (negativeWords.includes(word)) weaknesses.push(word);
        });

        setResult({
            sentiment: sentimentResult,
            strengths: strengths.length > 0 ? strengths.join(', ') : 'None',
            weaknesses: weaknesses.length > 0 ? weaknesses.join(', ') : 'None'
        });
    };

    const goToBackend = () => {
        window.open('http://localhost:8000/docs', '_blank');
    };

    return (
        <div className="container">
            <h1>Sentiment Analysis Tool</h1>
            <textarea
                value={review}
                onChange={(e) => setReview(e.target.value)}
                placeholder="Enter your review here..."
                rows={4}
            />
            <button onClick={analyzeSentiment}>Analyze Sentiment</button>

            {result && (
                <div className="result">
                    <h3>Result:</h3>
                    <p><b>Sentiment:</b> {result.sentiment}</p>
                    <p><b>Strengths:</b> {result.strengths}</p>
                    <p><b>Weaknesses:</b> {result.weaknesses}</p>
                </div>
            )}

            {/* Go to Backend Button */}
            <button onClick={goToBackend} style={{ marginTop: '20px' }}>Go to Backend</button>
        </div>
    );
};

export default SentimentForm;
