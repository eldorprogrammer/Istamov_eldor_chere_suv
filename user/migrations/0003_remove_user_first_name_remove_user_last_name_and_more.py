# Generated by Django 4.2.3 on 2024-07-01 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_first_name_user_last_name_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]