from django.urls import path
from .views import (
    GetAllProductsAPIView,
    GetDetailProductAPIView,
    CreateProductAPIView,
    UpdateProductAPIView,
    DeleteProductAPIView,
)

urlpatterns = [
    path("products/", GetAllProductsAPIView.as_view(), name="get_products"),
    path(
        "product/<int:pk>/",
        GetDetailProductAPIView.as_view(),
        name="get_detail_product",
    ),
    path("create/product/", CreateProductAPIView.as_view(), name="create_product"),
    path(
        "update/product/<int:pk>/",
        UpdateProductAPIView.as_view(),
        name="update_product",
    ),
    path(
        "delete/product/<int:pk>/",
        DeleteProductAPIView.as_view(),
        name="delete_product",
    ),
]
