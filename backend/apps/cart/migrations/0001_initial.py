# Generated by Django 4.1.6 on 2023-02-12 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("date", models.DateField(auto_now=True)),
                ("checked_out", models.BooleanField(default=False)),
                (
                    "shipping_total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "subtotal",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.cart",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cartitems",
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]
