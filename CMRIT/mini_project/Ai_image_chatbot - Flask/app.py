import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__)

# Load the API key from the .env file
API_KEY = os.getenv('GOOGLE_API_KEY')

# Define the Gemini API endpoint
GEMINI_API_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

# Set up file upload configurations
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for uploaded images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Check if the uploaded file is allowed by checking its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if a file is in the request
        if 'image' not in request.files:
            return "No file part in the request"

        file = request.files['image']
        
        if file.filename == '':
            return "No selected file"
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Simulating image recognition (You might replace this with actual image processing logic)
            # Assume we use OCR or another tool to generate text from the image
            simulated_image_text = "This is a placeholder text generated from image recognition."

            # Prepare the payload for the Gemini API
            payload = {
                "prompt": {
                    "text": simulated_image_text
                }
            }

            # Send the request to the Gemini API
            headers = {'Content-Type': 'application/json'}
            response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
                summary = result['candidates'][0]['output']
            else:
                summary = f"An error occurred: {response.status_code} {response.reason}"

            return render_template("index.html", summary=summary, image_url=file_path)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
