from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from .basket import Basket
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from shipping.models import Shipping

@login_required()
def basket_summary(request):
    basket = Basket(request)
    basket_products = basket.get_prods
    quantities = basket.basket
    totals = basket.basket_total()
    object_shipping = Shipping.objects.all()
    return render(request, 'basket_summary.html', {'basket_products': basket_products, 'quantities': quantities, 'totals': totals, 'object_shipping':object_shipping})


def basket_add(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product_id=product.id, quantity=product_qty)

        basket_quantity = basket.__len__()
        response = JsonResponse({'qty': basket_quantity})
        # response = JsonResponse({'Product Name:': product.name})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        basket.update(product_id=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        # return redirect('basket_summary')

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        basket.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response

