from django import forms
from review.models import ReviewModel

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields =['Name', 'Email','Phone_no','Rating' ,'Comment']