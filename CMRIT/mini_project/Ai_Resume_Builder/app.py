import os
import requests
from flask import Flask, request, render_template, send_file
from dotenv import load_dotenv
from fpdf import FPDF
import fitz  # PyMuPDF for PDF extraction
from docx import Document  # For Word document extraction

app = Flask(__name__)

# Load API key from environment variable
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

# Define the API endpoint
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def get_ai_response(prompt):
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
        return feedback.replace('\n', '<br>')  # Replace newlines with <br> for HTML rendering
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except KeyError:
        return "Unexpected response format from the API."


# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Extract text from Word document
def extract_text_from_word(uploaded_file):
    doc = Document(uploaded_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# PDF creation function
def create_pdf(resume_data, output_filename):
    pdf = FPDF()
    pdf.add_page()

    # Set the font for the PDF
    pdf.set_font("Arial", size=12)

    # Add sections to the PDF
    for section, content in resume_data.items():
        pdf.cell(200, 10, f"{section}:", ln=True)
        pdf.multi_cell(0, 10, content)
        pdf.ln(5)

    # Save the PDF
    pdf.output(output_filename)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create_resume():
    if request.method == 'POST':
        # Collect user inputs
        name = request.form.get('name')
        profile = request.form.get('profile')
        education = request.form.get('education')
        skills = request.form.get('skills')
        work_experience = request.form.get('work_experience')
        contact = request.form.get('contact')
        projects = request.form.get('projects')
        hobbies = request.form.get('hobbies')

        # Generate the organized resume content using AI
        prompt = f"""
        Provide a professional resume based on the candidate's information:
        Name: {name}
        Education: {education}
        Skills: {skills}
        Work Experience: {work_experience}
        Contact: {contact}
        Projects: {projects}
        Hobbies: {hobbies}
        Profile: {profile}
        Format the information professionally, use bullet points, and ensure clarity and conciseness.
        """
        organized_resume = get_ai_response(prompt)

        # Store the organized resume in a dictionary
        resume_data = {
            'Name': name,
            'Profile': profile,
            'Education': education,
            'Skills': skills,
            'Work Experience': work_experience,
            'Contact': contact,
            'Projects': projects,
            'Hobbies': hobbies
        }

        return render_template('create_resume.html', 
                               name=name,
                               organized_resume=organized_resume,
                               resume_data=resume_data)

    return render_template('create_resume.html', organized_resume=None)


@app.route('/update', methods=['GET', 'POST'])
def update_resume():
    if request.method == 'POST':
        uploaded_file = request.files['resume']
        if uploaded_file and uploaded_file.filename != '':
            if uploaded_file.filename.endswith('.pdf'):
                feedback_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.filename.endswith(('.doc', '.docx')):
                feedback_text = extract_text_from_word(uploaded_file)
            else:
                return render_template('update_resume.html', uploaded_filename=None, feedback="Invalid file format. Please upload a PDF or Word document.")

            # Generate feedback from AI
            prompt = f"Provide structured feedback on the candidate's resume based on the following text:\n{feedback_text}\nPlease analyze it and give suggestions for improvement in bullet points and lists."
            feedback = get_ai_response(prompt)

            return render_template('update_resume.html', 
                                   uploaded_filename=uploaded_file.filename,
                                   feedback=feedback)

    return render_template('update_resume.html', uploaded_filename=None, feedback=None)


@app.route('/download', methods=['POST'])
def download_resume():
    # Collect data again to generate the PDF
    name = request.form.get('name')
    profile = request.form.get('profile')
    education = request.form.get('education')
    skills = request.form.get('skills')
    work_experience = request.form.get('work_experience')
    contact = request.form.get('contact')
    projects = request.form.get('projects')
    hobbies = request.form.get('hobbies')

    # Store the organized resume in a dictionary
    resume_data = {
        'Name': name,
        'Profile': profile,
        'Education': education,
        'Skills': skills,
        'Work Experience': work_experience,
        'Contact': contact,
        'Projects': projects,
        'Hobbies': hobbies
    }

    # Create the PDF filename
    pdf_filename = f"{name.replace(' ', '_')}.pdf"
    create_pdf(resume_data, pdf_filename)  # Generate the PDF

    return send_file(pdf_filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
