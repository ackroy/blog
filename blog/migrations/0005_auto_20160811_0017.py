# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_archive'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_time']},
        ),
    ]
