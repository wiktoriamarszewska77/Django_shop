from django import forms
from .models import Order
from shipping.models import Shipping


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    street = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=50, required=True)
    postcode = forms.CharField(max_length=6, required=True)
    phone = forms.CharField(max_length=9, required=True)
    email = forms.EmailField(required=True)
    delivery = forms.ModelChoiceField(
        queryset=Shipping.objects.all(), widget=forms.RadioSelect
    )

    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "street",
            "city",
            "postcode",
            "phone",
            "email",
            "delivery",
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        kwargs.pop("basket", None)
        initial_fields = {
            "first_name": user.first_name if user else "",
            "last_name": user.last_name if user else "",
            "city": user.address if user else "",
            "phone": user.phone if user else "",
            "email": user.email if user else "",
        }
        super(OrderForm, self).__init__(*args, **kwargs)

        if user:
            for field_name, field_value in initial_fields.items():
                self.fields[field_name].initial = field_value
