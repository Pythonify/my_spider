# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_data', '0002_comment_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
