from rest_framework.viewsets import generics
from api.serializers import ProductSerializer
from products.models import Product


class GetAllProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
