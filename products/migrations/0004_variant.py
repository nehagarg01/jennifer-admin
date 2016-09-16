# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 16:59
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160916_1636',),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('compare_at_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=14)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=14)),
                ('pieces', models.IntegerField(default=1)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('option1', models.CharField(default='Default Title', max_length=255)),
                ('option2', models.CharField(blank=True, max_length=255)),
                ('option3', models.CharField(blank=True, max_length=255)),
                ('shopify_id', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.Product')),
            ],
        ),
    ]
