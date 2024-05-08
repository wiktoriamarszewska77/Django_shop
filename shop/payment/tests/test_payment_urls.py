import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_redirects_payment_page(
    client, authenticated_user, order
):
    client.force_login(authenticated_user)
    url = reverse("payment_view", kwargs={"order_id": order.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_return_error_when_no_logged_users_wants_to_redirects_payment_page(
    client, order
):
    url = reverse("payment_view", kwargs={"order_id": order.id})
    response = client.get(url)
    assert response.status_code == 302
