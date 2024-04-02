from django import forms

FORMAT_CHOICES = [
    ("pdf", "PDF"),
    ("xlsx", "XLSX"),
]

PARAMETERS_CHOICES = [
    ("order.id", "Order ID"),
    ("order.buyer", "Order Buyer"),
    ("order.street", "Order Street"),
    ("order.city", "Order City"),
    ("order.postcode", "Order Postcode"),
    ("order.date", "Order Date"),
    ("order.delivery.name", "Order Delivery Name"),
    ("order.delivery.price", "Order Delivery Price"),
    ("order.status", "Order Status"),
]


class NewReportForm(forms.Form):
    data_parameters = forms.MultipleChoiceField(
        label="Parameters",
        choices=PARAMETERS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )
    report_format = forms.ChoiceField(label="Format", choices=FORMAT_CHOICES)
    start_date = forms.DateField(
        label="Start Date",
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    end_date = forms.DateField(
        label="End Date",
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )
    report_name = forms.CharField(label="Report Name", max_length=100)
