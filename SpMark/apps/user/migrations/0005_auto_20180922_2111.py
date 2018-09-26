# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180922_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (3, '保密')], default='0', verbose_name='性别'),
        ),
    ]
