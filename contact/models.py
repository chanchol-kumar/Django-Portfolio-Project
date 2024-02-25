from django.db import models

class ContactModel(models.Model):
    Name = models.CharField(max_length = 30)
    Email = models.EmailField(max_length = 30)
    Message = models.TextField()
    
    def __str__(self):
        return f"name : {self.Name}"