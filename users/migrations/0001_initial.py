# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BerkeleyClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('class_name', models.IntegerField(max_length=5, choices=[(10100, 'CS 10'), (10610, 'CS 61A'), (10611, 'CS 61AS'), (10612, 'CS 61B/L'), (10613, 'CS 61C'), (10700, 'CS 70'), (11490, 'CS 149'), (11500, 'CS 150'), (11600, 'CS 160'), (11610, 'CS 161'), (11620, 'CS 162'), (11640, 'CS 164'), (11690, 'CS 169'), (11700, 'CS 170'), (11720, 'CS 172'), (11740, 'CS 174'), (11760, 'CS 176'), (11840, 'CS 184'), (11860, 'CS 186'), (11880, 'CS 188'), (11890, 'CS 189'), (11945, 'CS 194-5'), (11948, 'CS 194-8'), (11950, 'CS 195'), (20200, 'EE 20'), (20400, 'EE 40'), (21050, 'EE 105'), (21170, 'EE 117'), (21180, 'EE 118'), (21200, 'EE 120'), (21210, 'EE 121'), (21220, 'EE 122'), (21230, 'EE 123'), (21250, 'EE 125'), (21260, 'EE 126'), (21270, 'EE 127'), (21280, 'EE 128'), (21300, 'EE 130'), (21340, 'EE 134'), (21370, 'EE 137A'), (21371, 'EE 137B'), (21400, 'EE 140'), (21410, 'EE 141'), (21420, 'EE 142'), (21430, 'EE 143'), (21440, 'EE 144'), (21451, 'EE 145B'), (21470, 'EE 147'), (21490, 'EE 149'), (21500, 'EE 150'), (21920, 'EE 192'), (30010, 'Math 1A'), (30011, 'Math 1B'), (30530, 'Math 53'), (30540, 'Math 54'), (31040, 'Math 104'), (31100, 'Math 110'), (31130, 'Math 113'), (31280, 'Math 128A'), (31850, 'Math 185')])),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('family', models.CharField(max_length=200)),
                ('committee', models.CharField(max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Completion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('candidate', models.ForeignKey(to='users.CandidateProfile')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('day_of_week', models.IntegerField(max_length=1, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default=1)),
                ('hour', models.IntegerField(max_length=2, choices=[(11, '11 AM'), (12, '12 PM'), (13, '1 PM'), (14, '2 PM'), (15, '3 PM'), (16, '4 PM'), (17, '5 PM')], default=11)),
                ('officer_username', models.CharField(max_length=30, help_text='Please enter a valid officer username as this is used for website queries.')),
            ],
        ),
        migrations.CreateModel(
            name='OfficerClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('berkeley_class', models.ForeignKey(to='users.BerkeleyClass')),
            ],
        ),
        migrations.CreateModel(
            name='OfficerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('position', models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Technology')], default=1)),
                ('photo', models.ImageField(upload_to='images/officers/')),
                ('classes_taken', models.ManyToManyField(to='users.BerkeleyClass', through='users.OfficerClass')),
                ('office_hours', models.ManyToManyField(to='users.OfficeHour', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('user_type', models.IntegerField(max_length=1, verbose_name='You are a(n)', choices=[(1, 'Candidate'), (2, 'Member'), (3, 'Officer'), (4, 'Alumnus')], default=1)),
                ('grad_year', models.CharField(max_length=4, verbose_name='When are you graduating | When did you graduate?', choices=[('95', '1995'), ('96', '1996'), ('97', '1997'), ('98', '1998'), ('99', '1999'), ('00', '2000'), ('01', '2001'), ('02', '2002'), ('03', '2003'), ('04', '2004'), ('05', '2005'), ('06', '2006'), ('07', '2007'), ('08', '2008'), ('09', '2009'), ('10', '2010'), ('11', '2011'), ('12', '2012'), ('13', '2013'), ('14', '2014'), ('15', '2015'), ('16', '2016'), ('17', '2017'), ('18', '2018'), ('19', '2019'), ('20', '2020')], default='15')),
                ('year_joined', models.CharField(max_length=11, verbose_name='When did you join UPE?', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017')], default='F14')),
                ('picture', models.ImageField(upload_to='profile_images', default='/profile_images/spock.jpg')),
                ('personal_website', models.CharField(max_length=50, blank=True)),
                ('resume', models.FileField(null=True, upload_to='resumes', blank=True)),
                ('github', models.CharField(max_length=50, blank=True)),
                ('linkedin', models.CharField(max_length=50, blank=True)),
                ('approved', models.BooleanField(default=False)),
                ('candidate_profile', models.ForeignKey(to='users.CandidateProfile', null=True, blank=True)),
                ('officer_profile', models.ForeignKey(to='users.OfficerProfile', null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('committee', models.CharField(max_length=50, verbose_name='What committee are you in?', choices=[('NONE', 'No Committee'), ('IND', 'Industrial'), ('OUT', 'Outreach'), ('PRO', 'Professional Development'), ('PUB', 'Publicity'), ('SOC', 'Social'), ('WEB', 'Web Development')], default='NONE')),
            ],
        ),
        migrations.AddField(
            model_name='officerclass',
            name='officer',
            field=models.ForeignKey(to='users.OfficerProfile'),
        ),
        migrations.AddField(
            model_name='berkeleyclass',
            name='officers',
            field=models.ManyToManyField(to='users.OfficerProfile', through='users.OfficerClass'),
        ),
        migrations.RemoveField(
            model_name='officerprofile',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='officerprofile',
            name='classes_taken',
        ),
        migrations.RemoveField(
            model_name='officerprofile',
            name='office_hours',
        ),
        migrations.AddField(
            model_name='officerprofile',
            name='term',
            field=models.CharField(max_length=5, verbose_name='Officer term', choices=[('F95', 'Fall 1995'), ('F96', 'Fall 1996'), ('F97', 'Fall 1997'), ('F98', 'Fall 1998'), ('F99', 'Fall 1999'), ('F00', 'Fall 2000'), ('F01', 'Fall 2001'), ('F02', 'Fall 2002'), ('F03', 'Fall 2003'), ('F04', 'Fall 2004'), ('F05', 'Fall 2005'), ('F06', 'Fall 2006'), ('F07', 'Fall 2007'), ('F08', 'Fall 2008'), ('F09', 'Fall 2009'), ('F10', 'Fall 2010'), ('F11', 'Fall 2011'), ('F12', 'Fall 2012'), ('F13', 'Fall 2013'), ('F14', 'Fall 2014'), ('F15', 'Fall 2015'), ('F16', 'Fall 2016'), ('F17', 'Fall 2017'), ('S95', 'Spring 1995'), ('S96', 'Spring 1996'), ('S97', 'Spring 1997'), ('S98', 'Spring 1998'), ('S99', 'Spring 1999'), ('S00', 'Spring 2000'), ('S01', 'Spring 2001'), ('S02', 'Spring 2002'), ('S03', 'Spring 2003'), ('S04', 'Spring 2004'), ('S05', 'Spring 2005'), ('S06', 'Spring 2006'), ('S07', 'Spring 2007'), ('S08', 'Spring 2008'), ('S09', 'Spring 2009'), ('S10', 'Spring 2010'), ('S11', 'Spring 2011'), ('S12', 'Spring 2012'), ('S13', 'Spring 2013'), ('S14', 'Spring 2014'), ('S15', 'Spring 2015'), ('S16', 'Spring 2016'), ('S17', 'Spring 2017')], default='S15'),
        ),
        migrations.AlterField(
            model_name='berkeleyclass',
            name='class_name',
            field=models.IntegerField(max_length=5, choices=[(10100, 'CS 10'), (10610, 'CS 61A'), (10611, 'CS 61AS'), (10612, 'CS 61B/L'), (10613, 'CS 61C'), (10700, 'CS 70'), (10981, 'CS 98-1'), (10982, 'CS 98-2'), (10983, 'CS 98-32'), (10984, 'CS 98-47'), (11490, 'CS 149'), (11500, 'CS 150'), (11600, 'CS 160'), (11610, 'CS 161'), (11620, 'CS 162'), (11640, 'CS 164'), (11690, 'CS 169'), (11700, 'CS 170'), (11720, 'CS 172'), (11740, 'CS 174'), (11760, 'CS 176'), (11840, 'CS 184'), (11860, 'CS 186'), (11880, 'CS 188'), (11890, 'CS 189'), (11945, 'CS 194-5'), (11948, 'CS 194-8'), (11950, 'CS 195'), (11981, 'CS 198-1'), (11982, 'CS 198-2'), (11983, 'CS 198-32'), (11984, 'CS 198-47'), (20200, 'EE 20'), (20400, 'EE 40'), (21050, 'EE 105'), (21170, 'EE 117'), (21180, 'EE 118'), (21200, 'EE 120'), (21210, 'EE 121'), (21220, 'EE 122'), (21230, 'EE 123'), (21250, 'EE 125'), (21260, 'EE 126'), (21270, 'EE 127'), (21280, 'EE 128'), (21300, 'EE 130'), (21340, 'EE 134'), (21370, 'EE 137A'), (21371, 'EE 137B'), (21400, 'EE 140'), (21410, 'EE 141'), (21420, 'EE 142'), (21430, 'EE 143'), (21440, 'EE 144'), (21451, 'EE 145B'), (21470, 'EE 147'), (21490, 'EE 149'), (21500, 'EE 150'), (21920, 'EE 192'), (30010, 'Math 1A'), (30011, 'Math 1B'), (30530, 'Math 53'), (30540, 'Math 54'), (31040, 'Math 104'), (31100, 'Math 110'), (31130, 'Math 113'), (31280, 'Math 128A'), (31850, 'Math 185')]),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Web Development'), (10, 'Special Operations')], default=1),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Web Development'), (10, 'Outreach')], default=1),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Outreach'), (10, 'Web Development')], default=1),
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Outreach'), (10, 'Web Development'), (11, 'General Officers')], default=1),
        ),
        migrations.AddField(
            model_name='officerprofile',
            name='bio',
            field=models.TextField(default='Check back soon!'),
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='candidateprofile',
            name='family',
        ),
        migrations.CreateModel(
            name='InterviewSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('availability', models.BooleanField(default=True)),
                ('officer_username', models.CharField(max_length=30, help_text='Please enter a valid officer username as this is used for website queries.')),
                ('student', models.CharField(max_length=50, verbose_name='Student', blank=True)),
                ('student_email', models.EmailField(max_length=255, verbose_name='Student Email', blank=True)),
                ('day_of_week', models.IntegerField(max_length=1, choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
                ('hour', models.IntegerField(max_length=2, choices=[(9, '9am - 10am'), (10, '10am - 11am'), (11, '11am - 12pm'), (12, '12pm - 1pm'), (13, '1pm - 2pm'), (14, '2pm - 3pm'), (15, '3pm - 4pm'), (16, '4pm - 5pm')], default=9)),
                ('date', models.DateField(verbose_name='Date')),
            ],
        ),
        migrations.AlterField(
            model_name='officerprofile',
            name='position',
            field=models.IntegerField(max_length=1, choices=[(1, 'President'), (2, 'Vice President'), (3, 'Secretary'), (4, 'Treasurer'), (5, 'Professional Development'), (6, 'Industrial Relations'), (7, 'Social'), (8, 'Publicity'), (9, 'Outreach'), (10, 'Web Development'), (11, 'Facilities')], default=1),
        ),
    ]
