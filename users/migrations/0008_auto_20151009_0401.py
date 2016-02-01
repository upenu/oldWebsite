# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151009_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(default=1, max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Outreach'), (10, 'Web Development')]),
        ),
    ]
