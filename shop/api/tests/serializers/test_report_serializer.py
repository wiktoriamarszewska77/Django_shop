import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from api.serializers import ReportSerializer  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_validate_data_report_serializer(reports):
    data = {
        "id": reports.id,
        "name": reports.name,
        "creation_date": reports.creation_date,
        "status": reports.status,
        "parameters": reports.parameters,
    }

    serializer = ReportSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db(transaction=False)
def test_return_error_when_missing_required_field_for_report_serializer(reports):
    data = {
        "id": reports.id,
        "creation_date": reports.creation_date,
        "status": reports.status,
        "parameters": reports.parameters,
    }

    serializer = ReportSerializer(data=data)
    assert not serializer.is_valid()
    errors = serializer.errors
    assert "name" in errors
    assert errors["name"][0] == "This field is required."
