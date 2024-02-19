from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Company

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

class CompanyForm(forms.ModelForm):
    nip = forms.CharField(required=False, max_length=10)
    class Meta:
        model = Company
        fields = ['nip']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

