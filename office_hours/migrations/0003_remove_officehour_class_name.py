# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0002_auto_20150412_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officehour',
            name='class_name',
        ),
    ]
