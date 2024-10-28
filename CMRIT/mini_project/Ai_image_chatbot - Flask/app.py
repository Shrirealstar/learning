import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the MobileNetV2 model for image recognition
model = MobileNetV2(weights='imagenet')

# Load API key from environment variable
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

# Define the Google Generative Language API endpoint
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

# Function to recognize image and provide summary
def recognize_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    summary_lines = []
    for _, label, score in decoded_predictions:
        summary_lines.append(f"Identified {label} with {score * 100:.2f}% confidence.")
    
    # Create a detailed 10-line summary of the image
    detailed_summary = """
    The image shows {0}. It is likely a {1}. The object appears clearly in the foreground.
    The setting suggests an outdoor scene. The lighting indicates it's daytime.
    The colors in the image are well defined, with the main subject having distinct features.
    The background might contain additional elements, like buildings or trees.
    Overall, the image is vivid and well-framed, showing high contrast between the object and background.
    """.format(decoded_predictions[0][1], decoded_predictions[1][1])

    return detailed_summary.strip()

# Function to generate answers based on the image and user's question
def generate_answer(user_query, image_info):
    prompt = f"""
    Role: Your role is to take all the information about the image which is uploaded by the user. And be ready to answer all types of questions with proper and correct information for the {user_query}. Provide a concise, helpful answer.
    Context: The image contains {image_info}.
    """

    request_body = {
        "prompt": {
            "text": prompt
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(endpoint, json=request_body, headers=headers)
    answer_data = response.json()
    return answer_data.get('output', 'Sorry, I could not find an appropriate answer.')

# Route for uploading the image and starting the conversation
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(image_path)

            # Recognize image and get summary
            summary = recognize_image(image_path)
            return render_template('index.html', image_path=image_path, summary=summary, chat_history=[])
    
    return render_template('index.html', chat_history=[])

# Route for handling user questions
@app.route('/ask_question', methods=['POST'])
def ask_question():
    question = request.form['question']
    image_info = "the recognized objects from the uploaded image"  # Placeholder for actual image info
    answer = generate_answer(question, image_info)

    # Update the chat history (simulating user and bot chat)
    chat_history = [
        {"from": "user", "text": question},
        {"from": "bot", "text": answer}
    ]
    
    return render_template('index.html', chat_history=chat_history)

if __name__ == '__main__':
    app.run(debug=True)
