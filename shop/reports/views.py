from django.shortcuts import render, redirect
from .models import Report
from .forms import NewReportForm
from .tasks import generate_report_task
from django.contrib import messages
from order.models import Order
from django.http import HttpResponse
from django.conf import settings
import os


def new_report_view(request):
    if request.method == "POST":
        form = NewReportForm(request.POST)
        user_id = request.user.id
        if form.is_valid():
            data_parameters = form.cleaned_data["data_parameters"]
            report_format = form.cleaned_data["report_format"]
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
            report_name = form.cleaned_data["report_name"]

            selected_data = []
            for data_param in data_parameters:
                selected_data.append(data_param)

            generate_report_task.delay(
                user_id,
                report_name,
                data_parameters,
                report_format,
                start_date,
                end_date,
            )
            messages.success(request, "Generating a report.")
            # Report.objects.create(
            #     name=report_name,
            #     status="pending",
            #     parameters={
            #         "data_parameters": selected_data,
            #         "report_format": report_format,
            #         "start_date": start_date.isoformat(),
            #         "end_date": end_date.isoformat(),
            #     },
            # )
            return redirect("new_report_view")
    else:
        form = NewReportForm()

    return render(request, "new_report.html", {"form": form})


def reports_view(request):
    user = Order.objects.filter(buyer=request.user.id)
    reports = Report.objects.all()
    return render(
        request,
        template_name="reports.html",
        context={"user": user, "reports": reports},
    )


def download_report_pdf(request, report_name):
    report_file_path = os.path.join(
        settings.MEDIA_ROOT, "reports", f"{report_name}.pdf"
    )
    if not os.path.exists(report_file_path):
        return HttpResponse("Report Not Found", status=404)

    with open(report_file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{report_name}.pdf"'
        return response


def download_report_xlsx(request, report_name):
    report_file_path = os.path.join(
        settings.MEDIA_ROOT, "reports", f"{report_name}.xlsx"
    )
    if not os.path.exists(report_file_path):
        return HttpResponse("Report Not Found", status=404)

    with open(report_file_path, "rb") as file:
        response = HttpResponse(file.read(), content_type="application/xlsx")
        response["Content-Disposition"] = f'attachment; filename="{report_name}.xlsx"'
        return response
