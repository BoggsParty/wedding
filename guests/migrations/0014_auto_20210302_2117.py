# Generated by Django 3.1.5 on 2021-03-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0013_auto_20210302_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='rsvp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='guests',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
