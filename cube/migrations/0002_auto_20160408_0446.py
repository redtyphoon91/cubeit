# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cubeid',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
