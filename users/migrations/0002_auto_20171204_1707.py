# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('num_required', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='candidateprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='completion',
            name='date_completed',
            field=models.DateField(default=2, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completion',
            name='note',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='requirement',
            name='candidates',
            field=models.ManyToManyField(to='users.CandidateProfile', through='users.Completion'),
        ),
        migrations.AddField(
            model_name='completion',
            name='requirement',
            field=models.ForeignKey(to='users.Requirement', null=True),
        ),
    ]
