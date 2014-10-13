# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20140928_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalQuestion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('quest', models.ForeignKey(to='interview.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
