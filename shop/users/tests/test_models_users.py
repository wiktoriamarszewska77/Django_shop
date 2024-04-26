import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa
import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from .factories import UserFactory, CompanyFactory  # noqa


@pytest.mark.django_db
def test_user_models_save():
    user = UserFactory
    assert user.username
    assert user.phone
    assert user.address
    assert user.password


@pytest.mark.django_db
def test_company_models_save():
    company = CompanyFactory
    assert company.user
    assert company.name
    assert company.address
    assert company.nip
