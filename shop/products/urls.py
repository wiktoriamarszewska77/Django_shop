from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductListView,
    HomeView,
    BrandProductListView,
    AboutView,
    UserProductList,
    ContactView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("products/", ProductListView.as_view(), name="products-list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="detail-product"),
    path("add/product", ProductCreateView.as_view(), name="add-product"),
    path(
        "product/update/<int:pk>/", ProductUpdateView.as_view(), name="product-update"
    ),
    path(
        "product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product-delete"
    ),
    path(
        "category/<str:category>/",
        CategoryProductListView.as_view(),
        name="category-product",
    ),
    path("brand/<str:brand>/", BrandProductListView.as_view(), name="brand-product"),
    path("user/products/", UserProductList.as_view(), name="user_products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
