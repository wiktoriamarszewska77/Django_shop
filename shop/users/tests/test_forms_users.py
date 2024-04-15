import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from users.forms import RegisterForm, CompanyForm, UserProfileForm  # noqa
from users.models import User  # noqa


@pytest.mark.django_db
@pytest.mark.parametrize(
    "form_data",
    [
        {
            "username": "testuser1",
            "email": "email1@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        },
        {
            "username": "testuser2",
            "email": "email2@example.com",
            "password1": "WeakPass!@#",
            "password2": "WeakPass!@#",
        },
    ],
)
def test_register_form_validation_return_true_for_correctly_entered_data(form_data):
    form = RegisterForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize("password", ["short", "1234567", "abc123", "87654321"])
def test_registration_form_should_return_error_when_password_is_too_short_or_password_is_numbers(
    password,
):
    form_data = {
        "username": "testuser",
        "email": "email@example.pl",
        "password1": password,
        "password2": password,
    }
    form = RegisterForm(data=form_data)
    assert not form.is_valid()


@pytest.mark.django_db
@pytest.mark.parametrize("nip, expected_valid", [("1234567890", True), ("12345", True)])
def test_company_form_valid(nip, expected_valid):
    format_data = {"nip": nip}
    form = CompanyForm(data=format_data)
    assert form.is_valid() == expected_valid


@pytest.mark.django_db
def test_user_form_profile_return_true_for_valid_data():
    user = User.objects.create(username="testuser")
    form_data = {
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "phone": "123456789",
        "address": "Test Address",
        "image": "test.jpg",
    }
    form = UserProfileForm(instance=user, data=form_data)
    assert form.is_valid()
