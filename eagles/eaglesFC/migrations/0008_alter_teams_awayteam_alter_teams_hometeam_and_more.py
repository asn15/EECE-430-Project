# Generated by Django 4.0.4 on 2022-04-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eaglesFC', '0007_teamformationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='awayTeam',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='homeTeam',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
