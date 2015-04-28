# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0007_auto_20150419_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewreservation',
            name='available',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
