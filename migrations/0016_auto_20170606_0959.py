# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0015_controlmeta_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlmeta',
            name='slug',
        ),
        migrations.AddField(
            model_name='channel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
