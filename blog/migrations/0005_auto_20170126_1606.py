# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170126_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
