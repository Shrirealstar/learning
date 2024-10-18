from django.shortcuts import render

# Main page for uploading images and interacting with the chatbot
def index(request):
    return render(request, 'index.html')

# Chat interaction page to display chat UI
def chat_page(request):
    return render(request, 'chat.html')

def home(request):
    return render(request, 'home.html')

def chat_page(request):
    return render(request, 'chat_interface.html')