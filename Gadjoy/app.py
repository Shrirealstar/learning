from flask import Flask, request, jsonify, render_template
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

app = Flask(__name__)

# Load NLTK stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    return [word for word in words if word.isalnum() and word not in stop_words]

# Function to find the most relevant answer using TF-IDF
def get_most_relevant_answer(question, document_content):
    # Tokenize question and document
    preprocessed_question = preprocess_text(question)
    preprocessed_document = preprocess_text(document_content)

    # Combine question and document for TF-IDF
    all_texts = preprocessed_question + preprocessed_document

    # Calculate TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    # Calculate cosine similarity
    cosine_similarities = (tfidf_matrix * tfidf_matrix.T).toarray()

    # Find the index of the most relevant sentence
    question_index = len(preprocessed_question) - 1
    most_relevant_index = cosine_similarities[question_index].argsort()[-2]

    # Retrieve the most relevant sentence
    most_relevant_sentence = sent_tokenize(document_content)[most_relevant_index]

    return most_relevant_sentence

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def process_question():
    # Get the user's question
    user_question = request.form.get('question')

    # Specify the path to the document
    document_path = 'procedures.docx'

    try:
        # Read the document content
        doc = Document(document_path)
        document_content = ' '.join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        return jsonify({'error': f'Error reading document: {str(e)}'})

    # Get the most relevant answer for the question
    answer = get_most_relevant_answer(user_question, document_content)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
