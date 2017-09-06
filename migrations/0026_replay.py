# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-14 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0025_auto_20170607_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_source', models.CharField(blank=True, max_length=1023)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_it.Performer')),
            ],
        ),
    ]
