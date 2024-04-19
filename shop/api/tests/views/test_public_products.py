import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from django.contrib.auth.models import User  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_unregistered_user_can_view_all_products(client, product):
    expected_response = [
        {
            "seller": product.seller.id,
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
    ]

    response = client.get(reverse("get-products-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["seller"] == expected_response[0]["seller"]
    assert response_data[0]["name"] == expected_response[0]["name"]
    assert response_data[0]["brand"] == expected_response[0]["brand"]
    assert response_data[0]["category"] == expected_response[0]["category"]
    assert response_data[0]["price"] == expected_response[0]["price"]
    assert response_data[0]["data_added"] == expected_response[0]["data_added"]
    assert response_data[0]["description"] == expected_response[0]["description"]
    assert response_data[0]["stock_quantity"] == expected_response[0]["stock_quantity"]
    assert response_data[0]["available"] == expected_response[0]["available"]


def test_unregistered_user_can_view_detail_product(client, product):
    expected_response = {
        "seller": product.seller.id,
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
        "price": str(product.price),
        "data_added": product.data_added.strftime("%d-%m-%Y %H:%M:%S"),
        "description": product.description,
        "stock_quantity": product.stock_quantity,
        "available": product.available,
    }

    response = client.get(reverse("get-products-detail", kwargs={"pk": product.pk}))
    response_data = response.json()

    assert response.status_code == 200
    for key, value in expected_response.items():
        assert response_data[key] == value
