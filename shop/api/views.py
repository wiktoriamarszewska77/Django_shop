from rest_framework.viewsets import generics
from api.serializers import ProductSerializer, CreateProductSerializer
from products.models import Product
from rest_framework.permissions import BasePermission, IsAuthenticated
from users.models import Company


class GetAllProductsAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class GetDetailProductAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product


class SellerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Company.objects.filter(user=request.user).exists()
        return False


class CreateProductAPIView(generics.CreateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated, SellerPermission]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.company)


class UpdateProductAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CreateProductSerializer
    permission_classes = [IsAuthenticated, SellerPermission]
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user.company)

    def perform_update(self, serializer):
        serializer.save()


class DeleteProductAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, SellerPermission]
    queryset = Product.objects.all()

    def get_queryset(self):
        return self.queryset.filter(seller=self.request.user.company)
