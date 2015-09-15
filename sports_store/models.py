from django.db import models


class Product(models.Model):
    name = models.TextField(max_length=127)
    description = models.TextField(max_length=127)
    category = models.TextField(max_length=127)
    price = models.FloatField()


class Order(models.Model):
    name = models.CharField(max_length=127)
    street = models.CharField(max_length=127)
    city = models.CharField(max_length=127)
    state = models.CharField(max_length=127)
    zip = models.CharField(max_length=127)
    country = models.CharField(max_length=127)
    giftwrap = models.BooleanField()
    products = models.ManyToManyField(Product, null=True, blank=True)
