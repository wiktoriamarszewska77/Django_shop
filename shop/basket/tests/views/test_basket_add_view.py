import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_user_add_product_to_basket(
    client, authenticated_user, product
):
    user = authenticated_user
    client.force_login(user)

    response = client.post(
        reverse("basket_add"),
        {"action": "post", "product_id": product.id, "product_qty": 1},
    )
    assert response.status_code == 200
    assert "qty" in response.json()
    assert response.json()["qty"] == 1
