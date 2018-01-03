from django import forms
from django.core import validators
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            'title',
            'author',
            'about',
            'isbn',
            'file_url',
            'current_loc'
        ]

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty"
    )

    def clean_honeypost(self):
        honeypot = self.cleanded_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("honeypost is not empty!")
        return honeypot
