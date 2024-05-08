import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User  # noqa
from shipping.models import Shipping  # noqa
from order.models import Order  # noqa


@pytest.mark.django_db(transaction=False)
def test_checks_whether_the_property_function_for_order_address_is_correctly():
    user = User.objects.create(username="testuser")
    shipping = Shipping.objects.create(name="Standard", price=10, free_delivery=300)
    order = Order.objects.create(
        buyer=user,
        street="Test Street",
        city="Test City",
        postcode="12345",
        delivery=shipping,
    )

    expected_address = "Test Street, Test City 12345"
    assert order.address == expected_address
