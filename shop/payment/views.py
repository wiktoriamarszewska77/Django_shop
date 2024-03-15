from django.shortcuts import render

def payment_view(request):
    return render(request, template_name='payment.html')