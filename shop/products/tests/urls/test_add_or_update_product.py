import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from users.models import User  # noqa


@pytest.mark.django_db(transaction=False)
def test_redirects_the_user_when_he_wants_to_go_to_the_add_or_update_product_page_and_he_is_not_company(
    client,
):
    user = User.objects.create(username="test", first_name="Name")
    client.force_login(user)

    url = reverse("add-product")
    response = client.get(url)

    assert response.status_code == 302
