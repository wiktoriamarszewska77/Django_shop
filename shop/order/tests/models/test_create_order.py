import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User  # noqa
from shipping.models import Shipping  # noqa
from order.models import Order  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_correct_data_create_order():
    user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
    shipping = Shipping.objects.create(
        name="Standard Shipping", price=10.00, free_delivery=300
    )

    order = Order.objects.create(
        buyer=user,
        street="Test Street",
        city="Test City",
        postcode="12345",
        delivery=shipping,
        status="expectancy",
    )

    assert Order.objects.filter(id=order.id).exists()
