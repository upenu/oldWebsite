import datetime

class OfficerPosition:
    _current_index = 1
    positions = {} # Map from number to object

    def __init__(self, email_name, full_name):
        self.index = OfficerPosition._current_index
        OfficerPosition._current_index += 1
        self.email_name = email_name
        self.full_name = full_name
        self.users = []
        self.positions[self.index] = self

    @property
    def email(self):
        return '{0}@upe.berkeley.edu'.format(self.email_name)

    def __str__(self):
        return self.full_name

OfficerPosition('president', 'President')
OfficerPosition('vp', 'Vice President')
OfficerPosition('secretary', 'Secretary')
OfficerPosition('treasurer', 'Treasurer')
OfficerPosition('profdev', 'Professional Development')
OfficerPosition('ir', 'Industrial Relations')
OfficerPosition('social', 'Social')
OfficerPosition('publicity', 'Publicity')
OfficerPosition('outreach', 'Outreach')
OfficerPosition('webdev', 'Web Development')
OfficerPosition('general', 'General Officers')

current_time = datetime.datetime.now()
CURRENT_YEAR = current_time.year
YEAR_STRINGS = lambda offset: [str(year) for year in range(1995, CURRENT_YEAR + 1 + offset)]
fall_strings = tuple(('F' + year[2:], 'Fall ' + year) for year in YEAR_STRINGS(0))
spring_strings =  tuple(('S' + year[2:], 'Spring ' + year) for year in YEAR_STRINGS(0))
SEMESTERS = fall_strings + spring_strings
CURRENT_SEMESTER = spring_strings[-1] if current_time.month < 6 \
        else fall_strings[-1]



