from celery import shared_task
from .generators import generate_pdf_report, generate_xlsx_report, filter_orders_by_date
from .models import Report
from django.core.files.base import ContentFile
import sentry_sdk


@shared_task
def generate_report_task(
    user_id, report_id, data_parameters, report_format, start_date, end_date
):
    try:
        report = Report.objects.get(id=report_id)
        orders = filter_orders_by_date(start_date, end_date, user_id)

        print(data_parameters)
        sentry_sdk.set_context(
            "task_info",
            {
                "user_id": user_id,
                "report_id": report_id,
                "report_format": report_format,
                "start_date": start_date,
                "end_date": end_date,
            },
        )

        if report_format == "pdf":
            pdf_data = generate_pdf_report(orders, data_parameters)
            report.file.save(f"{report.name}.pdf", ContentFile(pdf_data))
        elif report_format == "xlsx":
            wb = generate_xlsx_report(orders, data_parameters)
            report.file.save(f"{report.name}.xlsx", ContentFile(wb))

        report.status = "finished"
        report.save()
        sentry_sdk.capture_message("Task executed successfully", level="info")

        return "Generating report completed."

    except Exception as e:
        sentry_sdk.capture_exception(e)
        return "An error occurred during report generation."
