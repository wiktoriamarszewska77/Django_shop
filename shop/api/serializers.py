from rest_framework import serializers
from products.models import Product


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
