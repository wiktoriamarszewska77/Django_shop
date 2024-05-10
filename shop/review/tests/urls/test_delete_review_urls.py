import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from review.models import Review  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_redirects_delete_review_page_and_are_the_authors(
    client, authenticated_user, product
):
    client.force_login(authenticated_user)
    review = Review.objects.create(user=authenticated_user, product=product, rating=5)

    url = reverse("delete_review", args=[review.pk])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_return_error_when_logged_users_wants_to_redirects_delete_review_page_and_not_the_authors(
    client, authenticated_user
):
    client.force_login(authenticated_user)

    url = reverse("delete_review", args=[1])
    response = client.get(url)
    assert response.status_code == 404


@pytest.mark.django_db(transaction=False)
def test_checks_whether_no_logged_user_is_redirected_to_the_login_page_if_he_tries_to_enter_the_delete_review_product_page(
    client, product
):
    url = reverse("delete_review", args=[1])
    response = client.get(url)
    assert response.status_code == 302
