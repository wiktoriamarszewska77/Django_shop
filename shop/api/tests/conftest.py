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
from shipping.models import Shipping  # noqa
from order.models import OrderItem, Order  # noqa
from reports.models import Report  # noqa
from django.core.files.uploadedfile import SimpleUploadedFile  # noqa
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


@pytest.fixture
def shipping():
    return baker.make(Shipping)


@pytest.fixture
def order(user, shipping):
    return baker.make(Order, buyer=user, delivery=shipping)


@pytest.fixture
def order_item(order, product):
    return baker.make(OrderItem, order=order, item=product)


@pytest.fixture
def reports(user):
    return baker.make(Report, user=user)


@pytest.fixture
def sample_file_pdf(reports):
    file_content = b"test content"
    file = SimpleUploadedFile("test.pdf", file_content, content_type="application/pdf")
    reports.file = file
    reports.save()
    yield reports
    reports.file.delete(save=False)
    reports.delete()


@pytest.fixture
def sample_file_xlsx(reports):
    file_content = b"test content"
    file = SimpleUploadedFile(
        "test.xlsx", file_content, content_type="application/xlsx"
    )
    reports.file = file
    reports.save()
    yield reports
    reports.file.delete(save=False)
    reports.delete()
