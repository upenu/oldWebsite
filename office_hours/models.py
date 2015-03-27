from django.db import models
from users.models import UserProfile

class OfficeHour(models.Model):
    user = models.ForeignKey(UserProfile)
    description = models.TextField(max_length=500, blank=True, null=True)
    is_interview_slot = False
    avaliable = True
    interviewee_email = models.CharField(max_length=30, blank = True, null = True)

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

    def __str__(self):
        return self.day_dict[self.day_of_week] + " " + self.time_dict[self.hour]

    @property
    def officer(self):
        return self.user.__str__()



class Misc(models.Model):
    # officer_username = models.CharField(max_length=30,
    #     help_text='Please enter a valid officer username as this is used for website queries.')

    def __str__(self):
        return self.name() + " " + self.officer_username
