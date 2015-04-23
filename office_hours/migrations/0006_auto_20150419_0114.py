# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0005_auto_20150415_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewreservation',
            name='generic_time',
            field=models.ForeignKey(to='office_hours.DateAndTime'),
        ),
    ]
