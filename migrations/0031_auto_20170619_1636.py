# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0030_auto_20170619_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='performer',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='performer',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='replay_source',
        ),
        migrations.RemoveField(
            model_name='performer',
            name='start_time',
        ),
        migrations.AddField(
            model_name='performer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='replay',
            name='control_meta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stream_it.ControlMeta'),
            preserve_default=False,
        ),
    ]