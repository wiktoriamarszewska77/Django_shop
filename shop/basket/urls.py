from django.urls import path
from .views import basket_summary, basket_add, basket_update, basket_delete

urlpatterns = [
    path("basket/", basket_summary, name="basket_summary"),
    path("add/", basket_add, name="basket_add"),
    path("update/", basket_update, name="basket_update"),
    path("delete/", basket_delete, name="basket_delete"),
]
