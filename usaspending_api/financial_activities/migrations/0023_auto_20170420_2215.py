# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-20 22:15
from __future__ import unicode_literals

from django.db import migrations
from usaspending_api.financial_activities.models import FinancialAccountsByProgramActivityObjectClass


def populate_final_of_fy(apps, schema_editor):
    FinancialAccountsByProgramActivityObjectClass.populate_final_of_fy()


class Migration(migrations.Migration):

    dependencies = [
        ('financial_activities', '0022_financialaccountsbyprogramactivityobjectclass_final_of_fy'),
    ]

    operations = [
        migrations.RunPython(populate_final_of_fy)
    ]
