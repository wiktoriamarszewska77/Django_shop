import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from django.urls import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_authenticated_user_enter_order_view(
    client, authenticated_user
):
    client.force_login(authenticated_user)
    form_data = {"street": "Street", "city": "City", "postcode": "12345"}
    response_get = client.get(reverse("order"))
    assert response_get.status_code == 200
    response_post = client.post(reverse("order"), form_data)
    assert response_post.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_checks_whether_it_redirects_to_page_login_when_not_authenticated_user_enter_order_view(
    client,
):
    response_get = client.get(reverse("order"))
    assert response_get.status_code == 302
