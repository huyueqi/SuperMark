# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-26 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0004_auto_20180926_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='sort',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]