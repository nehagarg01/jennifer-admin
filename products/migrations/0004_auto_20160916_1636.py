# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160819_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default', max_length=255)),
                ('width', models.DecimalField(decimal_places=2, max_digits=12)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=12)),
                ('height', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.AddField(
            model_name='dimension',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='products.Product'),
        ),
    ]