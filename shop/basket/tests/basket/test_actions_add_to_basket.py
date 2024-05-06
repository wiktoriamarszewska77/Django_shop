import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from basket.basket import Basket  # noqa


@pytest.mark.django_db(transaction=False)
def test_checks_whether_the_product_is_added_to_the_basket(client, product):
    request = client.request().wsgi_request
    basket = Basket(request)

    assert len(basket) == 0
    basket.add(product_id=product.id, quantity=1)
    assert len(basket) == 1
    assert basket.basket_total() == product.price
