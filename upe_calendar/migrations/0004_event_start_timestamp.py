# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upe_calendar', '0003_auto_20151007_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='start_timestamp',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
