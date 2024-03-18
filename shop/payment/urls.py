from django.urls import path
from .views import payment_view

urlpatterns = [
    path('payment/<int:order_id>/', payment_view, name='payment_view')
]