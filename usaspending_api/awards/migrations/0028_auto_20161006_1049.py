# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 14:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20160927_1157'),
        ('awards', '0027_auto_20161005_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialaccountsbyawards',
            name='submission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialaccountsbyawardstransactionobligations',
            name='submission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialassistanceaward',
            name='submission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='procurement',
            name='submission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes'),
            preserve_default=False,
        ),
    ]
