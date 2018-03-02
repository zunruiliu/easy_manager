# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('project_id', models.CharField(max_length=20, verbose_name='\u9879\u76ee\u7f16\u53f7')),
                ('project_name', models.CharField(max_length=200, verbose_name='\u9879\u76ee\u540d\u79f0')),
            ],
            options={
                'db_table': 'project_project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('project_id',)]),
        ),
        migrations.AlterIndexTogether(
            name='project',
            index_together=set([('created_time',), ('project_name',)]),
        ),
    ]
