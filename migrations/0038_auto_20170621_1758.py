# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0037_auto_20170621_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replay',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='replay_background/'),
        ),
    ]