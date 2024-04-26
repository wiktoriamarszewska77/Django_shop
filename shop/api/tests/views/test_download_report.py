import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from rest_framework import status  # noqa
import tempfile  # noqa


@pytest.mark.django_db(transaction=False)
def test_authenticated_user_can_report_download_pdf(
    client, authenticated_user, reports, sample_file_pdf
):
    tempfile.NamedTemporaryFile(delete=False)
    client.force_authenticate(user=authenticated_user)
    url = f"/api/download-report-pdf/{reports.id}"
    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_200_OK
    assert response["Content-Type"] == "application/pdf"
    assert (
        f'attachment; filename="{reports.name}.pdf"' in response["Content-Disposition"]
    )


@pytest.mark.django_db(transaction=False)
def test_return_error_when_authenticated_user_did_not_find_report_to_download_pdf(
    client, authenticated_user, reports, sample_file_pdf
):
    tempfile.NamedTemporaryFile(delete=False)
    client.force_authenticate(user=authenticated_user)
    url = f"/api/download-report-pdf/{reports.id + 1}"
    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["error"] == "Report not found"


@pytest.mark.django_db(transaction=False)
def test_authenticated_user_can_report_download_xlsx(
    client, authenticated_user, reports, sample_file_xlsx
):
    tempfile.NamedTemporaryFile(delete=False)
    client.force_authenticate(authenticated_user)
    url = f"/api/download-report-xlsx/{reports.id}"
    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_200_OK
    assert response["Content-Type"] == "application/xlsx"
    assert (
        f'attachment; filename="{reports.name}.xlsx"' in response["Content-Disposition"]
    )


@pytest.mark.django_db(transaction=False)
def test_return_error_when_authenticated_user_did_not_find_report_to_download_xlsx(
    client, authenticated_user, reports, sample_file_xlsx
):
    tempfile.NamedTemporaryFile(delete=False)
    client.force_authenticate(user=authenticated_user)
    url = f"/api/download-report-pdf/{reports.id + 1}"
    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["error"] == "Report not found"
