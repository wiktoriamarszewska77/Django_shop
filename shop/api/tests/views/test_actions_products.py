import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
from products.models import Product  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_company_can_create_product(client, authenticated_company):
    url = reverse("actions-products-list")
    data = {
        "name": "Test Product",
        "brand": "Test Brand",
        "category": "electronics",
        "price": "100.00",
        "description": "Test description",
        "stock_quantity": 10,
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Product.objects.filter(name="Test Product").exists()


@pytest.mark.django_db(transaction=False)
def test_authenticated_company_can_update_product(
    client, authenticated_company, product
):
    url = reverse("actions-products-detail", kwargs={"pk": product.id})
    data = {
        "name": "Updated Product",
        "brand": "Test Brand",
        "category": "electronics",
        "price": "100.00",
        "description": "Test description",
        "stock_quantity": 10,
    }
    response = client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    product.refresh_from_db()
    assert product.name == "Updated Product"


@pytest.mark.django_db(transaction=False)
def test_authenticated_company_can_delete_product(
    client, authenticated_company, product
):
    url = reverse("actions-products-detail", kwargs={"pk": product.id})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
