from django import forms
from skill.models import SkillModel

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields =['icon', 'skill_name','proficiency']