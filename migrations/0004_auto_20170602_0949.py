# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0003_auto_20170602_0651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upcoming',
            options={'ordering': ['-date']},
        ),
    ]