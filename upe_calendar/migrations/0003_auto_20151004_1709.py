# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upe_calendar', '0002_auto_20150328_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='event',
            name='banner',
            field=models.CharField(max_length=4096),
        ),
    ]
