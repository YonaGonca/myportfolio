from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}), required=True)