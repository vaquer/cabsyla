# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-11 18:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20161011_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='qrcode',
        ),
    ]
