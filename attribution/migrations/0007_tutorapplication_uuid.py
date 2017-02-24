# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-21 09:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('attribution', '0006_auto_20170215_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorapplication',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
