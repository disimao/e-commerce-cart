import uuid
import datetime

from django.db import models
from django.contrib.auth.models import User

from apps.product.models import Product


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cart"
    )
    date = models.DateField(auto_now=True)
    checked_out = models.BooleanField(default=False)
    shipping_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class CartItem(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cartitems",
    )
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
