# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-21 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_auto_20161010_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradetype',
            name='language_exam_required',
            field=models.BooleanField(default=False),
        ),
    ]
