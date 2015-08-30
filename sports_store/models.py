from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=127)
    description = models.TextField(max_length=127)
    category = models.TextField(max_length=127)
    price = models.FloatField()
