# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-12 19:30
from __future__ import unicode_literals

from django.db import migrations
from usaspending_api.references.models import RefCityCountyCode


def canonicalize_RefCityCountyCode(apps, schema_editor):
    """Update existing city and county names to canonicalized form."""
    RefCityCountyCode.canonicalize()


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0065_merge_20170410_2025'),
    ]

    operations = [
        migrations.RunPython(canonicalize_RefCityCountyCode, migrations.RunPython.noop),
    ]
