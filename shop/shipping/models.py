from django.db import models



class Shipping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.CharField(max_length=20)
    free_delivery = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.name}\nprice: {self.price}\nDelivery time: {self.delivery_time}\nFree delivery: {self.free_delivery}"