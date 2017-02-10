# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-12 18:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0039_auto_20170103_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeAgency',
            fields=[
                ('office_agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('aac_code', models.CharField(blank=True, max_length=4, null=True, verbose_name='Office Code')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Office Name')),
            ],
            options={
                'db_table': 'office_agency',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubtierAgency',
            fields=[
                ('subtier_agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('subtier_code', models.CharField(blank=True, max_length=4, null=True, verbose_name='Sub-Tier Agency Code')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Sub-Tier Agency Name')),
            ],
            options={
                'db_table': 'subtier_agency',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ToptierAgency',
            fields=[
                ('toptier_agency_id', models.AutoField(primary_key=True, serialize=False)),
                ('cgac_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='Top-Tier Agency Code')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Top-Tier Agency Name')),
            ],
            options={
                'db_table': 'toptier_agency',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='legalentity',
            unique_together=set([('recipient_name',)]),
        ),
        migrations.AddField(
            model_name='agency',
            name='office_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.OfficeAgency'),
        ),
        migrations.AddField(
            model_name='agency',
            name='subtier_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.SubtierAgency'),
        ),
        migrations.AddField(
            model_name='agency',
            name='toptier_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.ToptierAgency'),
        ),
    ]
