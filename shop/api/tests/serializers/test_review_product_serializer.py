import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
from api.serializers import ReviewProductSerializer  # noqa
from review.models import Review  # noqa
from datetime import datetime  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_validate_data_review_product_serializer(product, user):
    review_data = {
        "user": user.id,
        "product": product.id,
        "date": "2022-01-01",
        "comment": "Test comment",
        "rating": 5,
    }

    serializer = ReviewProductSerializer(data=review_data)
    assert serializer.is_valid()

    new_review = serializer.save()
    assert isinstance(new_review, Review)
    assert new_review.user_id == user.id
    assert new_review.product_id == product.id
    assert new_review.comment == "Test comment"
    assert new_review.rating == 5


@pytest.mark.django_db(transaction=False)
def test_return_error_when_missing_required_field_for_review_product_serializer(
    product, user
):
    review_data = {"user": user.id, "product": product.id, "rating": 5}

    serializer = ReviewProductSerializer(data=review_data)
    assert not serializer.is_valid()
    errors = serializer.errors
    assert "comment" in errors
    assert errors["comment"][0] == "This field is required."
