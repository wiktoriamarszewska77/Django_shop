from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from basket.basket import Basket
from .models import Order
from users.models import User, Company
from products.models import Product


@method_decorator(login_required, name='dispatch')
class OrderView(View):
    def get(self, request):
        order_form = OrderForm(user=request.user)
        basket = Basket(request)
        return render(request, template_name='order.html', context={'order_form': order_form, 'basket': basket})


    def post(self, request):
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.buyer = request.user
            order.save()  # Zapisz zamówienie do bazy danych
            basket = Basket(request)
            # basket.clear()  # Wyczyść koszyk po złożeniu zamówienia
            return redirect('profile')  # Przekieruj użytkownika na stronę profilu po złożeniu zamówienia

        return render(request, 'order.html', {'order_form': order_form})



