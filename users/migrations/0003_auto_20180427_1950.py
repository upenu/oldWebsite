# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180427_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='berkeleyclass',
            name='officers',
        ),
        migrations.RemoveField(
            model_name='officerclass',
            name='berkeley_class',
        ),
        migrations.RemoveField(
            model_name='officerclass',
            name='officer',
        ),
        migrations.DeleteModel(
            name='BerkeleyClass',
        ),
        migrations.DeleteModel(
            name='OfficerClass',
        ),
    ]
