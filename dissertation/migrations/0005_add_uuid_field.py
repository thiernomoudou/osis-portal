# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 13:00
from __future__ import unicode_literals
from django.core.exceptions import FieldDoesNotExist
from django.db import migrations, models
import uuid


def set_uuid_field(apps, schema_editor):
    """
    Set a random uuid value to all existing rows in all models containing an 'uuid' attribute in database.
    """
    base = apps.get_app_config('dissertation')
    for model_class in base.get_models():
        ids = model_class.objects.values_list('id', flat=True)
        if ids:
            for pk in ids:
                try:
                    model_class.objects.filter(pk=pk).update(uuid=uuid.uuid4())
                except FieldDoesNotExist:
                    break


class Migration(migrations.Migration):

    dependencies = [
        ('dissertation', '0004_auto_20161006_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='adviser',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertationgroup',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertationlocation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertationrole',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertationupdate',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='offerproposition',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='propositiondissertation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='propositionrole',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='propositiondocumentfile',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='dissertationdocumentfile',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, null=True),
        ),
        migrations.RunPython(set_uuid_field),
        migrations.AlterField(
            model_name='adviser',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertationgroup',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertationlocation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertationrole',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertationupdate',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='offerproposition',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='propositiondissertation',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='propositionrole',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='propositiondocumentfile',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='dissertationdocumentfile',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
