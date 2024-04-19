import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.test import APIClient  # noqa
from model_bakery import baker  # noqa
from products.models import Product  # noqa
from users.models import Company  # noqa
from review.models import Review  # noqa
from django.contrib.auth import get_user_model  # noqa

User = get_user_model()  # noqa


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def company():
    return baker.make(Company)


@pytest.fixture
def product(company):
    return baker.make(Product, seller=company)


@pytest.fixture
def user():
    user = baker.make(User)
    return user


@pytest.fixture
def review(product, user):
    return baker.make(Review, product=product, user=user)


@pytest.fixture
def authenticated_user(client, user):
    client.force_authenticate(user=user)
    return user


@pytest.fixture
def authenticated_company(client, company):
    client.force_authenticate(user=company.user)
    return company
