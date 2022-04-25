# Generated by Django 3.0.5 on 2022-04-25 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0017_auto_20220425_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='coach_name',
            field=models.CharField(choices=[('1', 'Youssef El Sayed'), ('2', 'Karim Nasreddine'), ('3', 'Jad Jawad'), ('4', 'Yasmina Mehshi'), ('5', 'Salwa Fidawi')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='name_1',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^([a-zA-Z]+\\s)*[a-zA-Z]+$', 'Only characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='number',
            field=models.PositiveIntegerField(max_length=100),
        ),
    ]
