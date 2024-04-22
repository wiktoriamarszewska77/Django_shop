# import os  # noqa
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")  # noqa
#
# import django  # noqa
#
# django.setup()  # noqa
#
# import pytest  # noqa
# from rest_framework.reverse import reverse  # noqa
# from rest_framework import status  # noqa
#
#
# @pytest.mark.django_db(transaction=False)
# def test_authenticated_user_can_generate_new_report(client, authenticated_user, order):
#     url = reverse("new-report-list")
#     data = {
#         "end_date": "2024-04-09",
#         "start_date": "2024-03-05",
#         "report_format": "pdf",
#         "data_parameters": ["order.id", "order.buyer"],
#         "report_name": "Test Report"
#     }
#     response = client.post(url, data)
#
#     assert response.status_code == status.HTTP_200_OK
#     assert "Generating a report" in response.data["message"]
