# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-03 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0007_auto_20170603_0231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controlmeta',
            options={'ordering': ['start_time']},
        ),
    ]
