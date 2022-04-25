from django.db import models

import datetime
# Create your models here.
from django.db.models import DO_NOTHING
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^([a-zA-Z]+\s)*[a-zA-Z]+$', 'Only characters are allowed.')



class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    details = models.TextField()

    # Display Team name instead of Object when calling a Team instance from database
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=256, validators=[alphanumeric])
    number = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    position_in_field = models.CharField(max_length=256,
                                         choices=(('1', 'GK'), ('2', 'RB'), ('3', 'RM'), ('4', 'ST')))
    is_captain = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    # Display playerName - clubName instead of Object
    def __str__(self):
        return '{} - {}'.format(self.name, self.team)


class GameScore(models.Model):
    first_team_relation = models.ForeignKey(Team, related_name='first_team', null=True, on_delete=DO_NOTHING)
    second_team_relation = models.ForeignKey(Team, related_name='second_team', null=True, on_delete=DO_NOTHING)
    first_team_score = models.PositiveIntegerField(default=0)
    second_team_score = models.PositiveIntegerField(default=0)
    game_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} - {} {}'.format(self.first_team_relation.name, self.first_team_relation.name, self.second_team_score, self.second_team)

class BookingAndPurchasesHistory(models.Model):
  Fields = models.CharField(max_length=256,
                                       choices=(('1', 'Tigers'), ('2', 'Lions'), ('3', 'Sharks'), ('4', 'Goats')), default = 'Tigers')
  Date = models.DateField(default=datetime.date.today)
  
  Timing = models.CharField(max_length=256,
                                       choices=(('1', '1PM - 2PM'), ('2', '2PM - 3PM'), ('3', '3PM - 4PM'), ('4', '4PM - 5PM')), default=None, 
                                       )

  def __str__(self):
      return '{} - {}'.format(self.time, self.description, self.timing)
  
    
class Consultation(models.Model):
    name_1 = models.CharField(max_length=256, validators=[alphanumeric])
    number = models.PositiveIntegerField()
    date = models.DateField(default=datetime.date.today)
    time = models.CharField(max_length=256,
                                         choices=(('1', '1PM - 2PM'), ('2', '2PM - 3PM'), ('3', '3PM - 4PM'), ('4', '4PM - 5PM')), default=None, 
                                         )
    coach_name = models.CharField(max_length= 256, 
                                  choices=(('1', 'Youssef El Sayed'), ('2', 'Karim Nasreddine'), ('3', 'Jad Jawad'), ('4', 'Yasmina Mehshi'), ('5', 'Salwa Fidawi')), default=None, 
                                  )

    def __str__(self):
        return '{} - {}'.format(self.name_1, self.number)