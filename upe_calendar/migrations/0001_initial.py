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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True, max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='event_images/thumbnails')),
                ('banner', models.ImageField(upload_to='event_images/banners')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
