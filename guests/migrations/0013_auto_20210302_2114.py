# Generated by Django 3.1.5 on 2021-03-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0012_auto_20210127_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('notes', models.TextField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='name',
            new_name='guest_1',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='last_name',
            new_name='guest_2',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='phone',
            new_name='kids',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='party_invite',
            new_name='paper_rsvp',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='additional_guests',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='plab_b_PA_rsvp',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='plab_b_chicago_rsvp',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='plan_b_PA',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='plan_b_chicago',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='rsvp_party',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='unknown_guest',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='unknown_guest_name',
        ),
        migrations.AlterField(
            model_name='guest',
            name='address',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
