from django.urls import path
from .views import (
    new_report_view,
    reports_view,
    download_report_pdf,
    download_report_xlsx,
)


urlpatterns = [
    path("new/report/", new_report_view, name="new_report_view"),
    path("reports/", reports_view, name="reports_view"),
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
]
