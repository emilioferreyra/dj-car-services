# Generated by Django 4.2.7 on 2023-11-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='last_reading_mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]