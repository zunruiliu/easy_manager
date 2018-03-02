# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-24 06:02
from __future__ import unicode_literals

import app.account.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name_cn', models.CharField(max_length=32, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('email', models.CharField(max_length=100, unique=True, validators=[django.core.validators.EmailValidator('\u8bf7\u8f93\u5165\u6b63\u786e\u7684email', b'invalid')], verbose_name='\u90ae\u7bb1')),
                ('department', models.CharField(blank=True, max_length=64, verbose_name='\u90e8\u95e8')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6700\u65b0\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', app.account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSessionKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('user_id', models.IntegerField(verbose_name='\u7528\u6237ID')),
                ('session_key', models.CharField(max_length=40, verbose_name='session key')),
            ],
            options={
                'db_table': 'account_session_key',
            },
        ),
    ]
