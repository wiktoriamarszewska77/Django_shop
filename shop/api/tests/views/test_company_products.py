import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_company_user_can_view_products_for_sell(
    client, authenticated_company, product
):
    expected_response = {
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
        "price": str(product.price),
        "data_added": product.data_added.strftime("%d-%m-%Y %H:%M:%S"),
        "description": product.description,
        "image": product.image,
        "stock_quantity": product.stock_quantity,
        "available": product.available,
    }
    response = client.get(reverse("user-products-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["name"] == expected_response["name"]
    assert response_data[0]["brand"] == expected_response["brand"]
    assert response_data[0]["category"] == expected_response["category"]
    assert response_data[0]["price"] == expected_response["price"]
    assert response_data[0]["description"] == expected_response["description"]
    assert response_data[0]["stock_quantity"] == expected_response["stock_quantity"]
    assert response_data[0]["available"] == expected_response["available"]


@pytest.mark.django_db(transaction=False)
def test_return_error_if_unauthenticated_user_wants_to_view_products_for_sell(client):
    client.force_authenticate(user=None)
    expected_response = {"detail": "Authentication credentials were not provided."}
    response = client.get(reverse("user-products-list"))
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
