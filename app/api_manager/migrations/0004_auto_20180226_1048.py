# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_manager', '0003_remove_api_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='project_name',
            field=models.CharField(max_length=200, null=True, verbose_name='\u9879\u76ee\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u63a5\u53e3\u540d\u79f0'),
        ),
    ]