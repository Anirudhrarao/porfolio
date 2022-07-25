from dataclasses import field
from pyexpat import model
from django import forms 
from .models import Contact

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(max_length=120,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter name'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Email'
        }
    ))
    phone_number = forms.CharField(max_length=14,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Phone Nmuber'
        }
    ))
    msg = forms.CharField(max_length=500,widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Message'
        }
    ))
    class Meta():
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'msg']