from openpyxl import Workbook
from openpyxl.styles import Alignment
import os
from django.conf import settings


def generate_xlsx_report(order, report_name, data_parameters):
    wb = Workbook()
    ws = wb.active

    headers_data = {
        "order.id": ("Order ID", order.id),
        "order.buyer": ("Order Buyer", order.buyer.username),
        "order.street": ("Order Street", order.street),
        "order.city": ("Order City", order.city),
        "order.postcode": ("Order Postcode", order.postcode),
        "order.date": ("Order Date", order.date.replace(tzinfo=None)),
        "order.delivery.name": ("Order Delivery Name", order.delivery.name),
        "order.delivery.price": ("Order Delivery Price", order.delivery.price),
        "order.status": ("Order Status", order.status),
    }

    row = 1
    for param in data_parameters:
        if param in headers_data:
            header, value = headers_data[param]
            ws.cell(1, row, header).alignment = Alignment(horizontal="center")
            ws.cell(2, row, value)
            row += 1

    return wb


def save_report_to_file_xlsx(report_data, report_name, report_format):
    user_folder = os.path.join(settings.MEDIA_ROOT, "reports")
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    filename = f"{report_name}.{report_format}"
    file_path = os.path.join(user_folder, filename)

    report_data.save(file_path)
    return file_path
