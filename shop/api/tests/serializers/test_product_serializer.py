import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
from api.serializers import ProductSerializer  # noqa


@pytest.mark.django_db(transaction=False)
def test_product_serializer_to_representation(product, product_data):
    serializer = ProductSerializer(instance=product)

    expected_data = {
        "seller": product.seller.id,
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
        "price": str(product.price),
        "data_added": product.data_added.strftime("%d-%m-%Y %H:%M:%S"),
        "description": product.description,
        "image": product.image.url,
        "stock_quantity": product.stock_quantity,
        "available": product.available,
    }

    assert serializer.data == expected_data


@pytest.mark.django_db(transaction=False)
def test_return_error_when_product_serializer_with_invalid_data():
    invalid_data = {
        "seller": 1,
        "name": "",
        "brand": "Test Brand",
        "category": "Test Category",
        "price": "invalid_price",
        "data_added": "2022-01-01",
        "description": "Test Description",
        "stock_quantity": -10,
        "available": "invalid_value",
    }

    serializer = ProductSerializer(data=invalid_data)
    assert not serializer.is_valid()
