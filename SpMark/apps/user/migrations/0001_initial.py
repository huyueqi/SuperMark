# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dorm', models.CharField(max_length=20)),
                ('tower', models.CharField(max_length=20)),
                ('where', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('num', models.SmallIntegerField(verbose_name=13)),
            ],
        ),
    ]