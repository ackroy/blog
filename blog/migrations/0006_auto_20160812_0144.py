# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160811_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]