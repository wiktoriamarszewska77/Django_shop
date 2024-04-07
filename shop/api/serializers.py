from rest_framework import serializers
from products.models import Product
from review.models import Review
from rest_framework.response import Response


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "seller",
            "name",
            "brand",
            "category",
            "price",
            "data_added",
            "description",
            "image",
            "stock_quantity",
            "available",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["data_added"] = instance.data_added.strftime("%d-%m-%Y %H:%M:%S")
        return representation


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "brand",
            "category",
            "price",
            "description",
            "image",
            "stock_quantity",
            "available",
        ]


class ReviewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "user", "product", "date", "comment", "rating"]


class AverageRatingProductSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    avg_rating = serializers.FloatField()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
