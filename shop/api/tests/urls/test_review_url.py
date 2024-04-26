import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_redirects_to_the_review_url_for_unauthenticated_user(client):
    client.force_authenticate(user=None)
    response = client.get(reverse("review-list"))
    assert response.status_code == 200
