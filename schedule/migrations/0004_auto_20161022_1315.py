# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20161022_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='clearance_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
