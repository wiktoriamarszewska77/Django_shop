from django import forms
from .models import Order
from django.core.validators import RegexValidator

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100)
    phone = forms.CharField(required=True, validators=[RegexValidator(r'^\d{9}$')])
    email = forms.EmailField(required=True)
    postcode = forms.CharField(required=True, validators=[RegexValidator(r'^\d{2}-\d{3}$')])

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'street', 'city', 'postcode', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        initial_fields = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'city': user.address,
            'phone': user.phone,
            'email': user.email
        }
        super(OrderForm, self).__init__(*args, **kwargs)

        if user:
            for field_name, field_value in initial_fields.items():
                self.fields[field_name].initial = field_value
