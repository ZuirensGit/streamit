# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-06 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0014_controlmeta_on_air'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlmeta',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
