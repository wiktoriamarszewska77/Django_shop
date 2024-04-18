import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.test import APIClient  # noqa
from model_bakery import baker  # noqa
from products.models import Product  # noqa
from users.models import Company  # noqa


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def company():
    return baker.make(Company)


@pytest.fixture
def product(company):
    return baker.make(Product, seller=company)
