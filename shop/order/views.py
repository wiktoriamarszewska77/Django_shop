from django.shortcuts import render, redirect
from django.views import View
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from basket.basket import Basket
from .models import Order, OrderItem
from users.models import User
from products.models import Product
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class OrderView(View):
    def get(self, request):
        order_form = OrderForm(user=request.user, basket=Basket(request))
        return render(request, template_name='order.html', context={'order_form': order_form})

    def post(self, request):
        basket = Basket(request)
        order_form = OrderForm(request.POST, user=request.user, basket=basket)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.buyer = request.user
            order.save()

            products = basket.get_prods()
            for product in products:
                OrderItem.objects.create(order=order, item=product, price=product.price, quantity=product.stock_quantity)

            basket.remove_basket()
            messages.success(request, "Order placed successfully!")
            return redirect('payment_view', order_id=order.id)

        return render(request, 'order.html', {'order_form': order_form})

@login_required()
def order_summary_view(request):
    orders = Order.objects.filter(buyer=request.user)
    order_items = OrderItem.objects.filter(order__buyer=request.user)
    return render(request, 'order_summary.html', {'orders': orders, 'order_items': order_items})
