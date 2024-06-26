from rest_framework import serializers
from products.models import Product
from review.models import Review
from rest_framework.response import Response
from order.models import OrderItem, Order
from reports.models import Report


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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["id", "item", "price", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["buyer", "street", "city", "postcode", "date", "delivery", "status"]


class UserProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
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


class NewReportSerializer(serializers.Serializer):
    data_parameters = serializers.JSONField()
    report_format = serializers.ChoiceField(choices=["pdf", "xlsx"])
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    report_name = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["data_parameters"] = list(data.get("data_parameters", []))
        return data


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["id", "name", "creation_date", "status", "parameters"]
