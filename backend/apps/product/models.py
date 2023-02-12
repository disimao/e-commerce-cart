import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=120)
    price = models.FloatField(default=0)
    score = models.IntegerField(default=0)
    image = models.CharField(max_length=120)
