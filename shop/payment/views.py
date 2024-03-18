from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

@login_required()
def payment_view(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'mark_as_paid':
            order.status = 'paid'
        elif action == 'mark_as_canceled':
            order.status = 'canceled'
        order.save()
        return redirect('order_summary')

    return render(request, 'payment.html', context={'order': order})