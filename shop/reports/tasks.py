from celery import shared_task
from order.models import Order
from .generate_report_xlsx import generate_xlsx_report
from .generate_report_pdf import (
    generate_pdf_report,
    save_report_to_file_pdf,
    filter_orders_by_date,
)


@shared_task
def generate_report_task(
    user_id, report_name, data_parameters, report_format, start_date, end_date
):
    orders = Order.objects.filter(buyer=user_id)

    for order in orders:
        filtered_orders = filter_orders_by_date(order, start_date, end_date)
        if report_format == "xlsx":
            for filtered_order in filtered_orders:
                generate_xlsx_report(filtered_order, report_name, data_parameters)

        elif report_format == "pdf":
            for filtered_order in filtered_orders:
                pdf_data = generate_pdf_report(filtered_order, data_parameters)
                save_report_to_file_pdf(
                    pdf_data, f"{report_name}_{filtered_order.id}", "pdf"
                )

    return "Generating reports completed."
