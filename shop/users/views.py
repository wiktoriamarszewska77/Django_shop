from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render('login')
        else:
            form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('profile')
        else:
            form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})