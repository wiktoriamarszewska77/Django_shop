import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from reports.forms import NewReportForm  # noqa


@pytest.mark.django_db(transaction=True)
def test_return_true_when_new_report_form_valid():
    form_data = {
        "data_parameters": ["order.id", "order.buyer"],
        "report_format": "pdf",
        "start_date": "2022-01-01",
        "end_date": "2022-01-31",
        "report_name": "Test Report",
    }
    form = NewReportForm(data=form_data)
    assert form.is_valid()


@pytest.mark.django_db(transaction=True)
def test_return_error_when_new_report_form_invalid():
    form_data = {
        "report_format": "pdf",
        "start_date": "2022-01-31",
        "end_date": "2022-01-01",
        "report_name": "Test Report",
    }
    form = NewReportForm(data=form_data)
    assert not form.is_valid()
