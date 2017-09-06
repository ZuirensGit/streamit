# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-14 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0026_replay'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stream_it.Channel'),
            preserve_default=False,
        ),
    ]
