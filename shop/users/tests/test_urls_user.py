import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from django.urls import reverse  # noqa
from users.models import User  # noqa


@pytest.mark.django_db
def test_url_return_true_for_redirects_to_the_register_page(client):
    url = reverse("register")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_return_true_for_redirects_to_the_login_page(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_return_true_redirects_to_the_profile_page_for_logged_in_users(client):
    user = User.objects.create(username="Test", password="TestPassword123!")
    client.force_login(user)

    response = client.get(reverse("profile"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_return_true_redirects_to_the_logout_page_for_logged_in_users(client):
    user = User.objects.create(username="Test", password="TestPassword123!")
    client.force_login(user)

    url = reverse("logout")
    response = client.post(url)
    assert response.status_code == 200
