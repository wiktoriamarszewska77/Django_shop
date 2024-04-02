from django.urls import path
from .views import GetAllProducts

urlpatterns = [
    path("products/", GetAllProducts.as_view(), name="get_products"),
]
