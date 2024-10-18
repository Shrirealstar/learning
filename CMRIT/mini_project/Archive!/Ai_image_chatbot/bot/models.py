from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image {self.id} uploaded at {self.upload_time}'

class ChatHistory(models.Model):
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Chat entry for image {self.image.id} at {self.timestamp}'
