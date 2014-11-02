# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0005_auto_20141012_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
