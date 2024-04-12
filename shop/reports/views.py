from django.shortcuts import render, redirect
from .models import Report
from .forms import NewReportForm
from .tasks import generate_report_task
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


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

            selected_data = data_parameters

            messages.success(request, "Generating a report.")
            report = Report.objects.create(
                user_id=user_id,
                name=report_name,
                status="pending",
                parameters={
                    "data_parameters": selected_data,
                    "report_format": report_format,
                    "start_date": start_date.isoformat(),
                    "end_date": end_date.isoformat(),
                },
            )
            generate_report_task.delay(
                user_id, report.id, data_parameters, report_format, start_date, end_date
            )
            return redirect("new_report_view")
    else:
        form = NewReportForm()

    return render(request, "new_report.html", {"form": form})


@login_required()
def reports_view(request):
    reports = Report.objects.filter(user=request.user)
    return render(
        request,
        template_name="reports.html",
        context={"reports": reports},
    )


def download_report_pdf(request, report_id: int):
    report = Report.objects.get(id=report_id)
    file = report.file

    response = HttpResponse(file, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{report.name}.pdf"'
    return response


def download_report_xlsx(request, report_id: int):
    report = Report.objects.get(id=report_id)
    file = report.file

    response = HttpResponse(file, content_type="application/xlsx")
    response["Content-Disposition"] = f'attachment; filename="{report.name}.xlsx"'
    return response
