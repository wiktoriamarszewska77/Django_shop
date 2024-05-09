import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.models import User, Company  # noqa
from rest_framework.reverse import reverse  # noqa
from review.models import Review  # noqa
from products.models import Product  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_correct_data_create_review():
    user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
    company = Company.objects.create(user=user, nip=123456)

    product = Product.objects.create(
        seller=company, name="Test Product", price=20, stock_quantity=1
    )

    review = Review.objects.create(
        user=user, product=product, comment="Comment", rating=5
    )

    assert Review.objects.filter(id=review.id).exists()
    assert review.comment == "Comment"
    assert review.rating == 5
