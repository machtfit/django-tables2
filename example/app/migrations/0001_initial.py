# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.PositiveIntegerField(verbose_name='poblaci\xf3n')),
                ('tz', models.CharField(max_length=50)),
                ('visits', models.PositiveIntegerField()),
                ('commonwealth', models.NullBooleanField()),
                ('flag', models.FileField(upload_to='country/flags/')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='full name')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
    ]
