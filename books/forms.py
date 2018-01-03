from django import forms
from django.core import validators

class ContactForm(forms.Form):
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave empty",
        validators=[validators.MaxLengthValidator(0)]
    )

    # def clean_honeypost(self):
    #     honeypot = self.cleanded_data['honeypot']
    #     if len(honeypot):
    #         raise forms.ValidationError("honeypost is not empty!")
    #     return honeypot
