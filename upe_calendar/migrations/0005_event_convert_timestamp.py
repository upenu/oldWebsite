# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import time
import pytz
from datetime import datetime, timedelta

def isDst(event_time):
    tz_pst = pytz.timezone("America/Los_Angeles")
    return event_time.astimezone(tz_pst).dst() != timedelta(0)

def convertToTimestamp(apps, schema_editor):
    tz_pst = pytz.timezone("America/Los_Angeles")
    Event = apps.get_model("upe_calendar", "Event")
    for event in Event.objects.all():
        # convert event time (stored in UTC) to PST
        if isDst(event.start_time):
            event_time = event.start_time + timedelta(hours=7)
        else:
            event_time = event.start_time + timedelta(hours=8)

        event.start_timestamp = int(event_time.timestamp())
        event.save()

class Migration(migrations.Migration):

    dependencies = [
        ('upe_calendar', '0004_event_start_timestamp'),
    ]

    operations = [
        migrations.RunPython(convertToTimestamp),
    ]
