# Generated by Django 4.1 on 2022-09-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_rename_profile_profile_pic_profile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='otp',
            field=models.BigIntegerField(),
        ),
    ]