# Generated by Django 3.0.5 on 2022-04-27 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0021_auto_20220427_1039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookingAndPurchasesHistory',
            new_name='BookingAndPurchasesHistoryModel',
        ),
    ]