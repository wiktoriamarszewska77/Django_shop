import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from products.models import Product  # noqa
from users.models import User, Company  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_users_wants_to_redirects_products_list_page(client):
    user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
    company = Company.objects.create(user=user, nip=123456)
    product1 = Product.objects.create(
        seller=company, name="test1", price=20, stock_quantity=1
    )
    product2 = Product.objects.create(
        seller=company, name="test2", price=5, stock_quantity=1
    )

    url = reverse("products-list")
    response = client.get(url)

    assert response.status_code == 200
    assert product1 in response.context["products"]
    assert product2 in response.context["products"]
