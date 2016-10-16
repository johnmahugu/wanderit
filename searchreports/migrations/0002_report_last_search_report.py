# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('searchreports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='last_search_report',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_search_report', to='searchreports.SearchReport'),
        ),
    ]
