from django import forms
from django.forms.fields import CharField

class LoginForm(forms.Form):
    mail = forms.EmailField(label='Mail')
    passWord =forms.CharField(lebel="Mot de passe", widget= forms.PasswordInput)