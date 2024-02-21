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


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'image']

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'nip']