from django.db import models

class SkillModel(models.Model):
    proficiency_levels = [
        (25, 'Beginner'),
        (50, 'Intermediate'),
        (75, 'Advanced'),
        (100, 'Expert'),
    ]
    icon = models.ImageField(upload_to='skill/media/', blank=True, null=True)
    skill_name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices = proficiency_levels)

    def __str__(self):
        return self.skill_name
