# Generated by Django 3.0.5 on 2022-04-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_auto_20220425_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_1', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('time', models.TimeField(max_length=100)),
                ('coach_name', models.CharField(max_length=100)),
            ],
        ),
    ]
