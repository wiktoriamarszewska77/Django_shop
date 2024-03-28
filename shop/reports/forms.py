from django import forms

FORMAT_CHOICES = [
    ("pdf", "PDF"),
    ("xml", "xml"),
]

PARAMETERS_CHOICES = [
    ("oder.id", "Order ID"),
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
    report_name = forms.CharField(label="Report Name", max_length=100)
