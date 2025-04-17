import React, { useState } from 'react';
import Sentiment from 'sentiment';

const SentimentForm = () => {
    const [review, setReview] = useState('');
    const [result, setResult] = useState(null);

    // const analyzeSentiment = async () => {
    //     try {
    //         const response = await fetch('http://localhost:8000/analyze', {
    //             method: 'POST',
    //             headers: {
    //                 'Content-Type': 'application/json',
    //             },
    //             body: JSON.stringify({ text: review }),
    //         });

    //         const data = await response.json();
    //         setResult({
    //             sentiment: data.sentiment,
    //             strengths: data.strengths || 'None',
    //             weaknesses: data.weaknesses || 'None',
    //         });
    //     } catch (error) {
    //         console.error('Error:', error);
    //     }
    // };


    // Using the Sentiment library to analyze sentiment
    const analyzeSentiment = async () => {
        try {
            const response = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: review }),
            });
    
            const data = await response.json();
            setResult({
                sentiment: data.sentiment,
                confidence: data.confidence,
            });
        } catch (error) {
            console.error('Error:', error);
        }
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
                    <p><b>score:</b> {result.confidence}</p>
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
