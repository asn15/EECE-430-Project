# Generated by Django 3.0.5 on 2022-04-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_bookingandpurchaseshistory_made_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingandpurchaseshistory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bookingandpurchaseshistory',
            name='time',
        ),
        migrations.AddField(
            model_name='bookingandpurchaseshistory',
            name='fields',
            field=models.CharField(choices=[('1', 'Tigers'), ('2', 'Lions'), ('3', 'Sharks'), ('4', 'Goats')], default='Tigers', max_length=256),
        ),
    ]
