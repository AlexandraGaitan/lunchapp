# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_menu_date_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='raiting',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Procesing'), (1, 'Shiping'), (2, 'Ended')], default=0),
        ),
    ]
