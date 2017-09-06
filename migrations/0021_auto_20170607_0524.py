# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-07 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0020_auto_20170607_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlmeta',
            name='background',
            field=models.ImageField(blank=True, default='/static/img/Zuirens-bg.jpg', null=True, upload_to='website_background/'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='background',
            field=models.ImageField(blank=True, default='/static/img/pioneer-dj.jpg', null=True, upload_to='sponsor_background/'),
        ),
    ]
