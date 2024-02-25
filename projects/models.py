from django.db import models

class ProjectsModel(models.Model):
    CHOICES = (
        ('Web Development', 'Web Development'),
        ('Adroid Development', 'Adroid Development'),
        ('Django Project ', 'Django Project'),
        ('Machine Learning', 'Machine Learning'),
    )
    
    category = models.CharField(max_length=30, choices=CHOICES,null=True, blank=True)
    image = models.ImageField(upload_to='project_img/', null=True, blank=True)
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=500)
    technology = models.CharField(max_length=100,null=True, blank=True)
    git_link = models.URLField(max_length=100, null=True, blank=True)
    live_link = models.URLField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.title
