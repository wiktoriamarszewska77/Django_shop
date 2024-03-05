from django.urls import path
from .views import basket_summary, basket_add

urlpatterns = [
    path('basket/', basket_summary, name='basket_summary'),
    path('add/', basket_add, name='basket_add'),
]
