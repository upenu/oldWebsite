# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('interview', '0004_question_pq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pq',
        ),
        migrations.AddField(
            model_name='personalquestion',
            name='user',
            field=models.OneToOneField(blank=True, null=True, to='users.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personalquestion',
            name='quest',
            field=models.ForeignKey(blank=True, null=True, to='interview.Question'),
        ),
    ]
