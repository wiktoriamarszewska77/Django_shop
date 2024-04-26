import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_get_all_products_url_for_unauthenticated_user(
    client,
):
    client.force_authenticate(user=None)
    response = client.get(reverse("get-products-list"))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_get_detail_product_url_for_unauthenticated_user(
    client, product
):
    client.force_authenticate(user=None)
    response = client.get(reverse("get-products-detail", kwargs={"pk": product.pk}))
    assert response.status_code == 200
