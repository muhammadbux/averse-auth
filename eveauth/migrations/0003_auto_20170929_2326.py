# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0002_auto_20170929_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mumble_password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
