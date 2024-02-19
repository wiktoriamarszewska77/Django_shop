from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import RegisterForm, CompanyForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


class RegisterView(View):
    def get(self, request):
        user_form = RegisterForm()
        company_form = CompanyForm()
        return render(request, template_name='register.html', context={'user_form': user_form, 'company_form': company_form})

    def post(self, request):
        user_form = RegisterForm(request.POST)
        company_form = CompanyForm(request.POST)
        if user_form.is_valid() and company_form.is_valid():
            user_form.save()
            company_form.save(commit=False)
            return redirect('login')
        else:
            user_form = RegisterForm()
            company_form = CompanyForm()
        return render(request, template_name='register.html', context={'user_form': user_form, 'company_form': company_form})

@login_required()
def profile_view(request):
    return render(request, 'profile.html')