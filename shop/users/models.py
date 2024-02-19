from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)