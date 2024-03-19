from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('add_review/<int:product_id>/', ReviewCreateView.as_view(), name='add_review'),
]