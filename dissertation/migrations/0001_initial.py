# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admission', '0002_auto_20160715_1252'),
        ('base', '0005_tutor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type',
                 models.CharField(choices=[('PRF', 'professor'), ('MGR', 'manager')], default='PRF', max_length=3)),
                ('available_by_email', models.BooleanField(default=False)),
                ('available_by_phone', models.BooleanField(default=False)),
                ('available_at_office', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, default='')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Person')),
            ],
        ),
        migrations.CreateModel(
            name='OfferProposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=200)),
                ('student_can_manage_readers', models.BooleanField(default=True)),
                ('readers_visibility_date_for_students', models.BooleanField(default=False)),
                ('adviser_can_suggest_reader', models.BooleanField(default=False)),
                ('evaluation_first_year', models.BooleanField(default=False)),
                ('validation_commission_exists', models.BooleanField(default=False)),
                ('start_visibility_proposition', models.DateField(default=django.utils.timezone.now)),
                ('end_visibility_proposition', models.DateField(default=django.utils.timezone.now)),
                ('start_visibility_dissertation', models.DateField(default=django.utils.timezone.now)),
                ('end_visibility_dissertation', models.DateField(default=django.utils.timezone.now)),
                ('offer_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                 to='admission.OfferYear')),
            ],
        ),
        migrations.CreateModel(
            name='PropositionDissertation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collaboration', models.CharField(
                    choices=[('POSSIBLE', 'possible'), ('REQUIRED', 'required'), ('FORBIDDEN', 'forbidden')],
                    default='FORBIDDEN', max_length=12)),
                ('description', models.TextField(blank=True, null=True)),
                ('level', models.CharField(
                    choices=[('DOMAIN', 'domain'), ('WORK', 'work'), ('QUESTION', 'question'), ('THEME', 'theme')],
                    default='DOMAIN', max_length=12)),
                ('max_number_student', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('RDL', 'literature_review'), ('EDC', 'case_study')], default='RDL',
                                          max_length=12)),
                ('visibility', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Adviser')),
                ('offer_proposition', models.ManyToManyField(to='dissertation.OfferProposition')),
            ],
            options={
                'ordering': ['author__person__last_name', 'author__person__middle_name', 'author__person__first_name',
                             'title'],
            },
        ),
        migrations.CreateModel(
            name='PropositionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status',
                 models.CharField(choices=[('PROMOTEUR', 'promoter'), ('CO_PROMOTEUR', 'copromoter'), ('READER', 'reader')],
                                  default='PROMOTEUR', max_length=12)),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Adviser')),
                ('proposition_dissertation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                               to='dissertation.PropositionDissertation')),
            ],
        ),
        migrations.CreateModel(
            name='Dissertation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('DRAFT', 'draft'), ('DIR_SUBMIT', 'submitted_to_director'),
                                                     ('DIR_OK', 'accepted_by_director'),
                                                     ('DIR_KO', 'refused_by_director'),
                                                     ('COM_SUBMIT', 'submitted_to_commission'),
                                                     ('COM_OK', 'accepted_by_commission'),
                                                     ('COM_KO', 'refused_by_commission'),
                                                     ('EVA_SUBMIT', 'submitted_to_first_year_evaluation'),
                                                     ('EVA_OK', 'accepted_by_first_year_evaluation'),
                                                     ('EVA_KO', 'refused_by_first_year_evaluation'),
                                                     ('TO_RECEIVE', 'to_be_received'), ('TO_DEFEND', 'to_be_defended'),
                                                     ('DEFENDED', 'defended'), ('ENDED', 'ended'),
                                                     ('ENDED_WIN', 'ended_win'), ('ENDED_LOS', 'ended_los')],
                                            default='DRAFT', max_length=12)),
                ('defend_periode', models.CharField(
                    choices=[('UNDEFINED', 'undefined'), ('JANUARY', 'january'), ('JUNE', 'june'),
                             ('SEPTEMBER', 'september')], default='UNDEFINED', max_length=12)),
                ('description', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Student')),
                ('defend_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                                  to='admission.AcademicYear')),
                ('offer_year_start',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.OfferYear')),
                ('proposition_dissertation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                               to='dissertation.PropositionDissertation')),
            ],
        ),
        migrations.CreateModel(
            name='DissertationGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dissertation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Dissertation')),
            ],
        ),
        migrations.CreateModel(
            name='DissertationRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(
                    choices=[('PROMOTEUR', 'promotor'), ('CO_PROMOTEUR', 'copromotor'), ('READER', 'reader')],
                    max_length=12)),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Adviser')),
                ('dissertation',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissertation.Dissertation')),
            ],
        ),
        migrations.AlterField(
            model_name='propositionrole',
            name='status',
            field=models.CharField(
                choices=[('PROMOTEUR', 'promotor'), ('CO_PROMOTEUR', 'copromotor'), ('READER', 'reader')],
                default='PROMOTEUR', max_length=12),
        ),
    ]
