from django import forms
from .models import Order
from django.core.validators import RegexValidator
from basket.basket import Basket
class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    postcode = forms.CharField(max_length=6)
    phone = forms.CharField(max_length=9)
    email = forms.EmailField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'street', 'city', 'postcode', 'phone', 'email', 'item', 'seller']


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        initial_fields = {
            'first_name': user.first_name if user else '',
            'last_name': user.last_name if user else '',
            'city': user.address if user else '',
            'phone': user.phone if user else '',
            'email': user.email if user else '',
        }
        super(OrderForm, self).__init__(*args, **kwargs)

        if user:
            for field_name, field_value in initial_fields.items():
                self.fields[field_name].initial = field_value
