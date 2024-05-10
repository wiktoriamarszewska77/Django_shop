import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User  # noqa
from shipping.models import Shipping  # noqa
from order.models import Order  # noqa


@pytest.mark.django_db(transaction=False)
def test_checks_whether_the_str_function_for_order_is_correctly():
    user = User.objects.create(username="User", first_name="John", last_name="Ame")
    shipping = Shipping.objects.create(name="Standard", price=10, free_delivery=300)
    order = Order.objects.create(
        buyer=user,
        street="Test Street",
        city="Test City",
        postcode="12345",
        delivery=shipping,
    )

    expected_str = f"Order placed {order.date.strftime('%Y-%m-%d %H:%M')} by {user.first_name} {user.last_name} shipping {shipping.price}"
    assert str(order) == expected_str
