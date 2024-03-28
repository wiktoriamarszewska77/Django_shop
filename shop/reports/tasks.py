import os
from celery import shared_task
from django.conf import settings
from .models import Order
from .utils import generate_payment_report


@shared_task
def generate_report_task(user_id):
    # started generating report %s, logging -> f'{}' , %s
    orders = Order.objects.filter(buyer=user_id)

    for order in orders:
        pdf_data = generate_payment_report(order)

        user_folder_name = f"reports_{order.buyer.id}"
        user_folder = os.path.join(settings.MEDIA_ROOT, user_folder_name)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        filename = f"order_{order.id}_report.pdf"
        file_path = os.path.join(user_folder, filename)

        with open(file_path, "wb") as file:
            file.write(pdf_data)

    return "Generating a report."
