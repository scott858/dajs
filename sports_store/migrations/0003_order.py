# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_store', '0002_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=127)),
                ('street', models.CharField(max_length=127)),
                ('city', models.CharField(max_length=127)),
                ('state', models.CharField(max_length=127)),
                ('zip', models.CharField(max_length=127)),
                ('country', models.CharField(max_length=127)),
                ('giftwrap', models.BooleanField()),
                ('products', models.ForeignKey(null=True, blank=True, to='sports_store.Product')),
            ],
        ),
    ]
