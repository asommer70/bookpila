from django import forms
from django.core import validators
from . import models

class BookForm(forms.ModelForm):
    upload = forms.FileField(required=False)
    isbn = forms.CharField(required=False)
    about = forms.CharField(widget=forms.Textarea, required=False)
    author = forms.CharField(required=False)
    current_loc = forms.IntegerField(required=False)
    cover_image = forms.ImageField(required=False)

    class Meta:
        model = models.Book
        fields = [
            'title',
            'author',
            'about',
            'isbn',
            'current_loc',
            'upload',
            'cover_image'
        ]


class TagForm(forms.Form):
    tags = forms.CharField(required=True, label="Add Tags")


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty"
    )

    def clean_honeypost(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("honeypost is not empty!")
        return honeypot
