# Generated by Django 3.0.5 on 2022-04-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20220425_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingandpurchaseshistory',
            name='timings',
            field=models.CharField(choices=[('1', '1PM - 2PM'), ('2', '2PM - 3PM'), ('3', '3PM - 4PM'), ('4', '4PM - 5PM')], default=None, max_length=256),
        ),
    ]
