# Generated by Django 2.1.5 on 2019-03-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='rsvp_dinner_main',
            new_name='rsvp_dinner',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='rsvp_party_main',
            new_name='rsvp_party',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='rsvp_party_second',
            new_name='rsvp_welcome_dinner',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='rsvp_dinner_second',
        ),
        migrations.AddField(
            model_name='guest',
            name='welcome_dinner_invite',
            field=models.BooleanField(default=False),
        ),
    ]
