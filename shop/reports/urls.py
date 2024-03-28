from django.urls import path
from .views import new_report_view


urlpatterns = [
    path("new/report/", new_report_view, name="new_report_view"),
]
