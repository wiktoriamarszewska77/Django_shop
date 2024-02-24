from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import RegisterForm, CompanyForm, UserProfileForm, CompanyProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        user_form = RegisterForm()
        company_form = CompanyForm()
        return render(request, template_name='register.html',
                      context={'user_form': user_form, 'company_form': company_form})

    def post(self, request):
        user_form = RegisterForm(request.POST)
        company_form = CompanyForm(request.POST)
        if user_form.is_valid() and company_form.is_valid():
            if company_form.cleaned_data.get('nip'):
                user = user_form.save()
                company = company_form.save(commit=False)
                company.user = user
                company.save()
                messages.success(request, 'You have been registered as a company!')
            else:
                user_form.save()
                messages.success(request, 'You have been registered as a user!')
            return redirect('login')
        else:
            user_form = RegisterForm()
            company_form = CompanyForm()
            messages.warning(request, 'Incorrect data, try again!')
        return render(request, template_name='register.html',
                      context={'user_form': user_form, 'company_form': company_form})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        if hasattr(request.user, 'company'):
            user_form = UserProfileForm(instance=request.user)
            company_form = CompanyProfileForm(instance=request.user.company)
        else:
            user_form = UserProfileForm(instance=request.user)
            company_form = None

        return render(request, 'profile.html', context={'user_form': user_form, 'company_form': company_form})

    def post(self, request):
        user_form = UserProfileForm(request.POST, request.FILES, instance=request.user)

        if hasattr(request.user, 'company'):
            company = request.user.company
            company_form = CompanyProfileForm(request.POST, request.FILES, instance=company)
        else:
            company_form = None

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Data updated!')
            if company_form and company_form.is_valid():
                company_form.save()
            return redirect('profile')

        return render(request, 'profile.html', context={'user_form': user_form, 'company_form': company_form})
