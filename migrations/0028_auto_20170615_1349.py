# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-15 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0027_replay_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='replay',
            name='background',
            field=models.ImageField(default='/static/img/Zuirens-bg.jpg', upload_to='replay_background/'),
        ),
        migrations.AddField(
            model_name='replay',
            name='description',
            field=models.TextField(default='zuirens'),
        ),
    ]
