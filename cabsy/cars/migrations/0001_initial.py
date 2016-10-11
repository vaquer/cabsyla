# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('modelcar', models.CharField(max_length=300)),
                ('yearcar', models.PositiveIntegerField()),
                ('tags', models.CharField(max_length=15)),
                ('startservicedate', models.DateTimeField()),
                ('qrStringCode', models.CharField(db_index=True, max_length=100)),
                ('qrCode', models.ImageField(upload_to='qrCodes')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]