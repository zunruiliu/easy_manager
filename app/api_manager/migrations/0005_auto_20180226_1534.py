# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_manager', '0004_auto_20180226_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='api_name',
            field=models.CharField(max_length=100, verbose_name='\u63a5\u53e3\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='api',
            name='request_method',
            field=models.CharField(default=2, max_length=200, verbose_name='\u8bf7\u6c42\u65b9\u6cd5'),
        ),
    ]