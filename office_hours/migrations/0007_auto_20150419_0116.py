# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0006_auto_20150419_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewreservation',
            name='generic_time',
        ),
        migrations.AddField(
            model_name='interviewreservation',
            name='hour',
            field=models.IntegerField(default=11, max_length=2, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')]),
            preserve_default=True,
        ),
    ]
