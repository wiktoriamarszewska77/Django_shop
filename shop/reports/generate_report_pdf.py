from reportlab.pdfgen import canvas
from io import BytesIO
from order.models import Order
from django.conf import settings
import os


def generate_pdf_report(order, data_parameters):
    report_data = []

    for param in data_parameters:
        if param == "order.id":
            report_data.append({"param": "Order ID", "value": order.id})
        elif param == "order.buyer":
            report_data.append({"param": "Order Buyer", "value": order.buyer})
        elif param == "order.street":
            report_data.append({"param": "Order Street", "value": order.street})
        elif param == "order.city":
            report_data.append({"param": "Order City", "value": order.city})
        elif param == "order.postcode":
            report_data.append({"param": "Order Postcode", "value": order.postcode})
        elif param == "order.date":
            report_data.append({"param": "Order Date", "value": order.date})
        elif param == "order.delivery.name":
            report_data.append(
                {"param": "Order Delivery Name", "value": order.delivery.name}
            )
        elif param == "order.delivery.price":
            report_data.append(
                {"param": "Order Delivery Price", "value": order.delivery.price}
            )
        elif param == "order.status":
            report_data.append({"param": "Order Status", "value": order.status})

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    y_position = 800
    for data in report_data:
        pdf.drawString(100, y_position, f"{data['param']}: {data['value']}")
        y_position -= 20

    pdf.save()
    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data


def filter_orders_by_date(order, start_date, end_date):
    return Order.objects.filter(buyer=order.buyer, date__range=[start_date, end_date])


def save_report_to_file_pdf(report_data, report_name, report_format):
    user_folder = os.path.join(settings.MEDIA_ROOT, "reports")
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    filename = f"{report_name}.{report_format}"
    file_path = os.path.join(user_folder, filename)

    with open(file_path, "wb") as file:
        file.write(report_data)
