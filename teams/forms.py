from django import forms
from django.forms import ModelForm
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

from teams.models import Team, GameScore, Player


class TeamForm(forms.Form):
    name = forms.CharField(label='Team Name')
    details = forms.CharField(label=' Team Details')


class PlayerForm(forms.Form):
    name = forms.CharField(label='Player Name')
    number = forms.IntegerField(label='Player Number')
    age = forms.IntegerField(label=' Player Age')
    position_in_field = forms.CharField(label='Position in field')
    is_captain = forms.BooleanField(label='Team Captain')
    team = forms.CharField(label='Team Name')


class TeamModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Team
        # fields = ['name', 'details']
        fields = '__all__'
        labels = {
            'name': 'Team Name',
            'details': 'Team Details',
        }

        error_messages = {
            'name': {
                'unique': 'This name already exists, please choose another.',
            }
        }


class PlayerModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayerModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Player

        fields = '__all__'
        labels = {
            'name': 'Player Name ',
            'number': 'Player Number',
            'age': 'Player Age',
            'position_in_field': 'Position on field',
            'is_captain': 'Is he team captain?',
            'team': 'Team Name',
        }

        error_messages = {
            'number': {
                'unique': 'This name already exists, please choose another.',
            }
        }


class ScoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScoreModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        # if kwargs['instance']:
        #     self.helper.add_input(Button('delete', 'Delete', onclick=GameScore.objects.all().delete()))


    class Meta:
        model = GameScore
        exclude = ['game_date']  # get all fields except game_date

        labels = {
            'first_team_relation': 'First Team Name',
            'second_team_relation': 'Second Team Name',
            'first_team_score': 'First Team Score',
            'second_team_score': 'Second Team Score',
        }
