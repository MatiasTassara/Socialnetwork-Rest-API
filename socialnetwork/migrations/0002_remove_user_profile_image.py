# Generated by Django 2.2.1 on 2019-06-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='profile_image',
        ),
    ]
