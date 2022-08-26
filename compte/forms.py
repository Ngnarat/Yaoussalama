from turtle import textinput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields,TextInput
from .models import User, Beneficiaire



class LoginForm(forms.Form):
    mail = forms.EmailField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Adresse mail'}), max_length=150)
    password =forms.CharField(label="Password", widget= forms.PasswordInput(attrs={'placeholder':'Mot de passe'}), max_length=50)
    

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email', 'dateOfBirth','telephone', \
            'adresse1','adresse2','codePostal','ville','country',)
        exclude = ['username']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control', 'placeholder':'name@example.com'}),
            'dateOfBirth': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'}),
            'adresse1': TextInput(attrs={'class': 'form-control'}),
            'adresse2': TextInput(attrs={'class': 'form-control'}),
            'codePostal': TextInput(attrs={'class': 'form-control','placeholder':'EX: 44000'}),
            'ville': TextInput(attrs={'class': 'form-control'}),
            'country': TextInput(attrs={'class': 'form-control'}),
            'password1': TextInput(attrs={'class': 'form-control'}),
            'password2': TextInput(attrs={'class': 'form-control'}),
        }
        
        
        
class BeneficaireForm(forms.ModelForm):
    class Meta:
        model  = Beneficiaire
        fields  = ('photo','first_name', 'last_name','dateOfBirth','LientFamilial',)
    
