# Generated by Django 4.1 on 2022-08-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.CharField(default='About ME', max_length=250, null=True),
        ),
    ]
