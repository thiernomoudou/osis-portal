# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_create_init_updt_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=100, null=True)),
                ('changed', models.DateTimeField(null=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]