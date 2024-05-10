import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_redirects_get_all_reports_page(
    client, authenticated_user
):
    client.force_login(authenticated_user)
    url = reverse("reports_view")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_checks_whether_an_no_logged_user_who_wants_to_redirects_get_all_reports_page_is_redirected_to_login(
    client,
):
    url = reverse("reports_view")
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse("login") + "?next=" + reverse("reports_view")
