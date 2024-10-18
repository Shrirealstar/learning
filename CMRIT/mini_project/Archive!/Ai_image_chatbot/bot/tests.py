from django.test import TestCase
from .forms import ImageUploadForm, ChatForm

class ImageUploadFormTest(TestCase):
    def test_image_upload_form(self):
        form_data = {}
        file_data = {'image': 'path/to/image.jpg'}
        form = ImageUploadForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())

class ChatFormTest(TestCase):
    def test_chat_form(self):
        form_data = {'user_message': 'What is in the image?'}
        form = ChatForm(data=form_data)
        self.assertTrue(form.is_valid())

class ViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
