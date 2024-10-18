from django.urls import path
from ..Ai_image_chatbot import backend_views  # Import backend views where image and chat are processed

urlpatterns = [
    path('process-image/', backend_views.process_image, name='process_image'),
    path('chat-response/', backend_views.chat_response, name='chat_response'),
]
