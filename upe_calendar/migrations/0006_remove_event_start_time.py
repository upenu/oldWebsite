# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upe_calendar', '0005_event_convert_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
    ]
