# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160131_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirement',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='family',
        ),
        migrations.RemoveField(
            model_name='completion',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='completion',
            name='date_completed',
        ),
        migrations.RemoveField(
            model_name='completion',
            name='requirement',
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='committee',
            field=models.CharField(verbose_name='What committee are you in?', default='NONE', max_length=50, choices=[('NONE', 'No Committee'), ('IND', 'Industrial'), ('OUT', 'Outreach'), ('PRO', 'Professional Development'), ('PUB', 'Publicity'), ('SOC', 'Social'), ('WEB', 'Web Development')]),
            preserve_default=True,
        ),
    ]
