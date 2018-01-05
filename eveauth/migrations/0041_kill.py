# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-05 20:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sde', '0019_auto_20171231_0418'),
        ('eveauth', '0040_add_required_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kill',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, default=0, max_digits=16)),
                ('killers', models.ManyToManyField(related_name='kills', to='eveauth.Character')),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losses', to='eveauth.Character')),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losses', to='sde.Type')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kills', to='sde.System')),
            ],
        ),
    ]
