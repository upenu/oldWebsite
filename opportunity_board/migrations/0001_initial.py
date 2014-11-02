# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('company_name', models.CharField(max_length=200)),
                ('job_title', models.CharField(max_length=200)),
                ('job_id', models.CharField(max_length=200)),
                ('job_description', models.TextField()),
                ('post_date', models.DateTimeField(verbose_name='Date Published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
