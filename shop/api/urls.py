from rest_framework import routers
from django.urls import path
from .views import (
    LoginAPIView,
    GetAllProductsAPIView,
    GetDetailProductAPIView,
    CreateProductAPIView,
    UpdateProductAPIView,
    DeleteProductAPIView,
    ReviewProductViewSet,
    AverageRatingProductViewSet,
    ProductsSoldViewSet,
    UserProductsViewSet,
    ProductsOrdered,
    ReportsViewSet,
    download_report_pdf,
    download_report_xlsx,
)

router = routers.DefaultRouter()

router.register("review", ReviewProductViewSet, basename="review")
router.register(
    "average/rating", AverageRatingProductViewSet, basename="average_rating"
)
router.register("products/sold", ProductsSoldViewSet, basename="products_sold")
router.register("user/products", UserProductsViewSet, basename="user_products")
router.register("products/ordered", ProductsOrdered, basename="products_ordered")
router.register("reports", ReportsViewSet, basename="reports")

urlpatterns = [
    path("loginup/", LoginAPIView.as_view(), name="loginup"),
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
    path(
        "download-report-pdf/<int:report_id>/",
        download_report_pdf,
        name="download_report_pdf",
    ),
    path(
        "download-report-xlsx/<int:report_id>/",
        download_report_xlsx,
        name="download_report_xlsx",
    ),
] + router.urls
