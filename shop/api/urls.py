from django.urls import path
from .views import GetAllProducts, GetDetailProduct, CreateProduct

urlpatterns = [
    path("products/", GetAllProducts.as_view(), name="get_products"),
    path("product/<int:pk>/", GetDetailProduct.as_view(), name="get_detail_product"),
    path("create/product/", CreateProduct.as_view(), name="create_product"),
]
