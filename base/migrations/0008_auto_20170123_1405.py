# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_academiccalendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academiccalendar',
            name='reference',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
