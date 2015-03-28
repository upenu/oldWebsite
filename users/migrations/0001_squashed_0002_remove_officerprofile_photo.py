# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('users', '0001_initial'), ('users', '0002_remove_officerprofile_photo')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BerkeleyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('class_name', models.IntegerField(max_length=5, choices=[(10100, 'CS 10'), (10610, 'CS 61A'), (10611, 'CS 61AS'), (10612, 'CS 61B/L'), (10613, 'CS 61C'), (10700, 'CS 70'), (11490, 'CS 149'), (11500, 'CS 150'), (11600, 'CS 160'), (11610, 'CS 161'), (11620, 'CS 162'), (11640, 'CS 164'), (11690, 'CS 169'), (11700, 'CS 170'), (11720, 'CS 172'), (11740, 'CS 174'), (11760, 'CS 176'), (11840, 'CS 184'), (11860, 'CS 186'), (11880, 'CS 188'), (11890, 'CS 189'), (11945, 'CS 194-5'), (11948, 'CS 194-8'), (11950, 'CS 195'), (20200, 'EE 20'), (20400, 'EE 40'), (21050, 'EE 105'), (21170, 'EE 117'), (21180, 'EE 118'), (21200, 'EE 120'), (21210, 'EE 121'), (21220, 'EE 122'), (21230, 'EE 123'), (21250, 'EE 125'), (21260, 'EE 126'), (21270, 'EE 127'), (21280, 'EE 128'), (21300, 'EE 130'), (21340, 'EE 134'), (21370, 'EE 137A'), (21371, 'EE 137B'), (21400, 'EE 140'), (21410, 'EE 141'), (21420, 'EE 142'), (21430, 'EE 143'), (21440, 'EE 144'), (21451, 'EE 145B'), (21470, 'EE 147'), (21490, 'EE 149'), (21500, 'EE 150'), (21920, 'EE 192'), (30010, 'Math 1A'), (30011, 'Math 1B'), (30530, 'Math 53'), (30540, 'Math 54'), (31040, 'Math 104'), (31100, 'Math 110'), (31130, 'Math 113'), (31280, 'Math 128A'), (31850, 'Math 185')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('family', models.CharField(max_length=200)),
                ('committee', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('date_completed', models.DateField(default=datetime.date.today)),
                ('candidate', models.ForeignKey(to='users.CandidateProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficeHour',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('day_of_week', models.IntegerField(max_length=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default=1)),
                ('hour', models.IntegerField(max_length=2, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')], default=11)),
                ('officer_username', models.CharField(max_length=30, help_text='Please enter a valid officer username as this is used for website queries.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficerClass',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('berkeley_class', models.ForeignKey(to='users.BerkeleyClass')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OfficerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('position', models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Technology')], default=1)),
                ('photo', models.ImageField(upload_to='images/officers/')),
                ('classes_taken', models.ManyToManyField(to='users.BerkeleyClass', through='users.OfficerClass')),
                ('office_hours', models.ManyToManyField(blank=True, to='users.OfficeHour')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('req_type', models.CharField(max_length=3, choices=[('SOC', 'Social'), ('PRO', 'Professional'), ('IND', 'Individual'), ('FAM', 'Family'), ('ACM', 'ACM Payment'), ('INI', 'Initiation Attendance'), ('GM', 'General Meetings')], default='SOC')),
                ('candidates', models.ManyToManyField(to='users.CandidateProfile', through='users.Completion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_type', models.IntegerField(verbose_name='You are a(n)', max_length=1, choices=[(1, 'Candidate'), (2, 'Member'), (3, 'Officer'), (4, 'Alumnus')], default=1)),
                ('grad_year', models.CharField(verbose_name='When are you graduating | When did you graduate?', max_length=4, choices=[('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018')], default='15')),
                ('year_joined', models.CharField(verbose_name='When did you join UPE?', max_length=11, choices=[('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014')], default='F14')),
                ('picture', models.ImageField(upload_to='profile_images', default='/profile_images/spock.jpg')),
                ('personal_website', models.CharField(max_length=50, blank=True)),
                ('resume', models.FileField(null=True, upload_to='resumes', blank=True)),
                ('github', models.CharField(max_length=50, blank=True)),
                ('linkedin', models.CharField(max_length=50, blank=True)),
                ('approved', models.BooleanField(default=True)),
                ('candidate_profile', models.ForeignKey(null=True, blank=True, to='users.CandidateProfile')),
                ('officer_profile', models.ForeignKey(null=True, blank=True, to='users.OfficerProfile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='officerclass',
            name='officer',
            field=models.ForeignKey(to='users.OfficerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='completion',
            name='requirement',
            field=models.ForeignKey(to='users.Requirement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='berkeleyclass',
            name='officers',
            field=models.ManyToManyField(to='users.OfficerProfile', through='users.OfficerClass'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='officerprofile',
            name='photo',
        ),
    ]
