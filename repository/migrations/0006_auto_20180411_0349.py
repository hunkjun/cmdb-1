# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_remove_idc_mem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='磁盘名称')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='磁盘大小')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='assets',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset', verbose_name='资产信息'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asset',
            name='cpu_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='CPU型号'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='kernel_version',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='内核版本'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='release',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='系统版本'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='datetime',
            field=models.DateField(default='2018-04-11', verbose_name='到期时间'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='create_at',
            field=models.DateField(default='2018-04-11', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='team',
            name='create_at',
            field=models.DateField(default='2018-04-11', verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='server',
            name='disk_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.Disk_info', verbose_name='硬盘信息'),
            preserve_default=False,
        ),
    ]
