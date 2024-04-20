import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
import json  # noqa
from rest_framework.authtoken.models import Token  # noqa
from users.models import User  # noqa


def test_authentication_user_login_view(client):
    username = "test"
    password = "TestPassword123!"

    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)

    response = client.post(
        reverse("loginup"), data={"username": username, "password": password}
    )

    if user.check_password(password):
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["message"] == "Login Successfully"
        assert "token" in response_data
        assert response_data["token"] == token.key
    else:
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["message"] == "Invalid username or password"
