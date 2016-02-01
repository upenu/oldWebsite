# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150328_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Web Development'), (10, 'Outreach')], default=1),
        ),
    ]
