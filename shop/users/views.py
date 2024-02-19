from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import RegisterForm


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

