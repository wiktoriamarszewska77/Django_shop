import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa


@pytest.mark.django_db(transaction=False)
def test_unauthenticated_user_can_view_average_rating_products(client, review):
    expected_response = [{"product": review.product.id, "avg_rating": 5.0}]
    response = client.get(reverse("average-rating-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["product"] == expected_response[0]["product"]
