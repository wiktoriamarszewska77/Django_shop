from django.db import models
from users.models import User, Company
from products.models import Product
from datetime import timezone



class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=6)
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self):
        return self.item