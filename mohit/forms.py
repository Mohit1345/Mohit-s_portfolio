# # forms.py
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(label='Your Name', max_length=100)
#     email = forms.EmailField(label='Your Email')
#     message = forms.CharField(label='Message', widget=forms.Textarea)


# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
