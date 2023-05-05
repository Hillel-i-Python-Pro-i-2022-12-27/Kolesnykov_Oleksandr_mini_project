from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Категория {self.name} | Описание: {self.description}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # цифры до и после запятой
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products_images")
    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Продукт: {self.name} | Описание: {self.description}"


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Корзина для {self.user.name} | Продукт: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity
