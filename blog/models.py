from django.db import models

class BlogModel(models.Model):
    image = models.ImageField(upload_to='blog_img/', null=True, blank=True)
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title