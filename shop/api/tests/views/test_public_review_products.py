import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


def test_unregistered_user_can_view_all_review_products(client, review):
    expected_response = [
        {
            "id": review.id,
            "user": review.user.id,
            "product": review.product.id,
            "date": review.date.strftime("%Y-%m-%d"),
            "comment": review.comment,
            "rating": review.rating,
        }
    ]
    response = client.get(reverse("review-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["id"] == expected_response[0]["id"]
    assert response_data[0]["user"] == expected_response[0]["user"]
    assert response_data[0]["product"] == expected_response[0]["product"]
    assert response_data[0]["date"] == expected_response[0]["date"]
    assert response_data[0]["comment"] == expected_response[0]["comment"]
    assert response_data[0]["rating"] == expected_response[0]["rating"]


def test_unregistered_user_can_view_detail_review_product(client, review):
    expected_response = {
        "id": review.id,
        "user": review.user.id,
        "product": review.product.id,
        "date": review.date.strftime("%Y-%m-%d"),
        "comment": review.comment,
        "rating": review.rating,
    }
    response = client.get(reverse("review-detail", kwargs={"pk": review.pk}))
    response_data = response.json()
    assert response.status_code == 200
    for key, value in expected_response.items():
        assert response_data[key] == value
