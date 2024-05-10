import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User  # noqa
from shipping.models import Shipping  # noqa


@pytest.mark.django_db(transaction=False)
def test_checks_whether_the_str_function_for_shipping_is_correctly():
    shipping = Shipping.objects.create(
        name="Test", price=5.99, delivery_time="5-7 day", free_delivery=100
    )

    expected_str = "Test\nprice: 5.99\nDelivery time: 5-7 day\nFree delivery: 100"
    assert str(shipping) == expected_str
