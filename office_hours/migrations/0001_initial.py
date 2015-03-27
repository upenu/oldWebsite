# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150327_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficeHour',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('interviewee_email', models.CharField(max_length=30, null=True, blank=True)),
                ('day_of_week', models.IntegerField(max_length=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default=1)),
                ('hour', models.IntegerField(max_length=2, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')], default=11)),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
