# Generated by Django 3.0.5 on 2022-04-25 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0018_auto_20220425_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='name_1',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^([a-zA-Z]+\\s)*[a-zA-Z]+$', 'Only characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]