from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryProductListView, HomeView, BrandProductListView





urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='products-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail-product'),
    path('add/product', ProductCreateView.as_view(), name='add-product'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('category/<str:category>/', CategoryProductListView.as_view(), name='category-product'),
    path('brand/<str:brand>/', BrandProductListView.as_view(), name='brand-product'),
]