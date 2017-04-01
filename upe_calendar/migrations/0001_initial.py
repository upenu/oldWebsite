# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('location', models.CharField(max_length=100)),
                ('banner', models.CharField(max_length=4096)),
                ('facebookid', models.BigIntegerField(default=0)),
                ('start_timestamp', models.BigIntegerField()),
            ],
        ),
    ]
