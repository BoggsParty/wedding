# Generated by Django 3.1.5 on 2021-04-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_auto_20210306_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='STD_sent',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='invitation_sent',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='no_std',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='paper_rsvp',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='rsvp_boat',
        ),
        migrations.AddField(
            model_name='guest',
            name='vaccinated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='notes',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
