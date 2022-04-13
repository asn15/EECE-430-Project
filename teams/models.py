from django.db import models


# Create your models here.
from django.db.models import DO_NOTHING


class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    details = models.TextField()

    # Display Team name instead of Object when calling a Team instance from database
    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=256)
    number = models.IntegerField()
    age = models.IntegerField()
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
    first_team_score = models.IntegerField(default=0)
    second_team_score = models.IntegerField(default=0)
    game_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} - {} {}'.format(self.first_team_relation.name, self.first_team_relation.name, self.second_team_score, self.second_team)
