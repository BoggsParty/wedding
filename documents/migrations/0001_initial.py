# Generated by Django 2.1.5 on 2019-08-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=200, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('document', models.FileField(upload_to='filestorage/')),
            ],
        ),
    ]
