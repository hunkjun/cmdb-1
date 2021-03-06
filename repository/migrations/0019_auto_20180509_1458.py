# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0018_auto_20180416_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='datetime',
            field=models.DateField(default='2018-05-09', verbose_name='到期时间'),
        ),
        migrations.AlterField(
            model_name='idc',
            name='create_at',
            field=models.DateField(default='2018-05-09', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='server',
            name='deadtime',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12), ('13', 13), ('14', 14), ('15', 15), ('16', 16), ('17', 17), ('18', 18), ('19', 19), ('20', 20), ('21', 21), ('22', 22), ('23', 23), ('24', 24), ('25', 25), ('26', 26), ('27', 27), ('28', 28), ('29', 29), ('30', 30), ('31', 31)], default=0, verbose_name='到期时间'),
        ),
        migrations.AlterField(
            model_name='server',
            name='env_status',
            field=models.CharField(choices=[('test', '测试环境'), ('prod', '生产环境'), ('preprod', '预生产环境'), ('base', '基础环境')], default='测试', max_length=20, verbose_name='所属环境'),
        ),
        migrations.AlterField(
            model_name='team',
            name='create_at',
            field=models.DateField(default='2018-05-09', verbose_name='创建时间'),
        ),
    ]
