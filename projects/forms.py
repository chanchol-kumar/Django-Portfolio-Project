from django import forms
from projects.models import ProjectsModel

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = ProjectsModel
        fields =['category', 'image', 'title','descriptions','technology','git_link','live_link']
