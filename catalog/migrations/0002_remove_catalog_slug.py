# Generated by Django 4.2.7 on 2023-11-11 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='slug',
        ),
    ]
