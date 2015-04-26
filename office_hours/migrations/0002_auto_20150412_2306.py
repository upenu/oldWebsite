# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('interviewee_email', models.CharField(null=True, max_length=30, blank=True)),
                ('specific_date', models.DateField()),
                ('generic_time', models.ForeignKey(to='office_hours.OfficeHour')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Misc',
        ),
        migrations.RemoveField(
            model_name='officehour',
            name='description',
        ),
        migrations.RemoveField(
            model_name='officehour',
            name='interviewee_email',
        ),
        migrations.AddField(
            model_name='officehour',
            name='class_name',
            field=models.IntegerField(choices=[(10100, 'CS 10'), (10610, 'CS 61A'), (10611, 'CS 61AS'), (10612, 'CS 61B/L'), (10613, 'CS 61C'), (10700, 'CS 70'), (10981, 'CS 98-1'), (10982, 'CS 98-2'), (10983, 'CS 98-32'), (10984, 'CS 98-47'), (11490, 'CS 149'), (11500, 'CS 150'), (11600, 'CS 160'), (11610, 'CS 161'), (11620, 'CS 162'), (11640, 'CS 164'), (11690, 'CS 169'), (11700, 'CS 170'), (11720, 'CS 172'), (11740, 'CS 174'), (11760, 'CS 176'), (11840, 'CS 184'), (11860, 'CS 186'), (11880, 'CS 188'), (11890, 'CS 189'), (11945, 'CS 194-5'), (11948, 'CS 194-8'), (11950, 'CS 195'), (11981, 'CS 198-1'), (11982, 'CS 198-2'), (11983, 'CS 198-32'), (11984, 'CS 198-47'), (20200, 'EE 20'), (20400, 'EE 40'), (21050, 'EE 105'), (21170, 'EE 117'), (21180, 'EE 118'), (21200, 'EE 120'), (21210, 'EE 121'), (21220, 'EE 122'), (21230, 'EE 123'), (21250, 'EE 125'), (21260, 'EE 126'), (21270, 'EE 127'), (21280, 'EE 128'), (21300, 'EE 130'), (21340, 'EE 134'), (21370, 'EE 137A'), (21371, 'EE 137B'), (21400, 'EE 140'), (21410, 'EE 141'), (21420, 'EE 142'), (21430, 'EE 143'), (21440, 'EE 144'), (21451, 'EE 145B'), (21470, 'EE 147'), (21490, 'EE 149'), (21500, 'EE 150'), (21920, 'EE 192'), (30010, 'Math 1A'), (30011, 'Math 1B'), (30530, 'Math 53'), (30540, 'Math 54'), (31040, 'Math 104'), (31100, 'Math 110'), (31130, 'Math 113'), (31280, 'Math 128A'), (31850, 'Math 185')], max_length=5, default=10100),
            preserve_default=True,
        ),
    ]
