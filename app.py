# Library imports
import requests
import random
import logging
import os
from flask import Flask, request, jsonify, render_template
import openai

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create the app object
app = Flask(__name__)

# Load API key from file
try:
    with open('openai_key.txt', 'r') as f:
        OPENAI_API_KEY = f.read().strip()
        openai.api_key = OPENAI_API_KEY
        logger.info("OpenAI API key loaded successfully")
except Exception as e:
    logger.error(f"Failed to load OpenAI API key: {str(e)}")
    raise

# Fallback responses for when the API doesn't provide a clear response
fallback_responses = [
    "I'm not quite sure I understand. Could you rephrase that?",
    "That's interesting! Can you tell me more?",
    "I'm still learning. What else would you like to talk about?",
    "I'm trying to understand what you mean. Could you explain differently?",
    "Let's talk about something else. How was your day?",
    "I'm not sure how to respond to that, but I'm here to chat!",
    "Interesting perspective. What makes you say that?",
    "I'd like to understand better. Could you elaborate?",
    "That's a unique thought! What else is on your mind?",
    "I'm learning from our conversation. What else would you like to discuss?"
]

# Define home route
@app.route('/')
def home():
    logger.debug("Rendering home page")
    return render_template('index.html')

# Function to get response from OpenAI
def get_openai_response(message):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and supportive chatbot. Keep responses brief, casual, and positive like talking to a friend."},
                {"role": "user", "content": message}
            ],
            max_tokens=150
        )
        
        response_text = response.choices[0].message.content
        logger.debug(f"OpenAI response: {response_text}")
        
        # Simple sentiment analysis based on words in response
        sentiment = "neutral"
        positive_words = ["happy", "great", "awesome", "good", "excellent", "love", "enjoy", "nice"]
        negative_words = ["sad", "sorry", "unfortunately", "bad", "difficult", "trouble", "problem"]
        
        response_lower = response_text.lower()
        positive_count = sum(word in response_lower for word in positive_words)
        negative_count = sum(word in response_lower for word in negative_words)
        
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
            
        return response_text, sentiment
    except Exception as e:
        logger.error(f"Error getting OpenAI response: {str(e)}")
        return None, "neutral"

# Define predict function
@app.route('/predict', methods=['POST'])
def predict():
    logger.debug("Received POST request to /predict")
    try:
        # Get user input
        query_asis = [str(x) for x in request.form.values()]
        logger.debug(f"User input: {query_asis}")
        if not query_asis or query_asis[0].strip() == '':
            raise ValueError("No input provided")

        user_message = query_asis[0]
        
        # Get response from OpenAI
        response_text, sentiment = get_openai_response(user_message)
        
        if response_text:
            response = response_text
        else:
            # Fallback if OpenAI request failed
            response = random.choice(fallback_responses)
        
        # Determine GIF based on sentiment
        gif = "Happy.gif" if sentiment == "positive" else "sad.gif"
        
        return jsonify({'response': response, 'gif': gif})
    except Exception as e:
        logger.error(f"Error in predict: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)