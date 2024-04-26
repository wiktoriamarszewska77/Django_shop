import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.serializers import OrderItemSerializer, OrderSerializer  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_validate_data_order_serializer(order):
    data = {
        "buyer": order.buyer.id,
        "street": order.street,
        "city": order.city,
        "postcode": order.postcode,
        "date": order.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "delivery": order.delivery.id,
        "status": order.status,
    }

    serializer = OrderSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db(transaction=False)
def test_return_true_for_validate_data_order_item_serializer(order_item, product):
    data = {
        "id": order_item.id,
        "item": product.id,
        "price": order_item.price,
        "quantity": order_item.quantity,
    }

    serializer = OrderItemSerializer(data=data)
    assert serializer.is_valid()
