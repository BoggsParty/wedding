# Generated by Django 3.1.5 on 2021-02-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
