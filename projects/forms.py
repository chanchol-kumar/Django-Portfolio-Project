from django import forms
from projects.models import ProjectsModel

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = ProjectsModel
        fields =['image', 'title','descriptions','descriptions']