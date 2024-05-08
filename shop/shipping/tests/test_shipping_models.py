import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User  # noqa
from shipping.models import Shipping  # noqa
from order.models import Order  # noqa
from rest_framework.reverse import reverse  # noqa
from shipping.models import Shipping  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_correct_data_create_shipping():
    shipping = Shipping.objects.create(
        name="Test", price=20, delivery_time="5 day", free_delivery=500
    )
    assert Shipping.objects.filter(id=shipping.id).exists()
    assert shipping.name == "Test"
    assert shipping.price == 20
    assert shipping.delivery_time == "5 day"
    assert shipping.free_delivery == 500
