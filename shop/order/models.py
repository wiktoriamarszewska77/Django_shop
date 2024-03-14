from django.db import models
from users.models import User
from products.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=5)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order placed {str(self.date)} by {self.buyer.first_name} {self.buyer.last_name}."

    @property
    def address(self):
        return f"{self.street}, {self.city} {self.postcode}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return f' {self.price} * {self.quantity}'

    def __str__(self):
        return f"Order Item - {self.item} ({self.order})"
