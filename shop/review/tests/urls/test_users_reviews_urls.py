import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from review.models import Review  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_redirects_all_review_page_of_which_he_is_the_author(
    client, authenticated_user, product
):
    client.force_login(authenticated_user)
    review1 = Review.objects.create(user=authenticated_user, product=product, rating=3)
    review2 = Review.objects.create(user=authenticated_user, product=product, rating=4)

    url = reverse("user_reviews")
    response = client.get(url)
    assert response.status_code == 200
    assert review1 in response.context["reviews"]
    assert review2 in response.context["reviews"]


@pytest.mark.django_db(transaction=False)
def test_checks_whether_no_logged_user_is_redirected_to_the_login_page_if_he_tries_to_enter_the_all_review_page_of_which_he_is_the_author(
    client, product
):
    url = reverse("user_reviews")
    response = client.get(url)
    assert response.status_code == 302
