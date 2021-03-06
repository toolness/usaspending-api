# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-01 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_populate_new_submission_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissionattributes',
            name='previous_submission',
            field=models.OneToOneField(blank=True, help_text='A reference to the most recent submission for this CGAC within the same fiscal year', null=True, on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
        ),
    ]
