# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_personalquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pq',
            field=models.ForeignKey(blank=True, to='interview.PersonalQuestion', null=True),
            preserve_default=True,
        ),
    ]
