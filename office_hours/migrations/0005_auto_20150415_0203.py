# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0004_auto_20150415_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateAndTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('day_of_week', models.IntegerField(max_length=1, default=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')])),
                ('hour', models.IntegerField(max_length=2, default=11, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='officehour',
            name='day_of_week',
        ),
        migrations.RemoveField(
            model_name='officehour',
            name='hour',
        ),
        migrations.AddField(
            model_name='officehour',
            name='date_and_time',
            field=models.ManyToManyField(to='office_hours.DateAndTime'),
            preserve_default=True,
        ),
    ]
