from django.db import models
from users.models import Company
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('electronics', 'Electronics'),
        ('fashion', 'Fashion'),
        ('sport', 'Sport'),
        ('kid', 'Kid'),
        ('automotive', 'Automotive'),
        ('beauty', 'Beauty'),
    )
    seller = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data_added = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    image = models.ImageField(default='no_image.jpg', upload_to='products_pics')
    stock_quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('detail-product', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img_product = Image.open(self.image.path)

        if img_product.height > 400 or img_product.width > 400:
            output_size = (400, 400)
            img_product.thumbnail(output_size)
            img_product.save(self.image.path)

    def __str__(self):
        return self.name
