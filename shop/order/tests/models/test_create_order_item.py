import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from api.tests.conftest import *  # noqa
from order.models import OrderItem  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_correct_data_create_order_item(product, order):
    order_item = OrderItem.objects.create(
        order=order, item=product, price=product.price, quantity=2
    )

    assert OrderItem.objects.filter(id=order_item.id).exists()
