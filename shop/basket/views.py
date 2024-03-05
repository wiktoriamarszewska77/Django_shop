from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from .basket import Basket
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def basket_summary(request):
    basket = Basket(request)
    basket_products = basket.get_prods
    return render(request, 'basket_summary.html', {'basket_products': basket_products})



def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product)

        basket_quantity = basket.__len__()
        response = JsonResponse({'qty': basket_quantity})
        # response = JsonResponse({'Product Name:': product.name})
        return response
