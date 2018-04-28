# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180427_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officehour',
            name='day_of_week',
            field=models.CharField(max_length=4, default='Mon', choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thur', 'Thursday'), ('Fri', 'Friday')]),
        ),
    ]
