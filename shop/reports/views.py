from django.shortcuts import render, redirect
from .models import Report
from .forms import NewReportForm
from .tasks import generate_report_task
from django.contrib import messages


def new_report_view(request):
    if request.method == "POST":
        form = NewReportForm(request.POST)
        user_id = request.user.id
        if form.is_valid():
            data_parameters = form.cleaned_data["data_parameters"]
            report_format = form.cleaned_data["report_format"]
            report_name = form.cleaned_data["report_name"]

            selected_data = []
            for data_param in data_parameters:
                selected_data.append(data_param)

            generate_report_task.delay(
                user_id, report_name, data_parameters, report_format
            )
            messages.success(request, "Generating a report.")
            report = Report(
                name=report_name,
                parameters={
                    "data_parameters": selected_data,
                    "report_format": report_format,
                },
            )
            report.save()
            return redirect("new_report_view")
    else:
        form = NewReportForm()

    return render(request, "new_report.html", {"form": form})