from rest_framework import routers
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from .views import (
    LoginAPIView,
    ProductViewSet,
    GetAllOrDetailProductsViewSet,
    ReviewProductViewSet,
    AverageRatingProductViewSet,
    ProductsSoldViewSet,
    UserProductsViewSet,
    ProductsOrdered,
    NewReportViewSet,
    ReportsViewSet,
    DownloadReportPDF,
    DownloadReportXLSX,
)

router = routers.DefaultRouter()
router.register("actions-products", ProductViewSet, basename="actions-products")
router.register(
    "get-products",
    GetAllOrDetailProductsViewSet,
    basename="get-products",
)
router.register("review", ReviewProductViewSet, basename="review")
router.register(
    "average-rating", AverageRatingProductViewSet, basename="average-rating"
)
router.register("products-sold", ProductsSoldViewSet, basename="products-sold")
router.register("user-products", UserProductsViewSet, basename="user-products")
router.register("products-ordered", ProductsOrdered, basename="products-ordered")
router.register("new-report", NewReportViewSet, basename="new-report")
router.register("reports", ReportsViewSet, basename="reports")

urlpatterns = [
    path("loginup/", LoginAPIView.as_view(), name="loginup"),
    path(
        "download-report-pdf/<int:report_id>/",
        DownloadReportPDF.as_view(),
        name="download_report_pdf",
    ),
    path(
        "download-report-xlsx/<int:report_id>/",
        DownloadReportXLSX.as_view(),
        name="download_report_xlsx",
    ),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
] + router.urls
