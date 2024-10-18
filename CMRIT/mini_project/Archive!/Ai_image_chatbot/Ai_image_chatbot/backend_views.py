import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Load environment variables (such as OpenAI API key)
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# Store information about the image when it's uploaded
uploaded_image_info = {}  # This is where we'll store processed image info globally for this example

@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        
        # Process the image (e.g., use an image recognition API like Google Vision, OpenCV, etc.)
        # For this example, let's pretend we detected an object in the image
        uploaded_image_info['description'] = "a cat sitting on a sofa"  # Replace with actual processing result
        
        return JsonResponse({'result': 'Image successfully processed!'})
    else:
        return JsonResponse({'result': 'No image uploaded.'}, status=400)

@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        user_query = request.POST.get('query', '')

        if user_query:
            try:
                # Ensure the image was processed earlier and has relevant info
                if 'description' in uploaded_image_info:
                    image_description = uploaded_image_info['description']
                    
                    # Combine user query with the image description for the AI prompt
                    prompt = f"The user uploaded an image of {image_description}. Respond to the following query: {user_query}"
                    
                    # Send the query to the OpenAI API (or your chosen AI model)
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=prompt,
                        max_tokens=150
                    )
                    
                    ai_response = response.choices[0].text.strip()
                else:
                    ai_response = "No image information available. Please upload an image first."
            except Exception as e:
                ai_response = f"Error processing your query: {str(e)}"
            
            return JsonResponse({'ai_response': ai_response})
        else:
            return JsonResponse({'ai_response': 'No query provided.'})
    else:
        return JsonResponse({'ai_response': 'Invalid request method.'})
