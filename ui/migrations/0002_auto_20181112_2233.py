# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-13 04:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]