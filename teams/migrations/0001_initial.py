# Generated by Django 3.0.5 on 2020-04-24 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team', models.CharField(max_length=256)),
                ('second_team', models.CharField(max_length=256)),
                ('first_team_score', models.IntegerField(default=0)),
                ('second_team_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('number', models.IntegerField()),
                ('age', models.PositiveIntegerField()),
                ('position_in_field', models.CharField(choices=[('1', 'GK'), ('2', 'RB'), ('3', 'RM'), ('4', 'ST')], max_length=256)),
                ('is_captain', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teams.Team')),
            ],
        ),
    ]
