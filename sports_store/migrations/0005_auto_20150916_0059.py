# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports_store', '0004_auto_20150915_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='giftwrap',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='sports_store.Product', blank=True),
        ),
    ]
