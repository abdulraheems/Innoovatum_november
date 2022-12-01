# Generated by Django 4.1 on 2022-08-27 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.TextField()),
                ('content', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
