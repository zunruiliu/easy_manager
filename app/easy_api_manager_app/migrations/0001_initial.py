# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-14 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('api_id', models.CharField(max_length=20, verbose_name='\u63a5\u53e3ID')),
                ('api_name', models.CharField(max_length=100, unique=True, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('api_url', models.URLField(max_length=500, verbose_name='\u63a5\u53e3URL')),
                ('api_path', models.CharField(max_length=500, verbose_name='\u63a5\u53e3\u8def\u5f84')),
                ('request_method', models.CharField(choices=[(1, b'GET\xe6\x96\xb9\xe6\xb3\x95'), (2, b'POST\xe6\x96\xb9\xe6\xb3\x95'), (3, b'PUT\xe6\x96\xb9\xe6\xb3\x95'), (4, b'DELETE\xe6\x96\xb9\xe6\xb3\x95'), (5, b'HEAD\xe6\x96\xb9\xe6\xb3\x95'), (6, b'CONNECT\xe6\x96\xb9\xe6\xb3\x95'), (8, b'TRACE\xe6\x96\xb9\xe6\xb3\x95')], default=2, max_length=10, verbose_name='\u8bf7\u6c42\u65b9\u6cd5')),
                ('request_date', models.TextField(verbose_name='\u8bf7\u6c42\u53c2\u6570')),
                ('response_data', models.TextField(verbose_name='\u54cd\u5e94\u53c2\u6570')),
                ('status', models.SmallIntegerField(choices=[(0, '\u7b49\u5f85'), (1, '\u6267\u884c\u4e2d'), (2, '\u5df2\u6267\u884c')], default=0, verbose_name='\u63a5\u53e3\u72b6\u6001')),
            ],
            options={
                'db_table': 'api_api',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('project_id', models.CharField(max_length=20, verbose_name='\u9879\u76ee\u7f16\u53f7')),
                ('project_name', models.CharField(max_length=200, unique=True, verbose_name='\u9879\u76ee\u540d\u79f0')),
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
        migrations.AlterUniqueTogether(
            name='api',
            unique_together=set([('api_id',)]),
        ),
        migrations.AlterIndexTogether(
            name='api',
            index_together=set([('api_name',), ('created_time',)]),
        ),
    ]
