import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_company_user_can_view_products_sold(
    client, authenticated_company, order_item
):
    expected_response = {
        "id": order_item.id,
        "item": order_item.item.id,
        "price": str(order_item.price),
        "quantity": order_item.quantity,
    }
    response = client.get(reverse("products-sold-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["id"] == expected_response["id"]
    assert response_data[0]["item"] == expected_response["item"]
    assert response_data[0]["price"] == expected_response["price"]
    assert response_data[0]["quantity"] == expected_response["quantity"]


def test_return_error_if_unauthenticated_user_wants_to_view_products_sold(client):
    client.force_authenticate(user=None)
    expected_response = {"detail": "Authentication credentials were not provided."}
    response = client.get(reverse("products-sold-list"))
    response_data = response.json()
    assert response.status_code == 403
    assert response_data == expected_response


@pytest.mark.django_db(transaction=False)
def test_return_error_if_authenticated_user_is_not_company(client, authenticated_user):
    client.force_authenticate(user=authenticated_user)
    expected_response = {"detail": "No Company matches the given query."}
    response = client.get(reverse("user-products-list"))
    response_data = response.json()
    assert response.status_code == 404
    assert response_data == expected_response
