# Generated by Django 3.1.5 on 2021-04-29 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0019_guest_rsvp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='expected_guests',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='vaccinated',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='guest',
            name='vaccinated',
            field=models.IntegerField(default=0),
        ),
    ]
