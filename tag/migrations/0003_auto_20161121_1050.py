# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20161121_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='article',
            field=models.ManyToManyField(blank=True, null=True, to='article.Article'),
        ),
    ]