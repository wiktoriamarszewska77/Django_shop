from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.username


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    nip = models.CharField(max_length=10)

    def __str__(self):
        return self.name
