from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.forms.fields import MultipleChoiceField

from users.utils import *

class UserProfile(models.Model):
    USER_TYPES = (
        (1, 'Candidate'),
        (2, 'Member'),
        (3, 'Officer'),
        (4, 'Alumnus'),
    )
    COMMITTEE_CHOICES = (
        ('NONE', 'No Committee'),
        ('IND', 'Industrial'),
        ('OUT', 'Outreach'),
        ('PRO', 'Professional Development'),
        ('PUB', 'Publicity'),
        ('SOC', 'Social'),
        ('WEB', 'Web Development'),
    )
    GRAD_YEARS = ((year[2:], year) for year in YEAR_STRINGS(3))
    YEAR_JOINED = SEMESTERS

    user = models.OneToOneField(User)
    user_type = models.IntegerField(max_length=1, choices=USER_TYPES, default=1, verbose_name='You are a(n)')
    committee = models.CharField(max_length=50, choices = COMMITTEE_CHOICES, default='NONE',verbose_name = 'What committee are you in?')
    grad_year = models.CharField(max_length=4, choices=GRAD_YEARS, default='15', verbose_name='When are you graduating | When did you graduate?')
    year_joined = models.CharField(max_length=11, choices=YEAR_JOINED, default='F14', verbose_name='When did you join UPE?')
    picture = models.ImageField(upload_to='profile_images', default='/profile_images/spock.jpg')
    personal_website = models.CharField(max_length=50, blank=True)
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    approved = models.BooleanField(default=False)
    candidate_profile = models.ForeignKey('CandidateProfile', blank=True, null=True)
    officer_profile = models.ForeignKey('OfficerProfile', blank=True, null=True)
    gives_office_hours = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def is_officer(self):
        return user_type == 3
    def get_committee_display(self):
        for tup in self.COMMITTEE_CHOICES:
            if self.committee == tup[0]:
                return tup[1]

# EVERYTHING BELOW IS FOR LATER.

class CandidateProfile(models.Model):
    user = models.OneToOneField(User)

    def get_progress(self):
        pass


    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class OfficerProfile(models.Model):
    OFFICER_POSITION_CHOICES = tuple((position.index, position.full_name)
            for position in OfficerPosition.positions.values())

    TERM = SEMESTERS

    user = models.OneToOneField(User)
    position_dict = dict(OFFICER_POSITION_CHOICES)
    position = models.IntegerField(max_length=1, choices=OFFICER_POSITION_CHOICES, default=1)
    term = models.CharField(max_length=5, choices=TERM, default='S15', verbose_name='Officer term')
    bio = models.TextField(default='Check back soon!')   
     
    #office_hours = models.ManyToManyField('OfficeHour', blank=True)
    #classes_taken = models.ManyToManyField('BerkeleyClass', through='OfficerClass')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    def name(self):
        return self.user.first_name + " " + self.user.last_name

    def positionname(self):
        return self.position_dict[self.position]

    def schedule(self):
        slots = sorted(self.office_hours.all(), key=lambda x: x.day_of_week * 100 + x.hour)
        str = ""
        if len(slots) > 0:
            str += slots[0].name()
        for i in range(1, len(slots)):
            str += ", " + slots[i].name()
        return str

    def experience(self):
        classes = sorted(self.classes_taken.all(), key=lambda x: x.class_name)
        str = ""
        if len(classes) > 0:
            str += classes[0].name()
        for i in range(1, len(classes)):
            str += ", " + classes[i].name()
        return str

class OfficerClass(models.Model):
    berkeley_class = models.ForeignKey('BerkeleyClass')
    officer = models.ForeignKey('OfficerProfile')

class OfficeHour(models.Model):
    DAY_OF_WEEK_CHOICES = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )
    TIME_OF_DAY_CHOICES = (
        (11, '11 AM'),
        (12, '12 PM'),
        (13, '1 PM'),
        (14, '2 PM'),
        (15, '3 PM'),
        (16, '4 PM'),
        (17, '5 PM'),
    )

    day_dict = dict(DAY_OF_WEEK_CHOICES)
    time_dict = dict(TIME_OF_DAY_CHOICES)

    day_of_week = models.IntegerField(max_length=1, choices=DAY_OF_WEEK_CHOICES, default=1)
    hour = models.IntegerField(max_length=2, choices=TIME_OF_DAY_CHOICES, default=11)
    user = models.ForeignKey('UserProfile', blank=True, null=True)

    def __str__(self):
        return self.user.user.first_name + " " + self.user.user.last_name + " : " + self.name()

    def name(self):
        return self.day_dict[self.day_of_week] + " " + self.time_dict[self.hour]

class BerkeleyClass(models.Model):
    CLASS_CHOICES = (
        (10100, 'CS 10'),
        (10610, 'CS 61A'),
        (10611, 'CS 61AS'),
        (10612, 'CS 61B/L'),
        (10613, 'CS 61C'),
        (10700, 'CS 70'),
        (10981, 'CS 98-1'),
        (10982, 'CS 98-2'),
        (10983, 'CS 98-32'),
        (10984, 'CS 98-47'),
        (11490, 'CS 149'),
        (11500, 'CS 150'),
        (11600, 'CS 160'),
        (11610, 'CS 161'),
        (11620, 'CS 162'),
        (11640, 'CS 164'),
        (11690, 'CS 169'),
        (11700, 'CS 170'),
        (11720, 'CS 172'),
        (11740, 'CS 174'),
        (11760, 'CS 176'),
        (11840, 'CS 184'),
        (11860, 'CS 186'),
        (11880, 'CS 188'),
        (11890, 'CS 189'),
        (11945, 'CS 194-5'),
        (11948, 'CS 194-8'),
        (11950, 'CS 195'),
        (11981, 'CS 198-1'),
        (11982, 'CS 198-2'),
        (11983, 'CS 198-32'),
        (11984, 'CS 198-47'),
        (20200, 'EE 20'),
        (20400, 'EE 40'),
        (21050, 'EE 105'),
        (21170, 'EE 117'),
        (21180, 'EE 118'),
        (21200, 'EE 120'),
        (21210, 'EE 121'),
        (21220, 'EE 122'),
        (21230, 'EE 123'),
        (21250, 'EE 125'),
        (21260, 'EE 126'),
        (21270, 'EE 127'),
        (21280, 'EE 128'),
        (21300, 'EE 130'),
        (21340, 'EE 134'),
        (21370, 'EE 137A'),
        (21371, 'EE 137B'),
        (21400, 'EE 140'),
        (21410, 'EE 141'),
        (21420, 'EE 142'),
        (21430, 'EE 143'),
        (21440, 'EE 144'),
        (21451, 'EE 145B'),
        (21470, 'EE 147'),
        (21490, 'EE 149'),
        (21500, 'EE 150'),
        (21920, 'EE 192'),
        (30010, 'Math 1A'),
        (30011, 'Math 1B'),
        (30530, 'Math 53'),
        (30540, 'Math 54'),
        (31040, 'Math 104'),
        (31100, 'Math 110'),
        (31130, 'Math 113'),
        (31280, 'Math 128A'),
        (31850, 'Math 185'),
    )

    class_dict = dict(CLASS_CHOICES)
    class_name = models.IntegerField(max_length=5, choices=CLASS_CHOICES)
    user = models.ForeignKey('UserProfile', blank=True, null=True)

    def __str__(self):
        return self.user.user.first_name + " " + self.user.user.last_name + " : " + self.name()

    def name(self):
        return self.class_dict[self.class_name]

"""class Requirement(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    candidates = models.ManyToManyField('CandidateProfile', through='Completion')
    REQUIREMENT_TYPE = (
        ('SOC', 'Social'),
        ('PRO', 'Professional'),
        ('IND', 'Individual'),
        ('FAM', 'Family'),
        ('ACM', 'ACM Payment'),
        ('INI', 'Initiation Attendance'),
        ('GM', 'General Meetings')
    )
    req_dict = dict(REQUIREMENT_TYPE)
    req_type = models.CharField(max_length=3, choices=REQUIREMENT_TYPE, default='SOC')

    def __str__(self):
        return self.req_dict[self.req_type] 

class Completion(models.Model):
    candidate = models.ForeignKey('CandidateProfile')
    requirement = models.ForeignKey('Requirement')
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(default=date.today)"""

class Completion(models.Model):
    candidate = models.ForeignKey('CandidateProfile')
