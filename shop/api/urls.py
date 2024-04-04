from django.urls import path
from .views import (
    GetAllProductsAPIView,
    GetDetailProductAPIView,
    CreateProductAPIView,
)

urlpatterns = [
    path("products/", GetAllProductsAPIView.as_view(), name="get_products"),
    path(
        "product/<int:pk>/",
        GetDetailProductAPIView.as_view(),
        name="get_detail_product",
    ),
    path("create/product/", CreateProductAPIView.as_view(), name="create_product"),
]
