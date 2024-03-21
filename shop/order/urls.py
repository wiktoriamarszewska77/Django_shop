from django.urls import path
from .views import OrderView, order_summary_view


urlpatterns = [
    path("order/", OrderView.as_view(), name="order"),
    path("order_summary/", order_summary_view, name="order_summary"),
]
