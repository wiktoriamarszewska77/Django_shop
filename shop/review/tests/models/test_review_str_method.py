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
def test_checks_whether_the_str_function_for_review_is_correctly():
    user = User.objects.create(username="testuser", first_name="John", last_name="Doe")
    company = Company.objects.create(user=user, nip=123456)

    product = Product.objects.create(
        seller=company, name="Test Product", price=20, stock_quantity=1
    )

    review = Review.objects.create(
        user=user, product=product, comment="Comment", rating=5
    )

    expected_str = f"Review by {user} for {product} and rating {review.rating}"
    assert str(review) == expected_str
