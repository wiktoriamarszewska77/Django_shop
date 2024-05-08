import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_when_logged_users_wants_to_enter_payment_view(
    client, authenticated_user, order
):
    client.force_login(authenticated_user)
    response_get = client.get(reverse("payment_view", kwargs={"order_id": order.id}))
    assert response_get.status_code == 200

    assert response_get.status_code == 200

    assert "order" in response_get.context
    assert response_get.context["order"] == order

    response_post = client.post(
        reverse("payment_view", kwargs={"order_id": order.id}),
        {"action": "mark_as_paid"},
    )

    order.refresh_from_db()
    assert order.status == "paid"

    assert response_post.status_code == 302
    assert response_post.url == reverse("order_summary")
