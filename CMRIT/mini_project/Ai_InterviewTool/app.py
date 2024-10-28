from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load API key from .env file
load_dotenv()
api_key = os.getenv('API_KEY')
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

# Home route - displays the topic input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle question generation based on the topic
@app.route('/', methods=['POST'])
def generate_question():
    topic_title = request.form.get('topic_title')
    question = generate_questions(topic_title)
    return render_template('questions.html', topic_title=topic_title, questions=question)

# Function to generate one unique interview question
def generate_questions(topic_title):
    prompt = f"""
    Generate one unique interview question for the topic '{topic_title}'.
    The question should be challenging but answerable by someone with knowledge of the topic.
    Provide only one question.
    """

    request_body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(f"{endpoint}?key={api_key}", json=request_body)
        response.raise_for_status()
        data = response.json()
        candidates = data.get('candidates', [])
        if not candidates:
            return ["No question generated. Please try again."]
        question = candidates[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
        if not question:
            return ["No question generated. Please try again."]
        return [question]
    except requests.exceptions.RequestException as e:
        return [f"An error occurred: {e}"]
    except KeyError:
        return ["Unexpected response format from the API."]

# Route to handle feedback submission after the user answers the question
@app.route('/feedback', methods=['POST'])
def feedback():
    answers = request.form.get('answers')
    questions = request.form.get('questions')
    feedback = analyze_feedback(answers)
    return render_template('feedback.html', feedback=feedback)

# Function to analyze feedback (can be modified to implement AI-based analysis)
def analyze_feedback(answers):
    # For now, a simple response. You can add AI-based feedback generation here.
    return f"Your answer was: {answers}\n\nStrengths: Detailed explanation.\nAreas for improvement: Be more concise."

if __name__ == '__main__':
    app.run(debug=True)
