# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0032_auto_20170619_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replay',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stream_it.Performer'),
        ),
    ]