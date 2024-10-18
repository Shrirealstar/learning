from django.contrib import admin
from django.urls import path, include  # Import include to include app-level URLs

from django.urls import path
from . import frontend_views, backend_views

urlpatterns = [
    path('', frontend_views.home, name='home'),  # Root URL
    path('process-image/', backend_views.process_image, name='process_image'),
    path('chat-response/', backend_views.chat_response, name='chat_response'),
]

