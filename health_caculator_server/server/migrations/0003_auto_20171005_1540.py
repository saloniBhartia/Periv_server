# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_pollutants_serial_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollutants',
            name='serial_num',
            field=models.IntegerField(max_length=100),
        ),
    ]