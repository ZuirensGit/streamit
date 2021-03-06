# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stream_it', '0010_auto_20170603_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stream_it.Channel')),
            ],
            options={
                'ordering': ['-start_time'],
            },
        ),
        migrations.RemoveField(
            model_name='upcoming',
            name='channel',
        ),
        migrations.AddField(
            model_name='controlmeta',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='website_background/'),
        ),
        migrations.AddField(
            model_name='controlmeta',
            name='stream_source',
            field=models.CharField(blank=True, max_length=1023),
        ),
        migrations.AddField(
            model_name='replay',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='replay',
            name='name',
            field=models.CharField(default=1, max_length=31),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UpComing',
        ),
    ]
