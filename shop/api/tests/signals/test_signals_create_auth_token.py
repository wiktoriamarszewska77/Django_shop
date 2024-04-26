import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.authtoken.models import Token  # noqa
from users.models import User  # noqa


@pytest.mark.django_db(transaction=False)
def test_checks_if_signal_creates_token_when_register_user():
    user = User.objects.create(
        username="test123", email="test@example.com", password="TestPassword123!"
    )
    token_exists = Token.objects.filter(user=user).exists()
    assert token_exists
