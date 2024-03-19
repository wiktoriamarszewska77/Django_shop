from django.urls import path
from .views import ReviewProductView, ReviewCreateView, UpdateView, DeleteView, ReviewUserView

urlpatterns = [
    path('review/product/<int:product_id>/', ReviewProductView.as_view(), name='review_product'),
    path('add/review/<int:product_id>/', ReviewCreateView.as_view(), name='add_review'),
    path('update/review/<int:product_id>/', UpdateView.as_view(), name='update_review'),
    path('delete/review<int:product_id>/', DeleteView.as_view(), name='delete_review'),
    path('user/reviews/', ReviewUserView.as_view(), name='user_reviews'),
]