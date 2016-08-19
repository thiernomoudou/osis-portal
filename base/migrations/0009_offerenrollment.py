# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-19 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0006_offeryear_offer'),
        ('base', '0008_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=100, null=True)),
                ('changed', models.DateTimeField(null=True)),
                ('date_enrollment', models.DateField()),
                ('offer_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.OfferYear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Student')),
            ],
        ),
    ]
