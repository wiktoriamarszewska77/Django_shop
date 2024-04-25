import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa

import pytest  # noqa
from api.serializers import NewReportSerializer  # noqa
import json  # noqa


@pytest.mark.django_db(transaction=False)
def test_return_true_for_validate_data_new_report_serializer():
    parameters = {"data_parameters": ["order.id", "order.buyer", "order.street"]}

    data = {
        "end_date": "2024-04-09",
        "start_date": "2024-03-05",
        "report_format": "pdf",
        "data_parameters": json.dumps(parameters),
        "report_name": "Test Report",
    }

    serializer = NewReportSerializer(data=data)
    assert serializer.is_valid()


@pytest.mark.django_db(transaction=False)
def test_return_error_when_missing_required_field_for_new_report_serializer():
    parameters = {"data_parameters": ["order.id", "order.buyer", "order.street"]}

    data = {
        "end_date": "2024-04-09",
        "start_date": "2024-03-05",
        "report_format": "pdf",
        "data_parameters": json.dumps(parameters),
    }

    serializer = NewReportSerializer(data=data)
    assert not serializer.is_valid()
    errors = serializer.errors
    assert "report_name" in errors
    assert errors["report_name"][0] == "This field is required."
