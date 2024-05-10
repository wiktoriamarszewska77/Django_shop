import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_authenticated_user_wants_to_view_summary_basket(
    authenticated_user, client
):
    user = authenticated_user
    client.force_login(user)

    response = client.get(reverse("basket_summary"))
    assert response.status_code == 200
    assert "basket_products" in response.context
    assert "quantities" in response.context
    assert "totals" in response.context
    assert "object_shipping" in response.context


@pytest.mark.django_db(transaction=False)
def test_unauthenticated_user_redirected_to_login_for_basket_summary(client):
    response = client.get(reverse("basket_summary"))
    assert response.status_code == 302
    assert response.url == reverse("login") + "?next=" + reverse("basket_summary")
