import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from django.urls import reverse  # noqa
from django.contrib.auth.models import User  # noqa
from users.models import User, Company  # noqa


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data",
    [
        {
            "username": "Test",
            "email": "example@example.pl",
            "password1": "TestPassword123!",
            "password2": "TestPassword123!",
        },
        {
            "username": "Test2",
            "email": "example2@example.pl",
            "password1": "TestPassword123!",
            "password2": "TestPassword123!",
            "nip": "1234556778",
        },
    ],
)
def test_register_view_return_true_when_data_sent_is_correct(client, data):
    response = client.post(reverse("register"), data=data)

    registered_user = User.objects.get(username=data["username"])
    assert response.status_code == 302
    assert registered_user.username == data["username"]
    assert registered_user.email == data["email"]
    if "nip" in data:
        assert registered_user.company.nip == data["nip"]
    assert User.objects.filter(username=data["username"]).exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data",
    [
        {
            "username": "Test",
            "email": "example@example.pl",
            "password1": "TestPassword123!",
        },
        {
            "username": "Test2",
            "email": "example2@example.pl",
            "password1": "Test",
            "password2": "Test",
            "nip": "12345567731338",
        },
    ],
)
def test_register_view_return_false_when_data_sent_is_incorrect(client, data):
    response = client.post(reverse("register"), data)
    assert response.status_code == 200
    assert not User.objects.filter(username=data["username"]).exists()


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data",
    [
        {
            "is_company": False,
            "username": "username",
            "email": "email@example.pl",
            "first_name": "name",
            "last_name": "surname",
            "phone": "123456789",
            "address": "Address",
        },
        {
            "is_company": True,
            "username": "company",
            "email": "company@example.pl",
            "first_name": "company_name",
            "last_name": "company_surname",
            "phone": "231456789",
            "address": "Address_company",
            "nip": "1234556778",
        },
    ],
)
def test_profile_view_return_true_when_data_sent_is_correct(client, data):
    if data["is_company"]:
        user = User.objects.create(username=data["username"])
        Company.objects.create(user=user, nip=data["nip"])
    else:
        user = User.objects.create(username=data["username"])

    client.force_login(user)

    response = client.post(reverse("profile"), data)
    assert response.status_code == 302

    user.refresh_from_db()
    assert user.username == data["username"]
    assert user.email == data["email"]
    assert user.first_name == data["first_name"]
    assert user.last_name == data["last_name"]
    assert user.phone == data["phone"]
    assert user.address == data["address"]

    if data["is_company"]:
        assert user.company.nip == data["nip"]


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data, expected_status",
    [
        (
            {
                "is_company": False,
                "username": "username",
                "email": "email",
                "first_name": "name",
                "last_name": "surname",
                "phone": "12345678913333",
                "address": "Address",
            },
            200,
        ),
        (
            {
                "is_company": True,
                "username": "company",
                "email": "company",
                "first_name": "company_name",
                "last_name": "company_surname",
                "phone": "23145678913",
                "address": "Address_company",
                "nip": "#451",
            },
            200,
        ),
    ],
)
def test_profile_view_return_status_code_for_incorrect_data(
    client, data, expected_status
):
    if data["is_company"]:
        user = User.objects.create(username=data["username"])
        Company.objects.create(user=user, nip=data["nip"])
    else:
        user = User.objects.create(username=data["username"])

    client.force_login(user)

    response = client.post(reverse("profile"), data)
    assert response.status_code == expected_status
