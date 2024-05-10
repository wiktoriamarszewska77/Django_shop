import os  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa

import django  # noqa

django.setup()  # noqa
import pytest  # noqa
from rest_framework.reverse import reverse  # noqa
from api.tests.conftest import *  # noqa
from django.core.files.uploadedfile import SimpleUploadedFile  # noqa
from reports.models import Report  # noqa
from users.models import User  # noqa


@pytest.mark.django_db(transaction=True)
def test_checks_the_correctness_of_the_report_model_creation():
    user = User.objects.create(username="test_user")
    file_content = b"Test file content"
    file = SimpleUploadedFile("test_report.pdf", file_content)

    report = Report.objects.create(
        user=user,
        name="Test Report",
        file=file,
        parameters={"param1": "value1", "param2": "value2"},
    )

    assert report.user == user
    assert report.name == "Test Report"
    assert report.file.read() == file_content
