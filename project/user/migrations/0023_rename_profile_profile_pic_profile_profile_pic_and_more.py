# Generated by Django 4.1 on 2022-08-28 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_rename_profile_followers_profile_followers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_profile_pic',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_user',
            new_name='user',
        ),
    ]
