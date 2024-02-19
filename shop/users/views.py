from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
        else:
            form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})

@login_required()
def profile_view(request):
    return render(request, 'profile.html')