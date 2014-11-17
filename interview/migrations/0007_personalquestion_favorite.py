# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_auto_20141026_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalquestion',
            name='favorite',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
