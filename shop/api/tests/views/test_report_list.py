import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_user_can_view_report_list(client, authenticated_user, reports):
    expected_response = {
        "id": reports.id,
        "name": reports.name,
        "creation_date": reports.creation_date.strftime("%Y-%m-%d"),
        "status": reports.status,
        "parameters": reports.parameters,
    }
    response = client.get(reverse("reports-list"))
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0]["id"] == expected_response["id"]
    assert response_data[0]["name"] == expected_response["name"]
    assert response_data[0]["creation_date"] == expected_response["creation_date"]
    assert response_data[0]["status"] == expected_response["status"]
    assert response_data[0]["parameters"] == expected_response["parameters"]


@pytest.mark.django_db(transaction=False)
def test_return_error_if_unauthenticated_user_wants_to_view_report_list(client):
    client.force_authenticate(user=None)
    expected_response = {"detail": "Authentication credentials were not provided."}
    response = client.get(reverse("reports-list"))
    response_data = response.json()
    assert response.status_code == 403
    assert response_data == expected_response
