from django.db import models
from users.models import User
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    comment = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    @staticmethod
    def count_comments_for_product(product_id):
        return Review.objects.filter(product_id=product_id).count()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"Review by {self.user} for {self.product} and rating {self.rating}"
