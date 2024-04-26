import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_actions_products_url_for_auth_company(
    client, authenticated_company
):
    response = client.get(reverse("actions-products-list"))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_return_errors_when_redirects_to_the_actions_products_url_for_auth_not_company(
    client, authenticated_user
):
    expected_response = {"detail": "You do not have permission to perform this action."}
    response = client.get(reverse("actions-products-list"))
    response_data = response.json()
    assert response.status_code == 403
    assert response_data == expected_response


@pytest.mark.django_db(transaction=False)
def test_return_errors_when_redirects_to_the_actions_products_url_for_not_auth_user(
    client,
):
    client.force_authenticate(user=None)
    response = client.get(reverse("actions-products-list"))
    expected_response = {"detail": "Authentication credentials were not provided."}

    response_data = response.json()
    assert response.status_code == 403
    assert response_data == expected_response
