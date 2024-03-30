from celery import shared_task
from order.models import Order
from .generate_report_xlsx import generate_xlsx_report, save_report_to_file_xlsx
from .generate_report_pdf import (
    generate_pdf_report,
    save_report_to_file_pdf,
    filter_orders_by_date,
)
from .models import Report


@shared_task
def generate_report_task(
    user_id, report_name, data_parameters, report_format, start_date, end_date
):
    orders = Order.objects.filter(buyer=user_id)
    report_status = "pending"

    try:
        for order in orders:
            filtered_orders = filter_orders_by_date(order, start_date, end_date)
            if report_format == "xlsx":
                for filtered_order in filtered_orders:
                    wb = generate_xlsx_report(
                        filtered_order, report_name, data_parameters
                    )
                    save_report_to_file_xlsx(
                        wb, f"{report_name}_{filtered_order.id}", "xlsx"
                    )

            elif report_format == "pdf":
                for filtered_order in filtered_orders:
                    pdf_data = generate_pdf_report(filtered_order, data_parameters)
                    save_report_to_file_pdf(
                        pdf_data, f"{report_name}_{filtered_order.id}", "pdf"
                    )
        report_status = "finished"
    except Exception:
        report_status = "error"

    Report.objects.filter(name=report_name).update(status=report_status)
    return "Generating reports completed."
