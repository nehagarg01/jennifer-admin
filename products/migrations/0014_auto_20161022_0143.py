# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20161022_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='sku',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
