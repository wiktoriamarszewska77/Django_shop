import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_user_can_view_products_ordered(
    client, authenticated_user, order_item
):
    expected_response = {
        "buyer": order_item.order.buyer.id,
        "street": order_item.order.street,
        "city": order_item.order.city,
        "date": order_item.order.date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        "delivery": order_item.order.delivery.id,
        "status": order_item.order.status,
    }
    response = client.get(reverse("products-ordered-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data["orders"]) == 1
    assert response_data["orders"][0]["buyer"] == expected_response["buyer"]
    assert response_data["orders"][0]["street"] == expected_response["street"]
    assert response_data["orders"][0]["city"] == expected_response["city"]
    assert response_data["orders"][0]["date"] == expected_response["date"]
    assert response_data["orders"][0]["delivery"] == expected_response["delivery"]
    assert response_data["orders"][0]["status"] == expected_response["status"]


@pytest.mark.django_db(transaction=False)
def test_return_error_if_unauthenticated_user_wants_to_view_products_ordered(client):
    client.force_authenticate(user=None)
    expected_response = {"detail": "Authentication credentials were not provided."}
    response = client.get(reverse("products-ordered-list"))
    response_data = response.json()
    assert response.status_code == 403
    assert response_data == expected_response
