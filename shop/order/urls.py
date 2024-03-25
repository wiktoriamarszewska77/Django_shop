from django.urls import path
from .views import OrderView, order_summary_view, ProductsSoldView


urlpatterns = [
    path("order/", OrderView.as_view(), name="order"),
    path("order_summary/", order_summary_view, name="order_summary"),
    path("products/sold/", ProductsSoldView.as_view(), name="products_sold"),
]
