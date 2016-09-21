# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0010_auto_20160917_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondaryeducationexam',
            name='result',
            field=models.CharField(blank=True, choices=[('LOW', 'Moins de 65%'), ('MIDDLE', 'entre 65% et 75%'), ('HIGH', 'plus de 75%'), ('SUCCEED', 'succeeded'), ('FAILED', 'failed'), ('ENROLLMENT_IN_PROGRESS', 'demanded_result')], max_length=30, null=True),
        ),
    ]