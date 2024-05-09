import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_redirects_create_review_page(
    client, authenticated_user, product
):
    client.force_login(authenticated_user)
    url = reverse("add_review", kwargs={"product_id": product.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_checks_whether_no_logged_user_is_redirected_to_the_login_page_if_he_tries_to_enter_the_add_review_product_page(
    client, product
):
    url = reverse("add_review", kwargs={"product_id": product.id})
    response = client.get(url)
    assert response.status_code == 302
