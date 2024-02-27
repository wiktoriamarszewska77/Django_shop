from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView



urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('add/product', ProductCreateView.as_view(), name='add-product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    ]