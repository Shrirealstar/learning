import os
import requests
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the GOOGLE_API_KEY environment variable.")

# Define the API endpoint for the Gemini model
endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"

def check_api_key():
    data = {
        "contents": [
            {
                "parts": [
                    {"text": "Explain AI in detail."}  # Prompt for explanation
                ]
            }
        ]
    }

    try:
        response = requests.post(f"{endpoint}?key={api_key}", json=data)
        response.raise_for_status()
        
        # Extracting only the relevant text from the response
        output_text = response.json()['candidates'][0]['content']['parts'][0]['text']
        print("Response:\n")
        print(output_text)  # Print the formatted response for the user query.
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError:
        print("Unexpected response format from the API.")

if __name__ == '__main__':
    check_api_key()
