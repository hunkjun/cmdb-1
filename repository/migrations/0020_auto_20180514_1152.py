# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-14 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0019_auto_20180509_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connect',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='固定电话'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='datetime',
            field=models.DateField(default='2018-05-14', verbose_name='到期时间'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='create_at',
            field=models.DateField(default='2018-05-14', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='create_at',
            field=models.DateField(default='2018-05-14', verbose_name='创建时间'),
        ),
    ]
