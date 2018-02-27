# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoPortal', '0004_himgiripost_srishtipost_vasundharapost'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('publish', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MunSocPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('publish', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
