from celery import shared_task
from .generate_report_xlsx import generate_xlsx_report
from .generate_report_pdf import (
    generate_pdf_report,
    filter_orders_by_date,
)
from .models import Report
from django.core.files.base import ContentFile


@shared_task
def generate_report_task(
    user_id, report_id, data_parameters, report_format, start_date, end_date
):
    report = Report.objects.get(id=report_id)
    orders = filter_orders_by_date(start_date, end_date, user_id)

    if report_format == "pdf":
        pdf_data = generate_pdf_report(orders, data_parameters)
        report.file.save(f"{report.name}.pdf", ContentFile(pdf_data))
    elif report_format == "xlsx":
        wb = generate_xlsx_report(orders, data_parameters)
        report.file.save(f"{report.name}.xlsx", ContentFile(wb))

    report.status = "finished"
    report.save()

    return "Generating report completed."
