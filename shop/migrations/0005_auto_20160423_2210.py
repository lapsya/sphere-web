# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, through='shop.CartItem', to='shop.Item'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, through='shop.ItemOrder', to='shop.Item'),
        ),
    ]
