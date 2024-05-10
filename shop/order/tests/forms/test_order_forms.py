import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from order.forms import OrderForm  # noqa


@pytest.mark.django_db(transaction=False)
def test_order_form_initial_values_with_client(client, authenticated_user):
    data = {
        "first_name": "Name",
        "last_name": "Surname",
        "street": "Street",
        "city": "City",
        "postcode": "12345",
        "phone": "123456789",
        "email": "example@example.com",
        "delivery": 1,
    }

    client.force_login(authenticated_user)
    url = reverse("order")
    response = client.post(url, data)

    form = OrderForm(data)
    is_valid = form.is_valid()

    assert response.status_code == 200
    assert is_valid == response.context["form"].is_valid()
