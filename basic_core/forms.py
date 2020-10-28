from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Full Name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Valid Email Address"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Your Message"
    }))