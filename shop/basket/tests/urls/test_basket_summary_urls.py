import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_summary_basket_url_for_login_users(
    client, authenticated_user
):
    client.force_login(authenticated_user)
    response = client.get(reverse("basket_summary"))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_summary_basket_url_for_no_logged_users(client):
    response = client.get(reverse("basket_summary"))
    assert response.status_code == 302
    assert response.url == reverse("login") + "?next=" + reverse("basket_summary")
