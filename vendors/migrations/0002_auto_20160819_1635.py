# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='code',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_person',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
