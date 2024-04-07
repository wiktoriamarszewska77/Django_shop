from rest_framework.viewsets import generics, GenericViewSet
from rest_framework import mixins
from api.serializers import (
    ProductSerializer,
    CreateProductSerializer,
    ReviewProductSerializer,
    AverageRatingProductSerializer,
)
from products.models import Product
from rest_framework.permissions import BasePermission
from users.models import Company
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from review.models import Review
from django.db.models import Avg


class GetAllProductsAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetDetailProductAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductSerializer
    queryset = Product


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Company.objects.filter(user=request.user).exists()
        return False


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [SellerPermission]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.company)


class UpdateProductAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [SellerPermission]
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user.company)

    def perform_update(self, serializer):
        serializer.save()


class DeleteProductAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [SellerPermission]
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user.company)


class ReviewProductViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Review.objects.all()
    serializer_class = ReviewProductSerializer


class AverageRatingProductViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Review.objects.values("product").annotate(avg_rating=Avg("rating"))
    serializer_class = AverageRatingProductSerializer
