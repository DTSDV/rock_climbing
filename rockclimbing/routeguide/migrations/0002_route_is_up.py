# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routeguide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='is_up',
            field=models.BooleanField(default=True),
        ),
    ]
