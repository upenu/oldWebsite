# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171204_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completion',
            name='date_completed',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
