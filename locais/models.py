from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=200)
    def __str__(self):
        return self.title