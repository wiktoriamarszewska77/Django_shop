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
def test_return_true_when_users_wants_to_redirects_detail_product_page(client):
    user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
    company = Company.objects.create(user=user, nip=123456)
    product = Product.objects.create(
        seller=company, name="test1", price=20, stock_quantity=1
    )

    url = reverse("detail-product", args=[product.pk])
    response = client.get(url)

    assert response.status_code == 200
