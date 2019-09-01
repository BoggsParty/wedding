# Generated by Django 2.1.5 on 2019-03-02 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(blank=True, default='', max_length=100)),
                ('address', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=100)),
                ('party_invite', models.BooleanField(default=False)),
                ('rsvp_dinner_main', models.BooleanField(default=True)),
                ('rsvp_dinner_second', models.BooleanField(default=True)),
                ('rsvp_party_main', models.BooleanField(default=False)),
                ('rsvp_party_second', models.BooleanField(default=False)),
                ('food_option', models.CharField(choices=[('1', 'Actual option 1'), ('2', 'Actual option 2')], default='1', max_length=1)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
