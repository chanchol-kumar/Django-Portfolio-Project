from django.db import models

class ReviewModel(models.Model):
    RATING_CHOICES = (
        ('⭐️', '⭐️'),
        ('⭐️⭐️', '⭐️⭐️'),
        ('⭐️⭐️⭐️', '⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️⭐️'),
        ('⭐️⭐️⭐️⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️⭐️⭐️'),
    )
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=30)
    Phone_no = models.CharField(max_length=30)
    Rating = models.CharField(max_length=14,choices=RATING_CHOICES)
    Comment = models.TextField()

    def __str__(self):
        return f"Name: {self.Name}"
