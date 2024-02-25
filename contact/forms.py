from django import forms
from contact.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields =['Name', 'Email', 'Message']