# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20180411_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='mem',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='内存'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='swap',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='swap'),
        ),
        migrations.AlterField(
            model_name='disk_info',
            name='size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='磁盘大小'),
        ),
    ]
