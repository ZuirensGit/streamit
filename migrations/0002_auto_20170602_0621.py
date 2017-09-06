# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replay',
            name='control_meta',
        ),
        migrations.AddField(
            model_name='replay',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stream_it.Channel'),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='background',
            field=models.ImageField(default=2, upload_to='sponsor_background/'),
            preserve_default=False,
        ),
    ]