import os
import requests
from flask import Flask, request, render_template
from dotenv import load_dotenv

app = Flask(__name__)

# Load API key from environment variable
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

# Define the API endpoint
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def generate_questions(topic_title, queries_num, level="Easy"):
    prompt = f"""
    Role: You are an expert in generating interview questions for academic positions with a strong understanding of the client's vision.
    Context: The user's requirements for the question you are analyzed. You have a solid understanding of their needs.
    Level: Based on the chosen level, provide questions to help the user improve their skills.
    Please generate {queries_num} interview questions for the topic "{topic_title}" suitable for an {level} level interview.
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
            return ["No questions generated. Please try again."]
        questions = candidates[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip().split('\n')
        if not questions or questions == ['']:
            return ["No questions generated. Please try again."]
        return questions
    except requests.exceptions.RequestException as e:
        return [f"An error occurred: {e}"]
    except KeyError:
        return ["Unexpected response format from the API."]

def get_ai_feedback(question, answer):
    prompt = f"""
    Provide feedback on the candidate's response to the question: "{question}" based on the provided answer.
    Focus on:
    - Feedback to improve the interviewer's impression (max 5 lines)
    - How to enhance the response (max 3 lines)
    - Positive aspects of the answer (max 3 lines)
    - Mistakes made (max 5 lines)
    - Suggestions for improvement (max 3 lines)
    - Additional tips (max 5 points)
    - Score out of 100 based on quality (max 2 lines)

    - Use bullet points and avoid repeating the question.
    - Ensure unique responses without repetition.
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
        feedback = data.get('candidates', [])[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
        return feedback
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Unexpected response format from the API."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic_title = request.form['topic_title']
        queries_num = int(request.form['queries_num'])
        questions = generate_questions(topic_title, queries_num)
        return render_template('questions.html', questions=questions, topic_title=topic_title, queries_num=queries_num)
    return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    questions = request.form.getlist('questions')
    answers = request.form.getlist('answers')
    feedbacks = [get_ai_feedback(question, answer) for question, answer in zip(questions, answers)]
    return render_template('feedback.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
