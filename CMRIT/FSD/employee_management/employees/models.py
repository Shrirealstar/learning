from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    courses = models.TextField()  # Store courses as a comma-separated string
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
