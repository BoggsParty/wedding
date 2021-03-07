# Generated by Django 3.1.5 on 2021-03-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0015_guest_expected_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='rsvp',
            field=models.BooleanField(choices=[(True, 'Accepts with pleasure'), (False, 'Declines with regret')], default=False),
        ),
    ]