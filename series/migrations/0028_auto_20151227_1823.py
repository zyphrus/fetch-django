# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 05:23
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0027_auto_20151117_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='media_type_options',
            field=jsonfield.fields.JSONField(blank=True, help_text='A JSON object of options made available from the media type'),
        ),
        migrations.AlterField(
            model_name='series',
            name='release_schedule_options',
            field=jsonfield.fields.JSONField(blank=True, help_text='A JSON object of needed info for each type of release schedule'),
        ),
    ]